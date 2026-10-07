---
file: models/EFDC/raw/source_code/EFDC-GVC/fstrse.for
lines: 48
sha256: 0650c1e75863a035ac5ee35461d5b6b35abac5fb7e60303cb64239e67080e1a3
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# fstrse.for — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 구분 주석과 `FUNCTION FSTRSE(VOID,BMECH1,BMECH2,BMECH3)` 선언(1–6). EFDC-FULL 1.0a·수정자·날짜, 지수형 구성 관계(constitutive relationship) 추가 이력과 변경 이력 틀(8–19). `EFDC.PAR` 포함(21). 물의 단위중량으로 정규화한 유효응력(effective stress)을 반환하며 단위는 m이라는 주석(23–25). |
| 27–36 | 시작 시 6행 FSTRSE 함수 안. 조건 `IF(BMECH1.GT.0.0)THEN` (27). 주석 관계 `st=sto*exp(-(void-voidso)/voidss)` (29), BMECH1/2/3=sto/voidso/voidss 대응(30–32). 실행식 `TMP=-(VOID-BMECH2)/BMECH3` (34), `FSTRSE=BMECH1*EXP(TMP)` (35). |
| 37–48 | 시작 시 6행 FSTRSE 함수·27행 BMECH1 조건 안. `ELSE` (37)는 BMECH1>0 불성립 경로다. 이전 다항식은 주석 처리(39–40). 실행식 `FSTRSELOG=-0.0147351*(VOID**3)+0.311854*(VOID**2)-2.96371*VOID` (41); `&          +7.34698` (42), `FSTRSE=EXP(FSTRSELOG)` (43). 조건 종료·RETURN·END와 주석(44–48). 외부 루틴 CALL 문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27·34: 지수형 관계 선택 조건은 BMECH1>0이다. BMECH3 나눗셈 앞에는 BMECH3에 대한 실행 조건 검사가 없다.
