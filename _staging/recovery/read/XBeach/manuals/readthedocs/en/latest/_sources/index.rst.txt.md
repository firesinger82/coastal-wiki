---
file: models/XBeach/raw/manuals/readthedocs/en/latest/_sources/index.rst.txt
lines: 139
sha256: a8b0dec90081ece71663ced179fa8d99e35e9e7d3f45441b056ce1e230bf4b1a
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# index.rst.txt — 판독 구간 기록

구간은 1행부터 139행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | Welcome to XBeach manual's documentation! — 2023-06-27 sphinx-quickstart 생성 주석과 root toctree 안내, 문서 제목·밑줄·빈 줄(1–8). |
| 9–33 | 모델 소개 — km 규모 모래 해안의 폭풍 수리·형태 영향 모델로 시작한 배경(9–13). 단/장파·setup·흐름·월파/침수·퇴적물·사면/하상/붕괴·식생/구조물 및 검증 설명(15–24). 정수압의 단파 진폭 분리와 위상 미해결, 비정수압의 단파 포함 및 계산 요구를 비교한다(26–32). 원문: `XBeach has two modes: a hydrostatic and a non-hydrostatic mode. In the` (26); `hydrostatic mode, the short wave amplitude variation is solved` (27); `separately from the long waves, currents and morphological` (28); `change. This saves considerable computational time, with the expense` (29); `that the phase of the short waves is not simulated. A more complete` (30); `model is the non-hydrostatic model which solves all processes` (31); `including short wave motions, but with more computational demand.` (32). |
| 34–69 | 개발·지원·매뉴얼 목적 — 미국/네덜란드/유럽 기관과 사구·도시·산호/환초·식생 적용 배경(34–48). TU Delft 비정수압 개발, 자갈 해안·선박 파랑 확장, 참여자 감사 및 도입/참고 매뉴얼 목적(50–68). |
| 70–101 | Contents / 앞 목차 — User manual, Parameters, Numerical implementation, Other functionalities의 toctree 지시문·깊이/캡션/항목을 포함한다(70–100). 원문: `Contents:` (70); `.. toctree::` (72); `   :maxdepth: 3` (73); `   :Caption: User manual` (74); `   xbeach_manual` (76); `.. toctree::` (80); `   :maxdepth: 3` (81); `   :Caption: Parameters` (82); `   input_parameters` (84); `   output_variables` (85); `.. toctree::` (89); `   :maxdepth: 3` (90); `   :Caption: Numerical implementation` (91); `   numerical_implementation` (93); `.. toctree::` (96); `   :maxdepth: 3` (97); `   :Caption: Other functionalities` (98); `   advanced_techniques` (100). |
| 102–130 | Contents / 뒤 목차 — Tools(Matlab tutorial/toolbox, Python), Examples/gallery, compile, cheatsheet의 toctree 지시문·깊이·캡션·항목 및 빈 줄(102–130). 원문: `.. toctree::` (102); `   :maxdepth: 3` (103); `   :Caption: Tools` (104); `   matlab_tutorials` (106); `   matlab_toolbox` (107); `   python_tools` (108); `.. toctree::` (110); `   :maxdepth: 3` (111); `   :Caption: Examples` (112); `   examples` (114); `   gallery` (115); `.. toctree::` (117); `   :maxdepth: 3` (118); `   :Caption: How to compile?` (119); `   compile` (121); `.. toctree::` (123); `   :maxdepth: 3` (124); `   :Caption: Instruction for manual` (125); `   cheatsheet` (127). |
| 131–139 | Bibliography / Footnotes — xbeach.bib의 cited·alpha 서지 지시문(131–135). 특정 파형 공식 적용 조건과 문헌·절 참조를 가진 각주 정의(137–139). 원문: `.. rubric:: Bibliography` (131); `.. bibliography:: xbeach.bib` (133); `   :cited:` (134); `   :style: alpha` (135); `.. rubric:: Footnotes` (137); ``.. [#1] Currently, this formulation is only possible when the wave shape formulation of :cite:`VanThieldeVries2009a` is applied, see :ref:`sec-wave-shape`.`` (139). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 137–139: 각주 정의의 `this formulation`이 가리키는 공식은 이 파일 본문에 제시되지 않는다. 참조 대상 절 `sec-wave-shape`는 이 파일 안에 정의되어 있지 않으며 다른 파일의 대상 유무는 확인하지 않았다.
