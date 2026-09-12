import hashlib,json,zipfile,subprocess
from pathlib import Path
from lxml import etree as E
root=Path.cwd();folder=root/'_staging/total-read/model-audit/XBeach/connectivity/manuals-docx-read';out=folder/'conditional-visual-read';out.mkdir(exist_ok=True)
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships','o':'urn:schemas-microsoft-com:office:office','v':'urn:schemas-microsoft-com:vml','w14':'http://schemas.microsoft.com/office/word/2010/wordml'}
def a(p):return {'path':str(p.relative_to(root)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
prior=folder/'native-conditional-probe.json';records=[]
for item in json.loads(prior.read_text())['records']:
 with zipfile.ZipFile(root/item['source']['path']) as z:
  rels={n.get('Id'):'word/'+n.get('Target') for n in E.fromstring(z.read('word/_rels/document.xml.rels'))}
  doc=E.fromstring(z.read('word/document.xml'))
  rid=next(k for k,v in rels.items() if v==item['member'])
  obj=doc.xpath('//o:OLEObject[@r:id="'+rid+'"]',namespaces=ns)[0]
  para=next(x for x in obj.iterancestors() if x.tag=='{'+ns['w']+'}p')
  group=next(x for x in obj.iterancestors() if x.tag=='{'+ns['w']+'}object')
  image=group.xpath('.//v:imagedata/@r:id',namespaces=ns)[0]
  base=('master' if 'master' in item['source']['path'] else 'kingsday')+'-'+Path(item['member']).stem
  p=out/(base+Path(rels[image]).suffix);p.write_bytes(z.read(rels[image]))
  xml=out/(base+'.xml');xml.write_bytes(E.tostring(para))
  records.append({'base':base,'source':item['source'],'member':item['member'],'ole_rid':rid,'preview_member':rels[image],'preview_rid':image,'paragraph_id':para.get('{'+ns['w14']+'}paraId'),'paragraph_text':''.join(para.xpath('.//w:t/text()',namespaces=ns)),'exception':item['prior_error'],'preview':a(p),'paragraph':a(xml)})
subprocess.run(['libreoffice','-env:UserInstallation=file:///tmp/xbeach-conditional-lo','--headless','--convert-to','pdf:draw_pdf_Export','--outdir',str(out)]+[str(root/r['preview']['path']) for r in records],check=True,stdout=subprocess.DEVNULL)
for r in records:
 pdf=out/(r['base']+'.pdf');png=out/(r['base']+'.png')
 subprocess.run(['pdftoppm','-r','180','-singlefile','-png',str(pdf),str(out/r['base'])],check=True)
 r['pdf']=a(pdf);r['png']=a(png)
(out/'preparation.json').write_text(json.dumps({'date':'2026-09-12','attribution':'AI preview comparison preparation','prior_receipt':a(prior),'records':records,'visually_inspected':False,'whole_model_read_gate':'NOT_PASSED','human_approval_issued':False},ensure_ascii=False,indent=2)+'\n')
print([(r['base'],r['paragraph_text'][-120:]) for r in records])
