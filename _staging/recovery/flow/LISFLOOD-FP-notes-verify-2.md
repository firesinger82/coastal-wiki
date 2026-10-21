# LISFLOOD-FP 노트 전수 대조 — 2/2

작업 대상은 `models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary-differences.md`이다.
작업 시작 때 파일의 전체 줄 수는 304줄이었다.
2/2 배정 구간은 원래 153–304행의 152줄이다.
배정 구간의 첫 행은 `cpu-gpu-swe:LG1-147`이고 마지막 행은 `theory:LT1-417`이다.
앞 구간의 동시 수정으로 줄 번호가 달라지면 행 ID로 배정 범위를 유지한다.
쓰기 대상은 이 기록과 대상 노트뿐이다.

상태: 배정 구간 2/2 전수 대조 완료.

기계 확인 후보: 사용자 제공 후보 없음.

## 대상 노트 대조 결과

대상은 [lisflood-fp-io-boundary-differences.md](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary-differences.md)의 2/2 구간이다.
원래 153–304행의 152줄을 모두 대조했다.
완료 시점에도 배정 구간은 153–304행이다.
정정은 14줄이다.
인용 보완은 3줄이다.
원문을 유지한 행은 135줄이다.
이 집계는 변경한 표 행을 기준으로 한다.
한 행에서 여러 부분을 고쳐도 한 줄로 센다.
대상 줄은 모두 차이 표 행이다.
frontmatter와 Mermaid 블록은 이 배정 구간에 없다.

| 보고서 계열 | 대상 노트 행 | 대조한 줄 수 | 정정 줄 수 | 보완 줄 수 |
|---|---|---:|---:|---:|
| cpu-gpu-swe | 153–154 | 2 | 0 | 2 |
| docx-manual | 155–199 | 45 | 11 | 0 |
| files-output | 200–237 | 38 | 2 | 0 |
| par | 238–287 | 50 | 1 | 0 |
| theory | 288–304 | 17 | 0 | 1 |
| 합계 | 153–304 | 152 | 14 | 3 |

## 대조 근거

[최종 결론 목록](../assign/LISFLOOD-FP-final-conclusions.tsv)의 행 ID를 배정된 152개 행에 대응했다.
[LG1](../compare/LISFLOOD-FP-conclusion-verify-LG1.md), [LV1](../compare/LISFLOOD-FP-conclusion-verify-LV1.md), [LI2](../compare/LISFLOOD-FP-conclusion-verify-LI2.md), [LI1](../compare/LISFLOOD-FP-conclusion-verify-LI1.md), [LT1](../compare/LISFLOOD-FP-conclusion-verify-LT1.md)의 최종 분류와 결론을 각각 대조했다.
[Claude 최종 조정](../compare/LISFLOOD-FP-conclusion-claude-final.md)의 조정 행도 확인했다.
그 조정 행은 이 배정 구간에 없다.
[외부 근거 보고서](../compare/LISFLOOD-FP-external-sources.md)의 끝 절도 확인했다.
해당 끝 절의 조정 행은 이 배정 구간에 없다.

현재 코드의 기준 경로는 `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/`이다.
아래 목록의 `파일:N`은 이 경로 아래의 원문 줄이다.
`v8.0:`·`v8.1:`·`v8.2:` 인용은 사용자 지정 이전 배포본 원문과 대조했다.
8.3 변경 여부는 `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP-8.3-package/lisflood-8.2-to-8.3.patch`와 대조했다.
옛 노트 인용은 `git show bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md`의 24·31·45·55·58·61행과 대조했다.
관련 보고서의 §4 수정안은 지정된 최종 결론과 함께 대조했다.

문서의 숫자·표·조건은 사용자 지정 쪽 이미지로 판정했다.
PDF 대조 쪽은 p.1–2·4–5·7·10–22·24–27·29–42이다.
DOCX 대조 쪽은 변환본 p.4·14–16·19–26·30–32·35–44이다.
쪽별 판독 기록은 이미지의 절 제목과 쪽 위치를 확인하는 데 함께 사용했다.

