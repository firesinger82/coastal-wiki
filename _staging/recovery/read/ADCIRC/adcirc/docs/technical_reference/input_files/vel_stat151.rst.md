---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/vel_stat151.rst
lines: 21
sha256: 3778cda584192cb5a67f4859fe13029f41755e6852405aeb4d6a43fa78e70ae8
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# vel_stat151.rst — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Vel_stat.151: Velocity Station Location Input File — fort.15의 속도 기록 관측점(velocity recording station) 수 NSTAV를 음수로 설정하면 이 파일을 읽는다(6). 원문: ``The reading of the vel_stat.151 file is triggered when the number of velocity recording stations (:ref:`NSTAV`) in the :doc:`fort.15 <fort15>` file is set to a negative value.`` (6). |
| 8–17 | File Structure — NSTAV2 뒤에 관측점별 XEV(k), YEV(k)를 기록하는 입력 형식을 제시한다(11–16). 원문: `.. parsed-literal::` (11); ``     :ref:`NSTAV2` `` (13); ``     for k=1, :ref:`NSTAV2` `` (14); ``         :ref:`XEV(k) <XEV>`, :ref:`YEV(k) <YEV>` `` (15); `    end k loop` (16). |
| 18–21 | Notes — NSTAV2가 fort.15의 NSTAV와 다르면 NSTAV2를 사용한다(21). 목록이 NSTAV2보다 적으면 오류로 중단한다(21). 목록이 NSTAV2보다 많으면 처음 NSTAV2개만 사용한다(21). 원문: `If the value of NSTAV2 differs from the value of NSTAV (as read from the fort.15 file) the value of NSTAV2 will be used. If there are fewer than NSTAV2 stations listed in the vel_stat.151 file, ADCIRC will stop with an error. If there are more than NSTAV2 stations listed in the vel_stat.151 file, only the first NSTAV2 of them will be used.` (21). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
