---
file: models/ROMS/raw/source_code/roms/Master/mct_coupler.h
lines: 122
sha256: 51939425797bd27525bd70d0ebb4ba54310e656ad5c8e0469f4aef8fa0cf0cb9
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# mct_coupler.h — 판독 구간 기록

구간은 1행부터 122행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | `cppdefs.h`(1)를 끼워 넣고 `mct_coupler_mod` 모듈(2)을 연다. 모델 결합과 MCT_LIB가 모두 정의된 범위(4)에 저작권·라이선스 및 Model Coupling Toolkit(MCT)을 통한 자료 교환 목적의 주석(5–20)이 있다. 원문 조건·대입식·반복·전처리: `#include "cppdefs.h"` (1); `#if defined MODEL_COUPLING && defined MCT_LIB` (4). |
| 21–78 | 시작 시 4행 `#if defined MODEL_COUPLING && defined MCT_LIB` 안. 시작 시 2행 `mct_coupler_mod` 모듈 안. MCTWorld 등록·정리(21–22), 영역 분할 지도(GlobalSegMap)의 초기화·크기·정리·정렬점(26–30), 속성 벡터(AttrVect)의 초기화·영값·크기·정리·실수 속성 입출력(34–40), Router 초기화·정리(44–46), MCT_Send·MCT_Recv(50–51), SparseMatrix와 SparseMatrixPlus의 초기화·행/열/원소 입력·정리(55–65), 행 분해 선택 Xonly(69), 희소행렬과 속성 벡터 곱 MCT_MatVecMul(73)을 가져온다. `implicit none`(75)과 기본 PRIVATE(77)를 선언한다. 이 구간에는 호출문이나 계산식이 없다. |
| 79–104 | 시작 시 4행 `#if defined MODEL_COUPLING && defined MCT_LIB` 안. 시작 시 2행 모듈 안. SWAN_COUPLING이면 해양-파랑 초기화·교환·정리 세 루틴을 공개(80–82)한다. WRF_COUPLING이면 해양-대기 세 루틴을 공개(85–87)한다. 별도 SWAN 분기는 wav2ocn_AV·ocn2wav_AV·ROMStoSWAN을 선언(93–95)한다. 별도 WRF 분기는 atm2ocn_AV·ocn2atm_AV·ROMStoWRF를 선언(98–100)한다. 공통 GSMapROMS(102)와 CONTAINS(104)가 뒤따른다. 원문 조건·대입식·반복·전처리: `# ifdef SWAN_COUPLING` (79); `# endif` (83); `# ifdef WRF_COUPLING` (84); `# endif` (88); `# ifdef SWAN_COUPLING` (92); `# endif` (96); `# ifdef WRF_COUPLING` (97); `# endif` (101). |
| 105–122 | 시작 시 4행 `#if defined MODEL_COUPLING && defined MCT_LIB` 안. 시작 시 2행 모듈 안. 통신 루틴 포함 주석(105–109) 뒤에서 SWAN_COUPLING은 `mct_roms_swan.h`(112), REFDIF_COUPLING은 `mct_roms_refdif.h`(115), WRF_COUPLING은 `mct_roms_wrf.h`(118)를 끼워 넣는다. 세 조건은 독립적이다. 121행은 4행 조건을 닫는다. 122행은 모듈을 끝낸다. 원문 조건·대입식·반복·전처리: `# ifdef SWAN_COUPLING` (111); `#  include "mct_roms_swan.h"` (112); `# endif` (113); `# ifdef REFDIF_COUPLING` (114); `#  include "mct_roms_refdif.h"` (115); `# endif` (116); `# ifdef WRF_COUPLING` (117); `#  include "mct_roms_wrf.h"` (118); `# endif` (119); `#endif` (121). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 79–101·111–119: SWAN과 WRF에는 공개 루틴과 결합 벡터·Router의 전용 선언 조건이 있다. REFDIF에는 이 파일 안의 전용 선언 조건 없이 포함 지시문만 있다. 포함 파일 내부는 이 사실의 판독 범위에 포함하지 않았다.
