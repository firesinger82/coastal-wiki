---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort52.rst
lines: 28
sha256: 23e28dd3dbca2ac1461c982f3be9d1c6fad985f3ef2460a4ff0d4b6e98b9d42c
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort52.rst — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | Fort.52: Depth-averaged Velocity Harmonic Constituents at Specified Velocity Recording Stations — 지정한 속도 관측점(velocity recording station)의 수심 평균 속도(depth-averaged velocity) 해를 조화 분석(harmonic analysis)해서 구한 진폭(amplitude)과 위상(phase) 정보이다(1–4). 분석 주파수는 fort.15에 지정한다(4). 원문: ``Amplitude and phase information obtained from harmonic analysis of the velocity solution at the velocity recording stations and for the frequencies specified in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>`.`` (4). |
| 6–24 | File Structure — NFREQ와 주파수별 HAFREQ(k), HAFF(k), HAFACE(k), NAMEFR(k)를 기록한다(13–16). NSTAV 관측점마다 NFREQ를 순회하면서 UMAG(k,j), PHASEDU(k,j), VMAG(k,j), PHASEDV(k,j)를 기록한다(18–23). 원문: `The basic file structure is shown below. Each line of output is represented by a line containing the output variable name(s). Loops indicate multiple lines of output.` (9); `.. parsed-literal::` (11); ``    :ref:`NFREQ <NFREQ>` `` (13); ``    for k = 1, :ref:`NFREQ <NFREQ>` `` (14); ``       :ref:`HAFREQ(k) <HAFREQ>`, :ref:`HAFF(k) <HAFF>`, :ref:`HAFACE(k) <HAFACE>`, :ref:`NAMEFR(k) <NAMEFR>` `` (15); `   end k loop` (16); ``    :ref:`NSTAV <NSTAV>` `` (18); ``    for k=1, :ref:`NSTAV <NSTAV>` `` (19); ``       for j=1, :ref:`NFREQ <NFREQ>` `` (20); ``          :ref:`UMAG(k,j) <UMAG>`, :ref:`PHASEDU(k,j) <PHASEDU>`, :ref:`VMAG(k,j) <VMAG>`, :ref:`PHASEDV(k,j) <PHASEDV>` `` (21); `      end j loop` (22); `   end k loop` (23). |
| 25–28 | Note — 출력 형식은 ASCII이다(28). 원문: `* Output format is ascii ` (28). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
