---
file: models/EFDC/raw/source_code/EFDC-GVC/fdstrse.for
lines: 56
sha256: f752a7c649f72f24386a6201fe11da6c12a49c4daca6dcec39ee06052b7eded7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# fdstrse.for — 판독 구간 기록

구간은 1행부터 56행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | 구분 주석과 `FUNCTION FDSTRSE(VOID,BMECH1,BMECH2,BMECH3)` 선언(1–6). EFDC-FULL 1.0a·수정자·날짜, 표준 지수형 구성 관계(constitutive relationship) 추가 이력(8–19). `EFDC.PAR` 포함(21). 압축 길이 척도(compression length scale)를 물의 단위중량으로 정규화한 유효응력(effective stress)의 간극비(void ratio) 미분에 음 부호를 붙인 값이라고 적는다(23–28). 주석 단위는 m(30). |
| 32–42 | 시작 시 6행 FDSTRSE 함수 안. 원문 조건 `IF(BMECH1.GT.0.0)THEN` (32). 주석은 `st=sto*exp(-(void-voidso)/voidss)` (34), BMECH1/2/3=sto/voidso/voidss 대응을 적는다(35–37). 실행식 `TMP=-(VOID-BMECH2)/BMECH3` (39), 동일한 `TMP=-(VOID-BMECH2)/BMECH3` (40), `FDSTRSE=(BMECH1/BMECH3)*EXP(TMP)` (41). 다른 루틴 호출은 없다. |
| 43–56 | 시작 시 6행 FDSTRSE 함수·32행 조건 안. `ELSE` (43)는 BMECH1>0 불성립 경로다. 이전 다항식은 주석 처리되어 있다(45–46). 실행식 `FSTRSEL=-0.0147351*(VOID**3)+0.311854*(VOID**2)` (47); `&          -2.96371*VOID+7.34698` (48). 미분 다항식 `DFSTRSEL=-0.0442053*(VOID**2)+0.623708*VOID` (49); `&          -2.96371` (50). 반환식 `FDSTRSE=DFSTRSEL*EXP(FSTRSEL)` (51). 조건 종료·RETURN·END와 주석(52–56). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 39–40: TMP에 같은 식을 연속 두 번 대입한다.
- 25·49–51: 머리말은 유효응력 미분의 음수를 적는다. ELSE 분기는 DFSTRSEL에 다항식의 미분을 대입하고 `DFSTRSEL*EXP(FSTRSEL)`을 반환하며 별도의 음 부호를 붙이지 않는다.
