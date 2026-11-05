---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/enpfbm.f
lines: 46
sha256: b70e12d24b735014cf7d1112f11389007746087fb6a330f379d60323e9461932
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# enpfbm.f — 판독 구간 기록

구간은 1행부터 46행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | ENPFBM의 암시적 형과 배열 크기를 선언한다. 해석: 이 배열들은 두 절점과 3×3 단면 적분에 대응한다. gauss_ln_3.h를 INCLUDE한다. 포함 파일 내부는 이 파일의 판독 범위에 포함하지 않았다. LCCBM과 DERXBM0를 차례로 호출한다. 해석: LCCBM은 국소좌표 정보를 구성한다. FC를 0으로 초기화한다. 원문: `      SUBROUTINE ENPFBM(FCG,EPS,S,GRID,UG,VG,NP,D1,D2,V,D,IGNL)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION TE(3,3),U(3,2),VS(3,2),VT(3,2),VST(3,2),VTT(3,2)`<br>`     &         ,AS(3,3,2),AT(3,3,2),GRID(3,*),UG(6,*),VG(3,2,2),NP(2)`<br>`     &         ,V(3),BX(3,12),BY(3,12),BZ(3,12),UX(3),UY(3),UZ(3)`<br>`     &         ,B(3,12),EPS0(3),EPS(3,3,3),DEPS(3),DS(3),D(6,3,3)`<br>`     &         ,S(3,3,3),BTS(6,2),FC(6,2),FCG(6,2)` (5–9); `      INCLUDE 'gauss_ln_3.h'` (11); `      CALL LCCBM(RL,TE,U,VST,VTT,AS,AT,VS,VT,GRID,UG,VG,NP,V,IGNL)` (13); `      CALL DERXBM0(BY,BZ,UY,UZ,VS,VT,AS,AT)` (15); `      FC(:,:) = 0.` (17). [11-04 전수 검증 정정] |
| 19–33 | 시작 시 1행 ENPFBM 루틴 안. I·J의 3×3 루프에서 좌표와 가중치(weight)를 구한다. DERXBM·BLMBM을 호출한다. 이전 EPS를 복사한 뒤 GREEN_BM을 호출한다. 호출 뒤 EPS와 EPS0의 차이 DEPS를 계산한다. 해석: EPS는 변형률이다. 원문: `      DO I = 1, 3` (19); `      DO J = 1, 3` (20); `        SG = XG(I,3)` (22); `        TG = XG(J,3)` (23); `        WGT = WG(I,3)*WG(J,3)` (24); `        CALL DERXBM(BX,UX,SG,TG,RL,D1,D2,U,VS,VT,AS,AT)` (26); `        CALL BLMBM(B,BX,BY,BZ,UX,UY,UZ,IGNL)` (28); `        EPS0(:) = EPS(:,I,J)` (30); `        CALL GREEN_BM(EPS(1,I,J),UX,UY,UZ,IGNL)` (31); `        DEPS(:) = EPS(:,I,J) - EPS0(:)` (32). [11-04 전수 검증 정정] |
| 34–46 | 시작 시 19행 `      DO I = 1, 3`과 20행 `      DO J = 1, 3` 안이다. J·I 루프는 각각 41·42행 ENDDO에서 닫힌다. MATML 호출 뒤 DS를 S에 더한다. 두 번째 MATML 호출 뒤 BTS에 WGT*D1*D2*RL*.25D0을 곱하여 FC에 더한다. 해석: DS는 응력 증분이며 D1·D2·RL은 치수이다. 두 루프 종료 후 MATML로 FCG를 구성한다. 루틴 끝을 포함한다. 원문: `        CALL MATML(DS,2,D(1,I,J),1,DEPS,2,3,1,3)` (34); `        S(:,I,J) = S(:,I,J) + DS(:)` (35); `        CALL MATML(BTS,2,B,3,S(1,I,J),2,12,1,3)` (37); `        FC(:,:) = FC(:,:) + BTS(:,:) * WGT * D1 * D2 * RL * .25D0` (39); `      ENDDO` (41); `      ENDDO` (42); `      CALL MATML(FCG,2,TE,3,FC,2,3,4,3)` (44); `      END` (46). [11-04 전수 검증 보완] [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8·19–24·39: I·J 루프 범위는 각각 1,3이다. FC 누적식에는 WGT*D1*D2*RL*.25D0이 있다. 해석: 이 루프는 3×3 단면 적분이며 해당 곱은 체적 적분 계수이다. [11-04 전수 검증 정정]
