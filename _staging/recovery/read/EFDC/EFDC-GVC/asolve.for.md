---
file: models/EFDC/raw/source_code/EFDC-GVC/asolve.for
lines: 34
sha256: 5302023a86ed087d289f261ce06acb78bf732c4b54e6ada82491d8da5cb96ed2
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# asolve.for — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 구분 주석과 `SUBROUTINE ASOLVE(PCGM,PTMPM)` 입구(1–6). EFDC-FULL 1.0a·수정일 및 빈 변경 기록 주석(8–20). `INCLUDE 'EFDC.PAR'` (21), `INCLUDE 'EFDC.CMN'` (22), PCGM·PTMPM을 길이 LCM 배열로 선언(23). 끝 주석(24). 포함 파일 내부는 이번 판독 대상이 아니다. |
| 25–29 | 시작 시 6행 ASOLVE 안. L=2..LA 루프(25–29)에서 LN=LNC(L), LS=LSC(L)를 가져온다(26–27). 배열 곱은 `PTMPM(L)=PCGM(L)*CC(L)` (28). 이 루프에는 조건 분기나 외부 루틴 호출이 없다. |
| 30–34 | 시작 시 6행 ASOLVE 안. PTMPM의 인덱스 1과 LC를 0으로 설정한다(30–31). 끝 주석(32), `RETURN` (33), `END` (34). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26–28: LN·LS를 대입한다. 이 파일의 계산식은 두 변수를 참조하지 않는다.
