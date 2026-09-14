from pathlib import Path
import urllib.request,hashlib,json
p=Path(__file__).resolve().parent / "sources"
p.mkdir(exist_ok=True)
u="https://www.aviso.altimetry.fr/fileadmin/documents/data/tools/hdbk_FES2022.pdf"
r=urllib.request.urlopen(u,timeout=60)
b=r.read(15_000_001)
if len(b)>15_000_000 or not b.startswith(b"%PDF"):raise ValueError("unexpected PDF")
(p/"fes2022-handbook.pdf").write_bytes(b)
(p/"fes2022-handbook-provenance.json").write_text(json.dumps({"url":u,"sha256":hashlib.sha256(b).hexdigest(),"bytes":len(b),"accessed":"2026-09-14"},indent=2)+"\n")
print("FES handbook downloaded",len(b),hashlib.sha256(b).hexdigest())
