---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/rmpccal.f
lines: 20
sha256: 8b7e6e6efb2e07b8cd40fa6614953af320a459c5ab72bc8f45b4178ad63c47b3
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# rmpccal.f — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | RMPCCAL은 MPC_WORK 모듈을 사용한다(4). IDL과 COLR의 SIZE로 NIDEP,NSIZ_R을 얻는다(9–10). 인수·암시적 형 및 배열 선언을 포함한다. 원문: 연속문(1–2): `      SUBROUTINE RMPCCAL(RMPC,NINDC,ISLV,INDC,IEDG,IELC,IVRQ,IEDQ,IFCQ` (1); `     &                  ,POS,ITO)` (2). `      USE MPC_WORK` (4). `      IMPLICIT REAL*8(A-H,O-Z)` (5). 연속문(6–7): `      DIMENSION ISLV(2,NINDC),POS(3,*),IELC(3,*),INDC(NINDC),IEDG(6,*)` (6); `     &         ,IVRQ(*),IEDQ(*),IFCQ(*),RMPC(*)` (7). `      NIDEP = SIZE(IDL)` (9). `      NSIZ_R = SIZE(COLR)` (10). |
| 12–20 | 시작 시 1–2행 RMPCCAL 루틴 안. CRH2SET으로 CRH를 구성한다(12). B 전체와 RMPC의 1:NSIZ_R 구간을 0으로 초기화한 뒤 MPCSLV에 RMPC를 우변 배열로 전달한다(14–18). END를 포함한다. 원문: `      CALL CRH2SET(CRH,NINDC,ISLV,INDC,IEDG,IELC,IVRQ,IEDQ,IFCQ,POS,IRH)` (12). `      B(:) = 0.` (14). `      RMPC(1:NSIZ_R) = 0.` (15). 연속문(17–18): `      CALL MPCSLV(NIDEP,B,RMPC,IDL,ROWL,COLL,ROWR,COLR,CIDP,IDX,IFRH,CRH` (17); `     &           ,ITO)` (18). `      END` (20). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
