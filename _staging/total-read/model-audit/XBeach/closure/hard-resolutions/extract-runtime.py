"""Read embedded cabinet without installing/executing the supplied Windows MSI."""
from pathlib import Path
import ctypes as C
import ctypes.util
import hashlib
import json
import olefile

ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent
SCRATCH = Path('/tmp/xbeach-closure-hard')
SCRATCH.mkdir(parents=True, exist_ok=True)
MSI = ROOT / 'models/XBeach/raw/source_code/trunk/lib/x64/mpich/mpich2-1.4.1p1-win-x86-64.msi'
TARGET = '_1BE96E15F472462586C19E8C77FF7927'
a = C.CDLL(ctypes.util.find_library('archive'))
for name, restype, argtypes in [
    ('archive_read_new', C.c_void_p, []),
    ('archive_read_support_format_cab', C.c_int, [C.c_void_p]),
    ('archive_read_support_filter_all', C.c_int, [C.c_void_p]),
    ('archive_read_open_memory', C.c_int, [C.c_void_p, C.c_void_p, C.c_size_t]),
    ('archive_read_next_header', C.c_int, [C.c_void_p, C.POINTER(C.c_void_p)]),
    ('archive_entry_pathname', C.c_char_p, [C.c_void_p]),
    ('archive_entry_size', C.c_int64, [C.c_void_p]),
    ('archive_read_data', C.c_ssize_t, [C.c_void_p, C.c_void_p, C.c_size_t]),
    ('archive_read_free', C.c_int, [C.c_void_p]),
    ('archive_error_string', C.c_char_p, [C.c_void_p]),
]:
    fn = getattr(a, name)
    fn.restype, fn.argtypes = restype, argtypes

sha = lambda b: hashlib.sha256(b).hexdigest()
with olefile.OleFileIO(MSI) as ole:
    cabinets = [(name, ole.openstream(name).read()) for name in ole.listdir()
                if ole.openstream(name).read(4) == b'MSCF']
assert len(cabinets) == 1
name, cab = cabinets[0]
buf = C.create_string_buffer(cab)
arc = a.archive_read_new()
a.archive_read_support_filter_all(arc)
a.archive_read_support_format_cab(arc)
assert a.archive_read_open_memory(arc, buf, len(cab)) == 0
entry = C.c_void_p()
found = None
members = []
while a.archive_read_next_header(arc, C.byref(entry)) == 0:
    member = a.archive_entry_pathname(entry).decode()
    size = a.archive_entry_size(entry)
    members.append({'name': member, 'size': size})
    pieces = []
    temp = C.create_string_buffer(1024 * 1024)
    while True:
        n = a.archive_read_data(arc, temp, len(temp))
        assert n >= 0, (member, a.archive_error_string(arc))
        if not n:
            break
        if member == TARGET:
            pieces.append(temp.raw[:n])
    if member == TARGET:
        found = b''.join(pieces)
        assert len(found) == size and found.startswith(b'MZ')
assert found is not None
a.archive_read_free(arc)
(SCRATCH / 'mpich2mpi.extracted.dll').write_bytes(found)
record = {'msi_path': str(MSI.relative_to(ROOT)), 'msi_sha256': sha(MSI.read_bytes()),
          'cabinet_stream': name, 'cabinet_sha256': sha(cab),
          'member': TARGET, 'member_sha256': sha(found), 'member_size': len(found),
          'method': 'olefile stream extraction + libarchive cabinet decompression; no execution',
          'members': members}
(OUT / 'runtime-provenance.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({k:v for k,v in record.items() if k != 'members'}, indent=2))
