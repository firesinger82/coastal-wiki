#!/usr/bin/env python3
"""KHOA 정점별 UTide 분석 + KHOA 공시 조화상수와 비교

입력: data/<obs_code>_2025.csv (시각 KST, tdlvHgt cm)
출력:
  results/<obs_code>_utide.json  (UTide 결과)
  results/<obs_code>_compare.json (KHOA 공시값 비교)
  results/SUMMARY.md (해역별 종합 표)
"""
import pandas as pd
import numpy as np
import json
import sys
import warnings
from pathlib import Path
from datetime import datetime, timezone, timedelta
from utide import solve

warnings.filterwarnings('ignore')

ROOT = Path(__file__).parent
DATA = ROOT / "data"
RESULTS = ROOT / "results"
RESULTS.mkdir(parents=True, exist_ok=True)

# 정점 목록 (fetch_khoa_tide.py와 동일)
STATIONS = [
    ("DT_0001", "인천", "west", 37.45194, 126.59222),
    ("DT_0018", "군산", "west", 35.97555, 126.56305),
    ("DT_0007", "목포", "west", 34.77972, 126.37555),
    ("DT_0025", "보령", "west", 36.40638, 126.48611),
    ("DT_0067", "안흥", "west", 36.67463, 126.12955),
    ("DT_0005", "부산", "south", 35.09638, 129.03527),
    ("DT_0020", "울산", "south", 35.50194, 129.38722),
    ("DT_0014", "통영", "south", 34.82777, 128.43472),
    ("DT_0016", "여수", "south", 34.74722, 127.76555),
    ("DT_0049", "광양", "south", 34.90367, 127.75483),
    ("DT_0006", "묵호", "east", 37.55027, 129.11638),
    ("DT_0091", "포항", "east", 36.05177, 129.37627),
    ("DT_0012", "속초", "east", 38.20722, 128.59416),
    ("DT_0004", "제주", "jeju", 33.52750, 126.54305),
    ("DT_0010", "서귀포", "jeju", 33.24000, 126.56166),
]

# KHOA 공시 조화상수
KHOA_HC = pd.read_csv("/mnt/d/Numerical_models/01_Models/DASHBOARD/data/조석/조위관측소_조화상수.csv")
KHOA_HC = KHOA_HC.drop_duplicates(['obs_code','hc_name'])  # 중복 제거 (사용자 doc 노트)

# Key constituents
K4 = ['M2', 'S2', 'K1', 'O1']

