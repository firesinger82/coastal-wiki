---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/cntrfc.f
lines: 48
sha256: 490fbf70312ab5066b34daca0519dd9a85bfa0dd5c0034c04fbafc0fa5df427f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cntrfc.f — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | CNTRFC는 MPC_WORK를 사용하고 배정밀도(double precision)와 배열 범위를 선언한다(1–7). INDC의 역대응 INDCR을 구축하고 RFCI를 0으로 초기화한다(9–15). MPC_WORK 내부는 판독하지 않았다. 원문(연속 표시는 같은 문장의 이어지는 행이다): `      SUBROUTINE CNTRFC(RFCI,NNOD,NINDC,NIDEP,NRANK,FTI,FTO,INDC,IRANK` (1); `     &                 ,INDCR)` (2); `      USE MPC_WORK` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      DIMENSION IRANK(NINDC),RFCI(6,NNOD),FTI(6,NNOD),FTO(6,NNOD)` (6); `     &         ,INDCR(NNOD),INDC(NINDC)` (7); `      INDCR(:) = 0` (9); `      DO I = 1, NINDC` (11); `        INDCR( INDC(I) ) = I` (12); `      ENDDO` (13); `      RFCI(:,:) = 0.D0` (15). |
| 17–48 | 시작 시 1–2행 CNTRFC 루틴 안. IR을 NRANK부터 1까지 역순으로 처리한다(17). NDS와 IFS는 각각 IDEP(1,I)와 IDEP(2,I)이다(21–22). `IRANK(INDCR(NDS)) /= IR`이면 해당 I를 건너뛴다(24). RFCI(IFS,NDS)를 26행 식으로 갱신한다. JS·JE는 IDX(1,I)·IDX(2,I)이다(28–29). NDM·IFM은 IRH(1,J)·IRH(2,J)이다(33–34). `NDM == NDS`이면 RFCI(IFM,NDM)에 음의 곱을 대입한다(36–37). 나머지 분기는 기존 값에서 곱을 뺀다(38–39). 원문(연속 표시는 같은 문장의 이어지는 행이다): `      DO IR = NRANK, 1, -1` (17); `        DO I = 1, NIDEP` (19); `          NDS = IDEP(1,I)` (21); `          IFS = IDEP(2,I)` (22); `          IF( IRANK(INDCR(NDS)) /= IR ) CYCLE` (24); `          RFCI(IFS,NDS) = FTI(IFS,NDS) - FTO(IFS,NDS) - RFCI(IFS,NDS)` (26); `          JS = IDX(1,I)` (28); `          JE = IDX(2,I)` (29); `          DO J = JS, JE` (31); `            NDM = IRH(1,J)` (33); `            IFM = IRH(2,J)` (34); `            IF( NDM == NDS ) THEN` (36); `              RFCI(IFM,NDM) = -CRH(J) * RFCI(IFS,NDS)` (37); `            ELSE` (38); `              RFCI(IFM,NDM) = RFCI(IFM,NDM) - CRH(J) * RFCI(IFS,NDS)` (39); `            ENDIF` (40); `          ENDDO` (42); `        ENDDO` (44); `      ENDDO` (46); `      END` (48). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–13·24: INDCR은 INDC에 있는 노드만 양수 인덱스를 받는다. NDS를 사용하는 IRANK(INDCR(NDS)) 앞에는 INDCR(NDS)>0 검사가 이 루틴에 없다.
