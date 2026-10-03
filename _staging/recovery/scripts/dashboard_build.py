# Insert dashboard-data.json into the template -> _staging/recovery/dashboard.html (run from repo root)
import json
d = open('_staging/recovery/dashboard-data.json').read()
json.loads(d)
t = open('_staging/recovery/dashboard.template.html').read()
open('_staging/recovery/dashboard.html', 'w').write(t.replace('__DATA__', d.replace('</', '<\\/')))
