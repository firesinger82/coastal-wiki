---
file: models/FUNWAVE/raw/source_code/FUNWAVE-GPU/src/sponge_gpu.F
lines: 44
sha256: 0d198a3bf4c39434eb4a7b338227fc34d7ff5f122ceffcdfd08647927dc7a639
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# sponge_gpu.F — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | Larsen-Dancy(1983)형 스펀지층(sponge layer)으로 파랑을 감쇠한다는 설명·2010년 이력·구분 주석(1–8). sponge_module은 cudafor·PARAM의 ZERO·GLOBAL의 전역 및 지역 크기와 유령 격자점(ghost point) 수·mod_cuda의 실행 배치와 ETA_d·U_d·V_d·SPONGE_d·MASK_d를 사용한다(9–14). 빈 줄·contains (15–17). 이 파일에는 전처리 조건이 없다. |
| 18–33 | 시작 시 9행 모듈 안이다. `attributes(global) subroutine sponge_damping_kernel(Mloc,Nloc)` (18), VALUE 정수 크기 인수와 i·j 선언(20–21). `i = threadIdx%x + (blockIdx%x-1)*BlockDimX_2D` (23), `j = threadIdx%y + (blockIdx%y-1)*BlockDimY_2D` (24). `if (i>=1 .AND. i<=Mloc .AND. j>=1 .AND. j<=Nloc) then` (25) 안의 `IF(MASK_d(I,J)>0)THEN` (26)이면 `ETA_d(I,J)=ETA_d(I,J)/SPONGE_d(I,J)` (27). 이 MASK 조건 밖이지만 크기 범위 조건 안에서 `U_d(I,J)=U_d(I,J)/SPONGE_d(I,J)` (29), `V_d(I,J)=V_d(I,J)/SPONGE_d(I,J)` (30). 조건·커널 종료·빈 줄(28·31–33). 이 커널 정의에는 전처리 제한이 없다. |
| 34–44 | 시작 시 9행 모듈 안이다. SPONGE_DAMPING_GPU 입구·IMPLICIT NONE·배치 주석(34–36). `tBlock = dim3 (BlockDimX_2D, BlockDimY_2D ,1)` (37), `grid = dim3 ( ceiling ( real ( Mloc ) / BlockDimX_2D ) , &` (38); `ceiling ( real ( Nloc ) / BlockDimY_2D ) , 1)` (39). `call sponge_damping_kernel<<<grid, tBlock>>>(Mloc,Nloc)` (40)로 CUDA Fortran 커널을 호출한다. 빈 줄·루틴·모듈 종료(41–44). 이 호출에는 전처리 플래그에 따른 선택이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–13: 가져온 ZERO·MGlob·NGlob·NGhost는 이 파일의 실행문에서 사용되지 않는다.
- 25–30: 수위 감쇠는 MASK_d>0 조건 안에 있다. U_d·V_d 감쇠는 그 MASK 조건 밖에 있다.
- 27–30: 세 감쇠 식은 SPONGE_d를 분모로 사용한다. 이 파일에는 SPONGE_d의 값 범위 검사나 0 여부 검사가 없다.
