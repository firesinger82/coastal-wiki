#!/usr/bin/env python3
"""KHOA 수치조류도 조화상수 CSV 의 `진폭`·`지각` 이 어떤 유속 성분인지 판별.

비교 대상은 같은 격자의 KHOA 예측 유속·유향 아카이브(data.go.kr 파일데이터 15130143
"해양수산부_수치조류도", 연도별 CSV — 지점당 하루 1개 표본, 시각 미기재)다.
유향은 진북 기준 시계방향(흐르는 방향)으로 보고 u = spd·sin(dir), v = spd·cos(dir).

  variance : 연도별로 ½ΣA² (S2 제외 13분조 — 하루 1회 표본에서 S2 위상은 고정) 과
             예측 u·v·장축·전체 분산의 비
  recon    : UTide FUV(nodal·천문인수) 로 CSV 분조를 합성, 표본 시각 h 를 0–24h 훑어
             관측 v·u 와 상관 (표본 지점 150개 무작위)
  api      : KHOA 바다누리 OpenAPI tidalCurrentArea 스냅샷(시각 지정) 과 CSV 합성 비교 —
             API 시각을 KST/UTC 로 가정해 각각 v·u 상관. 스냅샷은 --snap CSV
             (results/current_api_snapshots_20240421-22.csv, 2024-04-21~22 매시 48회, 126.0–126.3E·36.0–36.3N)
             를 쓰거나 --fetch 로 새로 받는다(인증키: 환경변수 KHOA_OCEANDATA_KEY — 저장소에 두지 않음)

주의: g(135°E) ↔ G 변환은 9h 시간 이동과 같으므로 recon 은 위상 기준을 따로 판별하지 않는다
(위상 기준은 current_phase_reference_test.py).

실행 (utide 필요):
  python3 current_component_test.py variance --harm <조화상수.csv> --pred <수치조류도.zip>
  python3 current_component_test.py recon    --harm <조화상수.csv> --pred <수치조류도.zip> --year 2024
  python3 current_component_test.py api      --harm <조화상수.csv> --snap results/current_api_snapshots_20240421-22.csv
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


def fetch_snap(out, dates=('20240421', '20240422'), box=(126.0, 126.3, 36.0, 36.3)):
    import json, os, urllib.parse, urllib.request
    key = os.environ['KHOA_OCEANDATA_KEY']
    rows = []
    for d in dates:
        for h in range(24):
            q = urllib.parse.urlencode({'ServiceKey': key, 'Date': d, 'Hour': f'{h:02d}', 'Minute': '00',
                                        'MinX': box[0], 'MaxX': box[1], 'MinY': box[2], 'MaxY': box[3],
                                        'ResultType': 'json'})
            r = json.load(urllib.request.urlopen('https://www.khoa.go.kr/oceandata/api/tidalCurrentArea/search.do?' + q, timeout=60))
            t = r['result']['meta']['sch_time']
            rows += [(t, x['pre_lon'], x['pre_lat'], x['current_speed'], x['current_dir']) for x in r['result']['data']]
    pd.DataFrame(rows, columns=['sch_time_api', 'pre_lon', 'pre_lat', 'current_speed_cm_s', 'current_dir_deg']).to_csv(out, index=False)


def api(a):
    from utide import harmonics
    from utide._ut_constants import ut_constants as k
    if a.fetch:
        fetch_snap(a.snap)
    A = pd.read_csv(a.snap)
    A['t'] = pd.to_datetime(A.sch_time_api)
    th = np.radians(A.current_dir_deg)
    A['u'], A['v'] = A.current_speed_cm_s * np.sin(th), A.current_speed_cm_s * np.cos(th)
    H = pd.read_csv(a.harm, encoding='cp949')
    xy = H['좌표'].str.split(expand=True).astype(float)
    hl, ha = xy[0].values, xy[1].values
    names = list(k.const.name)
    lind = np.array([names.index(c) for c in RECON])
    frq = np.array(k.const.freq)[lind]
    times = np.array(sorted(A.t.unique()))
    for label, shift in (('API=KST', 9), ('API=UTC', 0)):
        tu = [pd.Timestamp(x) - pd.Timedelta(hours=shift) for x in times]
        jd = np.array([x.toordinal() + (x.hour * 3600 + x.minute * 60) / 86400 for x in tu])
        F, U, V = harmonics.FUV(jd, jd[0], lind, 36.0, np.array([0, 0, 0, 0]))
        cv, cu, rm = [], [], []
        for (lo, la), g in A.groupby(['pre_lon', 'pre_lat']):
            dd = np.hypot((hl - lo) * 111.32 * np.cos(np.radians(la)), (ha - la) * 110.57)
            i = int(np.argmin(dd))
            if dd[i] > 0.5:
                continue
            Am = np.array([H[c.lower() + '_진폭'].values[i] for c in RECON])
            G = np.radians(np.array([H[c.lower() + '_지각'].values[i] for c in RECON]) - 9 * 360 * frq)
            pred = (F * Am * np.cos(2 * np.pi * (V + U) - G)).sum(axis=1)
            g = g.set_index('t').reindex(times)
            cv.append(np.corrcoef(pred, g.v)[0, 1]); cu.append(np.corrcoef(pred, g.u)[0, 1])
            rm.append(np.sqrt(np.mean((pred - g.v) ** 2)))
        print(f'{label}: pts {len(cv)}, times {len(times)}, corr(pred,v) median {np.median(cv):.3f} '
              f'[min {np.min(cv):.3f}], corr(pred,u) median {np.median(cu):.3f}, RMSE_v median {np.median(rm):.2f} cm/s')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=['variance', 'recon', 'api'])
    ap.add_argument('--harm', required=True)
    ap.add_argument('--pred')
    ap.add_argument('--snap', default='results/current_api_snapshots_20240421-22.csv')
    ap.add_argument('--fetch', action='store_true')
    ap.add_argument('--year', default='2024')
    a = ap.parse_args()
    {'variance': variance, 'recon': recon, 'api': api}[a.mode](a)
