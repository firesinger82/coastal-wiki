---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/crh2stke.f
lines: 38
sha256: 93ed9bcc131c88f0e0361caa24e5b148fdccef0bec5785f2f101372e0e016dc0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# crh2stke.f — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–38 | 루틴·암시적 자료형·배열을 선언한다(1–4). 두 끝점과 접촉점 좌표를 모아 LENCD를 호출하고 TM=1-T를 계산한다(6–10). IEDQ=0이면 TM·T를 세 번 반복해 6개 계수를 만든다(12–19). ELSE에서는 TM+.25D0*T와 .25D0*T를 세 묶음으로 배치하여 12개 계수를 만든다(21–34). 분기·루틴을 닫는다(36–38). 원문: `      SUBROUTINE CRH2STKE(CRH,NS,IG,IEDQ,POS)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION X(3,3),POS(3,*),IG(2),CRH(*),V(3)` (4); `      X(:,1:2) = POS(:,IG(:))` (6); `      X(:,3) = POS(:,NS)` (7); `      CALL LENCD(T,V,X)` (9); `      TM = 1.D0 - T` (10); `      IF( IEDQ == 0 ) THEN` (12); `        CRH(1) = TM` (14); `        CRH(2) = T` (15); `        CRH(3) = TM` (16); `        CRH(4) = T` (17); `        CRH(5) = TM` (18); `        CRH(6) = T` (19); `      ELSE` (21); `        CRH(1)  = TM + .25D0 * T` (23); `        CRH(2)  = .25D0 * T` (24); `        CRH(3)  = .25D0 * T` (25); `        CRH(4)  = .25D0 * T` (26); `        CRH(5)  = TM + .25D0 * T` (27); `        CRH(6)  = .25D0 * T` (28); `        CRH(7)  = .25D0 * T` (29); `        CRH(8)  = .25D0 * T` (30); `        CRH(9)  = TM + .25D0 * T` (31); `        CRH(10) = .25D0 * T` (32); `        CRH(11) = .25D0 * T` (33); `        CRH(12) = .25D0 * T` (34). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
