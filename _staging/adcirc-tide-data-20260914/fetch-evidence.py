"""Fetch only the public documents and small NAO input converter used here."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
from urllib.request import urlopen

HERE = Path(__file__).resolve().parent
OUT = Path('/tmp/adcirc-tide-data-sources')
URLS = {
    'nao-readme.html': 'https://www.miz.nao.ac.jp/rise/s/nao99/README_NAOTIDE_En.html',
    'naotidej000909.tar.gz': 'https://www.miz.nao.ac.jp/rise/s/nao99/data/naotidej000909.tar.gz',
    'pyfes-user.html': 'https://cnes.github.io/aviso-fes/user_guide.html',
    'pyfes-nodal.html': 'https://cnes.github.io/aviso-fes/theory/nodal_corrections.html',
    'pyfes-analysis.html': 'https://cnes.github.io/aviso-fes/theory/harmonic_analysis.html',
    'tpxo10.html': 'https://www.tpxo.net/global/tpxo10-atlas',
    'otps.html': 'https://www.tpxo.net/otps',
    'uhslc.html': 'https://uhslc.soest.hawaii.edu/datainfo/',
    'wang2022.html': 'https://os.copernicus.org/articles/18/881/2022/index.html',
}

def fetch(item):
    name, url = item
    with urlopen(url, timeout=45) as response:
        data = response.read(5_000_001)
        if len(data) > 5_000_000:
            raise ValueError('document exceeds 5 MB limit')
        final_url = response.url
    if name.endswith('.tar.gz') and not data.startswith(b'\x1f\x8b'):
        raise ValueError('expected gzip')
    (OUT / name).write_bytes(data)
    return {'file': name, 'url': url, 'final_url': final_url, 'bytes': len(data),
            'sha256': sha256(data).hexdigest(),
            'retrieved_utc': datetime.now(timezone.utc).isoformat()}

if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    with ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(fetch, URLS.items()))
    (HERE / 'sources' / 'web-provenance.json').write_text(
        json.dumps(records, indent=2) + '\n')
    for record in records:
        print(record['file'], record['bytes'], record['sha256'])
