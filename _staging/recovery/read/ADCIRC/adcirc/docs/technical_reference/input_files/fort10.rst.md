---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort10.rst
lines: 29
sha256: 7dc2749c9aadbece37993485c0cc4e9d8add33690ce47a36d481779dc0f54654
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort10.rst — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | Fort.10: Passive Scalar Transport Input File / File Structure — 수동 스칼라(passive scalar) 수송 입력의 참조 라벨·제목과 기본 형식이다(1–16). 두 헤더(header) 다음에 수와 절점별 농도 입력을 제시한다(11–16). 원문: `.. parsed-literal::` (9); `   Header Line 1` (11); `   Header Line 2` (12); ``    :ref:`NVP <NVP>` `` (13); ``    for k=1 to :ref:`NVP <NVP>` `` (14); ``       :ref:`jki <jki>`, :ref:`DACONC(jki) <DACONC>` `` (15); `   end k loop` (16). |
| 18–29 | File structure for a 3D run — 3차원 형식은 두 헤더 다음에 수직·수평 절점 수를 놓고 중첩 반복에서 절점 번호와 농도를 입력한다(18–29). 단위와 기본값은 이 파일에 적혀 있지 않다. 원문: `File structure for a 3D run:` (18); `.. parsed-literal::` (20); `   Header Line 1` (22); `   Header Line 2` (23); ``    :ref:`NVN <NVN>`, :ref:`NVP <NVP>` `` (24); ``    for k=1 to :ref:`NVP <NVP>` `` (25); ``       for j=1 to :ref:`NVN <NVN>` `` (26); ``          :ref:`NHNN <NHNN>`, :ref:`NVNN <NVNN>`, :ref:`CONC(NHNN,NVNN) <CONC>` `` (27); `      end j loop` (28); `   end k loop ` (29). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
