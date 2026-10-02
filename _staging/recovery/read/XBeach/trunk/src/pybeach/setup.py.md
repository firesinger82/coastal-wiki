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
| 1–5 | `setuptools.setup/find_packages`와 `sys/os`를 가져오고 패키지 버전을 `0.1`로 둔다(1–4). |
| 6–22 | `setup` 메타데이터: 이름 `XBeach`, 4행의 버전, 파랑·흐름·퇴적물·지형변화 모델 설명(6–10), 과학/물리·연구자·Beta·GPLv3 분류(11–17), 키워드·저자·전자우편·웹 주소·`license='GPLv3'`(18–22). 긴 설명에는 public-domain이라는 문구가 있다(10). |
| 23–36 | `find_packages(exclude=['ez_setup', 'examples', 'tests'])`, `include_package_data=True`, `zip_safe=False`(23–25). 설치 의존성은 `numpy`, `matplotlib`, `nose`, CI용 `teamcity-nose`이며 버전 제한이 없다(26–32). `entry_points` 문자열에는 주석만 있고 `setup` 호출이 끝난다(33–36). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10·16·22: 긴 설명의 public-domain 문구와 GPLv3 분류·license 설정이 함께 존재한다.
- 2: 가져온 `sys`, `os`는 이 파일의 이후 코드에서 사용하지 않는다.
- 23: 제외 목록은 `tests`(복수)이며, 지정 판독 대상의 테스트 패키지 경로는 `xbeach/test`(단수)이다.
