---
file: models/XBeach/raw/manuals/readthedocs/en/latest/_sources/advanced_techniques.rst.txt
lines: 27
sha256: b9d7dfb128ef70d9b3c376586b624d8b165a776e461aca7603f0965be75f698f
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# advanced_techniques.rst.txt — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | Advanced techniques — 단독 실행·MPI 실행에 더해 BMI 호환 library를 통한 큰 프레임워크 내부 실행 중 상호작용을 설명한다(4–9). 원문: `Traditionally, XBeach is used as a standalone executable that is ran` (4); `on a single XBeach model schematization, possibly distributed over` (5); `multiple processes through MPI. Nowadays, XBeach can also be used as a` (6); `BMI-compatible library. A library can be part of a larger framework` (7); `where XBeach interacts with other components during runtime. For` (8); `example:` (9). |
| 11–23 | 연동 예제 — Morphan GUI(11–12), 실행 중 변경 가능한 Sandbox(14–16), 풍성 퇴적물·생태·XBeach 자체 결합 모델과 링크를 제시한다(18–21). 빈 줄 포함. 원문: ``* A graphical user interface (e.g. `Morphan`` (11); ``  <https://www.helpdeskwater.nl/onderwerpen/applicaties-modellen/applicaties-per/aanleg-onderhoud/aanleg-onderhoud/morphan/>`_).`` (12); `* An interactive modeling tool that allow users to change the model` (14); ``  while running (e.g. `Sandbox`` (15); ``  <https://www.deltares.nl/en/software/sandbox/>`_).`` (16); `* A coupled model where XBeach runs simultaneously and interactively` (18); ``  with other models (e.g.  `aeolian sediment transport model`` (19); ``  <http://windsurf.readthedocs.io/en/latest/>`_, ecological model or`` (20); ``  `XBeach itself <http://xbeachmi.readthedocs.io/en/latest/>`_!).`` (21). |
| 24–27 | Library 배포 — Windows DLL은 daily build, Unix library는 실행파일과 함께 컴파일된다고 설명한다(24–27). Deltares build server라고 붙인 링크를 원문대로 기록한다. 원문: `The XBeach library (DLL) for Windows is shipped with the daily builds` (24); ``from the `Deltares build server`` (25); ``<http://xbeachmi.readthedocs.io/en/latest/>`_. A unix library is`` (26); `compiled alongside the XBeach executable.` (27). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 21·25–26: `XBeach itself`와 `Deltares build server`로 표시한 링크 주소가 모두 `http://xbeachmi.readthedocs.io/en/latest/`이다. 링크 접속 결과는 확인하지 않았다.