## 정정·보완 목록

아래 위치의 파일명은 모두 대상 노트 `models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary-differences.md`이다.
줄 번호는 완료 시점의 번호이다.
각 변경 표식은 해당 행의 결론 문장 칸 끝에 붙였다.

### 1. cpu-gpu-swe:LG1-147 — 보완

위치: `lisflood-fp-io-boundary-differences.md:153`.

전: Metal 원문: Metal은 호스트 입력 결과를 받는다.

후: Metal 원문: Metal은 호스트 입력 결과를 받는다(`metal/fv1/metal_fv1_simulate.mm:1312–1315·1367`).

근거 원문: 원문은 `sim.initialize(arrays.H, arrays.HU, arrays.HV, arrays.DEM, arrays.Manningsn);`와 `impl->copyToGPU(H, HU, HV, DEM, Mann);`이다. metal/fv1/metal_fv1_simulate.mm:1312–1315의 copyToGPU 호출; :1367의 sim.initialize(arrays.H, arrays.HU, arrays.HV, arrays.DEM, arrays.Manningsn)

### 2. cpu-gpu-swe:LG1-148 — 보완

위치: `lisflood-fp-io-boundary-differences.md:154`.

전: Metal 원문: Metal은 CPU 입력 결과를 복사한다.

후: Metal 원문: Metal은 CPU 입력 결과를 복사한다(`metal/fv1/metal_fv1_simulate.mm:575–577·1312–1315·1367`).

근거 원문: 원문은 `float h = (float)h_H[cpu_idx];`와 `d_H[gpu_idx] = h;`이다. metal/fv1/metal_fv1_simulate.mm:575–577의 h_H에서 d_H로 복사; :1312–1315·1367의 초기화 연결

### 3. docx-manual:LV1-136 — 정정

위치: `lisflood-fp-io-boundary-differences.md:165`.

전: 현재 loader의 점원 임시 배열은 20,000개다.

후: 현재 loader는 점원 좌표 임시 배열마다 원소 20,000개를 할당한다.

근거 원문: 원문은 `int pi = -1, maxpi = 20000;`와 `BCptr->xpi = new int[maxpi];` 및 `BCptr->ypi = new int[maxpi];`이다. input.cpp:1533의 maxpi = 20000과 :1542–1543의 xpi·ypi 각각 new int[maxpi]를 확인했다. 최종 LV1-136의 판정 이유도 배열의 고정 크기를 20000으로 설명한다. 배열 개수와 원소 개수를 구분했다.

### 4. docx-manual:LV1-141 — 정정

위치: `lisflood-fp-io-boundary-differences.md:166`.

전: PDF 대조: user manual.pdf p.27과 같음.

후: PDF 대조: user manual.pdf p.26–27과 같음.

근거 원문: PDF p.26은 시간 단위를 `days`, `hours`, `seconds`로 열거한다. PDF p.27에는 `Currently the only supported units are “seconds” and “hours”`가 있다. PDF p.26의 형식 목록에는 days가 있다. p.27의 본문은 seconds·hours만 적는다. 최종 LV1-141의 근거 목록도 p.26–27이다.

### 5. docx-manual:LV1-165 — 정정

위치: `lisflood-fp-io-boundary-differences.md:170`.

전: cuda/acc_nugrid/S는 x로 합산하지만 y로 길이를 제한한다.

후: N/S는 x로 합산하지만 y로 길이를 제한한다.

근거 원문: 최종 LV1-165의 결론 원문은 `N/S는 x로 합산하지만 y로 길이를 제한한다.`이다. `input.cpp:2338–2340`의 N/S 분기는 `gauge_grid_y`와 `ysz`를 사용한다. `util.cpp:242–250`의 N/S 합산은 x 방향 인덱스를 사용한다. input.cpp:2338–2343; util.cpp:242–259; conclusion-verify-LV1.md:148의 N/S 원문

### 6. docx-manual:LV1-200 — 정정

위치: `lisflood-fp-io-boundary-differences.md:178`.

