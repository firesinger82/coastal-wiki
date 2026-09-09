#!/usr/bin/env python3
"""Recover MSI File-table identities and selected members without installation."""

from __future__ import annotations

import ctypes as C
import ctypes.util
import hashlib
import json
from pathlib import Path
import re
import shutil
import struct
import subprocess

import olefile


ROOT = Path(__file__).resolve().parents[7]
OUT = Path(__file__).resolve().parent
SCRATCH = Path("/tmp/xbeach-mpich-identity")
MSI_REL = Path(
    "models/XBeach/raw/source_code/trunk/lib/x64/mpich/"
    "mpich2-1.4.1p1-win-x86-64.msi"
)
MSI = ROOT / MSI_REL
RAW_CXX_REL = Path("models/XBeach/raw/source_code/trunk/lib/x64/mpich/lib/cxx.lib")

# MSI File primary keys requested for the identity audit.  The names are
# validated against the File table before cabinet bytes are labeled.
EXPECTED = {
    "_00D89EB1B52A45B79628A8A91613E9C1": "CXX.LIB|cxx.lib",
    "_1BE96E15F472462586C19E8C77FF7927": "MPICH2~1.DLL|mpich2nemesisp.dll",
    "_7D9F6BC68D3B438D9D6834EF34F3754F": "MPICH2~5.DLL|mpich2mpi.dll",
}

MSI_NAME_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz._"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def decode_stream_name(encoded: str) -> str:
    """Decode Windows Installer's compressed compound-stream names."""
    decoded = []
    for char in encoded:
        value = ord(char)
        if value == 0x4840:
            decoded.append("!")
        elif 0x3800 <= value < 0x4800:
            pair = value - 0x3800
            decoded.extend(
                (MSI_NAME_ALPHABET[pair & 0x3F], MSI_NAME_ALPHABET[pair >> 6])
            )
        elif 0x4800 <= value < 0x4840:
            decoded.append(MSI_NAME_ALPHABET[value - 0x4800])
        else:
            decoded.append(char)
    return "".join(decoded)


def read_streams() -> dict[str, bytes]:
    with olefile.OleFileIO(MSI) as ole:
        return {
            decode_stream_name(path[0]): ole.openstream(path).read()
            for path in ole.listdir()
        }


def read_string_table(streams: dict[str, bytes]) -> list[str]:
    pool = streams["!_StringPool"]
    data = streams["!_StringData"]
    codepage, long_refs = struct.unpack_from("<HH", pool)
    assert codepage == 1252, codepage
    assert long_refs == 0, "long string references are not implemented"
    strings = [""]
    cursor = 0
    for offset in range(4, len(pool), 4):
        length, _references = struct.unpack_from("<HH", pool, offset)
        value = data[cursor : cursor + length]
        cursor += length
        strings.append(value.decode("cp1252"))
    assert cursor == len(data)
    return strings


def read_columns(stream: bytes, strings: list[str]) -> list[dict[str, object]]:
    # _Columns has four two-byte columns: Table, Number, Name, Type.
    assert len(stream) % 8 == 0
    row_count = len(stream) // 8
    rows: list[dict[str, object]] = [{} for _ in range(row_count)]
    cursor = 0
    for key, is_string in (
        ("Table", True),
        ("Number", False),
        ("Name", True),
        ("Type", False),
    ):
        for row in rows:
            raw = struct.unpack_from("<H", stream, cursor)[0]
            cursor += 2
            row[key] = strings[raw] if is_string else raw - 0x8000
    return rows


def read_file_table(
    stream: bytes, strings: list[str], columns: list[dict[str, object]]
) -> list[dict[str, object]]:
    schema = sorted(
        (row for row in columns if row["Table"] == "File"),
        key=lambda row: int(row["Number"]),
    )
    expected_schema = [
        ("File", 0x2D48),
        ("Component_", 0x0D48),
        ("FileName", 0x0FFF),
        ("FileSize", 0x0104),
        ("Version", 0x1D48),
        ("Language", 0x1D14),
        ("Attributes", 0x1502),
        ("Sequence", 0x0502),
    ]
    assert [(row["Name"], row["Type"]) for row in schema] == expected_schema

    widths = [4 if not int(row["Type"]) & 0x400 else 2 for row in schema]
    row_width = sum(widths)
    assert len(stream) % row_width == 0
    row_count = len(stream) // row_width
    rows: list[dict[str, object]] = [{} for _ in range(row_count)]
    cursor = 0
    for column, width in zip(schema, widths):
        name = str(column["Name"])
        is_string = bool(int(column["Type"]) & 0x800)
        for row in rows:
            raw = int.from_bytes(stream[cursor : cursor + width], "little")
            cursor += width
            if is_string:
                value: object = strings[raw] if raw else None
            elif raw == 0:
                value = None
            else:
                value = raw - (0x80000000 if width == 4 else 0x8000)
            row[name] = value
    return rows


