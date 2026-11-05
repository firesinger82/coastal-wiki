---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/enpfpn1.f
lines: 62
sha256: 7711f1a34c6d4ee3102e363300913f092bd0b021a3c0ca94fb71368730104a83
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# enpfpn1.f — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | ENPFPN1의 입출력과 6절점·3×2 적분 배열을 선언한다. `等価節点力`은 등가절점력(equivalent nodal force), `歪`은 변형률(strain), `応力`은 응력(stress), `節点座標`는 절점좌표(nodal coordinate), `節点変位`는 절점변위(nodal displacement)다. `要素の構成節点番号`는 요소를 구성하는 절점 번호, `構成則マトリックス`는 구성행렬(constitutive matrix)이다. IGNL의 `微小変形`은 미소변형(small deformation), `大変形`은 대변형(large deformation)이다. gauss_pn_32.h를 INCLUDE한다. 포함 파일 내부는 이 파일의 판독 범위에 포함하지 않았다. LCCPN1과 TRPN1S를 차례로 호출한다. 해석: LCCPN1은 국소좌표 정보를 구성한다. 원문: `      SUBROUTINE ENPFPN1(FCG,EPS,S,GRID,UG,NP,D,IGNL,ITO)` (1); 주석 원문 `!     FCG  : OUT : 等価節点力` (3); 주석 원문 `!     EPS  : OUT : 歪` (4); 주석 원문 `!     S    : OUT : 応力` (5); 주석 원문 `!     GRID : IN  : 節点座標` (6); 주석 원문 `!     UG   : IN  : 節点変位` (7); 주석 원문 `!     NP   : IN  : 要素の構成節点番号` (8); 주석 원문 `!     D    : IN  : 構成則マトリックス` (9); 주석 원문 `!     IGNL : IN  : =0:微小変形, =1:大変形` (10); `      IMPLICIT REAL*8(A-H,O-Z)` (12); `      DIMENSION TE(3,3),X0(3,6),U(3,6),GRID(3,*),UG(6,*),NP(6),TR(6,6)`<br>`     &         ,DNDX(3,6,3),DUDX(3,3,3),BLS(2,18,3),EPSS(2,3),BL(6,18)`<br>`     &         ,D(21,3,2),EPS0(6),EPS(6,3,2),DEPS(6),DS(6),S(6,3,2)`<br>`     &         ,BLTS(3,6),FC(3,6),FCG(3,6)` (14–17); `      INCLUDE 'gauss_pn_32.h'` (19); `      CALL LCCPN1(TE,X0,U,GRID,UG,NP)` (21); `      CALL TRPN1S(TR,X0,ITO)` (23). [11-04 전수 검증 정정] |
| 25–35 | 시작 시 1행 ENPFPN1 루틴 안. T=0인 평면의 3점에서 DERXPN2·MATML을 호출해 DNDX·DUDX를 구한다. BLMPN1S와 GREEN_PN1S를 호출한다. FC를 0으로 초기화한다. BLMPN1S의 BLS가 BL의 5·6행 성분이라는 주석은 `blmpn1s.f:3–4`에 있다. 해석: BLS와 EPSS의 두 성분은 전단 성분에 해당한다. 원문: `      DO I = 1, 3` (25); `        CALL DERXPN2(DNDX(1,1,I),DET,6,X0,RG(I),SG(I),0.D0,ITO)` (26); `        CALL MATML(DUDX(1,1,I),2,DNDX(1,1,I),2,U,3,3,3,6)` (27); `      ENDDO` (28); `      CALL BLMPN1S(BLS,DNDX,DUDX,TR,IGNL)` (30); `      CALL GREEN_PN1S(EPSS,DUDX,TR,IGNL)` (32); `      FC(:,:) = 0.` (34). [11-04 전수 검증 정정] |
| 36–49 | 시작 시 1행 ENPFPN1 루틴 안. J·I의 2×3 루프에서 DERXPN2·MATML·BLMPN1을 호출한다. BL의 5–6행을 BLS로 바꾼다. 이전 EPS를 복사하고 GREEN_PN1 결과의 5–6성분을 EPSS로 바꾼 뒤 DEPS를 계산한다. 원문: `      DO J = 1, 2` (36); `        DO I = 1, 3` (37); `          CALL DERXPN2(DNDX,DET,6,X0,RG(I),SG(I),TG(J),ITO)` (39); `          CALL MATML(DUDX,2,DNDX,2,U,3,3,3,6)` (40); `          CALL BLMPN1(BL,DNDX,DUDX,IGNL)` (42); `          BL(5:6,:) = BLS(:,:,I)` (43); `          EPS0(:) = EPS(:,I,J)` (45); `          CALL GREEN_PN1(EPS(:,I,J),DUDX,IGNL)` (46); `          EPS(5:6,I,J) = EPSS(:,I)` (47); `          DEPS(:) = EPS(:,I,J) - EPS0(:)` (48). |
| 50–62 | 시작 시 36행 `      DO J = 1, 2`와 37행 `        DO I = 1, 3` 안이다. I·J 루프는 각각 57·58행 ENDDO에서 닫힌다. MATML의 DS를 S에 누적한다. 다음 MATML 결과 BLTS에 DET/6을 곱하여 FC에 누적한다. 두 루프 뒤 MATML에 TE와 FC를 전달하여 FCG를 계산한다. 루틴 끝을 포함한다. 원문: `          CALL MATML(DS,2,D(1,I,J),1,DEPS,2,6,1,6)` (50); `          S(:,I,J) = S(:,I,J) + DS(:)` (51); `          CALL MATML(BLTS,2,BL,3,S(1,I,J),2,18,1,6)` (53); `          FC(:,:) = FC(:,:) + BLTS(:,:) * DET / 6.D0` (55); `        ENDDO` (57); `      ENDDO` (58); `      CALL MATML(FCG,2,TE,3,FC,2,3,6,3)` (60); `      END` (62). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 39–40: DNDX·DUDX는 3차원으로 선언되어 있지만 이 위치의 DERXPN2·MATML에는 배열 전체 이름을 전달한다. 앞의 26–27행은 세 번째 첨자 I를 명시한 시작 원소를 전달한다.
- 55: 절점력 누적 계수는 DET/6.D0으로 고정되어 있다. 이 문장에는 WGI·WGJ를 곱하지 않는다.
