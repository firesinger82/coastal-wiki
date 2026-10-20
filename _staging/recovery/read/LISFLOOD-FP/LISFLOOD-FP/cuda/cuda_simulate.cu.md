---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_simulate.cu
lines: 434
sha256: 5b508c4b52dc914dee9b0875baac464cff609e8fb3d7654af2c18b5d36eab92a
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_simulate.cu — 판독 구간 기록

구간은 1행부터 434행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | simulate·util·UnifiedAllocator·io·VersionHistory 헤더(1–5), 두 include 주석(6–7). Simulation::print_device_info(9)는 get_device·get_device_properties(11–13), 장치 번호와 UUID 출력(14–20). UUID 바이트는 reinterpret_cast<unsigned char*>로 참조한다(15). 이 파일 자체의 전처리 조건 분기는 없다. |
| 23–70 | initialise_H(23–33)는 `if (states.startfile == ON)` (35)에서 StartFile::load(37), 그 안 `if (states.startelev == ON)` (38)일 때 StartFile::subtract_dem(40). nullify_max(47–56)의 `for (int j = 0; j < geometry.ysz; j++)` (59), `for (int i = 0; i < geometry.xsz; i++)` (61)에서 `maxHtm[j * pitch + i + offset] = NULLVAL;` (63), `initHtm[j * pitch + i + offset] = NULLVAL;` (64), `totalHtm[j * pitch + i + offset] = C(0.0);` (65). 함수·빈 줄 포함. |
| 71–117 | initialise_discharge(71–81)의 `if (states.startq2d == ON)` (83)에서 800자 버퍼 두 개에 startfilename을 strcpy하고 .Qx·.Qy를 strcat한다(85–91). StartFile::load로 HU·HV 로드(93–94). initialise_manning(98–106)은 fopen_or_die rb 모드(108), AsciiRaster::read_header(111), match_cell_dimensions_or_die(112–113), read(114), fclose(115). |
| 118–148 | load_boundaries(118–125)는 LoadBCs(127), LoadBCVar에 세 nullptr와 verbose를 전달한다(128–129). update_geometry(132–136)는 Geometry의 xsz·ysz·blx·bly·tly·dx·dy를 Pars의 대응 필드에 복사(138–144). 147행은 이전 read_checkpoint 호출 주석, 빈 줄(148). |
| 149–178 | read_checkpoint의 파일명·상태·Pars·Solver·수심·유량·최대 수심·침수 시간 배열·StatsCollector·verbose 인수 선언(149–164). 차원·파일 포인터·버전 정수(167–172), 두 수로 관련 선언 주석(169–170). `NUMERIC_TYPE* dummy;` (174). 모델 버전 계산식은 `LFv = (int(LF_VersionMajor) * 100) + (int(LF_VersionMinor) * 10) + int(LF_VersionInc);` (176). |
| 179–222 | 시작 시 149행 read_checkpoint 안. 기본 파일 우선 탐색 주석(179–181), `if ((check_fp = fopen(filenames.checkpointfilename, "rb")) == NULL) // open file and check it exists` (182). 그 안 `if (verbose == ON)` (185)는 미발견 로그, `if (states.checkfile == ON)` (188)에서 `if ((check_fp = fopen(filenames.loadCheckpointFilename, "rb")) == NULL) // open file and check it exists` (191). 내부 `if (verbose == ON)` (194)는 대체 파일 미발견 로그, `else` (196)의 `if (verbose == ON)` (199)는 열림 로그. 182행의 `else` (203)는 `if (states.checkfile == ON) // let user know program is using newer default checkpoint rather then alternative file` (205)에서 대체 파일 미사용 안내(207–208), `if (verbose == ON)` (211)에서 기본 파일 열림 로그. 빈 줄·판독 순서 주석(213–222). |
| 223–275 | 시작 시 149행 read_checkpoint 안이며 파일 탐색 분기 밖. `if (check_fp == NULL) // no file opened in initial sequence` (223)는 `if (verbose == ON)` (226)에서 처음부터 시작 로그. `else` (228)는 `if (verbose == ON)` (231) 로그 후 checkv를 fread(234). `if (feof(check_fp)) {` (235)의 `if (verbose == ON)` (236)는 빈 파일 로그. `else if (checkv != int(LF_CheckVersion)) {` (238)의 `if (verbose == ON)` (239)는 체크포인트(checkpoint) 버전 차이 로그. `else {` (241)는 version 판독(245), `if (version != LFv) {` (246)의 `if (verbose == ON)` (247)는 모델 버전 경고. itrn_time·t·itCount, MassTotal·InitTstep·MinTstep, single_op·op_multiswitch·SaveNo·SaveTotal 순으로 읽는다(249–260). 차원 xchk·ychk 판독(263–264), `if (xchk != pars.xsz \|\| ychk != pars.ysz)` (265)의 `if (verbose == ON)` (267)에서 차원 출력(269–271), exit(0)(273). |
| 276–328 | 시작 시 149행 read_checkpoint·223행 조건의 228행 else·235/238행 조건의 241행 else 안. H·maxH·maxHtm·initHtm은 pars.xsz * pars.ysz개, Qx·Qy는 (pars.xsz + 1) * (pars.ysz + 1)개 판독(277–282). `if (checkv > 1) fread(totalHtm, sizeof(NUMERIC_TYPE), pars.xsz * pars.ysz, check_fp);` (283). 수로·마스크·통계 관련 fread 주석(285–289·292·294–297). dummy 주소로 수치 한 개씩 읽는 호출은 `fread(&dummy, sizeof(NUMERIC_TYPE), 1, check_fp);` (291·293). dx·dy·dA·tlx·tly·blx·bly 판독(299–306), 면적 대신 dummy 판독(309), Stats_Collector.previous_volume 판독(311), 오차 대신 dummy 판독(314). `//` 뒤 `if (checkv > 2) {` (316)와 두 fread는 주석(316–319). `if (verbose == ON)` (321)에서 solver.itrn_time/C(3600.0) 등의 진행 로그, fclose(check_fp)(322). 분기 종료(323–324), return·함수 종료(326–328). |
| 329–366 | 빈 줄(329–330), write_checkpoint 인수 선언(331–347). 파일 포인터·버전 변수(350–354), 수로 관련 선언 주석(351–352). `checkv = int(LF_CheckVersion);` (356), `version = (int(LF_VersionMajor) * 100) + (int(LF_VersionMinor) * 10) + int(LF_VersionInc);` (357). 바이너리(binary) 정밀도 보존 주석(361). `if ((check_fp = fopen(filenames.checkpointfilename, "wb")) == NULL) {` (362)의 `if (verbose == ON)` (363)에서 열기 실패 로그, `states.checkpoint = OFF;` (364), return(365). |
| 367–400 | 시작 시 331행 write_checkpoint 안. 362행 조건의 `else {` (367)에서 checkv·version, solver.itrn_time_now·t·itCount, pars.MassTotal·dt·solver.MinTstep, states.single_op, pars.op_multiswitch·SaveNo·SaveTotal·xsz·ysz를 순서대로 fwrite(369–386). H·maxH·maxHtm·initHtm은 pars.xsz * pars.ysz개, Qx·Qy는 (pars.xsz + 1) * (pars.ysz + 1)개 기록(388–393). `if (checkv > 1) fwrite(totalHtm, sizeof(NUMERIC_TYPE), pars.xsz * pars.ysz, check_fp);` (394). 수로·마스크 fwrite는 주석이다(396–400). |
| 401–434 | 시작 시 331행 write_checkpoint·362행 조건의 367행 else 안. Stats_Entry.mass.in·mass.out 기록(402–403), 수로·점원 관련 fwrite 주석(404–407). dx·dy·dA·tlx·tly·blx·bly 기록(409–416), Stats_Entry.area·volume·discharge_error 기록(418·420–421). 419행은 이전 체적 fwrite 주석. `//if (checkv > 2) {` (423)와 침투·증발 손실 fwrite는 주석이다(423–426). fclose(check_fp)(428), solver.itrn_time_now/C(3600.0)의 체크포인트 로그(429). else 종료(430), return·함수 종료(432–434). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 35–42·83–95: 초기 수심·유량 함수는 해당 시작 파일 플래그가 ON일 때만 배열을 변경한다. 그 밖의 배열 초기화 분기는 없다.
- 55·59–68: nullify_max의 verbose 인수는 본문에서 사용하지 않는다.
- 85–91: 유량 시작 파일명은 800자 배열에 strcpy·strcat으로 조합한다. 이 블록에는 길이 비교가 없다.
- 110–114: initialise_manning은 입력 결측값을 read_header로 받는다. 그 결측값을 치환하는 호출은 이 함수에 없다.
- 174·291·293·309·314: dummy는 NUMERIC_TYPE 포인터로 선언한다. 건너뛰는 수치 항목의 fread는 dummy 자체의 주소에 sizeof(NUMERIC_TYPE) 바이트를 쓴다.
- 258·381: op_multiswitch 판독은 &pars.op_multiswitch를 전달한다. 기록은 pars.op_multiswitch를 전달한다.
- 234–322: fread 호출의 반환 개수를 검사하는 문장은 없다. 첫 버전 판독 뒤 feof 검사는 있다(235).
- 235–241·322: fclose는 버전 검사를 통과한 241행 else 안에 있다. 빈 파일 또는 체크포인트 버전 불일치 분기에는 fclose가 없다.
- 245–248: 모델 버전 불일치는 경고만 출력하며 이후 데이터 판독을 계속한다.
- 249·254·372·377: 기록한 itrn_time_now와 dt는 판독에서 각각 itrn_time과 InitTstep에 저장한다.
- 369–429: fwrite 호출의 반환 개수를 검사하는 문장은 없다.
