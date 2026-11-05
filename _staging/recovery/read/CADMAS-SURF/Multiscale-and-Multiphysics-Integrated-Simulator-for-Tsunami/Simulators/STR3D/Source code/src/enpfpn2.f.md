---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/enpfpn2.f
lines: 47
sha256: 6013805b56ea33f436adeb86ce7a04f1afe06a0aee51642e9abdb7d7247b6521
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# enpfpn2.f — 판독 구간 기록

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | ENPFPN2의 입출력과 15절점·7×3 적분 배열을 선언한다. `等価節点力`은 등가절점력(equivalent nodal force), `歪`은 변형률(strain), `応力`은 응력(stress), `節点座標`는 절점좌표(nodal coordinate), `節点変位`는 절점변위(nodal displacement)다. `要素の構成節点番号`는 요소를 구성하는 절점 번호, `構成則マトリックス`는 구성행렬(constitutive matrix)이다. IGNL의 `微小変形`은 미소변형(small deformation), `大変形`은 대변형(large deformation)이다. gauss_pn_73.h를 INCLUDE한다. 포함 파일 내부는 이 파일의 판독 범위에 포함하지 않았다. 원문: `      SUBROUTINE ENPFPN2(FC,EPS,S,GRID,UG,NP,D,IGNL,ITO)` (1); 주석 원문 `!     FC   : OUT : 等価節点力` (3); 주석 원문 `!     EPS  : OUT : 歪` (4); 주석 원문 `!     S    : OUT : 応力` (5); 주석 원문 `!     GRID : IN  : 節点座標` (6); 주석 원문 `!     UG   : IN  : 節点変位` (7); 주석 원문 `!     NP   : IN  : 要素の構成節点番号` (8); 주석 원문 `!     D    : IN  : 構成則マトリックス` (9); 주석 원문 `!     IGNL : IN  : =0:微小変形, =1:大変形` (10); `      IMPLICIT REAL*8(A-H,O-Z)` (12); `      DIMENSION X0(3,15),U(3,15),GRID(3,*),UG(6,*),NP(15),D(21,7,3)`<br>`     &         ,DNDX(3,15),DUDX(3,3),BL(6,45),EPS0(6),EPS(6,7,3),DEPS(6)`<br>`     &         ,DS(6),S(6,7,3),BLTS(3,15),FC(3,15)` (14–16); `      INCLUDE 'gauss_pn_73.h'` (18). |
| 20–32 | 시작 시 1행 ENPFPN2 루틴 안. NP로 좌표와 변위를 모으고 FC를 0으로 초기화한다. J·I의 3×7 루프에서 DERXPN2와 MATML로 미분 배열을 계산하고 BLMTX를 호출한다. 원문: `      X0(:,:) = GRID(:,NP(:))` (20); `      U(:,:) = UG(1:3,NP(:))` (21); `      FC(:,:) = 0.` (23); `      DO J = 1, 3` (25); `        DO I = 1, 7` (26); `          CALL DERXPN2(DNDX,DET,15,X0,RG(I),SG(I),TG(J),ITO)` (28); `          CALL MATML(DUDX,2,DNDX,2,U,3,3,3,15)` (29); `          CALL BLMTX(BL,DNDX,DUDX,15,IGNL)` (31). |
| 33–47 | 시작 시 25행 `      DO J = 1, 3`과 26행 `        DO I = 1, 7` 안이다. I·J 루프는 각각 44·45행 ENDDO에서 닫힌다. 이전 EPS를 복사하고 GREEN 결과와의 차이 DEPS를 구한다. MATML로 DS를 계산하여 S에 더한다. 다음 MATML 결과 BLTS에 DET*WGI(I)*WGJ(J)를 곱하여 FC에 누적한다. 루프와 루틴 끝을 포함한다. 원문: `          EPS0(:) = EPS(:,I,J)` (33); `          CALL GREEN(EPS(:,I,J),DUDX,IGNL)` (34); `          DEPS(:) = EPS(:,I,J) - EPS0(:)` (35); `          CALL MATML(DS,2,D(1,I,J),1,DEPS,2,6,1,6)` (37); `          S(:,I,J) = S(:,I,J) + DS(:)` (38); `          CALL MATML(BLTS,2,BL,3,S(1,I,J),2,45,1,6)` (40); `          FC(:,:) = FC(:,:) + BLTS(:,:) * DET * WGI(I) * WGJ(J)` (42); `        ENDDO` (44); `      ENDDO` (45); `      END` (47). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 33–38: EPS의 이전 값과 S의 기존 값을 사용한다. 이 루틴 안에는 EPS·S의 초기값을 설정하는 문장이 없다.
