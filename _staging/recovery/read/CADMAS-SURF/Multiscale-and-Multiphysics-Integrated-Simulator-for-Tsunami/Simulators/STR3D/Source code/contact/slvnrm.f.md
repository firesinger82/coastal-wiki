---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/slvnrm.f
lines: 30
sha256: e030b5b8acbf2f4d7d22ed96ce314a301cabad359d4698fa5913748b232914c5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# slvnrm.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | 해석: SLVNRM는 종속 절점(slave node) 법선(normal) 배열 SNRM을 구성하는 루틴이다. 전체 절점 작업 배열 SNRMW를 0으로 초기화한다(9). POS와 SNRMW는 NNOD+NIGSF까지 선언한다(5–7). 원문: `      SUBROUTINE SLVNRM(SNRM,SNRMW,NNOD,NIGSF,NIELC,NINDC,IELC,INDC,POS)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). 연속문(5–7): `      DIMENSION IELC(3,NIELC),INDC(NINDC),SNRM(3,NINDC)` (5); `     &         ,SNRMW(3,NNOD+NIGSF),POS(3,NNOD+NIGSF),IG(3),V12(3)` (6); `     &         ,V13(3),EN(3)` (7). `      SNRMW(:,:) = 0.` (9). [11-04 전수 검증 정정] |
| 11–25 | 시작 시 1행 SLVNRM 루틴 안. 각 삼각형 면(face)의 두 변을 구하고 CROSS2(V13,V12,EN)을 호출한다(11–18). EN을 그 면의 세 절점 SNRMW에 누적한다(20–24). 원문: `      DO I = 1, NIELC` (11). `        IG(:) = IELC(:,I)` (13). `        V12(:) = POS(:,IG(2)) - POS(:,IG(1))` (15). `        V13(:) = POS(:,IG(3)) - POS(:,IG(1))` (16). `        CALL CROSS2(V13,V12,EN)` (18). `        DO J = 1, 3` (20). `          SNRMW(:,IG(J)) = SNRMW(:,IG(J)) + EN(:)` (21). `        ENDDO` (22). `      ENDDO` (24). |
| 26–30 | 시작 시 1행 SLVNRM 루틴 안. 각 INDC 절점의 누적 SNRMW를 DIRCOS에 전달하여 SNRM을 얻는다(26–28). END를 포함한다. 원문: `      DO I = 1, NINDC` (26). `        CALL DIRCOS(SNRM(1,I),SNRMW(1,INDC(I)),3)` (27). `      ENDDO` (28). `      END` (30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18·27: CROSS2 인수 순서는 V13,V12이며 누적값에 대한 DIRCOS 호출 앞에 영벡터 검사는 없다.