전: PDF 대조: user manual.pdf p.36과 같음.

후: PDF 대조: user manual.pdf p.36–37과 같음.

근거 원문: PDF p.37의 원문은 `Numbering of overpass times commences at zero.`이다. PDF p.36은 .op·.opelev의 설명과 파일 이름 형식이다. 번호가 0에서 시작한다는 문장은 p.37 첫 문단이다. 최종 LV1-200의 근거 목록도 p.36–37이다.

### 7. docx-manual:LV1-215 — 정정

위치: `lisflood-fp-io-boundary-differences.md:182`.

전: `lisflood.cpp:762–768`은 debug일 때 진단 함수를 호출한 뒤 `.dem`을 별도로 항상 쓴다.

후: `lisflood.cpp:756–768`은 `if (Statesptr->maxdepthonly == ON)`의 `else`에서 `.dem`을 debug 조건과 별개로 쓴다.

근거 원문: 원문은 `if (Statesptr->maxdepthonly == ON)` 다음의 빈 블록과 `else`이다. `if (Statesptr->debugmode == ON)`이 감싸는 호출은 `debugfileoutput(Fnameptr, Statesptr, Parptr, Arrptr);`이다. `.dem`의 두 `write_ascfile` 호출은 그 debug 조건 밖에 있다. lisflood.cpp:756–768의 maxdepthonly 분기; conclusion-verify-LV1.md:185

### 8. docx-manual:LV1-218 — 정정

위치: `lisflood-fp-io-boundary-differences.md:184`.

전: PDF 대조: user manual.pdf p.39와 같음.

후: PDF 대조: user manual.pdf p.39–40과 같음.

근거 원문: PDF p.39는 `As all of the output files (and input files) are simple, space character delimited text files`라고 적는다. PDF p.40은 `All gridded output data from the model is in ARC ascii raster format`이라고 적는다. user manual.pdf 쪽 이미지 p.39의 모든 입출력 텍스트 문장과 p.40의 모든 격자 ARC ASCII 문장을 각각 확인했다. 최종 LV1-218의 근거 목록도 p.39–40이다.

### 9. docx-manual:LV1-245 — 정정

위치: `lisflood-fp-io-boundary-differences.md:188`.

전: `input.cpp:2189`의 마스크 읽기.

후: `input.cpp:2190`의 마스크 읽기.

근거 원문: 읽기 원문은 `fscanf(fp, "%" NUM_FMT"", Arrptr->Rainmask + i + j*Parptr->xsz);`이다. input.cpp:2189는 여는 중괄호이다. :2190은 fscanf(fp, "%" NUM_FMT"", Arrptr->Rainmask + i + j*Parptr->xsz)이다.

### 10. docx-manual:LV1-255 — 정정

위치: `lisflood-fp-io-boundary-differences.md:190`.

전: user manual.docx p.19–26(변환본) 표 4–6; user manual.pdf p.15–21 표 4–6

후: user manual.docx p.19–26(변환본) §3.2.1·표 5–11; user manual.pdf p.15–21 §3.2.1·표 5–11

근거 원문: §3.2.1이 열거한 번호는 `Table 5`부터 `Table 11`까지이다. `Table 4`는 입력 자료 요구 표이다. docx p.19와 PDF p.15의 §3.2.1은 키워드 표를 Table 5부터 Table 11까지 열거한다. docx p.20–26 및 PDF p.16–21의 쪽 이미지와 대조했다.

### 11. docx-manual:LV1-257 — 정정

위치: `lisflood-fp-io-boundary-differences.md:191`.

전: user manual.docx p.19–26(변환본) 표 4–6; user manual.pdf p.15–21 표 4–6

후: user manual.docx p.19–26(변환본) §3.2.1·표 5–11; user manual.pdf p.15–21 §3.2.1·표 5–11

