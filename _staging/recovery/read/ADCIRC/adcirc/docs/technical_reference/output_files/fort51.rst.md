---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort51.rst
lines: 28
sha256: e0bf184b6262f22b80d1f62e8bd07d69b6801ce4c2ab7197a4ae1ea15c46dd29
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort51.rst — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | Fort.51: Elevation Harmonic Constituents at Specified Elevation Recording Stations — 지정한 수위 관측점(elevation recording station)의 수위 해(elevation solution)를 조화 분석(harmonic analysis)해서 구한 진폭(amplitude)과 위상(phase) 정보이다(1–4). 분석 주파수는 fort.15에 지정한다(4). 원문: ``Amplitude and phase information obtained from harmonic analysis of the elevation solution at the elevation recording stations and for the frequencies specified in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>`.`` (4). |
| 6–24 | File Structure — NFREQ와 주파수별 HAFREQ(k), HAFF(k), HAFACE(k), NAMEFR(k)를 기록한다(13–16). NSTAE 관측점마다 NFREQ를 순회하면서 EMAG(k,j), PHASEDE(k,j)를 기록한다(18–23). 원문: `The basic file structure is shown below. Each line of output is represented by a line containing the output variable name(s). Loops indicate multiple lines of output.` (9); `.. parsed-literal::` (11); ``    :ref:`NFREQ <NFREQ>` `` (13); ``    for k = 1, :ref:`NFREQ <NFREQ>` `` (14); ``       :ref:`HAFREQ(k) <HAFREQ>`, :ref:`HAFF(k) <HAFF>`, :ref:`HAFACE(k) <HAFACE>`, :ref:`NAMEFR(k) <NAMEFR>` `` (15); `   end k loop` (16); ``    :ref:`NSTAE <NSTAE>` `` (18); ``    for k=1, :ref:`NSTAE <NSTAE>` `` (19); ``       for j=1, :ref:`NFREQ <NFREQ>` `` (20); ``          :ref:`EMAG(k,j) <EMAG>`, :ref:`PHASEDE(k,j) <PHASEDE>` `` (21); `      end j loop` (22); `   end k loop` (23). |
| 25–28 | Note — 출력 형식은 ASCII이다(28). 원문: `* Output format is ascii ` (28). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
