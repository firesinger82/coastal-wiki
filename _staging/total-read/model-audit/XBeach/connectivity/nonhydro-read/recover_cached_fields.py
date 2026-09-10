#!/usr/bin/env python3
"""Source-specific MathType cache recovery; never execute fields or change raw DOC."""
import argparse
import hashlib
import json
import re
import struct
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import olefile
from lxml import etree as E

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
SOURCE = ROOT / 'models/XBeach/raw/source_code/trunk/doc/reports/non-hydrostatic_report_draft.doc'
SOURCE_SHA = '07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec'
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def extract():
    assert sha(SOURCE.read_bytes()) == SOURCE_SHA
    with olefile.OleFileIO(SOURCE) as ole:
        word = ole.openstream('WordDocument').read()
        table = ole.openstream('1Table').read()
    # Fixed-SHA source profile, not a general DOC parser. Confirm the single
    # compressed piece before interpreting byte spans as main-text positions.
    fc, size = struct.unpack_from('<II', word, 418)
    clx = table[fc:fc + size]
    assert size == 21 and clx[0] == 2 and struct.unpack_from('<I', clx, 1)[0] == 16
    cp0, cp1 = struct.unpack_from('<II', clx, 5)
    encoded_fc = struct.unpack_from('<I', clx, 15)[0]
    assert cp0 == 0 and cp1 == 204328 and encoded_fc == 0x40001000
    start = (encoded_fc & 0x3fffffff) // 2
    main_chars = struct.unpack_from('<I', word, 76)[0]
    assert main_chars == 203547
    stop = start + main_chars
    assert stop <= start + cp1 <= len(word)

    def parse(pos):
        begin = pos
        pos += 1
        literal = pos
        parts = []
        while pos < stop:
            char = word[pos]
            if char == 19:
                parts.append(word[literal:pos].decode('cp1252', errors='replace'))
                child, pos = parse(pos)
                parts.append(child)
                literal = pos
                continue
            if char in (20, 21):
                parts.append(word[literal:pos].decode('cp1252', errors='replace'))
                if char == 20:
                    parts.append(None)
                    pos += 1
                    literal = pos
                    continue
                # These wrappers omit an outer separator; their nested SEQ/REF
                # result plus intervening punctuation is the saved display.
                body = parts[parts.index(None) + 1:] if None in parts else parts[1:]
                visible = ''.join(p['cached_display'] if isinstance(p, dict) else p
                                  for p in body if p is not None)
                return {'word_stream_start': begin, 'word_stream_end_exclusive': pos + 1,
                        'cp_start': begin - start, 'command': parts[0],
                        'cached_display': visible,
                        'raw_field_sha256': sha(word[begin:pos + 1])}, pos + 1
            pos += 1
        raise ValueError('Unclosed field at ' + str(begin))

    pattern = rb'\x13 (?:MACROBUTTON MTPlaceRef|GOTOBUTTON ZEqnNum)'
    rows = [parse(m.start())[0] for m in re.compile(pattern).finditer(word, start, stop)]
    for r in rows:
        r['nested_in_target'] = any(q['word_stream_start'] < r['word_stream_start'] <
                                   r['word_stream_end_exclusive'] < q['word_stream_end_exclusive'] for q in rows)
    outer = [r for r in rows if not r['nested_in_target']]
    assert len(rows) == 167 and len(outer) == 166
    assert sum(r['command'].strip().startswith('MACROBUTTON') for r in outer) == 90
    assert sum(bool(r['cached_display']) for r in outer) == 165
    return {'source_path': str(SOURCE.relative_to(ROOT)), 'source_sha256': SOURCE_SHA,
            'word_stream_sha256': sha(word), 'table_stream_sha256': sha(table),
            'piece': {'fcClx': fc, 'lcbClx': size, 'clx_hex': clx.hex(),
                      'text_byte_start': start, 'main_characters': main_chars},
            'scope': 'Saved field-cache values, not recalculated numbering or equation validity. One empty outer field and one empty nested wrapper retained.',
            'specifications': [
                'https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-doc/01d5d8c4-cf9c-4ef9-80fd-439e763cfe01',
                'https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-doc/aa2e55a2-f4f2-4795-bab5-6d9d7a0ed249',
                'https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-doc/9316ddeb-3441-4840-a501-85225ba32b35'],
            'records': rows}


def restore(converted, output, evidence):
    rows = [r for r in evidence['records'] if not r['nested_in_target']]
    with ZipFile(converted) as archive:
        root = E.fromstring(archive.read('word/document.xml'))
        fields = [e for e in root.findall('.//' + W + 'instrText')
                  if re.match(r'\s*(MACROBUTTON MTPlaceRef|GOTOBUTTON ZEqnNum)', e.text or '')]
        assert len(fields) == len(rows)
        for element, row in zip(fields, rows):
            assert (element.text or '').strip() == row['command'].strip()
            run = element.getparent()
            siblings = list(run.getparent())
            idx = siblings.index(run)
            sep = end = None
            for sibling in siblings[idx + 1:]:
                field = sibling.find(W + 'fldChar')
                if field is not None:
                    kind = field.get(W + 'fldCharType')
                    if kind == 'separate':
                        sep = sibling
                    if kind == 'end':
                        end = sibling
                        break
            assert sep is not None and end is not None
            interval = siblings[siblings.index(sep) + 1:siblings.index(end)]
            assert not ''.join(t.text or '' for s in interval for t in s.iter(W + 't'))
            replacement = E.Element(W + 'r')
            E.SubElement(replacement, W + 't').text = row['cached_display']
            end.addprevious(replacement)
            begin = next(s for s in reversed(siblings[:idx]) if s.find(W + 'fldChar') is not None
                         and s.find(W + 'fldChar').get(W + 'fldCharType') == 'begin')
            # Flatten ONLY these empty display fields in the derived review copy;
            # keep bookmarks and equation objects. Field execution is not needed.
            for sibling in siblings[siblings.index(begin):siblings.index(end) + 1]:
                if sibling.tag == W + 'r':
                    sibling.getparent().remove(sibling)
        with ZipFile(output, 'w', ZIP_DEFLATED) as dest:
            for info in archive.infolist():
                data = E.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True) if info.filename == 'word/document.xml' else archive.read(info.filename)
                dest.writestr(info, data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--converted-docx', type=Path)
    parser.add_argument('--output-docx', type=Path)
    parser.add_argument('--receipt', type=Path, default=HERE / 'cached-fields.json')
    args = parser.parse_args()
    evidence = extract()
    args.receipt.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + '\n')
    if args.converted_docx or args.output_docx:
        assert args.converted_docx and args.output_docx
        restore(args.converted_docx, args.output_docx, evidence)
    print('167 source field spans; 166 outer fields; 165 nonempty cached displays')


if __name__ == '__main__':
    main()
