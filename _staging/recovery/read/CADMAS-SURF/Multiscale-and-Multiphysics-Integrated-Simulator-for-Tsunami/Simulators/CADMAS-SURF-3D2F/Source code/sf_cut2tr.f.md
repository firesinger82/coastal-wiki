---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_cut2tr.f
lines: 38
sha256: 53fc197d5e93b0a654968381df328da80702344053f0237bba5e668202da1da8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_cut2tr.f — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–38 | SF_CUT2TR 선언과 배열 범위(1–6). SF_S34의 S로 EPSA=-S*1.D-9를 정하고 SF_TRM2로 변환 자료를 만든다(8–11). SS=0부터 SF_CUT2X를 세 차례 호출한다(13–28). N1·N2·N3 결과 루프 중 앞 두 단계 뒤에는 SF_TRNS2를 호출한다(17–29). 해석: SF_TRM2와 SF_TRNS2는 좌표 변환 자료 생성과 좌표 변환을 수행한다. 마지막 삼각형의 SF_S34 결과를 SS에 누적한다(30–31). 원문: `      SUBROUTINE SF_CUT2TR(SS,P0,X,EPS)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>연속문: `      DIMENSION P0(2,3),P1(2,3,2),P2(2,3,2),P3(2,3,2),TR(4,2),X0(2,2)` (5); `     &         ,X(2,3)` (6)<br>`      CALL SF_S34(S,X,3)` (8)<br>`      EPSA = -S * 1.D-9` (9)<br>`      CALL SF_TRM2(TR,X0,X)` (11)<br>`      SS = 0.` (13)<br>`      CALL SF_CUT2X(N1,P1(1,1,1),P1(1,1,2),P0,0.D0,EPS,EPSA,1,2,1)` (15)<br>`      DO I = 1, N1` (17)<br>`        CALL SF_TRNS2(P1(1,1,I),X0(1,1),TR(1,1))` (19)<br>연속문: `        CALL SF_CUT2X(N2,P2(1,1,1),P2(1,1,2),P1(1,1,I),0.D0,EPS,EPSA,1` (21); `     &               ,2,1)` (22)<br>`        DO J = 1, N2` (23)<br>`          CALL SF_TRNS2(P2(1,1,J),X0(1,2),TR(1,2))` (25)<br>연속문: `          CALL SF_CUT2X(N3,P3(1,1,1),P3(1,1,2),P2(1,1,J),0.D0,EPS,EPSA` (27); `     &                 ,1,2,1)` (28)<br>`          DO K = 1, N3` (29)<br>`            CALL SF_S34(S,P3(1,1,K),3)` (30)<br>`            SS = SS + S` (31)<br>`          ENDDO` (32)<br>`        ENDDO` (34)<br>`      ENDDO` (36)<br>`      END` (38) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