근거 원문: §3.2.1이 열거한 번호는 `Table 5`부터 `Table 11`까지이다. `Table 4`는 입력 자료 요구 표이다. docx p.19와 PDF p.15의 §3.2.1은 키워드 표를 Table 5부터 Table 11까지 열거한다. docx p.20–26 및 PDF p.16–21의 쪽 이미지와 대조했다.

### 12. docx-manual:LV1-260 — 정정

위치: `lisflood-fp-io-boundary-differences.md:193`.

전: user manual.docx p.19–26(변환본) 표 4–6; user manual.pdf p.15–21 표 4–6

후: user manual.docx p.19–26(변환본) §3.2.1·표 5–11; user manual.pdf p.15–21 §3.2.1·표 5–11

근거 원문: §3.2.1이 열거한 번호는 `Table 5`부터 `Table 11`까지이다. `Table 4`는 입력 자료 요구 표이다. docx p.19와 PDF p.15의 §3.2.1은 키워드 표를 Table 5부터 Table 11까지 열거한다. docx p.20–26 및 PDF p.16–21의 쪽 이미지와 대조했다.

### 13. docx-manual:LV1-263 — 정정

위치: `lisflood-fp-io-boundary-differences.md:194`.

전: user manual.docx p.19–26(변환본) 표 4–6; user manual.pdf p.15–21 표 4–6

후: user manual.docx p.19–26(변환본) §3.2.1·표 5–11; user manual.pdf p.15–21 §3.2.1·표 5–11

근거 원문: §3.2.1이 열거한 번호는 `Table 5`부터 `Table 11`까지이다. `Table 4`는 입력 자료 요구 표이다. docx p.19와 PDF p.15의 §3.2.1은 키워드 표를 Table 5부터 Table 11까지 열거한다. docx p.20–26 및 PDF p.16–21의 쪽 이미지와 대조했다.

### 14. files-output:LI2-151 — 정정

위치: `lisflood-fp-io-boundary-differences.md:209`.

전: 모델 버전 불일치는 경고 후 읽는다.

후: 모델 버전만 다르면 읽기를 계속한다. 경고는 `if(verbose == ON)`일 때 출력한다.

근거 원문: 원문은 `if(version!=LFv) {` 안의 `if(verbose == ON) printf("\nWARNING: LISFLOOD-FP version differs from current version\n");`와 그 블록 뒤의 `fread(&Solverptr->itrn_time,sizeof(NUMERIC_TYPE),1,check_fp);`이다. chkpnt.cpp:106–109의 if(version!=LFv) 안에서 경고만 if(verbose == ON)에 걸린다. 이어지는 fread는 계속 실행된다.

### 15. files-output:LI2-309 — 정정

위치: `lisflood-fp-io-boundary-differences.md:220`.

전: user manual.pdf p.16·22·32

후: user manual.pdf p.16·27·32

근거 원문: PDF p.27의 DEM 헤더에는 `NODATA_value -9999`가 있다. 같은 쪽의 마찰 파일 절 제목은 `3.2.8 Floodplain friction coefficient file (.n.ascii)`이다. user manual.pdf 쪽 이미지 p.22에는 .par 예시와 .river 설명이 있다. DEM의 NODATA_value는 p.27의 DEM 헤더에 있다. 마찰 래스터 설명은 같은 쪽 §3.2.8에 있다. input.cpp:934·1168·1517의 결론은 유지한다.

### 16. par:LI1-361 — 정정

위치: `lisflood-fp-io-boundary-differences.md:287`.

전: `v8.2:pars.cpp:996–1004`

후: `v8.2:pars.cpp:995–1003`

근거 원문: v8.2의 키워드 원문은 `if (read_string_param(param_name, line_number, param_value_ptr, "dynamicrainfile", Fnameptr->dynamicrainfilename, verbose, mode))`이다. 현재 판의 같은 분기는 `pars.cpp:996–1004`이다. v8.2:pars.cpp:995가 dynamicrainfile의 read_string_param이고 1003이 닫는 중괄호이다. bf804e23의 입출력 노트:58과 lisflood-par-vs-code.md §4 LI1-361을 대조했다. 옛 인용은 쟁점인 dynamicrainfall 문장만 발췌하여 남겼다.

