#!/usr/bin/env python3
# coastal-wiki 사본(2026-09-28): 원본 ~/khoa_tide/utide_validation/build_validation_targets.py. 입력(KHOA ZIP·정점목록·캐시)은 저장소 밖. 결과 사본 results/typhoon_surge_peaks.json 은 vendor 필드 제거본.
"""Gate-4 검증 타깃 패키지 — 태풍별 관측 최대해일 (전 KHOA 정점, utide 편차).

목적: ADCIRC korea_multiuse backbone Gate 4(태풍 hindcast, RMSE≤30cm) 검증 타깃.
      fort.61 정점 시계열이 나오면 바로 RMSE 계산에 연결할 수 있는 형태.
입력: data/<정점>/<연도>.zip (KHOA 조위), 9_eva_cache.json(정점목록),
      20_model_hindcast.json(타사 벤치마크 — 참고용)
출력: extensions/23_validation_targets.{json,csv,png}
  - obs[태풍][정점] = {max_cm, peak_kst} (피크시각 포함 — 위상 검증용)
  - vendor[태풍][정점] = cm (타사, 10정점 한정, 참고용)
방법: 18번(analyze_gwangyang_check)과 동일 — 연단위 utide OLS 분해 → 편차,
      태풍 기준일 ±2일 윈도우 최대. |편차|≥400cm 스파이크 제거.
"""
from __future__ import annotations
import json, zipfile, warnings, csv
from pathlib import Path
import numpy as np, pandas as pd
import matplotlib as mpl, matplotlib.pyplot as plt
from matplotlib import font_manager
from utide import solve, reconstruct

warnings.filterwarnings('ignore')
_kr = Path('/home/firesinger/.fonts/malgun.ttf')
if _kr.exists(): font_manager.fontManager.addfont(str(_kr))
mpl.rcParams['font.family'] = ['Malgun Gothic', 'DejaVu Sans']; mpl.rcParams['axes.unicode_minus'] = False
ROOT = Path('/home/firesinger/khoa_tide'); DATA = ROOT / 'data'
EXT = ROOT / 'utide_validation' / 'extensions'
STA = pd.read_csv(Path('/mnt/e/study/tide/observations/stations_khoa.csv'))
STA.columns = [c.lstrip('﻿') for c in STA.columns]
LL = {r['name']: (float(r['lat']), float(r['lon'])) for _, r in STA.iterrows()}
CACHE = json.load(open(EXT / '9_eva_cache.json', encoding='utf-8'))
VENDOR = json.load(open(EXT / '20_model_hindcast.json', encoding='utf-8'))['storms']

# 태풍 기준일(KST 피크 근방) — ID = 타사 RE_* 명명과 동일 (연도2+호수2_영문명)
TYPHOONS = {
    '0215_RUSA':       ('루사',     '2002-08-31'),
    '0314_MAEMI':      ('매미',     '2003-09-12'),
    '0415_MEGI':       ('메기',     '2004-08-18'),
    '0711_NARI':       ('나리',     '2007-09-16'),
    '1215_BOLAVEN':    ('볼라벤',   '2012-08-28'),
    '1216_SANBA':      ('산바',     '2012-09-17'),
    '1618_CHABA':      ('차바',     '2016-10-05'),
    '1825_KONG-REY':   ('콩레이',   '2018-10-06'),
    '1918_MITAG':      ('미탁',     '2019-10-02'),
    '2009_MAYSAK':     ('마이삭',   '2020-09-03'),
    '2010_HAISHEN':    ('하이선',   '2020-09-07'),
    '2211_HINNAMNOR':  ('힌남노',   '2022-09-06'),   # ★ Gate 4
    '2214_NANMADOL':   ('난마돌',   '2022-09-19'),
    '2306_KHANUN':     ('카눈',     '2023-08-10'),   # ★ Gate 4
}
WINDOW_DAYS = 2


def parse(name, y):
    zp = DATA / name / f'{y}.zip'
    if not zp.exists(): return None
    with zipfile.ZipFile(zp) as z:
        raw = z.read(z.namelist()[0]).decode('cp949', errors='replace')
    rows = []
    for ln in raw.splitlines():
        p = ln.strip().split()
        if len(p) < 3 or '/' not in p[0][:5]: continue
        try: rows.append((f'{p[0]} {p[1]}', float(p[2])))
        except ValueError: continue
    if not rows: return None
    df = pd.DataFrame(rows, columns=['t', 'eta'])
    df['t'] = pd.to_datetime(df['t'], format='%Y/%m/%d %H:%M', errors='coerce')
    df = df.dropna(subset=['t', 'eta']); df['tutc'] = df['t'] - pd.Timedelta(hours=9)
    return df


def residual_year(name, y, lat):
    df = parse(name, y)
    if df is None or len(df) < 24 * 30 * 6: return None
    t = np.array(df['tutc'].dt.to_pydatetime()); eta = df['eta'].to_numpy(float)
    try:
        coef = solve(t, eta, lat=lat, method='ols', conf_int='none', verbose=False)
        rec = reconstruct(t, coef, verbose=False)
    except Exception: return None
    s = pd.Series(eta - rec.h, index=df['t'].values)   # KST index
    return s[np.abs(s) < 400]


