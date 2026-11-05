---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/module/mpc_work.f90
lines: 35
sha256: 23f1da184973ab38c7eddb0358e385aa368eb8753a07931f6027899fcc7023f4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mpc_work.f90 — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | 해석: MPC_WORK 모듈은 ISLVG/NS/NM/ICORR, 종속 인덱스 IDEP/CIDP, IDX/IRH/IFRH/CRH/INDP/IDL, 행·열 인덱스 배열, 실수 벡터 B와 정수 작업 배열 IDWK를 할당 가능 배열로 선언한다(1–35). 모든 배열은 지연 크기이고 이 모듈에는 실행문이 없다. 원문(연속행은 앞 문장에 이어짐): `MODULE MPC_WORK` (1); `  INTEGER, ALLOCATABLE :: ISLVG(:,:)` (3); `  INTEGER, ALLOCATABLE :: NS(:)` (4); `  INTEGER, ALLOCATABLE :: NM(:)` (5); `  INTEGER, ALLOCATABLE :: ICORR(:)` (6); `  INTEGER, ALLOCATABLE :: IDEP(:,:)` (7); `  REAL(8), ALLOCATABLE :: CIDP(:)` (8); `  INTEGER, ALLOCATABLE :: IDX(:,:)` (9); `  INTEGER, ALLOCATABLE :: IRH(:,:)` (10); `  INTEGER, ALLOCATABLE :: IFRH(:)` (11); `  REAL(8), ALLOCATABLE :: CRH(:)` (12); `  INTEGER, ALLOCATABLE :: INDP(:,:)` (13); `  INTEGER, ALLOCATABLE :: IDL(:)` (14); `  INTEGER, ALLOCATABLE :: ROWL(:)` (15); `  INTEGER, ALLOCATABLE :: ROWR(:)` (16); `  INTEGER, ALLOCATABLE :: COLL(:)` (17); `  INTEGER, ALLOCATABLE :: COLR(:)` (18); `  INTEGER, ALLOCATABLE :: COLL0(:)` (19); `  INTEGER, ALLOCATABLE :: COLR0(:)` (20); `  INTEGER, ALLOCATABLE :: RWL2(:)` (21); `  INTEGER, ALLOCATABLE :: CLL2(:)` (22); `  INTEGER, ALLOCATABLE :: CLL20(:)` (23); `  INTEGER, ALLOCATABLE :: RWR2(:)` (24); `  INTEGER, ALLOCATABLE :: CLR2(:)` (25); `  INTEGER, ALLOCATABLE :: CLR20(:)` (26); `  INTEGER, ALLOCATABLE :: RWR3(:)` (27); `  INTEGER, ALLOCATABLE :: CLR3(:)` (28); `  INTEGER, ALLOCATABLE :: CLR30(:)` (29); `  INTEGER, ALLOCATABLE :: RWR4(:)` (30); `  INTEGER, ALLOCATABLE :: CLR4(:)` (31); `  REAL(8), ALLOCATABLE :: B(:)` (32); `  INTEGER, ALLOCATABLE :: IDWK(:)` (33); `END MODULE MPC_WORK` (35) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1–35: 이 모듈에는 IMPLICIT NONE 문이 없다. 모든 선언 변수는 명시적으로 INTEGER 또는 REAL(8) 형을 갖는다.