같은 행의 옛 노트 인용도 발췌 범위를 줄였다.

전: `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:58` `ascii_out`/`binary_out`/`netcdf_out`(`pars.cpp:384-402`), `depthoff`/`elevoff`/`vtkoff`(283-298), `qoutput`(329), `voutput`/`hazard`(338-363), `maxdepthonly`(333), `gzip`(895). `netcdf_out`의 실제 NetCDF I/O는 본 6파일이 아니라 `lisflood2/`·`rain/` 하위(예: lisflood2/lis2_output.cpp)에 `_NETCDF` 매크로 가드로 존재 — 본 노트 범위 밖. `dynamicrainfall`은 NetCDF 미컴파일 시 abort (`pars.cpp:998-1001`).

후: `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:58` 중 해당 문장: `dynamicrainfall`은 NetCDF 미컴파일 시 abort (`pars.cpp:998-1001`).

이 발췌는 해당 행의 수정 쟁점인 입력 키워드 문장을 보존한다. 옛 범위 제한 문장은 사용자 지시 6에 따라 인용에서 제외했다.

### 17. theory:LT1-082 — 보완

위치: `lisflood-fp-io-boundary-differences.md:289`.

전: `infevap.cpp:371`의 조건은 LT1-081에 인용했다.

후: `infevap.cpp:371`의 조건은 `if(h0<Solverptr->DepthThresh || Sfy>=Parptr->RouteSfThresh || Sfx>=Parptr->RouteSfThresh)`이다.

근거 원문: 원문은 `if(h0<Solverptr->DepthThresh || Sfy>=Parptr->RouteSfThresh || Sfx>=Parptr->RouteSfThresh)`이다. LT1-081은 별도 lisflood-theory-vs-code.md:175에 있다. 이 노트에는 해당 행이 없으므로 현재 infevap.cpp:371의 조건식을 직접 인용했다. LT1-082 최종 결론의 조건식도 같다.

## 최종 확인

배정한 행 ID 152개가 빠짐없이 남아 있다.
각 행의 표 칸 수는 6개이다.
최종 결론 분류는 A 24행, B 15행, C 89행, E 23행, F 1행이다.
152개 행의 분류는 최종 결론 목록과 같다.
E 23행의 근거 강도는 최종 재검증 행과 같다.
호출되지 않는 충돌 검사 경로의 표시는 유지했다.
고전 증발의 v8.0·v8.1·v8.2 루프는 현재 루프와 같다.
8.3 패치의 변경 파일 목록에 `infevap.cpp`는 없다.
이 근거는 LT1-314의 “8.3 패치는 이 부분을 고치지 않는다”는 결론과 같다.

코드 인용 967개를 해당 파일의 지정 줄과 기계 대조했다.
공백과 표의 파이프 이스케이프를 정규화한 뒤 남은 인용 불일치는 0개이다.
이 기계 대조와 별도로 설명 문장·조건·단위·분류·인용 위치를 원문과 대조했다.
상대 링크 152개는 모두 노트 위치를 기준으로 실제 파일을 가리킨다.
배정 구간에는 사용자 홈의 절대 경로가 없다.
배정 구간에는 물결표 홈 경로와 위키 링크 구문이 없다.
배정 구간에는 미검수·후속 대상으로 남긴 문장이 없다.
수정한 17개 행에는 정정 또는 보완 표식이 있다.
표식은 모두 결론 문장 칸 끝에 있다.

LV1-136의 최종 결론 문구는 원문의 배열 원소 수를 명확히 하도록 정정했다.
LI2-151의 최종 결론 문구는 원문의 verbose 조건을 복원했다.
두 행의 분류는 유지했다.
LI1-316에 대한 최종 보고서의 실행 한계 문장은 사용자 지시 6에 따라 노트에서 제외된 상태를 유지했다.

기계 확인 후보 판정: 사용자 제공 후보 없음.
미해결 항목: 없음.
배정 구간 2/2의 전수 대조를 완료했다.
