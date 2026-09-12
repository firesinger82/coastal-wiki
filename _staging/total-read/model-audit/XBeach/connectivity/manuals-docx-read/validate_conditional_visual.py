"""Source bindings for the inspected conditional equation previews."""
import hashlib
import json
import zipfile
from lxml import etree as E


def validate(root,folder):
    r=json.loads((folder/'conditional-visual-read/receipt.json').read_text());checks=[]
    ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships','o':'urn:schemas-microsoft-com:office:office','v':'urn:schemas-microsoft-com:vml'}
    def check(n,v):checks.append({'check':'conditional-visual-'+n,'pass':bool(v)})
    def bound(a):return hashlib.sha256((root/a['path']).read_bytes()).hexdigest()==a['sha256']
    prior=json.loads((root/r['prior_receipt']['path']).read_text())
    check('prior-and-contact-hashes',bound(r['prior_receipt']) and all(bound(a) for a in r['contact_sheets']))
    check('exact-20',len(r['records'])==20 and {(x['source']['path'],x['member']) for x in r['records']}=={(x['source']['path'],x['member']) for x in prior['records']})
    for x in r['records']:
        with zipfile.ZipFile(root/x['source']['path']) as z:
            rels={n.get('Id'):'word/'+n.get('Target') for n in E.fromstring(z.read('word/_rels/document.xml.rels'))}
            doc=E.fromstring(z.read('word/document.xml'))
            obj=doc.xpath('//o:OLEObject[@r:id="'+x['ole_rid']+'"]',namespaces=ns)[0]
            para=next(n for n in obj.iterancestors() if n.tag=='{'+ns['w']+'}p')
            check(x['base'],all(bound(x[k]) for k in ('source','preview','paragraph','pdf','png')) and
                  rels[x['ole_rid']]==x['member'] and rels[x['preview_rid']]==x['preview_member'] and
                  x['preview_rid'] in para.xpath('.//v:imagedata/@r:id',namespaces=ns) and
                  E.tostring(para)==(root/x['paragraph']['path']).read_bytes() and
                  z.read(x['preview_member'])==(root/x['preview']['path']).read_bytes() and bool(x['observation']))
    check('qualified-visual-read',r['visually_inspected'] is True and r['whole_model_read_gate']=='NOT_PASSED' and r['human_approval_issued'] is False)
    return checks
