---
file: models/EFDC/raw/source_code/EFDC-GVC/smlcfg.for
lines: 38
sha256: 4c36632534bad787ed4904a6c4bfb7f34bb0266f7f1877d7fae57dba0cdd9c53
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# smlcfg.for — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 구분 주석·SMLCFG(NOTUSED, XSOL, FVAL, GRAD, HAVEG) 선언(1–7), EFDC.PAR·EFDC.CMN 포함(8–9), LOGICAL HAVEG 및 XSOL(LCM-2)·GRAD(LCM-2)·PVAL(LCM) 배열 선언(11–12). `      HAVEG=.TRUE.` (14)로 기울기(gradient) 제공 표시를 설정한다. 주석도 포함한다. |
| 16–24 | 시작 시 6행 SMLCFG 루틴 안. XSOL을 PVAL로 옮긴다는 주석(16). PVAL(1)·PVAL(LC)를 0으로 두고(18–19), L=2..LA에서 XSOL(L-1)을 PVAL(L)에 복사한다(21–23). 주석도 포함한다. |
| 25–38 | 시작 시 6행 SMLCFG 루틴 안. 함수·기울기 계산 주석(25). FVAL을 0으로 두고 L=2..LA에서 LN·LS를 가져온다(27–30). 다섯 점 계수 곱의 연속식은 `        GVAL=CCC(L)*PVAL(L)+CCS(L)*PVAL(LS)+CCW(L)*PVAL(L-1)` (31); `     &        +CCE(L)*PVAL(L+1)+CCN(L)*PVAL(LN)` (32). 목적함수(objective function) 누적은 `        FVAL=FVAL+PVAL(L)*( 0.5*GVAL-FPTMP(L) )` (33). 기울기는 `        GRAD(L-1)=GVAL-FPTMP(L)` (34). 루프·주석·RETURN·END를 포함한다(35–38). 다른 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·8–38: NOTUSED는 인수 목록에만 있으며 실행문에서 참조하지 않는다.
- 18–23·28–34: PVAL은 1·LC와 2..LA에 값을 대입한다. XSOL·GRAD는 L-1 인덱스를 사용한다. 이 루틴에는 LA·LC·LCM의 관계를 검사하는 문장이 없다.