def archive_api() -> C.CDLL:
    ctypes_name = ctypes.util.find_library("archive")
    assert ctypes_name, "system libarchive was not found"
    archive = C.CDLL(ctypes_name)
    declarations = [
        ("archive_read_new", C.c_void_p, []),
        ("archive_read_support_format_cab", C.c_int, [C.c_void_p]),
        ("archive_read_support_filter_all", C.c_int, [C.c_void_p]),
        (
            "archive_read_open_memory",
            C.c_int,
            [C.c_void_p, C.c_void_p, C.c_size_t],
        ),
        (
            "archive_read_next_header",
            C.c_int,
            [C.c_void_p, C.POINTER(C.c_void_p)],
        ),
        ("archive_entry_pathname", C.c_char_p, [C.c_void_p]),
        ("archive_entry_size", C.c_int64, [C.c_void_p]),
        (
            "archive_read_data",
            C.c_ssize_t,
            [C.c_void_p, C.c_void_p, C.c_size_t],
        ),
        ("archive_read_free", C.c_int, [C.c_void_p]),
        ("archive_error_string", C.c_char_p, [C.c_void_p]),
    ]
    for name, result_type, argument_types in declarations:
        function = getattr(archive, name)
        function.restype = result_type
        function.argtypes = argument_types
    return archive


def extract(cabinet: bytes, labels: dict[str, str]) -> dict[str, bytes]:
    archive = archive_api()
    buffer = C.create_string_buffer(cabinet)
    reader = archive.archive_read_new()
    archive.archive_read_support_filter_all(reader)
    archive.archive_read_support_format_cab(reader)
    assert archive.archive_read_open_memory(reader, buffer, len(cabinet)) == 0
    entry = C.c_void_p()
    recovered: dict[str, bytes] = {}
    while archive.archive_read_next_header(reader, C.byref(entry)) == 0:
        member = archive.archive_entry_pathname(entry).decode()
        pieces = []
        chunk = C.create_string_buffer(1024 * 1024)
        while True:
            count = archive.archive_read_data(reader, chunk, len(chunk))
            assert count >= 0, archive.archive_error_string(reader)
            if not count:
                break
            if member in labels:
                pieces.append(chunk.raw[:count])
        if member in labels:
            recovered[member] = b"".join(pieces)
    archive.archive_read_free(reader)
    assert recovered.keys() == labels.keys()
    return recovered


def run_objdump(arguments: list[str]) -> str:
    executable = shutil.which("objdump")
    assert executable, "GNU objdump was not found"
    return subprocess.run(
        [executable, *arguments], check=True, text=True, stdout=subprocess.PIPE
    ).stdout


