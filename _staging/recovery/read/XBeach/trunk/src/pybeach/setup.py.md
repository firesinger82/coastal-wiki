---
file: models/XBeach/raw/source_code/trunk/src/pybeach/setup.py
lines: 36
sha256: 8ba71c00c19e37b255d7fd74ccb5a1b2fc247fd6edb67960847a25cd0d26a6c6
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# setup.py — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | setuptools의 setup·find_packages 및 sys·os 가져오기(1–2), 버전 기본값 `version = '0.1'` (4), 빈 줄. |
| 6–25 | setup 호출의 이름 XBeach·version·짧은/긴 설명(6–10). classifiers는 과학/공학·물리·연구자·Beta·GPLv3(11–17); 키워드·작성자·메일·URL·license='GPLv3'(18–22). `packages=find_packages(exclude=['ez_setup', 'examples', 'tests'])` (23), `include_package_data=True` (24), `zip_safe=False` (25). 조건 분기 없음. |
| 26–36 | install_requires는 numpy·matplotlib·nose·teamcity-nose이며 마지막 항목은 Deltares CI용이라는 주석(26–32). entry_points는 실제 엔트리 없이 자리표시자 주석 문자열(33–35); setup 호출 종료(36). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 2: sys·os를 가져오지만 이후 이 파일에서 사용하지 않는다.
- 10·16·22: 긴 설명은 public-domain model이라고 쓰고, 패키지 classifier와 license는 GPLv3로 적는다.
- 23: 제외 이름은 'tests'이며 지정된 소스 트리의 테스트 패키지 이름은 xbeach/test이다. 제외 목록에 'test'는 없다.
