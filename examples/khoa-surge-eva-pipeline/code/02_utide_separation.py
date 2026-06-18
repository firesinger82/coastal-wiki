"""
02_utide_separation.py — utide 조화분석 -> 천문조 예측 -> 폭풍해일 잔차 (절차 outline)

목적: 관측 조위 시계열 η_obs(t) 에서 천문조 η_tide(t) 를 제거해
      폭풍해일 잔차 S(t) = η_obs(t) − η_tide(t) 산출.

출처(방법):
 - concepts/tides/03-analysis-methods.md §1 — 조화분해 η(t)=Z0+ΣHn cos(σn t − gn)
 - concepts/storm-surge/03-analysis-methods.md §1.1 — non-tidal residual (Pugh §6:1)

검증: 추출 조화상수 (Hn, gn) 를 KHOA 공시값과 cross-check
      (experience/khoa-49-station-16yr-utide-2026.md §4).

⚠ 재현 절차 outline. 정량값은 experience 노트 귀속.
"""
import numpy as np
import utide  # ~/coastal-wiki/.venv (uv) — utide>=0.3.1


def separate_surge(t_python_datenum, eta_obs_m, lat_deg):
    """utide 조화분석 + 재구성으로 폭풍해일 잔차 분리.

    t_python_datenum : matplotlib datenum (utide 입력 관례)
    eta_obs_m        : 관측 조위 (datum 기준, m)
    lat_deg          : 정점 위도 (nodal correction 용)
    반환             : (coef, eta_tide, surge_residual)
    """
    # 1) 조화분석: robust IRLS, nodal correction on, 선형 trend 추정
    coef = utide.solve(
        t_python_datenum,
        eta_obs_m,
        lat=lat_deg,
        method="robust",   # IRLS — 폭풍 outlier 에 강건
        nodal=True,        # 18.6년 nodal 변조 보정
        trend=True,        # MSL 선형 추세 동시 추정
        conf_int="MC",
        verbose=False,
    )

    # 2) 천문조 예측 재구성 (동일 시각)
    recon = utide.reconstruct(t_python_datenum, coef, verbose=False)
    eta_tide = recon.h  # = Z0 + Σ Hn cos(σn t − gn)  (+ 추세항)

    # 3) 폭풍해일 잔차 = 관측 − 천문조 (Pugh §6:1 non-tidal residual)
    surge_residual = np.asarray(eta_obs_m) - np.asarray(eta_tide)

    return coef, eta_tide, surge_residual


# 주요 4대분조 진폭·지각은 coef.aux / coef.A, coef.g 등으로 접근.
# KHOA 공시 조화상수와 M2/S2/K1/O1 cross-check 후 신뢰도 확정
# (experience/khoa-49-station-16yr-utide-2026.md §4: 신뢰 ranking
#  M2≈S2≈K1≈O1 ≫ N2≈P1 > K2 > Q1).
#
# 다음 단계: 03_eva_return_level.py 로 surge_residual 에 극치분석 적용.