def main() -> None:
    streams = read_streams()
    strings = read_string_table(streams)
    columns = read_columns(streams["!_Columns"], strings)
    rows = read_file_table(streams["!File"], strings, columns)
    by_identifier = {str(row["File"]): row for row in rows}
    for identifier, expected_name in EXPECTED.items():
        assert by_identifier[identifier]["FileName"] == expected_name

    cabinets = [(name, data) for name, data in streams.items() if data[:4] == b"MSCF"]
    assert len(cabinets) == 1
    cabinet_name, cabinet = cabinets[0]

    labels = {
        identifier: str(by_identifier[identifier]["FileName"]).split("|")[-1]
        for identifier in EXPECTED
    }
    recovered = extract(cabinet, labels)
    SCRATCH.mkdir(parents=True, exist_ok=True)
    for identifier, data in recovered.items():
        (SCRATCH / labels[identifier]).write_bytes(data)

    raw_cxx = (ROOT / RAW_CXX_REL).read_bytes()
    assert raw_cxx == recovered["_00D89EB1B52A45B79628A8A91613E9C1"]

    table_lines = [
        "File\tFileName\tFileSize\tSequence\tcabinet_member_sha256",
    ]
    selected = []
    for identifier in EXPECTED:
        row = by_identifier[identifier]
        member_hash = sha256(recovered[identifier])
        table_lines.append(
            f"{identifier}\t{row['FileName']}\t{row['FileSize']}\t"
            f"{row['Sequence']}\t{member_hash}"
        )
        selected.append(
            {
                "File": identifier,
                "FileName_raw": row["FileName"],
                "long_name": labels[identifier],
                "FileSize": row["FileSize"],
                "Sequence": row["Sequence"],
                "cabinet_member_sha256": member_hash,
            }
        )
    (OUT / "msi-file-identity.tsv").write_text("\n".join(table_lines) + "\n")

    mpi_dll = SCRATCH / "mpich2mpi.dll"
    portable = run_objdump(["-p", str(mpi_dll)])
    eat = {
        int(match.group(1)): match.group(2)
        for match in re.finditer(
            r"^\s*\[\s*(\d+)\]\s+\+base\[\s*\d+\]\s+([0-9a-fA-F]+) Export RVA$",
            portable,
            re.MULTILINE,
        )
    }
    names = {
        match.group(2): int(match.group(1))
        for match in re.finditer(
            r"^\s*\[\s*(\d+)\]\s+(MPI_Comm_dup|PMPI_Comm_dup)$",
            portable,
            re.MULTILINE,
        )
    }
    assert names.keys() == {"MPI_Comm_dup", "PMPI_Comm_dup"}
    export_lines = ["ImageBase\t0000000180000000"]
    export_records = []
    for name in ("MPI_Comm_dup", "PMPI_Comm_dup"):
        index = names[name]
        rva = int(eat[index], 16)
        export_lines.append(f"{name}\tEAT-index={index}\tRVA=0x{rva:x}")
        export_records.append({"name": name, "eat_index": index, "rva": f"0x{rva:x}"})
    (OUT / "mpich2mpi-export-map.txt").write_text("\n".join(export_lines) + "\n")

    disassembly_parts = []
    for record in export_records:
        start = 0x180000000 + int(str(record["rva"]), 16)
        disassembly_parts.append(
            run_objdump(
                [
                    "-d",
                    f"--start-address=0x{start:x}",
                    f"--stop-address=0x{start + 0x50:x}",
                    str(mpi_dll),
                ]
            ).rstrip()
        )
    (OUT / "mpich2mpi-comm-dup.disassembly.txt").write_text(
        "\n\n".join(disassembly_parts) + "\n"
    )

    # These literal strings show that the front DLL selects/loads another DLL;
    # they do not establish which choice any XBeach process made at runtime.
    dispatcher_tokens = (
        "MPI_DLL_PATH",
        "MPI_WRAP_DLL_NAME",
        "MPI_DLL_NAME",
        "MPICH2_CHANNEL",
        "mpich2nemesis.dll",
        "mpich2.dll",
        "mpich2%s.dll",
    )
    mpi_dll_bytes = mpi_dll.read_bytes()
    assert all(token.encode() in mpi_dll_bytes for token in dispatcher_tokens)
    (OUT / "mpich2mpi-dispatcher-strings.txt").write_text(
        "\n".join(dispatcher_tokens) + "\n"
    )

    mpi_import = ROOT / "models/XBeach/raw/source_code/trunk/lib/x64/mpich/lib/mpi.lib"
    import_dump = run_objdump(["-x", str(mpi_import)])
    import_lines = sorted(
        {
            line.strip()
            for line in import_dump.splitlines()
            if (
                "__IMPORT_DESCRIPTOR_mpich2mpi" in line
                or "mpich2mpi_NULL_THUNK_DATA" in line
                or re.search(r"(?:__imp_)?P?MPI_Comm_dup$", line)
            )
        }
    )
    (OUT / "mpi-import-target.txt").write_text("\n".join(import_lines) + "\n")

    record = {
        "msi_path": str(MSI_REL),
        "msi_sha256": sha256(MSI.read_bytes()),
        "streams": {
            name: {"size": len(streams[name]), "sha256": sha256(streams[name])}
            for name in ("!_StringPool", "!_StringData", "!_Columns", "!File")
        },
        "cabinet_stream_decoded_name": cabinet_name,
        "cabinet_size": len(cabinet),
        "cabinet_sha256": sha256(cabinet),
        "selected_file_rows": selected,
        "raw_cxx_path": str(RAW_CXX_REL),
        "raw_cxx_sha256": sha256(raw_cxx),
        "raw_cxx_byte_identical_to_msi_member": True,
        "exports": export_records,
        "dispatcher_literal_strings": list(dispatcher_tokens),
        "scratch": str(SCRATCH),
        "method": "OLE stream read, MSI string/File table decode, libarchive cabinet extraction; no installation or execution",
    }
    (OUT / "extraction-record.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
