---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/conc_stat151.rst
lines: 23
sha256: 27b413fde356d40899a154c7eb0b4adfecc9a470805ffa24e1535ad94aaa0f31
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# conc_stat151.rst — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Conc_stat.151: Concentration Station Location Input File — 참조 라벨·제목·빈 줄과 농도(concentration) 기록 지점 수가 음수일 때 읽는 조건을 제시한다(1–6). 원문: ``The reading of the conc_stat.151 file is triggered when the number of concentration recording stations (:ref:`NSTAC`) in the :doc:`fort.15 <fort15>` file is set to a negative value.`` (6). |
| 8–17 | File Structure — 지점 수 다음에 각 지점의 좌표를 쓰는 parsed-literal 형식이다(11–16). 원문: `.. parsed-literal::` (11); ``     :ref:`NSTAC2` `` (13); ``     for k=1, :ref:`NSTAC2` `` (14); ``         :ref:`XEC(k) <XEC>`, :ref:`YEC(k) <YEC>` `` (15); `    end k loop` (16). |
| 18–23 | Notes — 수가 다르면 이 파일의 지점 수를 사용한다(21). 지점이 지정 수보다 적으면 오류로 중지한다(21). 지점이 더 많으면 지정 수만큼 앞에서 사용한다(21). 모델 구성에 따른 조건부 입력임을 적는다(23). 원문: `If the value of NSTAC2 differs from the value of NSTAC (as read from the fort.15 file) the value of NSTAC2 will be used. If there are fewer than NSTAC2 stations listed in the conc_stat.151 file, ADCIRC will stop with an error. If there are more than NSTAC2 stations listed in the conc_stat.151 file, only the first NSTAC2 of them will be used.` (21); `This file is used for concentration station location input and is conditional on the model configuration. ` (23). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
