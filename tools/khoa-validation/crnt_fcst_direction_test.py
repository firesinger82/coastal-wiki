#!/usr/bin/env python3
"""KHOA 조류예보(시계열) API 의 16방위 유향 검증 — 변환표와 '흐르는 방향' 규약.

  (1) 변환표: 같은 기관의 최강창낙조 API(crntFcstFldEbb, 유향 숫자 deg)와 조류예보(시계열)
      API(crntFcstTime, 16방위 문자, min=1)를 같은 지점·같은 최강 시각에서 비교.
  (2) 규약: 규약이 검증된 수치조류도 API(tidalCurrentArea, KST, 흐르는 방향 —
      experience/khoa-tidal-current-phase-reference-2026.md §3c)의 최근접 격자점과 매시 비교.

인증키: 환경변수 DATAGOKR_KEY (data.go.kr, crntFcstTime·crntFcstFldEbb 활용신청),
        KHOA_OCEANDATA_KEY (바다누리). 저장소에 두지 않는다.
실행: python3 crnt_fcst_direction_test.py [--days 20260920-20260929]
"""
import json, os, sys, urllib.parse, urllib.request
import numpy as np

DIR16 = ['북', '북북동', '북동', '동북동', '동', '동남동', '남동', '남남동',
         '남', '남남서', '남서', '서남서', '서', '서북서', '북서', '북북서']
DEG = {n: i * 22.5 for i, n in enumerate(DIR16)}
STATIONS = {'16LTC10': (128.48655, 34.66758), '21LTC01': (129.09069, 35.04375)}
GW = 'https://apis.data.go.kr/1192136'


def gw(service, op, **p):
    """data.go.kr 게이트웨이 — 연속 호출 시 503(속도 제한)이 나므로 재시도·대기."""
    import time, urllib.error
    q = urllib.parse.urlencode(p)
    url = f"{GW}/{service}/{op}?serviceKey={os.environ['DATAGOKR_KEY']}&type=json&{q}"
    for attempt in range(6):
        try:
            return json.load(urllib.request.urlopen(url, timeout=60))['body']
        except urllib.error.HTTPError as e:
            if e.code != 503 or attempt == 5:
                raise
            time.sleep(5 * (attempt + 1))


def gw_all(service, op, **p):
    b = gw(service, op, numOfRows=300, pageNo=1, **p)
    items = b['items']['item']
    for pg in range(2, (b['totalCount'] + 299) // 300 + 1):
        items += gw(service, op, numOfRows=300, pageNo=pg, **p)['items']['item']
    return items


def wrap(d):
    return (d + 180) % 360 - 180


def test_table(days):
    rows = []
    for code in STATIONS:
        fe = {x['predcDt']: x for x in gw_all('crntFcstFldEbb', 'GetCrntFcstFldEbbApiService', obsCode=code)
              if x['crsp'] > 0}
        ts = {}
        for d in days:
            for x in gw_all('crntFcstTime', 'GetCrntFcstTimeApiService', obsCode=code, reqDate=d, min=1):
                ts[x['predcDt']] = x
        for t, m in fe.items():
            if t in ts:
                x = ts[t]
                rows.append((wrap(DEG[x['crdir']] - m['crdir']), x['crsp'] - m['crsp']))
    dd = np.array([r[0] for r in rows]); ds = np.array([r[1] for r in rows])
    print(f'[1] table: {len(rows)} max-current instants, |ddir| max {np.abs(dd).max():.2f} mean {dd.mean():.2f}, '
          f'>11.25: {(np.abs(dd) > 11.25).sum()}, ~180: {(np.abs(np.abs(dd) - 180) < 30).sum()}, '
          f'|dspeed| max {np.abs(ds).max():.3f} cm/s')


def test_convention(day):
    out = []
    for code, (lo, la) in STATIONS.items():
        fc = {x['predcDt'][11:13]: x for x in gw_all('crntFcstTime', 'GetCrntFcstTimeApiService',
                                                     obsCode=code, reqDate=day, min=60)}
        for h in range(24):
            q = urllib.parse.urlencode({'ServiceKey': os.environ['KHOA_OCEANDATA_KEY'], 'Date': day,
                                        'Hour': f'{h:02d}', 'Minute': '00', 'MinX': lo - 0.03, 'MaxX': lo + 0.03,
                                        'MinY': la - 0.03, 'MaxY': la + 0.03, 'ResultType': 'json'})
            data = json.load(urllib.request.urlopen(
                'https://www.khoa.go.kr/oceandata/api/tidalCurrentArea/search.do?' + q, timeout=60))['result'].get('data') or []
            f = fc.get(f'{h:02d}')
            if not data or not f:
                continue
            g = min(data, key=lambda x: (float(x['pre_lon']) - lo) ** 2 + (float(x['pre_lat']) - la) ** 2)
            out.append((wrap(DEG[f['crdir']] - float(g['current_dir'])), min(f['crsp'], float(g['current_speed']))))
    dd = np.array([o[0] for o in out]); strong = np.array([o[1] > 20 for o in out])
    print(f'[2] convention: {len(out)} pairs, strong(>20 cm/s) n={strong.sum()}, median |ddir| {np.median(np.abs(dd[strong])):.1f}, '
          f'within 45: {(np.abs(dd[strong]) < 45).sum()}, near 180 (±45): {(np.abs(np.abs(dd[strong]) - 180) < 45).sum()}')


if __name__ == '__main__':
    rng = sys.argv[sys.argv.index('--days') + 1] if '--days' in sys.argv else '20260920-20260929'
    a, b = rng.split('-')
    days = [str(d) for d in range(int(a), int(b) + 1)]
    test_table(days)
    test_convention(days[-1])
