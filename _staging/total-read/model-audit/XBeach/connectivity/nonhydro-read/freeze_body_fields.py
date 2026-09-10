#!/usr/bin/env python3
"""Freeze cached body fields in the saved nonhydro review derivative only.

Preserve display runs, objects and every other ZIP member, including PAGE fields.
This is not a general Word field evaluator and does not execute field commands.
"""
import argparse
from pathlib import Path
from zipfile import ZipFile
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'


def freeze(source, target):
    source, target = Path(source), Path(target)
    if source.resolve() == target.resolve():
        raise ValueError('A separate review derivative is required')
    with ZipFile(source) as before:
        root = etree.fromstring(before.read('word/document.xml'))
        if root.findall('.//{%s}fldSimple' % W):
            raise ValueError('Simple fields require a separate treatment')
        nodes = root.xpath('//w:instrText | //w:fldChar', namespaces={'w': W})
        for node in nodes:
            node.getparent().remove(node)
        xml = etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
        with ZipFile(target, 'w') as after:
            for member in before.infolist():
                after.writestr(member, xml if member.filename == 'word/document.xml'
                               else before.read(member.filename))
    return len(nodes)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('target', type=Path)
    args = parser.parse_args()
    print(freeze(args.source, args.target))
