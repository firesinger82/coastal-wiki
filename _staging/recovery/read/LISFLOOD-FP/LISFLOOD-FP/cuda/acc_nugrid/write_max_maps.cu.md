---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/write_max_maps.cu
lines: 205
sha256: 7bc48f2d1772248d6f7e9a5444f56bed97bf1eeba1b1dd8bb706634f34954ecc
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_max_maps.cu — 판독 구간 기록

구간은 1행부터 205행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–44 | 관련 헤더 포함(1). `__host__ void lis::cuda::acc_nugrid::write_max_maps` (3)의 호스트(host) 함수는 결과 경로·격자 차원·Pars·최대 수심 및 시간 배열 네 개·정밀도를 받는다(4–13). 길이 800의 경로 버퍼(15), 행·열 수 0 초기화(17–18), cell_size=pars.dx와 좌하단 x/y 좌표 복사(20–23). 결측값 기본 설정은 `int NODATA_value = -9999;` (25). ncols·nrows에 xsz·ysz를 복사한다(29–30). 각 호스트 배열의 크기는 mesh_dim * mesh_dim이다(32–35). 바이트 수는 `size_t bytes = mesh_dim * mesh_dim * sizeof(NUMERIC_TYPE);` (37)이며 copy_cuda 네 번으로 배열을 가져온다(39–42). 빈 줄을 포함한다. 전처리 조건 분기는 없다. |
| 45–82 | 시작 시 3행 write_max_maps 함수 안. snprintf에 버퍼 크기 800 * sizeof(char)와 .inittm 접미사를 넘긴다(47). wb 모드로 연다(50). `if (NULL == fp)` (52)이면 오류 출력·exit(-1)(54–55). ncols·nrows·xllcorner·yllcorner·cellsize·NODATA_value 머리말을 fprintf로 쓴다(58–63). `for (int j = 0; j < nrows; j++)` (65)와 `for (int i = 0; i < ncols; i++)` (67)에서 `int idx = (nrows - 1 - j) * mesh_dim + i;` (69)로 행 순서를 뒤집은 인덱스를 계산한다. 다른 인덱스식은 주석이다(70). precision으로 initHtm[idx]를 출력하고 행마다 줄바꿈한다(72–77). fclose 및 구분 주석·빈 줄(79–82). |
| 83–120 | 시작 시 3행 write_max_maps 함수 안. snprintf로 .totaltm 경로를 만들고 wb 모드로 연다(85–88). `if (NULL == fp)` (90)이면 오류 출력·exit(-1)(92–93). 같은 여섯 머리말을 쓴다(96–101). `for (int j = 0; j < nrows; j++)` (103)와 `for (int i = 0; i < ncols; i++)` (105)에서 `int idx = (nrows - 1 - j) * mesh_dim + i;` (107)로 인덱스를 계산한다. 대체 인덱스는 주석(108). precision으로 totalHtm[idx]를 출력하고 행마다 줄바꿈한다(110–115). fclose와 구분 주석·빈 줄(117–120). |
| 121–158 | 시작 시 3행 write_max_maps 함수 안. snprintf로 .max 경로를 만들고 wb 모드로 연다(123–126). `if (NULL == fp)` (128)이면 오류 출력·exit(-1)(130–131). 같은 여섯 머리말을 쓴다(134–139). `for (int j = 0; j < nrows; j++)` (141)와 `for (int i = 0; i < ncols; i++)` (143)에서 `int idx = (nrows - 1 - j) * mesh_dim + i;` (145)로 인덱스를 계산한다. 대체 식은 주석(146). precision으로 maxH[idx]를 출력하고 행마다 줄바꿈한다(148–153). fclose·구분 주석·빈 줄(155–158). |
| 159–205 | 시작 시 3행 write_max_maps 함수 안. snprintf로 .maxtm 경로를 만들고 wb 모드로 연다(161–164). `if (NULL == fp)` (166)이면 오류 출력·exit(-1)(168–169). 같은 여섯 머리말을 쓴다(172–177). `for (int j = 0; j < nrows; j++)` (179)와 `for (int i = 0; i < ncols; i++)` (181)에서 `int idx = (nrows - 1 - j) * mesh_dim + i;` (183)으로 인덱스를 계산한다. 대체 식은 주석(184). precision으로 maxHtm[idx]를 출력하고 행마다 줄바꿈한다(186–191). fclose와 구분 주석(193–195). 네 호스트 배열을 delete[]로 해제한다(198–201). 빈 줄·마지막 주석·함수 닫기를 포함한다(196–197·202–205). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 25·63·101·139·177: 출력 머리말의 NODATA_value는 -9999로 고정되어 있다. 네 출력 반복에는 배열값을 이 값으로 치환하는 조건이 없다.
- 50·58–76·88·96–114·126·134–152·164·172–190: 네 파일은 wb 모드로 열지만 데이터는 fprintf로 출력한다.
- 32–35·65–69·103–107·141–145·179–183: 배열은 mesh_dim 제곱 크기로 할당한다. 출력 범위는 pars.ysz·pars.xsz이며 이 범위와 mesh_dim을 비교하는 검사는 함수 안에 없다.
