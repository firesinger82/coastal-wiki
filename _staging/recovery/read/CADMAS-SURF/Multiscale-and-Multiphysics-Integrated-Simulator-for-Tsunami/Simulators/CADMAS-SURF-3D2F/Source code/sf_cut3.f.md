---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_cut3.f
lines: 46
sha256: fcd7eaf808e83d096ee3dcf4cb0ed0dd40f3cddca3d5388317ee9db5c8e08ad2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_cut3.f — 판독 구간 기록

구간은 1행부터 46행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–46 | SF_CUT3 선언과 사면체(tetrahedron) 작업 배열 범위(1–6). DX·DY·DZ와 EPSV를 계산한다(8–12). 해석: EPSV는 격자 부피에 비례하는 허용값이다. VV·SX·SY·SZ를 0으로 시작한다(14–17). SF_CUT3X를 X·Y·Z의 하한·상한 순서로 호출하며 N1부터 N6까지 결과 수를 중첩 순회한다(19–44). 마지막 사면체의 SF_TETVOL 결과를 VV에 누적한다(37–38). 원문: `      SUBROUTINE SF_CUT3(VV,SX,SY,SZ,P0,XG,YG,ZG,EPS)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>연속문: `      DIMENSION P0(3,4),XG(2),YG(2),ZG(2),P1(3,4,3),P2(3,4,3),P3(3,4,3)` (5); `     &         ,P4(3,4,3),P5(3,4,3),P6(3,4,3)` (6)<br>`      DX = XG(2) - XG(1)` (8)<br>`      DY = YG(2) - YG(1)` (9)<br>`      DZ = ZG(2) - ZG(1)` (10)<br>`      EPSV = DX * DY * DZ * 1.D-9` (12)<br>`      VV = 0.` (14)<br>`      SX = 0.` (15)<br>`      SY = 0.` (16)<br>`      SZ = 0.` (17)<br>연속문: `      CALL SF_CUT3X(N1,P1(1,1,1),P1(1,1,2),P1(1,1,3),SX,P0,XG(1),YG,ZG` (19); `     &             ,EPS,EPSV,1,2,3,1)` (20)<br>`      DO I = 1, N1` (21)<br>연속문: `        CALL SF_CUT3X(N2,P2(1,1,1),P2(1,1,2),P2(1,1,3),SX,P1(1,1,I)` (22); `     &               ,XG(2),YG,ZG,EPS,EPSV,1,2,3,2)` (23)<br>`        DO J = 1, N2` (24)<br>연속문: `          CALL SF_CUT3X(N3,P3(1,1,1),P3(1,1,2),P3(1,1,3),SY,P2(1,1,J)` (25); `     &                 ,YG(1),ZG,XG,EPS,EPSV,2,3,1,1)` (26)<br>`          DO K = 1, N3` (27)<br>연속문: `            CALL SF_CUT3X(N4,P4(1,1,1),P4(1,1,2),P4(1,1,3),SY,P3(1,1,K)` (28); `     &                   ,YG(2),ZG,XG,EPS,EPSV,2,3,1,2)` (29)<br>`            DO L = 1, N4` (30)<br>연속문: `              CALL SF_CUT3X(N5,P5(1,1,1),P5(1,1,2),P5(1,1,3),SZ` (31); `     &                     ,P4(1,1,L),ZG(1),XG,YG,EPS,EPSV,3,1,2,1)` (32)<br>`              DO M = 1, N5` (33)<br>연속문: `                CALL SF_CUT3X(N6,P6(1,1,1),P6(1,1,2),P6(1,1,3),SZ` (34); `     &                       ,P5(1,1,M),ZG(2),XG,YG,EPS,EPSV,3,1,2,2)` (35)<br>`                DO N = 1, N6` (36)<br>`                  CALL SF_TETVOL(P6(1,1,N),V)` (37)<br>`                  VV = VV + V` (38)<br>`                ENDDO` (39)<br>`              ENDDO` (40)<br>`            ENDDO` (41)<br>`          ENDDO` (42)<br>`        ENDDO` (43)<br>`      ENDDO` (44)<br>`      END` (46) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
