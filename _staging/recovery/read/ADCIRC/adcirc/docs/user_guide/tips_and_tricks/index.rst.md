---
file: models/ADCIRC/raw/source_code/adcirc/docs/user_guide/tips_and_tricks/index.rst
lines: 34
sha256: 18835b04a34ddcfbc8ccf28a742da6a59b9b14e4f9356e64a07c22cefdd25f08
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.rst — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | Tips and Tricks — ADCIRC 사용의 팁, 요령, 모범 사례(best practices)를 포함하는 절이라고 설명한다(1–4). 제목 표시와 빈 줄을 포함한다(1–5). |
| 6–10 | Pre-Processing Tips — grid_dev_edit 문서로 ADCIRC 격자 생성과 편집 안내를 연결한다(9). 문서 참조 지시문과 빈 줄을 포함한다(6–10). 원문: `` * :doc:`grid_dev_edit` - Guide for generating and editing ADCIRC grids `` (9). |
| 11–16 | ADCIRC-Only Tips — meteorologial_only_mode는 빠른 기상 자료 처리를 위한 기상 전용 모드(meteorological-only mode) 안내라고 적는다(14). ramping_met_forcing_at_hotstart는 핫스타트(hotstart) 파일에서 시작할 때 기상 외력(meteorological forcing)을 점진적으로 적용하는 안내라고 적는다(15). 문서 참조와 빈 줄을 포함한다(11–16). 원문: `` * :doc:`meteorologial_only_mode` - Run ADCIRC in meteorological-only mode for quick processing of meteorological data `` (14); `` * :doc:`ramping_met_forcing_at_hotstart` - Properly ramp meteorological forcing when starting from a hotstart file `` (15). |
| 17–21 | ADCIRC+SWAN Tips — coupled_adcirc_swan으로 결합 ADCIRC+SWAN 실행 안내를 연결한다(20). 제목 표시와 빈 줄을 포함한다(17–21). 원문: `` * :doc:`coupled_adcirc_swan` - Tips for running coupled ADCIRC+SWAN simulations `` (20). |
| 22–26 | Post-Processing Tips — visualization으로 ADCIRC 결과의 시각화(visualization) 안내를 연결한다(25). 제목 표시와 빈 줄을 포함한다(22–26). 원문: `` * :doc:`visualization` - Guide for visualizing ADCIRC results `` (25). |
| 27–34 | 숨겨진 목차(toctree) — hidden 옵션과 다섯 문서 항목을 원문 순서대로 적는다(27–34). 마지막 항목 visualization까지 포함한다(34). 원문: ` .. toctree:: ` (27); `    :hidden: ` (28); `    coupled_adcirc_swan ` (30); `    grid_dev_edit ` (31); `    meteorologial_only_mode ` (32); `    ramping_met_forcing_at_hotstart ` (33); `    visualization ` (34). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
