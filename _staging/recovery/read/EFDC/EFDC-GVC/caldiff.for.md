---
file: models/EFDC/raw/source_code/EFDC-GVC/caldiff.for
lines: 49
sha256: 1c8eda5419e569b1865fa7d15f9a704b85a9e6ac5c8c94e2f29f51bad58bdeb3
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# caldiff.for — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | 구분 주석과 `SUBROUTINE CALDIFF (ISTL,M,CON1)` 선언(6). EFDC-FULL 1.0a·최종 수정·빈 변경 기록(8–17). 목적 주석은 용존·부유 성분 M의 수평 확산(horizontal diffusion) 수송과 N+1 시각 값 수정을 설명한다(19–22). `EFDC.PAR`·`EFDC.CMN`을 포함한다(26–27). CON1(LCM,KCM) 인수 배열을 선언한다(28). 수평 확산 플럭스(flux) 제목·구분·빈 주석(29–35). |
| 36–45 | 시작 시 6행 CALDIFF 루틴 안. `DO K=1,KC` (36)·`DO L=2,LA` (37)에서 남쪽 셀 LS=LSC(L)을 정한다(38). u 방향 플럭스와 v 방향 플럭스를 기존 값에 누적한다. 계수 0.5, 면 마스크 SUB/SVB, 면 폭 DYU/DXV, 수심 HU/HV, 이웃 AH 합, 농도 차, 격자 간격 역수 DXIU/DYIV를 사용하는 원문은 `FUHU(L,K)=FUHU(L,K)+0.5*SUB(L)*DYU(L)*HU(L)*(AH(L,K)+AH(L-1,K))*` (39); `&          (CON1(L-1,K)-CON1(L,K))*DXIU(L)` (40); `FVHU(L,K)=FVHU(L,K)+0.5*SVB(L)*DXV(L)*HV(L)*(AH(L,K)+AH(LS,K))*` (41); `&          (CON1(LS,K)-CON1(L,K))*DYIV(L)` (42). 두 루프 종료(43–44)와 주석(45). 이 블록에는 조건 분기나 CALL 문이 없다. |
| 46–49 | 시작 시 6행 CALDIFF 루틴 안. 구분·빈 주석(46–47), RETURN(48), END(49)로 루틴을 끝낸다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·36–44: 인수 ISTL과 M은 서브루틴 선언에 있다(6). 이 파일의 실행식에는 ISTL과 M 참조가 없다.
- 19–22·39–42: 목적 주석은 N+1 시각 농도 수정까지 설명한다. 실행 대입 대상은 FUHU와 FVHU이며 CON1에 값을 대입하는 문장은 이 파일에 없다.
