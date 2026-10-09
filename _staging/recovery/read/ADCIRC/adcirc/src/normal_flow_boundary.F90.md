---
file: models/ADCIRC/raw/source_code/adcirc/src/normal_flow_boundary.F90
lines: 106
sha256: 8b85a0a96b3731377ccc18470a3f51a47fbd1e472a0c5281e8d6739d7bbe8f2d
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# normal_flow_boundary.F90 — 판독 구간 기록

구간은 1행부터 106행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | 저작권·LGPL v3 이상·무보증 머리말(1–19). 파일/모듈 설명 주석은 법선 유량(normal flow), 즉 하천 경계 조건을 회전 좌표계(rotated coordinate system)로 변환한다고 적는다(21–23). 사용 범위 주석은 ICS=-20,-22 등이며 QNIN1/QNIN2에서 회전 유량 성분 및 경계 강제력(flux forcing) QN_R/QN2_R을 만든다고 설명한다(23–28). 경계 인덱스·회전 법선·격자 축척(mesh scaling)을 사용한다는 주석(30–31). |
| 33–43 | 빈 줄과 `module mod_normal_flow_boundary` 시작(33–34). implicit none·기본 private(36–38), 공개 함수 rotate_normal_flux(40), contains·빈 줄(42–43). |
| 44–74 | 시작 시 34행 mod_normal_flow_boundary 모듈 안. 함수 설명 주석은 LBCODEI(J)=2,12,22,32 경계 절점의 두 QN_IN 배열을 읽고 회전 법선 NX_R/NY_R 및 유량 성분 QX_R/QY_R을 계산한다고 적는다(45–51). 주석은 QN을 크기 NVEL의 inout 배열이라고 설명하고, Q/Q2를 MNVEL 크기로 할당하지 않았으면 즉시 반환한다고 적는다(53–57). 실제 선언은 `real(8) function rotate_normal_flux(ICS, IDX, Q) result(QROT)` (59). boundaries의 NBV/CSII/SIII/CSII_OLD/SIII_OLD, mesh의 SFMX/SFCX/SFCY/YCSFAC/RVELF, global의 IFSPROTS 사용(60–62). 입력은 INTEGER ICS/IDX와 REAL(8) 스칼라 Q이며 모두 intent(in)(66–68). 회전 유량·접선·회전 후 성분·2성분 벡터·법선 지역 실수 선언(70–73). |
| 75–87 | 시작 시 34행 모듈·59행 rotate_normal_flux 안. `select case (ICS)` (75)의 `case (20:24)` (76), 즉 20..24 분기. 법선 식은 `NX_R = CSII_OLD(IDX)/SFMX(NBV(IDX))` (78), NY_R=SIII_OLD(IDX) 복사(79). 접선 식은 `TAUX_R = -1.0d0*NY_R` (81), TAUY_R=NX_R 복사(82). 유량 성분 식은 `QY_R = Q/(((-1.0d0*TAUY_R)/TAUX_R)*NX_R + NY_R)` (85), `QX_R = -TAUY_R*QY_R/TAUX_R` (86). 주석·빈 줄을 포함한다(77·80·83–84·87). |
| 88–97 | 시작 시 34행 모듈·59행 함수·75행 select·76행 ICS=20..24 case 안. `if (IFSPROTS == 1) then` (88)이면 VO=[QX_R,QY_R] 구성(89), `VR = matmul(RVELF(1:2, 1:2, IDX), VO)` (90)로 2×2 행렬과 벡터를 곱한다. QX_ROT/QY_ROT에 VR(1)/VR(2) 복사(91–92). `else` (93)는 QX_ROT=QX_R·QY_ROT=QY_R 복사(94–95). 조건 종료·빈 줄(96–97). |
| 98–106 | 시작 시 34행 모듈·59행 함수·75행 select·76행 ICS=20..24 case 안이며 88행 IFSPROTS 조건 밖. 새 강제력 계산 주석(98), `QROT = SFCX(NBV(IDX))*QX_ROT*CSII(IDX) + SFCY(NBV(IDX))*QY_ROT*SIII(IDX)*YCSFAC(NBV(IDX))` (99). 같은 select의 병렬 `case default` (100)는 QROT=Q를 그대로 반환(101). select·함수·모듈 종료와 빈 줄(102–106). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23·75–76·100–101: 모듈 설명은 ICS=-20,-22 등에서만 사용한다고 적는다. 함수의 계산 case는 양수 20:24이다. 음수 ICS는 case default에서 입력 Q를 그대로 반환한다.
- 47–57·59·66–68: 함수 주석은 LBCODEI 검사·두 유량 배열·QN inout·Q/Q2 사전 할당과 미할당 시 즉시 반환을 설명한다. 실제 함수는 ICS/IDX/Q 세 스칼라 입력을 받는다. 함수 본문에는 LBCODEI·QN_IN·QN·Q2 참조나 할당 검사가 없다.
- 78·81·85–86: 식은 SFMX(NBV(IDX)), TAUX_R 및 QY_R 식의 전체 분모로 나눈다. 함수 본문에는 이 분모가 0인지 검사하는 조건이 없다. TAUX_R는 -1.0d0*NY_R이다.

