# ADCIRC upstream 영향 대조 — 저장 자료 한정

AI 분석 결과. 아래 노트 발췌·diff와 분석 판단을 구분하며 canonical 노트 수정안 또는 실행 검증 결과가 아니다.

범위: `6037225ce4573efd3c1f8877a5dc908d01c199a8` → `e8b62a70db39dbc8875785ee999a2214be75302b`. **14커밋, 31개 고유 파일, 45 commit×file 변경 단위**. 분류: **NOTE_IMPACTING 21개**, **POSSIBLY_IMPACTING 12개**, **NON_IMPACTING 12개**.

## 방법·범위·검증

- 네트워크 및 raw 소스 조회 없이 compare.json, commits/, commit-details/, patches/, SHA256MANIFEST.csv, NOTE_REFERENCES.csv와 필요한 ADCIRC Markdown 노트만 대조했다. 쓰기는 이 디렉터리의 결과물에 한정했다.
- manifest 60개 원자료의 bytes/SHA-256 일치. compare의 31 patch와 patches/ 전문 일치. 14커밋 parent 체인이 baseline에서 tip까지 연결된다. commit_date는 **author date**이며 정렬은 날짜가 아닌 compare/parent 순서다.
- NOTE_REFERENCES.csv 2,200행/61개 노트를 검사했다. ref_file은 전체 raw 경로 접두사 제거, 정확한 상대경로, 고유 basename 순으로 정규화했다. URL 유사 오탐(예: //github.c)은 파일 참조로 매칭하지 않았다. 변경 파일 직접 매칭은 **463 CSV행**, 반복 변경을 포함한 대조는 **786 참조×commit×file**이다.
- CSV의 file-kind에도 `[file=... line=...]`가 들어 있으므로 해당 노트 원문 행에서 숫자를 보완했다. `file:1-3,5-7`의 후속 범위도 포함했다. 파일 소속이 불명확한 단독 `:123`은 임의로 귀속하지 않았다. 원장에는 각 CSV 원행 번호(헤더=1)를 남겼다. symbol은 아래 별도 매칭 원장으로 보완한다.
- hunk 헤더와 +/- 본문으로 줄 대응을 구성하고, baseline 인용 좌표를 parent 체인을 따라 옮긴 뒤 해당 커밋의 이동을 판정했다. 컨텍스트 줄 자체는 변경으로 세지 않는다. 동수 교체는 위치를 보존하되 내용 변경 표시; 비동수 교체·삭제점은 정확한 대응 unknown. 이는 **노트 좌표가 baseline 좌표라는 조건부 대조**이며 과거부터 틀린 인용을 원소스로 재검증하지 않았다.
- CSV line_shift는 해당 파일의 숫자 인용 중 하나라도 이번 커밋에서 이동하면 yes, 모두 그대로면 no, 숫자 인용이 없거나 대응이 불명확하면 unknown. 일부 yes와 unknown이 섞이면 yes이며 상세 원장에 unknown을 보존한다. 파일 전체 행 수 변화와 다르다. NOTE는 기술 서술뿐 아니라 인용 주소 이동도 포함하므로 NOTE가 곧 노트 전체 오류를 뜻하지 않는다.
- 빌드 의존성(KP 전달), 주석 제거, affiliation/CITATION은 사용자 지시에 따라 NON_IMPACTING 우선. 이들에도 인용 줄 이동은 기록한다. 반면 Fortran 출력 FORMAT I6→I12는 출력 레코드 변경이고, SWAN !ADC/!NADC 표식은 조건 선택용 소스 지점이므로 단순 주석 정리로 제외하지 않았다. 표식의 실제 빌드 전개는 이번 범위에서 검증하지 않았다.
- 각 파일의 판정은 가장 강한 확인 근거를 반영한다. 같은 파일 안의 무관·유지되는 인용은 원장에서 NON으로 분리한다. 파일만 인용하여 일치가 불분명하면 POSSIBLE; 상세에서 명시한 심볼/주제 anchor가 더 강한 근거를 제공할 수 있다.

## 커밋별 요약

| SHA | author date | 파일 단위 | NOTE | POSSIBLE | NON | 메시지 |
|---|---|---:|---:|---:|---:|---|
| 69f5fbba209e | 2026-05-29T23:31:09Z | 1 | 1 | 0 | 0 | Fixing #505 - incorrect h0 assignment for node 2 |
| 8c547d26c19b | 2026-06-18T23:15:49Z | 1 | 0 | 1 | 0 | Fixing issue where coincident nodes could corrupt the neighbor table |
| aef3777ed09d | 2026-06-26T13:27:47Z | 1 | 0 | 0 | 1 | Adding CITATION.cff so that Zenodo picks up the correct metadata |
| e65ef6063673 | 2026-06-01T00:12:33Z | 7 | 7 | 0 | 0 | Fix multiple 3D baroclinic model routines |
| f7e98050e025 | 2026-06-11T20:34:05Z | 1 | 1 | 0 | 0 | Restore depth-dependent scalar diffusivity for 3D temperature |
| bf6957a976d9 | 2026-06-20T16:51:30Z | 2 | 0 | 0 | 2 | Avoid GLOBAL_3DVS dependency in nodalattr legacy build |
| 8a80ef218a6c | 2026-07-08T05:06:10Z | 3 | 0 | 0 | 3 | Cleaning up comments in code |
| e5995720925d | 2026-06-16T22:27:48Z | 1 | 1 | 0 | 0 | Following convention for opening only a small subset of prep files at a time for prep20 |
| bdc531653bef | 2026-07-10T15:58:08Z | 2 | 2 | 0 | 0 | Write velocity output in the input frame on rotated-pole meshes |
| daae7d9f9edc | 2026-07-24T14:53:59Z | 1 | 1 | 0 | 0 | Fix potential out-of-bounds access in CondensedNodesDefVal |
| 976fc5b6cafb | 2026-03-05T17:46:48Z | 17 | 6 | 11 | 0 | Adding SWAN temporal controls |
| 5203dafc6871 | 2026-08-24T16:51:44Z | 1 | 1 | 0 | 0 | Fix for segmentation fault in CondensedNodesDefVal allocation |
| 40201037d1a6 | 2026-08-27T21:46:04Z | 6 | 0 | 0 | 6 | Updating affiliations |
| e8b62a70db39 | 2026-08-31T15:31:49Z | 1 | 1 | 0 | 0 | Fix redundant (de)allocation in CondensedNodesDefVal |

## NOTE_IMPACTING 목록 — 21개 변경 단위

대표 근거 노트만 이 표에 표시하며 모든 관련 노트/행은 CSV 및 전수 원장을 참조한다.

| SHA | 변경 파일 | 대표 노트 인용 |
|---|---|---|
| 69f5fbba209e | src/gwce.F | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:29; models/ADCIRC/source-analysis/adcirc-3d-mode.md:25 |
| e65ef6063673 | src/cstart.F | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:60; models/ADCIRC/source-analysis/adcirc-3d-mode.md:15 |
| e65ef6063673 | src/hstart.F | models/ADCIRC/source-analysis/adcirc-hotstart.md:21; models/ADCIRC/source-analysis/adcirc-hotstart.md:130 |
| e65ef6063673 | src/netcdfio.F90 | models/ADCIRC/source-analysis/adcirc-hotstart.md:24; models/ADCIRC/source-analysis/adcirc-swan-coupling.md:25 |
| e65ef6063673 | src/nodalattr.F | models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:30; models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:19 |
| e65ef6063673 | src/read_input.F | models/ADCIRC/source-analysis/adcirc-3d-mode.md:70; models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:254 |
| e65ef6063673 | src/vsmy.F | models/ADCIRC/source-analysis/adcirc-3d-mode.md:26; models/ADCIRC/source-analysis/adcirc-transport-solver.md:20 |
| e65ef6063673 | src/write_output.F | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:77; models/ADCIRC/source-analysis/adcirc-hotstart.md:22 |
| f7e98050e025 | src/vsmy.F | models/ADCIRC/source-analysis/adcirc-3d-mode.md:26; models/ADCIRC/source-analysis/adcirc-3d-mode.md:122; models/ADCIRC/source-analysis/adcirc-hotstart.md:86 |
| e5995720925d | prep/prep.F | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:49 |
| bdc531653bef | src/global.F | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:50 |
| bdc531653bef | src/write_output.F | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:47; models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:49 |
| daae7d9f9edc | src/nodalattr.F | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51; models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:42 |
| 976fc5b6cafb | prep/prep.F | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:200 |
| 976fc5b6cafb | prep/presizes.F | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:199 |
| 976fc5b6cafb | src/couple2swan.F | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:193; models/ADCIRC/source-analysis/adcirc-swan-coupling.md:201; models/ADCIRC/source-analysis/adcirc-swan-coupling.md:222 |
| 976fc5b6cafb | src/global.F | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:186; models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:50 |
| 976fc5b6cafb | src/nodalattr.F | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:21; models/ADCIRC/source-analysis/adcirc-swan-coupling.md:178 |
| 976fc5b6cafb | src/read_input.F | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:182; models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:34; models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:49 |
| 5203dafc6871 | src/nodalattr.F | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:21; models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51 |
| e8b62a70db39 | src/nodalattr.F | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51; models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:42 |

## NOTE_IMPACTING·POSSIBLY_IMPACTING 상세

### 69f5fbba209e · src/gwce.F · NOTE_IMPACTING

- commit: `69f5fbba209e3db6fd5a11672fd6496a7e085485`; 상태 `modified`; line_shift **no**.
- 판단: GWCE_New에서 H0N2=H2(NM1)을 H0N2=H1(NM2)로 교체. 노트의 gwce.F:780-1450 및 998-1617 범위 안이며 행 수는 동일. 수치 결과 변화량은 판단하지 않음.
- diff 원천: `commit-details/69f5fbba209e.json` → `files[filename=src/gwce.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -1064,7 +1064,7 @@ SUBROUTINE GWCE_New(IT,ITIME_BGN,TimeLoc,TimeH)
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:29`

  > - RHS forcing assembly at `[file=src/gwce.F line=998-1617]`

- `models/ADCIRC/source-analysis/adcirc-3d-mode.md:25`

  > - `gwce.F:780-1450` — GWCE 3D additions.

대표 줄 대응(전체는 아래 참조 원장):

- CSV#129 `models/ADCIRC/source-analysis/adcirc-3d-mode.md:25`: baseline 780-1450: parent 780..1450 → child 780..1450; Δ=+0; changed/replaced
- CSV#592 `models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:29`: baseline 998-1617: parent 998..1617 → child 998..1617; Δ=+0; changed/replaced

### 8c547d26c19b · src/mesh.F · POSSIBLY_IMPACTING

- commit: `8c547d26c19bf0ba64cdde8aa54e08672341bedc`; 상태 `modified`; line_shift **no**.
- 판단: NEIGHB의 ANGLEMORE 하한 필터를 제거하고 선택한 각도를 400으로 치환; 동각도는 작은 NEITEM 우선. JLOW=0 종료 검사와 csr_position=0 초기화·누락 검사 추가. 노트의 mesh.F:1822-1834는 변경 앞쪽이어서 그대로이며 weir/이웃표 주제만 관련.
- diff 원천: `commit-details/8c547d26c19b.json` → `files[filename=src/mesh.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -3091,7 +3091,7 @@ SUBROUTINE NEIGHB()
@@ -3225,18 +3225,26 @@ SUBROUTINE NEIGHB()
@@ -3341,6 +3349,18 @@ subroutine neighb_terminateDuplicateNode(i,j)
@@ -5259,11 +5279,13 @@ end function onIBTYP64Floodplain
@@ -5276,6 +5298,14 @@ subroutine compute_csr_positions()
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:19`

  > > `weir_boundary.F90`(2715, module `WEIR`) 직접 read. [[adcirc-boundary-conditions]] 의 **internal barrier(IBTYPE 4/24 levee·5/25 +pipes·64 vertical element wall)** 월류(overtopping) 계산의 실제 구현. paired weir node 양쪽 수위차로 둑 위 월류 유량 산출. 제방·방조제·도로 둑의 범람(overtopping flooding) 핵심 — 한국 연안 방조제·storm surge 침수.

숫자 인용의 직접 이동/교집합은 위 근거만으로 확인되지 않음. 심볼·주제 일치와 불확실성을 구분해 판정했다.

### e65ef6063673 · src/cstart.F · NOTE_IMPACTING

- commit: `e65ef606367369e38e09d724f69d7aafc8cdd3e4`; 상태 `modified`; line_shift **yes**.
- 판단: COLDSTART_3D의 fort.39 열기를 BndBCRiver AND IDEN=2/3/4로 제한하고 STATUS=OLD,ACTION=READ 추가. 하류의 초기 dry-node 인용은 +5행 이동.
- diff 원천: `commit-details/e65ef6063673.json` → `files[filename=src/cstart.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -957,8 +957,13 @@ SUBROUTINE COLDSTART_3D()
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:60`

  > - No-flux land suppression via `NODECODE` masking at `[file=src/gwce.F line=474-477, 1010-1015]`; dry/landlocked nodes init in cold start at `[file=src/cstart.F line=1221-1223, 1258-1260]`

- `models/ADCIRC/source-analysis/adcirc-3d-mode.md:15`

  > 

대표 줄 대응(전체는 아래 참조 원장):

- CSV#638 `models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:60`: baseline 1221-1223: parent 1221..1223 → child 1226..1228; Δ=+5; baseline 1258-1260: parent 1258..1260 → child 1263..1265; Δ=+5
- CSV#649 `models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:74`: baseline 1221-1231: parent 1221..1231 → child 1226..1236; Δ=+5; baseline 1258-1268: parent 1258..1268 → child 1263..1273; Δ=+5

### e65ef6063673 · src/hstart.F · NOTE_IMPACTING

- commit: `e65ef606367369e38e09d724f69d7aafc8cdd3e4`; 상태 `modified`; line_shift **yes**.
- 판단: ITHS=0이면 DTDPHS=DTDP; heat flux 읽기 반복 NH→NP; fort.39 조건에 IDEN=2/3/4; initOutput3D 인수 IRType→IDen; fort.47 헤더를 ABS(I3DGD)=1 및 로컬/전역·rank 조건에 따라 작성. HOTSTART 인용 범위와 하류 좌표 영향.
- diff 원천: `commit-details/e65ef6063673.json` → `files[filename=src/hstart.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -716,7 +716,12 @@ SUBROUTINE binaryRead2D(array, length, lun, counter)
@@ -2060,6 +2065,8 @@ END SUBROUTINE HOTSTART
@@ -2255,7 +2262,8 @@ SUBROUTINE HOTSTART_3D(TimeLoc,ITHS)
@@ -2373,8 +2381,13 @@ SUBROUTINE HOTSTART_3D(TimeLoc,ITHS)
@@ -2512,17 +2525,46 @@ SUBROUTINE HOTSTART_3D(TimeLoc,ITHS)
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-hotstart.md:21`

  > - `hstart.F:47-3048` — main reader, mappers, 3D reader.

- `models/ADCIRC/source-analysis/adcirc-hotstart.md:130`

  > Meteorology is **not preserved** — reconstructed at `TimeLoc` from forcing files (`hstart.F:1440-1444`).

대표 줄 대응(전체는 아래 참조 원장):

- CSV#603 `models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:37`: baseline 719-720: parent 719..720 → child 725..725 [?]; Δ=+5; changed/replaced; 삭제/치환점 정확한 대응 불명
- CSV#642 `models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:65`: baseline 1522-1522: parent 1522..1522 → child 1527..1527; Δ=+5; baseline 1530-1532: parent 1530..1532 → child 1535..1537; Δ=+5
- CSV#680 `models/ADCIRC/source-analysis/adcirc-hotstart.md:21`: baseline 47-3048: parent 47..3048 → child 47..3090 [?]; Δ=+0/+5/+7/+8/+13/+42; changed/replaced; 삭제/치환점 정확한 대응 불명

### e65ef6063673 · src/netcdfio.F90 · NOTE_IMPACTING

- commit: `e65ef606367369e38e09d724f69d7aafc8cdd3e4`; 상태 `modified`; line_shift **yes**.
- 판단: 3D salinity/temperature 정의·쓰기 및 hotstart 조건의 IDEN을 abs(IDEN)으로 교체; temperature long_name 정정; temperature varid 대상 nodal_data_id→w_nodal_data_id; l 읽기 velocity3D→turbulence3D. 기존 NetCDF hotstart 인용 범위와 좌표에 영향.
- diff 원천: `commit-details/e65ef6063673.json` → `files[filename=src/netcdfio.F90].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -675,12 +675,16 @@ subroutine initStationFile(sta, descript1, reterr)
@@ -699,7 +703,9 @@ subroutine initStationFile(sta, descript1, reterr)
@@ -715,7 +721,9 @@ subroutine initStationFile(sta, descript1, reterr)
@@ -1365,12 +1373,16 @@ subroutine initStationFile(sta, descript1, reterr)
@@ -1547,12 +1559,16 @@ subroutine initNodalDataFile(dat, descript1, reterr)
@@ -1569,7 +1585,9 @@ subroutine initNodalDataFile(dat, descript1, reterr)
@@ -1582,7 +1600,9 @@ subroutine initNodalDataFile(dat, descript1, reterr)
@@ -3610,12 +3630,16 @@ subroutine initNodalDataFile(dat, descript1, reterr)
@@ -4353,7 +4377,9 @@ subroutine writeStationData(sta, lun, descript1, timesec, &
@@ -4367,7 +4393,9 @@ subroutine writeStationData(sta, lun, descript1, timesec, &
@@ -4656,12 +4684,16 @@ subroutine writeNodalData(dat, lun, descript1, timesec, &
@@ -4870,6 +4902,7 @@ subroutine writeNodalData(dat, lun, descript1, timesec, &
@@ -4880,7 +4913,7 @@ subroutine writeNodalData(dat, lun, descript1, timesec, &
@@ -4890,7 +4923,7 @@ subroutine writeNodalData(dat, lun, descript1, timesec, &
@@ -6559,7 +6592,9 @@ subroutine initNetCDFHotstart3D(lun, netcdf_format)
@@ -6571,7 +6606,9 @@ subroutine initNetCDFHotstart3D(lun, netcdf_format)
@@ -6584,12 +6621,16 @@ subroutine initNetCDFHotstart3D(lun, netcdf_format)
@@ -6692,17 +6733,23 @@ subroutine initNetCDFHotstart3D(lun, netcdf_format)
@@ -7806,7 +7853,9 @@ subroutine writeNetCDFHotstart3DVar(lun, descript)
@@ -9407,7 +9456,9 @@ subroutine readNetCDFHotstart3D(lun)
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-hotstart.md:24`

  > - `netcdfio.F90:3866-9188` — NetCDF naming, definitions, read/write.

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:25`

  > - `hstart.F:325-337`, `write_output.F:4969-5112`, `netcdfio.F90:5555-7045, 8017-8085` — hot-start.

대표 줄 대응(전체는 아래 참조 원장):

- CSV#684 `models/ADCIRC/source-analysis/adcirc-hotstart.md:24`: baseline 3866-9188: parent 3866..9188 → child 3890..9237 [?]; Δ=+24/+26/+28/+30/+32/+33/+35/+37/+39/+41/+43/+45/+47/+49; changed/replaced; 삭제/치환점 정확한 대응 불명
- CSV#707 `models/ADCIRC/source-analysis/adcirc-hotstart.md:90`: baseline 3866-3871: parent 3866..3871 → child 3890..3895; Δ=+24
- CSV#718 `models/ADCIRC/source-analysis/adcirc-hotstart.md:123`: baseline 5357-5380: parent 5357..5380 → child 5390..5413; Δ=+33

### e65ef6063673 · src/nodalattr.F · NOTE_IMPACTING

- commit: `e65ef606367369e38e09d724f69d7aafc8cdd3e4`; 상태 `modified`; line_shift **no**.
- 판단: Apply3DBottomFriction에 H1<H0이면 H1=H0 및 TK(NH)를 abs(Q(NH,1)) 이하·KP*abs(Q(NH,1)) 이상으로 제한하는 두 IF 추가. 노트가 호출 심볼을 명시; 2D Manning 공식 변경으로 확대 해석하지 않음.
- diff 원천: `commit-details/e65ef6063673.json` → `files[filename=src/nodalattr.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -2446,6 +2446,11 @@ END SUBROUTINE Apply2DBottomFriction
@@ -2474,6 +2479,9 @@ SUBROUTINE Apply3DBottomFriction(Q, SIGMA, DP, ETA2, G,
@@ -2496,6 +2504,9 @@ SUBROUTINE Apply3DBottomFriction(Q, SIGMA, DP, ETA2, G,
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:30`

  > | 4 | **bottom friction** `Apply2DBottomFriction`(→TK) + `Apply2DInternalWaveDrag` + `Apply2DMomentumDisp` / 3D `Apply3DBottomFriction` | 210-226 |

- `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:19`

  > > `src/nodalattr.F`(3193) 직접 read. ADCIRC 의 **공간변화 파라미터**(fort.13) 시스템 — bottom friction·tau0·wind roughness·canopy·internal tide 등을 node별로 지정. [[adcirc-momentum-implementation]] 의 `FRIC`(bottom friction 계수)·[[adcirc-gwce-implementation]] 의 tau0·[[adcirc-tidal-forcing]] 의 internal tide drag 의 **입력 소스**. fort.15 의 `NWP` + fort.13 파일.

숫자 인용의 직접 이동/교집합은 위 근거만으로 확인되지 않음. 심볼·주제 일치와 불확실성을 구분해 판정했다.

### e65ef6063673 · src/read_input.F · NOTE_IMPACTING

- commit: `e65ef606367369e38e09d724f69d7aafc8cdd3e4`; 상태 `modified`; line_shift **yes**.
- 판단: READ_INPUT_3D의 ABS(RES_BC_FLAG)=3/4 파싱을 공유하고 TTBCTIMEINC/TTBCSTATIM 읽기를 NOPE>0 내부에서 밖으로 이동. 뒤쪽 EOS·SAL reader 인용 좌표 +24행; NWS/조석 합성 알고리즘 변경 근거는 없음.
- diff 원천: `commit-details/e65ef6063673.json` → `files[filename=src/read_input.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -5520,7 +5520,8 @@ SUBROUTINE READ_INPUT_3D(StaTime,NT)
@@ -5550,47 +5551,70 @@ SUBROUTINE READ_INPUT_3D(StaTime,NT)
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-3d-mode.md:70`

  > `Eqnstate` from input (`read_input.F:5682`):

- `models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:254`

  > Called from main startup (`adcirc.F:292-293`); reader at `read_input.F:6282-6463`.

대표 줄 대응(전체는 아래 참조 원장):

- CSV#123 `models/ADCIRC/source-analysis/adcirc-3d-mode.md:20`: baseline 1176-1191: parent 1176..1191 → child 1176..1191; Δ=+0; baseline 3072-3072: parent 3072..3072 → child 3072..3072; Δ=+0; baseline 5139-5482: parent 5139..5482 → child 5139..5482; Δ=+0; baseline 5682-5682: parent 5682..5682 → child 5706..5706; Δ=+24
- CSV#146 `models/ADCIRC/source-analysis/adcirc-3d-mode.md:70`: baseline 5682-5682: parent 5682..5682 → child 5706..5706; Δ=+24
- CSV#373 `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:54`: baseline 6425-6425: parent 6425..6425 → child 6449..6449; Δ=+24; baseline 6453-6453: parent 6453..6453 → child 6477..6477; Δ=+24

### e65ef6063673 · src/vsmy.F · NOTE_IMPACTING

- commit: `e65ef606367369e38e09d724f69d7aafc8cdd3e4`; 상태 `modified`; line_shift **yes**.
- 판단: VSSOL의 river T/S 갱신을 IDEN=2/3/4로 제한. CALC_SIGMAT_3D에서 보간 SALM/TEMPM을 S_min/S_max,T_min/T_max로 제한. VSSOL/EOS 인용 범위와 후속 dispatch 줄 번호에 영향.
- diff 원천: `commit-details/e65ef6063673.json` → `files[filename=src/vsmy.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -1479,8 +1479,10 @@ SUBROUTINE VSSOL(IT,TimeLoc)
@@ -4053,6 +4055,19 @@ SUBROUTINE CALC_SIGMAT_3D ()
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-3d-mode.md:26`

  > - `vsmy.F:1168, 1543-3871, 4061-4315` — internal solve, EOS, MY2.5.

- `models/ADCIRC/source-analysis/adcirc-transport-solver.md:20`

  > > **정체**: 3D baroclinic **염분/수온 이류-확산** solver(sigma 좌표). 하나의 generic in/out 배열로 S·T 모두 처리 — ADCIRC prognostic 성층 엔진(하구 성층·thermohaline surge). dispatch: `vsmy.F:1548-1553` `CALL TRANS_3D(SAL,NLSD,NVSD,...)` + `(TEMP,NLTD,NVTD,...)`.

대표 줄 대응(전체는 아래 참조 원장):

- CSV#130 `models/ADCIRC/source-analysis/adcirc-3d-mode.md:26`: baseline 1168-1168: parent 1168..1168 → child 1168..1168; Δ=+0; baseline 1543-3871: parent 1543..3871 → child 1545..3873; Δ=+2; baseline 4061-4315: parent 4061..4315 → child 4076..4330; Δ=+15
- CSV#141 `models/ADCIRC/source-analysis/adcirc-3d-mode.md:60`: baseline 1548-1553: parent 1548..1553 → child 1550..1555; Δ=+2
- CSV#145 `models/ADCIRC/source-analysis/adcirc-3d-mode.md:68`: baseline 1630-1630: parent 1630..1630 → child 1632..1632; Δ=+2

### e65ef6063673 · src/write_output.F · NOTE_IMPACTING

- commit: `e65ef606367369e38e09d724f69d7aafc8cdd3e4`; 상태 `modified`; line_shift **yes**.
- 판단: 3D 출력 FORMAT I6→I12(데이터 레코드 형식 변경); fort.47 ASCII 쓰기를 rank 0으로 제한하고 QSurfKp1Descript%array_g 연결; NetCDF qsurfkp1 전역 gather/해제 추가. 단순 소스 포맷 정리가 아님. 하류 writer/hotstart 인용 이동.
- diff 원천: `commit-details/e65ef6063673.json` → `files[filename=src/write_output.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -2970,7 +2970,8 @@ SUBROUTINE writeOutput3D(TimeLoc,IT)
@@ -3874,17 +3875,22 @@ SUBROUTINE writeOutput3D(TimeLoc,IT)
@@ -3938,18 +3944,42 @@ SUBROUTINE writeOutput3D(TimeLoc,IT)
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:77`

  > - Descriptor setup: `[file=src/write_output.F line=2980-3103]`

- `models/ADCIRC/source-analysis/adcirc-hotstart.md:22`

  > - `write_output.F:4429, 4920-5374` — binary writer, full vs local.

대표 줄 대응(전체는 아래 참조 원장):

- CSV#132 `models/ADCIRC/source-analysis/adcirc-3d-mode.md:28`: baseline 2993-3331: parent 2993..3331 → child 2994..3332; Δ=+1
- CSV#169 `models/ADCIRC/source-analysis/adcirc-3d-mode.md:135`: baseline 2993-2993: parent 2993..2993 → child 2994..2994; Δ=+1
- CSV#171 `models/ADCIRC/source-analysis/adcirc-3d-mode.md:144`: baseline 3331-3331: parent 3331..3331 → child 3332..3332; Δ=+1

### f7e98050e025 · src/vsmy.F · NOTE_IMPACTING

- commit: `f7e98050e02541ddbe811358f520aee326f3d216`; 상태 `modified`; line_shift **yes**.
- 판단: turb의 NTVMIN=EVMIN을 H≤15:0, 15≤H≤30:(0.001/15)*(H-15), H≥30:0.001 분기로 교체. 3D 혼합을 다루는 노트의 넓은 vsmy.F:1543-3871 범위 안이며 뒤쪽 hotstart/EOS 인용 +5행.
- diff 원천: `commit-details/f7e98050e025.json` → `files[filename=src/vsmy.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -3074,16 +3074,21 @@ subroutine turb(nh,H,bsx_loc,bsy_loc,wsx,wsy,istart,Z0B1)
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-3d-mode.md:26`

  > - `vsmy.F:1168, 1543-3871, 4061-4315` — internal solve, EOS, MY2.5.

- `models/ADCIRC/source-analysis/adcirc-3d-mode.md:122`

  > | `50, 51` | **MY2.5 quasi-equilibrium** (`vsmy.F:2035, 2403`) |

- `models/ADCIRC/source-analysis/adcirc-hotstart.md:86`

  > - 3D: `HSTART3D_OUT(IT)` in `vsmy.F:3254`.

대표 줄 대응(전체는 아래 참조 원장):

- CSV#130 `models/ADCIRC/source-analysis/adcirc-3d-mode.md:26`: baseline 1168-1168: parent 1168..1168 → child 1168..1168; Δ=+0; baseline 1543-3871: parent 1545..3873 → child 1545..3878 [?]; Δ=+0/+1/+5; changed/replaced; 삭제/치환점 정확한 대응 불명; baseline 4061-4315: parent 4076..4330 → child 4081..4335; Δ=+5
- CSV#149 `models/ADCIRC/source-analysis/adcirc-3d-mode.md:74`: baseline 4061-4061: parent 4076..4076 → child 4081..4081; Δ=+5
- CSV#683 `models/ADCIRC/source-analysis/adcirc-hotstart.md:23`: baseline 3254-3254: parent 3256..3256 → child 3261..3261; Δ=+5; baseline 3531-3778: parent 3533..3780 → child 3538..3785; Δ=+5

### e5995720925d · prep/prep.F · NOTE_IMPACTING

- commit: `e5995720925df9b7b8fbe022883bfb38b2b2ff28`; 상태 `modified`; line_shift **yes**.
- 판단: PREP20에서 전체 fort.20을 batch마다 재읽고 startProc..endProc에만 분배; OpenPrepFiles에 IOMSG와 IOSTAT!=0 검사 추가. PREP80 등 뒤쪽 인용 +29행. maxOpenFiles=256이나 endProc=startProc+deltaProc의 포함 구간은 최대 257개이므로 256개 보장을 단정하지 않음.
- diff 원천: `commit-details/e5995720925d.json` → `files[filename=prep/prep.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -3098,6 +3098,10 @@ SUBROUTINE PREP20(sponge)
@@ -3108,64 +3112,76 @@ SUBROUTINE PREP20(sponge)
@@ -7168,6 +7184,7 @@ SUBROUTINE OpenPrepFiles(UnitNumber, Description,
@@ -7207,11 +7224,17 @@ SUBROUTINE OpenPrepFiles(UnitNumber, Description,
@@ -7232,10 +7255,16 @@ SUBROUTINE OpenPrepFiles(UnitNumber, Description,
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:49`

  > `PREP80` writer at `[file=prep/prep.F line=7432]`, header at `[file=prep/prep.F line=7444-7463]`:

대표 줄 대응(전체는 아래 참조 원장):

- CSV#471 `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:109`: baseline 7439-7439: parent 7439..7439 → child 7468..7468; Δ=+29
- CSV#1118 `models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:49`: baseline 7432-7432: parent 7432..7432 → child 7461..7461; Δ=+29; baseline 7444-7463: parent 7444..7463 → child 7473..7492; Δ=+29
- CSV#1119 `models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:49`: baseline 7432-7432: parent 7432..7432 → child 7461..7461; Δ=+29; baseline 7444-7463: parent 7444..7463 → child 7473..7492; Δ=+29

### bdc531653bef · src/global.F · NOTE_IMPACTING

- commit: `bdc531653bef28d00ec882a58ae7264237b34df0`; 상태 `modified`; line_shift **yes**.
- 판단: UU2_GEO/VV2_GEO allocatable TARGET 배열 선언 추가. global.F:387,1045의 조석 관련 인용 좌표는 +6행이며 해당 조석 변수 로직 변경은 없음.
- diff 원천: `commit-details/bdc531653bef.json` → `files[filename=src/global.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -255,6 +255,12 @@ MODULE GLOBAL
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:50`

  >   - Amplitude `EMO(I,J)` and phase `EFA(I,J)` at `[file=src/read_input.F line=3450-3456]`, `[file=src/global.F line=387, 1045]`

대표 줄 대응(전체는 아래 참조 원장):

- CSV#1990 `models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:50`: baseline 387-387: parent 387..387 → child 393..393; Δ=+6; baseline 1045-1045: parent 1045..1045 → child 1051..1051; Δ=+6

### bdc531653bef · src/write_output.F · NOTE_IMPACTING

- commit: `bdc531653bef28d00ec882a58ae7264237b34df0`; 상태 `modified`; line_shift **yes**.
- 판단: IFSPROTS=1일 때 VelSta/Vel descriptor를 UU2_GEO/VV2_GEO로 연결; 출력 직전에 DRVMAP2DSPVEC(...,FWD=.FALSE.)를 호출해 출력 속도를 변환. 기존 fort.62/64 descriptor 인용과 일치. hotstart 보존 의도는 추가 주석에 명시되나 실행 검증은 하지 않음.
- diff 원천: `commit-details/bdc531653bef.json` → `files[filename=src/write_output.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -350,11 +350,12 @@ SUBROUTINE initOutput2D(timeloc)
@@ -553,8 +554,23 @@ SUBROUTINE initOutput2D(timeloc)
@@ -714,8 +730,14 @@ SUBROUTINE initOutput2D(timeloc)
@@ -1770,6 +1792,30 @@ END SUBROUTINE INT_FIELD_ALLOCATE
@@ -1790,9 +1836,12 @@ SUBROUTINE writeOutput2D(IT,TimeLoc)
@@ -1823,6 +1872,16 @@ SUBROUTINE writeOutput2D(IT,TimeLoc)
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:47`

  > - Mirror of elevation structure at `[file=src/write_output.F line=537-563, 710-714]`

- `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:49`

  > - `num_items_per_record = 2` (U,V components) at `[file=src/write_output.F line=548-557, 716-720]`

대표 줄 대응(전체는 아래 참조 원장):

- CSV#132 `models/ADCIRC/source-analysis/adcirc-3d-mode.md:28`: baseline 2993-3331: parent 2994..3332 → child 3053..3391; Δ=+59
- CSV#169 `models/ADCIRC/source-analysis/adcirc-3d-mode.md:135`: baseline 2993-2993: parent 2994..2994 → child 3053..3053; Δ=+59
- CSV#171 `models/ADCIRC/source-analysis/adcirc-3d-mode.md:144`: baseline 3331-3331: parent 3332..3332 → child 3391..3391; Δ=+59

### daae7d9f9edc · src/nodalattr.F · NOTE_IMPACTING

- commit: `daae7d9f9edc29f8016dcc4e4af002c13701db96`; 상태 `modified`; line_shift **yes**.
- 판단: CondensedNodesDefVal(4)을 allocatable(:)로 변경하고 CondensedNodesNoOfVals 크기 할당을 allocateNodalAttributes/fort.13 read에 추가. fort.13 reader 인용 줄 +3행 등; condensed_nodes 카탈로그만으로 메모리 결함 설명 여부는 불확실.
- diff 원천: `commit-details/daae7d9f9edc.json` → `files[filename=src/nodalattr.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -132,7 +132,7 @@ MODULE NodalAttributes
@@ -958,6 +958,9 @@ subroutine allocateNodalAttributes()
@@ -1262,6 +1265,8 @@ SUBROUTINE ReadNodalAttr(NScreen, ScreenUnit, MyProc, NAbOut)
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51`

  > | **13** | Nodal attributes (Manning's n, primitive weighting, bridge piers, surface canopy, etc.) | `NWP > 0` | `ReadNodalAttr` | `[file=src/nodalattr.F line=1141]`, `[file=src/nodalattr.F line=1154]` | `[file=wiki:adcirc:Fort.13_file]`; e.g. `mannings_n_at_sea_floor` `[file=wiki:adcirc:Manning_s_n_at_sea_floor]` requires `NOLIBF=1` |

- `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:42`

  > | `condensed_nodes` | 노드 병합 | mesh |

대표 줄 대응(전체는 아래 참조 원장):

- CSV#361 `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51`: baseline 1141-1141: parent 1141..1141 → child 1144..1144; Δ=+3; baseline 1154-1154: parent 1154..1154 → child 1157..1157; Δ=+3
- CSV#362 `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51`: baseline 1141-1141: parent 1141..1141 → child 1144..1144; Δ=+3; baseline 1154-1154: parent 1154..1154 → child 1157..1157; Δ=+3
- CSV#489 `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:160`: baseline 1051-1051: parent 1051..1051 → child 1054..1054; Δ=+3

### 976fc5b6cafb · prep/prep.F · NOTE_IMPACTING

- commit: `976fc5b6cafb0e8248cac1726f01ef3350b7b860`; 상태 `modified`; line_shift **yes**.
- 판단: PREP15가 SWANTimeControl namelist를 분할 fort.15에 출력. SWAN 노트 200행이 같은 변경을 이미 설명함; 그 뒤 PREP80 인용은 추가 +4행.
- diff 원천: `commit-details/976fc5b6cafb.json` → `files[filename=prep/prep.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -2278,6 +2278,10 @@ SUBROUTINE PREP15()
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:200`

  > | `prep/prep.F` | `PREP15` 에서 `SWANTimeControl` namelist write | 파티션 prep 단계 출력 보존 |

대표 줄 대응(전체는 아래 참조 원장):

- CSV#471 `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:109`: baseline 7439-7439: parent 7468..7468 → child 7472..7472; Δ=+4
- CSV#1118 `models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:49`: baseline 7432-7432: parent 7461..7461 → child 7465..7465; Δ=+4; baseline 7444-7463: parent 7473..7492 → child 7477..7496; Δ=+4
- CSV#1119 `models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:49`: baseline 7432-7432: parent 7461..7461 → child 7465..7465; Δ=+4; baseline 7444-7463: parent 7473..7492 → child 7477..7496; Δ=+4

### 976fc5b6cafb · prep/presizes.F · NOTE_IMPACTING

- commit: `976fc5b6cafb0e8248cac1726f01ef3350b7b860`; 상태 `modified`; line_shift **unknown**.
- 판단: RunStartDateTime import와 SWANTimeControl namelist/읽기 추가; 읽기 실패 시 -99999 설정 후 rewind. 노트 199행에 이미 설명된 지점과 일치.
- diff 원천: `commit-details/976fc5b6cafb.json` → `files[filename=prep/presizes.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -146,6 +146,8 @@ MODULE PRESIZES
@@ -270,6 +272,8 @@ MODULE PRESIZES
@@ -733,6 +737,15 @@ SUBROUTINE SIZEUP15()
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:199`

  > | `prep/presizes.F` | +RunStartDateTime 변수 + SWANTimeControl namelist + SIZEUP15 read with default `"-99999"` | namelist 정의 + fort.15 parse |

숫자 인용의 직접 이동/교집합은 위 근거만으로 확인되지 않음. 심볼·주제 일치와 불확실성을 구분해 판정했다.

### 976fc5b6cafb · src/couple2swan.F · NOTE_IMPACTING

- commit: `976fc5b6cafb0e8248cac1726f01ef3350b7b860`; 상태 `modified`; line_shift **yes**.
- 판단: INIT에서 날짜 offset을 SwanTimeStep에 설정; RUN에서 1..SWAN_MTC일 때만 SWMAIN 호출. 밖에서는 HS/DIR/TM01/TPS/TMM10=-99999, WindX/WindY/TM02=0; 응력의 이전 column 보존 후 새 column=0. 노트의 전체 시간 SWAN 및 등 6개 sentinel·응력 전체 0 요약은 실제 조건/대입과 차이가 있어 재검토 대상.
- diff 원천: `commit-details/976fc5b6cafb.json` → `files[filename=src/couple2swan.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -954,6 +954,8 @@ SUBROUTINE PADCSWAN_INIT
@@ -963,12 +965,16 @@ SUBROUTINE PADCSWAN_INIT
@@ -1079,6 +1085,18 @@ SUBROUTINE PADCSWAN_INIT
@@ -1104,10 +1122,21 @@ SUBROUTINE PADCSWAN_RUN(ITIME)
@@ -1212,7 +1241,55 @@ SUBROUTINE PADCSWAN_RUN(ITIME)
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:193`

  > → namelist 없거나 `RunStartDateTime` 에 `-` 포함 (default sentinel `"-99999"`) 시 **기존 동작 그대로 (전체 시간 SWAN)**. backward-compat.

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:201`

  > | `src/couple2swan.F` | `SwanTimeStep` 초기값 = 0 명시; `PADCSWAN_INIT` 에서 `RunStartDateTime` 파싱 → `SwanTimeStep = NINT((AdcircStartTime - SWAN_TINIC) / SWAN_DT)`; `PADCSWAN_RUN` 에서 `[1, SWAN_MTC]` 범위 밖이면 `SWMAIN` skip + wave output sentinel + radiation stress 0 | 핵심 coupling 제어 |

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:222`

  >    Swan_HSOut(:) = -99999.D0  ! 등 6개 출력 sentinel

대표 줄 대응(전체는 아래 참조 원장):

- CSV#1242 `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:19`: baseline 67-1236: parent 67..1236 → child 67..1313 [?]; Δ=+0/+2/+4/+6/+18/+27/+29/+77; changed/replaced; 삭제/치환점 정확한 대응 불명
- CSV#1265 `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:51`: baseline 950-950: parent 950..950 → child 950..950; Δ=+0; baseline 965-965: parent 965..965 → child 967..967; Δ=+2
- CSV#1268 `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:54`: baseline 1212-1215: parent 1212..1215 → child 1241..1243 [?]; Δ=+29; changed/replaced; 삭제/치환점 정확한 대응 불명

### 976fc5b6cafb · src/global.F · NOTE_IMPACTING

- commit: `976fc5b6cafb0e8248cac1726f01ef3350b7b860`; 상태 `modified`; line_shift **yes**.
- 판단: CHARACTER(LEN=15) RunStartDateTime 선언 추가. SWAN 시간 제어 주제와 관련; 뒤쪽 global.F:387,1045 인용 추가 +2행.
- diff 원천: `commit-details/976fc5b6cafb.json` → `files[filename=src/global.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -316,6 +316,8 @@ MODULE GLOBAL
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:186`

  >   `RunStartDateTime` 은 현 ADCIRC 시뮬레이션의 시작 시각

- `models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:50`

  >   - Amplitude `EMO(I,J)` and phase `EFA(I,J)` at `[file=src/read_input.F line=3450-3456]`, `[file=src/global.F line=387, 1045]`

대표 줄 대응(전체는 아래 참조 원장):

- CSV#1990 `models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:50`: baseline 387-387: parent 393..393 → child 395..395; Δ=+2; baseline 1045-1045: parent 1051..1051 → child 1053..1053; Δ=+2

### 976fc5b6cafb · src/nodalattr.F · NOTE_IMPACTING

- commit: `976fc5b6cafb0e8248cac1726f01ef3350b7b860`; 상태 `modified`; line_shift **yes**.
- 판단: swan_local_control(2값) 선언·기본값 [1,0]·XDMF/fort.13 CASE·누락 검사·할당·초기화 추가. 노트의 attribute CASE 카탈로그 636-686 안에 새 CASE가 들어가며 spatial controls phase 2 예정 서술도 재검토 후보.
- diff 원천: `commit-details/976fc5b6cafb.json` → `files[filename=src/nodalattr.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -82,6 +82,12 @@
@@ -144,6 +150,8 @@ MODULE NodalAttributes
@@ -164,7 +172,8 @@ MODULE NodalAttributes
@@ -187,6 +196,7 @@ MODULE NodalAttributes
@@ -208,6 +218,7 @@ MODULE NodalAttributes
@@ -228,6 +239,7 @@ MODULE NodalAttributes
@@ -294,6 +306,7 @@ MODULE NodalAttributes
@@ -421,6 +434,7 @@ SUBROUTINE InitNAModule()
@@ -440,6 +454,7 @@ SUBROUTINE InitNAModule()
@@ -460,6 +475,7 @@ SUBROUTINE InitNAModule()
@@ -481,6 +497,9 @@ SUBROUTINE InitNAModule()
@@ -645,6 +664,8 @@ SUBROUTINE readNodalAttrXDMF()
@@ -788,6 +809,10 @@ SUBROUTINE readNodalAttrXDMF()
@@ -892,6 +917,8 @@ subroutine checkForMissingNodalAttributes()
@@ -942,6 +969,7 @@ subroutine allocateNodalAttributes()
@@ -1062,6 +1090,8 @@ SUBROUTINE ReadNodalAttr(NScreen, ScreenUnit, MyProc, NAbOut)
@@ -1201,6 +1231,12 @@ SUBROUTINE ReadNodalAttr(NScreen, ScreenUnit, MyProc, NAbOut)
@@ -1363,6 +1399,15 @@ SUBROUTINE ReadNodalAttr(NScreen, ScreenUnit, MyProc, NAbOut)
@@ -1992,6 +2037,17 @@ SUBROUTINE InitNodalAttr(DP, NP, G, NScreen, ScreenUnit,
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:21`

  > ## 1. Attribute 카탈로그 (nodalattr.F:636-686)

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:178`

  > PR [#498](https://github.com/adcirc/adcirc/pull/498) (OPEN, branch `Spatial-and-Temporal-Controls`, +274 -30, 17 files). 사용자가 ADCIRC+SWAN coupled simulation 의 SWAN computation 시간을 storm landfall 즈음으로 제한 가능 → 전체 mesh + 전체 timeframe SWAN 호출 회피로 wall-clock 절감. Spatial controls 은 phase 2 예정. 외부 docs: [CCHT-NCSU/Spatial-Temporal-Controls](https://github.com/ccht-ncsu/Spatial-Temporal-Controls).

대표 줄 대응(전체는 아래 참조 원장):

- CSV#361 `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51`: baseline 1141-1141: parent 1144..1144 → child 1174..1174; Δ=+30; baseline 1154-1154: parent 1157..1157 → child 1187..1187; Δ=+30
- CSV#362 `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51`: baseline 1141-1141: parent 1144..1144 → child 1174..1174; Δ=+30; baseline 1154-1154: parent 1157..1157 → child 1187..1187; Δ=+30
- CSV#489 `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:160`: baseline 1051-1051: parent 1054..1054 → child 1082..1082; Δ=+28

### 976fc5b6cafb · src/read_input.F · NOTE_IMPACTING

- commit: `976fc5b6cafb0e8248cac1726f01ef3350b7b860`; 상태 `modified`; line_shift **yes**.
- 판단: SWANTimeControl/RunStartDateTime import·namelist·읽기·로그 추가. 474행 이후 원래 인용은 +14행(더 앞은 +2/+4); NWS/GAHM/조석 파일 인용의 주소 이동이며 그 계산 로직 변경을 의미하지 않음.
- diff 원천: `commit-details/976fc5b6cafb.json` → `files[filename=src/read_input.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -91,6 +91,8 @@ SUBROUTINE READ_INPUT()
@@ -234,6 +236,8 @@ SUBROUTINE READ_INPUT()
@@ -468,6 +472,16 @@ SUBROUTINE READ_INPUT()
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:182`

  > - **fort.15 (ADCIRC)** 끝에 namelist 추가:

- `models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:34`

  > | +1 | -- | `wind.F:2149-2164` | `read_input.F:1825-1832` |

- `models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:49`

  > - 개요의 `AMIG` 설명에는 amplitude가 나오지만, 상세 정의와 코드에서 **AMIG는 주파수**, 경계 진폭은 **EMO**다. `PER=2π/AMIG`와 시간 인수에 곱하는 위치를 함께 확인한다. `docs/user_guide/model_configuration/tides/index.rst:29–32`; `docs/technical_reference/parameter_definitions/index.rst:789–801`; `src/read_input.F:3431–3441`; `src/gwce.F:1638–1649`.

대표 줄 대응(전체는 아래 참조 원장):

- CSV#123 `models/ADCIRC/source-analysis/adcirc-3d-mode.md:20`: baseline 1176-1191: parent 1176..1191 → child 1190..1205; Δ=+14; baseline 3072-3072: parent 3072..3072 → child 3086..3086; Δ=+14; baseline 5139-5482: parent 5139..5482 → child 5153..5496; Δ=+14; baseline 5682-5682: parent 5706..5706 → child 5720..5720; Δ=+14
- CSV#135 `models/ADCIRC/source-analysis/adcirc-3d-mode.md:37`: baseline 1176-1191: parent 1176..1191 → child 1190..1205; Δ=+14
- CSV#136 `models/ADCIRC/source-analysis/adcirc-3d-mode.md:44`: baseline 5139-5139: parent 5139..5139 → child 5153..5153; Δ=+14

### 976fc5b6cafb · thirdparty/swan/SwanBpntlist.ftn90 · POSSIBLY_IMPACTING

- commit: `976fc5b6cafb0e8248cac1726f01ef3350b7b860`; 상태 `modified`; line_shift **unknown**.
- 판단: PSNAME 8→16; !ADC/!NADC 표식의 faceloop 종료 조건을 num_int_src 반영 형태로 바꾸고 return→exit; internal source 목록 처리 추가. 직접 파일 인용 없음. SWAN 결합·입출력 주제와 관련하나 기존 인용 지점 일치 불확실.
- diff 원천: `commit-details/976fc5b6cafb.json` → `files[filename=thirdparty/swan/SwanBpntlist.ftn90].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -63,10 +63,16 @@ subroutine SwanBpntlist
@@ -109,7 +115,7 @@ subroutine SwanBpntlist
@@ -323,8 +329,9 @@ subroutine SwanBpntlist
@@ -347,12 +354,23 @@ subroutine SwanBpntlist
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:178`

  > PR [#498](https://github.com/adcirc/adcirc/pull/498) (OPEN, branch `Spatial-and-Temporal-Controls`, +274 -30, 17 files). 사용자가 ADCIRC+SWAN coupled simulation 의 SWAN computation 시간을 storm landfall 즈음으로 제한 가능 → 전체 mesh + 전체 timeframe SWAN 호출 회피로 wall-clock 절감. Spatial controls 은 phase 2 예정. 외부 docs: [CCHT-NCSU/Spatial-Temporal-Controls](https://github.com/ccht-ncsu/Spatial-Temporal-Controls).

숫자 인용의 직접 이동/교집합은 위 근거만으로 확인되지 않음. 심볼·주제 일치와 불확실성을 구분해 판정했다.

### 976fc5b6cafb · thirdparty/swan/SwanCompUnstruc.ftn90 · POSSIBLY_IMPACTING

- commit: `976fc5b6cafb0e8248cac1726f01ef3350b7b860`; 상태 `modified`; line_shift **unknown**.
- 판단: !ADC/!NADC 표식 분기에서 SwanLocalControl(:,1)=1 및 수심으로 active 지정, (:,2)=0인 active vertex만 update하도록 조건 추가. 직접 파일 인용 없음. SWAN 결합·입출력 주제와 관련하나 기존 인용 지점 일치 불확실.
- diff 원천: `commit-details/976fc5b6cafb.json` → `files[filename=thirdparty/swan/SwanCompUnstruc.ftn90].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -99,7 +99,8 @@ subroutine SwanCompUnstruc ( ac2, ac1, compda, spcsig, spcdir, xytst, cross, it
@@ -639,11 +640,19 @@ subroutine SwanCompUnstruc ( ac2, ac1, compda, spcsig, spcdir, xytst, cross, it
@@ -846,8 +855,9 @@ subroutine SwanCompUnstruc ( ac2, ac1, compda, spcsig, spcdir, xytst, cross, it
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:178`

  > PR [#498](https://github.com/adcirc/adcirc/pull/498) (OPEN, branch `Spatial-and-Temporal-Controls`, +274 -30, 17 files). 사용자가 ADCIRC+SWAN coupled simulation 의 SWAN computation 시간을 storm landfall 즈음으로 제한 가능 → 전체 mesh + 전체 timeframe SWAN 호출 회피로 wall-clock 절감. Spatial controls 은 phase 2 예정. 외부 docs: [CCHT-NCSU/Spatial-Temporal-Controls](https://github.com/ccht-ncsu/Spatial-Temporal-Controls).

숫자 인용의 직접 이동/교집합은 위 근거만으로 확인되지 않음. 심볼·주제 일치와 불확실성을 구분해 판정했다.

### 976fc5b6cafb · thirdparty/swan/SwanGriddata.ftn90 · POSSIBLY_IMPACTING

- commit: `976fc5b6cafb0e8248cac1726f01ef3350b7b860`; 상태 `modified`; line_shift **unknown**.
- 판단: int_src_nd(:) allocatable 배열과 num_int_src 정수 선언 추가. 직접 파일 인용 없음. SWAN 결합·입출력 주제와 관련하나 기존 인용 지점 일치 불확실.
- diff 원천: `commit-details/976fc5b6cafb.json` → `files[filename=thirdparty/swan/SwanGriddata.ftn90].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -69,6 +69,9 @@ module SwanGriddata
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:178`

  > PR [#498](https://github.com/adcirc/adcirc/pull/498) (OPEN, branch `Spatial-and-Temporal-Controls`, +274 -30, 17 files). 사용자가 ADCIRC+SWAN coupled simulation 의 SWAN computation 시간을 storm landfall 즈음으로 제한 가능 → 전체 mesh + 전체 timeframe SWAN 호출 회피로 wall-clock 절감. Spatial controls 은 phase 2 예정. 외부 docs: [CCHT-NCSU/Spatial-Temporal-Controls](https://github.com/ccht-ncsu/Spatial-Temporal-Controls).

숫자 인용의 직접 이동/교집합은 위 근거만으로 확인되지 않음. 심볼·주제 일치와 불확실성을 구분해 판정했다.

### 976fc5b6cafb · thirdparty/swan/SwanReadADCGrid.ftn90 · POSSIBLY_IMPACTING

- commit: `976fc5b6cafb0e8248cac1726f01ef3350b7b860`; 상태 `modified`; line_shift **unknown**.
- 판단: !ADC 표식 블록에 SwanLocalControl(:,2)>0인 내부 source 수/노드 목록 계산 및 vmark 설정 추가. 직접 파일 인용 없음. SWAN 결합·입출력 주제와 관련하나 기존 인용 지점 일치 불확실.
- diff 원천: `commit-details/976fc5b6cafb.json` → `files[filename=thirdparty/swan/SwanReadADCGrid.ftn90].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -56,6 +56,8 @@ subroutine SwanReadADCGrid
@@ -78,6 +80,9 @@ subroutine SwanReadADCGrid
@@ -181,6 +186,32 @@ subroutine SwanReadADCGrid
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:178`

  > PR [#498](https://github.com/adcirc/adcirc/pull/498) (OPEN, branch `Spatial-and-Temporal-Controls`, +274 -30, 17 files). 사용자가 ADCIRC+SWAN coupled simulation 의 SWAN computation 시간을 storm landfall 즈음으로 제한 가능 → 전체 mesh + 전체 timeframe SWAN 호출 회피로 wall-clock 절감. Spatial controls 은 phase 2 예정. 외부 docs: [CCHT-NCSU/Spatial-Temporal-Controls](https://github.com/ccht-ncsu/Spatial-Temporal-Controls).

숫자 인용의 직접 이동/교집합은 위 근거만으로 확인되지 않음. 심볼·주제 일치와 불확실성을 구분해 판정했다.

### 976fc5b6cafb · thirdparty/swan/SwanVTKPDataSets.ftn90 · POSSIBLY_IMPACTING

- commit: `976fc5b6cafb0e8248cac1726f01ef3350b7b860`; 상태 `modified`; line_shift **unknown**.
- 판단: 출력 frame 이름 psname 길이 8→16. 직접 파일 인용 없음. SWAN 결합·입출력 주제와 관련하나 기존 인용 지점 일치 불확실.
- diff 원천: `commit-details/976fc5b6cafb.json` → `files[filename=thirdparty/swan/SwanVTKPDataSets.ftn90].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -66,7 +66,7 @@ subroutine SwanVTKPDataSets ( upvt, pstype, nvar, ivtyp, mxk, myk, vtkfile, upvd
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:178`

  > PR [#498](https://github.com/adcirc/adcirc/pull/498) (OPEN, branch `Spatial-and-Temporal-Controls`, +274 -30, 17 files). 사용자가 ADCIRC+SWAN coupled simulation 의 SWAN computation 시간을 storm landfall 즈음으로 제한 가능 → 전체 mesh + 전체 timeframe SWAN 호출 회피로 wall-clock 절감. Spatial controls 은 phase 2 예정. 외부 docs: [CCHT-NCSU/Spatial-Temporal-Controls](https://github.com/ccht-ncsu/Spatial-Temporal-Controls).

숫자 인용의 직접 이동/교집합은 위 근거만으로 확인되지 않음. 심볼·주제 일치와 불확실성을 구분해 판정했다.

### 976fc5b6cafb · thirdparty/swan/swanout2.ftn · POSSIBLY_IMPACTING

- commit: `976fc5b6cafb0e8248cac1726f01ef3350b7b860`; 상태 `modified`; line_shift **unknown**.
- 판단: PSNAME 선언 길이 8→16(주석만이 아닌 CHARACTER 선언 변경). 직접 파일 인용 없음. SWAN 결합·입출력 주제와 관련하나 기존 인용 지점 일치 불확실.
- diff 원천: `commit-details/976fc5b6cafb.json` → `files[filename=thirdparty/swan/swanout2.ftn].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -97,7 +97,7 @@
@@ -483,7 +483,7 @@
@@ -798,7 +798,7 @@
@@ -1292,7 +1292,7 @@
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:15`

  > How the `padcswan` binary couples ADCIRC and SWAN over a shared unstructured mesh, the actual NWS encoding (`3xx` for `NRS=3`, **not literal `NWS=83/84`**), how time-stepping is coordinated by integer ratio `SWAN_DT/DT`, what fields are exchanged each direction, how the build system selects SWAN sources for the coupled binary, and the hot-start protocol for the combined run. Use this when wiring a coupled tide+wave simulation, debugging coupling interval mismatches, or interpreting `NRS=3` log entries.

숫자 인용의 직접 이동/교집합은 위 근거만으로 확인되지 않음. 심볼·주제 일치와 불확실성을 구분해 판정했다.

### 976fc5b6cafb · thirdparty/swan/swanparll.ftn · POSSIBLY_IMPACTING

- commit: `976fc5b6cafb0e8248cac1726f01ef3350b7b860`; 상태 `modified`; line_shift **unknown**.
- 판단: PSNAME 선언 길이 8→16. 직접 파일 인용 없음. SWAN 결합·입출력 주제와 관련하나 기존 인용 지점 일치 불확실.
- diff 원천: `commit-details/976fc5b6cafb.json` → `files[filename=thirdparty/swan/swanparll.ftn].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -5129,7 +5129,7 @@
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:15`

  > How the `padcswan` binary couples ADCIRC and SWAN over a shared unstructured mesh, the actual NWS encoding (`3xx` for `NRS=3`, **not literal `NWS=83/84`**), how time-stepping is coordinated by integer ratio `SWAN_DT/DT`, what fields are exchanged each direction, how the build system selects SWAN sources for the coupled binary, and the hot-start protocol for the combined run. Use this when wiring a coupled tide+wave simulation, debugging coupling interval mismatches, or interpreting `NRS=3` log entries.

숫자 인용의 직접 이동/교집합은 위 근거만으로 확인되지 않음. 심볼·주제 일치와 불확실성을 구분해 판정했다.

### 976fc5b6cafb · thirdparty/swan/swanpre1.ftn · POSSIBLY_IMPACTING

- commit: `976fc5b6cafb0e8248cac1726f01ef3350b7b860`; 상태 `modified`; line_shift **unknown**.
- 판단: PSNAME/PNAME 선언 길이 8→16. 직접 파일 인용 없음. SWAN 결합·입출력 주제와 관련하나 기존 인용 지점 일치 불확실.
- diff 원천: `commit-details/976fc5b6cafb.json` → `files[filename=thirdparty/swan/swanpre1.ftn].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -445,7 +445,7 @@
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:15`

  > How the `padcswan` binary couples ADCIRC and SWAN over a shared unstructured mesh, the actual NWS encoding (`3xx` for `NRS=3`, **not literal `NWS=83/84`**), how time-stepping is coordinated by integer ratio `SWAN_DT/DT`, what fields are exchanged each direction, how the build system selects SWAN sources for the coupled binary, and the hot-start protocol for the combined run. Use this when wiring a coupled tide+wave simulation, debugging coupling interval mismatches, or interpreting `NRS=3` log entries.

숫자 인용의 직접 이동/교집합은 위 근거만으로 확인되지 않음. 심볼·주제 일치와 불확실성을 구분해 판정했다.

### 976fc5b6cafb · thirdparty/swan/swanpre2.ftn · POSSIBLY_IMPACTING

- commit: `976fc5b6cafb0e8248cac1726f01ef3350b7b860`; 상태 `modified`; line_shift **unknown**.
- 판단: 7개 SNAME 입력 길이 제한 검사 LENCST>8→>16; RNAME 제한은 이 diff에서 유지. 직접 파일 인용 없음. SWAN 결합·입출력 주제와 관련하나 기존 인용 지점 일치 불확실.
- diff 원천: `commit-details/976fc5b6cafb.json` → `files[filename=thirdparty/swan/swanpre2.ftn].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -330,7 +330,7 @@
@@ -384,7 +384,7 @@
@@ -462,7 +462,7 @@
@@ -536,7 +536,7 @@
@@ -700,7 +700,7 @@
@@ -801,7 +801,7 @@
@@ -2323,7 +2323,7 @@
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:15`

  > How the `padcswan` binary couples ADCIRC and SWAN over a shared unstructured mesh, the actual NWS encoding (`3xx` for `NRS=3`, **not literal `NWS=83/84`**), how time-stepping is coordinated by integer ratio `SWAN_DT/DT`, what fields are exchanged each direction, how the build system selects SWAN sources for the coupled binary, and the hot-start protocol for the combined run. Use this when wiring a coupled tide+wave simulation, debugging coupling interval mismatches, or interpreting `NRS=3` log entries.

숫자 인용의 직접 이동/교집합은 위 근거만으로 확인되지 않음. 심볼·주제 일치와 불확실성을 구분해 판정했다.

### 976fc5b6cafb · thirdparty/swan/swmod1.ftn · POSSIBLY_IMPACTING

- commit: `976fc5b6cafb0e8248cac1726f01ef3350b7b860`; 상태 `modified`; line_shift **unknown**.
- 판단: SNAME CHARACTER 길이 8→16. 직접 파일 인용 없음. SWAN 결합·입출력 주제와 관련하나 기존 인용 지점 일치 불확실.
- diff 원천: `commit-details/976fc5b6cafb.json` → `files[filename=thirdparty/swan/swmod1.ftn].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -948,7 +948,7 @@
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:15`

  > How the `padcswan` binary couples ADCIRC and SWAN over a shared unstructured mesh, the actual NWS encoding (`3xx` for `NRS=3`, **not literal `NWS=83/84`**), how time-stepping is coordinated by integer ratio `SWAN_DT/DT`, what fields are exchanged each direction, how the build system selects SWAN sources for the coupled binary, and the hot-start protocol for the combined run. Use this when wiring a coupled tide+wave simulation, debugging coupling interval mismatches, or interpreting `NRS=3` log entries.

숫자 인용의 직접 이동/교집합은 위 근거만으로 확인되지 않음. 심볼·주제 일치와 불확실성을 구분해 판정했다.

### 976fc5b6cafb · thirdparty/swan/swmod2.ftn · POSSIBLY_IMPACTING

- commit: `976fc5b6cafb0e8248cac1726f01ef3350b7b860`; 상태 `modified`; line_shift **unknown**.
- 판단: MAX_OUTP_REQ 250→5000; OPSDAT/ORQDAT의 PSNAME 길이 8→16. 직접 파일 인용 없음. SWAN 결합·입출력 주제와 관련하나 기존 인용 지점 일치 불확실.
- diff 원천: `commit-details/976fc5b6cafb.json` → `files[filename=thirdparty/swan/swmod2.ftn].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -202,7 +202,7 @@
@@ -254,7 +254,7 @@
@@ -268,7 +268,7 @@
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:15`

  > How the `padcswan` binary couples ADCIRC and SWAN over a shared unstructured mesh, the actual NWS encoding (`3xx` for `NRS=3`, **not literal `NWS=83/84`**), how time-stepping is coordinated by integer ratio `SWAN_DT/DT`, what fields are exchanged each direction, how the build system selects SWAN sources for the coupled binary, and the hot-start protocol for the combined run. Use this when wiring a coupled tide+wave simulation, debugging coupling interval mismatches, or interpreting `NRS=3` log entries.

숫자 인용의 직접 이동/교집합은 위 근거만으로 확인되지 않음. 심볼·주제 일치와 불확실성을 구분해 판정했다.

### 5203dafc6871 · src/nodalattr.F · NOTE_IMPACTING

- commit: `5203dafc6871a1104700ae8358e9114da9ea2dc7`; 상태 `modified`; line_shift **yes**.
- 판단: InitNAModule에서 기본값 대입 전 CondensedNodesDefVal 해제/할당 추가; allocateNodalAttributes에서도 다시 해제/할당하도록 변경. catalog/read 인용 좌표 이동. 후자의 재할당은 e8b62a70에서 제거되므로 tip 동작과 중간 커밋을 구분.
- diff 원천: `commit-details/5203dafc6871.json` → `files[filename=src/nodalattr.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -429,7 +429,9 @@ SUBROUTINE InitNAModule()
@@ -986,9 +988,8 @@ subroutine allocateNodalAttributes()
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:21`

  > ## 1. Attribute 카탈로그 (nodalattr.F:636-686)

- `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51`

  > | **13** | Nodal attributes (Manning's n, primitive weighting, bridge piers, surface canopy, etc.) | `NWP > 0` | `ReadNodalAttr` | `[file=src/nodalattr.F line=1141]`, `[file=src/nodalattr.F line=1154]` | `[file=wiki:adcirc:Fort.13_file]`; e.g. `mannings_n_at_sea_floor` `[file=wiki:adcirc:Manning_s_n_at_sea_floor]` requires `NOLIBF=1` |

대표 줄 대응(전체는 아래 참조 원장):

- CSV#361 `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51`: baseline 1141-1141: parent 1174..1174 → child 1175..1175; Δ=+1; baseline 1154-1154: parent 1187..1187 → child 1188..1188; Δ=+1
- CSV#362 `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51`: baseline 1141-1141: parent 1174..1174 → child 1175..1175; Δ=+1; baseline 1154-1154: parent 1187..1187 → child 1188..1188; Δ=+1
- CSV#489 `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:160`: baseline 1051-1051: parent 1082..1082 → child 1083..1083; Δ=+1

### e8b62a70db39 · src/nodalattr.F · NOTE_IMPACTING

- commit: `e8b62a70db39dbc8875785ee999a2214be75302b`; 상태 `modified`; line_shift **yes**.
- 판단: allocateNodalAttributes의 CondensedNodesDefVal 재해제/재할당 두 줄 제거; PrepCondensedNodes에 node/CondensedNodesDefVal 로그 두 줄 추가. fort.13 reader 인용은 이 커밋에서 -2행; 파일 총 행 수 0 변화와 구간 좌표 변화를 구분.
- diff 원천: `commit-details/e8b62a70db39.json` → `files[filename=src/nodalattr.F].patch`; 아래는 해당 변경 hunk 헤더다.
```diff
@@ -988,8 +988,6 @@ subroutine allocateNodalAttributes()
@@ -3216,6 +3214,8 @@ SUBROUTINE PrepCondensedNodes()
```

노트 원문 발췌(판단 근거/주제 anchor):

- `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51`

  > | **13** | Nodal attributes (Manning's n, primitive weighting, bridge piers, surface canopy, etc.) | `NWP > 0` | `ReadNodalAttr` | `[file=src/nodalattr.F line=1141]`, `[file=src/nodalattr.F line=1154]` | `[file=wiki:adcirc:Fort.13_file]`; e.g. `mannings_n_at_sea_floor` `[file=wiki:adcirc:Manning_s_n_at_sea_floor]` requires `NOLIBF=1` |

- `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:42`

  > | `condensed_nodes` | 노드 병합 | mesh |

대표 줄 대응(전체는 아래 참조 원장):

- CSV#361 `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51`: baseline 1141-1141: parent 1175..1175 → child 1173..1173; Δ=-2; baseline 1154-1154: parent 1188..1188 → child 1186..1186; Δ=-2
- CSV#362 `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51`: baseline 1141-1141: parent 1175..1175 → child 1173..1173; Δ=-2; baseline 1154-1154: parent 1188..1188 → child 1186..1186; Δ=-2
- CSV#489 `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:160`: baseline 1051-1051: parent 1083..1083 → child 1081..1081; Δ=-2

## NON_IMPACTING — 범위 제외 변경 한 줄씩

| SHA · 파일 | 판정·근거 | 관련 참조 | line_shift |
|---|---|---|---|
| aef3777ed09d · CITATION.cff | NON_IMPACTING: CITATION 메타데이터 추가 또는 affiliation/연락처 주석 갱신; 사용자 메타데이터 제외 규칙 적용. | 직접 파일 참조 없음 | unknown |
| bf6957a976d9 · src/nodalattr.F | NON_IMPACTING: legacy 빌드 의존성 제거: Apply3DBottomFriction의 KP를 USE GLOBAL_3DVS 대신 인수로 전달(정의부 +3행). 사용자 빌드 변경 제외 규칙 적용; 인터페이스/줄 이동은 별도 기록. | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:160; models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:175; models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51; models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:68; models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:19; models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:21; models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:6; models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:73; models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:39; models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:56 | no |
| bf6957a976d9 · src/timestep.F | NON_IMPACTING: legacy 빌드 의존성 제거: Apply3DBottomFriction의 KP를 USE GLOBAL_3DVS 대신 인수로 전달(호출부 +4행). 사용자 빌드 변경 제외 규칙 적용; 인터페이스/줄 이동은 별도 기록. | models/ADCIRC/source-analysis/adcirc-3d-mode.md:112; models/ADCIRC/source-analysis/adcirc-3d-mode.md:24; models/ADCIRC/source-analysis/adcirc-3d-mode.md:84; models/ADCIRC/source-analysis/adcirc-3d-mode.md:88; models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:23; models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:7; models/ADCIRC/source-analysis/adcirc-dg-continuity-solver.md:268; models/ADCIRC/source-analysis/adcirc-dg-continuity-solver.md:60; models/ADCIRC/source-analysis/adcirc-hotstart.md:116; models/ADCIRC/source-analysis/adcirc-hotstart.md:25; models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:6; models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:66; models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:69; models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:40; models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:7; models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:157; models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:63; models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:83; models/ADCIRC/source-analysis/adcirc-swan-coupling.md:139; models/ADCIRC/source-analysis/adcirc-swan-coupling.md:24; models/ADCIRC/source-analysis/adcirc-swan-coupling.md:62; models/ADCIRC/source-analysis/adcirc-swan-coupling.md:63; models/ADCIRC/source-analysis/adcirc-swan-coupling.md:77; models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:20; models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:22; models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:36; models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:45; models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:49; models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:51; models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:7; models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:19; models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:2; models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:21; models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:23; models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:7; models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:106; models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:110; models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:123; models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:137; models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:144; models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:163; models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:176; models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:43; models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:128; models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:167; models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:222; models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:310; models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:333; models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:335; models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:337; models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:339 | yes |
| 8a80ef218a6c · src/cstart.F | NON_IMPACTING: 비활성 옛 코드·설명 주석 삭제만; 사용자 주석 변경 제외 규칙 적용. 줄 번호 이동은 별도 기록. | models/ADCIRC/source-analysis/adcirc-3d-mode.md:23; models/ADCIRC/source-analysis/adcirc-3d-mode.md:36; models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:145; models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:180; models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:53; models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:63; models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:64; models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:65; models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:66; models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:67; models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:68; models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:69; models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:70; models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:71; models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:105; models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:57; models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:60; models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:74; models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:178 | yes |
| 8a80ef218a6c · src/hstart.F | NON_IMPACTING: 비활성 옛 코드·설명 주석 삭제만; 사용자 주석 변경 제외 규칙 적용. 줄 번호 이동은 별도 기록. | models/ADCIRC/source-analysis/adcirc-3d-mode.md:194; models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:145; models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:180; models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:105; models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:37; models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:57; models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:65; models/ADCIRC/source-analysis/adcirc-hotstart.md:122; models/ADCIRC/source-analysis/adcirc-hotstart.md:123; models/ADCIRC/source-analysis/adcirc-hotstart.md:130; models/ADCIRC/source-analysis/adcirc-hotstart.md:144; models/ADCIRC/source-analysis/adcirc-hotstart.md:21; models/ADCIRC/source-analysis/adcirc-hotstart.md:35; models/ADCIRC/source-analysis/adcirc-hotstart.md:36; models/ADCIRC/source-analysis/adcirc-hotstart.md:38; models/ADCIRC/source-analysis/adcirc-hotstart.md:45; models/ADCIRC/source-analysis/adcirc-hotstart.md:70; models/ADCIRC/source-analysis/adcirc-hotstart.md:72; models/ADCIRC/source-analysis/adcirc-hotstart.md:76; models/ADCIRC/source-analysis/adcirc-hotstart.md:83; models/ADCIRC/source-analysis/adcirc-swan-coupling.md:129; models/ADCIRC/source-analysis/adcirc-swan-coupling.md:25; models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:106; models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:137; models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:178; models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:223; models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:310 | yes |
| 8a80ef218a6c · src/netcdfio.F90 | NON_IMPACTING: 비활성 옛 코드·설명 주석 삭제만; 사용자 주석 변경 제외 규칙 적용. 줄 번호 이동은 별도 기록. | models/ADCIRC/source-analysis/adcirc-hotstart.md:123; models/ADCIRC/source-analysis/adcirc-hotstart.md:138; models/ADCIRC/source-analysis/adcirc-hotstart.md:188; models/ADCIRC/source-analysis/adcirc-hotstart.md:24; models/ADCIRC/source-analysis/adcirc-hotstart.md:90; models/ADCIRC/source-analysis/adcirc-swan-coupling.md:135; models/ADCIRC/source-analysis/adcirc-swan-coupling.md:142; models/ADCIRC/source-analysis/adcirc-swan-coupling.md:174; models/ADCIRC/source-analysis/adcirc-swan-coupling.md:25 | yes |
| 40201037d1a6 · CITATION.cff | NON_IMPACTING: CITATION 메타데이터 추가 또는 affiliation/연락처 주석 갱신; 사용자 메타데이터 제외 규칙 적용. | 직접 파일 참조 없음 | unknown |
| 40201037d1a6 · README.md | NON_IMPACTING: CITATION 메타데이터 추가 또는 affiliation/연락처 주석 갱신; 사용자 메타데이터 제외 규칙 적용. | 직접 파일 참조 없음 | unknown |
| 40201037d1a6 · src/constants.F90 | NON_IMPACTING: CITATION 메타데이터 추가 또는 affiliation/연락처 주석 갱신; 사용자 메타데이터 제외 규칙 적용. | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:133; models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:29 | no |
| 40201037d1a6 · src/owiwind.F | NON_IMPACTING: CITATION 메타데이터 추가 또는 affiliation/연락처 주석 갱신; 사용자 메타데이터 제외 규칙 적용. | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:161; models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:177; models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:52; models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:124; models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:154; models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:65; models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:66; models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:70; models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:71; models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:72; models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:27; models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:85 | no |
| 40201037d1a6 · src/weir_boundary.F90 | NON_IMPACTING: CITATION 메타데이터 추가 또는 affiliation/연락처 주석 갱신; 사용자 메타데이터 제외 규칙 적용. | models/ADCIRC/source-analysis/adcirc-weir-boundary.md:17; models/ADCIRC/source-analysis/adcirc-weir-boundary.md:19; models/ADCIRC/source-analysis/adcirc-weir-boundary.md:2; models/ADCIRC/source-analysis/adcirc-weir-boundary.md:6 | unknown |
| 40201037d1a6 · util/adcircResultsComparison.F90 | NON_IMPACTING: CITATION 메타데이터 추가 또는 affiliation/연락처 주석 갱신; 사용자 메타데이터 제외 규칙 적용. | 직접 파일 참조 없음 | unknown |

## 판독상 주의·미해결 항목

- mesh.F 이웃 정렬/CSR 검사는 weir 주제와 관련하지만 현재 직접 인용한 1822-1834와 떨어져 있다. POSSIBLE 1개로 유지한다. SWAN 내부 11파일도 직접 참조가 없어 POSSIBLE로 유지한다. 소스 전체나 부속 도구 조사는 하지 않았다.
- SWAN 노트 178행은 PR OPEN / spatial phase 2 예정, 202행은 나머지 14 files를 테스트/build/docs로 요약한다. 이번 976fc5b6cafb의 저장 diff에는 실제 swan_local_control과 SWAN 계산/입출력 변경이 있다. 과거 PR의 전체 내용이나 현재 웹 상태는 확인하지 않았으며, 위 문구를 현재 tip 설명으로 재사용할 수 있는지 재검토가 필요하다.
- SWAN 노트 193행의 sentinel이면 전체 시간 SWAN이라는 단정은 diff의 RUN 조건 1≤SwanTimeStep≤SWAN_MTC로 보장되지 않는다. 222-223행의 sentinel 개수/응력 전체 0 요약도 diff의 5개 -99999 출력, 3개 0 출력 및 이전 column 보존과 구분해야 한다. timestep 증가를 매 ADCIRC step이라고 한 요약은 이번 hunk 밖 호출 조건까지 검증하지 않았다.
- 3D nodalattr의 TK(I) 문맥과 새 TK(NH) 제한은 diff에서 그대로 관찰된다. 의도·전체 인덱스 정합·성능/안정성 효과는 추정하지 않았다. CondensedNodesDefVal 수정은 daae→5203→e8b6 순서로 읽어야 하며 중간 재할당이 tip에서 제거된다.
- PREP20 maxOpenFiles 주석과 inclusive endProc 계산의 256/257 차이는 diff 관찰 사실이다. 실제 열린 descriptor 수나 런타임 성공 여부는 검증하지 않았다.
- NetCDF e65의 +51행은 8a80 주석 제거 -51행으로 tip에서 상쇄된다. cstart는 +5/-2=+3, hstart는 +42/-14=+28. NON 주석 변경에도 중간 좌표는 이동한다. 아래 baseline→tip 원장을 최종 주소 영향에 사용한다.
- 이 보고서는 해당 변경 집합과 주어진 CSV의 영향 분류만 완료한다. 모델 빌드/실행, 전체 노트 정확성, upstream 기능 완결성, 물리 타당성은 미검증이다. 기존 baseline을 명시한 역사적 인용은 보존 가능하며 tip 인용으로 바꿀 때에만 주소/서술 재대조가 필요하다.

## 변경 파일 관련 CSV 참조 전수 원장

N=NOTE_IMPACTING, P=POSSIBLY_IMPACTING, X=NON_IMPACTING. 아래는 **참조별 판정**으로, 45개 파일 단위 집계와 합산하지 않는다. 파일만 인용한 경우의 P는 위치 불확실성이다. 문맥 원문과 전체 affected_notes는 CSV/상세를 함께 참조한다.

### 참조 원장 69f5fbba209e · src/gwce.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 129 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:25 | gwce.F:780-1450 | N | baseline 780-1450: parent 780..1450 → child 780..1450; Δ=+0; changed/replaced; 인용 변경/좌표 이동 |
| 157 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:102 | gwce.F:780 | X | baseline 780-780: parent 780..780 → child 780..780; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 158 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:105 | gwce.F:1196,1283,1405,1450 | X | baseline 1196-1196: parent 1196..1196 → child 1196..1196; Δ=+0; baseline 1283-1283: parent 1283..1283 → child 1283..1283; Δ=+0; baseline 1405-1405: parent 1405..1405 → child 1405..1405; Δ=+0; baseline 1450-1450: parent 1450..1450 → child 1450..1450; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 263 | models/ADCIRC/source-analysis/adcirc-boundary-conditions.md:20 | gwce.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 467 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:107 | src/gwce.F:148 | X | baseline 148-148: parent 148..148 → child 148..148; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 577 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:21 | src/gwce.F:237,427 | X | baseline 237-237: parent 237..237 → child 237..237; Δ=+0; baseline 427-427: parent 427..427 → child 427..427; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 578 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:21 | src/gwce.F:237,427 | X | baseline 237-237: parent 237..237 → child 237..237; Δ=+0; baseline 427-427: parent 427..427 → child 427..427; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 581 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:22 | src/gwce.F:418-420 | X | baseline 418-420: parent 418..420 → child 418..420; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 582 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:25 | src/gwce.F:538-540 | X | baseline 538-540: parent 538..540 → child 538..540; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 585 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:26 | src/gwce.F:564-592 | X | baseline 564-592: parent 564..592 → child 564..592; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 587 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:27 | src/gwce.F:517,538-539,607,623 | X | baseline 517-517: parent 517..517 → child 517..517; Δ=+0; baseline 538-539: parent 538..539 → child 538..539; Δ=+0; baseline 607-607: parent 607..607 → child 607..607; Δ=+0; baseline 623-623: parent 623..623 → child 623..623; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 589 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:28 | src/gwce.F:429-636 | X | baseline 429-636: parent 429..636 → child 429..636; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 592 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:29 | src/gwce.F:998-1617 | N | baseline 998-1617: parent 998..1617 → child 998..1617; Δ=+0; changed/replaced; 인용 변경/좌표 이동 |
| 593 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:30 | src/gwce.F:638-673,1846-1854 | X | baseline 638-673: parent 638..673 → child 638..673; Δ=+0; baseline 1846-1854: parent 1846..1854 → child 1846..1854; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 594 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:30 | src/gwce.F:638-673,1846-1854 | X | baseline 638-673: parent 638..673 → child 638..673; Δ=+0; baseline 1846-1854: parent 1846..1854 → child 1846..1854; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 596 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:31 | src/gwce.F:141,430,455,595,709,1846,1856 | X | baseline 141-141: parent 141..141 → child 141..141; Δ=+0; baseline 430-430: parent 430..430 → child 430..430; Δ=+0; baseline 455-455: parent 455..455 → child 455..455; Δ=+0; baseline 595-595: parent 595..595 → child 595..595; Δ=+0; baseline 709-709: parent 709..709 → child 709..709; Δ=+0; baseline 1846-1846: parent 1846..1846 → child 1846..1846; Δ=+0; baseline 1856-1856: parent 1856..1856 → child 1856..1856; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 598 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:32 | src/gwce.F:141-154 | X | baseline 141-154: parent 141..154 → child 141..154; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 601 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:36 | src/gwce.F:538-539,623,1429,1741,1758 | X | baseline 538-539: parent 538..539 → child 538..539; Δ=+0; baseline 623-623: parent 623..623 → child 623..623; Δ=+0; baseline 1429-1429: parent 1429..1429 → child 1429..1429; Δ=+0; baseline 1741-1741: parent 1741..1741 → child 1741..1741; Δ=+0; baseline 1758-1758: parent 1758..1758 → child 1758..1758; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 605 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:38 | src/gwce.F:2514-2522 | X | baseline 2514-2522: parent 2514..2522 → child 2514..2522; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 607 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:39 | src/gwce.F:1540-1543,2851-2852 | X | baseline 1540-1543: parent 1540..1543 → child 1540..1543; Δ=+0; baseline 2851-2852: parent 2851..2852 → child 2851..2852; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 608 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:39 | src/gwce.F:1540-1543,2851-2852 | X | baseline 1540-1543: parent 1540..1543 → child 1540..1543; Δ=+0; baseline 2851-2852: parent 2851..2852 → child 2851..2852; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 610 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:40 | src/gwce.F:1622-1631 | X | baseline 1622-1631: parent 1622..1631 → child 1622..1631; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 611 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:41 | src/gwce.F:2007,2020 | X | baseline 2007-2007: parent 2007..2007 → child 2007..2007; Δ=+0; baseline 2020-2020: parent 2020..2020 → child 2020..2020; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 612 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:41 | src/gwce.F:2007,2020 | X | baseline 2007-2007: parent 2007..2007 → child 2007..2007; Δ=+0; baseline 2020-2020: parent 2020..2020 → child 2020..2020; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 613 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:43 | src/gwce.F:2477-2482 | X | baseline 2477-2482: parent 2477..2482 → child 2477..2482; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 616 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:47 | src/gwce.F:2001-2004 | X | baseline 2001-2004: parent 2001..2004 → child 2001..2004; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 618 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:48 | src/gwce.F:2010-2017 | X | baseline 2010-2017: parent 2010..2017 → child 2010..2017; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 619 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:49 | src/gwce.F:146,2002 | X | baseline 146-146: parent 146..146 → child 146..146; Δ=+0; baseline 2002-2002: parent 2002..2002 → child 2002..2002; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 620 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:49 | src/gwce.F:146,2002 | X | baseline 146-146: parent 146..146 → child 146..146; Δ=+0; baseline 2002-2002: parent 2002..2002 → child 2002..2002; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 622 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:50 | src/gwce.F:150 | X | baseline 150-150: parent 150..150 → child 150..150; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 623 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:51 | src/gwce.F:2005 | X | baseline 2005-2005: parent 2005..2005 → child 2005..2005; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 625 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:55 | src/gwce.F:1638-1650 | X | baseline 1638-1650: parent 1638..1650 → child 1638..1650; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 627 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:56 | src/gwce.F:1659-1673 | X | baseline 1659-1673: parent 1659..1673 → child 1659..1673; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 628 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:57 | src/gwce.F:270-271 | X | baseline 270-271: parent 270..271 → child 270..271; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 631 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:58 | src/gwce.F:1725-1834,1740-1764,1782-1805 | X | baseline 1725-1834: parent 1725..1834 → child 1725..1834; Δ=+0; baseline 1740-1764: parent 1740..1764 → child 1740..1764; Δ=+0; baseline 1782-1805: parent 1782..1805 → child 1782..1805; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 632 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:58 | src/gwce.F:1725-1834,1740-1764,1782-1805 | X | baseline 1725-1834: parent 1725..1834 → child 1725..1834; Δ=+0; baseline 1740-1764: parent 1740..1764 → child 1740..1764; Δ=+0; baseline 1782-1805: parent 1782..1805 → child 1782..1805; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 635 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:59 | src/gwce.F:652-673,1840-1861 | X | baseline 652-673: parent 652..673 → child 652..673; Δ=+0; baseline 1840-1861: parent 1840..1861 → child 1840..1861; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 636 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:59 | src/gwce.F:652-673,1840-1861 | X | baseline 652-673: parent 652..673 → child 652..673; Δ=+0; baseline 1840-1861: parent 1840..1861 → child 1840..1861; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 637 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:60 | src/gwce.F:474-477,1010-1015 | X | baseline 474-477: parent 474..477 → child 474..477; Δ=+0; baseline 1010-1015: parent 1010..1015 → child 1010..1015; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 643 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:66 | src/gwce.F:1181-1184,1450-1452,1462-1464 | X | baseline 1181-1184: parent 1181..1184 → child 1181..1184; Δ=+0; baseline 1450-1452: parent 1450..1452 → child 1450..1452; Δ=+0; baseline 1462-1464: parent 1462..1464 → child 1462..1464; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 644 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:66 | src/gwce.F:1181-1184,1450-1452,1462-1464 | X | baseline 1181-1184: parent 1181..1184 → child 1181..1184; Δ=+0; baseline 1450-1452: parent 1450..1452 → child 1450..1452; Δ=+0; baseline 1462-1464: parent 1462..1464 → child 1462..1464; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 646 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:71 | src/gwce.F:477,605,1015,1074 | X | baseline 477-477: parent 477..477 → child 477..477; Δ=+0; baseline 605-605: parent 605..605 → child 605..605; Δ=+0; baseline 1015-1015: parent 1015..1015 → child 1015..1015; Δ=+0; baseline 1074-1074: parent 1074..1074 → child 1074..1074; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 647 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:73 | src/gwce.F:465-473,541-547,1055-1063,1436-1439 | X | baseline 465-473: parent 465..473 → child 465..473; Δ=+0; baseline 541-547: parent 541..547 → child 541..547; Δ=+0; baseline 1055-1063: parent 1055..1063 → child 1055..1063; Δ=+0; baseline 1436-1439: parent 1436..1439 → child 1436..1439; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 648 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:73 | src/gwce.F:465-473,541-547,1055-1063,1436-1439 | X | baseline 465-473: parent 465..473 → child 465..473; Δ=+0; baseline 541-547: parent 541..547 → child 541..547; Δ=+0; baseline 1055-1063: parent 1055..1063 → child 1055..1063; Δ=+0; baseline 1436-1439: parent 1436..1439 → child 1436..1439; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 651 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:81 | gwce.F:538-592 | X | baseline 538-592: parent 538..592 → child 538..592; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 657 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:83 | gwce.F:1638-1650 | X | baseline 1638-1650: parent 1638..1650 → child 1638..1650; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 659 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:84 | gwce.F:477 | X | baseline 477-477: parent 477..477 → child 477..477; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 668 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:103 | src/gwce.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 746 | models/ADCIRC/source-analysis/adcirc-itpack-solver.md:6 | gwce.F:2003 | X | baseline 2003-2003: parent 2003..2003 → child 2003..2003; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 749 | models/ADCIRC/source-analysis/adcirc-itpack-solver.md:21 | gwce.F:2003 | X | baseline 2003-2003: parent 2003..2003 → child 2003..2003; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 751 | models/ADCIRC/source-analysis/adcirc-itpack-solver.md:30 | gwce.F:2010 | X | baseline 2010-2010: parent 2010..2010 → child 2010..2010; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 904 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:6 | gwce.F:2479 | X | baseline 2479-2479: parent 2479..2479 → child 2479..2479; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 922 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:61 | gwce.F:2479 | X | baseline 2479-2479: parent 2479..2479 → child 2479..2479; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 932 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:68 | gwce.F:2477-2482 | X | baseline 2477-2482: parent 2477..2482 → child 2477..2482; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 935 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:73 | gwce.F:442 | X | baseline 442-442: parent 442..442 → child 442..442; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 940 | models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:7 | gwce.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 944 | models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:18 | gwce.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 954 | models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:54 | gwce.F:1725-1810 | X | baseline 1725-1810: parent 1725..1810 → child 1725..1810; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 955 | models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:54 | gwce.F:1725-1810 | X | baseline 1725-1810: parent 1725..1810 → child 1725..1810; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 958 | models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:78 | gwce.F:1727-1733 | X | baseline 1727-1733: parent 1727..1733 → child 1727..1733; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1166 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:96 | src/gwce.F:1874-1879 | X | baseline 1874-1879: parent 1874..1879 → child 1874..1879; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1346 | models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:7 | gwce.F:1181 | X | baseline 1181-1181: parent 1181..1181 → child 1181..1181; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1360 | models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:36 | gwce.F:1181 | X | baseline 1181-1181: parent 1181..1181 → child 1181..1181; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1382 | models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:78 | gwce.F:1181 | X | baseline 1181-1181: parent 1181..1181 → child 1181..1181; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1386 | models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:7 | gwce.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1390 | models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:21 | gwce.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1404 | models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:40 | gwce.F:166-226 | X | baseline 166-226: parent 166..226 → child 166..226; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1413 | models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:81 | gwce.F:2514-2522 | X | baseline 2514-2522: parent 2514..2522 → child 2514..2522; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1415 | models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:82 | gwce.F:1540-1543 | X | baseline 1540-1543: parent 1540..1543 → child 1540..1543; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1418 | models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:83 | gwce.F:71,182 | X | baseline 71-71: parent 71..71 → child 71..71; Δ=+0; baseline 182-182: parent 182..182 → child 182..182; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1420 | models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:84 | gwce.F:418-420,2001-2017 | X | baseline 418-420: parent 418..420 → child 418..420; Δ=+0; baseline 2001-2017: parent 2001..2017 → child 2001..2017; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1506 | models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:27 | src/gwce.F:506-507,1318-1321,2474,2571-2573 | X | baseline 506-507: parent 506..507 → child 506..507; Δ=+0; baseline 1318-1321: parent 1318..1321 → child 1318..1321; Δ=+0; baseline 2474-2474: parent 2474..2474 → child 2474..2474; Δ=+0; baseline 2571-2573: parent 2571..2573 → child 2571..2573; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1542 | models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:72 | gwce.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1550 | models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:76 | src/gwce.F:477 | X | baseline 477-477: parent 477..477 → child 477..477; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1557 | models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:81 | src/gwce.F:515-516 | X | baseline 515-516: parent 515..516 → child 515..516; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1559 | models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:85 | src/gwce.F:2477-2482 | X | baseline 2477-2482: parent 2477..2482 → child 2477..2482; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1573 | models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:122 | src/gwce.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1995 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:66 | gwce.F:1644-1649 | X | baseline 1644-1649: parent 1644..1649 → child 1644..1649; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2000 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:73 | src/gwce.F:1638-1650 | X | baseline 1638-1650: parent 1638..1650 → child 1638..1650; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2035 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:143 | src/gwce.F:1644-1649 | X | baseline 1644-1649: parent 1644..1649 → child 1644..1649; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2046 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:163 | src/gwce.F:1638-1650 | X | baseline 1638-1650: parent 1638..1650 → child 1638..1650; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2056 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:175 | src/gwce.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 2073 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:49 | src/gwce.F:1638-1649 | X | baseline 1638-1649: parent 1638..1649 → child 1638..1649; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2079 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:72 | src/gwce.F:1638-1649 | X | baseline 1638-1649: parent 1638..1649 → child 1638..1649; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2085 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:123 | src/gwce.F:1638-1649 | X | baseline 1638-1649: parent 1638..1649 → child 1638..1649; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2088 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:128 | src/gwce.F:1638-1651 | X | baseline 1638-1651: parent 1638..1651 → child 1638..1651; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2096 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:143 | src/gwce.F:1638-1649 | X | baseline 1638-1649: parent 1638..1649 → child 1638..1649; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2121 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:221 | gwce.F:1638-1650 | X | baseline 1638-1650: parent 1638..1650 → child 1638..1650; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2155 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:305 | gwce.F:1644-1649 | X | baseline 1644-1649: parent 1644..1649 → child 1644..1649; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2159 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:315 | src/gwce.F:1642-1649 | X | baseline 1642-1649: parent 1642..1649 → child 1642..1649; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2168 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:335 | src/gwce.F:1642-1649 | X | baseline 1642-1649: parent 1642..1649 → child 1642..1649; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2173 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:337 | gwce.F:1642-1644 | X | baseline 1642-1644: parent 1642..1644 → child 1642..1644; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2177 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:339 | src/gwce.F:1642-1649 | X | baseline 1642-1649: parent 1642..1649 → child 1642..1649; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2179 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:346 | src/gwce.F:1638-1649 | X | baseline 1638-1649: parent 1638..1649 → child 1638..1649; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2181 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:356 | src/gwce.F:1642-1649 | X | baseline 1642-1649: parent 1642..1649 → child 1642..1649; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |

### 참조 원장 8c547d26c19b · src/mesh.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 1993 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:66 | mesh.F:1822-1834 | X | baseline 1822-1834: parent 1822..1834 → child 1822..1834; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2076 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:63 | src/mesh.F:1822-1834 | X | baseline 1822-1834: parent 1822..1834 → child 1822..1834; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2131 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:250 | src/mesh.F:1822-1834 | X | baseline 1822-1834: parent 1822..1834 → child 1822..1834; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |

### 참조 원장 aef3777ed09d · CITATION.cff

직접 ref_file 매칭 0행. 주제/심볼 anchor는 위 판정 참조.

### 참조 원장 e65ef6063673 · src/cstart.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 126 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:23 | cstart.F:348 | X | baseline 348-348: parent 348..348 → child 348..348; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 134 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:36 | cstart.F:348 | X | baseline 348-348: parent 348..348 → child 348..348; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 371 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:53 | src/cstart.F:313 | X | baseline 313-313: parent 313..313 → child 313..313; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 383 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:63 | src/cstart.F:376 | X | baseline 376-376: parent 376..376 → child 376..376; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 389 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:64 | src/cstart.F:394 | X | baseline 394-394: parent 394..394 → child 394..394; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 393 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:65 | src/cstart.F:487 | X | baseline 487-487: parent 487..487 → child 487..487; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 396 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:66 | src/cstart.F:584 | X | baseline 584-584: parent 584..584 → child 584..584; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 399 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:67 | src/cstart.F:467 | X | baseline 467-467: parent 467..467 → child 467..467; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 402 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:68 | src/cstart.F:412 | X | baseline 412-412: parent 412..412 → child 412..412; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 405 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:69 | src/cstart.F:665 | X | baseline 665-665: parent 665..665 → child 665..665; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 408 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:70 | src/cstart.F:501 | X | baseline 501-501: parent 501..501 → child 501..501; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 412 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:71 | src/cstart.F:492 | X | baseline 492-492: parent 492..492 → child 492..492; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 475 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:145 | cstart.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 502 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:180 | src/cstart.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 629 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:57 | src/cstart.F:64 | X | baseline 64-64: parent 64..64 → child 64..64; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 638 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:60 | src/cstart.F:1221-1223,1258-1260 | N | baseline 1221-1223: parent 1221..1223 → child 1226..1228; Δ=+5; baseline 1258-1260: parent 1258..1260 → child 1263..1265; Δ=+5; 인용 변경/좌표 이동 |
| 649 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:74 | src/cstart.F:1221-1231,1258-1268 | N | baseline 1221-1231: parent 1221..1231 → child 1226..1236; Δ=+5; baseline 1258-1268: parent 1258..1268 → child 1263..1273; Δ=+5; 인용 변경/좌표 이동 |
| 670 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:105 | src/cstart.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 2061 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:178 | src/cstart.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |

### 참조 원장 e65ef6063673 · src/hstart.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 179 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:194 | hstart.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 476 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:145 | hstart.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 477 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:145 | hstart.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 503 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:180 | src/hstart.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 603 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:37 | src/hstart.F:719-720 | N | baseline 719-720: parent 719..720 → child 725..725 [?]; Δ=+5; changed/replaced; 삭제/치환점 정확한 대응 불명; 인용 변경/좌표 이동 |
| 630 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:57 | src/hstart.F:58 | X | baseline 58-58: parent 58..58 → child 58..58; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 642 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:65 | src/hstart.F:1522,1530-1532 | N | baseline 1522-1522: parent 1522..1522 → child 1527..1527; Δ=+5; baseline 1530-1532: parent 1530..1532 → child 1535..1537; Δ=+5; 인용 변경/좌표 이동 |
| 671 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:105 | src/hstart.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 680 | models/ADCIRC/source-analysis/adcirc-hotstart.md:21 | hstart.F:47-3048 | N | baseline 47-3048: parent 47..3048 → child 47..3090 [?]; Δ=+0/+5/+7/+8/+13/+42; changed/replaced; 삭제/치환점 정확한 대응 불명; 인용 변경/좌표 이동 |
| 691 | models/ADCIRC/source-analysis/adcirc-hotstart.md:35 | hstart.F:242-253 | X | baseline 242-253: parent 242..253 → child 242..253; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 692 | models/ADCIRC/source-analysis/adcirc-hotstart.md:36 | hstart.F:452-465 | X | baseline 452-465: parent 452..465 → child 452..465; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 693 | models/ADCIRC/source-analysis/adcirc-hotstart.md:38 | hstart.F:673-690 | X | baseline 673-690: parent 673..690 → child 673..690; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 695 | models/ADCIRC/source-analysis/adcirc-hotstart.md:45 | hstart.F:485-492 | X | baseline 485-492: parent 485..492 → child 485..492; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 698 | models/ADCIRC/source-analysis/adcirc-hotstart.md:70 | hstart.F:506-668 | X | baseline 506-668: parent 506..668 → child 506..668; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 699 | models/ADCIRC/source-analysis/adcirc-hotstart.md:72 | hstart.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 700 | models/ADCIRC/source-analysis/adcirc-hotstart.md:76 | hstart.F:47 | X | baseline 47-47: parent 47..47 → child 47..47; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 702 | models/ADCIRC/source-analysis/adcirc-hotstart.md:83 | hstart.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 715 | models/ADCIRC/source-analysis/adcirc-hotstart.md:122 | hstart.F:526-536 | X | baseline 526-536: parent 526..536 → child 526..536; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 717 | models/ADCIRC/source-analysis/adcirc-hotstart.md:123 | hstart.F:529-533 | X | baseline 529-533: parent 529..533 → child 529..533; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 722 | models/ADCIRC/source-analysis/adcirc-hotstart.md:130 | hstart.F:1440-1444 | N | baseline 1440-1444: parent 1440..1444 → child 1445..1449; Δ=+5; 인용 변경/좌표 이동 |
| 725 | models/ADCIRC/source-analysis/adcirc-hotstart.md:144 | hstart.F:1442-1444 | N | baseline 1442-1444: parent 1442..1444 → child 1447..1449; Δ=+5; 인용 변경/좌표 이동 |
| 1250 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:25 | hstart.F:325-337 | X | baseline 325-337: parent 325..337 → child 325..337; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1293 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:129 | hstart.F:325-337 | X | baseline 325-337: parent 325..337 → child 325..337; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2006 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:106 | src/hstart.F:1529-1532 | N | baseline 1529-1532: parent 1529..1532 → child 1534..1537; Δ=+5; 인용 변경/좌표 이동 |
| 2026 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:137 | src/hstart.F:1525-1532 | N | baseline 1525-1532: parent 1525..1532 → child 1530..1537; Δ=+5; 인용 변경/좌표 이동 |
| 2060 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:178 | src/hstart.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 2124 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:223 | hstart.F:1525-1532 | N | baseline 1525-1532: parent 1525..1532 → child 1530..1537; Δ=+5; 인용 변경/좌표 이동 |
| 2157 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:310 | hstart.F:1525-1532 | N | baseline 1525-1532: parent 1525..1532 → child 1530..1537; Δ=+5; 인용 변경/좌표 이동 |

### 참조 원장 e65ef6063673 · src/netcdfio.F90

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 684 | models/ADCIRC/source-analysis/adcirc-hotstart.md:24 | netcdfio.F90:3866-9188 | N | baseline 3866-9188: parent 3866..9188 → child 3890..9237 [?]; Δ=+24/+26/+28/+30/+32/+33/+35/+37/+39/+41/+43/+45/+47/+49; changed/replaced; 삭제/치환점 정확한 대응 불명; 인용 변경/좌표 이동 |
| 707 | models/ADCIRC/source-analysis/adcirc-hotstart.md:90 | netcdfio.F90:3866-3871 | N | baseline 3866-3871: parent 3866..3871 → child 3890..3895; Δ=+24; 인용 변경/좌표 이동 |
| 718 | models/ADCIRC/source-analysis/adcirc-hotstart.md:123 | netcdfio.F90:5357-5380 | N | baseline 5357-5380: parent 5357..5380 → child 5390..5413; Δ=+33; 인용 변경/좌표 이동 |
| 724 | models/ADCIRC/source-analysis/adcirc-hotstart.md:138 | netcdfio.F90:8109-8158 | N | baseline 8109-8158: parent 8109..8158 → child 8158..8207; Δ=+49; 인용 변경/좌표 이동 |
| 744 | models/ADCIRC/source-analysis/adcirc-hotstart.md:188 | netcdfio.F90:8017-8085 | N | baseline 8017-8085: parent 8017..8085 → child 8066..8134; Δ=+49; 인용 변경/좌표 이동 |
| 1252 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:25 | netcdfio.F90:5555-7045,8017-8085 | N | baseline 5555-7045: parent 5555..7045 → child 5588..7092 [?]; Δ=+33/+35/+37/+39/+41/+43/+45/+47; changed/replaced; 삭제/치환점 정확한 대응 불명; baseline 8017-8085: parent 8017..8085 → child 8066..8134; Δ=+49; 인용 변경/좌표 이동 |
| 1295 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:135 | netcdfio.F90:5555-5568 | N | baseline 5555-5568: parent 5555..5568 → child 5588..5601; Δ=+33; 인용 변경/좌표 이동 |
| 1301 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:142 | netcdfio.F90:8017-8085 | N | baseline 8017-8085: parent 8017..8085 → child 8066..8134; Δ=+49; 인용 변경/좌표 이동 |
| 1316 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:174 | netcdfio.F90:8017-8085 | N | baseline 8017-8085: parent 8017..8085 → child 8066..8134; Δ=+49; 인용 변경/좌표 이동 |

### 참조 원장 e65ef6063673 · src/nodalattr.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 361 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51 | src/nodalattr.F:1141,1154 | X | baseline 1141-1141: parent 1141..1141 → child 1141..1141; Δ=+0; baseline 1154-1154: parent 1154..1154 → child 1154..1154; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 362 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51 | src/nodalattr.F:1141,1154 | X | baseline 1141-1141: parent 1141..1141 → child 1141..1141; Δ=+0; baseline 1154-1154: parent 1154..1154 → child 1154..1154; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 489 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:160 | src/nodalattr.F:1051 | X | baseline 1051-1051: parent 1051..1051 → child 1051..1051; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 495 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:175 | src/nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 931 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:68 | nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 961 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:6 | models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 962 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:19 | src/nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 965 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:21 | nodalattr.F:636-686 | X | baseline 636-686: parent 636..686 → child 636..686; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 983 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:73 | nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1218 | models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:39 | src/nodalattr.F:1051 | X | baseline 1051-1051: parent 1051..1051 → child 1051..1051; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1375 | models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:56 | nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |

### 참조 원장 e65ef6063673 · src/read_input.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 123 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:20 | read_input.F:1176-1191,3072,5139-5482,5682 | N | baseline 1176-1191: parent 1176..1191 → child 1176..1191; Δ=+0; baseline 3072-3072: parent 3072..3072 → child 3072..3072; Δ=+0; baseline 5139-5482: parent 5139..5482 → child 5139..5482; Δ=+0; baseline 5682-5682: parent 5682..5682 → child 5706..5706; Δ=+24; 인용 변경/좌표 이동 |
| 135 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:37 | read_input.F:1176-1191 | X | baseline 1176-1191: parent 1176..1191 → child 1176..1191; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 136 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:44 | read_input.F:5139 | X | baseline 5139-5139: parent 5139..5139 → child 5139..5139; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 146 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:70 | read_input.F:5682 | N | baseline 5682-5682: parent 5682..5682 → child 5706..5706; Δ=+24; 인용 변경/좌표 이동 |
| 162 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:116 | read_input.F:5235 | X | baseline 5235-5235: parent 5235..5235 → child 5235..5235; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 168 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:135 | read_input.F:5296 | X | baseline 5296-5296: parent 5296..5296 → child 5296..5296; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 183 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:7 | read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 194 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:25 | read_input.F:5073 | X | baseline 5073-5073: parent 5073..5073 → child 5073..5073; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 197 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:30 | read_input.F:5127 | X | baseline 5127-5127: parent 5127..5127 → child 5127..5127; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 214 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:65 | read_input.F:5102 | X | baseline 5102-5102: parent 5102..5102 → child 5102..5102; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 302 | models/ADCIRC/source-analysis/adcirc-dg-continuity-solver.md:62 | src/read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 327 | models/ADCIRC/source-analysis/adcirc-dg-continuity-solver.md:276 | read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 353 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:44 | src/read_input.F:380 | X | baseline 380-380: parent 380..380 → child 380..380; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 357 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:45 | src/read_input.F:394,5296 | X | baseline 394-394: parent 394..394 → child 394..394; Δ=+0; baseline 5296-5296: parent 5296..5296 → child 5296..5296; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 358 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:45 | src/read_input.F:394,5296 | X | baseline 394-394: parent 394..394 → child 394..394; Δ=+0; baseline 5296-5296: parent 5296..5296 → child 5296..5296; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 373 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:54 | src/read_input.F:6425,6453 | N | baseline 6425-6425: parent 6425..6425 → child 6449..6449; Δ=+24; baseline 6453-6453: parent 6453..6453 → child 6477..6477; Δ=+24; 인용 변경/좌표 이동 |
| 374 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:54 | src/read_input.F:6425,6453 | N | baseline 6425-6425: parent 6425..6425 → child 6449..6449; Δ=+24; baseline 6453-6453: parent 6453..6453 → child 6477..6477; Δ=+24; 인용 변경/좌표 이동 |
| 492 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:174 | src/read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 522 | models/ADCIRC/source-analysis/adcirc-fort15-checklist-v1.md:7 | read_input.F:1133-1162 | X | baseline 1133-1162: parent 1133..1162 → child 1133..1162; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 543 | models/ADCIRC/source-analysis/adcirc-fort15-checklist-v1.md:88 | models/ADCIRC/raw/source_code/adcirc/src/read_input.F:1133-1135 | X | baseline 1133-1135: parent 1133..1135 → child 1133..1135; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 661 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:88 | read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 666 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:97 | read_input.F:3431-3456 | X | baseline 3431-3456: parent 3431..3456 → child 3431..3456; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 675 | models/ADCIRC/source-analysis/adcirc-hotstart.md:19 | read_input.F:1050-1075,4504-4544 | X | baseline 1050-1075: parent 1050..1075 → child 1050..1075; Δ=+0; baseline 4504-4544: parent 4504..4544 → child 4504..4544; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 687 | models/ADCIRC/source-analysis/adcirc-hotstart.md:30 | read_input.F:1050-1053 | X | baseline 1050-1053: parent 1050..1053 → child 1050..1053; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 694 | models/ADCIRC/source-analysis/adcirc-hotstart.md:41 | read_input.F:1063-1075 | X | baseline 1063-1075: parent 1063..1075 → child 1063..1075; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 711 | models/ADCIRC/source-analysis/adcirc-hotstart.md:104 | read_input.F:4504-4508 | X | baseline 4504-4508: parent 4504..4508 → child 4504..4508; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 784 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:21 | src/read_input.F:1755-1774 | X | baseline 1755-1774: parent 1755..1774 → child 1755..1774; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 792 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:27 | src/read_input.F:1825-2070 | X | baseline 1825-2070: parent 1825..2070 → child 1825..2070; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 794 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:33 | read_input.F:1819-1824 | X | baseline 1819-1824: parent 1819..1824 → child 1819..1824; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 796 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:34 | read_input.F:1825-1832 | X | baseline 1825-1832: parent 1825..1832 → child 1825..1832; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 799 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:35 | read_input.F:1833-1852 | X | baseline 1833-1852: parent 1833..1852 → child 1833..1852; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 801 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:36 | read_input.F:1853-1864 | X | baseline 1853-1864: parent 1853..1864 → child 1853..1864; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 803 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:37 | read_input.F:1865-1890 | X | baseline 1865-1890: parent 1865..1890 → child 1865..1890; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 805 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:38 | read_input.F:1891-1916 | X | baseline 1891-1916: parent 1891..1916 → child 1891..1916; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 807 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:39 | read_input.F:1917-1929 | X | baseline 1917-1929: parent 1917..1929 → child 1917..1929; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 809 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:40 | read_input.F:1933-1952 | X | baseline 1933-1952: parent 1933..1952 → child 1933..1952; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 811 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:41 | read_input.F:1976-1989 | X | baseline 1976-1989: parent 1976..1989 → child 1976..1989; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 813 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:42 | read_input.F:1990-2002 | X | baseline 1990-2002: parent 1990..2002 → child 1990..2002; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 815 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:43 | read_input.F:2004-2031 | X | baseline 2004-2031: parent 2004..2031 → child 2004..2031; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 817 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:44 | read_input.F:2658,4671 | X | baseline 2658-2658: parent 2658..2658 → child 2658..2658; Δ=+0; baseline 4671-4671: parent 4671..4671 → child 4671..4671; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 819 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:45 | read_input.F:2033-2058 | X | baseline 2033-2058: parent 2033..2058 → child 2033..2058; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 821 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:46 | read_input.F:2059-2069,2767-2774 | X | baseline 2059-2069: parent 2059..2069 → child 2059..2069; Δ=+0; baseline 2767-2774: parent 2767..2774 → child 2767..2774; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 853 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:83 | src/read_input.F:269-270,516-519 | X | baseline 269-270: parent 269..270 → child 269..270; Δ=+0; baseline 516-519: parent 516..519 → child 516..519; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 858 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:89 | src/read_input.F:2032-2058 | X | baseline 2032-2058: parent 2032..2058 → child 2032..2058; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 865 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:94 | src/read_input.F:2059-2069 | X | baseline 2059-2069: parent 2059..2069 → child 2059..2069; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 873 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:105 | src/read_input.F:238,484-487 | X | baseline 238-238: parent 238..238 → child 238..238; Δ=+0; baseline 484-487: parent 484..487 → child 484..487; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 883 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:121 | read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 884 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:122 | src/read_input.F:3988-3993,4003-4014,4051 | X | baseline 3988-3993: parent 3988..3993 → child 3988..3993; Δ=+0; baseline 4003-4014: parent 4003..4014 → child 4003..4014; Δ=+0; baseline 4051-4051: parent 4051..4051 → child 4051..4051; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 885 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:123 | src/read_input.F:4345-4353,4360-4371 | X | baseline 4345-4353: parent 4345..4353 → child 4345..4353; Δ=+0; baseline 4360-4371: parent 4360..4371 → child 4360..4371; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 889 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:124 | read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 901 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:156 | src/read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 938 | models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:7 | read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 945 | models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:20 | read_input.F:3504-3589 | X | baseline 3504-3589: parent 3504..3589 → child 3504..3589; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 947 | models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:22 | read_input.F:3505 | X | baseline 3505-3505: parent 3505..3505 → child 3505..3505; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 994 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:31 | read_input.F:3613-3633,4124-4152 | X | baseline 3613-3633: parent 3613..3633 → child 3613..3633; Δ=+0; baseline 4124-4152: parent 4124..4152 → child 4124..4152; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 995 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:31 | src/read_input.F:3613-3633,4124-4152 | X | baseline 3613-3633: parent 3613..3633 → child 3613..3633; Δ=+0; baseline 4124-4152: parent 4124..4152 → child 4124..4152; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1012 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:56 | read_input.F:3998-4021,4356-4384 | X | baseline 3998-4021: parent 3998..4021 → child 3998..4021; Δ=+0; baseline 4356-4384: parent 4356..4384 → child 4356..4384; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1013 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:56 | src/read_input.F:3998-4021,4356-4384 | X | baseline 3998-4021: parent 3998..4021 → child 3998..4021; Δ=+0; baseline 4356-4384: parent 4356..4384 → child 4356..4384; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1026 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:70 | src/read_input.F:4421-4452,4500 | X | baseline 4421-4452: parent 4421..4452 → child 4421..4452; Δ=+0; baseline 4500-4500: parent 4500..4500 → child 4500..4500; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1149 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:78 | src/read_input.F:394 | X | baseline 394-394: parent 394..394 → child 394..394; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1246 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:22 | read_input.F:1080-1083,1790-1817,2255-2261 | X | baseline 1080-1083: parent 1080..1083 → child 1080..1083; Δ=+0; baseline 1790-1817: parent 1790..1817 → child 1790..1817; Δ=+0; baseline 2255-2261: parent 2255..2261 → child 2255..2261; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1287 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:94 | read_input.F:1790-1817 | X | baseline 1790-1817: parent 1790..1817 → child 1790..1817; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1296 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:138 | read_input.F:1080-1083 | X | baseline 1080-1083: parent 1080..1083 → child 1080..1083; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1414 | models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:82 | read_input.F:2996 | X | baseline 2996-2996: parent 2996..2996 → child 2996..2996; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1845 | models/ADCIRC/source-analysis/storm-surge/README.md:9 | read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1848 | models/ADCIRC/source-analysis/storm-surge/README.md:16 | read_input.F:2157 | X | baseline 2157-2157: parent 2157..2157 → child 2157..2157; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1854 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-foundation.md:7 | read_input.F:1782 | X | baseline 1782-1782: parent 1782..1782 → child 1782..1782; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1863 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-foundation.md:95 | read_input.F:1782 | X | baseline 1782-1782: parent 1782..1782 → child 1782..1782; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1890 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md:7 | read_input.F:1782 | X | baseline 1782-1782: parent 1782..1782 → child 1782..1782; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1894 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md:55 | read_input.F:1782 | X | baseline 1782-1782: parent 1782..1782 → child 1782..1782; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1922 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:24 | read_input.F:2157,2190,2255-2261,2430,2706,2884,2975 | X | baseline 2157-2157: parent 2157..2157 → child 2157..2157; Δ=+0; baseline 2190-2190: parent 2190..2190 → child 2190..2190; Δ=+0; baseline 2255-2261: parent 2255..2261 → child 2255..2261; Δ=+0; baseline 2430-2430: parent 2430..2430 → child 2430..2430; Δ=+0; baseline 2706-2706: parent 2706..2706 → child 2706..2706; Δ=+0; baseline 2884-2884: parent 2884..2884 → child 2884..2884; Δ=+0; baseline 2975-2975: parent 2975..2975 → child 2975..2975; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1933 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:36 | read_input.F:2706 | X | baseline 2706-2706: parent 2706..2706 → child 2706..2706; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1945 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:61 | read_input.F:2157 | X | baseline 2157-2157: parent 2157..2157 → child 2157..2157; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1969 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:157 | read_input.F:2430 | X | baseline 2430-2430: parent 2430..2430 → child 2430..2430; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1979 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:38 | src/read_input.F:1705-1731 | X | baseline 1705-1731: parent 1705..1731 → child 1705..1731; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1981 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:42 | src/read_input.F:6282-6463 | N | baseline 6282-6463: parent 6282..6463 → child 6306..6487; Δ=+24; 인용 변경/좌표 이동 |
| 1985 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:47 | src/read_input.F:3410-3436 | X | baseline 3410-3436: parent 3410..3436 → child 3410..3436; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1989 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:50 | src/read_input.F:3450-3456 | X | baseline 3450-3456: parent 3450..3456 → child 3450..3456; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1991 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:64 | src/read_input.F:3431-3456,3485-3497 | X | baseline 3431-3456: parent 3431..3456 → child 3431..3456; Δ=+0; baseline 3485-3497: parent 3485..3497 → child 3485..3497; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1994 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:66 | read_input.F:3493-3496 | X | baseline 3493-3496: parent 3493..3496 → child 3493..3496; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2001 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:77 | src/read_input.F:3410-3436,3450-3456 | X | baseline 3410-3436: parent 3410..3436 → child 3410..3436; Δ=+0; baseline 3450-3456: parent 3450..3456 → child 3450..3456; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2002 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:88 | src/read_input.F:6282-6463 | N | baseline 6282-6463: parent 6282..6463 → child 6306..6487; Δ=+24; 인용 변경/좌표 이동 |
| 2005 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:98 | src/read_input.F:6429-6455 | N | baseline 6429-6455: parent 6429..6455 → child 6453..6479; Δ=+24; 인용 변경/좌표 이동 |
| 2012 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:112 | src/read_input.F:3347-3354 | X | baseline 3347-3354: parent 3347..3354 → child 3347..3354; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2031 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:142 | src/read_input.F:3349,3371-3383 | X | baseline 3349-3349: parent 3349..3349 → child 3349..3349; Δ=+0; baseline 3371-3383: parent 3371..3383 → child 3371..3383; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2034 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:143 | src/read_input.F:3429-3436,3433 | X | baseline 3429-3436: parent 3429..3436 → child 3429..3436; Δ=+0; baseline 3433-3433: parent 3433..3433 → child 3433..3433; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2039 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:144 | src/read_input.F:2541 | X | baseline 2541-2541: parent 2541..2541 → child 2541..2541; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2054 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:174 | src/read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 2066 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:48 | src/read_input.F:1703-1731,3335-3349 | X | baseline 1703-1731: parent 1703..1731 → child 1703..1731; Δ=+0; baseline 3335-3349: parent 3335..3349 → child 3335..3349; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2072 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:49 | src/read_input.F:3431-3441 | X | baseline 3431-3441: parent 3431..3441 → child 3431..3441; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2077 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:63 | src/read_input.F:3431-3456,3485-3497 | X | baseline 3431-3456: parent 3431..3456 → child 3431..3456; Δ=+0; baseline 3485-3497: parent 3485..3497 → child 3485..3497; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2078 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:71 | src/read_input.F:1717-1731,3431-3435,3485-3497 | X | baseline 1717-1731: parent 1717..1731 → child 1717..1731; Δ=+0; baseline 3431-3435: parent 3431..3435 → child 3431..3435; Δ=+0; baseline 3485-3497: parent 3485..3497 → child 3485..3497; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2086 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:128 | src/read_input.F:2894-2902 | X | baseline 2894-2902: parent 2894..2902 → child 2894..2902; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2089 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:130 | src/read_input.F:3628-3632,3757-3761,4143-4148,4217-4222,4534-4537 | X | baseline 3628-3632: parent 3628..3632 → child 3628..3632; Δ=+0; baseline 3757-3761: parent 3757..3761 → child 3757..3761; Δ=+0; baseline 4143-4148: parent 4143..4148 → child 4143..4148; Δ=+0; baseline 4217-4222: parent 4217..4222 → child 4217..4222; Δ=+0; baseline 4534-4537: parent 4534..4537 → child 4534..4537; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2119 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:220 | read_input.F:1705-1731,3344-3497,6282-6463 | N | baseline 1705-1731: parent 1705..1731 → child 1705..1731; Δ=+0; baseline 3344-3497: parent 3344..3497 → child 3344..3497; Δ=+0; baseline 6282-6463: parent 6282..6463 → child 6306..6487; Δ=+24; 인용 변경/좌표 이동 |
| 2125 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:241 | read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 2132 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:250 | src/read_input.F:3493-3496 | X | baseline 3493-3496: parent 3493..3496 → child 3493..3496; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2136 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:254 | read_input.F:6282-6463 | N | baseline 6282-6463: parent 6282..6463 → child 6306..6487; Δ=+24; 인용 변경/좌표 이동 |
| 2165 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:335 | src/read_input.F:2534-2543,3436,3493-3496 | X | baseline 2534-2543: parent 2534..2543 → child 2534..2543; Δ=+0; baseline 3436-3436: parent 3436..3436 → child 3436..3436; Δ=+0; baseline 3493-3496: parent 3493..3496 → child 3493..3496; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2167 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:335 | src/read_input.F:2534-2543,3436,3493-3496 | X | baseline 2534-2543: parent 2534..2543 → child 2534..2543; Δ=+0; baseline 3436-3436: parent 3436..3436 → child 3436..3436; Δ=+0; baseline 3493-3496: parent 3493..3496 → child 3493..3496; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2178 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:346 | src/read_input.F:3431-3456,3485-3497 | X | baseline 3431-3456: parent 3431..3456 → child 3431..3456; Δ=+0; baseline 3485-3497: parent 3485..3497 → child 3485..3497; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2180 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:355 | src/read_input.F:3485-3497 | X | baseline 3485-3497: parent 3485..3497 → child 3485..3497; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 2182 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:368 | src/read_input.F:1705-1731,3410-3444 | X | baseline 1705-1731: parent 1705..1731 → child 1705..1731; Δ=+0; baseline 3410-3444: parent 3410..3444 → child 3410..3444; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |

### 참조 원장 e65ef6063673 · src/vsmy.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 130 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:26 | vsmy.F:1168,1543-3871,4061-4315 | N | baseline 1168-1168: parent 1168..1168 → child 1168..1168; Δ=+0; baseline 1543-3871: parent 1543..3871 → child 1545..3873; Δ=+2; baseline 4061-4315: parent 4061..4315 → child 4076..4330; Δ=+15; 인용 변경/좌표 이동 |
| 141 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:60 | vsmy.F:1548-1553 | N | baseline 1548-1553: parent 1548..1553 → child 1550..1555; Δ=+2; 인용 변경/좌표 이동 |
| 145 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:68 | vsmy.F:1630 | N | baseline 1630-1630: parent 1630..1630 → child 1632..1632; Δ=+2; 인용 변경/좌표 이동 |
| 149 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:74 | vsmy.F:4061 | N | baseline 4061-4061: parent 4061..4061 → child 4076..4076; Δ=+15; 인용 변경/좌표 이동 |
| 156 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:94 | vsmy.F:1168 | X | baseline 1168-1168: parent 1168..1168 → child 1168..1168; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 164 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:121 | vsmy.F:1823,1840,1870,1931,1983 | N | baseline 1823-1823: parent 1823..1823 → child 1825..1825; Δ=+2; baseline 1840-1840: parent 1840..1840 → child 1842..1842; Δ=+2; baseline 1870-1870: parent 1870..1870 → child 1872..1872; Δ=+2; baseline 1931-1931: parent 1931..1931 → child 1933..1933; Δ=+2; baseline 1983-1983: parent 1983..1983 → child 1985..1985; Δ=+2; 인용 변경/좌표 이동 |
| 165 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:122 | vsmy.F:2035,2403 | N | baseline 2035-2035: parent 2035..2035 → child 2037..2037; Δ=+2; baseline 2403-2403: parent 2403..2403 → child 2405..2405; Δ=+2; 인용 변경/좌표 이동 |
| 166 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:127 | vsmy.F:2740 | N | baseline 2740-2740: parent 2740..2740 → child 2742..2742; Δ=+2; 인용 변경/좌표 이동 |
| 181 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:2 | vsmy.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 182 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:7 | vsmy.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 188 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:23 | vsmy.F:142-1703 | N | baseline 142-1703: parent 142..1703 → child 142..1705 [?]; Δ=+0/+2; changed/replaced; 삭제/치환점 정확한 대응 불명; 인용 변경/좌표 이동 |
| 200 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:43 | vsmy.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 208 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:53 | vsmy.F:2299-2319 | N | baseline 2299-2319: parent 2299..2319 → child 2301..2321; Δ=+2; 인용 변경/좌표 이동 |
| 244 | models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:61 | vsmy.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 683 | models/ADCIRC/source-analysis/adcirc-hotstart.md:23 | vsmy.F:3254,3531-3778 | N | baseline 3254-3254: parent 3254..3254 → child 3256..3256; Δ=+2; baseline 3531-3778: parent 3531..3778 → child 3533..3780; Δ=+2; 인용 변경/좌표 이동 |
| 706 | models/ADCIRC/source-analysis/adcirc-hotstart.md:86 | vsmy.F:3254 | N | baseline 3254-3254: parent 3254..3254 → child 3256..3256; Δ=+2; 인용 변경/좌표 이동 |
| 719 | models/ADCIRC/source-analysis/adcirc-hotstart.md:127 | vsmy.F:3531-3778 | N | baseline 3531-3778: parent 3531..3778 → child 3533..3780; Δ=+2; 인용 변경/좌표 이동 |
| 909 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:19 | vsmy.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 936 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:75 | vsmy.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 937 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:80 | vsmy.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1465 | models/ADCIRC/source-analysis/adcirc-transport-solver.md:6 | vsmy.F:1543,1548-1553 | N | baseline 1543-1543: parent 1543..1543 → child 1545..1545; Δ=+2; baseline 1548-1553: parent 1548..1553 → child 1550..1555; Δ=+2; 인용 변경/좌표 이동 |
| 1466 | models/ADCIRC/source-analysis/adcirc-transport-solver.md:6 | vsmy.F:1543,1548-1553 | N | baseline 1543-1543: parent 1543..1543 → child 1545..1545; Δ=+2; baseline 1548-1553: parent 1548..1553 → child 1550..1555; Δ=+2; 인용 변경/좌표 이동 |
| 1472 | models/ADCIRC/source-analysis/adcirc-transport-solver.md:20 | vsmy.F:1548-1553 | N | baseline 1548-1553: parent 1548..1553 → child 1550..1555; Δ=+2; 인용 변경/좌표 이동 |
| 1473 | models/ADCIRC/source-analysis/adcirc-transport-solver.md:21 | vsmy.F:1543 | N | baseline 1543-1543: parent 1543..1543 → child 1545..1545; Δ=+2; 인용 변경/좌표 이동 |
| 1474 | models/ADCIRC/source-analysis/adcirc-transport-solver.md:21 | vsmy.F:1543 | N | baseline 1543-1543: parent 1543..1543 → child 1545..1545; Δ=+2; 인용 변경/좌표 이동 |
| 1486 | models/ADCIRC/source-analysis/adcirc-transport-solver.md:59 | vsmy.F:1548-1553 | N | baseline 1548-1553: parent 1548..1553 → child 1550..1555; Δ=+2; 인용 변경/좌표 이동 |
| 1487 | models/ADCIRC/source-analysis/adcirc-transport-solver.md:62 | vsmy.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1490 | models/ADCIRC/source-analysis/adcirc-transport-solver.md:68 | vsmy.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |

### 참조 원장 e65ef6063673 · src/write_output.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 132 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:28 | write_output.F:2993-3331 | N | baseline 2993-3331: parent 2993..3331 → child 2994..3332; Δ=+1; 인용 변경/좌표 이동 |
| 169 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:135 | write_output.F:2993 | N | baseline 2993-2993: parent 2993..2993 → child 2994..2994; Δ=+1; 인용 변경/좌표 이동 |
| 171 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:144 | write_output.F:3331 | N | baseline 3331-3331: parent 3331..3331 → child 3332..3332; Δ=+1; 인용 변경/좌표 이동 |
| 306 | models/ADCIRC/source-analysis/adcirc-dg-continuity-solver.md:66 | src/write_output.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 382 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:63 | src/write_output.F:510 | X | baseline 510-510: parent 510..510 → child 510..510; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 388 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:64 | src/write_output.F:546 | X | baseline 546-546: parent 546..546 → child 546..546; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 392 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:65 | src/write_output.F:598 | X | baseline 598-598: parent 598..598 → child 598..598; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 395 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:66 | src/write_output.F:710 | X | baseline 710-710: parent 710..710 → child 710..710; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 398 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:67 | src/write_output.F:946 | X | baseline 946-946: parent 946..946 → child 946..946; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 401 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:68 | src/write_output.F:1160 | X | baseline 1160-1160: parent 1160..1160 → child 1160..1160; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 404 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:69 | src/write_output.F:1191 | X | baseline 1191-1191: parent 1191..1191 → child 1191..1191; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 407 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:70 | src/write_output.F:619 | X | baseline 619-619: parent 619..619 → child 619..619; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 411 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:71 | src/write_output.F:641 | X | baseline 641-641: parent 641..641 → child 641..641; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 413 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:79 | src/write_output.F:735 | X | baseline 735-735: parent 735..735 → child 735..735; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 418 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:80 | src/write_output.F:775 | X | baseline 775-775: parent 775..775 → child 775..775; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 422 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:81 | src/write_output.F:817 | X | baseline 817-817: parent 817..817 → child 817..817; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 426 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:82 | src/write_output.F:904 | X | baseline 904-904: parent 904..904 → child 904..904; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 430 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:83 | src/write_output.F:1064 | X | baseline 1064-1064: parent 1064..1064 → child 1064..1064; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 433 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:84 | src/write_output.F:1039 | X | baseline 1039-1039: parent 1039..1039 → child 1039..1039; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 436 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:90 | src/write_output.F:2993 | N | baseline 2993-2993: parent 2993..2993 → child 2994..2994; Δ=+1; 인용 변경/좌표 이동 |
| 443 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:91 | src/write_output.F:3059 | N | baseline 3059-3059: parent 3059..3059 → child 3060..3060; Δ=+1; 인용 변경/좌표 이동 |
| 453 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:99 | src/write_output.F:2178 | X | baseline 2178-2178: parent 2178..2178 → child 2178..2178; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 459 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:100 | src/write_output.F:2232 | X | baseline 2232-2232: parent 2232..2232 → child 2232..2232; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 463 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:101 | src/write_output.F:2339 | X | baseline 2339-2339: parent 2339..2339 → child 2339..2339; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 504 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:181 | src/write_output.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 681 | models/ADCIRC/source-analysis/adcirc-hotstart.md:22 | write_output.F:4429,4920-5374 | N | baseline 4429-4429: parent 4429..4429 → child 4459..4459; Δ=+30; baseline 4920-5374: parent 4920..5374 → child 4950..5404; Δ=+30; 인용 변경/좌표 이동 |
| 696 | models/ADCIRC/source-analysis/adcirc-hotstart.md:45 | write_output.F:4920-4923 | N | baseline 4920-4923: parent 4920..4923 → child 4950..4953; Δ=+30; 인용 변경/좌표 이동 |
| 697 | models/ADCIRC/source-analysis/adcirc-hotstart.md:47 | write_output.F:4922-4931 | N | baseline 4922-4931: parent 4922..4931 → child 4952..4961; Δ=+30; 인용 변경/좌표 이동 |
| 703 | models/ADCIRC/source-analysis/adcirc-hotstart.md:84 | write_output.F:4429 | N | baseline 4429-4429: parent 4429..4429 → child 4459..4459; Δ=+30; 인용 변경/좌표 이동 |
| 716 | models/ADCIRC/source-analysis/adcirc-hotstart.md:122 | write_output.F:4935-4945 | N | baseline 4935-4945: parent 4935..4945 → child 4965..4975; Δ=+30; 인용 변경/좌표 이동 |
| 890 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:124 | write_output.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 986 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:21 | src/write_output.F:1773 | X | baseline 1773-1773: parent 1773..1773 → child 1773..1773; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 988 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:22 | src/write_output.F:523,1811-1823 | X | baseline 523-523: parent 523..523 → child 523..523; Δ=+0; baseline 1811-1823: parent 1811..1823 → child 1811..1823; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 990 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:23 | src/write_output.F:504-523,593-603 | X | baseline 504-523: parent 504..523 → child 504..523; Δ=+0; baseline 593-603: parent 593..603 → child 593..603; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 996 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:32 | src/write_output.F:4226-4250 | N | baseline 4226-4250: parent 4226..4250 → child 4256..4280; Δ=+30; 인용 변경/좌표 이동 |
| 1001 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:42 | src/write_output.F:1568-1575,1691-1693 | X | baseline 1568-1575: parent 1568..1575 → child 1568..1575; Δ=+0; baseline 1691-1693: parent 1691..1693 → child 1691..1693; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1002 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:47 | src/write_output.F:537-563,710-714 | X | baseline 537-563: parent 537..563 → child 537..563; Δ=+0; baseline 710-714: parent 710..714 → child 710..714; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1003 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:49 | src/write_output.F:548-557,716-720 | X | baseline 548-557: parent 548..557 → child 548..557; Δ=+0; baseline 716-720: parent 716..720 → child 716..720; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1008 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:54 | src/write_output.F:735-748,775-792 | X | baseline 735-748: parent 735..748 → child 735..748; Δ=+0; baseline 775-792: parent 775..792 → child 775..792; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1010 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:55 | src/write_output.F:817-823,906-913 | X | baseline 817-823: parent 817..823 → child 817..823; Δ=+0; baseline 906-913: parent 906..913 → child 906..913; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1014 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:57 | src/write_output.F:760-762,804-806,828-830,920-922 | X | baseline 760-762: parent 760..762 → child 760..762; Δ=+0; baseline 804-806: parent 804..806 → child 804..806; Δ=+0; baseline 828-830: parent 828..830 → child 828..830; Δ=+0; baseline 920-922: parent 920..922 → child 920..922; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1022 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:67 | src/write_output.F:2673 | X | baseline 2673-2673: parent 2673..2673 → child 2673..2673; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1024 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:68 | src/write_output.F:2701-2750 | X | baseline 2701-2750: parent 2701..2750 → child 2701..2750; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1025 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:69 | src/write_output.F:2752-2760 | X | baseline 2752-2760: parent 2752..2760 → child 2752..2760; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1034 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:76 | src/write_output.F:2787-2843 | X | baseline 2787-2843: parent 2787..2843 → child 2787..2843; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1036 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:77 | src/write_output.F:2980-3103 | N | baseline 2980-3103: parent 2980..3103 → child 2981..3104; Δ=+1; 인용 변경/좌표 이동 |
| 1038 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:79 | src/write_output.F:3403-3416,3584-3591,3623-3630 | N | baseline 3403-3416: parent 3403..3416 → child 3404..3417; Δ=+1; baseline 3584-3591: parent 3584..3591 → child 3585..3592; Δ=+1; baseline 3623-3630: parent 3623..3630 → child 3624..3631; Δ=+1; 인용 변경/좌표 이동 |
| 1041 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:84 | src/write_output.F:6343-6374 | N | baseline 6343-6374: parent 6343..6374 → child 6373..6404; Δ=+30; 인용 변경/좌표 이동 |
| 1044 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:85 | src/write_output.F:1205-1237,1239-1268 | X | baseline 1205-1237: parent 1205..1237 → child 1205..1237; Δ=+0; baseline 1239-1268: parent 1239..1268 → child 1239..1268; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1045 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:86 | src/write_output.F:1890-1898 | X | baseline 1890-1898: parent 1890..1898 → child 1890..1898; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1047 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:92 | src/write_output.F:4226-4271 | N | baseline 4226-4271: parent 4226..4271 → child 4256..4301; Δ=+30; 인용 변경/좌표 이동 |
| 1048 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:95 | src/write_output.F:1611-1615 | X | baseline 1611-1615: parent 1611..1615 → child 1611..1615; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1050 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:97 | src/write_output.F:1572-1580,1691-1693 | X | baseline 1572-1580: parent 1572..1580 → child 1572..1580; Δ=+0; baseline 1691-1693: parent 1691..1693 → child 1691..1693; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1051 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:97 | src/write_output.F:1572-1580,1691-1693 | X | baseline 1572-1580: parent 1572..1580 → child 1572..1580; Δ=+0; baseline 1691-1693: parent 1691..1693 → child 1691..1693; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1085 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:155 | src/write_output.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1181 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:116 | src/write_output.F:1205-1260 | X | baseline 1205-1260: parent 1205..1260 → child 1205..1260; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1182 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:117 | src/write_output.F:4322-4324 | N | baseline 4322-4324: parent 4322..4324 → child 4352..4354; Δ=+30; 인용 변경/좌표 이동 |
| 1190 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:136 | src/write_output.F:4246-4250 | N | baseline 4246-4250: parent 4246..4250 → child 4276..4280; Δ=+30; 인용 변경/좌표 이동 |
| 1251 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:25 | write_output.F:4969-5112 | N | baseline 4969-5112: parent 4969..5112 → child 4999..5142; Δ=+30; 인용 변경/좌표 이동 |
| 1294 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:133 | write_output.F:4969-5112 | N | baseline 4969-5112: parent 4969..5112 → child 4999..5142; Δ=+30; 인용 변경/좌표 이동 |

### 참조 원장 f7e98050e025 · src/vsmy.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 130 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:26 | vsmy.F:1168,1543-3871,4061-4315 | N | baseline 1168-1168: parent 1168..1168 → child 1168..1168; Δ=+0; baseline 1543-3871: parent 1545..3873 → child 1545..3878 [?]; Δ=+0/+1/+5; changed/replaced; 삭제/치환점 정확한 대응 불명; baseline 4061-4315: parent 4076..4330 → child 4081..4335; Δ=+5; 인용 변경/좌표 이동 |
| 141 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:60 | vsmy.F:1548-1553 | X | baseline 1548-1553: parent 1550..1555 → child 1550..1555; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 145 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:68 | vsmy.F:1630 | X | baseline 1630-1630: parent 1632..1632 → child 1632..1632; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 149 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:74 | vsmy.F:4061 | N | baseline 4061-4061: parent 4076..4076 → child 4081..4081; Δ=+5; 인용 변경/좌표 이동 |
| 156 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:94 | vsmy.F:1168 | X | baseline 1168-1168: parent 1168..1168 → child 1168..1168; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 164 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:121 | vsmy.F:1823,1840,1870,1931,1983 | X | baseline 1823-1823: parent 1825..1825 → child 1825..1825; Δ=+0; baseline 1840-1840: parent 1842..1842 → child 1842..1842; Δ=+0; baseline 1870-1870: parent 1872..1872 → child 1872..1872; Δ=+0; baseline 1931-1931: parent 1933..1933 → child 1933..1933; Δ=+0; baseline 1983-1983: parent 1985..1985 → child 1985..1985; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 165 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:122 | vsmy.F:2035,2403 | X | baseline 2035-2035: parent 2037..2037 → child 2037..2037; Δ=+0; baseline 2403-2403: parent 2405..2405 → child 2405..2405; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 166 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:127 | vsmy.F:2740 | X | baseline 2740-2740: parent 2742..2742 → child 2742..2742; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 181 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:2 | vsmy.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 182 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:7 | vsmy.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 188 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:23 | vsmy.F:142-1703 | P | baseline 142-1703: parent 142..1705 [?] → child 142..1705 [?]; Δ=+0; 삭제/치환점 정확한 대응 불명; 파일만 인용 또는 치환점 대응 불명 |
| 200 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:43 | vsmy.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 208 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:53 | vsmy.F:2299-2319 | X | baseline 2299-2319: parent 2301..2321 → child 2301..2321; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 244 | models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:61 | vsmy.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 683 | models/ADCIRC/source-analysis/adcirc-hotstart.md:23 | vsmy.F:3254,3531-3778 | N | baseline 3254-3254: parent 3256..3256 → child 3261..3261; Δ=+5; baseline 3531-3778: parent 3533..3780 → child 3538..3785; Δ=+5; 인용 변경/좌표 이동 |
| 706 | models/ADCIRC/source-analysis/adcirc-hotstart.md:86 | vsmy.F:3254 | N | baseline 3254-3254: parent 3256..3256 → child 3261..3261; Δ=+5; 인용 변경/좌표 이동 |
| 719 | models/ADCIRC/source-analysis/adcirc-hotstart.md:127 | vsmy.F:3531-3778 | N | baseline 3531-3778: parent 3533..3780 → child 3538..3785; Δ=+5; 인용 변경/좌표 이동 |
| 909 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:19 | vsmy.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 936 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:75 | vsmy.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 937 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:80 | vsmy.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1465 | models/ADCIRC/source-analysis/adcirc-transport-solver.md:6 | vsmy.F:1543,1548-1553 | X | baseline 1543-1543: parent 1545..1545 → child 1545..1545; Δ=+0; baseline 1548-1553: parent 1550..1555 → child 1550..1555; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1466 | models/ADCIRC/source-analysis/adcirc-transport-solver.md:6 | vsmy.F:1543,1548-1553 | X | baseline 1543-1543: parent 1545..1545 → child 1545..1545; Δ=+0; baseline 1548-1553: parent 1550..1555 → child 1550..1555; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1472 | models/ADCIRC/source-analysis/adcirc-transport-solver.md:20 | vsmy.F:1548-1553 | X | baseline 1548-1553: parent 1550..1555 → child 1550..1555; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1473 | models/ADCIRC/source-analysis/adcirc-transport-solver.md:21 | vsmy.F:1543 | X | baseline 1543-1543: parent 1545..1545 → child 1545..1545; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1474 | models/ADCIRC/source-analysis/adcirc-transport-solver.md:21 | vsmy.F:1543 | X | baseline 1543-1543: parent 1545..1545 → child 1545..1545; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1486 | models/ADCIRC/source-analysis/adcirc-transport-solver.md:59 | vsmy.F:1548-1553 | X | baseline 1548-1553: parent 1550..1555 → child 1550..1555; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1487 | models/ADCIRC/source-analysis/adcirc-transport-solver.md:62 | vsmy.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1490 | models/ADCIRC/source-analysis/adcirc-transport-solver.md:68 | vsmy.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |

### 참조 원장 bf6957a976d9 · src/nodalattr.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 361 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51 | src/nodalattr.F:1141,1154 | X | baseline 1141-1141: parent 1141..1141 → child 1141..1141; Δ=+0; baseline 1154-1154: parent 1154..1154 → child 1154..1154; Δ=+0; 범위 제외 규칙 |
| 362 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51 | src/nodalattr.F:1141,1154 | X | baseline 1141-1141: parent 1141..1141 → child 1141..1141; Δ=+0; baseline 1154-1154: parent 1154..1154 → child 1154..1154; Δ=+0; 범위 제외 규칙 |
| 489 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:160 | src/nodalattr.F:1051 | X | baseline 1051-1051: parent 1051..1051 → child 1051..1051; Δ=+0; 범위 제외 규칙 |
| 495 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:175 | src/nodalattr.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 931 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:68 | nodalattr.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 961 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:6 | models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 962 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:19 | src/nodalattr.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 965 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:21 | nodalattr.F:636-686 | X | baseline 636-686: parent 636..686 → child 636..686; Δ=+0; 범위 제외 규칙 |
| 983 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:73 | nodalattr.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 1218 | models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:39 | src/nodalattr.F:1051 | X | baseline 1051-1051: parent 1051..1051 → child 1051..1051; Δ=+0; 범위 제외 규칙 |
| 1375 | models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:56 | nodalattr.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |

### 참조 원장 bf6957a976d9 · src/timestep.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 128 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:24 | timestep.F:1121,1125,1918,2150-2355 | X | baseline 1121-1121: parent 1121..1121 → child 1125..1125; Δ=+4; baseline 1125-1125: parent 1125..1125 → child 1129..1129; Δ=+4; baseline 1918-1918: parent 1918..1918 → child 1922..1922; Δ=+4; baseline 2150-2355: parent 2150..2355 → child 2154..2359; Δ=+4; 범위 제외 규칙 |
| 150 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:84 | timestep.F:1121 | X | baseline 1121-1121: parent 1121..1121 → child 1125..1125; Δ=+4; 범위 제외 규칙 |
| 151 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:88 | timestep.F:1125 | X | baseline 1125-1125: parent 1125..1125 → child 1129..1129; Δ=+4; 범위 제외 규칙 |
| 159 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:112 | timestep.F:2150-2355 | X | baseline 2150-2355: parent 2150..2355 → child 2154..2359; Δ=+4; 범위 제외 규칙 |
| 185 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:7 | timestep.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 189 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:23 | timestep.F:1121-1123 | X | baseline 1121-1123: parent 1121..1123 → child 1125..1127; Δ=+4; 범위 제외 규칙 |
| 190 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:23 | timestep.F:1121-1123 | X | baseline 1121-1123: parent 1121..1123 → child 1125..1127; Δ=+4; 범위 제외 규칙 |
| 300 | models/ADCIRC/source-analysis/adcirc-dg-continuity-solver.md:60 | src/timestep.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 321 | models/ADCIRC/source-analysis/adcirc-dg-continuity-solver.md:268 | timestep.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 685 | models/ADCIRC/source-analysis/adcirc-hotstart.md:25 | timestep.F:1192-1211 | X | baseline 1192-1211: parent 1192..1211 → child 1196..1215; Δ=+4; 범위 제외 규칙 |
| 713 | models/ADCIRC/source-analysis/adcirc-hotstart.md:116 | timestep.F:1192-1197 | X | baseline 1192-1197: parent 1192..1197 → child 1196..1201; Δ=+4; 범위 제외 규칙 |
| 905 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:6 | timestep.F:129 | X | baseline 129-129: parent 129..129 → child 129..129; Δ=+0; 범위 제외 규칙 |
| 923 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:66 | timestep.F:129 | X | baseline 129-129: parent 129..129 → child 129..129; Δ=+0; 범위 제외 규칙 |
| 934 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:69 | timestep.F:1634 | X | baseline 1634-1634: parent 1634..1634 → child 1638..1638; Δ=+4; 범위 제외 규칙 |
| 939 | models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:7 | timestep.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 950 | models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:40 | timestep.F:860-880 | X | baseline 860-880: parent 860..880 → child 864..884; Δ=+4; 범위 제외 규칙 |
| 1017 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:63 | src/timestep.F:1184 | X | baseline 1184-1184: parent 1184..1184 → child 1188..1188; Δ=+4; 범위 제외 규칙 |
| 1039 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:83 | src/timestep.F:1162 | X | baseline 1162-1162: parent 1162..1162 → child 1166..1166; Δ=+4; 범위 제외 규칙 |
| 1087 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:157 | src/timestep.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 1249 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:24 | timestep.F:664-682,695-725,1214-1218 | X | baseline 664-682: parent 664..682 → child 668..686; Δ=+4; baseline 695-725: parent 695..725 → child 699..729; Δ=+4; baseline 1214-1218: parent 1214..1218 → child 1218..1222; Δ=+4; 범위 제외 규칙 |
| 1271 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:62 | timestep.F:695-703 | X | baseline 695-703: parent 695..703 → child 699..707; Δ=+4; 범위 제외 규칙 |
| 1272 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:63 | timestep.F:721-725 | X | baseline 721-725: parent 721..725 → child 725..729; Δ=+4; 범위 제외 규칙 |
| 1280 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:77 | timestep.F:664-682 | X | baseline 664-682: parent 664..682 → child 668..686; Δ=+4; 범위 제외 규칙 |
| 1298 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:139 | timestep.F:1214-1218 | X | baseline 1214-1218: parent 1214..1218 → child 1218..1222; Δ=+4; 범위 제외 규칙 |
| 1341 | models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:7 | models/ADCIRC/raw/source_code/adcirc/src/timestep.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 1347 | models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:20 | timestep.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 1351 | models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:22 | timestep.F:1527-1556 | X | baseline 1527-1556: parent 1527..1556 → child 1531..1560; Δ=+4; 범위 제외 규칙 |
| 1361 | models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:36 | timestep.F:1133 | X | baseline 1133-1133: parent 1133..1133 → child 1137..1137; Δ=+4; 범위 제외 규칙 |
| 1363 | models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:45 | timestep.F:1527 | X | baseline 1527-1527: parent 1527..1527 → child 1531..1531; Δ=+4; 범위 제외 규칙 |
| 1366 | models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:49 | timestep.F:162 | X | baseline 162-162: parent 162..162 → child 162..162; Δ=+0; 범위 제외 규칙 |
| 1372 | models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:51 | timestep.F:1543-1547 | X | baseline 1543-1547: parent 1543..1547 → child 1547..1551; Δ=+4; 범위 제외 규칙 |
| 1384 | models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:2 | timestep.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 1385 | models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:7 | models/ADCIRC/raw/source_code/adcirc/src/timestep.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 1388 | models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:19 | timestep.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 1389 | models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:21 | timestep.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 1392 | models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:23 | timestep.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 1982 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:43 | src/timestep.F:1517-1560 | X | baseline 1517-1560: parent 1517..1560 → child 1521..1564; Δ=+4; 범위 제외 규칙 |
| 2007 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:106 | src/timestep.F:1547-1555 | X | baseline 1547-1555: parent 1547..1555 → child 1551..1559; Δ=+4; 범위 제외 규칙 |
| 2008 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:110 | src/timestep.F:1507-1562 | X | baseline 1507-1562: parent 1507..1562 → child 1511..1566; Δ=+4; 범위 제외 규칙 |
| 2019 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:123 | src/timestep.F:1501-1503,1536 | X | baseline 1501-1503: parent 1501..1503 → child 1505..1507; Δ=+4; baseline 1536-1536: parent 1536..1536 → child 1540..1540; Δ=+4; 범위 제외 규칙 |
| 2025 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:137 | src/timestep.F:1541-1555 | X | baseline 1541-1555: parent 1541..1555 → child 1545..1559; Δ=+4; 범위 제외 규칙 |
| 2038 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:144 | src/timestep.F:251-259 | X | baseline 251-259: parent 251..259 → child 251..259; Δ=+0; 범위 제외 규칙 |
| 2045 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:163 | src/timestep.F:1517-1556,1520-1521 | X | baseline 1517-1556: parent 1517..1556 → child 1521..1560; Δ=+4; baseline 1520-1521: parent 1520..1521 → child 1524..1525; Δ=+4; 범위 제외 규칙 |
| 2047 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:163 | src/timestep.F:1517-1556,1520-1521 | X | baseline 1517-1556: parent 1517..1556 → child 1521..1560; Δ=+4; baseline 1520-1521: parent 1520..1521 → child 1524..1525; Δ=+4; 범위 제외 규칙 |
| 2057 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:176 | src/timestep.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 2087 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:128 | src/timestep.F:257-258,301-308 | X | baseline 257-258: parent 257..258 → child 257..258; Δ=+0; baseline 301-308: parent 301..308 → child 301..308; Δ=+0; 범위 제외 규칙 |
| 2105 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:167 | src/timestep.F:1543-1555 | X | baseline 1543-1555: parent 1543..1555 → child 1547..1559; Δ=+4; 범위 제외 규칙 |
| 2122 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:222 | timestep.F:251-258,1517-1562 | X | baseline 251-258: parent 251..258 → child 251..258; Δ=+0; baseline 1517-1562: parent 1517..1562 → child 1521..1566; Δ=+4; 범위 제외 규칙 |
| 2156 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:310 | timestep.F:1547-1548 | X | baseline 1547-1548: parent 1547..1548 → child 1551..1552; Δ=+4; 범위 제외 규칙 |
| 2164 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:333 | timestep.F:251-258 | X | baseline 251-258: parent 251..258 → child 251..258; Δ=+0; 범위 제외 규칙 |
| 2166 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:335 | src/timestep.F:257-258 | X | baseline 257-258: parent 257..258 → child 257..258; Δ=+0; 범위 제외 규칙 |
| 2174 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:337 | timestep.F:1532-1535 | X | baseline 1532-1535: parent 1532..1535 → child 1536..1539; Δ=+4; 범위 제외 규칙 |
| 2176 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:339 | src/timestep.F:257-258 | X | baseline 257-258: parent 257..258 → child 257..258; Δ=+0; 범위 제외 규칙 |

### 참조 원장 8a80ef218a6c · src/cstart.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 126 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:23 | cstart.F:348 | X | baseline 348-348: parent 348..348 → child 348..348; Δ=+0; 범위 제외 규칙 |
| 134 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:36 | cstart.F:348 | X | baseline 348-348: parent 348..348 → child 348..348; Δ=+0; 범위 제외 규칙 |
| 371 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:53 | src/cstart.F:313 | X | baseline 313-313: parent 313..313 → child 313..313; Δ=+0; 범위 제외 규칙 |
| 383 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:63 | src/cstart.F:376 | X | baseline 376-376: parent 376..376 → child 376..376; Δ=+0; 범위 제외 규칙 |
| 389 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:64 | src/cstart.F:394 | X | baseline 394-394: parent 394..394 → child 394..394; Δ=+0; 범위 제외 규칙 |
| 393 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:65 | src/cstart.F:487 | X | baseline 487-487: parent 487..487 → child 487..487; Δ=+0; 범위 제외 규칙 |
| 396 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:66 | src/cstart.F:584 | X | baseline 584-584: parent 584..584 → child 584..584; Δ=+0; 범위 제외 규칙 |
| 399 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:67 | src/cstart.F:467 | X | baseline 467-467: parent 467..467 → child 467..467; Δ=+0; 범위 제외 규칙 |
| 402 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:68 | src/cstart.F:412 | X | baseline 412-412: parent 412..412 → child 412..412; Δ=+0; 범위 제외 규칙 |
| 405 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:69 | src/cstart.F:665 | X | baseline 665-665: parent 665..665 → child 665..665; Δ=+0; 범위 제외 규칙 |
| 408 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:70 | src/cstart.F:501 | X | baseline 501-501: parent 501..501 → child 501..501; Δ=+0; 범위 제외 규칙 |
| 412 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:71 | src/cstart.F:492 | X | baseline 492-492: parent 492..492 → child 492..492; Δ=+0; 범위 제외 규칙 |
| 475 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:145 | cstart.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 502 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:180 | src/cstart.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 629 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:57 | src/cstart.F:64 | X | baseline 64-64: parent 64..64 → child 64..64; Δ=+0; 범위 제외 규칙 |
| 638 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:60 | src/cstart.F:1221-1223,1258-1260 | X | baseline 1221-1223: parent 1226..1228 → child 1224..1226; Δ=-2; baseline 1258-1260: parent 1263..1265 → child 1261..1263; Δ=-2; 범위 제외 규칙 |
| 649 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:74 | src/cstart.F:1221-1231,1258-1268 | X | baseline 1221-1231: parent 1226..1236 → child 1224..1234; Δ=-2; baseline 1258-1268: parent 1263..1273 → child 1261..1271; Δ=-2; 범위 제외 규칙 |
| 670 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:105 | src/cstart.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 2061 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:178 | src/cstart.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |

### 참조 원장 8a80ef218a6c · src/hstart.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 179 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:194 | hstart.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 476 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:145 | hstart.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 477 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:145 | hstart.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 503 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:180 | src/hstart.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 603 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:37 | src/hstart.F:719-720 | X | baseline 719-720: parent 725..725 [?] → child 725..725 [?]; Δ=+0; 삭제/치환점 정확한 대응 불명; 범위 제외 규칙 |
| 630 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:57 | src/hstart.F:58 | X | baseline 58-58: parent 58..58 → child 58..58; Δ=+0; 범위 제외 규칙 |
| 642 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:65 | src/hstart.F:1522,1530-1532 | X | baseline 1522-1522: parent 1527..1527 → child 1527..1527; Δ=+0; baseline 1530-1532: parent 1535..1537 → child 1535..1537; Δ=+0; 범위 제외 규칙 |
| 671 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:105 | src/hstart.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 680 | models/ADCIRC/source-analysis/adcirc-hotstart.md:21 | hstart.F:47-3048 | X | baseline 47-3048: parent 47..3090 [?] → child 47..3076 [?]; Δ=-14/-3/-1/+0; 삭제/치환점 정확한 대응 불명; 범위 제외 규칙 |
| 691 | models/ADCIRC/source-analysis/adcirc-hotstart.md:35 | hstart.F:242-253 | X | baseline 242-253: parent 242..253 → child 242..253; Δ=+0; 범위 제외 규칙 |
| 692 | models/ADCIRC/source-analysis/adcirc-hotstart.md:36 | hstart.F:452-465 | X | baseline 452-465: parent 452..465 → child 452..465; Δ=+0; 범위 제외 규칙 |
| 693 | models/ADCIRC/source-analysis/adcirc-hotstart.md:38 | hstart.F:673-690 | X | baseline 673-690: parent 673..690 → child 673..690; Δ=+0; 범위 제외 규칙 |
| 695 | models/ADCIRC/source-analysis/adcirc-hotstart.md:45 | hstart.F:485-492 | X | baseline 485-492: parent 485..492 → child 485..492; Δ=+0; 범위 제외 규칙 |
| 698 | models/ADCIRC/source-analysis/adcirc-hotstart.md:70 | hstart.F:506-668 | X | baseline 506-668: parent 506..668 → child 506..668; Δ=+0; 범위 제외 규칙 |
| 699 | models/ADCIRC/source-analysis/adcirc-hotstart.md:72 | hstart.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 700 | models/ADCIRC/source-analysis/adcirc-hotstart.md:76 | hstart.F:47 | X | baseline 47-47: parent 47..47 → child 47..47; Δ=+0; 범위 제외 규칙 |
| 702 | models/ADCIRC/source-analysis/adcirc-hotstart.md:83 | hstart.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 715 | models/ADCIRC/source-analysis/adcirc-hotstart.md:122 | hstart.F:526-536 | X | baseline 526-536: parent 526..536 → child 526..536; Δ=+0; 범위 제외 규칙 |
| 717 | models/ADCIRC/source-analysis/adcirc-hotstart.md:123 | hstart.F:529-533 | X | baseline 529-533: parent 529..533 → child 529..533; Δ=+0; 범위 제외 규칙 |
| 722 | models/ADCIRC/source-analysis/adcirc-hotstart.md:130 | hstart.F:1440-1444 | X | baseline 1440-1444: parent 1445..1449 → child 1445..1449; Δ=+0; 범위 제외 규칙 |
| 725 | models/ADCIRC/source-analysis/adcirc-hotstart.md:144 | hstart.F:1442-1444 | X | baseline 1442-1444: parent 1447..1449 → child 1447..1449; Δ=+0; 범위 제외 규칙 |
| 1250 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:25 | hstart.F:325-337 | X | baseline 325-337: parent 325..337 → child 325..337; Δ=+0; 범위 제외 규칙 |
| 1293 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:129 | hstart.F:325-337 | X | baseline 325-337: parent 325..337 → child 325..337; Δ=+0; 범위 제외 규칙 |
| 2006 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:106 | src/hstart.F:1529-1532 | X | baseline 1529-1532: parent 1534..1537 → child 1534..1537; Δ=+0; 범위 제외 규칙 |
| 2026 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:137 | src/hstart.F:1525-1532 | X | baseline 1525-1532: parent 1530..1537 → child 1530..1537; Δ=+0; 범위 제외 규칙 |
| 2060 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:178 | src/hstart.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 2124 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:223 | hstart.F:1525-1532 | X | baseline 1525-1532: parent 1530..1537 → child 1530..1537; Δ=+0; 범위 제외 규칙 |
| 2157 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:310 | hstart.F:1525-1532 | X | baseline 1525-1532: parent 1530..1537 → child 1530..1537; Δ=+0; 범위 제외 규칙 |

### 참조 원장 8a80ef218a6c · src/netcdfio.F90

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 684 | models/ADCIRC/source-analysis/adcirc-hotstart.md:24 | netcdfio.F90:3866-9188 | X | baseline 3866-9188: parent 3890..9237 [?] → child 3866..9188 [?]; Δ=-49/-47/-45/-43/-41/-39/-37/-35/-33/-32/-30/-28/-26/-24; 삭제/치환점 정확한 대응 불명; 범위 제외 규칙 |
| 707 | models/ADCIRC/source-analysis/adcirc-hotstart.md:90 | netcdfio.F90:3866-3871 | X | baseline 3866-3871: parent 3890..3895 → child 3866..3871; Δ=-24; 범위 제외 규칙 |
| 718 | models/ADCIRC/source-analysis/adcirc-hotstart.md:123 | netcdfio.F90:5357-5380 | X | baseline 5357-5380: parent 5390..5413 → child 5357..5380; Δ=-33; 범위 제외 규칙 |
| 724 | models/ADCIRC/source-analysis/adcirc-hotstart.md:138 | netcdfio.F90:8109-8158 | X | baseline 8109-8158: parent 8158..8207 → child 8109..8158; Δ=-49; 범위 제외 규칙 |
| 744 | models/ADCIRC/source-analysis/adcirc-hotstart.md:188 | netcdfio.F90:8017-8085 | X | baseline 8017-8085: parent 8066..8134 → child 8017..8085; Δ=-49; 범위 제외 규칙 |
| 1252 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:25 | netcdfio.F90:5555-7045,8017-8085 | X | baseline 5555-7045: parent 5588..7092 [?] → child 5555..7045 [?]; Δ=-47/-45/-43/-41/-39/-37/-35/-33; 삭제/치환점 정확한 대응 불명; baseline 8017-8085: parent 8066..8134 → child 8017..8085; Δ=-49; 범위 제외 규칙 |
| 1295 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:135 | netcdfio.F90:5555-5568 | X | baseline 5555-5568: parent 5588..5601 → child 5555..5568; Δ=-33; 범위 제외 규칙 |
| 1301 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:142 | netcdfio.F90:8017-8085 | X | baseline 8017-8085: parent 8066..8134 → child 8017..8085; Δ=-49; 범위 제외 규칙 |
| 1316 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:174 | netcdfio.F90:8017-8085 | X | baseline 8017-8085: parent 8066..8134 → child 8017..8085; Δ=-49; 범위 제외 규칙 |

### 참조 원장 e5995720925d · prep/prep.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 295 | models/ADCIRC/source-analysis/adcirc-dg-continuity-solver.md:55 | prep/prep.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 471 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:109 | prep/prep.F:7439 | N | baseline 7439-7439: parent 7439..7439 → child 7468..7468; Δ=+29; 인용 변경/좌표 이동 |
| 509 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:182 | prep/prep.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1112 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:39 | prep/prep.F:1276 | X | baseline 1276-1276: parent 1276..1276 → child 1276..1276; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1113 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:40 | prep/prep.F:1818 | X | baseline 1818-1818: parent 1818..1818 → child 1818..1818; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1114 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:41 | prep/prep.F:1162 | X | baseline 1162-1162: parent 1162..1162 → child 1162..1162; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1118 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:49 | prep/prep.F:7432,7444-7463 | N | baseline 7432-7432: parent 7432..7432 → child 7461..7461; Δ=+29; baseline 7444-7463: parent 7444..7463 → child 7473..7492; Δ=+29; 인용 변경/좌표 이동 |
| 1119 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:49 | prep/prep.F:7432,7444-7463 | N | baseline 7432-7432: parent 7432..7432 → child 7461..7461; Δ=+29; baseline 7444-7463: parent 7444..7463 → child 7473..7492; Δ=+29; 인용 변경/좌표 이동 |
| 1134 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:60 | prep/prep.F:7465-7469 | N | baseline 7465-7469: parent 7465..7469 → child 7494..7498; Δ=+29; 인용 변경/좌표 이동 |
| 1136 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:61 | prep/prep.F:7471-7474 | N | baseline 7471-7474: parent 7471..7474 → child 7500..7503; Δ=+29; 인용 변경/좌표 이동 |
| 1137 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:65 | prep/prep.F:7479-7482 | N | baseline 7479-7482: parent 7479..7482 → child 7508..7511; Δ=+29; 인용 변경/좌표 이동 |
| 1139 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:70 | prep/prep.F:2850-2905 | X | baseline 2850-2905: parent 2850..2905 → child 2850..2905; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1204 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:177 | prep/prep.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1239 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:6 | prep.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1323 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:200 | prep/prep.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |

### 참조 원장 bdc531653bef · src/global.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 305 | models/ADCIRC/source-analysis/adcirc-dg-continuity-solver.md:65 | src/global.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1212 | models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:7 | global.F:86-91 | X | baseline 86-91: parent 86..91 → child 86..91; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1216 | models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:25 | src/global.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1225 | models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:61 | global.F:86 | X | baseline 86-86: parent 86..86 → child 86..86; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1227 | models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:64 | global.F:91 | X | baseline 91-91: parent 91..91 → child 91..91; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1990 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:50 | src/global.F:387,1045 | N | baseline 387-387: parent 387..387 → child 393..393; Δ=+6; baseline 1045-1045: parent 1045..1045 → child 1051..1051; Δ=+6; 인용 변경/좌표 이동 |

### 참조 원장 bdc531653bef · src/write_output.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 132 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:28 | write_output.F:2993-3331 | N | baseline 2993-3331: parent 2994..3332 → child 3053..3391; Δ=+59; 인용 변경/좌표 이동 |
| 169 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:135 | write_output.F:2993 | N | baseline 2993-2993: parent 2994..2994 → child 3053..3053; Δ=+59; 인용 변경/좌표 이동 |
| 171 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:144 | write_output.F:3331 | N | baseline 3331-3331: parent 3332..3332 → child 3391..3391; Δ=+59; 인용 변경/좌표 이동 |
| 306 | models/ADCIRC/source-analysis/adcirc-dg-continuity-solver.md:66 | src/write_output.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 382 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:63 | src/write_output.F:510 | N | baseline 510-510: parent 510..510 → child 511..511; Δ=+1; 인용 변경/좌표 이동 |
| 388 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:64 | src/write_output.F:546 | N | baseline 546-546: parent 546..546 → child 547..547; Δ=+1; 인용 변경/좌표 이동 |
| 392 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:65 | src/write_output.F:598 | N | baseline 598-598: parent 598..598 → child 614..614; Δ=+16; 인용 변경/좌표 이동 |
| 395 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:66 | src/write_output.F:710 | N | baseline 710-710: parent 710..710 → child 726..726; Δ=+16; 인용 변경/좌표 이동 |
| 398 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:67 | src/write_output.F:946 | N | baseline 946-946: parent 946..946 → child 968..968; Δ=+22; 인용 변경/좌표 이동 |
| 401 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:68 | src/write_output.F:1160 | N | baseline 1160-1160: parent 1160..1160 → child 1182..1182; Δ=+22; 인용 변경/좌표 이동 |
| 404 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:69 | src/write_output.F:1191 | N | baseline 1191-1191: parent 1191..1191 → child 1213..1213; Δ=+22; 인용 변경/좌표 이동 |
| 407 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:70 | src/write_output.F:619 | N | baseline 619-619: parent 619..619 → child 635..635; Δ=+16; 인용 변경/좌표 이동 |
| 411 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:71 | src/write_output.F:641 | N | baseline 641-641: parent 641..641 → child 657..657; Δ=+16; 인용 변경/좌표 이동 |
| 413 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:79 | src/write_output.F:735 | N | baseline 735-735: parent 735..735 → child 757..757; Δ=+22; 인용 변경/좌표 이동 |
| 418 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:80 | src/write_output.F:775 | N | baseline 775-775: parent 775..775 → child 797..797; Δ=+22; 인용 변경/좌표 이동 |
| 422 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:81 | src/write_output.F:817 | N | baseline 817-817: parent 817..817 → child 839..839; Δ=+22; 인용 변경/좌표 이동 |
| 426 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:82 | src/write_output.F:904 | N | baseline 904-904: parent 904..904 → child 926..926; Δ=+22; 인용 변경/좌표 이동 |
| 430 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:83 | src/write_output.F:1064 | N | baseline 1064-1064: parent 1064..1064 → child 1086..1086; Δ=+22; 인용 변경/좌표 이동 |
| 433 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:84 | src/write_output.F:1039 | N | baseline 1039-1039: parent 1039..1039 → child 1061..1061; Δ=+22; 인용 변경/좌표 이동 |
| 436 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:90 | src/write_output.F:2993 | N | baseline 2993-2993: parent 2994..2994 → child 3053..3053; Δ=+59; 인용 변경/좌표 이동 |
| 443 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:91 | src/write_output.F:3059 | N | baseline 3059-3059: parent 3060..3060 → child 3119..3119; Δ=+59; 인용 변경/좌표 이동 |
| 453 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:99 | src/write_output.F:2178 | N | baseline 2178-2178: parent 2178..2178 → child 2237..2237; Δ=+59; 인용 변경/좌표 이동 |
| 459 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:100 | src/write_output.F:2232 | N | baseline 2232-2232: parent 2232..2232 → child 2291..2291; Δ=+59; 인용 변경/좌표 이동 |
| 463 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:101 | src/write_output.F:2339 | N | baseline 2339-2339: parent 2339..2339 → child 2398..2398; Δ=+59; 인용 변경/좌표 이동 |
| 504 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:181 | src/write_output.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 681 | models/ADCIRC/source-analysis/adcirc-hotstart.md:22 | write_output.F:4429,4920-5374 | N | baseline 4429-4429: parent 4459..4459 → child 4518..4518; Δ=+59; baseline 4920-5374: parent 4950..5404 → child 5009..5463; Δ=+59; 인용 변경/좌표 이동 |
| 696 | models/ADCIRC/source-analysis/adcirc-hotstart.md:45 | write_output.F:4920-4923 | N | baseline 4920-4923: parent 4950..4953 → child 5009..5012; Δ=+59; 인용 변경/좌표 이동 |
| 697 | models/ADCIRC/source-analysis/adcirc-hotstart.md:47 | write_output.F:4922-4931 | N | baseline 4922-4931: parent 4952..4961 → child 5011..5020; Δ=+59; 인용 변경/좌표 이동 |
| 703 | models/ADCIRC/source-analysis/adcirc-hotstart.md:84 | write_output.F:4429 | N | baseline 4429-4429: parent 4459..4459 → child 4518..4518; Δ=+59; 인용 변경/좌표 이동 |
| 716 | models/ADCIRC/source-analysis/adcirc-hotstart.md:122 | write_output.F:4935-4945 | N | baseline 4935-4945: parent 4965..4975 → child 5024..5034; Δ=+59; 인용 변경/좌표 이동 |
| 890 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:124 | write_output.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 986 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:21 | src/write_output.F:1773 | N | baseline 1773-1773: parent 1773..1773 → child 1819..1819; Δ=+46; 인용 변경/좌표 이동 |
| 988 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:22 | src/write_output.F:523,1811-1823 | N | baseline 523-523: parent 523..523 → child 524..524; Δ=+1; baseline 1811-1823: parent 1811..1823 → child 1860..1872; Δ=+49; 인용 변경/좌표 이동 |
| 990 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:23 | src/write_output.F:504-523,593-603 | N | baseline 504-523: parent 504..523 → child 505..524; Δ=+1; baseline 593-603: parent 593..603 → child 609..619; Δ=+16; 인용 변경/좌표 이동 |
| 996 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:32 | src/write_output.F:4226-4250 | N | baseline 4226-4250: parent 4256..4280 → child 4315..4339; Δ=+59; 인용 변경/좌표 이동 |
| 1001 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:42 | src/write_output.F:1568-1575,1691-1693 | N | baseline 1568-1575: parent 1568..1575 → child 1590..1597; Δ=+22; baseline 1691-1693: parent 1691..1693 → child 1713..1715; Δ=+22; 인용 변경/좌표 이동 |
| 1002 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:47 | src/write_output.F:537-563,710-714 | N | baseline 537-563: parent 537..563 → child 538..579 [?]; Δ=+1/+16; changed/replaced; 삭제/치환점 정확한 대응 불명; baseline 710-714: parent 710..714 → child 726..730; Δ=+16; 인용 변경/좌표 이동 |
| 1003 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:49 | src/write_output.F:548-557,716-720 | N | baseline 548-557: parent 548..557 → child 549..556 [?]; Δ=+1; changed/replaced; 삭제/치환점 정확한 대응 불명; baseline 716-720: parent 716..720 → child 732..742 [?]; Δ=+16/+22; changed/replaced; 삭제/치환점 정확한 대응 불명; 인용 변경/좌표 이동 |
| 1008 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:54 | src/write_output.F:735-748,775-792 | N | baseline 735-748: parent 735..748 → child 757..770; Δ=+22; baseline 775-792: parent 775..792 → child 797..814; Δ=+22; 인용 변경/좌표 이동 |
| 1010 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:55 | src/write_output.F:817-823,906-913 | N | baseline 817-823: parent 817..823 → child 839..845; Δ=+22; baseline 906-913: parent 906..913 → child 928..935; Δ=+22; 인용 변경/좌표 이동 |
| 1014 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:57 | src/write_output.F:760-762,804-806,828-830,920-922 | N | baseline 760-762: parent 760..762 → child 782..784; Δ=+22; baseline 804-806: parent 804..806 → child 826..828; Δ=+22; baseline 828-830: parent 828..830 → child 850..852; Δ=+22; baseline 920-922: parent 920..922 → child 942..944; Δ=+22; 인용 변경/좌표 이동 |
| 1022 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:67 | src/write_output.F:2673 | N | baseline 2673-2673: parent 2673..2673 → child 2732..2732; Δ=+59; 인용 변경/좌표 이동 |
| 1024 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:68 | src/write_output.F:2701-2750 | N | baseline 2701-2750: parent 2701..2750 → child 2760..2809; Δ=+59; 인용 변경/좌표 이동 |
| 1025 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:69 | src/write_output.F:2752-2760 | N | baseline 2752-2760: parent 2752..2760 → child 2811..2819; Δ=+59; 인용 변경/좌표 이동 |
| 1034 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:76 | src/write_output.F:2787-2843 | N | baseline 2787-2843: parent 2787..2843 → child 2846..2902; Δ=+59; 인용 변경/좌표 이동 |
| 1036 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:77 | src/write_output.F:2980-3103 | N | baseline 2980-3103: parent 2981..3104 → child 3040..3163; Δ=+59; 인용 변경/좌표 이동 |
| 1038 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:79 | src/write_output.F:3403-3416,3584-3591,3623-3630 | N | baseline 3403-3416: parent 3404..3417 → child 3463..3476; Δ=+59; baseline 3584-3591: parent 3585..3592 → child 3644..3651; Δ=+59; baseline 3623-3630: parent 3624..3631 → child 3683..3690; Δ=+59; 인용 변경/좌표 이동 |
| 1041 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:84 | src/write_output.F:6343-6374 | N | baseline 6343-6374: parent 6373..6404 → child 6432..6463; Δ=+59; 인용 변경/좌표 이동 |
| 1044 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:85 | src/write_output.F:1205-1237,1239-1268 | N | baseline 1205-1237: parent 1205..1237 → child 1227..1259; Δ=+22; baseline 1239-1268: parent 1239..1268 → child 1261..1290; Δ=+22; 인용 변경/좌표 이동 |
| 1045 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:86 | src/write_output.F:1890-1898 | N | baseline 1890-1898: parent 1890..1898 → child 1949..1957; Δ=+59; 인용 변경/좌표 이동 |
| 1047 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:92 | src/write_output.F:4226-4271 | N | baseline 4226-4271: parent 4256..4301 → child 4315..4360; Δ=+59; 인용 변경/좌표 이동 |
| 1048 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:95 | src/write_output.F:1611-1615 | N | baseline 1611-1615: parent 1611..1615 → child 1633..1637; Δ=+22; 인용 변경/좌표 이동 |
| 1050 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:97 | src/write_output.F:1572-1580,1691-1693 | N | baseline 1572-1580: parent 1572..1580 → child 1594..1602; Δ=+22; baseline 1691-1693: parent 1691..1693 → child 1713..1715; Δ=+22; 인용 변경/좌표 이동 |
| 1051 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:97 | src/write_output.F:1572-1580,1691-1693 | N | baseline 1572-1580: parent 1572..1580 → child 1594..1602; Δ=+22; baseline 1691-1693: parent 1691..1693 → child 1713..1715; Δ=+22; 인용 변경/좌표 이동 |
| 1085 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:155 | src/write_output.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1181 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:116 | src/write_output.F:1205-1260 | N | baseline 1205-1260: parent 1205..1260 → child 1227..1282; Δ=+22; 인용 변경/좌표 이동 |
| 1182 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:117 | src/write_output.F:4322-4324 | N | baseline 4322-4324: parent 4352..4354 → child 4411..4413; Δ=+59; 인용 변경/좌표 이동 |
| 1190 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:136 | src/write_output.F:4246-4250 | N | baseline 4246-4250: parent 4276..4280 → child 4335..4339; Δ=+59; 인용 변경/좌표 이동 |
| 1251 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:25 | write_output.F:4969-5112 | N | baseline 4969-5112: parent 4999..5142 → child 5058..5201; Δ=+59; 인용 변경/좌표 이동 |
| 1294 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:133 | write_output.F:4969-5112 | N | baseline 4969-5112: parent 4999..5142 → child 5058..5201; Δ=+59; 인용 변경/좌표 이동 |

### 참조 원장 daae7d9f9edc · src/nodalattr.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 361 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51 | src/nodalattr.F:1141,1154 | N | baseline 1141-1141: parent 1141..1141 → child 1144..1144; Δ=+3; baseline 1154-1154: parent 1154..1154 → child 1157..1157; Δ=+3; 인용 변경/좌표 이동 |
| 362 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51 | src/nodalattr.F:1141,1154 | N | baseline 1141-1141: parent 1141..1141 → child 1144..1144; Δ=+3; baseline 1154-1154: parent 1154..1154 → child 1157..1157; Δ=+3; 인용 변경/좌표 이동 |
| 489 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:160 | src/nodalattr.F:1051 | N | baseline 1051-1051: parent 1051..1051 → child 1054..1054; Δ=+3; 인용 변경/좌표 이동 |
| 495 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:175 | src/nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 931 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:68 | nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 961 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:6 | models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 962 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:19 | src/nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 965 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:21 | nodalattr.F:636-686 | X | baseline 636-686: parent 636..686 → child 636..686; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 983 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:73 | nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1218 | models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:39 | src/nodalattr.F:1051 | N | baseline 1051-1051: parent 1051..1051 → child 1054..1054; Δ=+3; 인용 변경/좌표 이동 |
| 1375 | models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:56 | nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |

### 참조 원장 976fc5b6cafb · prep/prep.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 295 | models/ADCIRC/source-analysis/adcirc-dg-continuity-solver.md:55 | prep/prep.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 471 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:109 | prep/prep.F:7439 | N | baseline 7439-7439: parent 7468..7468 → child 7472..7472; Δ=+4; 인용 변경/좌표 이동 |
| 509 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:182 | prep/prep.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1112 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:39 | prep/prep.F:1276 | X | baseline 1276-1276: parent 1276..1276 → child 1276..1276; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1113 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:40 | prep/prep.F:1818 | X | baseline 1818-1818: parent 1818..1818 → child 1818..1818; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1114 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:41 | prep/prep.F:1162 | X | baseline 1162-1162: parent 1162..1162 → child 1162..1162; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1118 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:49 | prep/prep.F:7432,7444-7463 | N | baseline 7432-7432: parent 7461..7461 → child 7465..7465; Δ=+4; baseline 7444-7463: parent 7473..7492 → child 7477..7496; Δ=+4; 인용 변경/좌표 이동 |
| 1119 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:49 | prep/prep.F:7432,7444-7463 | N | baseline 7432-7432: parent 7461..7461 → child 7465..7465; Δ=+4; baseline 7444-7463: parent 7473..7492 → child 7477..7496; Δ=+4; 인용 변경/좌표 이동 |
| 1134 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:60 | prep/prep.F:7465-7469 | N | baseline 7465-7469: parent 7494..7498 → child 7498..7502; Δ=+4; 인용 변경/좌표 이동 |
| 1136 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:61 | prep/prep.F:7471-7474 | N | baseline 7471-7474: parent 7500..7503 → child 7504..7507; Δ=+4; 인용 변경/좌표 이동 |
| 1137 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:65 | prep/prep.F:7479-7482 | N | baseline 7479-7482: parent 7508..7511 → child 7512..7515; Δ=+4; 인용 변경/좌표 이동 |
| 1139 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:70 | prep/prep.F:2850-2905 | N | baseline 2850-2905: parent 2850..2905 → child 2854..2909; Δ=+4; 인용 변경/좌표 이동 |
| 1204 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:177 | prep/prep.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1239 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:6 | prep.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1323 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:200 | prep/prep.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |

### 참조 원장 976fc5b6cafb · prep/presizes.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 297 | models/ADCIRC/source-analysis/adcirc-dg-continuity-solver.md:57 | prep/presizes.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1238 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:6 | presizes.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1322 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:199 | prep/presizes.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |

### 참조 원장 976fc5b6cafb · src/couple2swan.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 1240 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:6 | couple2swan.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1242 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:19 | couple2swan.F:67-1236 | N | baseline 67-1236: parent 67..1236 → child 67..1313 [?]; Δ=+0/+2/+4/+6/+18/+27/+29/+77; changed/replaced; 삭제/치환점 정확한 대응 불명; 인용 변경/좌표 이동 |
| 1255 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:34 | couple2swan.F:947 | X | baseline 947-947: parent 947..947 → child 947..947; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1265 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:51 | couple2swan.F:950,965 | N | baseline 950-950: parent 950..950 → child 950..950; Δ=+0; baseline 965-965: parent 965..965 → child 967..967; Δ=+2; 인용 변경/좌표 이동 |
| 1268 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:54 | couple2swan.F:1212-1215 | N | baseline 1212-1215: parent 1212..1215 → child 1241..1243 [?]; Δ=+29; changed/replaced; 삭제/치환점 정확한 대응 불명; 인용 변경/좌표 이동 |
| 1270 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:60 | couple2swan.F:112-119,177-196 | X | baseline 112-119: parent 112..119 → child 112..119; Δ=+0; baseline 177-196: parent 177..196 → child 177..196; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1273 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:67 | couple2swan.F:67-75,974-982 | N | baseline 67-75: parent 67..75 → child 67..75; Δ=+0; baseline 974-982: parent 974..982 → child 980..988; Δ=+6; 인용 변경/좌표 이동 |
| 1284 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:86 | couple2swan.F:596-598,800-835 | X | baseline 596-598: parent 596..598 → child 596..598; Δ=+0; baseline 800-835: parent 800..835 → child 800..835; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1309 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:162 | couple2swan.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1326 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:201 | src/couple2swan.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1332 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:204 | couple2swan.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |

### 참조 원장 976fc5b6cafb · src/global.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 305 | models/ADCIRC/source-analysis/adcirc-dg-continuity-solver.md:65 | src/global.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1212 | models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:7 | global.F:86-91 | X | baseline 86-91: parent 86..91 → child 86..91; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1216 | models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:25 | src/global.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1225 | models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:61 | global.F:86 | X | baseline 86-86: parent 86..86 → child 86..86; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1227 | models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:64 | global.F:91 | X | baseline 91-91: parent 91..91 → child 91..91; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 1990 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:50 | src/global.F:387,1045 | N | baseline 387-387: parent 393..393 → child 395..395; Δ=+2; baseline 1045-1045: parent 1051..1051 → child 1053..1053; Δ=+2; 인용 변경/좌표 이동 |

### 참조 원장 976fc5b6cafb · src/nodalattr.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 361 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51 | src/nodalattr.F:1141,1154 | N | baseline 1141-1141: parent 1144..1144 → child 1174..1174; Δ=+30; baseline 1154-1154: parent 1157..1157 → child 1187..1187; Δ=+30; 인용 변경/좌표 이동 |
| 362 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51 | src/nodalattr.F:1141,1154 | N | baseline 1141-1141: parent 1144..1144 → child 1174..1174; Δ=+30; baseline 1154-1154: parent 1157..1157 → child 1187..1187; Δ=+30; 인용 변경/좌표 이동 |
| 489 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:160 | src/nodalattr.F:1051 | N | baseline 1051-1051: parent 1054..1054 → child 1082..1082; Δ=+28; 인용 변경/좌표 이동 |
| 495 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:175 | src/nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 931 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:68 | nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 961 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:6 | models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 962 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:19 | src/nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 965 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:21 | nodalattr.F:636-686 | N | baseline 636-686: parent 636..686 → child 655..707; Δ=+19/+21; changed/replaced; 인용 변경/좌표 이동 |
| 983 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:73 | nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1218 | models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:39 | src/nodalattr.F:1051 | N | baseline 1051-1051: parent 1054..1054 → child 1082..1082; Δ=+28; 인용 변경/좌표 이동 |
| 1375 | models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:56 | nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |

### 참조 원장 976fc5b6cafb · src/read_input.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 123 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:20 | read_input.F:1176-1191,3072,5139-5482,5682 | N | baseline 1176-1191: parent 1176..1191 → child 1190..1205; Δ=+14; baseline 3072-3072: parent 3072..3072 → child 3086..3086; Δ=+14; baseline 5139-5482: parent 5139..5482 → child 5153..5496; Δ=+14; baseline 5682-5682: parent 5706..5706 → child 5720..5720; Δ=+14; 인용 변경/좌표 이동 |
| 135 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:37 | read_input.F:1176-1191 | N | baseline 1176-1191: parent 1176..1191 → child 1190..1205; Δ=+14; 인용 변경/좌표 이동 |
| 136 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:44 | read_input.F:5139 | N | baseline 5139-5139: parent 5139..5139 → child 5153..5153; Δ=+14; 인용 변경/좌표 이동 |
| 146 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:70 | read_input.F:5682 | N | baseline 5682-5682: parent 5706..5706 → child 5720..5720; Δ=+14; 인용 변경/좌표 이동 |
| 162 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:116 | read_input.F:5235 | N | baseline 5235-5235: parent 5235..5235 → child 5249..5249; Δ=+14; 인용 변경/좌표 이동 |
| 168 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:135 | read_input.F:5296 | N | baseline 5296-5296: parent 5296..5296 → child 5310..5310; Δ=+14; 인용 변경/좌표 이동 |
| 183 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:7 | read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 194 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:25 | read_input.F:5073 | N | baseline 5073-5073: parent 5073..5073 → child 5087..5087; Δ=+14; 인용 변경/좌표 이동 |
| 197 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:30 | read_input.F:5127 | N | baseline 5127-5127: parent 5127..5127 → child 5141..5141; Δ=+14; 인용 변경/좌표 이동 |
| 214 | models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:65 | read_input.F:5102 | N | baseline 5102-5102: parent 5102..5102 → child 5116..5116; Δ=+14; 인용 변경/좌표 이동 |
| 302 | models/ADCIRC/source-analysis/adcirc-dg-continuity-solver.md:62 | src/read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 327 | models/ADCIRC/source-analysis/adcirc-dg-continuity-solver.md:276 | read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 353 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:44 | src/read_input.F:380 | N | baseline 380-380: parent 380..380 → child 384..384; Δ=+4; 인용 변경/좌표 이동 |
| 357 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:45 | src/read_input.F:394,5296 | N | baseline 394-394: parent 394..394 → child 398..398; Δ=+4; baseline 5296-5296: parent 5296..5296 → child 5310..5310; Δ=+14; 인용 변경/좌표 이동 |
| 358 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:45 | src/read_input.F:394,5296 | N | baseline 394-394: parent 394..394 → child 398..398; Δ=+4; baseline 5296-5296: parent 5296..5296 → child 5310..5310; Δ=+14; 인용 변경/좌표 이동 |
| 373 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:54 | src/read_input.F:6425,6453 | N | baseline 6425-6425: parent 6449..6449 → child 6463..6463; Δ=+14; baseline 6453-6453: parent 6477..6477 → child 6491..6491; Δ=+14; 인용 변경/좌표 이동 |
| 374 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:54 | src/read_input.F:6425,6453 | N | baseline 6425-6425: parent 6449..6449 → child 6463..6463; Δ=+14; baseline 6453-6453: parent 6477..6477 → child 6491..6491; Δ=+14; 인용 변경/좌표 이동 |
| 492 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:174 | src/read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 522 | models/ADCIRC/source-analysis/adcirc-fort15-checklist-v1.md:7 | read_input.F:1133-1162 | N | baseline 1133-1162: parent 1133..1162 → child 1147..1176; Δ=+14; 인용 변경/좌표 이동 |
| 543 | models/ADCIRC/source-analysis/adcirc-fort15-checklist-v1.md:88 | models/ADCIRC/raw/source_code/adcirc/src/read_input.F:1133-1135 | N | baseline 1133-1135: parent 1133..1135 → child 1147..1149; Δ=+14; 인용 변경/좌표 이동 |
| 661 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:88 | read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 666 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:97 | read_input.F:3431-3456 | N | baseline 3431-3456: parent 3431..3456 → child 3445..3470; Δ=+14; 인용 변경/좌표 이동 |
| 675 | models/ADCIRC/source-analysis/adcirc-hotstart.md:19 | read_input.F:1050-1075,4504-4544 | N | baseline 1050-1075: parent 1050..1075 → child 1064..1089; Δ=+14; baseline 4504-4544: parent 4504..4544 → child 4518..4558; Δ=+14; 인용 변경/좌표 이동 |
| 687 | models/ADCIRC/source-analysis/adcirc-hotstart.md:30 | read_input.F:1050-1053 | N | baseline 1050-1053: parent 1050..1053 → child 1064..1067; Δ=+14; 인용 변경/좌표 이동 |
| 694 | models/ADCIRC/source-analysis/adcirc-hotstart.md:41 | read_input.F:1063-1075 | N | baseline 1063-1075: parent 1063..1075 → child 1077..1089; Δ=+14; 인용 변경/좌표 이동 |
| 711 | models/ADCIRC/source-analysis/adcirc-hotstart.md:104 | read_input.F:4504-4508 | N | baseline 4504-4508: parent 4504..4508 → child 4518..4522; Δ=+14; 인용 변경/좌표 이동 |
| 784 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:21 | src/read_input.F:1755-1774 | N | baseline 1755-1774: parent 1755..1774 → child 1769..1788; Δ=+14; 인용 변경/좌표 이동 |
| 792 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:27 | src/read_input.F:1825-2070 | N | baseline 1825-2070: parent 1825..2070 → child 1839..2084; Δ=+14; 인용 변경/좌표 이동 |
| 794 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:33 | read_input.F:1819-1824 | N | baseline 1819-1824: parent 1819..1824 → child 1833..1838; Δ=+14; 인용 변경/좌표 이동 |
| 796 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:34 | read_input.F:1825-1832 | N | baseline 1825-1832: parent 1825..1832 → child 1839..1846; Δ=+14; 인용 변경/좌표 이동 |
| 799 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:35 | read_input.F:1833-1852 | N | baseline 1833-1852: parent 1833..1852 → child 1847..1866; Δ=+14; 인용 변경/좌표 이동 |
| 801 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:36 | read_input.F:1853-1864 | N | baseline 1853-1864: parent 1853..1864 → child 1867..1878; Δ=+14; 인용 변경/좌표 이동 |
| 803 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:37 | read_input.F:1865-1890 | N | baseline 1865-1890: parent 1865..1890 → child 1879..1904; Δ=+14; 인용 변경/좌표 이동 |
| 805 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:38 | read_input.F:1891-1916 | N | baseline 1891-1916: parent 1891..1916 → child 1905..1930; Δ=+14; 인용 변경/좌표 이동 |
| 807 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:39 | read_input.F:1917-1929 | N | baseline 1917-1929: parent 1917..1929 → child 1931..1943; Δ=+14; 인용 변경/좌표 이동 |
| 809 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:40 | read_input.F:1933-1952 | N | baseline 1933-1952: parent 1933..1952 → child 1947..1966; Δ=+14; 인용 변경/좌표 이동 |
| 811 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:41 | read_input.F:1976-1989 | N | baseline 1976-1989: parent 1976..1989 → child 1990..2003; Δ=+14; 인용 변경/좌표 이동 |
| 813 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:42 | read_input.F:1990-2002 | N | baseline 1990-2002: parent 1990..2002 → child 2004..2016; Δ=+14; 인용 변경/좌표 이동 |
| 815 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:43 | read_input.F:2004-2031 | N | baseline 2004-2031: parent 2004..2031 → child 2018..2045; Δ=+14; 인용 변경/좌표 이동 |
| 817 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:44 | read_input.F:2658,4671 | N | baseline 2658-2658: parent 2658..2658 → child 2672..2672; Δ=+14; baseline 4671-4671: parent 4671..4671 → child 4685..4685; Δ=+14; 인용 변경/좌표 이동 |
| 819 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:45 | read_input.F:2033-2058 | N | baseline 2033-2058: parent 2033..2058 → child 2047..2072; Δ=+14; 인용 변경/좌표 이동 |
| 821 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:46 | read_input.F:2059-2069,2767-2774 | N | baseline 2059-2069: parent 2059..2069 → child 2073..2083; Δ=+14; baseline 2767-2774: parent 2767..2774 → child 2781..2788; Δ=+14; 인용 변경/좌표 이동 |
| 853 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:83 | src/read_input.F:269-270,516-519 | N | baseline 269-270: parent 269..270 → child 273..274; Δ=+4; baseline 516-519: parent 516..519 → child 530..533; Δ=+14; 인용 변경/좌표 이동 |
| 858 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:89 | src/read_input.F:2032-2058 | N | baseline 2032-2058: parent 2032..2058 → child 2046..2072; Δ=+14; 인용 변경/좌표 이동 |
| 865 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:94 | src/read_input.F:2059-2069 | N | baseline 2059-2069: parent 2059..2069 → child 2073..2083; Δ=+14; 인용 변경/좌표 이동 |
| 873 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:105 | src/read_input.F:238,484-487 | N | baseline 238-238: parent 238..238 → child 242..242; Δ=+4; baseline 484-487: parent 484..487 → child 498..501; Δ=+14; 인용 변경/좌표 이동 |
| 883 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:121 | read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 884 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:122 | src/read_input.F:3988-3993,4003-4014,4051 | N | baseline 3988-3993: parent 3988..3993 → child 4002..4007; Δ=+14; baseline 4003-4014: parent 4003..4014 → child 4017..4028; Δ=+14; baseline 4051-4051: parent 4051..4051 → child 4065..4065; Δ=+14; 인용 변경/좌표 이동 |
| 885 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:123 | src/read_input.F:4345-4353,4360-4371 | N | baseline 4345-4353: parent 4345..4353 → child 4359..4367; Δ=+14; baseline 4360-4371: parent 4360..4371 → child 4374..4385; Δ=+14; 인용 변경/좌표 이동 |
| 889 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:124 | read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 901 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:156 | src/read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 938 | models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:7 | read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 945 | models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:20 | read_input.F:3504-3589 | N | baseline 3504-3589: parent 3504..3589 → child 3518..3603; Δ=+14; 인용 변경/좌표 이동 |
| 947 | models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:22 | read_input.F:3505 | N | baseline 3505-3505: parent 3505..3505 → child 3519..3519; Δ=+14; 인용 변경/좌표 이동 |
| 994 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:31 | read_input.F:3613-3633,4124-4152 | N | baseline 3613-3633: parent 3613..3633 → child 3627..3647; Δ=+14; baseline 4124-4152: parent 4124..4152 → child 4138..4166; Δ=+14; 인용 변경/좌표 이동 |
| 995 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:31 | src/read_input.F:3613-3633,4124-4152 | N | baseline 3613-3633: parent 3613..3633 → child 3627..3647; Δ=+14; baseline 4124-4152: parent 4124..4152 → child 4138..4166; Δ=+14; 인용 변경/좌표 이동 |
| 1012 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:56 | read_input.F:3998-4021,4356-4384 | N | baseline 3998-4021: parent 3998..4021 → child 4012..4035; Δ=+14; baseline 4356-4384: parent 4356..4384 → child 4370..4398; Δ=+14; 인용 변경/좌표 이동 |
| 1013 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:56 | src/read_input.F:3998-4021,4356-4384 | N | baseline 3998-4021: parent 3998..4021 → child 4012..4035; Δ=+14; baseline 4356-4384: parent 4356..4384 → child 4370..4398; Δ=+14; 인용 변경/좌표 이동 |
| 1026 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:70 | src/read_input.F:4421-4452,4500 | N | baseline 4421-4452: parent 4421..4452 → child 4435..4466; Δ=+14; baseline 4500-4500: parent 4500..4500 → child 4514..4514; Δ=+14; 인용 변경/좌표 이동 |
| 1149 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:78 | src/read_input.F:394 | N | baseline 394-394: parent 394..394 → child 398..398; Δ=+4; 인용 변경/좌표 이동 |
| 1246 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:22 | read_input.F:1080-1083,1790-1817,2255-2261 | N | baseline 1080-1083: parent 1080..1083 → child 1094..1097; Δ=+14; baseline 1790-1817: parent 1790..1817 → child 1804..1831; Δ=+14; baseline 2255-2261: parent 2255..2261 → child 2269..2275; Δ=+14; 인용 변경/좌표 이동 |
| 1287 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:94 | read_input.F:1790-1817 | N | baseline 1790-1817: parent 1790..1817 → child 1804..1831; Δ=+14; 인용 변경/좌표 이동 |
| 1296 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:138 | read_input.F:1080-1083 | N | baseline 1080-1083: parent 1080..1083 → child 1094..1097; Δ=+14; 인용 변경/좌표 이동 |
| 1414 | models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:82 | read_input.F:2996 | N | baseline 2996-2996: parent 2996..2996 → child 3010..3010; Δ=+14; 인용 변경/좌표 이동 |
| 1845 | models/ADCIRC/source-analysis/storm-surge/README.md:9 | read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1848 | models/ADCIRC/source-analysis/storm-surge/README.md:16 | read_input.F:2157 | N | baseline 2157-2157: parent 2157..2157 → child 2171..2171; Δ=+14; 인용 변경/좌표 이동 |
| 1854 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-foundation.md:7 | read_input.F:1782 | N | baseline 1782-1782: parent 1782..1782 → child 1796..1796; Δ=+14; 인용 변경/좌표 이동 |
| 1863 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-foundation.md:95 | read_input.F:1782 | N | baseline 1782-1782: parent 1782..1782 → child 1796..1796; Δ=+14; 인용 변경/좌표 이동 |
| 1890 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md:7 | read_input.F:1782 | N | baseline 1782-1782: parent 1782..1782 → child 1796..1796; Δ=+14; 인용 변경/좌표 이동 |
| 1894 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md:55 | read_input.F:1782 | N | baseline 1782-1782: parent 1782..1782 → child 1796..1796; Δ=+14; 인용 변경/좌표 이동 |
| 1922 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:24 | read_input.F:2157,2190,2255-2261,2430,2706,2884,2975 | N | baseline 2157-2157: parent 2157..2157 → child 2171..2171; Δ=+14; baseline 2190-2190: parent 2190..2190 → child 2204..2204; Δ=+14; baseline 2255-2261: parent 2255..2261 → child 2269..2275; Δ=+14; baseline 2430-2430: parent 2430..2430 → child 2444..2444; Δ=+14; baseline 2706-2706: parent 2706..2706 → child 2720..2720; Δ=+14; baseline 2884-2884: parent 2884..2884 → child 2898..2898; Δ=+14; baseline 2975-2975: parent 2975..2975 → child 2989..2989; Δ=+14; 인용 변경/좌표 이동 |
| 1933 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:36 | read_input.F:2706 | N | baseline 2706-2706: parent 2706..2706 → child 2720..2720; Δ=+14; 인용 변경/좌표 이동 |
| 1945 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:61 | read_input.F:2157 | N | baseline 2157-2157: parent 2157..2157 → child 2171..2171; Δ=+14; 인용 변경/좌표 이동 |
| 1969 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:157 | read_input.F:2430 | N | baseline 2430-2430: parent 2430..2430 → child 2444..2444; Δ=+14; 인용 변경/좌표 이동 |
| 1979 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:38 | src/read_input.F:1705-1731 | N | baseline 1705-1731: parent 1705..1731 → child 1719..1745; Δ=+14; 인용 변경/좌표 이동 |
| 1981 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:42 | src/read_input.F:6282-6463 | N | baseline 6282-6463: parent 6306..6487 → child 6320..6501; Δ=+14; 인용 변경/좌표 이동 |
| 1985 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:47 | src/read_input.F:3410-3436 | N | baseline 3410-3436: parent 3410..3436 → child 3424..3450; Δ=+14; 인용 변경/좌표 이동 |
| 1989 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:50 | src/read_input.F:3450-3456 | N | baseline 3450-3456: parent 3450..3456 → child 3464..3470; Δ=+14; 인용 변경/좌표 이동 |
| 1991 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:64 | src/read_input.F:3431-3456,3485-3497 | N | baseline 3431-3456: parent 3431..3456 → child 3445..3470; Δ=+14; baseline 3485-3497: parent 3485..3497 → child 3499..3511; Δ=+14; 인용 변경/좌표 이동 |
| 1994 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:66 | read_input.F:3493-3496 | N | baseline 3493-3496: parent 3493..3496 → child 3507..3510; Δ=+14; 인용 변경/좌표 이동 |
| 2001 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:77 | src/read_input.F:3410-3436,3450-3456 | N | baseline 3410-3436: parent 3410..3436 → child 3424..3450; Δ=+14; baseline 3450-3456: parent 3450..3456 → child 3464..3470; Δ=+14; 인용 변경/좌표 이동 |
| 2002 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:88 | src/read_input.F:6282-6463 | N | baseline 6282-6463: parent 6306..6487 → child 6320..6501; Δ=+14; 인용 변경/좌표 이동 |
| 2005 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:98 | src/read_input.F:6429-6455 | N | baseline 6429-6455: parent 6453..6479 → child 6467..6493; Δ=+14; 인용 변경/좌표 이동 |
| 2012 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:112 | src/read_input.F:3347-3354 | N | baseline 3347-3354: parent 3347..3354 → child 3361..3368; Δ=+14; 인용 변경/좌표 이동 |
| 2031 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:142 | src/read_input.F:3349,3371-3383 | N | baseline 3349-3349: parent 3349..3349 → child 3363..3363; Δ=+14; baseline 3371-3383: parent 3371..3383 → child 3385..3397; Δ=+14; 인용 변경/좌표 이동 |
| 2034 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:143 | src/read_input.F:3429-3436,3433 | N | baseline 3429-3436: parent 3429..3436 → child 3443..3450; Δ=+14; baseline 3433-3433: parent 3433..3433 → child 3447..3447; Δ=+14; 인용 변경/좌표 이동 |
| 2039 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:144 | src/read_input.F:2541 | N | baseline 2541-2541: parent 2541..2541 → child 2555..2555; Δ=+14; 인용 변경/좌표 이동 |
| 2054 | models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:174 | src/read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 2066 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:48 | src/read_input.F:1703-1731,3335-3349 | N | baseline 1703-1731: parent 1703..1731 → child 1717..1745; Δ=+14; baseline 3335-3349: parent 3335..3349 → child 3349..3363; Δ=+14; 인용 변경/좌표 이동 |
| 2072 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:49 | src/read_input.F:3431-3441 | N | baseline 3431-3441: parent 3431..3441 → child 3445..3455; Δ=+14; 인용 변경/좌표 이동 |
| 2077 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:63 | src/read_input.F:3431-3456,3485-3497 | N | baseline 3431-3456: parent 3431..3456 → child 3445..3470; Δ=+14; baseline 3485-3497: parent 3485..3497 → child 3499..3511; Δ=+14; 인용 변경/좌표 이동 |
| 2078 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:71 | src/read_input.F:1717-1731,3431-3435,3485-3497 | N | baseline 1717-1731: parent 1717..1731 → child 1731..1745; Δ=+14; baseline 3431-3435: parent 3431..3435 → child 3445..3449; Δ=+14; baseline 3485-3497: parent 3485..3497 → child 3499..3511; Δ=+14; 인용 변경/좌표 이동 |
| 2086 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:128 | src/read_input.F:2894-2902 | N | baseline 2894-2902: parent 2894..2902 → child 2908..2916; Δ=+14; 인용 변경/좌표 이동 |
| 2089 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:130 | src/read_input.F:3628-3632,3757-3761,4143-4148,4217-4222,4534-4537 | N | baseline 3628-3632: parent 3628..3632 → child 3642..3646; Δ=+14; baseline 3757-3761: parent 3757..3761 → child 3771..3775; Δ=+14; baseline 4143-4148: parent 4143..4148 → child 4157..4162; Δ=+14; baseline 4217-4222: parent 4217..4222 → child 4231..4236; Δ=+14; baseline 4534-4537: parent 4534..4537 → child 4548..4551; Δ=+14; 인용 변경/좌표 이동 |
| 2119 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:220 | read_input.F:1705-1731,3344-3497,6282-6463 | N | baseline 1705-1731: parent 1705..1731 → child 1719..1745; Δ=+14; baseline 3344-3497: parent 3344..3497 → child 3358..3511; Δ=+14; baseline 6282-6463: parent 6306..6487 → child 6320..6501; Δ=+14; 인용 변경/좌표 이동 |
| 2125 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:241 | read_input.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 2132 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:250 | src/read_input.F:3493-3496 | N | baseline 3493-3496: parent 3493..3496 → child 3507..3510; Δ=+14; 인용 변경/좌표 이동 |
| 2136 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:254 | read_input.F:6282-6463 | N | baseline 6282-6463: parent 6306..6487 → child 6320..6501; Δ=+14; 인용 변경/좌표 이동 |
| 2165 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:335 | src/read_input.F:2534-2543,3436,3493-3496 | N | baseline 2534-2543: parent 2534..2543 → child 2548..2557; Δ=+14; baseline 3436-3436: parent 3436..3436 → child 3450..3450; Δ=+14; baseline 3493-3496: parent 3493..3496 → child 3507..3510; Δ=+14; 인용 변경/좌표 이동 |
| 2167 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:335 | src/read_input.F:2534-2543,3436,3493-3496 | N | baseline 2534-2543: parent 2534..2543 → child 2548..2557; Δ=+14; baseline 3436-3436: parent 3436..3436 → child 3450..3450; Δ=+14; baseline 3493-3496: parent 3493..3496 → child 3507..3510; Δ=+14; 인용 변경/좌표 이동 |
| 2178 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:346 | src/read_input.F:3431-3456,3485-3497 | N | baseline 3431-3456: parent 3431..3456 → child 3445..3470; Δ=+14; baseline 3485-3497: parent 3485..3497 → child 3499..3511; Δ=+14; 인용 변경/좌표 이동 |
| 2180 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:355 | src/read_input.F:3485-3497 | N | baseline 3485-3497: parent 3485..3497 → child 3499..3511; Δ=+14; 인용 변경/좌표 이동 |
| 2182 | models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:368 | src/read_input.F:1705-1731,3410-3444 | N | baseline 1705-1731: parent 1705..1731 → child 1719..1745; Δ=+14; baseline 3410-3444: parent 3410..3444 → child 3424..3458; Δ=+14; 인용 변경/좌표 이동 |

### 참조 원장 976fc5b6cafb · thirdparty/swan/SwanBpntlist.ftn90

직접 ref_file 매칭 0행. 주제/심볼 anchor는 위 판정 참조.

### 참조 원장 976fc5b6cafb · thirdparty/swan/SwanCompUnstruc.ftn90

직접 ref_file 매칭 0행. 주제/심볼 anchor는 위 판정 참조.

### 참조 원장 976fc5b6cafb · thirdparty/swan/SwanGriddata.ftn90

직접 ref_file 매칭 0행. 주제/심볼 anchor는 위 판정 참조.

### 참조 원장 976fc5b6cafb · thirdparty/swan/SwanReadADCGrid.ftn90

직접 ref_file 매칭 0행. 주제/심볼 anchor는 위 판정 참조.

### 참조 원장 976fc5b6cafb · thirdparty/swan/SwanVTKPDataSets.ftn90

직접 ref_file 매칭 0행. 주제/심볼 anchor는 위 판정 참조.

### 참조 원장 976fc5b6cafb · thirdparty/swan/swanout2.ftn

직접 ref_file 매칭 0행. 주제/심볼 anchor는 위 판정 참조.

### 참조 원장 976fc5b6cafb · thirdparty/swan/swanparll.ftn

직접 ref_file 매칭 0행. 주제/심볼 anchor는 위 판정 참조.

### 참조 원장 976fc5b6cafb · thirdparty/swan/swanpre1.ftn

직접 ref_file 매칭 0행. 주제/심볼 anchor는 위 판정 참조.

### 참조 원장 976fc5b6cafb · thirdparty/swan/swanpre2.ftn

직접 ref_file 매칭 0행. 주제/심볼 anchor는 위 판정 참조.

### 참조 원장 976fc5b6cafb · thirdparty/swan/swmod1.ftn

직접 ref_file 매칭 0행. 주제/심볼 anchor는 위 판정 참조.

### 참조 원장 976fc5b6cafb · thirdparty/swan/swmod2.ftn

직접 ref_file 매칭 0행. 주제/심볼 anchor는 위 판정 참조.

### 참조 원장 5203dafc6871 · src/nodalattr.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 361 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51 | src/nodalattr.F:1141,1154 | N | baseline 1141-1141: parent 1174..1174 → child 1175..1175; Δ=+1; baseline 1154-1154: parent 1187..1187 → child 1188..1188; Δ=+1; 인용 변경/좌표 이동 |
| 362 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51 | src/nodalattr.F:1141,1154 | N | baseline 1141-1141: parent 1174..1174 → child 1175..1175; Δ=+1; baseline 1154-1154: parent 1187..1187 → child 1188..1188; Δ=+1; 인용 변경/좌표 이동 |
| 489 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:160 | src/nodalattr.F:1051 | N | baseline 1051-1051: parent 1082..1082 → child 1083..1083; Δ=+1; 인용 변경/좌표 이동 |
| 495 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:175 | src/nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 931 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:68 | nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 961 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:6 | models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 962 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:19 | src/nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 965 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:21 | nodalattr.F:636-686 | N | baseline 636-686: parent 655..707 → child 657..709; Δ=+2; 인용 변경/좌표 이동 |
| 983 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:73 | nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1218 | models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:39 | src/nodalattr.F:1051 | N | baseline 1051-1051: parent 1082..1082 → child 1083..1083; Δ=+1; 인용 변경/좌표 이동 |
| 1375 | models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:56 | nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |

### 참조 원장 40201037d1a6 · CITATION.cff

직접 ref_file 매칭 0행. 주제/심볼 anchor는 위 판정 참조.

### 참조 원장 40201037d1a6 · README.md

직접 ref_file 매칭 0행. 주제/심볼 anchor는 위 판정 참조.

### 참조 원장 40201037d1a6 · src/constants.F90

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 1930 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:29 | constants.F90:54 | X | baseline 54-54: parent 54..54 → child 54..54; Δ=+0; 범위 제외 규칙 |
| 1962 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:133 | constants.F90:54 | X | baseline 54-54: parent 54..54 → child 54..54; Δ=+0; 범위 제외 규칙 |

### 참조 원장 40201037d1a6 · src/owiwind.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 366 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:52 | src/owiwind.F:188 | X | baseline 188-188: parent 188..188 → child 188..188; Δ=+0; 범위 제외 규칙 |
| 491 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:161 | src/owiwind.F:188 | X | baseline 188-188: parent 188..188 → child 188..188; Δ=+0; 범위 제외 규칙 |
| 499 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:177 | src/owiwind.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 837 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:65 | src/owiwind.F:168-255,269-369 | X | baseline 168-255: parent 168..255 → child 168..255; Δ=+0; baseline 269-369: parent 269..369 → child 269..369; Δ=+0; 범위 제외 규칙 |
| 838 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:65 | src/owiwind.F:168-255,269-369 | X | baseline 168-255: parent 168..255 → child 168..255; Δ=+0; baseline 269-369: parent 269..369 → child 269..369; Δ=+0; 범위 제외 규칙 |
| 841 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:66 | src/owiwind.F:798-807,830-836,888-903 | X | baseline 798-807: parent 798..807 → child 798..807; Δ=+0; baseline 830-836: parent 830..836 → child 830..836; Δ=+0; baseline 888-903: parent 888..903 → child 888..903; Δ=+0; 범위 제외 규칙 |
| 842 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:70 | src/owiwind.F:489-490,508-509,579-580 | X | baseline 489-490: parent 489..490 → child 489..490; Δ=+0; baseline 508-509: parent 508..509 → child 508..509; Δ=+0; baseline 579-580: parent 579..580 → child 579..580; Δ=+0; 범위 제외 규칙 |
| 843 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:71 | src/owiwind.F:554-569 | X | baseline 554-569: parent 554..569 → child 554..569; Δ=+0; 범위 제외 규칙 |
| 844 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:72 | src/owiwind.F:1085-1099 | X | baseline 1085-1099: parent 1085..1099 → child 1085..1099; Δ=+0; 범위 제외 규칙 |
| 887 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:124 | owiwind.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 899 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:154 | src/owiwind.F | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 1928 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:27 | owiwind.F:184,269 | X | baseline 184-184: parent 184..184 → child 184..184; Δ=+0; baseline 269-269: parent 269..269 → child 269..269; Δ=+0; 범위 제외 규칙 |
| 1949 | models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:85 | owiwind.F:184 | X | baseline 184-184: parent 184..184 → child 184..184; Δ=+0; 범위 제외 규칙 |

### 참조 원장 40201037d1a6 · src/weir_boundary.F90

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 1491 | models/ADCIRC/source-analysis/adcirc-weir-boundary.md:2 | weir_boundary.F90 | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 1492 | models/ADCIRC/source-analysis/adcirc-weir-boundary.md:6 | models/ADCIRC/raw/source_code/adcirc/src/weir_boundary.F90 | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 1493 | models/ADCIRC/source-analysis/adcirc-weir-boundary.md:17 | weir_boundary.F90 | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |
| 1494 | models/ADCIRC/source-analysis/adcirc-weir-boundary.md:19 | weir_boundary.F90 | X | 숫자 범위 없음: 줄 이동 unknown; 범위 제외 규칙 |

### 참조 원장 40201037d1a6 · util/adcircResultsComparison.F90

직접 ref_file 매칭 0행. 주제/심볼 anchor는 위 판정 참조.

### 참조 원장 e8b62a70db39 · src/nodalattr.F

| CSV행 | note_file:note_line | ref | 참조 판정 | 이동 및 근거 |
|---:|---|---|---|---|
| 361 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51 | src/nodalattr.F:1141,1154 | N | baseline 1141-1141: parent 1175..1175 → child 1173..1173; Δ=-2; baseline 1154-1154: parent 1188..1188 → child 1186..1186; Δ=-2; 인용 변경/좌표 이동 |
| 362 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51 | src/nodalattr.F:1141,1154 | N | baseline 1141-1141: parent 1175..1175 → child 1173..1173; Δ=-2; baseline 1154-1154: parent 1188..1188 → child 1186..1186; Δ=-2; 인용 변경/좌표 이동 |
| 489 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:160 | src/nodalattr.F:1051 | N | baseline 1051-1051: parent 1083..1083 → child 1081..1081; Δ=-2; 인용 변경/좌표 이동 |
| 495 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:175 | src/nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 931 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:68 | nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 961 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:6 | models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 962 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:19 | src/nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 965 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:21 | nodalattr.F:636-686 | X | baseline 636-686: parent 657..709 → child 657..709; Δ=+0; 이 커밋에서 인용 범위 내용/좌표 변화 없음 |
| 983 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:73 | nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |
| 1218 | models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:39 | src/nodalattr.F:1051 | N | baseline 1051-1051: parent 1083..1083 → child 1081..1081; Δ=-2; 인용 변경/좌표 이동 |
| 1375 | models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:56 | nodalattr.F | P | 숫자 범위 없음: 줄 이동 unknown; 파일만 인용 또는 치환점 대응 불명 |

## baseline→tip 숫자 인용 대응

동일 note/ref 중복은 한 번만 표기. 아래 주소는 baseline 좌표라는 전제 아래 diff로 계산한 결과이며 원소스 존재 검증을 대체하지 않는다.

| note_file:note_line | baseline ref | tip 대응 범위 | 상태 |
|---|---|---|---|
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:20 | src/read_input.F:1176-1191 | 1190-1205 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:20 | src/read_input.F:3072-3072 | 3086-3086 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:20 | src/read_input.F:5139-5482 | 5153-5496 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:20 | src/read_input.F:5682-5682 | 5720-5720 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:23 | src/cstart.F:348-348 | 348-348 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:24 | src/timestep.F:1121-1121 | 1125-1125 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:24 | src/timestep.F:1125-1125 | 1129-1129 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:24 | src/timestep.F:1918-1918 | 1922-1922 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:24 | src/timestep.F:2150-2355 | 2154-2359 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:25 | src/gwce.F:780-1450 | 780-1450 | 내용 변경 포함 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:26 | src/vsmy.F:1168-1168 | 1168-1168 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:26 | src/vsmy.F:1543-3871 | 1545-3878 | 일부 삭제/치환 unknown; 내용 변경 포함 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:26 | src/vsmy.F:4061-4315 | 4081-4335 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:28 | src/write_output.F:2993-3331 | 3053-3391 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:36 | src/cstart.F:348-348 | 348-348 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:37 | src/read_input.F:1176-1191 | 1190-1205 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:44 | src/read_input.F:5139-5139 | 5153-5153 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:60 | src/vsmy.F:1548-1553 | 1550-1555 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:68 | src/vsmy.F:1630-1630 | 1632-1632 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:70 | src/read_input.F:5682-5682 | 5720-5720 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:74 | src/vsmy.F:4061-4061 | 4081-4081 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:84 | src/timestep.F:1121-1121 | 1125-1125 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:88 | src/timestep.F:1125-1125 | 1129-1129 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:94 | src/vsmy.F:1168-1168 | 1168-1168 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:102 | src/gwce.F:780-780 | 780-780 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:105 | src/gwce.F:1196-1196 | 1196-1196 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:105 | src/gwce.F:1283-1283 | 1283-1283 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:105 | src/gwce.F:1405-1405 | 1405-1405 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:105 | src/gwce.F:1450-1450 | 1450-1450 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:112 | src/timestep.F:2150-2355 | 2154-2359 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:116 | src/read_input.F:5235-5235 | 5249-5249 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:121 | src/vsmy.F:1823-1823 | 1825-1825 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:121 | src/vsmy.F:1840-1840 | 1842-1842 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:121 | src/vsmy.F:1870-1870 | 1872-1872 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:121 | src/vsmy.F:1931-1931 | 1933-1933 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:121 | src/vsmy.F:1983-1983 | 1985-1985 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:122 | src/vsmy.F:2035-2035 | 2037-2037 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:122 | src/vsmy.F:2403-2403 | 2405-2405 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:127 | src/vsmy.F:2740-2740 | 2742-2742 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:135 | src/read_input.F:5296-5296 | 5310-5310 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:135 | src/write_output.F:2993-2993 | 3053-3053 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-mode.md:144 | src/write_output.F:3331-3331 | 3391-3391 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:23 | src/vsmy.F:142-1703 | 142-1705 | 일부 삭제/치환 unknown; 내용 변경 포함 |
| models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:23 | src/timestep.F:1121-1123 | 1125-1127 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:25 | src/read_input.F:5073-5073 | 5087-5087 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:30 | src/read_input.F:5127-5127 | 5141-5141 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:53 | src/vsmy.F:2299-2319 | 2301-2321 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:65 | src/read_input.F:5102-5102 | 5116-5116 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:44 | src/read_input.F:380-380 | 384-384 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:45 | src/read_input.F:394-394 | 398-398 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:45 | src/read_input.F:5296-5296 | 5310-5310 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51 | src/nodalattr.F:1141-1141 | 1173-1173 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51 | src/nodalattr.F:1154-1154 | 1186-1186 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:52 | src/owiwind.F:188-188 | 188-188 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:53 | src/cstart.F:313-313 | 313-313 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:54 | src/read_input.F:6425-6425 | 6463-6463 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:54 | src/read_input.F:6453-6453 | 6491-6491 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:63 | src/write_output.F:510-510 | 511-511 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:63 | src/cstart.F:376-376 | 376-376 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:64 | src/write_output.F:546-546 | 547-547 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:64 | src/cstart.F:394-394 | 394-394 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:65 | src/write_output.F:598-598 | 614-614 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:65 | src/cstart.F:487-487 | 487-487 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:66 | src/write_output.F:710-710 | 726-726 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:66 | src/cstart.F:584-584 | 584-584 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:67 | src/write_output.F:946-946 | 968-968 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:67 | src/cstart.F:467-467 | 467-467 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:68 | src/write_output.F:1160-1160 | 1182-1182 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:68 | src/cstart.F:412-412 | 412-412 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:69 | src/write_output.F:1191-1191 | 1213-1213 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:69 | src/cstart.F:665-665 | 665-665 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:70 | src/write_output.F:619-619 | 635-635 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:70 | src/cstart.F:501-501 | 501-501 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:71 | src/write_output.F:641-641 | 657-657 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:71 | src/cstart.F:492-492 | 492-492 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:79 | src/write_output.F:735-735 | 757-757 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:80 | src/write_output.F:775-775 | 797-797 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:81 | src/write_output.F:817-817 | 839-839 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:82 | src/write_output.F:904-904 | 926-926 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:83 | src/write_output.F:1064-1064 | 1086-1086 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:84 | src/write_output.F:1039-1039 | 1061-1061 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:90 | src/write_output.F:2993-2993 | 3053-3053 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:91 | src/write_output.F:3059-3059 | 3119-3119 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:99 | src/write_output.F:2178-2178 | 2237-2237 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:100 | src/write_output.F:2232-2232 | 2291-2291 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:101 | src/write_output.F:2339-2339 | 2398-2398 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:107 | src/gwce.F:148-148 | 148-148 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:109 | prep/prep.F:7439-7439 | 7472-7472 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:160 | src/nodalattr.F:1051-1051 | 1081-1081 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:161 | src/owiwind.F:188-188 | 188-188 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort15-checklist-v1.md:7 | src/read_input.F:1133-1162 | 1147-1176 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-fort15-checklist-v1.md:88 | src/read_input.F:1133-1135 | 1147-1149 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:21 | src/gwce.F:237-237 | 237-237 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:21 | src/gwce.F:427-427 | 427-427 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:22 | src/gwce.F:418-420 | 418-420 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:25 | src/gwce.F:538-540 | 538-540 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:26 | src/gwce.F:564-592 | 564-592 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:27 | src/gwce.F:517-517 | 517-517 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:27 | src/gwce.F:538-539 | 538-539 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:27 | src/gwce.F:607-607 | 607-607 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:27 | src/gwce.F:623-623 | 623-623 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:28 | src/gwce.F:429-636 | 429-636 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:29 | src/gwce.F:998-1617 | 998-1617 | 내용 변경 포함 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:30 | src/gwce.F:638-673 | 638-673 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:30 | src/gwce.F:1846-1854 | 1846-1854 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:31 | src/gwce.F:141-141 | 141-141 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:31 | src/gwce.F:430-430 | 430-430 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:31 | src/gwce.F:455-455 | 455-455 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:31 | src/gwce.F:595-595 | 595-595 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:31 | src/gwce.F:709-709 | 709-709 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:31 | src/gwce.F:1846-1846 | 1846-1846 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:31 | src/gwce.F:1856-1856 | 1856-1856 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:32 | src/gwce.F:141-154 | 141-154 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:36 | src/gwce.F:538-539 | 538-539 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:36 | src/gwce.F:623-623 | 623-623 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:36 | src/gwce.F:1429-1429 | 1429-1429 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:36 | src/gwce.F:1741-1741 | 1741-1741 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:36 | src/gwce.F:1758-1758 | 1758-1758 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:37 | src/hstart.F:719-720 | 725-725 | 일부 삭제/치환 unknown; 내용 변경 포함 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:38 | src/gwce.F:2514-2522 | 2514-2522 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:39 | src/gwce.F:1540-1543 | 1540-1543 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:39 | src/gwce.F:2851-2852 | 2851-2852 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:40 | src/gwce.F:1622-1631 | 1622-1631 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:41 | src/gwce.F:2007-2007 | 2007-2007 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:41 | src/gwce.F:2020-2020 | 2020-2020 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:43 | src/gwce.F:2477-2482 | 2477-2482 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:47 | src/gwce.F:2001-2004 | 2001-2004 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:48 | src/gwce.F:2010-2017 | 2010-2017 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:49 | src/gwce.F:146-146 | 146-146 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:49 | src/gwce.F:2002-2002 | 2002-2002 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:50 | src/gwce.F:150-150 | 150-150 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:51 | src/gwce.F:2005-2005 | 2005-2005 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:55 | src/gwce.F:1638-1650 | 1638-1650 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:56 | src/gwce.F:1659-1673 | 1659-1673 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:57 | src/gwce.F:270-271 | 270-271 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:57 | src/cstart.F:64-64 | 64-64 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:57 | src/hstart.F:58-58 | 58-58 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:58 | src/gwce.F:1725-1834 | 1725-1834 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:58 | src/gwce.F:1740-1764 | 1740-1764 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:58 | src/gwce.F:1782-1805 | 1782-1805 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:59 | src/gwce.F:652-673 | 652-673 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:59 | src/gwce.F:1840-1861 | 1840-1861 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:60 | src/gwce.F:474-477 | 474-477 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:60 | src/gwce.F:1010-1015 | 1010-1015 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:60 | src/cstart.F:1221-1223 | 1224-1226 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:60 | src/cstart.F:1258-1260 | 1261-1263 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:65 | src/hstart.F:1522-1522 | 1527-1527 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:65 | src/hstart.F:1530-1532 | 1535-1537 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:66 | src/gwce.F:1181-1184 | 1181-1184 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:66 | src/gwce.F:1450-1452 | 1450-1452 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:66 | src/gwce.F:1462-1464 | 1462-1464 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:71 | src/gwce.F:477-477 | 477-477 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:71 | src/gwce.F:605-605 | 605-605 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:71 | src/gwce.F:1015-1015 | 1015-1015 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:71 | src/gwce.F:1074-1074 | 1074-1074 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:73 | src/gwce.F:465-473 | 465-473 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:73 | src/gwce.F:541-547 | 541-547 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:73 | src/gwce.F:1055-1063 | 1055-1063 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:73 | src/gwce.F:1436-1439 | 1436-1439 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:74 | src/cstart.F:1221-1231 | 1224-1234 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:74 | src/cstart.F:1258-1268 | 1261-1271 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:81 | src/gwce.F:538-592 | 538-592 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:83 | src/gwce.F:1638-1650 | 1638-1650 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:84 | src/gwce.F:477-477 | 477-477 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:97 | src/read_input.F:3431-3456 | 3445-3470 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:19 | src/read_input.F:1050-1075 | 1064-1089 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:19 | src/read_input.F:4504-4544 | 4518-4558 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:21 | src/hstart.F:47-3048 | 47-3076 | 일부 삭제/치환 unknown; 내용 변경 포함 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:22 | src/write_output.F:4429-4429 | 4518-4518 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:22 | src/write_output.F:4920-5374 | 5009-5463 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:23 | src/vsmy.F:3254-3254 | 3261-3261 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:23 | src/vsmy.F:3531-3778 | 3538-3785 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:24 | src/netcdfio.F90:3866-9188 | 3866-9188 | 일부 삭제/치환 unknown; 내용 변경 포함 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:25 | src/timestep.F:1192-1211 | 1196-1215 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:30 | src/read_input.F:1050-1053 | 1064-1067 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:35 | src/hstart.F:242-253 | 242-253 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:36 | src/hstart.F:452-465 | 452-465 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:38 | src/hstart.F:673-690 | 673-690 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:41 | src/read_input.F:1063-1075 | 1077-1089 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:45 | src/hstart.F:485-492 | 485-492 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:45 | src/write_output.F:4920-4923 | 5009-5012 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:47 | src/write_output.F:4922-4931 | 5011-5020 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:70 | src/hstart.F:506-668 | 506-668 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:76 | src/hstart.F:47-47 | 47-47 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:84 | src/write_output.F:4429-4429 | 4518-4518 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:86 | src/vsmy.F:3254-3254 | 3261-3261 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:90 | src/netcdfio.F90:3866-3871 | 3866-3871 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:104 | src/read_input.F:4504-4508 | 4518-4522 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:116 | src/timestep.F:1192-1197 | 1196-1201 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:122 | src/hstart.F:526-536 | 526-536 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:122 | src/write_output.F:4935-4945 | 5024-5034 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:123 | src/hstart.F:529-533 | 529-533 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:123 | src/netcdfio.F90:5357-5380 | 5357-5380 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:127 | src/vsmy.F:3531-3778 | 3538-3785 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:130 | src/hstart.F:1440-1444 | 1445-1449 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:138 | src/netcdfio.F90:8109-8158 | 8109-8158 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:144 | src/hstart.F:1442-1444 | 1447-1449 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-hotstart.md:188 | src/netcdfio.F90:8017-8085 | 8017-8085 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-itpack-solver.md:6 | src/gwce.F:2003-2003 | 2003-2003 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-itpack-solver.md:21 | src/gwce.F:2003-2003 | 2003-2003 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-itpack-solver.md:30 | src/gwce.F:2010-2010 | 2010-2010 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:21 | src/read_input.F:1755-1774 | 1769-1788 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:27 | src/read_input.F:1825-2070 | 1839-2084 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:33 | src/read_input.F:1819-1824 | 1833-1838 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:34 | src/read_input.F:1825-1832 | 1839-1846 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:35 | src/read_input.F:1833-1852 | 1847-1866 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:36 | src/read_input.F:1853-1864 | 1867-1878 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:37 | src/read_input.F:1865-1890 | 1879-1904 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:38 | src/read_input.F:1891-1916 | 1905-1930 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:39 | src/read_input.F:1917-1929 | 1931-1943 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:40 | src/read_input.F:1933-1952 | 1947-1966 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:41 | src/read_input.F:1976-1989 | 1990-2003 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:42 | src/read_input.F:1990-2002 | 2004-2016 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:43 | src/read_input.F:2004-2031 | 2018-2045 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:44 | src/read_input.F:2658-2658 | 2672-2672 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:44 | src/read_input.F:4671-4671 | 4685-4685 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:45 | src/read_input.F:2033-2058 | 2047-2072 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:46 | src/read_input.F:2059-2069 | 2073-2083 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:46 | src/read_input.F:2767-2774 | 2781-2788 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:65 | src/owiwind.F:168-255 | 168-255 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:65 | src/owiwind.F:269-369 | 269-369 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:66 | src/owiwind.F:798-807 | 798-807 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:66 | src/owiwind.F:830-836 | 830-836 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:66 | src/owiwind.F:888-903 | 888-903 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:70 | src/owiwind.F:489-490 | 489-490 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:70 | src/owiwind.F:508-509 | 508-509 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:70 | src/owiwind.F:579-580 | 579-580 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:71 | src/owiwind.F:554-569 | 554-569 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:72 | src/owiwind.F:1085-1099 | 1085-1099 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:83 | src/read_input.F:269-270 | 273-274 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:83 | src/read_input.F:516-519 | 530-533 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:89 | src/read_input.F:2032-2058 | 2046-2072 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:94 | src/read_input.F:2059-2069 | 2073-2083 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:105 | src/read_input.F:238-238 | 242-242 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:105 | src/read_input.F:484-487 | 498-501 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:122 | src/read_input.F:3988-3993 | 4002-4007 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:122 | src/read_input.F:4003-4014 | 4017-4028 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:122 | src/read_input.F:4051-4051 | 4065-4065 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:123 | src/read_input.F:4345-4353 | 4359-4367 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:123 | src/read_input.F:4360-4371 | 4374-4385 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:6 | src/gwce.F:2479-2479 | 2479-2479 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:6 | src/timestep.F:129-129 | 129-129 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:61 | src/gwce.F:2479-2479 | 2479-2479 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:66 | src/timestep.F:129-129 | 129-129 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:68 | src/gwce.F:2477-2482 | 2477-2482 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:69 | src/timestep.F:1634-1634 | 1638-1638 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:73 | src/gwce.F:442-442 | 442-442 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:20 | src/read_input.F:3504-3589 | 3518-3603 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:22 | src/read_input.F:3505-3505 | 3519-3519 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:40 | src/timestep.F:860-880 | 864-884 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:54 | src/gwce.F:1725-1810 | 1725-1810 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:78 | src/gwce.F:1727-1733 | 1727-1733 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:21 | src/nodalattr.F:636-686 | 657-709 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:21 | src/write_output.F:1773-1773 | 1819-1819 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:22 | src/write_output.F:523-523 | 524-524 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:22 | src/write_output.F:1811-1823 | 1860-1872 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:23 | src/write_output.F:504-523 | 505-524 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:23 | src/write_output.F:593-603 | 609-619 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:31 | src/read_input.F:3613-3633 | 3627-3647 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:31 | src/read_input.F:4124-4152 | 4138-4166 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:32 | src/write_output.F:4226-4250 | 4315-4339 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:42 | src/write_output.F:1568-1575 | 1590-1597 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:42 | src/write_output.F:1691-1693 | 1713-1715 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:47 | src/write_output.F:537-563 | 538-579 | 일부 삭제/치환 unknown; 내용 변경 포함 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:47 | src/write_output.F:710-714 | 726-730 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:49 | src/write_output.F:548-557 | 549-556 | 일부 삭제/치환 unknown; 내용 변경 포함 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:49 | src/write_output.F:716-720 | 732-742 | 일부 삭제/치환 unknown; 내용 변경 포함 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:54 | src/write_output.F:735-748 | 757-770 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:54 | src/write_output.F:775-792 | 797-814 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:55 | src/write_output.F:817-823 | 839-845 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:55 | src/write_output.F:906-913 | 928-935 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:56 | src/read_input.F:3998-4021 | 4012-4035 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:56 | src/read_input.F:4356-4384 | 4370-4398 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:57 | src/write_output.F:760-762 | 782-784 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:57 | src/write_output.F:804-806 | 826-828 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:57 | src/write_output.F:828-830 | 850-852 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:57 | src/write_output.F:920-922 | 942-944 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:63 | src/timestep.F:1184-1184 | 1188-1188 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:67 | src/write_output.F:2673-2673 | 2732-2732 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:68 | src/write_output.F:2701-2750 | 2760-2809 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:69 | src/write_output.F:2752-2760 | 2811-2819 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:70 | src/read_input.F:4421-4452 | 4435-4466 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:70 | src/read_input.F:4500-4500 | 4514-4514 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:76 | src/write_output.F:2787-2843 | 2846-2902 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:77 | src/write_output.F:2980-3103 | 3040-3163 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:79 | src/write_output.F:3403-3416 | 3463-3476 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:79 | src/write_output.F:3584-3591 | 3644-3651 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:79 | src/write_output.F:3623-3630 | 3683-3690 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:83 | src/timestep.F:1162-1162 | 1166-1166 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:84 | src/write_output.F:6343-6374 | 6432-6463 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:85 | src/write_output.F:1205-1237 | 1227-1259 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:85 | src/write_output.F:1239-1268 | 1261-1290 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:86 | src/write_output.F:1890-1898 | 1949-1957 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:92 | src/write_output.F:4226-4271 | 4315-4360 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:95 | src/write_output.F:1611-1615 | 1633-1637 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:97 | src/write_output.F:1572-1580 | 1594-1602 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:97 | src/write_output.F:1691-1693 | 1713-1715 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:39 | prep/prep.F:1276-1276 | 1276-1276 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:40 | prep/prep.F:1818-1818 | 1818-1818 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:41 | prep/prep.F:1162-1162 | 1162-1162 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:49 | prep/prep.F:7432-7432 | 7465-7465 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:49 | prep/prep.F:7444-7463 | 7477-7496 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:60 | prep/prep.F:7465-7469 | 7498-7502 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:61 | prep/prep.F:7471-7474 | 7504-7507 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:65 | prep/prep.F:7479-7482 | 7512-7515 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:70 | prep/prep.F:2850-2905 | 2854-2909 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:78 | src/read_input.F:394-394 | 398-398 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:96 | src/gwce.F:1874-1879 | 1874-1879 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:116 | src/write_output.F:1205-1260 | 1227-1282 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:117 | src/write_output.F:4322-4324 | 4411-4413 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:136 | src/write_output.F:4246-4250 | 4335-4339 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:7 | src/global.F:86-91 | 86-91 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:39 | src/nodalattr.F:1051-1051 | 1081-1081 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:61 | src/global.F:86-86 | 86-86 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:64 | src/global.F:91-91 | 91-91 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:19 | src/couple2swan.F:67-1236 | 67-1313 | 일부 삭제/치환 unknown; 내용 변경 포함 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:22 | src/read_input.F:1080-1083 | 1094-1097 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:22 | src/read_input.F:1790-1817 | 1804-1831 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:22 | src/read_input.F:2255-2261 | 2269-2275 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:24 | src/timestep.F:664-682 | 668-686 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:24 | src/timestep.F:695-725 | 699-729 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:24 | src/timestep.F:1214-1218 | 1218-1222 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:25 | src/hstart.F:325-337 | 325-337 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:25 | src/write_output.F:4969-5112 | 5058-5201 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:25 | src/netcdfio.F90:5555-7045 | 5555-7045 | 일부 삭제/치환 unknown; 내용 변경 포함 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:25 | src/netcdfio.F90:8017-8085 | 8017-8085 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:34 | src/couple2swan.F:947-947 | 947-947 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:51 | src/couple2swan.F:950-950 | 950-950 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:51 | src/couple2swan.F:965-965 | 967-967 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:54 | src/couple2swan.F:1212-1215 | 1241-1243 | 일부 삭제/치환 unknown; 내용 변경 포함 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:60 | src/couple2swan.F:112-119 | 112-119 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:60 | src/couple2swan.F:177-196 | 177-196 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:62 | src/timestep.F:695-703 | 699-707 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:63 | src/timestep.F:721-725 | 725-729 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:67 | src/couple2swan.F:67-75 | 67-75 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:67 | src/couple2swan.F:974-982 | 980-988 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:77 | src/timestep.F:664-682 | 668-686 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:86 | src/couple2swan.F:596-598 | 596-598 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:86 | src/couple2swan.F:800-835 | 800-835 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:94 | src/read_input.F:1790-1817 | 1804-1831 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:129 | src/hstart.F:325-337 | 325-337 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:133 | src/write_output.F:4969-5112 | 5058-5201 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:135 | src/netcdfio.F90:5555-5568 | 5555-5568 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:138 | src/read_input.F:1080-1083 | 1094-1097 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:139 | src/timestep.F:1214-1218 | 1218-1222 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:142 | src/netcdfio.F90:8017-8085 | 8017-8085 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-swan-coupling.md:174 | src/netcdfio.F90:8017-8085 | 8017-8085 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:7 | src/gwce.F:1181-1181 | 1181-1181 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:22 | src/timestep.F:1527-1556 | 1531-1560 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:36 | src/gwce.F:1181-1181 | 1181-1181 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:36 | src/timestep.F:1133-1133 | 1137-1137 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:45 | src/timestep.F:1527-1527 | 1531-1531 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:49 | src/timestep.F:162-162 | 162-162 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:51 | src/timestep.F:1543-1547 | 1547-1551 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:78 | src/gwce.F:1181-1181 | 1181-1181 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:40 | src/gwce.F:166-226 | 166-226 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:81 | src/gwce.F:2514-2522 | 2514-2522 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:82 | src/read_input.F:2996-2996 | 3010-3010 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:82 | src/gwce.F:1540-1543 | 1540-1543 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:83 | src/gwce.F:71-71 | 71-71 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:83 | src/gwce.F:182-182 | 182-182 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:84 | src/gwce.F:418-420 | 418-420 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:84 | src/gwce.F:2001-2017 | 2001-2017 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-transport-solver.md:6 | src/vsmy.F:1543-1543 | 1545-1545 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-transport-solver.md:6 | src/vsmy.F:1548-1553 | 1550-1555 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-transport-solver.md:20 | src/vsmy.F:1548-1553 | 1550-1555 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-transport-solver.md:21 | src/vsmy.F:1543-1543 | 1545-1545 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-transport-solver.md:59 | src/vsmy.F:1548-1553 | 1550-1555 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:27 | src/gwce.F:506-507 | 506-507 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:27 | src/gwce.F:1318-1321 | 1318-1321 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:27 | src/gwce.F:2474-2474 | 2474-2474 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:27 | src/gwce.F:2571-2573 | 2571-2573 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:76 | src/gwce.F:477-477 | 477-477 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:81 | src/gwce.F:515-516 | 515-516 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:85 | src/gwce.F:2477-2482 | 2477-2482 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/README.md:16 | src/read_input.F:2157-2157 | 2171-2171 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-foundation.md:7 | src/read_input.F:1782-1782 | 1796-1796 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-foundation.md:95 | src/read_input.F:1782-1782 | 1796-1796 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md:7 | src/read_input.F:1782-1782 | 1796-1796 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md:55 | src/read_input.F:1782-1782 | 1796-1796 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:24 | src/read_input.F:2157-2157 | 2171-2171 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:24 | src/read_input.F:2190-2190 | 2204-2204 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:24 | src/read_input.F:2255-2261 | 2269-2275 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:24 | src/read_input.F:2430-2430 | 2444-2444 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:24 | src/read_input.F:2706-2706 | 2720-2720 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:24 | src/read_input.F:2884-2884 | 2898-2898 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:24 | src/read_input.F:2975-2975 | 2989-2989 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:27 | src/owiwind.F:184-184 | 184-184 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:27 | src/owiwind.F:269-269 | 269-269 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:29 | src/constants.F90:54-54 | 54-54 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:36 | src/read_input.F:2706-2706 | 2720-2720 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:61 | src/read_input.F:2157-2157 | 2171-2171 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:85 | src/owiwind.F:184-184 | 184-184 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:133 | src/constants.F90:54-54 | 54-54 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md:157 | src/read_input.F:2430-2430 | 2444-2444 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:38 | src/read_input.F:1705-1731 | 1719-1745 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:42 | src/read_input.F:6282-6463 | 6320-6501 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:43 | src/timestep.F:1517-1560 | 1521-1564 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:47 | src/read_input.F:3410-3436 | 3424-3450 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:50 | src/read_input.F:3450-3456 | 3464-3470 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:50 | src/global.F:387-387 | 395-395 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:50 | src/global.F:1045-1045 | 1053-1053 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:64 | src/read_input.F:3431-3456 | 3445-3470 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:64 | src/read_input.F:3485-3497 | 3499-3511 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:66 | src/mesh.F:1822-1834 | 1822-1834 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:66 | src/read_input.F:3493-3496 | 3507-3510 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:66 | src/gwce.F:1644-1649 | 1644-1649 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:73 | src/gwce.F:1638-1650 | 1638-1650 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:77 | src/read_input.F:3410-3436 | 3424-3450 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:77 | src/read_input.F:3450-3456 | 3464-3470 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:88 | src/read_input.F:6282-6463 | 6320-6501 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:98 | src/read_input.F:6429-6455 | 6467-6493 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:106 | src/hstart.F:1529-1532 | 1534-1537 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:106 | src/timestep.F:1547-1555 | 1551-1559 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:110 | src/timestep.F:1507-1562 | 1511-1566 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:112 | src/read_input.F:3347-3354 | 3361-3368 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:123 | src/timestep.F:1501-1503 | 1505-1507 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:123 | src/timestep.F:1536-1536 | 1540-1540 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:137 | src/timestep.F:1541-1555 | 1545-1559 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:137 | src/hstart.F:1525-1532 | 1530-1537 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:142 | src/read_input.F:3349-3349 | 3363-3363 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:142 | src/read_input.F:3371-3383 | 3385-3397 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:143 | src/read_input.F:3429-3436 | 3443-3450 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:143 | src/read_input.F:3433-3433 | 3447-3447 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:143 | src/gwce.F:1644-1649 | 1644-1649 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:144 | src/timestep.F:251-259 | 251-259 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:144 | src/read_input.F:2541-2541 | 2555-2555 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:163 | src/timestep.F:1517-1556 | 1521-1560 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:163 | src/timestep.F:1520-1521 | 1524-1525 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:163 | src/gwce.F:1638-1650 | 1638-1650 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:48 | src/read_input.F:1703-1731 | 1717-1745 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:48 | src/read_input.F:3335-3349 | 3349-3363 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:49 | src/read_input.F:3431-3441 | 3445-3455 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:49 | src/gwce.F:1638-1649 | 1638-1649 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:63 | src/mesh.F:1822-1834 | 1822-1834 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:63 | src/read_input.F:3431-3456 | 3445-3470 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:63 | src/read_input.F:3485-3497 | 3499-3511 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:71 | src/read_input.F:1717-1731 | 1731-1745 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:71 | src/read_input.F:3431-3435 | 3445-3449 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:71 | src/read_input.F:3485-3497 | 3499-3511 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:72 | src/gwce.F:1638-1649 | 1638-1649 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:123 | src/gwce.F:1638-1649 | 1638-1649 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:128 | src/read_input.F:2894-2902 | 2908-2916 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:128 | src/timestep.F:257-258 | 257-258 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:128 | src/timestep.F:301-308 | 301-308 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:128 | src/gwce.F:1638-1651 | 1638-1651 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:130 | src/read_input.F:3628-3632 | 3642-3646 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:130 | src/read_input.F:3757-3761 | 3771-3775 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:130 | src/read_input.F:4143-4148 | 4157-4162 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:130 | src/read_input.F:4217-4222 | 4231-4236 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:130 | src/read_input.F:4534-4537 | 4548-4551 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:143 | src/gwce.F:1638-1649 | 1638-1649 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:167 | src/timestep.F:1543-1555 | 1547-1559 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:220 | src/read_input.F:1705-1731 | 1719-1745 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:220 | src/read_input.F:3344-3497 | 3358-3511 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:220 | src/read_input.F:6282-6463 | 6320-6501 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:221 | src/gwce.F:1638-1650 | 1638-1650 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:222 | src/timestep.F:251-258 | 251-258 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:222 | src/timestep.F:1517-1562 | 1521-1566 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:223 | src/hstart.F:1525-1532 | 1530-1537 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:250 | src/mesh.F:1822-1834 | 1822-1834 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:250 | src/read_input.F:3493-3496 | 3507-3510 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:254 | src/read_input.F:6282-6463 | 6320-6501 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:305 | src/gwce.F:1644-1649 | 1644-1649 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:310 | src/timestep.F:1547-1548 | 1551-1552 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:310 | src/hstart.F:1525-1532 | 1530-1537 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:315 | src/gwce.F:1642-1649 | 1642-1649 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:333 | src/timestep.F:251-258 | 251-258 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:335 | src/read_input.F:2534-2543 | 2548-2557 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:335 | src/read_input.F:3436-3436 | 3450-3450 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:335 | src/read_input.F:3493-3496 | 3507-3510 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:335 | src/timestep.F:257-258 | 257-258 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:335 | src/gwce.F:1642-1649 | 1642-1649 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:337 | src/gwce.F:1642-1644 | 1642-1644 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:337 | src/timestep.F:1532-1535 | 1536-1539 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:339 | src/timestep.F:257-258 | 257-258 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:339 | src/gwce.F:1642-1649 | 1642-1649 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:346 | src/read_input.F:3431-3456 | 3445-3470 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:346 | src/read_input.F:3485-3497 | 3499-3511 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:346 | src/gwce.F:1638-1649 | 1638-1649 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:355 | src/read_input.F:3485-3497 | 3499-3511 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:356 | src/gwce.F:1642-1649 | 1642-1649 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:368 | src/read_input.F:1705-1731 | 1719-1745 | 생존 줄 주소 대응 |
| models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:368 | src/read_input.F:3410-3444 | 3424-3458 | 생존 줄 주소 대응 |

## 파일 소속 없는 symbol 참조 대조

2,200행 중 symbol-kind 전체를 추가/삭제 코드의 식별자 및 변경 hunk의 routine/module 이름과 대소문자 무시 완전 일치로 대조했다. 일반 주석·문자열은 제외하고 SWAN !ADC/!NADC 표식은 코드 후보로 취급했다. 이 절의 P는 **같은 식별자가 나타난다는 후보 매칭**으로 파일 소속/같은 로직을 확정하지 않는다. 명시적인 Apply3DBottomFriction anchor만 N, 빌드 변경은 X다. 미매칭 symbol은 이 제한된 diff에서 관련 지점을 식별하지 못한 것으로 남기며 영향 없음을 보증하지 않는다.

| SHA · 파일 | CSV행 | 노트 | 심볼 | 참조 판정 |
|---|---:|---|---|---|
| 69f5fbba209e · src/gwce.F | 579 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:21 | GWCE_New | POSSIBLY_IMPACTING |
| 8c547d26c19b · src/mesh.F | 1600 | models/ADCIRC/source-analysis/adcirc_asgs_operational_system.md:81 | ANGLE | POSSIBLY_IMPACTING |
| e65ef6063673 · src/cstart.F | 144 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:62 | IDEN | POSSIBLY_IMPACTING |
| e65ef6063673 · src/cstart.F | 1148 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:77 | INPUTDIR | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 144 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:62 | IDEN | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 440 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:90 | initOutput3D | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 484 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:154 | RUNDES | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 485 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:154 | RUNID | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 486 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:154 | AGRID | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 507 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:181 | initOutput3D | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 604 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:37 | DTDP | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 662 | models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:88 | DTDP | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 674 | models/ADCIRC/source-analysis/adcirc-hotstart.md:15 | TimeLoc | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 723 | models/ADCIRC/source-analysis/adcirc-hotstart.md:130 | TimeLoc | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 726 | models/ADCIRC/source-analysis/adcirc-hotstart.md:144 | HOTSTART | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 727 | models/ADCIRC/source-analysis/adcirc-hotstart.md:144 | TimeLoc | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 728 | models/ADCIRC/source-analysis/adcirc-hotstart.md:144 | ITHS | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 731 | models/ADCIRC/source-analysis/adcirc-hotstart.md:154 | TimeLoc | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 733 | models/ADCIRC/source-analysis/adcirc-hotstart.md:155 | TIMELOC | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 734 | models/ADCIRC/source-analysis/adcirc-hotstart.md:156 | TimeLoc | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 739 | models/ADCIRC/source-analysis/adcirc-hotstart.md:168 | TimeLoc | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 855 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:84 | TIMELOC | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 1035 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:76 | initOutput3D | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 1105 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:29 | MNPROC | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 1121 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:51 | RUNDES | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 1122 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:51 | RUNID | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 1123 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:51 | AGRID | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 1132 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:56 | MYPROC | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 1148 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:77 | INPUTDIR | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 1219 | models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:43 | AGRID | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 1311 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:164 | HOTSTART | POSSIBLY_IMPACTING |
| e65ef6063673 · src/hstart.F | 1314 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:172 | TIMELOC | POSSIBLY_IMPACTING |
| e65ef6063673 · src/netcdfio.F90 | 137 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:44 | NFEN | POSSIBLY_IMPACTING |
| e65ef6063673 · src/netcdfio.F90 | 144 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:62 | IDEN | POSSIBLY_IMPACTING |
| e65ef6063673 · src/netcdfio.F90 | 710 | models/ADCIRC/source-analysis/adcirc-hotstart.md:100 | readNetCDFHotstart3D | POSSIBLY_IMPACTING |
| e65ef6063673 · src/netcdfio.F90 | 1037 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:78 | NFEN | POSSIBLY_IMPACTING |
| e65ef6063673 · src/nodalattr.F | 1393 | models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:30 | Apply2DBottomFriction | POSSIBLY_IMPACTING |
| e65ef6063673 · src/nodalattr.F | 1396 | models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:30 | Apply3DBottomFriction | NOTE_IMPACTING |
| e65ef6063673 · src/read_input.F | 360 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:45 | READ_INPUT_3D | POSSIBLY_IMPACTING |
| e65ef6063673 · src/read_input.F | 494 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:174 | READ_INPUT_3D | POSSIBLY_IMPACTING |
| e65ef6063673 · src/vsmy.F | 144 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:62 | IDEN | POSSIBLY_IMPACTING |
| e65ef6063673 · src/vsmy.F | 224 | models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:20 | CBaroclinic | POSSIBLY_IMPACTING |
| e65ef6063673 · src/vsmy.F | 910 | models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:31 | CBaroclinic | POSSIBLY_IMPACTING |
| e65ef6063673 · src/write_output.F | 144 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:62 | IDEN | POSSIBLY_IMPACTING |
| e65ef6063673 · src/write_output.F | 441 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:90 | writeOutput3D | POSSIBLY_IMPACTING |
| e65ef6063673 · src/write_output.F | 508 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:181 | writeOutput3D | POSSIBLY_IMPACTING |
| e65ef6063673 · src/write_output.F | 674 | models/ADCIRC/source-analysis/adcirc-hotstart.md:15 | TimeLoc | POSSIBLY_IMPACTING |
| e65ef6063673 · src/write_output.F | 723 | models/ADCIRC/source-analysis/adcirc-hotstart.md:130 | TimeLoc | POSSIBLY_IMPACTING |
| e65ef6063673 · src/write_output.F | 727 | models/ADCIRC/source-analysis/adcirc-hotstart.md:144 | TimeLoc | POSSIBLY_IMPACTING |
| e65ef6063673 · src/write_output.F | 731 | models/ADCIRC/source-analysis/adcirc-hotstart.md:154 | TimeLoc | POSSIBLY_IMPACTING |
| e65ef6063673 · src/write_output.F | 733 | models/ADCIRC/source-analysis/adcirc-hotstart.md:155 | TIMELOC | POSSIBLY_IMPACTING |
| e65ef6063673 · src/write_output.F | 734 | models/ADCIRC/source-analysis/adcirc-hotstart.md:156 | TimeLoc | POSSIBLY_IMPACTING |
| e65ef6063673 · src/write_output.F | 739 | models/ADCIRC/source-analysis/adcirc-hotstart.md:168 | TimeLoc | POSSIBLY_IMPACTING |
| e65ef6063673 · src/write_output.F | 855 | models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:84 | TIMELOC | POSSIBLY_IMPACTING |
| e65ef6063673 · src/write_output.F | 1105 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:29 | MNPROC | POSSIBLY_IMPACTING |
| e65ef6063673 · src/write_output.F | 1132 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:56 | MYPROC | POSSIBLY_IMPACTING |
| e65ef6063673 · src/write_output.F | 1180 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:115 | collectFullDomainArray | POSSIBLY_IMPACTING |
| e65ef6063673 · src/write_output.F | 1184 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:126 | collectFullDomainArray | POSSIBLY_IMPACTING |
| e65ef6063673 · src/write_output.F | 1191 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:136 | writeOutArrayNetCDF | POSSIBLY_IMPACTING |
| e65ef6063673 · src/write_output.F | 1314 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:172 | TIMELOC | POSSIBLY_IMPACTING |
| bf6957a976d9 · src/nodalattr.F | 137 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:44 | NFEN | NON_IMPACTING |
| bf6957a976d9 · src/nodalattr.F | 1037 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:78 | NFEN | NON_IMPACTING |
| bf6957a976d9 · src/nodalattr.F | 1393 | models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:30 | Apply2DBottomFriction | NON_IMPACTING |
| bf6957a976d9 · src/nodalattr.F | 1396 | models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:30 | Apply3DBottomFriction | NON_IMPACTING |
| bf6957a976d9 · src/nodalattr.F | 1507 | models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:27 | IFNLFA | NON_IMPACTING |
| bf6957a976d9 · src/nodalattr.F | 1572 | models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:121 | IFNLFA | NON_IMPACTING |
| bf6957a976d9 · src/timestep.F | 137 | models/ADCIRC/source-analysis/adcirc-3d-mode.md:44 | NFEN | NON_IMPACTING |
| bf6957a976d9 · src/timestep.F | 1037 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:78 | NFEN | NON_IMPACTING |
| e5995720925d · prep/prep.F | 1106 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:29 | NPROC | POSSIBLY_IMPACTING |
| e5995720925d · prep/prep.F | 1126 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:52 | NPROC | POSSIBLY_IMPACTING |
| e5995720925d · prep/prep.F | 1130 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:55 | NPROC | POSSIBLY_IMPACTING |
| e5995720925d · prep/prep.F | 1133 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:56 | NPROC | POSSIBLY_IMPACTING |
| bdc531653bef · src/write_output.F | 386 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:63 | initOutput2D | POSSIBLY_IMPACTING |
| bdc531653bef · src/write_output.F | 387 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:63 | writeOutput2D | POSSIBLY_IMPACTING |
| bdc531653bef · src/write_output.F | 416 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:79 | initOutput2D | POSSIBLY_IMPACTING |
| bdc531653bef · src/write_output.F | 505 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:181 | initOutput2D | POSSIBLY_IMPACTING |
| bdc531653bef · src/write_output.F | 506 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:181 | writeOutput2D | POSSIBLY_IMPACTING |
| bdc531653bef · src/write_output.F | 987 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:21 | writeOutput2D | POSSIBLY_IMPACTING |
| bdc531653bef · src/write_output.F | 991 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:23 | initOutput2D | POSSIBLY_IMPACTING |
| daae7d9f9edc · src/nodalattr.F | 363 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51 | ReadNodalAttr | POSSIBLY_IMPACTING |
| daae7d9f9edc · src/nodalattr.F | 496 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:175 | ReadNodalAttr | POSSIBLY_IMPACTING |
| 976fc5b6cafb · prep/prep.F | 1324 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:200 | PREP15 | POSSIBLY_IMPACTING |
| 976fc5b6cafb · prep/prep.F | 1325 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:200 | SWANTimeControl | POSSIBLY_IMPACTING |
| 976fc5b6cafb · prep/presizes.F | 1319 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:186 | RunStartDateTime | POSSIBLY_IMPACTING |
| 976fc5b6cafb · prep/presizes.F | 1321 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:193 | RunStartDateTime | POSSIBLY_IMPACTING |
| 976fc5b6cafb · prep/presizes.F | 1325 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:200 | SWANTimeControl | POSSIBLY_IMPACTING |
| 976fc5b6cafb · prep/presizes.F | 1329 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:201 | RunStartDateTime | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/couple2swan.F | 1256 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:34 | PADCSWAN_INIT | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/couple2swan.F | 1262 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:40 | PADCSWAN_INIT | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/couple2swan.F | 1266 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:51 | SWAN_DT | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/couple2swan.F | 1306 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:159 | SWAN_DT | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/couple2swan.F | 1313 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:170 | SWAN_DT | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/couple2swan.F | 1319 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:186 | RunStartDateTime | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/couple2swan.F | 1321 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:193 | RunStartDateTime | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/couple2swan.F | 1327 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:201 | SwanTimeStep | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/couple2swan.F | 1328 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:201 | PADCSWAN_INIT | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/couple2swan.F | 1329 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:201 | RunStartDateTime | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/couple2swan.F | 1330 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:201 | PADCSWAN_RUN | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/couple2swan.F | 1331 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:201 | SWMAIN | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/couple2swan.F | 1333 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:227 | SWAN_MTC | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/couple2swan.F | 1335 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:227 | SWAN_MTC | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/global.F | 1319 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:186 | RunStartDateTime | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/global.F | 1321 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:193 | RunStartDateTime | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/global.F | 1329 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:201 | RunStartDateTime | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/nodalattr.F | 363 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:51 | ReadNodalAttr | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/nodalattr.F | 496 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:175 | ReadNodalAttr | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/nodalattr.F | 524 | models/ADCIRC/source-analysis/adcirc-fort15-checklist-v1.md:41 | NABOUT | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/nodalattr.F | 525 | models/ADCIRC/source-analysis/adcirc-fort15-checklist-v1.md:42 | NSCREEN | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/nodalattr.F | 527 | models/ADCIRC/source-analysis/adcirc-fort15-checklist-v1.md:54 | NSCREEN | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/nodalattr.F | 979 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:45 | readNodalAttrXDMF | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/nodalattr.F | 1132 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:56 | MYPROC | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/nodalattr.F | 1192 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:141 | nabout | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/read_input.F | 359 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:45 | READ_INPUT | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/read_input.F | 375 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:54 | READ_INPUT | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/read_input.F | 493 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:174 | READ_INPUT | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/read_input.F | 1150 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:78 | READ_INPUT | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/read_input.F | 1193 | models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:142 | ECHO | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/read_input.F | 1319 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:186 | RunStartDateTime | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/read_input.F | 1321 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:193 | RunStartDateTime | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/read_input.F | 1325 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:200 | SWANTimeControl | POSSIBLY_IMPACTING |
| 976fc5b6cafb · src/read_input.F | 1329 | models/ADCIRC/source-analysis/adcirc-swan-coupling.md:201 | RunStartDateTime | POSSIBLY_IMPACTING |

## 산출물 검증

45행 CSV의 (commit_sha, changed_file)은 commit-details 전체 파일 집합과 일대일 일치하며, 14 SHA/31 고유 파일을 포함한다. 위 원장은 변경 파일 매칭 CSV 원행을 누락 없이 포함한다. models/와 위키 노트에 쓰기 작업을 수행하지 않았다. 산출 후 manifest 60개 원자료 bytes/SHA-256 재확인 통과. ADCIRC의 raw 제외 Markdown 64개는 산출물 생성 전후 SHA-256이 모두 동일하다. commit 누적 줄 대응과 compare 전체 diff의 생존 인용점 25,643회 대조도 일치했다. 파일 소속 없는 symbol 후보 대조는 121 참조×변경 단위를 추가 기록했다.
