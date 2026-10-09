---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/met_stat151.rst
lines: 21
sha256: 272fc800e27df93ab443fac8a4259a52b4e675c877823e0f0d088b690121af4e
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# met_stat151.rst — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Met_stat.151: Meteorological Recording Station Location Input File — fort.15의 기상 기록 관측점(meteorological recording station) 수 NSTAM을 음수로 설정하면 이 파일을 읽는다(6). 원문: ``The reading of the met_stat.151 file is triggered when the number of meteorological recording stations (:ref:`NSTAM`) in the :doc:`fort.15 <fort15>` file is set to a negative value.`` (6). |
| 8–17 | File Structure — NSTAM2 뒤에 관측점별 XEM(k), YEM(k)를 기록하는 입력 형식을 제시한다(11–16). 원문: `.. parsed-literal::` (11); ``     :ref:`NSTAM2` `` (13); ``     for k=1, :ref:`NSTAM2` `` (14); ``         :ref:`XEM(k) <XEM>`, :ref:`YEM(k) <YEM>` `` (15); `    end k loop` (16). |
| 18–21 | Notes — NSTAM2가 fort.15의 NSTAM과 다르면 NSTAM2를 사용한다(21). 목록이 NSTAM2보다 적으면 오류로 중단한다(21). 목록이 NSTAM2보다 많으면 처음 NSTAM2개만 사용한다(21). 원문: `If the value of NSTAM2 differs from the value of NSTAM (as read from the fort.15 file) the value of NSTAM2 will be used. If there are fewer than NSTAM2 stations listed in the met_stat.151 file, ADCIRC will stop with an error. If there are more than NSTAM2 stations listed in the met_stat.151 file, only the first NSTAM2 of them will be used. ` (21). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
