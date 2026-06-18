"""
01_fetch_khoa.py — KHOA 조위 관측 fetch (절차 outline)

목적: KHOA 조위 관측 시계열(실측 tdlvHgt + 예측 bscTdlvHgt) 확보.
출처(방법): concepts/storm-surge/04-code-and-tools.md §4.1 (OpenAPI surveyTideLevel,
            archive 약 1년 rolling retention 한계).

⚠ 본 파일은 재현 절차 outline (placeholder). 실제 운영 스크립트는 위키 외부
   (~/khoa_tide/utide_validation/) 로컬 한정. 정량 결과는 experience 노트 귀속.

전제: 환경변수 KHOA_API_KEY (data.go.kr 발급).
"""
import os
from urllib.parse import unquote

import requests


def fetch_tide_day(obs_code: str, req_date: str, interval_min: int = 60):
    """하루치 조위(실측·예측) fetch. archive 1년 이전이면 NODATA_ERROR.

    obs_code : KHOA 정점 코드 (예: 인천 DT_0001, 포항 DT_0091)
    req_date : 'YYYYMMDD'
    반환     : list of {time, tdlvHgt(실측 cm), bscTdlvHgt(예측 cm)}
    """
    key = unquote(os.environ["KHOA_API_KEY"])
    url = "https://apis.data.go.kr/1192136/surveyTideLevel/GetSurveyTideLevelApiService"
    n_rows = 24 * 60 // interval_min
    params = {
        "serviceKey": key,
        "type": "json",
        "obsCode": obs_code,
        "reqDate": req_date,
        "min": interval_min,
        "numOfRows": n_rows,
    }
    r = requests.get(url, params=params, timeout=20)
    body = r.json().get("body", {})
    # archive 한계: 약 1년 이전 reqDate -> body.resultCode == NODATA_ERROR
    # (concepts/storm-surge/04-code-and-tools.md §4.1 verified 측정)
    items = body.get("items", {}).get("item", [])
    # 주의: 일부 record 에 tdlvHgt / bscTdlvHgt 가 None — None 체크 필수
    return items


# 과거 storm event (1년 이전) 는 OpenAPI 불가 -> distribution.do ZIP 또는
# Annual Report 경로 사용. ZIP 일괄 다운로드(distributionSearchZipFile.do)는
# 1956~ 과거자료 확장 가능하나 product 가 OpenAPI 와 다름
# (ZIP '1시간 조위' != OpenAPI tdlvHgt; experience/khoa-49-station-16yr-utide-2026.md §2 진단).
#
# 다음 단계: 02_utide_separation.py 로 천문조 예측·폭풍해일 잔차 분리.
