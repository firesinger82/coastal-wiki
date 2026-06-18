"""
03_eva_return_level.py — 폭풍해일 잔차 -> 100년 재현값 + 부트스트랩 CI (절차 outline)

목적: 폭풍해일 잔차 S(t) 에서 극값 표본을 추출하고 극치분포를 적합해
      100년 재현 폭풍해일고 z100 과 95% 신뢰구간을 산정.

출처(방법):
 - concepts/storm-surge/03-analysis-methods.md §3 (annual maxima 표본),
   §4 (ranking P=(2r−1)/2M, trend 사전보정), §5 (joint convolution)
 - experience/khoa-design-surge-eva-2026.md §2·§11·§13 — 극치 4법 수렴·POT 자동임계·
   부트스트랩 CI·정점별 고정 시드 재현성

⚠ 재현 절차 outline. 정점별 정량 결과·판정은 experience 노트 귀속.
"""
import numpy as np
from scipy import stats  # ~/coastal-wiki/.venv — scipy>=1.17


# --- ③ 극값 표본 추출 -------------------------------------------------------
def annual_maxima(times, surge, years):
    """연최대(AM) 표본 — 매년 surge 최댓값. (Pugh §8:3:2)"""
    return np.array([surge[(times.year == y)].max() for y in years])


def peaks_over_threshold(surge, threshold, min_sep_hours=48):
    """POT 표본 — 임계 초과 피크, 동일 폭풍 중복은 디클러스터(시간 분리).

    threshold     : 임계 τ (자동선정: z100 plateau 탐색, experience §11)
    min_sep_hours : 디클러스터 간격 (독립 event 보장)
    """
    exceed = np.where(surge > threshold)[0]
    peaks, last = [], -10**9
    for i in exceed:
        if i - last >= min_sep_hours:
            peaks.append(surge[i])
            last = i
        elif peaks and surge[i] > peaks[-1]:
            peaks[-1] = surge[i]  # 같은 cluster 내 더 큰 피크로 갱신
    return np.array(peaks)


# --- ④/⑤ 극치분포 적합 + 100년 재현값 --------------------------------------
def return_level_gev(am_sample, period=100):
    """GEV(L-moment 대용: scipy MLE) 100년 재현값. shape 가 꼬리 결정."""
    c, loc, scale = stats.genextreme.fit(am_sample)  # c = −shape (scipy 관례)
    p_nonexceed = 1 - 1.0 / period
    return stats.genextreme.ppf(p_nonexceed, c, loc=loc, scale=scale)


def return_level_gumbel(am_sample, period=100):
    """Gumbel(가벼운 꼬리) 100년 재현값. 단기록일수록 과소 경향(experience §2)."""
    loc, scale = stats.gumbel_r.fit(am_sample)
    return stats.gumbel_r.ppf(1 - 1.0 / period, loc=loc, scale=scale)


def return_level_gpd(pot_sample, threshold, n_years, lam, period=100):
    """POT/GPD 100년 재현값. lam = 연평균 초과 횟수(rate)."""
    c, loc, scale = stats.genpareto.fit(pot_sample - threshold, floc=0)
    # 100년 = lam*period 회 중 1회 초과 수준
    p = 1 - 1.0 / (lam * period)
    return threshold + stats.genpareto.ppf(p, c, loc=0, scale=scale)


# --- ⑤ 부트스트랩 95% CI ---------------------------------------------------
def bootstrap_ci(sample, estimator, n_boot=2000, seed=0, period=100):
    """재표집 부트스트랩 95% CI (정점별 고정 시드로 재현성, experience §13)."""
    rng = np.random.default_rng(seed)  # 정점별 CRC32 시드 권장
    n = len(sample)
    ests = [estimator(rng.choice(sample, n, replace=True), period) for _ in range(n_boot)]
    return np.percentile(ests, [2.5, 97.5])


# 절차 요약:
#  1) (선택) ranking 전 Mann-Kendall trend 검출 -> SLR 제거 -> 공통연도 normalize
#     (Pugh §8:3:2; concepts/storm-surge/03-analysis-methods.md §4.3)
#  2) AM·POT 표본 추출 -> Gumbel/GEV/GPD 각각 적합 -> z100 산정
#  3) 부트스트랩 CI -> 방법 간 수렴/발산 검토 (단일 방법 결론 금지, experience §2)
#  4) (지역빈도 RFA) 유사 정점 권역화 index-flood — Hosking-Wallis H 동질성 진단
#     -> 단일정점 단기록 CI 과대 완화 (experience §13)
#  5) (감사·joint·SSP) ⑥ 단계 — 정량 결론은 experience 노트 귀속