def analyze_station(obs_code, obs_name, region, lat, lon):
    csv_path = DATA / f"{obs_code}_2025.csv"
    if not csv_path.exists():
        return None, "no data"

    df = pd.read_csv(csv_path)
    if len(df) < 24*30:  # 최소 1개월
        return None, f"insufficient data ({len(df)} rows)"

    # 시각 변환: KST → UTC (UTide는 datetime64 UTC 가정)
    df['t_kst'] = pd.to_datetime(df['t_kst'])
    df['t_utc'] = df['t_kst'] - pd.Timedelta(hours=9)
    df = df.dropna(subset=['tdlvHgt_cm'])
    df['eta_m'] = df['tdlvHgt_cm'] / 100.0  # m 단위

    # UTide
    try:
        coef = solve(
            df['t_utc'].values.astype('datetime64[ns]'),
            df['eta_m'].values,
            lat=lat,
            nodal=True, trend=False,
            method='robust',                # 한국 천해 강함
            conf_int='linear',
            Rayleigh_min=0.95,
            verbose=False,
        )
    except Exception as e:
        return None, f"UTide error: {e}"

    # 결과 추출
    utide_results = {}
    for n in K4:
        idx = list(coef['name']).index(n) if n in list(coef['name']) else -1
        if idx >= 0:
            utide_results[n] = {
                'amp_m': float(coef['A'][idx]),
                'amp_cm': float(coef['A'][idx]) * 100,
                'g_deg': float(coef['g'][idx]),         # UTide G (Greenwich)
            }

    # KHOA 공시값 (cm + G, KST)
    khoa = KHOA_HC[KHOA_HC['obs_code'] == obs_code]
    khoa_dict = {}
    for n in K4:
        row = khoa[khoa['hc_name'] == n]
        if len(row) > 0:
            khoa_dict[n] = {
                'amp_cm': float(row.iloc[0]['amp']),
                'g_gmt': float(row.iloc[0]['pha_gmt']),
                'g_kst': float(row.iloc[0]['pha_kst']),
            }

    # 비교 (UTide vs KHOA G)
    comparison = {}
    for n in K4:
        if n in utide_results and n in khoa_dict:
            u = utide_results[n]
            k = khoa_dict[n]
            d_amp = u['amp_cm'] - k['amp_cm']
            d_pct = 100 * d_amp / k['amp_cm'] if k['amp_cm'] > 0.5 else None
            # 위상 차이 (mod 360)
            d_g = (u['g_deg'] - k['g_gmt']) % 360
            if d_g > 180: d_g -= 360
            comparison[n] = {
                'utide_amp_cm': u['amp_cm'],
                'khoa_amp_cm': k['amp_cm'],
                'amp_diff_cm': d_amp,
                'amp_diff_pct': d_pct,
                'utide_G': u['g_deg'],
                'khoa_G': k['g_gmt'],
                'G_diff_deg': d_g,
            }

    # 비조화상수 계산
    nh = {}
    if all(n in utide_results for n in K4):
        Z0 = sum(utide_results[n]['amp_cm'] for n in K4)
        nh['Z0'] = Z0
        nh['MSL_cm'] = Z0
        nh['HHWL_cm'] = 2 * Z0
        H_M2 = utide_results['M2']['amp_cm']
        H_S2 = utide_results['S2']['amp_cm']
        H_K1 = utide_results['K1']['amp_cm']
        H_O1 = utide_results['O1']['amp_cm']
        nh['spring_rise_cm'] = 2*H_M2 + 2*H_S2 + H_K1 + H_O1
        nh['neap_rise_cm'] = 2*H_M2 + H_K1 + H_O1
        nh['mean_range_cm'] = 2*H_M2
        nh['spring_range_cm'] = 2*(H_M2 + H_S2)
        nh['neap_range_cm'] = 2*(H_M2 - H_S2)
        nh['form_factor'] = (H_K1 + H_O1) / (H_M2 + H_S2)
        # 분류
        F = nh['form_factor']
        if F < 0.25:
            nh['form_class'] = 'semidiurnal'
        elif F < 1.5:
            nh['form_class'] = 'mixed-semidiurnal'
        elif F < 3.0:
            nh['form_class'] = 'mixed-diurnal'
        else:
            nh['form_class'] = 'diurnal'

    return {
        'obs_code': obs_code,
        'obs_name': obs_name,
        'region': region,
        'lat': lat, 'lon': lon,
        'n_records': len(df),
        'utide': utide_results,
        'khoa_published': khoa_dict,
        'comparison': comparison,
        'non_harmonic': nh,
    }, None

if __name__ == "__main__":
    summary = []
    for obs_code, obs_name, region, lat, lon in STATIONS:
        print(f"[{datetime.now().isoformat()}] {obs_code} {obs_name} ({region}) 분석…", flush=True)
        result, err = analyze_station(obs_code, obs_name, region, lat, lon)
        if err:
            print(f"  SKIP: {err}")
            continue
        # save per-station
        with open(RESULTS / f"{obs_code}_result.json", 'w') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        summary.append(result)
        # console snapshot
        for n in K4:
            if n in result['comparison']:
                c = result['comparison'][n]
                print(f"  {n}: UTide={c['utide_amp_cm']:7.2f} cm  KHOA={c['khoa_amp_cm']:7.2f} cm  Δ={c['amp_diff_cm']:+6.2f} ({c['amp_diff_pct']:+.1f}%)  ΔG={c['G_diff_deg']:+.2f}°")
        if result['non_harmonic']:
            nh = result['non_harmonic']
            print(f"  Z0={nh['Z0']:.1f} cm  Form F={nh['form_factor']:.3f} ({nh['form_class']})")

    # save full summary
    with open(RESULTS / "ALL_RESULTS.json", 'w') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"\n총 {len(summary)} 정점 분석 완료. 결과: {RESULTS}/")
