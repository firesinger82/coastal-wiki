---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/elev_stat151.rst
lines: 21
sha256: de88c4ec89e5ce3a1c1d5d6ad3607c4d9d6f9282debf302c38c3cdeae07ffb64
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# elev_stat151.rst — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Elev_stat.151: Elevation Station Location Input File — 참조 라벨·제목·빈 줄과 수위(elevation) 기록 지점 수가 음수일 때 읽는 조건을 제시한다(1–6). 원문: ``The reading of the elev_stat.151 file is triggered when the number of elevation recording stations (:ref:`NSTAE`) in the :doc:`fort.15 <fort15>` file is set to a negative value.`` (6). |
| 8–17 | File Structure — 지점 수 다음에 각 지점의 좌표를 쓰는 parsed-literal 형식이다(11–16). 원문: `.. parsed-literal::` (11); ``     :ref:`NSTAE2` `` (13); ``     for k=1 to :ref:`NSTAE2` `` (14); ``         :ref:`XEL(k) <XEL>`, :ref:`YEL(k) <YEL>` `` (15); `    end k loop` (16). |
| 18–21 | Notes — 수가 다르면 이 파일의 지점 수를 사용한다(21). 지점이 지정 수보다 적으면 오류로 중지한다(21). 지점이 더 많으면 지정 수만큼 앞에서 사용한다(21). 원문: `If the value of NSTAE2 differs from the value of NSTAE (as read from the fort.15 file) the value of NSTAE2 will be used. If there are fewer than NSTAE2 stations listed in the elev_stat.151 file, ADCIRC will stop with an error. If there are more than NSTAE2 stations listed in the elev_stat.151 file, only the first NSTAE2 of them will be used.` (21). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
