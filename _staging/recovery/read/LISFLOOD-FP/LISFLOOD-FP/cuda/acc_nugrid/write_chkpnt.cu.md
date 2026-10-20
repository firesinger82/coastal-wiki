---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/write_chkpnt.cu
lines: 130
sha256: c6590797109a7c38669940f94dc9354d87fcad4fcb6d79f459d94ea8e070dac4
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_chkpnt.cu — 판독 구간 기록

구간은 1행부터 130행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | 관련 헤더와 VersionHistory 포함(1–2). `__host__ void lis::cuda::acc_nugrid::write_chkpnt` (4)는 체크포인트(checkpoint)를 쓰는 호스트(host) 함수이다. 조립 해(assembled solution)·이웃·파일명·Pars·Solver의 const 참조, States 수정 참조, 네 통계 배열, non_uniform_n·최세밀 요소 수·verbose를 받는다(5–19). 파일 포인터와 버전 정수 선언(22–24). 버전 변환·조합식은 `checkv = int(LF_CheckVersion);` (26)<br>`version = (int(LF_VersionMajor) * 100) + (int(LF_VersionMinor) * 10) + int(LF_VersionInc);` (27). 이 파일에는 전처리 조건 분기가 없다. LF_CheckVersion·LF_VersionMajor·LF_VersionMinor·LF_VersionInc의 수치 정의는 이 파일에 없다. |
| 29–49 | 시작 시 4행 write_chkpnt 함수 안. h·q 호스트 배열을 조립 해 길이·이웃 길이로 확보한다(29–30). 바이트 수는 `size_t bytes_sol     = d_assem_sol.length * sizeof(NUMERIC_TYPE);` (32)<br>`size_t bytes_dis     = d_non_uniform_nghbrs.length * sizeof(NUMERIC_TYPE);` (33). copy_cuda로 h·q를 복사한다(35–36). maxH·totalHtm·maxHtm·initHtm은 num_finest_elems 크기로 할당한다(38–41). 바이트 수는 `size_t bytes = num_finest_elems * sizeof(NUMERIC_TYPE);` (43), copy_cuda 네 번으로 통계 배열을 복사한다(45–48). 빈 줄까지 포함한다. |
| 50–88 | 시작 시 4행 함수 안. 정밀도 유지를 위해 이진(binary) 출력한다는 주석(50). 열기 조건은 `if ((check_fp = fopen(filenames.checkpointfilename, "wb")) == NULL) {` (51). 실패 시 `if (verbose == ON) printf("Unable to open checkpoint file: checkpointing off");` (52), checkpoint=OFF와 return(53–54). `else {` (56)의 성공 분기에서는 checkv·version, itrn_time_now·t·itCount, MassTotal·Tstep·MinTstep, SaveNo·SaveTotal, xsz·ysz, h·q 순서로 fwrite한다(58–76). 정수는 int, itCount는 long, 나머지 수치·배열은 NUMERIC_TYPE을 사용한다. `if (non_uniform_n) {` (78)이면 n0를 임시 할당·copy_cuda·fwrite한다(79–82). maxH·maxHtm·initHtm을 쓰고(84–86) `if (checkv > 1) fwrite(totalHtm, sizeof(NUMERIC_TYPE), num_finest_elems, check_fp);` (87)일 때 totalHtm을 쓴다. |
| 89–117 | 시작 시 4행 함수·56행 파일 열기 성공 else 분기 안. 질량 유입·유출 및 경계 상태 fwrite는 주석이다(89–94). dx·dy·dA, tlx·tly·blx·bly를 NUMERIC_TYPE으로 각각 fwrite한다(96–103). 통계 항목 및 checkv>2 손실 출력 블록은 주석이다(105–113). fclose 호출(115), 계산 시간을 시간 단위로 표시하는 전체 출력식은 `printf("Checkpointed at %.4" NUM_FMT" hours computation time\n", (solver.itrn_time_now / C(3600.0)));` (116). 성공 분기를 닫는다(117). |
| 118–130 | 시작 시 4행 write_chkpnt 함수 안이며 51행 파일 열기 조건과 56행 else 밖. h·q, maxH·totalHtm·maxHtm·initHtm을 delete[]로 해제한다(120–126). 빈 줄과 return·함수 닫기를 포함한다(118–119·122·127–130). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 29–48·51–54·120–126: 파일 열기 전에 여섯 호스트 배열을 할당한다. 열기 실패 분기는 이 배열들의 delete[]에 도달하기 전에 반환한다.
- 78–82·120–126: non_uniform_n 분기에서 할당한 n0에 대응하는 delete[] 문장은 이 함수에 없다.
- 58–103: 실행되는 fwrite 호출의 반환값을 검사하는 조건은 없다.
- 52·116: 열기 실패 메시지에는 verbose 조건이 있다. 성공 후 Checkpointed 메시지는 verbose 조건 없이 출력한다.
