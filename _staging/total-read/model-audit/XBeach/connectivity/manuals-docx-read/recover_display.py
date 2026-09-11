#!/usr/bin/env python3
"""Recover saved MathType display arguments, then freeze body fields in a copy.

This is a bounded OOXML reader for the two archived XBeach manuals. It does not
evaluate SEQ/REF, follow links, run macros, or infer labels from another edition.
Only word/document.xml changes; all other ZIP members retain their bytes.
"""
import argparse
import hashlib
import io
import json
import re
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import olefile

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS = {'w': W}
TARGET = re.compile(r'^\s*(?:MACROBUTTON MTPlaceRef|GOTOBUTTON ZEqnNum\d+)\s+\\\* MERGEFORMAT\s*(\(?)$')


def inventory(source):
    """Hash package members and embedded OLE streams without interpreting them."""
    members, embeddings = [], []
    with ZipFile(source) as package:
        assert len(package.namelist()) == len(set(package.namelist()))
        for member in package.infolist():
            data = package.read(member)
            members.append({'path': member.filename, 'bytes': len(data),
                            'sha256': hashlib.sha256(data).hexdigest()})
            if member.filename.startswith('word/embeddings/') and not member.is_dir():
                streams = []
                with olefile.OleFileIO(io.BytesIO(data)) as ole:
                    for parts in ole.listdir():
                        payload = ole.openstream(parts).read()
                        streams.append({'path': '/'.join(parts), 'bytes': len(payload),
                                        'sha256': hashlib.sha256(payload).hexdigest()})
                embeddings.append({'path': member.filename, 'streams': streams})
        body = etree.fromstring(package.read('word/document.xml'))
    return {'members': members, 'embeddings': embeddings,
            'body_object_count': len(body.xpath('//w:object', namespaces=NS)),
            'omml_count': len(body.findall('.//{http://schemas.openxmlformats.org/officeDocument/2006/math}oMath')),
            'scope': 'Container and stream identity only; Equation Native payload semantics remain unread.'}


def parse(root):
    fields, stack = [], []
    for ordinal, node in enumerate(root.iter()):
        if node.tag == '{%s}fldChar' % W:
            kind = node.get('{%s}fldCharType' % W)
            if kind == 'begin':
                field = {'start_xml_ordinal': ordinal, 'code': [], 'result': [],
                         'separated': False, 'nodes': []}
                fields.append(field)
                if stack:
                    stack[-1]['result' if stack[-1]['separated'] else 'code'].append(field)
                stack.append(field)
            elif kind == 'separate':
                assert stack and not stack[-1]['separated'], 'Unbalanced separator'
                stack[-1]['separated'] = True
            elif kind == 'end':
                assert stack, 'Unbalanced end'
                stack.pop()['end_xml_ordinal'] = ordinal
            else:
                raise ValueError('Unknown field control: ' + str(kind))
        elif node.tag in ('{%s}instrText' % W, '{%s}t' % W) and stack:
            stack[-1]['result' if stack[-1]['separated'] else 'code'].append(node.text or '')
            stack[-1]['nodes'].append(node)
    assert not stack, 'Unterminated field'
    return fields


def serial(field):
    return {k: [serial(v) if isinstance(v, dict) else v for v in value]
            if k in ('code', 'result') else value
            for k, value in field.items() if k != 'nodes'}


def cached(field):
    """Read a nested field's saved result; hidden counters contribute no text."""
    if field['separated']:
        assert all(isinstance(v, str) for v in field['result']), 'Nested result needs review'
        return ''.join(field['result'])
    code = ''.join(v for v in field['code'] if isinstance(v, str))
    assert re.fullmatch(r'\s*SEQ MTEqn\s+\\h\s+\\\* MERGEFORMAT\s*', code), code
    return ''


def recover(source, target):
    source, target = Path(source), Path(target)
    assert source.resolve() != target.resolve(), 'A separate derivative is required'
    with ZipFile(source) as before:
        root = etree.fromstring(before.read('word/document.xml'))
        assert not root.xpath('//w:fldSimple', namespaces=NS), 'Simple fields need review'
        original_text = root.xpath('//w:t/text()', namespaces=NS)
        objects = [etree.tostring(n) for n in root.xpath('//w:object', namespaces=NS)]
        fields = parse(root)
        records = []
        inserted = []
        for field in fields:
            if not field['code'] or not isinstance(field['code'][0], str):
                continue
            head = field['code'][0]
            if not re.match(r'\s*(MACROBUTTON MTPlaceRef|GOTOBUTTON ZEqnNum)', head):
                continue
            match = TARGET.fullmatch(head)
            assert match, head
            assert not field['separated'], 'Unexpected outer cached result'
            value = match.group(1) + ''.join(cached(v) if isinstance(v, dict) else v for v in field['code'][1:])
            assert not value or re.fullmatch(r'\((?:2|B|C)\.\d+\)', value), value
            record = serial(field)
            record['display'] = value
            records.append(record)
            if not value:
                continue  # No saved label: retain an explicit unresolved record.
            node = field['nodes'][0]
            assert node.tag == '{%s}instrText' % W and node.text == head
            node.tag = '{%s}t' % W
            node.text = value
            inserted.append(node)
        # Removing controls alone would lose all the recovered display arguments.
        removed = root.xpath('//w:instrText | //w:fldChar', namespaces=NS)
        for node in removed:
            node.getparent().remove(node)
        assert [n.text for n in root.xpath('//w:t', namespaces=NS) if n not in inserted] == original_text
        assert [etree.tostring(n) for n in root.xpath('//w:object', namespaces=NS)] == objects
        xml = etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
        with ZipFile(target, 'w') as after:
            for member in before.infolist():
                after.writestr(member, xml if member.filename == 'word/document.xml' else before.read(member))
    return {'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
            'body_fields_parsed': len(fields), 'target_fields': len(records),
            'display_arguments_recovered': len(inserted),
            'empty_display_arguments': len(records) - len(inserted),
            'remaining_control_nodes_removed': len(removed), 'fields': records,
            'scope': 'Saved OOXML display arguments only; no field evaluation or equation decoding.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('target', type=Path)
    parser.add_argument('evidence', type=Path)
    args = parser.parse_args()
    evidence = recover(args.source, args.target)
    args.evidence.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in evidence.items() if k != 'fields'}))
