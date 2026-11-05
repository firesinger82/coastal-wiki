---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/enpfhx2.f
lines: 54
sha256: 724abb7849c54dd289953e56aa1ea136497fa1a7c7dcf42283ee21c5e33ea877
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# enpfhx2.f — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | ENPFHX2의 입출력과 20절점·3×3×3 적분 배열을 선언한다. `等価節点力`은 등가절점력(equivalent nodal force), `歪`은 변형률(strain), `応力`은 응력(stress), `節点座標`는 절점좌표(nodal coordinate), `節点変位`는 절점변위(nodal displacement)다. `要素の構成節点番号`는 요소를 구성하는 절점 번호, `構成則マトリックス`는 구성행렬(constitutive matrix)이다. IGNL의 `微小変形`은 미소변형(small deformation), `大変形`은 대변형(large deformation)이다. gauss_ln_3.h를 INCLUDE한다. 포함 파일 내부는 이 파일의 판독 범위에 포함하지 않았다. 원문: `      SUBROUTINE ENPFHX2(FC,EPS,S,GRID,UG,NP,D,IGNL,ITO)` (1); 주석 원문 `!     FC   : OUT : 等価節点力` (3); 주석 원문 `!     EPS  : OUT : 歪` (4); 주석 원문 `!     S    : OUT : 応力` (5); 주석 원문 `!     GRID : IN  : 節点座標` (6); 주석 원문 `!     UG   : IN  : 節点変位` (7); 주석 원문 `!     NP   : IN  : 要素の構成節点番号` (8); 주석 원문 `!     D    : IN  : 構成則マトリックス` (9); 주석 원문 `!     IGNL : IN  : =0:微小変形, =1:大変形` (10); `      IMPLICIT REAL*8(A-H,O-Z)` (12); `      DIMENSION X0(3,20),U(3,20),GRID(3,*),UG(6,*),NP(20),D(21,3,3,3)`<br>`     &         ,DNDX(3,20),DUDX(3,3),BL(6,60),EPS0(6),EPS(6,3,3,3)`<br>`     &         ,DEPS(6),DS(6),S(6,3,3,3),BLTS(3,20),FC(3,20)` (14–16); `      INCLUDE 'gauss_ln_3.h'` (18). |
| 20–38 | 시작 시 1행 ENPFHX2 루틴 안. NP로 좌표와 변위를 모으고 FC를 0으로 초기화한다. I·J·K 루프에서 적분 좌표와 가중치(weight)를 계산한다. DERXHX2로 공간 미분을 구하고 MATML로 DUDX를 구성한 뒤 BLMTX를 호출한다. 원문: `      X0(:,:) = GRID(:,NP(:))` (20); `      U(:,:) = UG(1:3,NP(:))` (21); `      FC(:,:) = 0.` (23); `      DO I = 1, 3` (25); `      DO J = 1, 3` (26); `      DO K = 1, 3` (27); `        XG1 = XG(I,3)` (29); `        XG2 = XG(J,3)` (30); `        XG3 = XG(K,3)` (31); `        WGT = WG(I,3)*WG(J,3)*WG(K,3)` (32); `        CALL DERXHX2(DNDX,DET,XG1,XG2,XG3,X0,20,ITO)` (34); `        CALL MATML(DUDX,2,DNDX,2,U,3,3,3,20)` (35); `        CALL BLMTX(BL,DNDX,DUDX,20,IGNL)` (37). |
| 39–54 | 시작 시 25행 `      DO I = 1, 3`, 26행 `      DO J = 1, 3`, 27행 `      DO K = 1, 3` 안이다. K·J·I 루프는 각각 50·51·52행 ENDDO에서 닫힌다. 이전 EPS를 복사하고 GREEN으로 새 EPS를 얻어 DEPS를 계산한다. MATML 결과 DS를 S에 더하고 다음 MATML 결과 BLTS에 DET*WGT를 곱해 FC에 누적한다. 루프와 루틴 끝을 포함한다. 원문: `        EPS0(:) = EPS(:,I,J,K)` (39); `        CALL GREEN(EPS(:,I,J,K),DUDX,IGNL)` (40); `        DEPS(:) = EPS(:,I,J,K) - EPS0(:)` (41); `        CALL MATML(DS,2,D(1,I,J,K),1,DEPS,2,6,1,6)` (43); `        S(:,I,J,K) = S(:,I,J,K) + DS(:)` (44); `        CALL MATML(BLTS,2,BL,3,S(1,I,J,K),2,60,1,6)` (46); `        FC(:,:) = FC(:,:) + BLTS(:,:) * DET * WGT` (48); `      ENDDO` (50); `      ENDDO` (51); `      ENDDO` (52); `      END` (54). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 39–44: EPS의 이전 값을 EPS0에 복사하고 S의 기존 값에 DS를 더한다. 이 루틴 안에는 EPS·S의 초기값을 설정하는 문장이 없다.
