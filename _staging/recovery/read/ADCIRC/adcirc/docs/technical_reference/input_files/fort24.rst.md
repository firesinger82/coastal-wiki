---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort24.rst
lines: 53
sha256: cbbed91ab8f435c6132f4989f7791b5e542acc823d29c8b50817f00f08536ec5
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort24.rst — 판독 구간 기록

구간은 1행부터 53행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Fort.24: Self Attraction/Earth Load Tide Forcing File — 자기 인력·지구 하중 조석(self attraction/earth load tides)의 NTIP 조건을 제시한다(6). 속도 정보가 없는 tea 조화 형식(harmonic format), 분조(constituents) 순서·위상(phase)과 진폭(amplitude) 단위 및 절점 인자(nodal factor)·평형 인수(equilibrium argument) 보정을 설명한다(8). 원문: ``Self attraction/earth load tides are used to force ADCIRC when NTIP=2 in the :ref:`Model Parameter and Periodic Boundary Condition File <fort15>`.`` (6); ``The format of this file is identical to the "tea" harmonic format with no velocity information included. Entries are grouped by constituents and must be in the same order as the tidal potential terms listed in the :ref:`Model Parameter and Periodic Boundary Condition File <fort15>`. Phases must be in degrees. Amplitudes must be in units compatible with the units of gravity. These values are modified by the nodal factor and equilibrium argument provided for the tidal potential terms.`` (8). |
| 10–26 | File Structure — 분조별 네 선행 줄 다음에 전체 절점의 절점 번호·진폭·위상을 입력하는 반복 형식이다(13–25). 원문: `.. parsed-literal::` (15); ``    for k=1, :ref:`NTIF <NTIF>` `` (17); `      Alpha line` (18); `      Constituent frequency` (19); `      1` (20); `      Constituent name (e.g., M2)` (21); ``       for j=1, :ref:`NP <NP>` `` (22); ``          :ref:`JN <JN>`, :ref:`SALTAMP(k,JN) <SALTAMP>`, :ref:`SALTPHA(k,JN) <SALTPHA>` `` (23); `      end j loop` (24); `   end k loop` (25). |
| 27–39 | Notes — 분조별 선행 네 줄은 파일에 반드시 있어야 하나 ADCIRC가 읽을 때 건너뛴다고 적는다(30). 분조 순서·위상과 진폭 단위 및 조석 보정을 다시 명시한다(32–38). 원문: `1. The first four lines (Alpha line, Constituent frequency, 1, Constituent name) for each constituent must be present in the file but they are skipped over during the ADCIRC read.` (30); ``2. Entries must be grouped by constituents and must be in the same order as the tidal potential terms listed in the :ref:`Model Parameter and Periodic Boundary Condition File <fort15>`.`` (32); `3. Phases must be in degrees.` (34); `4. Amplitudes must be in units compatible with the units of gravity.` (36); `5. These values are modified by the nodal factor and equilibrium argument provided for the tidal potential terms.` (38). |
| 40–53 | Example — 파일 시작의 Alpha line, 분조 주파수·이름과 절점 세 개의 진폭·위상 예시이다(43–53). 원문: `.. code-block:: none` (45); `   Alpha line` (47); `   0.0805114017` (48); `   1` (49); `   M2` (50); `   1    0.12345E+00  0.23456E+00` (51); `   2    0.34567E+00  0.45678E+00` (52); `   3    0.56789E+00  0.67890E+00` (53). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
