---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/drifters.F90
lines: 69
sha256: 42c0e8bae3a881126deaa48617848576cfcfad387a1eb9c5be185d899bda76c9
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# drifters.F90 — 판독 구간 기록

구간은 1행부터 69행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | private 모듈에서 drifter 공개(1–6), 루틴 사용 모듈·입력과 지역 변수 선언(7–20). USEMPI이면 rank별 시작 인덱스에서 1을 뺀 shift, 미정의면 두 shift 0(23–29). 원문(USEMPI 정의 시 → 조건·반복 블록 밖): `#ifdef USEMPI` (23). `ishift  = s%is(xmpi_rank+1)-1` (24). `jshift  = s%js(xmpi_rank+1)-1` (25). 원문(조건·반복 블록 밖): `#else` (26). 원문(USEMPI 미정의 시 → 조건·반복 블록 밖): `ishift  = 0` (27). `jshift  = 0` (28). 원문(조건·반복 블록 밖): `#endif` (29). |
| 31–52 | 각 drifter의 시작·종료 시간 사이일 때만 실행(31–32). 가장 가까운 u/v 격자 인덱스를 nint로 결정(35–38), 네 인덱스가 각 범위 안일 때만 속도/격자간격×dt 변위 계산과 idrift/jdrift 누적(41–51). 원문(조건·반복 블록 밖): `do i=1,par%ndrifter` (31). 원문(31행 반복 안): `if (par%t>s%tdriftb(i) .and. par%t<s%tdrifte(i)) then` (32). 원문(31행 반복 안 → 32행 if 참 분기): `iu          = nint(s%idrift(i)-ishift-0.d5)` (35). `ju          = nint(s%jdrift(i)-jshift     )` (36). `iv          = nint(s%idrift(i)-ishift     )` (37). `jv          = nint(s%jdrift(i)-jshift-0.d5)` (38). `if (    iu >= 1 .and. iu <= s%nx .and.  &` (41); `ju >= 1 .and. ju <= s%ny .and.  &` (42); `iv >= 1 .and. iv <= s%nx .and.  &` (43); `jv >= 1 .and. jv <= s%ny            ) then` (44). 원문(31행 반복 안 → 32행 if 참 분기 → 41행 if 참 분기): `di      = s%uu(iu,ju)/s%dsu(iu,ju)*par%dt` (47). `dj      = s%vv(iv,jv)/s%dnv(iv,jv)*par%dt` (48). `s%idrift(i) = s%idrift(i) + di` (50). `s%jdrift(i) = s%jdrift(i) + dj` (51). |
| 53–69 | 첫 행은 31행 반복과 32행 시간조건 및 41행 영역조건 안의 전처리 지시다. USEMPI의 else에서는 영역 밖 drifter 좌표를 huge−10000으로 설정(54–56); 영역조건 종료 후에도 시간조건·반복 안에서 MPI_MIN allreduce 두 번(60–63). 시간조건·루프·루틴·모듈 종료(65–69). 첫 행의 바깥 범위: 31행 반복 안 → 32행 if 참 분기 → 41행 if 참 분기. 원문(USEMPI 정의 시 → 31행 반복 안 → 32행 if 참 분기 → 41행 if 참 분기): `#ifdef USEMPI` (53). 원문(USEMPI 정의 시 → 31행 반복 안 → 32행 if 참 분기): `else` (54). 원문(USEMPI 정의 시 → 31행 반복 안 → 32행 if 참 분기 → 54행 else(41행 조건 불성립)): `s%idrift(i)  = huge(0.0d0)-10000.d0` (55). `s%jdrift(i)  = huge(0.0d0)-10000.d0` (56). `#endif` (57). 원문(USEMPI 미정의 시 → 31행 반복 안 → 32행 if 참 분기 → 41행 if 참 분기): `#endif` (57). 원문(USEMPI 정의 시 → 31행 반복 안 → 32행 if 참 분기 → 54행 else(41행 조건 불성립)): `endif` (58). 원문(USEMPI 미정의 시 → 31행 반복 안 → 32행 if 참 분기 → 41행 if 참 분기): `endif` (58). 원문(USEMPI 정의 시 → 31행 반복 안 → 32행 if 참 분기): `#ifdef USEMPI` (60). `call xmpi_allreduce(s%idrift(i),MPI_MIN)` (61). `call xmpi_allreduce(s%jdrift(i),MPI_MIN)` (62). 원문(31행 반복 안 → 32행 if 참 분기): `#endif` (63). `endif` (65). 원문(31행 반복 안): `enddo` (66). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32: 활성 시간 조건은 `>`와 `<`이므로 시작·종료 시간과 정확히 같은 시각은 이 조건에 포함되지 않는다.
- 41–44: j 인덱스 상한은 두 성분 모두 s%ny이며 ny=0에 대한 별도 분기는 없다.
- 53–63: 영역 밖 sentinel 대입과 MPI_MIN 집계는 USEMPI 경로에만 있다.
