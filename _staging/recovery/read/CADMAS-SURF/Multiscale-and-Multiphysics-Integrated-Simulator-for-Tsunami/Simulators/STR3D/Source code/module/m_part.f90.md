---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/module/m_part.f90
lines: 75
sha256: 0840d3cb928b6d261722b881c522da5d62236bf5f49b686373fea038eface430
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# m_part.f90 — 판독 구간 기록

구간은 1행부터 75행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | M_PART 모듈을 선언한다(1). 암묵 형 선언을 금지한다(3). 해석: 분할별 내부·외부 절점 수와 요소·면·IDZ 수, 절점·요소 연결표 및 작업용 가져오기(import)·내보내기(export) 통신표를 할당 가능 배열(allocatable array)로 선언한다(5–22). 해석: NPE/NIMP/NEXP와 현재 분할 통신 인덱스 배열을 선언한다(24–30). 원문(연속행은 앞 문장에 이어짐): `MODULE M_PART` (1); `  IMPLICIT NONE` (3); `  INTEGER, ALLOCATABLE :: NN_INT(:)` (5); `  INTEGER, ALLOCATABLE :: NN_EXT(:)` (6); `  INTEGER, ALLOCATABLE :: NE(:)` (7); `  INTEGER, ALLOCATABLE :: NPF(:)` (8); `  INTEGER, ALLOCATABLE :: NDZ(:)` (9); `  INTEGER, ALLOCATABLE :: NOD(:,:)` (11); `  INTEGER, ALLOCATABLE :: IEL(:,:)` (12); `  INTEGER, ALLOCATABLE :: IPF(:,:)` (13); `  INTEGER, ALLOCATABLE :: IDZ(:,:)` (14); `  INTEGER, ALLOCATABLE :: NPEW(:),NIMPW(:),NEXPW(:)` (16); `  INTEGER, ALLOCATABLE :: IPEW(:,:)` (18); `  INTEGER, ALLOCATABLE :: IDXIMPW(:,:,:)` (19); `  INTEGER, ALLOCATABLE :: NODIMPW(:,:)` (20); `  INTEGER, ALLOCATABLE :: IDXEXPW(:,:,:)` (21); `  INTEGER, ALLOCATABLE :: NODEXPW(:,:)` (22); `  INTEGER :: NPE,NIMP,NEXP` (24); `  INTEGER, ALLOCATABLE :: IPE(:)` (26); `  INTEGER, ALLOCATABLE :: IDXIMP(:,:)` (27); `  INTEGER, ALLOCATABLE :: NODIMP(:)` (28); `  INTEGER, ALLOCATABLE :: IDXEXP(:,:)` (29); `  INTEGER, ALLOCATABLE :: NODEXP(:)` (30) [11-04 전수 검증 정정] |
| 31–58 | 시작 시 1행 M_PART 모듈 안. 해석: NG부터 NIBT까지의 개수와 NODG부터 IBT까지의 연결표, NODP/IELCP/INDCP/IEDGP 및 NODC/NODGC/IELMC 계열 배열을 선언한다(32–57). 이 구간에는 실행문이 없다. 원문(연속행은 앞 문장에 이어짐): `  INTEGER, ALLOCATABLE :: NG(:)` (32); `  INTEGER, ALLOCATABLE :: NIEC(:)` (33); `  INTEGER, ALLOCATABLE :: NINC(:)` (34); `  INTEGER, ALLOCATABLE :: NIEG(:)` (35); `  INTEGER, ALLOCATABLE :: NIEQ(:)` (36); `  INTEGER, ALLOCATABLE :: NIBT(:)` (37); `  INTEGER, ALLOCATABLE :: NODG(:,:)` (39); `  INTEGER, ALLOCATABLE :: IEC(:,:)` (40); `  INTEGER, ALLOCATABLE :: INC(:,:)` (41); `  INTEGER, ALLOCATABLE :: IEG(:,:)` (42); `  INTEGER, ALLOCATABLE :: IEQ(:,:)` (43); `  INTEGER, ALLOCATABLE :: IBT(:,:)` (44); `  INTEGER, ALLOCATABLE :: NODP(:,:)` (46); `  INTEGER, ALLOCATABLE :: IELCP(:,:)` (47); `  INTEGER, ALLOCATABLE :: INDCP(:,:)` (48); `  INTEGER, ALLOCATABLE :: IEDGP(:,:)` (49); `  INTEGER, ALLOCATABLE :: NN_EXTC(:)` (51); `  INTEGER, ALLOCATABLE :: NGC(:)` (52); `  INTEGER, ALLOCATABLE :: NEC(:)` (53); `  INTEGER, ALLOCATABLE :: NODC(:,:)` (55); `  INTEGER, ALLOCATABLE :: NODGC(:,:)` (56); `  INTEGER, ALLOCATABLE :: IELMC(:,:)` (57) [11-04 전수 검증 정정] |
| 59–75 | 시작 시 1행 M_PART 모듈 안. 해석: 확장 절점 배열 NN_EXTX/NODX와 NPIMPX/NIMPX, NPEXPX/NEXPX 및 해당 프로세스·인덱스·절점 배열을 선언하고 모듈을 닫는다(59–75). 원문(연속행은 앞 문장에 이어짐): `  INTEGER, ALLOCATABLE :: NN_EXTX(:)` (59); `  INTEGER, ALLOCATABLE :: NODX(:,:)` (61); `  INTEGER :: NPIMPX,NIMPX` (63); `  INTEGER, ALLOCATABLE :: IPIMPX(:)` (65); `  INTEGER, ALLOCATABLE :: IDXIMPX(:,:)` (66); `  INTEGER, ALLOCATABLE :: NODIMPX(:)` (67); `  INTEGER :: NPEXPX,NEXPX` (69); `  INTEGER, ALLOCATABLE :: IPEXPX(:)` (71); `  INTEGER, ALLOCATABLE :: IDXEXPX(:,:)` (72); `  INTEGER, ALLOCATABLE :: NODEXPX(:)` (73); `END MODULE M_PART` (75) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24·63·69: 스칼라 NPE/NIMP/NEXP, NPIMPX/NIMPX, NPEXPX/NEXPX 선언에는 초기값이 없다. 이 파일에는 배열 할당문이나 실행 루틴이 없다.
