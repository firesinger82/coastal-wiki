---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/enpfte1.f
lines: 37
sha256: fa0042b624694118d52f10d8ec55bde973cd7e64b7c07460fa531dec2b185a25
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# enpfte1.f — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | ENPFTE1의 입출력과 4절점 배열을 선언한다. `等価節点力`은 등가절점력(equivalent nodal force), `歪`은 변형률(strain), `応力`은 응력(stress), `節点座標`는 절점좌표(nodal coordinate), `節点変位`는 절점변위(nodal displacement)다. `要素の構成節点番号`는 요소를 구성하는 절점 번호, `構成則マトリックス`는 구성행렬(constitutive matrix)이다. IGNL의 `微小変形`은 미소변형(small deformation), `大変形`은 대변형(large deformation)이다. 원문: `      SUBROUTINE ENPFTE1(FC,EPS,S,GRID,UG,NP,D,IGNL,ITO)` (1); 주석 원문 `!     FC   : OUT : 等価節点力` (3); 주석 원문 `!     EPS  : OUT : 歪` (4); 주석 원문 `!     S    : OUT : 応力` (5); 주석 원문 `!     GRID : IN  : 節点座標` (6); 주석 원문 `!     UG   : IN  : 節点変位` (7); 주석 원문 `!     NP   : IN  : 要素の構成節点番号` (8); 주석 원문 `!     D    : IN  : 構成則マトリックス` (9); 주석 원문 `!     IGNL : IN  : =0:微小変形, =1:大変形` (10); `      IMPLICIT REAL*8(A-H,O-Z)` (12); `      DIMENSION X0(3,4),U(3,4),GRID(3,*),UG(6,*),NP(4),DNDX(3,4)`<br>`     &         ,DUDX(3,3),BL(6,12),EPS0(6),EPS(6),DEPS(6),D(21),DS(6)`<br>`     &         ,S(6),BLTS(3,4),FC(3,4)` (14–16). |
| 18–29 | 시작 시 1행 ENPFTE1 루틴 안. NP로 좌표와 변위를 모은다. DERXTE1로 공간 미분과 DET를 얻고 MATML로 DUDX를 계산한다. BLMTX를 호출한다. 이전 EPS를 복사하고 GREEN 결과와의 차이 DEPS를 구한다. 원문: `      X0(:,:) = GRID(:,NP(:))` (18); `      U(:,:) = UG(1:3,NP(:))` (19); `      CALL DERXTE1(DNDX,DET,X0,ITO)` (21); `      CALL MATML(DUDX,2,DNDX,2,U,3,3,3,4)` (22); `      CALL BLMTX(BL,DNDX,DUDX,4,IGNL)` (24); `      EPS0(:) = EPS(:)` (26); `      CALL GREEN(EPS(:),DUDX,IGNL)` (27); `      DEPS(:) = EPS(:) - EPS0(:)` (28). |
| 30–37 | 시작 시 1행 ENPFTE1 루틴 안. MATML로 DS를 구하여 S에 더한다. 다음 MATML 결과 BLTS에 DET/6을 곱해 FC에 대입한다. 루틴 끝을 포함한다. 원문: `      CALL MATML(DS,2,D,1,DEPS,2,6,1,6)` (30); `      S(:) = S(:) + DS(:)` (31); `      CALL MATML(BLTS,2,BL,3,S,2,12,1,6)` (33); `      FC(:,:) = BLTS(:,:) * DET / 6.D0` (35); `      END` (37). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26–31: EPS의 이전 값과 S의 기존 값을 사용한다. 이 루틴 안에는 EPS·S의 초기값을 설정하는 문장이 없다.
