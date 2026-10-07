---
file: models/EFDC/raw/source_code/EFDC-GVC/bal2t4.for
lines: 72
sha256: a2ccfead9548e5bcf782eb283fe5977d91bb94c445d823f1c52d2b9604c20a45
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# bal2t4.for — 판독 구간 기록

구간은 1행부터 72행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–42 | 구분 주석과 `SUBROUTINE BAL2T4` 입구(1–6). EFDC-FULL 1.0a·수정일·두 시각 단계(two time-level) 수지(balance) 추가 기록과 전역 운동량·에너지 수지 안내(8–22). `INCLUDE 'EFDC.PAR'` (26), `INCLUDE 'EFDC.CMN'` (27). `IF(ISDYNSTP.EQ.0)THEN` (31)이면 DELT=DT(32), `ELSE` (33)이면 DELT=DTDYN(34), 분기 종료(35). 운동량·에너지 소산(dissipation) 안내와 구분 주석(36–42). 포함 파일 내부는 이번 판독 대상이 아니다. |
| 43–54 | 시작 시 6행 BAL2T4 안. L=2..LA에서 LN=LNC(L)(43–44). 면적 DXYU·DXYV를 쓰는 예전 소산 식은 주석(45–48). 실행식은 `UUEOUT=UUEOUT+0.5*DELT*SPB(L)*DXYP(L)*(U(L,1)*TBX(L)` (49), `&       +U(L+1,1)*TBX(L+1)-U(L,KC)*TSX(L)-U(L+1,KC)*TSX(L+1))` (50), `VVEOUT=VVEOUT+0.5*DELT*SPB(L)*DXYP(L)*(V(L,1)*TBY(L)` (51), `&       +V(LN,1)*TBX(LN)-V(L,KC)*TSY(L)-V(LN,KC)*TSX(LN))` (52). 루프 종료·주석(53–54). |
| 55–72 | 시작 시 6행 BAL2T4 안. K=1..KS, L=2..LA에서 LN=LNC(L)(55–57). 수직 속도 차는 `DUTMP=0.5*( U(L,K+1)+U(L+1,K+1)-U(L,K)-U(L+1,K) )` (58), `DVTMP=0.5*( V(L,K+1)+V(LN,K+1)-V(L,K)-V(LN,K) )` (59). `UUEOUT=UUEOUT+DELT*SPB(L)*2.0*DXYP(L)*AV(L,K)` (60), `&      *( DUTMP*DUTMP )/(DZC(K+1)+DZC(K))` (61), `VVEOUT=VVEOUT+DELT*SPB(L)*2.0*DXYP(L)*AV(L,K)` (62), `&      *( DVTMP*DVTMP )/(DZC(K+1)+DZC(K))` (63). 부력(buoyancy) 에너지 식은 `BBEOUT=BBEOUT+DELT*SCB(L)*DXYP(L)*HP(L)` (64), `&      *GP*AB(L,K)*(B(L,K+1)-B(L,K))` (65). 루프 종료·구분 주석(66–70), `RETURN` (71), `END` (72). 외부 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 51–52: VVEOUT의 L 셀 항은 TBY·TSY를 사용한다. LN 셀 항은 TBX·TSX를 사용한다.
