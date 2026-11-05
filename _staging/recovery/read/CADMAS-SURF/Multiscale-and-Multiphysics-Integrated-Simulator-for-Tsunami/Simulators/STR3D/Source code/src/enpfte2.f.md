---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/enpfte2.f
lines: 45
sha256: 5d5c0d53b131ab0058c1c929f30d6f965081fc9f4040c9c3d9b0273d3b430839
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# enpfte2.f — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | ENPFTE2의 인수·선언·적분표 포함과 좌표·변위 수집 및 절점력 초기화 구간이다. FC는 등가 절점력(equivalent nodal force)이다. 원문: `      SUBROUTINE ENPFTE2(FC,EPS,S,GRID,UG,NP,D,IGNL,ITO)` (1)； `!     FC   : OUT : 等価節点力` (3) (등가 절점력 출력이다.)； `!     EPS  : OUT : 歪` (4) (변형률 출력이다.)； `!     S    : OUT : 応力` (5) (응력 출력이다.)； `!     GRID : IN  : 節点座標` (6) (절점 좌표 입력이다.)； `!     UG   : IN  : 節点変位` (7) (절점 변위 입력이다.)； `!     NP   : IN  : 要素の構成節点番号` (8) (요소 구성 절점 번호 입력이다.)； `!     D    : IN  : 構成則マトリックス` (9) (구성법칙 행렬 입력이다.)； `!     IGNL : IN  : =0:微小変形, =1:大変形` (10) (0은 미소변형, 1은 대변형이다.)； `      IMPLICIT REAL*8(A-H,O-Z)` (12)； 연속문(14–16): `      DIMENSION X0(3,10),U(3,10),GRID(3,*),UG(6,*),NP(10),DNDX(3,10)` (14)； `     &         ,DUDX(3,3),BL(6,30),EPS0(6),EPS(6,5),DEPS(6),D(21,5)` (15)； `     &         ,DS(6),S(6,5),BLTS(3,10),FC(3,10)` (16)； `      INCLUDE 'gauss_te_5.h'` (18)； `      X0(:,:) = GRID(:,NP(:))` (20)； `      U(:,:) = UG(1:3,NP(:))` (21)； `      FC(:,:) = 0.` (23)。 |
| 25–45 | 시작 시 1행 ENPFTE2 루틴 안이다. 다섯 적분점에서 DERXTE2·MATML·BLMTX·GREEN을 호출한다. 변형률(strain) 증분으로 응력(stress)을 갱신한다. FC 누적식은 `BLTS(:,:) * DET * WG(I)`이다. 해석: DET는 행렬식이고 WG는 적분 가중치이다. 루프와 루틴이 끝난다. 원문: `      DO I = 1, 5` (25)； `        CALL DERXTE2(DNDX,DET,RLG(1,I),X0,ITO)` (27)； `        CALL MATML(DUDX,2,DNDX,2,U,3,3,3,10)` (28)； `        CALL BLMTX(BL,DNDX,DUDX,10,IGNL)` (30)； `        EPS0(:) = EPS(:,I)` (32)； `        CALL GREEN(EPS(:,I),DUDX,IGNL)` (33)； `        DEPS(:) = EPS(:,I) - EPS0(:)` (34)； `        CALL MATML(DS,2,D(1,I),1,DEPS,2,6,1,6)` (36)； `        S(:,I) = S(:,I) + DS(:)` (37)； `        CALL MATML(BLTS,2,BL,3,S(1,I),2,30,1,6)` (39)； `        FC(:,:) = FC(:,:) + BLTS(:,:) * DET * WG(I)` (41)； `      ENDDO` (43)； `      END` (45)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27·41: DET를 FC 누적식에 그대로 곱한다. 이 루틴에는 DET의 부호나 0 여부를 검사하는 조건이 없다.
