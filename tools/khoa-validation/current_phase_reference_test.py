#!/usr/bin/env python3
"""KHOA 수치조류도 조화상수 CSV 의 `지각` 위상 기준(G vs g=135°E) 판별 검정.

근거: G 와 g 의 차이는 분조별로 9*a (a = 각속도 °/h) 로 다르다. 같은 정점에서
조류 위상과 조위 G 위상의 차이 (phi_c - phi_e) 는 물리적으로 분조 대역 간에
비슷해야 하므로, CSV 가 g 기준이면 그 차이가 H=9h 오프셋을 빼야 분조 간 일관된다.

  build : 수치조류도 CSV + 49정점 UTide 결과(JSON) → 정점별 최근접 격자 입력표
  test  : 입력표 → 교차 대역 쌍 검정 + 오프셋 H 스캔 + 부트스트랩

입력:
  --csv      data.go.kr 파일데이터 15145955 "해양수산부 국립해양조사원_수치조류도 기반 조화상수_20250814.csv" (cp949, 813,703행)
  --utide    49정점 UTide 결과 디렉터리 (DT_*.json, utide.<CONST>.g_gmt = UTC 입력 G 위상)
  --rows     입력표 CSV (build 출력 / test 입력)
"""
import argparse, glob, json
import numpy as np
import pandas as pd

ANG = {'M2': 28.984104156, 'S2': 30.0, 'N2': 28.43972952, 'K2': 30.08213728,
       'K1': 15.041068639, 'O1': 13.943035584, 'P1': 14.95893136, 'Q1': 13.39866088}
PAIRS = [('M2', 'K1'), ('M2', 'O1'), ('S2', 'K1'), ('N2', 'O1'), ('K2', 'P1'), ('M2', 'Q1')]
MAX_KM = 5.0


def build(csv, utide_dir, rows_out):
    df = pd.read_csv(csv, encoding='cp949')
    xy = df['좌표'].str.split(expand=True).astype(float)   # "lon lat"
    lon, lat = xy[0].values, xy[1].values
    rows = []
    for f in sorted(glob.glob(f'{utide_dir}/DT_*.json')):
        d = json.load(open(f))
        la, lo = d['lat'], d['lon']
        dist = np.hypot((lon - lo) * 111.32 * np.cos(np.radians(la)), (lat - la) * 110.57)
        i = int(np.argmin(dist))
        r = {'code': d['obs_code'], 'name': d['obs_name'], 'lat': la, 'lon': lo,
             'grid_lon': lon[i], 'grid_lat': lat[i], 'dist_km': round(float(dist[i]), 3)}
        for c in ANG:
            r[c + '_e'] = d['utide'][c]['g_gmt']
            r[c + '_c'] = df[f'{c.lower()}_지각'].values[i]
            r[c + '_ca'] = df[f'{c.lower()}_진폭'].values[i]
        rows.append(r)
    pd.DataFrame(rows).to_csv(rows_out, index=False)
    print(f'wrote {rows_out} ({len(rows)} stations)')


def circ_mean_mod180(a):
    """180° 모호성(장축 부호) 처리: 각도를 2배로 원형 평균."""
    m = np.exp(1j * np.radians(2 * np.asarray(a))).mean()
    return (np.degrees(np.angle(m)) / 2) % 180, abs(m)


def station_R(R, H):
    out = []
    for _, r in R.iterrows():
        res = np.array([r[c + '_c'] - H * ANG[c] - r[c + '_e'] for c in ANG])
        out.append(abs(np.exp(1j * np.radians(2 * res)).mean()))
    return np.array(out)


def test(rows_in):
    R = pd.read_csv(rows_in)
    print(f'stations {len(R)}, dist_km median {R.dist_km.median():.2f}, >{MAX_KM:g} km: {(R.dist_km > MAX_KM).sum()}')
    R = R[R.dist_km <= MAX_KM]
    print(f'used {len(R)}')
    print('\n[1] cross-band pairs: mean of (dphi_a - dphi_b) mod 180')
    for a, b in PAIRS:
        D = ((R[a + '_c'] - R[a + '_e']) - (R[b + '_c'] - R[b + '_e'])) % 360
        shift = 9 * (ANG[a] - ANG[b]) % 180
        m, rl = circ_mean_mod180(D.values)
        rg = min(m, 180 - m)
        rk = min(abs(m - shift), 180 - abs(m - shift))
        print(f'  {a}-{b}: mean {m:6.1f} R {rl:.2f} | G expects 0 (resid {rg:5.1f}) | g expects {shift:6.1f} (resid {rk:5.1f})')
    print('\n[2] offset scan H (h): mean per-station consistency R across 8 constituents')
    Hs = np.arange(0, 24.01, 0.25)
    sc = [station_R(R, h).mean() for h in Hs]
    i = int(np.argmax(sc))
    print(f'  best H = {Hs[i]:.2f} h, meanR = {sc[i]:.3f}')
    for h in (0, 3, 6, 8, 9, 10, 12):
        print(f'  H={h:5.2f}  meanR={station_R(R, h).mean():.3f}')
    print('\n[3] R(9h) - R(0h) per station, bootstrap')
    d = station_R(R, 9) - station_R(R, 0)
    bs = np.random.default_rng(0).choice(d, (10000, len(d))).mean(axis=1)
    lo, hi = np.percentile(bs, [2.5, 97.5])
    print(f'  9h > 0h at {(d > 0).sum()}/{len(d)} stations; mean diff {d.mean():.3f}; 95% CI [{lo:.3f}, {hi:.3f}]')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=['build', 'test'])
    ap.add_argument('--csv')
    ap.add_argument('--utide')
    ap.add_argument('--rows', default='results/current_phase_reference_rows.csv')
    a = ap.parse_args()
    if a.mode == 'build':
        build(a.csv, a.utide, a.rows)
    else:
        test(a.rows)
