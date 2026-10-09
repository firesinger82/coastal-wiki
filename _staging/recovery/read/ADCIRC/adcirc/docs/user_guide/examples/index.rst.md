---
file: models/ADCIRC/raw/source_code/adcirc/docs/user_guide/examples/index.rst
lines: 46
sha256: 13aec56d342be2ad6b8ef1e6f60c6c1235a757ebb9892b7b3c5e7fe5712c7e2b
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.rst — 판독 구간 기록

구간은 1행부터 46행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | Examples — 메타 지시문·앵커·제목을 포함한다(1–8). 기본 용도와 일반 ADCIRC 기능을 다루는 시험 사례 목록을 소개한다(10–11). 더 많은 시험이 있는 GitHub 시험 모음을 안내한다(12–14). 원문: `Below is a list of convenient test cases covering a range of basic uses and` (10); `common ADCIRC capabilities. In addition to the test cases shown below, note the` (11); `ADCIRC test suite hosted on the GitHub repository,` (12); `https://github.com/adcirc/adcirc-testsuite, which has many of the tests below` (13); `and more.` (14). |
| 16–38 | 사례 링크 목록 — 항만·해협·월류 경계·바람·대형 격자·Katrina 및 전 지구 조석·알래스카 해빙·이상화 수로 사례를 나열한다(16–37). 차원 표기와 NWS 값을 원문대로 기록한다. 원문: ``-  `Quarter Annular Harbor with Tidal Forcing (2D and`` (16); ``   3D) <https://adcirc.org/home/documentation/example-problems/quarter-annular-harbor-with-tidal-forcing-example/>`__`` (17); ``-  `Shinnecock Inlet with Tidal Forcing`` (18); ``   (2D) <https://adcirc.org/home/documentation/example-problems/shinnecock-inlet-ny-with-tidal-forcing-example>`__`` (19); ``-  `Beaufort Inlet`` (20); ``   (2D) <https://adcirc.org/home/documentation/example-problems/beaufort-inlet-nc-example/>`__`` (21); ``-  `Idealized Inlet`` (22); ``   (2D) <https://adcirc.org/home/documentation/example-problems/idealized-inlet-test-cases/>`__`` (23); ``-  `Internal Overflow Boundary`` (24); ``   (2D) <https://adcirc.org/home/documentation/example-problems/internal-overflow-boundaries-example/>`__`` (25); ``-  `APES Wind Run (NWS = 3)`` (26); ``   (2D) <https://adcirc.org/home/documentation/example-problems/apes-wind-run-example/>`__`` (27); ``-  `Hurricane Isabel Wind Run (NWS = 4)`` (28); ``   (2D) <https://adcirc.org/home/documentation/example-problems/hurricane-isabel-example/>`__`` (29); ``-  `Large Grid (~300,000 nodes) Tides`` (30); ``   Only <https://adcirc.org/home/documentation/example-problems/large-grid-tides-example/>`__`` (31); ``-  `Hurricane Katrina`` (32); ``   (NWS=20) <https://adcirc.org/home/documentation/example-problems/katrina-run-2015-nws-20-example/>`__`` (33); `` -  :doc:`Global Astronomical M2 Tide (2D) <global_astronomical_m2_tide>` `` (34); `` -  :doc:`Global Storm Tide - Hurricane Katrina (NWS = -14) (2D) <global_storm_tide_katrina>` `` (35); `` -  :doc:`Alaskan Winter Storm with Ice (NWS = 14) (2D) <alaskan_winter_storm_with_ice>` `` (36); `` -  :doc:`Idealized Channel Problem (2D) <idealized_channel>` `` (37). |
| 39–46 | 숨김 toctree — `:hidden:` 옵션 아래에 알래스카 해빙, 전 지구 M2, Katrina, 이상화 수로 문서 이름을 적는다(39–45). 마지막 공백 행을 포함한다(46). 원문: `.. toctree::` (39); `   :hidden:` (40); `   alaskan_winter_storm_with_ice` (42); `   global_astronomical_m2_tide` (43); `   global_storm_tide_katrina` (44); `   idealized_channel` (45). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 36: 알래스카 사례 링크의 표시값은 `NWS = 14`이다. 이번에 함께 읽은 `alaskan_winter_storm_with_ice.rst`의 34행 사례 설정은 `NWS` = `14014`이다.
