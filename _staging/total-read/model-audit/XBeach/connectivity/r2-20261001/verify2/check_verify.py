#!/usr/bin/env python3
"""검증 결과(-o 최종 메시지)의 fenced json 에 배치 id 가 전부·정확히 1회·유효 verdict 로 있는지 확인."""
import json, re, sys
txt, ids = open(sys.argv[1]).read(), open(sys.argv[2]).read().split()
F = "`" * 3
m = re.search(F + r"json\s*\n(.*?)\n" + F, txt, re.S)
if not m: print("no json block"); sys.exit(1)
d = json.loads(m.group(1)); got = [x.get("id") for x in d]
bad = [x for x in d if x.get("verdict") not in ("STANDS", "NARROWED", "REFUTED")]
miss = set(ids) - set(got); extra = set(got) - set(ids); dup = len(got) - len(set(got))
from collections import Counter
print(f"n={len(d)} {dict(Counter(x.get('verdict') for x in d))} missing={len(miss)} extra={len(extra)} dup={dup} badverdict={len(bad)}")
sys.exit(1 if (miss or extra or dup or bad) else 0)
