---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/output.cpp
lines: 193
sha256: 17fd9273ce418131f4125a75b35cd8c7f30a738b25a44957eff335f71984f961
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# output.cpp — 판독 구간 기록

구간은 1행부터 193행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | 헤더 포함(1) 뒤 `write_mass_stats`가 질량 수지(mass balance) 통계를 출력한다. 시간·현재/최소 시간 간격·반복 수·침수 면적·체적·유입·Hds·유출·유량/체적 오차·강우 순량을 한 줄로 적고 fflush한다(11–28). 마지막 값은 RainTotalLoss에서 침투·증발 누계를 뺀 값이다. 조건부 전처리 분기는 없다. 원문: `Parptr->RainTotalLoss - (Parptr->InfilTotalLoss + Parptr->EvapTotalLoss)` (26). |
| 31–58 | `write_depth_samples`는 시각을 적고 Nstages 표본을 순회한다. 각 H를 격자 인덱스로 먼저 읽은 뒤 stage_check가 1이면 값을, else면 대시·탭을 적는다. 마지막 줄바꿈 후 fflush한다(55–56). 원문: `for (int i = 0; i<Stageptr->Nstages; i++)` (41); `{` (42); `NUMERIC_TYPE H = Arrptr->H[` (43); `Stageptr->stage_grid_y[i]*Parptr->xsz + Stageptr->stage_grid_x[i]];` (44); `if (Stageptr->stage_check[i] == 1)` (46); `else` (50). |
| 59–101 | `write_speed_samples`는 시각을 적고 표본마다 평탄화 인덱스의 H·HU·HV를 읽는다. H가 DepthThresh보다 크면 속력(speed)을 계산하고 else는 0이다. stage_check가 1이면 속력, else면 대시·탭을 적는다. 줄바꿈과 fflush로 끝낸다(98–99). 원문: `for (int i = 0; i<Stageptr->Nstages; i++)` (69); `{` (70); `const int index =` (71); `Stageptr->stage_grid_y[i]*Parptr->xsz + Stageptr->stage_grid_x[i];` (72); `NUMERIC_TYPE H = Arrptr->H[index];` (74); `NUMERIC_TYPE HU = Arrptr->HU[index];` (75); `NUMERIC_TYPE HV = Arrptr->HV[index];` (76); `NUMERIC_TYPE speed;` (78); `if (H > Solverptr->DepthThresh)` (80); `{` (81); `speed = sqrt(HU/H * HU/H + HV/H * HV/H);` (82); `}` (83); `else` (84); `{` (85); `speed = C(0.0);` (86); `}` (87); `if (Stageptr->stage_check[i] == 1)` (89); `else` (93). |
| 102–147 | `write_solution`은 SaveTotal 이전이면 반환한다. save_depth 조건에서 .wd/.wdb, save_elev 조건에서 .elev/.elevb, save_Qs 조건에서 .Qx/.Qxb와 .Qy/.Qyb, voutput 조건에서 .Vx/.Vxb와 .Vy/.Vyb를 쓴다. 수면고(water surface elevation)는 DEM과 출력 모드 3을 raster 함수에 넘긴다. 출력 후 예정 시각과 번호를 한 번 증가시킨다. 원문: `if (Solverptr->t < Parptr->SaveTotal) return;` (111); `if (Statesptr->save_depth == ON)` (113); `{` (114); `write_field(Arrptr->H, ".wd", ".wdb", Fnameptr, Statesptr, Parptr);` (115); `}` (116); `if (Statesptr->save_elev == ON)` (118); `{` (119); `if (Statesptr->binary_out == ON)` (120); `{` (121); `write_binrasterfile(Fnameptr->resrootname, Parptr->SaveNo,` (122); `".elevb", Arrptr->H, Arrptr->DEM, 3, Statesptr, Parptr);` (123); `}` (124); `else` (125); `{` (126); `write_ascfile(Fnameptr->resrootname, Parptr->SaveNo,` (127); `".elev", Arrptr->H, Arrptr->DEM, 3, Statesptr, Parptr);` (128); `}` (129); `}` (130); `if (Statesptr->save_Qs == ON)` (132); `{` (133); `write_field(Arrptr->HU, ".Qx", ".Qxb", Fnameptr, Statesptr, Parptr);` (134); `write_field(Arrptr->HV, ".Qy", ".Qyb", Fnameptr, Statesptr, Parptr);` (135); `}` (136); `if (Statesptr->voutput == ON)` (138); `{` (139); `write_field(Arrptr->Vx, ".Vx", ".Vxb", Fnameptr, Statesptr, Parptr);` (140); `write_field(Arrptr->Vy, ".Vy", ".Vyb", Fnameptr, Statesptr, Parptr);` (141); `}` (142); `Parptr->SaveTotal += Parptr->SaveInt;` (144); `Parptr->SaveNo += 1;` (145). |
| 148–167 | `write_max_field`는 binary_out이 ON이면 이진 격자(binary raster) .maxb, else면 ASCII 격자 .max를 쓴다. 출력 번호는 −1, 자료는 maxH와 DEM, 모드는 0이다. 원문: `if (Statesptr->binary_out == ON)` (156); `{` (157); `write_binrasterfile(Fnameptr->resrootname, -1, ".maxb", Arrptr->maxH,` (158); `Arrptr->DEM, 0, Statesptr, Parptr);` (159); `}` (160); `else` (161); `{` (162); `write_ascfile(Fnameptr->resrootname, -1, ".max", Arrptr->maxH,` (163); `Arrptr->DEM, 0, Statesptr, Parptr);` (164); `}` (165). |
| 168–193 | `write_field`는 binary_out 조건으로 `write_binrasterfile` 또는 `write_ascfile`을 호출한다. DEM 인수는 nullptr, 모드는 0이다. ASCII 경로는 길이 16의 format_specifier에 output_precision을 담아 전달한다. 마지막 빈 줄까지 포함한다. 원문: `if (Statesptr->binary_out == ON)` (178); `{` (179); `write_binrasterfile(Fnameptr->resrootname, Parptr->SaveNo,` (180); `binary_suffix, field, nullptr, 0, Statesptr, Parptr);` (181); `}` (182); `else` (183); `{` (184); `char format_specifier[16];` (185); `snprintf(format_specifier, 16*sizeof(char), "%%.%i",` (186); `Parptr->output_precision);` (187); `write_ascfile(Fnameptr->resrootname, Parptr->SaveNo,` (189); `ascii_suffix, field, nullptr, 0, Statesptr, Parptr, C(0.0), format_specifier);` (190); `}` (191). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 43–46·71–89: 표본의 H 또는 H·HU·HV 배열 접근은 stage_check 조건 검사보다 먼저 실행된다.
- 144–145: `write_solution`의 한 번 호출은 SaveTotal과 SaveNo를 각각 한 번만 증가시킨다. 여러 저장 시각을 따라잡는 반복문은 이 함수에 없다.
- 185–190: ASCII 출력 형식 문자열의 작업 배열과 snprintf 길이는 16으로 고정되어 있다.