def main():
    years = sorted({pd.Timestamp(d).year for _, (_, d) in TYPHOONS.items()})
    stations = [nm for nm in CACHE if nm in LL]
    print(f'정점 {len(stations)}개 × 연도 {years}')

    # (정점,연도) 편차 시계열 1회 계산
    resid = {}
    for y in years:
        for nm in stations:
            s = residual_year(nm, y, LL[nm][0])
            if s is not None: resid[(nm, y)] = s
        print(f'  {y}: {sum(1 for k in resid if k[1]==y)}/{len(stations)} 정점 분해 완료', flush=True)

    obs = {}
    for tid, (kr, date) in TYPHOONS.items():
        d = pd.Timestamp(date); y = d.year
        rec = {}
        for nm in stations:
            s = resid.get((nm, y))
            if s is None: continue
            w = s[(s.index >= d - pd.Timedelta(days=WINDOW_DAYS)) & (s.index <= d + pd.Timedelta(days=WINDOW_DAYS))]
            if not len(w): continue
            imax = w.idxmax()
            rec[nm] = {'max_cm': round(float(w.max()), 1),
                       'peak_kst': pd.Timestamp(imax).strftime('%Y-%m-%d %H:%M')}
        obs[tid] = rec
        print(f'  {tid}({kr}): {len(rec)}정점, 최대 ' +
              (max(rec.items(), key=lambda kv: kv[1]['max_cm'])[0] if rec else '-') +
              f" {max((v['max_cm'] for v in rec.values()), default=0):.0f}cm", flush=True)

    vendor = {tid: {nm: VENDOR[nm][tid] for nm in VENDOR if tid in VENDOR[nm]}
              for tid in TYPHOONS}

    json.dump({'typhoons': {k: {'name_kr': v[0], 'ref_date': v[1], 'window_days': WINDOW_DAYS}
                            for k, v in TYPHOONS.items()},
               'stations': {nm: {'lat': LL[nm][0], 'lon': LL[nm][1]} for nm in stations},
               'obs': obs, 'vendor_model_cm': vendor,
               'meta': {'method': 'utide OLS 연단위 분해 편차, ±2일 윈도우 최대, |편차|<400cm',
                        'unit': 'cm', 'tz': 'KST',
                        'vendor_note': '타 업체 산출물 — 참고용 벤치마크, 인용 불가',
                        'purpose': 'ADCIRC korea_multiuse Gate 4 (RMSE<=30cm) 검증 타깃'}},
              open(EXT / '23_validation_targets.json', 'w'), ensure_ascii=False, indent=1)

    # CSV (wide): 정점 × 태풍 관측최대
    with open(EXT / '23_validation_targets.csv', 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f)
        w.writerow(['정점', '위도', '경도'] + [f'{v[0]}({k.split("_")[0]})' for k, v in TYPHOONS.items()])
        for nm in stations:
            row = [nm, LL[nm][0], LL[nm][1]]
            for tid in TYPHOONS:
                v = obs[tid].get(nm)
                row.append(v['max_cm'] if v else '')
            w.writerow(row)

    # 그림: (a) 관측 vs 타사 산점 (b) Gate-4 태풍 정점별 관측
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    ax = axes[0]
    xs, ys, labels = [], [], []
    for tid in TYPHOONS:
        for nm, mv in vendor[tid].items():
            ov = obs[tid].get(nm)
            if ov and mv is not None:
                xs.append(ov['max_cm']); ys.append(mv); labels.append((tid, nm))
    xs, ys = np.array(xs), np.array(ys)
    ax.scatter(xs, ys, s=30, alpha=.6, color='#3b6ea5')
    lim = max(xs.max(), ys.max()) * 1.05
    ax.plot([0, lim], [0, lim], 'k--', lw=1, label='1:1')
    ax.plot([0, lim], [0, lim * 1.5], ':', color='#c0392b', lw=1, label='×1.5')
    rmse = float(np.sqrt(np.mean((ys - xs) ** 2))); bias = float(np.mean(ys - xs))
    ax.set_xlabel('관측 최대해일 (cm)'); ax.set_ylabel('타사 모델 (cm)')
    ax.set_title(f'타사 벤치마크 vs 관측 — {len(TYPHOONS)}태풍×10정점\nRMSE {rmse:.0f}cm, bias {bias:+.0f}cm (Gate4 기준 30cm)')
    ax.legend(); ax.grid(alpha=.3)
    ax = axes[1]
    for tid, c in [('2211_HINNAMNOR', '#c0392b'), ('2306_KHANUN', '#3b6ea5')]:
        items = sorted(obs[tid].items(), key=lambda kv: -kv[1]['max_cm'])[:18]
        nms = [k for k, _ in items]; vs = [v['max_cm'] for _, v in items]
        off = -0.2 if tid.startswith('2211') else 0.2
        ax.bar(np.arange(len(nms)) + off, vs, 0.38, label=TYPHOONS[tid][0], color=c, alpha=.85)
        if tid.startswith('2211'): ax.set_xticks(np.arange(len(nms))); ax.set_xticklabels(nms, rotation=45, ha='right', fontsize=8)
    ax.set_ylabel('관측 최대해일 (cm)'); ax.legend()
    ax.set_title('Gate-4 태풍 관측 타깃 (상위 18정점, 힌남노 기준 정렬)')
    ax.grid(axis='y', alpha=.3)
    fig.tight_layout(); fig.savefig(EXT / '23_validation_targets.png', dpi=125, bbox_inches='tight')
    n_obs = sum(len(v) for v in obs.values())
    print(f'→ 23_validation_targets.*  (관측 타깃 {n_obs}개, 타사대조 {len(xs)}쌍, 타사 RMSE {rmse:.0f}cm)')


if __name__ == '__main__':
    main()
