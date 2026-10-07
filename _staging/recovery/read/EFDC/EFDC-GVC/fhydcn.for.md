---
file: models/EFDC/raw/source_code/EFDC-GVC/fhydcn.for
lines: 51
sha256: 0db43c7b4baf989888506b7f2ad8508a3c6248e65c731b912a1e6c2f4ab830e2
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# fhydcn.for — 판독 구간 기록

구간은 1행부터 51행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | 구분 주석과 `FUNCTION FHYDCN(VOID,BMECH4,BMECH5,BMECH6,IBMECHK)` 선언(1–6). EFDC-FULL 1.0a·수정자·날짜, 지수형 구성 관계(constitutive relationship) 추가 이력(8–19). 빈 주석과 `EFDC.PAR` 포함(20–23). 주석은 수리전도도(hydraulic conductivity)를 1+간극비(void ratio)로 나눈 값이며 단위는 m/s라고 적는다(24–26). |
| 28–41 | 시작 시 6행 FHYDCN 함수 안. 원문 조건 `IF(BMECH4.GT.0.0)THEN` (28). 주석 관계 `k=ko*exp((void-voidko)/voidkk)` (30), BMECH4/5/6=ko/voidko/voidkk 대응(31–33). 실행식 `TMP=(VOID-BMECH5)/BMECH6` (35). 내부 조건 `IF(IBMECHK.EQ.0) THEN` (36)은 `FHYDCN=BMECH4*EXP(TMP)/(1.+VOID)` (37)를 반환한다. `ELSE` (38)는 `FHYDCN=BMECH4*EXP(TMP)` (39)를 반환한다. 내부 조건 종료와 빈 주석(40–41). |
| 42–51 | 시작 시 6행 FHYDCN 함수·28행 BMECH4 조건 안. 바깥 `ELSE` (42)는 BMECH4>0 불성립 경로다. 실행식 `FHYDCNLOG=0.00816448*(VOID**3)-0.232453*(VOID**2)+2.5759*VOID` (44); `&         -28.581` (45). 반환식 `FHYDCN=EXP(FHYDCNLOG)` (46). 바깥 조건 종료·RETURN·END와 주석(47–51). 다른 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24·36–39: 머리말은 1+VOID로 나눈 전도도를 설명한다. BMECH4>0이고 IBMECHK가 0이 아니면 반환식에는 1+VOID 나눗셈이 없다.
- 28–48: IBMECHK 검사는 BMECH4>0 분기에만 있다. 다항식 ELSE 분기는 IBMECHK를 참조하지 않는다.
