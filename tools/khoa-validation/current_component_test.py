#!/usr/bin/env python3
"""KHOA 수치조류도 조화상수 CSV 의 `진폭`·`지각` 이 어떤 유속 성분인지 판별.

비교 대상은 같은 격자의 KHOA 예측 유속·유향 아카이브(data.go.kr 파일데이터 15130143
"해양수산부_수치조류도", 연도별 CSV — 지점당 하루 1개 표본, 시각 미기재)다.
유향은 진북 기준 시계방향(흐르는 방향)으로 보고 u = spd·sin(dir), v = spd·cos(dir).

  variance : 연도별로 ½ΣA² (S2 제외 13분조 — 하루 1회 표본에서 S2 위상은 고정) 과
             예측 u·v·장축·전체 분산의 비
  recon    : UTide FUV(nodal·천문인수) 로 CSV 분조를 합성, 표본 시각 h 를 0–24h 훑어
             관측 v·u 와 상관 (표본 지점 150개 무작위)

주의: g(135°E) ↔ G 변환은 9h 시간 이동과 같으므로 recon 은 위상 기준을 따로 판별하지 않는다
(위상 기준은 current_phase_reference_test.py).

실행 (utide 필요):
  python3 current_component_test.py variance --harm <조화상수.csv> --pred <수치조류도.zip>
  python3 current_component_test.py recon    --harm <조화상수.csv> --pred <수치조류도.zip> --year 2024
"""
import argparse, datetime as dt, zipfile
import numpy as np
import pandas as pd

CONS13 = ['j1', 'k1', 'k2', 'l2', 'm1', 'm2', 'mu2', 'n2', 'nu2', 'o1', 'oo1', 'p1', 'q1']
RECON = ['Q1', 'O1', 'P1', 'K1', 'J1', 'OO1', 'MU2', 'N2', 'NU2', 'M2', 'L2', 'S2', 'K2']  # UTide 에 M1 없음


def load_harm(path):
    H = pd.read_csv(path, encoding='cp949')
    xy = H['좌표'].str.split(expand=True).astype(float)  # "lon lat"
    H['lo'], H['la'] = xy[0].round(3), xy[1].round(3)
    return H.drop_duplicates(['lo', 'la']).set_index(['lo', 'la'])


def load_pred(zpath, year):
    z = zipfile.ZipFile(zpath)
    info = [x for x in z.infolist() if year in x.filename][0]
    df = pd.read_csv(z.open(info), encoding='utf-8-sig')
    df.columns = ['t', 'bx1', 'bx0', 'by1', 'by0', 'lon', 'lat', 'spd', 'dir']
    th = np.radians(df['dir'])
    df['u'], df['v'] = df.spd * np.sin(th), df.spd * np.cos(th)
    df['lo'], df['la'] = df.lon.round(3), df.lat.round(3)
    return df


def variance(a):
    H = load_harm(a.harm)
    A2 = 0.5 * (H[[c + '_진폭' for c in CONS13]] ** 2).sum(axis=1)
    for yr in ('2021', '2022', '2023', '2024'):
        df = load_pred(a.pred, yr)
        rows = []
        for key, g in df.groupby(['lo', 'la']):
            if len(g) < 300 or key not in A2.index:
                continue
            C = np.cov(g.u, g.v)
            w = np.linalg.eigvalsh(C)
            rows.append((A2[key], C[0, 0], C[1, 1], w[1], w[0] + w[1]))
        R = pd.DataFrame(rows, columns=['a', 'var_u', 'var_v', 'var_major', 'var_total'])
        R = R[(R.a > 1) & (R.var_v > 1)]
        out = [f'{yr}: pts {len(R)}']
        for c in ('var_v', 'var_u', 'var_major', 'var_total'):
            r = R.a / R[c]
            out.append(f'{c} {r.median():.3f} [{r.quantile(.25):.3f},{r.quantile(.75):.3f}]')
        out.append(f'logcorr_v {np.corrcoef(np.log(R.a), np.log(R.var_v))[0, 1]:.3f}')
        print('  '.join(out))


def recon(a):
    from utide import harmonics
    from utide._ut_constants import ut_constants as k
    H = load_harm(a.harm)
    df = load_pred(a.pred, a.year)
    names = list(k.const.name)
    lind = np.array([names.index(c) for c in RECON])
    frq = np.array(k.const.freq)[lind]  # cycles/h
    dates = sorted(df.t.unique())
    d0 = np.array([dt.date.fromisoformat(s).toordinal() for s in dates], float)
    hours = np.arange(0, 24, 0.5)
    fuv = [harmonics.FUV(d0 + h / 24, d0[0], lind, 34.0, np.array([0, 0, 0, 0])) for h in hours]
    pts = df.groupby(['lo', 'la']).size().index.tolist()
    pts = [pts[i] for i in np.random.default_rng(1).choice(len(pts), 150, replace=False)]
    idx = df.set_index(['lo', 'la', 't'])
    res = []
    for p in pts:
        if p not in H.index:
            continue
        g = idx.loc[p].reindex(dates)
        m = g.v.notna().values
        A = np.array([H.loc[p, c.lower() + '_진폭'] for c in RECON])
        G = np.radians(np.array([H.loc[p, c.lower() + '_지각'] for c in RECON]) - 9 * 360 * frq)  # g → G
        row = []
        for F, U, V in fuv:
            pred = (F * A * np.cos(2 * np.pi * (V + U) - G)).sum(axis=1)
            row.append((np.corrcoef(pred[m], g.v.values[m])[0, 1], np.corrcoef(pred[m], g.u.values[m])[0, 1],
                        np.sqrt(np.mean((pred[m] - g.v.values[m]) ** 2))))
        res.append(row)
    arr = np.array(res)
    mv, mu = np.nanmedian(arr[:, :, 0], axis=0), np.nanmedian(arr[:, :, 1], axis=0)
    i = int(np.argmax(mv))
    print(f'{a.year}: points {arr.shape[0]}, best h = {hours[i]:.1f} UTC (g 가정), '
          f'corr_v median {mv[i]:.3f} IQR {np.nanpercentile(arr[:, i, 0], [25, 75]).round(3).tolist()}, '
          f'corr_u median {mu[i]:.3f}, RMSE_v median {np.nanmedian(arr[:, i, 2]):.2f} cm/s')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=['variance', 'recon'])
    ap.add_argument('--harm', required=True)
    ap.add_argument('--pred', required=True)
    ap.add_argument('--year', default='2024')
    a = ap.parse_args()
    variance(a) if a.mode == 'variance' else recon(a)
