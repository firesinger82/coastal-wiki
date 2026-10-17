# FUNWAVE-TVD 2.1 예제·참고문헌과 현재 코드 대조

## 1 요약

분류별 개수: A 5, B 12, C 25, D 3, E 2, F 0, H 102, X 0. 일치 75. 합계 224행이다. §5의 최종 분류는 일치가 아닌 149행이다.

p.43–77의 35쪽을 대조했다.
같은 여섯 예제의 3.0 문서 차이를 §2.6에 적었다.
참고문헌 56개는 FV2-150–205로 식별했다.
개수는 표의 고유 행 ID를 센 값이다.
같은 원인이 문서와 노트 양쪽에 나타나면 각각의 서술을 별도 행으로 셌다.

SPONGE_ON은 제공된 코드 이력에서 입력 스위치로 구현되지 않았다(FV2-049).
INI_SOL은 예제의 LAGTIME을 읽지 않는다(FV2-047).
점성 쇄파의 누락 기본값은 2019년 변경 때문에 2.1 예제 설명과 다르다(FV2-301).
현재 TVD는 두 최소 수심을 MIN으로 병합한다(FV2-306).
현재 GPU는 두 최소 수심을 MAX로 병합한다(FV2-306).
초기 고립파 중심과 직렬 SLOPE 지형의 두 차이는 근거가 강한 코드 결함 후보다(FV2-136·304).
이 두 후보는 정적 분석 결과다.

이 보고서는 AI가 원자료를 대조하여 작성한 분석이다.
대상 문서는 `funwave_tvd_2.1_manual.pdf p.43–77`이다.
PDF 쪽 번호와 인쇄 쪽 번호는 이 범위에서 같다.
현재 TVD 코드는 `models/FUNWAVE/raw/source_code/FUNWAVE-TVD/`의 작업 트리이다.
현재 GPU 코드는 `models/FUNWAVE/raw/source_code/FUNWAVE-GPU/`의 작업 트리이다.
GPU 원자료의 etauv_solver_gpu.F·mod_cuda.F·Makefile_cuda에는 공개 커밋과 다른 로컬 수정이 있다.
GPU 인용은 공개 HEAD라고 가정한 코드가 아니라 현재 작업 트리의 대응 경로다.
이 보고서의 `TVD/`와 `GPU/`는 각각 위 경로를 뜻한다.
코드 인용의 `src/`는 별도 표시가 없으면 `TVD/src/`를 뜻한다.
과거 코드 인용은 `_staging/recovery/extract/FUNWAVE/external/tvd`에서 `git show`로 읽은 원문이다.
과거 코드 인용은 `HASH:src/파일:줄` 형식을 쓴다.

판정의 `일치`는 입력 이름·형식·적용 조건 또는 구현 경로를 정적으로 확인했다는 뜻이다.
입력 예제의 수치는 사용자가 지정한 값이다.
이 보고서는 예제 수치를 코드 기본값으로 해석하지 않는다.
예제 결과와 실험 배치는 H로 분류한다.
이 보고서는 모델을 실행하지 않는다.
이 보고서는 수치 결과와 물리 타당성을 재검증하지 않는다.

## 2 대조 표

### 2.1 판독 범위

대상 범위의 35쪽 이미지를 직접 열었다.
다음 표의 쪽 수는 p.43부터 p.77까지 포함하여 센 값이다.
이 범위에는 빈 쪽이 없다.
그림만 있는 쪽도 아래 표에 포함했다.
반복 입력은 §2.3에서 같은 키의 행에 모든 출현 위치와 값을 모았다.
이 묶음은 입력 한 줄을 생략한다는 뜻이 아니다.
§5의 개수는 반복 출현 횟수가 아니라 고유 행 ID 수이다.

| funwave_tvd_2.1_manual.pdf 쪽 | 확인한 내용 | 대조 위치 |
|---|---|---|
| p.43 | 중첩 읽기 예시 끝, 결합 파일, 출력 설명, 5장 서문, 해빈 예제 설명 | §2.2, §2.4 |
| p.44 | 해빈 결과 설명, 해빈 입력 앞부분 | §2.3, §2.4 |
| p.45 | 해빈 입력 뒷부분, 불규칙파 예제 설명 시작 | §2.3, §2.4 |
| p.46 | 그림 3과 캡션만 있음 | FV2-106 |
| p.47 | 그림 4와 캡션만 있음 | FV2-107 |
| p.48 | 그림 5와 캡션만 있음 | FV2-108 |
| p.49 | 불규칙파 절차·결과, 식 (79), 입력 앞부분 | §2.3, §2.4 |
| p.50 | 그림 6·7과 캡션만 있음 | FV2-114, FV2-115 |
| p.51 | 그림 8과 캡션만 있음 | FV2-116 |
| p.52 | 불규칙파 입력 계속 | §2.3 |
| p.53 | 불규칙파 입력 끝·후처리, 천퇴 예제 설명 | §2.3, §2.4 |
| p.54 | 천퇴 후처리·결과 설명, 그림 9, 천퇴 입력 시작 | §2.3, §2.4 |
| p.55 | 그림 10과 캡션만 있음 | FV2-122 |
| p.56 | 천퇴 입력 계속 | §2.3 |
| p.57 | 천퇴 입력 끝, 원뿔섬 설명, 원뿔섬 입력 시작 | §2.3, §2.4 |
| p.58 | 그림 11·12와 캡션만 있음 | FV2-124, FV2-125 |
| p.59 | 그림 13, 표 1, 원뿔섬 입력 계속 | §2.3, FV2-126, FV2-127 |
| p.60 | 그림 14, 원뿔섬 입력 계속 | §2.3, FV2-128 |
| p.61 | 그림 15·16과 캡션만 있음 | FV2-129, FV2-130 |
| p.62 | 원뿔섬 입력 끝·관측점 파일 설명, 천해붕 예제 설명 시작 | §2.3, §2.4 |
| p.63 | 그림 17과 캡션만 있음 | FV2-133 |
| p.64 | 그림 18과 캡션만 있음 | FV2-134 |
| p.65 | 그림 19, 천해붕 설정·결과 설명 | §2.4 |
| p.66 | 그림 20과 캡션만 있음 | FV2-138 |
| p.67 | 그림 21과 캡션만 있음 | FV2-139 |
| p.68 | 천해붕 결과 설명 끝, 천해붕 입력 앞부분 | §2.3, §2.4 |
| p.69 | 천해붕 입력 끝·후처리, 중첩 예제 설명·디렉터리 | §2.3, §2.4 |
| p.70 | 중첩 절차, Grid_A 입력 앞부분 | §2.3, §2.4 |
| p.71 | Grid_A 입력 끝, Grid_B 입력 앞부분 | §2.3 |
| p.72 | Grid_B 입력 끝, 참고문헌 시작 | §2.3, §2.5 |
| p.73 | 그림 22와 캡션만 있음 | FV2-146 |
| p.74 | 참고문헌 | §2.5 |
| p.75 | 참고문헌 | §2.5 |
| p.76 | 참고문헌 | §2.5 |
| p.77 | 참고문헌 끝 | §2.5 |

현재 빌드의 좌표 조건은 `TVD/Makefile:25`의 `SPHERICAL   = false`이다.
`TVD/GNUMake/Essential/Make_Essential:123–127`은 이 설정에서 `FLAG_CARTESIAN = -DCARTESIAN`을 선택한다.
같은 파일의 `:129–130`은 병렬 설정에서 `FLAG_PARALLEL = -DPARALLEL`을 선택한다.
같은 파일의 `:208–211`은 다음 빌드 목록을 쓴다.

```make
MAIN  = main.F bc.F fluxes.F init.F io.F tridiagnal.F       \
        breaker.F derivatives.F dispersion.F etauv_solver.F \
        sponge.F sources.F masks.F parallel.F statistics.F \
        wavemaker.F mixing.F nesting.F misc.F samples.F\
```

`fluxes_21v.F`와 `fluxes_33v.F`는 이 목록의 활성 플럭스 파일이 아니다.
이 보고서는 직교 예제에서 `CARTESIAN` 분기를 적용한다.
이 보고서는 중첩 예제에서 `CARTESIAN`을 정의하지 않는 구면 분기를 적용한다.
`COUPLING`은 Grid_B에서만 정의한다.
`MANNING`, `VESSEL`, `METEO`, `SEDIMENT`, `FOAM`은 해당 예제 입력의 필수 조건이 아니다.
`ZALPHA`를 정의하지 않은 구면 코드에서는 `Beta_ref` 입력의 적용 조건이 달라진다.
그 차이는 FV2-062에 적었다.

### 2.2 p.43의 중첩·출력 설명

| 행 ID | 문서 원문 | 코드 원문 | 판정 | 이유 |
|---|---|---|---|---|
| FV2-001 | funwave_tvd_2.1_manual.pdf p.43: `ENDDO`, `119 FORMAT(5E16.6)` | `src/nesting.F:114` `119      FORMAT(5E16.6)` | 일치 | 형식 지정자는 같다. 앞쪽 p.42에서 시작한 발췌의 `ENDDO`를 독립 실행문으로 해석하지 않는다. |
| FV2-002 | funwave_tvd_2.1_manual.pdf p.43: `where N_COUPLING_EAST is Num of points at the EAST boundary.` | `src/nesting.F:79` `READ(11,*) N_COUPLING_EAST,J_START_EAST`; `:98` `IF(N_COUPLING_EAST.GT.0)THEN` | 일치 | 동쪽 지점 수와 읽기 조건이 대응한다. |
| FV2-003 | funwave_tvd_2.1_manual.pdf p.43: `Specify the file of coupling data in input.txt`; `COUPLING_FILE = coupling.txt`; `! if do coupling, have to set -DCOUPLING in Makefile` | `src/io.F:3270` `# if defined (COUPLING)`; `:3280` `CALL READ_STRING(COUPLING_FILE,FILE_NAME,'COUPLING_FILE',ierr)`; `src/nesting.F:71` `OPEN(11,FILE=TRIM(COUPLING_FILE))` | 일치 | 문자열을 그대로 파일 경로로 쓴다. `TVD/Makefile:11`의 `#  FLAG_1  = -DCOUPLING`은 현재 주석 상태다. Grid_B용으로 활성화해야 한다. |
| FV2-004 | funwave_tvd_2.1_manual.pdf p.43: `The output files are saved in the result directory defined by RESULT_FOLDER in input.txt.` | `src/io.F:3314` `CALL READ_STRING(RESULT_FOLDER,FILE_NAME,'RESULT_FOLDER',ierr)`; `:3316` `RESULT_FOLDER = './output/'`; `:4327` `FDIR=TRIM(RESULT_FOLDER)` | 일치 — 경로 조건부 | 지정 폴더를 출력 접두 경로로 쓴다. 폴더 기본값은 문서의 이 문장이 제시한 값이 아니다. 끝의 경로 구분자 조건은 FV2-314에 적었다. |
| FV2-005 | funwave_tvd_2.1_manual.pdf p.43: `eta_0001, eta_0002, ....` | `src/io.F:4347` `itmp1=mod(icount/10000,10)`; `:4357` `write(file_name(5:5),'(I1)')itmp5   !ykchoi`; `:4372` `TMP_NAME = TRIM(FDIR)//'eta_'//TRIM(FILE_NAME)` | 불일치 — B | 현재 장 출력 순번은 다섯 자리다. 문서가 저장된 커밋의 코드도 다섯 자리다. 이력 근거는 §5에 적었다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-006 | funwave_tvd_2.1_manual.pdf p.43: `The format and read/write algorithm are consistent with a depth file.` | `src/io.F:4919` `DO J=Nghost+1,Nloc-Nghost,OUTPUT_RES`; `:4920` `WRITE(1,FORMAT_LEN)(real(PHI(I,J)),I=Nghost+1,Mloc-Nghost,OUTPUT_RES)` | 일치 | 기본 `OUTPUT_RES=1`의 ASCII 출력은 행마다 x 방향 자료를 쓴다. `DEBUG`, 출력 간격 변경, 병렬 바이너리 출력은 별도 조건이다. |
| FV2-007 | funwave_tvd_2.1_manual.pdf p.43: `sta_0001, sta_0002 ....` | `src/io.F:3869` `write(file_name(1:4),'(I4.4)') i`; `:3870` `TMP_NAME = TRIM(FDIR)//'sta_'//TRIM(FILE_NAME)` | 일치 | 관측점 파일은 네 자리 관측점 순번을 쓴다. 이 순번은 장 출력 시각 순번과 다르다. |
| FV2-008 | funwave_tvd_2.1_manual.pdf p.43: `The NetCDF output format is under development.` | `src/io.F:4873` `SELECT CASE (TRIM(FIELD_IO_TYPE))`; `:4874` `CASE ('ASCII' , 'ascii')`; `:4876` `CASE ('BINARY' , 'binary' )` `src/io.F:3330–3332·4873–4880`의 병렬 선택기는 ASCII·BINARY와 기본 ASCII 분기를 둔다. 직렬 경로 `:4894–4920`는 ASCII를 쓴다. | 일치 | 일치는 NetCDF 출력이 이 선택기에 구현되어 있지 않다는 범위다. 2.1의 개발 중 문장을 NetCDF 지원으로 읽지 않는다. 현재 병렬 장 출력은 ASCII·BINARY이고 직렬 장 출력은 ASCII다(FV2-315). [10-18 결론 검증 정정] [10-18 결론 검증 보완] |

### 2.3 입력 블록의 모든 키와 값

문서 출현 위치는 다음 사례 이름으로 구분한다.
해빈은 §5.1이다.
불규칙파는 §5.2이다.
천퇴는 §5.3이다.
원뿔섬은 §5.4이다.
천해붕은 §5.5이다.
Grid_A와 Grid_B는 §5.6의 큰 영역과 중첩 영역이다.
입력 블록의 `! DEPTH`, `! DIMENSION`, `! TIME`, `! GRID`, `! WAVEMAKER`, `! SPONGE LAYER`, `! PHYSICS`, `! NUMERICS`, `! WET-DRY`, `! OUTPUT`, `! COUPLING`은 주석 표제다.
`src/mod_input.F:290–292`의 `LOCATION = index(TEXT_READ,com_char)`, `if(LOCATION == 0)LOCATION = len_trim(TEXT_READ)+1`, `TMPV = TEXT_READ(1:LOCATION-1)`은 `!` 뒤의 표제와 설명을 제거한다.
따라서 p.44에서 `DX`와 `DY` 위에 쓴 `TIME`은 입력 구문에 영향을 주지 않는다.
`src/mod_input.F:297`의 `IF(ADJUSTL(TRIM(TMPV_NEXT)) == TRIM(MatchCharacter))THEN`은 키를 대소문자까지 비교한다.
`src/mod_input.F:340–345`는 `DotLocation = index(VREAD,".")`의 결과로 실수와 정수를 구분한다.
예제의 격자 수와 관측점 수는 정수 형식이다.
예제의 실수 값은 모두 소수점을 포함한다.
예제의 논리 값은 대문자 `T` 또는 `F`이다.
`src/mod_input.F:214–215`의 `LOGICAL_VAL = .FALSE.`, `IF(VAL_READ(1:1) == 'T') LOGICAL_VAL = .TRUE.`가 이 값을 읽는다.

#### 2.3.1 지형·격자·시간

| 행 ID | 문서 원문과 출현 위치 | 코드 원문 | 판정 | 이유 |
|---|---|---|---|---|
| FV2-020 | funwave_tvd_2.1_manual.pdf p.44·49: `DEPTH_TYPE = SLOPE`; p.54·57·68: `DEPTH_TYPE = DATA`; p.70·71: `DEPTH_TYPE = FLAT` | `src/io.F:464` `CALL READ_STRING(DEPTH_TYPE,FILE_NAME,'DEPTH_TYPE',ierr)`; `:485` `IF(DEPTH_TYPE(1:3)=='DAT')THEN`; `:494` `IF(DEPTH_TYPE(1:3)=='FLA')THEN`; `:518` `IF(DEPTH_TYPE(1:3)=='SLO')THEN` | 일치 | 세 문자열은 해당 분기에 들어간다. |
| FV2-021 | funwave_tvd_2.1_manual.pdf p.54·57: `DEPTH_FILE = ../input/depth.txt`; p.68: `DEPTH_FILE = ../input/depth_wkshop.txt` | `src/io.F:486` `CALL READ_STRING(DEPTH_FILE,FILE_NAME,'DEPTH_FILE',ierr)` | 일치 | DATA 분기는 파일 이름을 문자열로 읽는다. 파일 내용과 실험 지형의 동일성은 이 입력 이름 판정에 포함하지 않는다. |
| FV2-022 | funwave_tvd_2.1_manual.pdf p.44: `DEPTH_FLAT = 0.36`; p.49: `DEPTH_FLAT = 0.47`; p.70·71: `DEPTH_FLAT = 10.0` | `src/io.F:495` 및 `:519` `CALL READ_FLOAT(DEPTH_FLAT,FILE_NAME,'DEPTH_FLAT',ierr)`; `src/init.F:763` `Depth(I,J) = Depth_FLat` | 일치 | SLOPE와 FLAT는 같은 실수 키를 읽는다. |
| FV2-023 | funwave_tvd_2.1_manual.pdf p.44: `SLP = 0.0292`; p.52: `SLP = 0.05` | `src/io.F:534` `CALL READ_FLOAT(SLP,FILE_NAME,'SLP',ierr)`; `src/init.F:768` `Depth(I,J) = Depth_Flat-SLP*(I-(INT(Xslp/DX)+1+Ibeg))*DX` | 일치 | 양의 경사는 오른쪽으로 정수심을 감소시킨다. `0.0292`는 본문의 `1:34.26`을 반올림한 설정이다. |
| FV2-024 | funwave_tvd_2.1_manual.pdf p.44: `Xslp = 55.0`; p.52: `Xslp = 10.0` | `src/io.F:549` `CALL READ_FLOAT(Xslp,FILE_NAME,'Xslp',ierr)`; `src/init.F:767` `DO I=INT(Xslp/DX)+1+Ibeg,Iend` | 일치 | 키와 실수 형식은 같다. 경사 시작점을 격자에 놓는 실제 식은 FV2-304에 따로 적었다. |
| FV2-025 | funwave_tvd_2.1_manual.pdf p.44: `Mglob = 3001`; p.52: `Mglob = 500`; p.54: `Mglob = 600`; p.59: `Mglob = 702`; p.68: `Mglob = 501` | `src/io.F:248` `CALL READ_INTEGER(Mglob,FILE_NAME,'Mglob',ierr)` | 일치 | 각 값은 정수다. Grid_A·Grid_B 발췌에는 이 필수 키가 없다. 그 누락은 FV2-310에 분리했다. |
| FV2-026 | funwave_tvd_2.1_manual.pdf p.44·52: `Nglob = 3`; p.54: `Nglob = 200`; p.59: `Nglob = 602`; p.68: `Nglob = 261` | `src/io.F:263` `CALL READ_INTEGER(Nglob,FILE_NAME,'Nglob',ierr)` | 일치 | 세 격자 행은 1차원 파형을 두는 얇은 2차원 영역의 설정이다. 키 자체가 1차원 전용 코드를 선택하지 않는다. |
| FV2-027 | funwave_tvd_2.1_manual.pdf p.52: `TOTAL_TIME = 716.0`; p.56: `TOTAL_TIME = 30.0`; p.59: `TOTAL_TIME = 25.0`; p.68: `TOTAL_TIME = 45.0`; p.70·71: `TOTAL_TIME = 400.0` | `src/io.F:603` `CALL READ_FLOAT(TOTAL_TIME,FILE_NAME,'TOTAL_TIME',ierr)`; `src/main.F:284` `DO WHILE (TIME<TOTAL_TIME)` | 일치 | 값은 종료할 모델 시각이다. 결합 초기 시각부터 추가로 이 시간만큼 계산한다는 뜻이 아니다. |
| FV2-028 | funwave_tvd_2.1_manual.pdf p.52: `PLOT_INTV = 10.0`; p.56: `PLOT_INTV = 0.02`; p.59·70·71: `PLOT_INTV = 1.0`; p.68: `PLOT_INTV = 0.2` | `src/io.F:634` `CALL READ_FLOAT(PLOT_INTV,FILE_NAME,'PLOT_INTV',ierr)`; `:97` `IF(PLOT_COUNT>=PLOT_INTV)THEN` | 일치 | 코드가 경과시간 누적값과 비교한다. |
| FV2-029 | funwave_tvd_2.1_manual.pdf p.52·59: `PLOT_INTV_STATION = 0.05`; p.56: `PLOT_INTV_STATION = 0.02`; p.68: `PLOT_INTV_STATION = 0.2`; p.70: `PLOT_INTV_STATION = 0.0`; p.71: `PLOT_INTV_STATION = 1.00` | `src/io.F:649` `CALL READ_FLOAT(PLOT_INTV_STATION,FILE_NAME,'PLOT_INTV_STATION',ierr)`; `:82` `IF(PLOT_COUNT_STATION>=PLOT_INTV_STATION)THEN` | 일치 | p.70의 `! 0.0 means make station output every time step for nesting data`는 관측점 수가 양수일 때 성립한다. 실제 파일 쓰기는 버퍼를 거친다. |
| FV2-030 | funwave_tvd_2.1_manual.pdf p.52·59·70·71: `SCREEN_INTV = 1.0`; p.56: `SCREEN_INTV = 0.1`; p.68: `SCREEN_INTV = 0.2` | `src/io.F:678` `CALL READ_FLOAT(SCREEN_INTV,FILE_NAME,'SCREEN_INTV',ierr)`; `:74` `IF(SCREEN_COUNT>=SCREEN_INTV)THEN` | 일치 | 코드가 화면 통계의 시간 간격으로 읽는다. |
| FV2-031 | funwave_tvd_2.1_manual.pdf p.44: `DX = 0.025`; p.52: `DX = 0.04`; p.56·59: `DX = 0.05`; p.68: `DX = 0.1` | `src/io.F:284` `# if defined (CARTESIAN)`; `:286` `CALL READ_FLOAT(DX,FILE_NAME,'DX',ierr)` | 일치 | 직교 분기의 길이 간격이다. |
| FV2-032 | funwave_tvd_2.1_manual.pdf p.44: `DY = 0.2`; p.52·56: `DY = 0.10`; p.60: `DY = 0.05`; p.68: `DY = 0.1` | `src/io.F:304` `CALL READ_FLOAT(DY,FILE_NAME,'DY',ierr)` | 일치 | 모든 값은 소수점을 포함한다. p.44의 큰 DY 권고는 FV2-104에서 H로 분류했다. |

#### 2.3.2 조파기

| 행 ID | 문서 원문과 출현 위치 | 코드 원문 | 판정 | 이유 |
|---|---|---|---|---|
| FV2-033 | funwave_tvd_2.1_manual.pdf p.44·56: `WAVEMAKER = WK_REG`; p.52: `WAVEMAKER = WK_TIME_SERIES`; p.60·68·70·71: `WAVEMAKER = INI_SOL` | `src/io.F:870` `CALL READ_STRING(WaveMaker,FILE_NAME,'WAVEMAKER',ierr)`; `:950` `IF(WaveMaker(1:7)=='WK_TIME')THEN`; `:1101` `IF(WaveMaker(1:7)=='INI_SOL')THEN`; `:1427` `IF(WaveMaker(1:6)=='WK_REG')THEN` | 일치 | `WK_TIME_SERIES`는 앞 일곱 글자 검사에 들어간다. |
| FV2-034 | funwave_tvd_2.1_manual.pdf p.44: `Xc_WK = 45.0`; p.52: `Xc_WK = 10.0`; p.56: `Xc_WK = 3.0` | `src/io.F:996` 및 `:1428` `CALL READ_FLOAT(Xc_WK,FILE_NAME,'Xc_WK',ierr)` | 일치 | 내부 조파원의 x 위치를 실수로 읽는다. 천퇴의 실험 좌표와 모델 좌표는 FV2-120에서 구분했다. |
| FV2-035 | funwave_tvd_2.1_manual.pdf p.44: `Tperiod = 3.33`; p.56: `Tperiod = 1.0` | `src/io.F:1458` `CALL READ_FLOAT(Tperiod,FILE_NAME,'Tperiod',ierr)` | 일치 | 규칙파 주기를 읽는다. |
| FV2-036 | funwave_tvd_2.1_manual.pdf p.44: `AMP_WK = 0.0185`; p.56: `AMP_WK = 0.0232` | `src/io.F:1473` `CALL READ_FLOAT(AMP_WK,FILE_NAME,'AMP_WK',ierr)` | 일치 | 값은 파 진폭이다. 해빈 본문의 입사 파고 4.3 cm와 이 진폭을 곧바로 같은 값으로 놓지 않는다. 3.0의 조정 설명은 §2.6에 적었다. |
| FV2-037 | funwave_tvd_2.1_manual.pdf p.44: `DEP_WK = 0.36`; p.52: `DEP_WK = 0.47`; p.56: `DEP_WK = 0.45` | `src/io.F:1025` 및 `:1488` `CALL READ_FLOAT(DEP_WK,FILE_NAME,'DEP_WK',ierr)` | 일치 | 조파원 수심을 읽는다. |
| FV2-038 | funwave_tvd_2.1_manual.pdf p.44·56: `Theta_WK = 0.0` | `src/io.F:1503` `CALL READ_FLOAT(Theta_WK,FILE_NAME,'Theta_WK',ierr)`; `src/wavemaker.F:106` `IF(Theta_WK.NE.ZERO)THEN` | 일치 | 두 규칙파는 영도 입사다. 주기 경계용 비영각 조정 조건에 들어가지 않는다. |
| FV2-039 | funwave_tvd_2.1_manual.pdf p.44·52·56: `Time_ramp = 1.0` | `src/io.F:1040` 및 `:1517` `CALL READ_FLOAT(Time_ramp,FILE_NAME,'Time_ramp',ierr)`; `src/sources.F:110` `AA = TANH(PI/(Time_ramp*Tperiod)*TIME)*D_gen`; `:136` `AA = TANH(PI/(Time_ramp*PeakPeriod)*TIME)` | 일치 | 규칙파는 Tperiod의 배수다. 성분파는 PeakPeriod의 배수다. 예제 블록은 이 값을 초 단위라고 적지 않는다. |
| FV2-040 | funwave_tvd_2.1_manual.pdf p.45: `Delta_WK = 0.3`; p.52: `Delta_WK = 0.4 ! width parameter 0.3-0.6`; p.56: `Delta_WK = 0.5 ! width parameter 0.3-0.6` | `src/io.F:1054` 및 `:1531` `CALL READ_FLOAT(Delta_WK,FILE_NAME,'Delta_WK',ierr)`; `src/wavemaker.F:2453` `beta_gen(I)=80.0_SP/delta**2/wave_length**2` | 일치 | 세 값은 폭 매개변수로 읽힌다. 주석의 권고 범위는 강제 검사 범위가 아니다. |
| FV2-041 | funwave_tvd_2.1_manual.pdf p.52: `NumWaveComp = 1505` | `src/io.F:951` `CALL READ_INTEGER(NumWaveComp,FILE_NAME,'NumWaveComp',ierr)`; `src/wavemaker.F:353` `DO J=1,NumWaveComp` | 일치 | 코드가 성분 자료 1505행을 읽는다. |
| FV2-042 | funwave_tvd_2.1_manual.pdf p.52: `PeakPeriod = 1.0` | `src/io.F:966` `CALL READ_FLOAT(PeakPeriod,FILE_NAME,'PeakPeriod',ierr)`; `src/wavemaker.F:2464` `omgn_tmp=2.0_SP*pi/PeakPeriod`; `:2470` `width=delta*wave_length/2.0_SP` | 일치 | 전체 조파원 폭과 시간 증가 구간에 쓰는 첨두 주기다. 모든 성분의 주기가 1초라는 뜻이 아니다. |
| FV2-043 | funwave_tvd_2.1_manual.pdf p.52: `WaveCompFile = ../fft/wavemk_per_amp_pha.txt` | `src/io.F:981` `CALL READ_STRING(WaveCompFile,FILE_NAME,'WaveCompFile',ierr)`; `src/wavemaker.F:352` `OPEN(1,FILE=TRIM(WaveCompFile))`; `:354` `READ(1,*)(WAVE_COMP(J,I),I=1,3)` | 일치 | 파일은 각 성분의 주기·진폭·위상 세 열을 제공한다. 코드는 원시 시계열의 FFT를 여기서 수행하지 않는다. |
| FV2-044 | funwave_tvd_2.1_manual.pdf p.52·56: `Ywidth_WK = 10000.0` | `src/io.F:1069` 및 `:1545` `CALL READ_FLOAT(Ywidth_WK,FILE_NAME,'Ywidth_WK',ierr)` | 일치 | 조파원을 y 방향으로 자르는 폭이다. 실제 마스크 조건과 중심 기본값은 FV2-305에 적었다. |
| FV2-045 | funwave_tvd_2.1_manual.pdf p.60: `AMP = 0.0144 ! 0.02912 for case B and 0.05792 for case C`; p.68: `AMP = 0.39`; p.70·71: `AMP = 0.1` | `src/io.F:1132` `CALL READ_FLOAT(AMP_SOLI,FILE_NAME,'AMP',ierr)`; `src/samples.F:536` `CALL SUB_SLTRY(AMP_Soli,Dep_Soli,alpha,Cph,B,A1,A2,A,C_ph)` | 일치 | 세 사례의 실제 입력 키는 `AMP`다. 원뿔섬의 `!` 뒤 두 값은 사례를 바꿀 때 사용할 설명이다. 코드가 세 파를 한 번에 만들지 않는다. |
| FV2-046 | funwave_tvd_2.1_manual.pdf p.60: `DEP = 0.32`; p.68: `DEP = 0.78`; p.70·71: `DEP = 10.0` | `src/io.F:1147` `CALL READ_FLOAT(DEP_SOLI,FILE_NAME,'DEP',ierr)` | 일치 | 초기 고립파 해의 수심을 읽는다. |
| FV2-047 | funwave_tvd_2.1_manual.pdf p.60·68: `LAGTIME = 5.0`; p.70·71: `LAGTIME = 0.0` | `src/io.F:890`의 LEF_SOL 분기 아래 `:924` `CALL READ_FLOAT(LAG_SOLI,FILE_NAME,'LAGTIME',ierr)`; INI_SOL 분기는 `:1132`, `:1147`, `:1162`에서 AMP·DEP·XWAVEMAKER를 읽는다. | 불일치 — B | 예제는 모두 INI_SOL이다. 이 경로는 LAGTIME을 읽지 않는다. INI_SOL 초기화는 시간 지연 없이 실행한다. 문서 저장 시점의 코드도 같다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-048 | funwave_tvd_2.1_manual.pdf p.60: `XWAVEMAKER = 8.0`; p.68: `XWAVEMAKER = 10.0`; p.70·71: `XWAVEMAKER = 1000.0` | `src/io.F:1162` `CALL READ_FLOAT(XWAVEMAKER,FILE_NAME,'XWAVEMAKER',ierr)` | 일치 | 입력 이름과 실수 형식은 같다. 초기 파형의 실제 중심에는 가상 셀 좌표 차이가 있다. FV2-136은 이 차이를 E로 분류한다. |

#### 2.3.3 완충층·물리·수치 설정

| 행 ID | 문서 원문과 출현 위치 | 코드 원문 | 판정 | 이유 |
|---|---|---|---|---|
| FV2-049 | funwave_tvd_2.1_manual.pdf p.45·52·56: `SPONGE_ON = T`; p.60·68: `SPONGE_ON = F` | `src/io.F:2280` `CALL READ_LOGICAL(DIFFUSION_SPONGE,FILE_NAME,'DIFFUSION_SPONGE',ierr)`; `:2285` `CALL READ_LOGICAL(DIRECT_SPONGE,FILE_NAME,'DIRECT_SPONGE',ierr)`; `:2290` `CALL READ_LOGICAL(FRICTION_SPONGE,FILE_NAME,'FRICTION_SPONGE',ierr)` | 문서에만 — D | 현재 파서는 SPONGE_ON을 입력 키로 찾지 않는다. 전체 원자료의 rg -i와 제공 git 이력의 log -S는 동명 변수 선언만 찾았다. 검색어와 결과는 §5에 적었다. 세 실제 스위치의 누락 기본값은 모두 거짓이다. 따라서 T로 쓴 세 예제의 완충층은 이 발췌만으로 켜지지 않는다. F로 쓴 예제의 완충층 비활성은 실제 스위치의 누락 기본값 때문에 성립한다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-050 | funwave_tvd_2.1_manual.pdf p.45: `Sponge_west_width = 10.0`; p.52·56: `Sponge_west_width = 2.0` | `src/io.F:2374` `IF(DIFFUSION_SPONGE.OR.DIRECT_SPONGE.OR.FRICTION_SPONGE)THEN`; `:2375` `CALL READ_FLOAT(Sponge_west_width,FILE_NAME,'Sponge_west_width',ierr)` | 일치 — 활성 조건부 | 키와 값 형식은 맞다. FV2-049의 예제에서는 활성 조건이 거짓이라 이 키를 읽지 않는다. |
| FV2-051 | funwave_tvd_2.1_manual.pdf p.45·52: `Sponge_east_width = 0.0`; p.56: `Sponge_east_width = 2.0` | `src/io.F:2389` `CALL READ_FLOAT(Sponge_east_width,FILE_NAME,'Sponge_east_width',ierr)` | 일치 — 활성 조건부 | FV2-050과 같은 조건이다. |
| FV2-052 | funwave_tvd_2.1_manual.pdf p.45·52·56: `Sponge_south_width = 0.0` | `src/io.F:2403` `CALL READ_FLOAT(Sponge_south_width,FILE_NAME,'Sponge_south_width',ierr)` | 일치 — 활성 조건부 | FV2-050과 같은 조건이다. |
| FV2-053 | funwave_tvd_2.1_manual.pdf p.45·52·56: `Sponge_north_width = 0.0` | `src/io.F:2417` `CALL READ_FLOAT(Sponge_north_width,FILE_NAME,'Sponge_north_width',ierr)` | 일치 — 활성 조건부 | FV2-050과 같은 조건이다. |
| FV2-054 | funwave_tvd_2.1_manual.pdf p.45: `R_sponge = 0.95`; p.52·56: `R_sponge = 0.90` | `src/io.F:2431` `CALL READ_FLOAT(R_sponge,FILE_NAME,'R_sponge',ierr)` | 일치 — 활성 조건부 | 키와 실수 형식은 맞다. FV2-050과 같은 활성 조건이다. |
| FV2-055 | funwave_tvd_2.1_manual.pdf p.45·52·56: `A_sponge = 5.0` | `src/io.F:2445` `CALL READ_FLOAT(A_sponge,FILE_NAME,'A_sponge',ierr)` | 일치 — 활성 조건부 | FV2-050과 같은 조건이다. |
| FV2-056 | funwave_tvd_2.1_manual.pdf p.45·52·56·60·68·70·72: `DISPERSION = T` | `src/io.F:2577` `CALL READ_LOGICAL(DISPERSION,FILE_NAME,'DISPERSION',ierr)`; `:2579` `DISPERSION = .TRUE.` | 일치 | 예제의 T와 누락 기본값이 같다. 분산 항은 지역 MASK9의 영향도 받는다. |
| FV2-057 | funwave_tvd_2.1_manual.pdf p.45·52·56·60·68·70·72: `Gamma1 = 1.0` | `src/io.F:2591` `CALL READ_FLOAT(Gamma1,FILE_NAME,'Gamma1',ierr)`; `:2593` `Gamma1 = 1.0_SP` | 일치 | 선형 분산 계수를 읽는다. |
| FV2-058 | funwave_tvd_2.1_manual.pdf p.45·53·56·60·68: `Gamma2 = 1.0` | `src/io.F:2605` `# if defined (CARTESIAN)`; `:2606` `CALL READ_FLOAT(Gamma2,FILE_NAME,'Gamma2',ierr)`; `:2608` `Gamma2 = 1.0_SP` | 일치 | 직교 예제는 비선형 분산 계수 1을 읽는다. |
| FV2-059 | funwave_tvd_2.1_manual.pdf p.70·72: `Gamma2 = 0.0` | `src/io.F:2605` `# if defined (CARTESIAN)`; `:2606` `CALL READ_FLOAT(Gamma2,FILE_NAME,'Gamma2',ierr)`; `:2634` `# endif` | 불일치 — B | 구면 예제는 이 읽기 구간을 컴파일하지 않는다. 0이라는 값이 구면 약비선형 방정식을 선택하는 입력은 아니다. 같은 문서 p.41도 구면 코드에 Gamma2를 지정할 필요가 없다고 설명한다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-060 | funwave_tvd_2.1_manual.pdf p.45: `Gamma3=1.0`; p.53·56·60·68·70·72: `Gamma3 = 1.0` | `src/io.F:2651` `CALL READ_FLOAT(Gamma3,FILE_NAME,'Gamma3',ierr)`; `:2653` `Gamma3 = 1.0_SP` | 일치 | 등호 주변 공백의 차이는 키 비교에서 제거한다. |
| FV2-061 | funwave_tvd_2.1_manual.pdf p.45·53·56·60·68: `Beta_ref=-0.531` | `src/io.F:2620` `CALL READ_FLOAT(Beta_ref,FILE_NAME,'Beta_ref',ierr)`; `:2622` `Beta_ref = - 0.531_SP` | 일치 | 직교 분기는 이 실수 키를 읽는다. |
| FV2-062 | funwave_tvd_2.1_manual.pdf p.71·72: `Beta_ref=-0.531` | `src/io.F:2635` `# if defined (ZALPHA)`; `:2636` `CALL READ_FLOAT(Beta_ref,FILE_NAME,'Beta_ref',ierr)`; `:2638` `Beta_ref = -0.531_SP` | 불일치 — C | 2.1 p.8과 3.0 p.9는 `-DZALPHA`를 설명한다. `funwave_tvd_3.0.tex` 173행도 같은 플래그를 적는다. C의 범위는 2.1 p.71–72 입력 발췌에 Beta_ref 읽기의 ZALPHA 조건을 연결하지 않은 점이다. 구면에서 Beta_ref 입력은 ZALPHA 분기에만 적용한다. 플래그 자체는 2.1 p.8·3.0 p.9에 설명되어 있다. 중첩 입력 발췌에 이 조건을 함께 적는다. [10-18 결론 검증 보완] |
| FV2-063 | funwave_tvd_2.1_manual.pdf p.45: `SWE_ETA_DEP = 0.8`; p.53·56·60·68·71·72: `SWE_ETA_DEP = 0.80` | `src/io.F:2713` `CALL READ_FLOAT(SWE_ETA_DEP,FILE_NAME,'SWE_ETA_DEP',ierr)`; `:2715` `SWE_ETA_DEP = 0.80_SP` | 일치 | 입력값은 모두 수치적으로 같다. 현재 기본 쇄파 방식에서 이 값이 전환을 일으키지 않는 차이는 FV2-301에 적었다. |
| FV2-064 | funwave_tvd_2.1_manual.pdf p.45·56: `Cd = 0.0`; p.53·69: `Cd = 0.001`; p.62: `Cd = 0.01`; p.71·72: `Cd = 0.00` | `src/io.F:2777` `CALL READ_FLOAT(Cd_fixed,FILE_NAME,'Cd',ierr)`; `src/init.F:887` `Cd(I,J) = Cd_fixed` | 일치 | 현재 코드의 입력 키도 Cd다. 내부 변수 이름 Cd_fixed를 입력 키로 바꾸면 안 된다. `MANNING`을 정의하면 같은 배열의 물리적 의미가 달라진다. |
| FV2-065 | funwave_tvd_2.1_manual.pdf p.45·53·56·62·69·71·72: `Time_Scheme = Runge_Kutta` | `src/io.F:2806` `CALL READ_STRING(Time_Scheme,FILE_NAME,'Time_Scheme',ierr)`; `:2808` `Time_Scheme = 'Runge_Kutta'` | 일치 | 문자열과 누락 기본값이 같다. 실제 시간 적분 경로는 FV2-309에 적었다. |
| FV2-066 | funwave_tvd_2.1_manual.pdf p.45·53·57·62·69: `HIGH_ORDER = FOURTH`; p.71·72: `HIGH_ORDER = THIRD` | `src/io.F:2842` `CALL READ_STRING(HIGH_ORDER,FILE_NAME,'HIGH_ORDER',ierr)`; `src/fluxes.F:56` `IF(HIGH_ORDER(1:3)=='FOU') THEN       !ykchoi (08/28/2016)` | 일치 | 현재 활성 fluxes.F는 FOURTH를 인식한다. THIRD는 낮은 차수 구성 분기로 간다. 같은 값 이름이 보장하는 limiter 계보는 FV2-308에 분리했다. |
| FV2-067 | funwave_tvd_2.1_manual.pdf p.45·53·57·62·69·71·72: `CONSTRUCTION = HLLC` | `src/io.F:2826` `CALL READ_STRING(CONSTR,FILE_NAME,'CONSTRUCTION',ierr)`; `src/fluxes.F:109` `IF(CONSTR(1:3)=='HLL')THEN`; `:110` `CALL FLUX_AT_INTERFACE_HLL` | 일치 | 앞 세 글자가 HLL이므로 HLL 플럭스 분기를 선택한다. 별도의 HLLC 분기가 있다고 해석하지 않는다. |
| FV2-068 | funwave_tvd_2.1_manual.pdf p.45·53·57·62·69·71·72: `CFL = 0.5` | `src/io.F:2862` `CALL READ_FLOAT(CFL,FILE_NAME,'CFL',ierr)`; `:2864` `CFL = 0.5_SP` | 일치 | 값과 실수 형식이 같다. |
| FV2-069 | funwave_tvd_2.1_manual.pdf p.45·53·57·62·69: `MinDepth=0.001` | `src/io.F:2919` `CALL READ_FLOAT(MinDepth,FILE_NAME,'MinDepth',ierr)`; `:2921` `MinDepth = 0.1_SP` | 일치 — 한 줄에 한 대입문 조건 | 0.001은 예제 지정값이다. 코드 누락 기본값 0.1과 구별한다. p.53의 인쇄 줄 형식은 FV2-086에 적었다. |
| FV2-070 | funwave_tvd_2.1_manual.pdf p.45·53·57·62·69: `MinDepthFrc = 0.001` | `src/io.F:2933` `CALL READ_FLOAT(MinDepthFrc,FILE_NAME,'MinDepthFrc',ierr)`; `:2935` `MinDepthFrc = 0.1_SP`; `:2948` `MinDepthFrc=MIN(MinDepthFrc,MinDepth)`; `:2949` `MinDepth=MinDepthFrc` | 일치 — 한 줄에 한 대입문 조건 | 두 값이 모두 0.001이면 현재 병합 후에도 0.001이다. 서로 다른 값을 지정할 때의 판 차이는 FV2-306에 적었다. |

#### 2.3.4 출력·구면 격자·결합 입력

| 행 ID | 문서 원문과 출현 위치 | 코드 원문 | 판정 | 이유 |
|---|---|---|---|---|
| FV2-071 | funwave_tvd_2.1_manual.pdf p.53: `NumberStations = 12`; p.57: `NumberStations = 0`; p.62: `NumberStations = 16`; p.71 Grid_A: `NumberStations = 3` | `src/io.F:3359` `CALL READ_INTEGER(NumberStations,FILE_NAME,'NumberStations',ierr)`; `:3360` `IF(NumberStations>0)THEN` | 일치 | 양수일 때만 관측점 파일을 읽는다. 원뿔섬 본문의 관측점 수 설명은 FV2-131에서 따로 대조했다. |
| FV2-072 | funwave_tvd_2.1_manual.pdf p.53: `STATIONS_FILE = gauges_004.txt`; p.62: `STATIONS_FILE = gauges.txt`; p.71 Grid_A: `STATIONS_FILE = station.txt` | `src/io.F:3361` `CALL READ_STRING(STATIONS_FILE,FILE_NAME,'STATIONS_FILE',ierr)` | 일치 | 키의 복수형 STATIONS와 대소문자가 같다. 파일의 관측점 순서가 출력 파일 순서를 정한다. |
| FV2-073 | funwave_tvd_2.1_manual.pdf p.45·53·57·62·69: `DEPTH_OUT = T` | `src/io.F:3385` `CALL READ_LOGICAL(OUT_DEPTH,FILE_NAME,'DEPTH_OUT',ierr)` | 일치 | 수심 출력 플래그를 켠다. |
| FV2-074 | funwave_tvd_2.1_manual.pdf p.45·53·57·62·69: `ETA = T` | `src/io.F:3388` `CALL READ_LOGICAL(OUT_ETA,FILE_NAME,'ETA',ierr)` | 일치 | 수면변위 출력 플래그를 켠다. |
| FV2-075 | funwave_tvd_2.1_manual.pdf p.45·62·69: `MASK = T` | `src/io.F:3397` `CALL READ_LOGICAL(OUT_MASK,FILE_NAME,'MASK',ierr)` | 일치 | 젖음·마름 마스크 출력 플래그를 켠다. |
| FV2-076 | funwave_tvd_2.1_manual.pdf p.62: `Hmax = T` | `src/io.F:3392` `CALL READ_LOGICAL(OUT_Hmax,FILE_NAME,'Hmax',ierr)` | 일치 | 예제의 철자는 Hmax다. 전부 대문자인 HMAX로 바꾸면 이 키와 같지 않다. |
| FV2-077 | funwave_tvd_2.1_manual.pdf p.69: `U = T` | `src/io.F:3386` `CALL READ_LOGICAL(OUT_U,FILE_NAME,'U',ierr)` | 일치 | x 방향 유속 장을 출력한다. |
| FV2-078 | funwave_tvd_2.1_manual.pdf p.69: `V = T` | `src/io.F:3387` `CALL READ_LOGICAL(OUT_V,FILE_NAME,'V',ierr)` | 일치 | y 방향 유속 장을 출력한다. |
| FV2-079 | funwave_tvd_2.1_manual.pdf p.70·71: `StretchGrid = F` | `src/io.F:327` `CALL READ_LOGICAL(StretchGrid,FILE_NAME,'StretchGrid',ierr)`; `:329` `StretchGrid = .FALSE.`; `:380` `else  ! not stretch` | 일치 | CARTESIAN을 정의하지 않은 구면 분기의 균일 각도 격자를 선택한다. |
| FV2-080 | funwave_tvd_2.1_manual.pdf p.70·71: `Lon_West = 120.0` | `src/io.F:382` `CALL READ_FLOAT(Lon_West,FILE_NAME,'Lon_West',ierr)` | 일치 | 구면 영역 서쪽 경도를 읽는다. |
| FV2-081 | funwave_tvd_2.1_manual.pdf p.70·71: `Lat_South = 0.0` | `src/io.F:398` `CALL READ_FLOAT(Lat_South,FILE_NAME,'Lat_South',ierr)` | 일치 | 구면 영역 남쪽 위도를 읽는다. |
| FV2-082 | funwave_tvd_2.1_manual.pdf p.70 Grid_A: `Dphi = 0.000035972`; p.71 Grid_B: `Dphi = 0.000017986` | `src/io.F:414` `CALL READ_FLOAT(Dphi,FILE_NAME,'Dphi',ierr)`; `src/init.F:363` `Dphi_r=Dphi*pi/180.0_SP`; `:379` `Dx(I,J) = R_earth*Dphi_r*COS(Lat_theta(I,J))` | 일치 | 각도 간격을 m 간격으로 환산한다. 적도에서 두 값은 약 4 m와 2 m다. 약값은 `src/mod_param.F:72`의 `REAL(SP), PARAMETER::R_earth = 6371000.0_SP`로 계산했다. |
| FV2-083 | funwave_tvd_2.1_manual.pdf p.70·71: `Dtheta = 0.0001` | `src/io.F:430` `CALL READ_FLOAT(Dtheta,FILE_NAME,'Dtheta',ierr)`; `src/init.F:380` `Dy(I,J) = R_earth*Dtheta_r` | 일치 | 두 격자의 위도 간격은 같다. 입력 형식은 실수다. |
| FV2-084 | funwave_tvd_2.1_manual.pdf p.71 Grid_A·p.72 Grid_B: `FroudeCap = 10.0` | `src/io.F:2898` `CALL READ_FLOAT(FroudeCap,FILE_NAME,'FroudeCap',ierr)`; `:2900` `FroudeCap = 3.0_SP` | 일치 | 10은 예제 지정값이다. 누락 기본값은 3이다. |
| FV2-085 | funwave_tvd_2.1_manual.pdf p.72: `COUPLING_FILE = ../make_nest_file/coupling.txt` | `src/io.F:3280` `CALL READ_STRING(COUPLING_FILE,FILE_NAME,'COUPLING_FILE',ierr)`; `src/nesting.F:71` `OPEN(11,FILE=TRIM(COUPLING_FILE))` | 일치 | COUPLING을 정의한 Grid_B에서만 읽는다. 경로는 실행 디렉터리 기준 상대 경로다. |
| FV2-086 | funwave_tvd_2.1_manual.pdf p.53의 연속 두 줄: `MinDepth=0.001` / `MinDepthFrc = 0.001` | `src/mod_input.F:287` `READ(10,'(A)',END=100) TEXT_READ`; `:295` `FRONT = index(TEXT,"=")`; `:298` `VAL  = ADJUSTL(TEXT(FRONT+1:TEXT_LENGTH))` | 일치 | 원해상도 이미지에서 두 대입문은 서로 다른 줄이다. PDF 글자 기준선도 각각 y=261.193630과 y=274.742630이다. 한 줄에 한 키를 읽는 파서와 맞는다. 3.0 p.52도 두 줄이다. |

### 2.4 예제 설명·식·절차·그림

다음 표는 입력 블록 밖의 설정 설명과 결과 설명을 구분한다.
H 행의 코드 열에서 `해당 없음`은 코드 미판독을 뜻하지 않는다.
H 행은 해당 문장이 코드 대조 대상이 아니라는 뜻이다.
결과 그림의 범례·축·캡션 사이 차이도 H 행에 보존한다.
그 차이를 수치 결과 검증으로 바꾸지 않는다.

#### 2.4.1 해빈과 불규칙파

| 행 ID | 문서 원문 | 코드 원문 | 판정 | 이유 |
|---|---|---|---|---|
| FV2-100 | funwave_tvd_2.1_manual.pdf p.43: `The model has been validated extensively using laboratory experiments for wave shoaling and breaking as in the FUNWAVE manual by Kirby et al. (1998).`; `Tests of mass conservation and convergence are included in Tehranirad et al. (2011).` | 해당 없음 | 코드 대조 대상 아님 — H | 과거 검증의 서술이다. Version 1.0과 NTHMP의 벤치마크 시험 언급도 여기에 포함한다. |
| FV2-101 | funwave_tvd_2.1_manual.pdf p.43: `Waves were generated on a flat bottom a 0.36 m depth, and the beach slope was 1:34.26.`; `The wave height and wave period are 4.3 cm and 3.33 s, respectively, for the plunging case, and 6.7 cm and 1.67 s for the spilling case.` | 해당 없음 | 코드 대조 대상 아님 — H | Hansen and Svendsen 실험의 조건이다. 권파형·권파와 붕파의 혼합형·붕파형을 포함한다는 실험 분류도 H다. 입력 블록은 권파형 한 사례를 발췌했다. |
| FV2-102 | funwave_tvd_2.1_manual.pdf p.43: `we adopted three grid sizes, dx = 0.05 m, 0.025 m and 0.0125 m, respectively, for each cases.` | `src/io.F:286` `CALL READ_FLOAT(DX,FILE_NAME,'DX',ierr)` 2.1 p.44의 발췌는 `DX = 0.025`를 지정한다. `src/io.F:284–286`의 CARTESIAN 분기에서 DX를 읽는다. | 일치 | 일치는 직교 격자 간격을 DX 실수 입력으로 지정하는 경로에 한정한다. p.43의 0.05·0.025·0.0125 m는 문서가 사용했다고 보고한 세 해상도이고, 발췌 입력은 0.025 m 한 값이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-103 | funwave_tvd_2.1_manual.pdf p.43–44: `All three models underpredict the peak wave height at breaking and overpredict wave height inside of the surfzone.`; `About 10% underprediction of peak wave height can be found in our tests with dx = 0.025 m and 0.0125 m`; `The model with a coarser grid (dx = 0.05 m) underpredicted the maximum wave height by 20%.` | 해당 없음 | 불일치 — B | 2.1 p.44의 두 `dx = 0.25 m` 표기는 p.43의 해상도 목록·p.44 입력 `DX = 0.025`·p.48 그림 5의 `dx = 0.025 m`와 다르다. B는 결과 설명의 격자 간격 오기에 한정한다. 0.25 m는 0.025 m로 바로잡아 읽는다. 파고 과소·과대 예측과 평균수위 평가는 문서가 보고한 결과다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-104 | funwave_tvd_2.1_manual.pdf p.44: `! give any larger value than DX for 1-D case` | `src/io.F:304` `CALL READ_FLOAT(DY,FILE_NAME,'DY',ierr)` 2.1 p.44의 실제 입력은 `DX = 0.025`, `DY = 0.2`다. `src/io.F:286·304`는 두 값을 각각 READ_FLOAT로 읽는다. | 일치 | DY=0.2는 DX=0.025보다 큰 예제 지정값이다. 코드의 입력 경로는 이 두 값을 각각 읽는다. 문서 주석은 사례의 권고이며 DY와 DX의 크기 비교를 강제하는 입력 조건은 아니다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-105 | funwave_tvd_2.1_manual.pdf p.45: `! Cd is not sensitive for this case`; p.53: `! not sensitive for this case`; p.62: `! note: not sensitive, could give a small value like 0.001` | `src/io.F:2777` `CALL READ_FLOAT(Cd_fixed,FILE_NAME,'Cd',ierr)` `src/io.F:2738–2740·2777–2779`는 FRICTION_MATRIX와 Cd를 읽는다. `src/init.F:884–887`은 고정 Cd를 배열로 배포한다. `src/sources.F:237–242`가 그 배열을 마찰항에 사용한다. | 일치 | 일치는 FRICTION_MATRIX가 거짓인 예제에서 Cd를 읽고 마찰항에 적용하는 경로에 한정한다. '민감하지 않다'는 문서의 사례 평가다. 이 표현은 Cd 입력을 생략하거나 무시하는 분기라는 뜻이 아니다(FV2-307·409). [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-106 | funwave_tvd_2.1_manual.pdf p.46 그림 3: `Comparisons of wave height (upper panel) and wave setup (lower panel) between measured data and model results from grid resolutions of dx = 0.0125 m, 0.025 m and 0.050 m, respectively. Case: plunging breaker.` | 해당 없음 | 코드 대조 대상 아님 — H | 파고·평균수위 결과 그림만 있는 쪽이다. |
| FV2-107 | funwave_tvd_2.1_manual.pdf p.47 그림 4: `Snapshots of surface elevation at t = 17.4, 18.6 and 19.9 s from models with grid resolutions of dx = 0.025 (solid lines) and 0.050 m (dashed lines).`; p.44: `the ratio of surface elevation to water depth reached the threshold value of 0.8.` | `src/masks.F:184` `IF(ABS(Eta(I,J))/MAX(DEPTH(I,J),MinDepthFrc)>SWE_ETA_DEP)THEN` `src/io.F:2689·2713`는 VISCOSITY_BREAKING·SWE_ETA_DEP를 읽는다. `src/masks.F:177–184`는 VISCOSITY_BREAKING이 거짓인 분기에서 임계값을 검사한다. | 표현 차이 — F | 문서의 '0.8에 도달'은 전환을 요약한 표현이다. 실제 조건은 `IF(ABS(Eta(I,J))/MAX(DEPTH(I,J),MinDepthFrc)>SWE_ETA_DEP)THEN`이다. 0.8과 같다는 조건이 아니다. 점성 쇄파 선택 시 이 검사는 우회한다(FV2-301). 19.9초는 문서가 보고한 전환 시각이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-108 | funwave_tvd_2.1_manual.pdf p.48 그림 5: `Model/data comparisons of wave height (upper panel) and wave setup (dx = 0.025 m). Case: spilling breaker.` | 해당 없음 | 코드 대조 대상 아님 — H | 붕파형의 결과 그림만 있는 쪽이다. p.44의 `dx = 0.25 m`와 캡션의 0.025 m를 구분했다. |
| FV2-109 | funwave_tvd_2.1_manual.pdf p.45: `a constant depth of 0.47 m on the left connects to a constant slope of 1:20 on the right.`; `0.6 Hz (run 1) and 1.0 Hz (run 2)`; `The target incident spectrum was a Pierson-Moskowitz spectrum.` | 해당 없음 | 코드 대조 대상 아님 — H | Mase and Kirby 실험 조건이다. 수심 47, 35, 30, 25, 20, 17.5, 15, 12.5, 10, 7.5, 5, 2.5 cm의 파고계 설명도 실험 배치다. |
| FV2-110 | funwave_tvd_2.1_manual.pdf p.49: `The computational domain is from x = 0 m to 20 m with a grid size of 0.04 m. The toe of the slope starts at x = 10 m.`; `A sponge layer is specified at the left side boundary, to absorb reflected waves, but no sponge layer is needed on the right boundary` | `src/init.F:577` `Xco(Ibeg) = ZERO`; `:582` `Xco(I) = Xco(I-1)+DX`; `src/io.F:2374` `IF(DIFFUSION_SPONGE.OR.DIRECT_SPONGE.OR.FRICTION_SPONGE)THEN` | 문서에만 — D | 지형·간격 입력은 대응한다. 그러나 SPONGE_ON=T는 왼쪽 완충층을 켜지 않는다. 이 행의 D는 완충층 입력 스위치의 미구현을 뜻한다. 격자 중심 좌표는 500점에서 0–19.96 m다. 경사 시작점의 격자 배치는 FV2-304에 적었다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-111 | funwave_tvd_2.1_manual.pdf p.49: `A FFT was used to transform between the time domain and frequency domain data required by the wavemaker.`; `fft4wavemaker.m`; `r2d470.dat`; `wavemk_per_amp_pha.txt`; `The low and high-frequency cutoffs are 0.2 and 10.0 Hz, respectively.` | 해당 없음 | 코드 대조 대상 아님 — H | MATLAB 전처리의 사용법이다. 파일 이름의 `amp_pha`는 주기·진폭·위상의 파일 열 순서를 변경하지 않는다. 외부 전처리의 주파수 차단값을 Fortran 입력 옵션으로 해석하지 않는다. |
| FV2-112 | funwave_tvd_2.1_manual.pdf p.49: `saves calculated wave amplitude, period and phase information for each component`; p.52: `WAVEMAKER = WK_TIME_SERIES` | `src/wavemaker.F:2435` `omgn=2.*pi/Wave_COMP(I,1)`; `:2437` `AMP_WK = WAVE_COMP(I,2)`; `src/sources.F:138` `BB1(kf,1) = COS(2.0_SP*PI/WAVE_COMP(kf,1)*TIME-WAVE_COMP(kf,3))` | 일치 | 첫 열은 주기다. 둘째 열은 진폭이다. 셋째 열은 라디안 위상이다. 본문의 산출 정보 나열 순서를 파일 열 정의로 바꾸지 않는다. |
| FV2-113 | funwave_tvd_2.1_manual.pdf p.49 식 (79), §2.4.1에 옮긴 인쇄식; `where H denotes the Hilbert transform, <> is the mean operator, and the mean has been removed from the time series of surface elevation.` | 해당 없음 | 코드 대조 대상 아님 — H | 왜도·비대칭도의 후처리 정의다. 모델 시간 적분식이 아니다. |
| FV2-114 | funwave_tvd_2.1_manual.pdf p.50 그림 6: `Experiment layout of Mase and Kirby (1992).` | 해당 없음 | 코드 대조 대상 아님 — H | 47 cm 수심, 1:20 경사, 조파판에서 사면 기슭까지 10 m, 파고계 1·2·3·12를 표시한 실험 배치다. |
| FV2-115 | funwave_tvd_2.1_manual.pdf p.50 그림 7: `Time series comparison of η between model (dashed lines) and data (solid lines) at 11 wave gauges in Mase and Kirby (1992).`; p.49: `from t = 20 s to t = 40 s` | 해당 없음 | 코드 대조 대상 아님 — H | 11개 비교 파고계의 시계열 결과다. 수심 15 cm에서 대부분의 파가 쇄파한다는 설명과 파형 재현 평가는 결과 주장이다. |
| FV2-116 | funwave_tvd_2.1_manual.pdf p.51 그림 8: `Comparison of skewness (◦) and asymmetry (×) at different water depths. Solid lines are experiment data ( Mase and Kirby, 1992). Dashed lines are numerical results` | 해당 없음 | 코드 대조 대상 아님 — H | 왜도·비대칭도 결과 그림만 있는 쪽이다. |
| FV2-117 | funwave_tvd_2.1_manual.pdf p.49: `The model predicted skewness and asymmetry reasonably well with a slightly overprediction of wave skewness inside the surf zone.` | 해당 없음 | 코드 대조 대상 아님 — H | 모델과 실험의 통계 비교 결과다. |
| FV2-118 | funwave_tvd_2.1_manual.pdf p.49: `The present model did not encounter any stability problem without filtering.` | 해당 없음 | 코드 대조 대상 아님 — H | 특정 계산의 안정성 보고다. Kirby et al. (1998)이 쇄파 뒤에 필터링을 더 자주 사용했다는 비교도 결과 설명이다. |
| FV2-119 | funwave_tvd_2.1_manual.pdf p.53: `Model output at 12 gauges are saved in sta_0001, sta_0002, ..., sta_0012. Use MATLAB scripts, comp_mkskew.m and cmop_series.m for plots.` | `src/io.F:3843` `do i=1,NumberStations`; `:3855` `write(file_name(1:4),'(I4.4)') i` | 일치 | 12개 파일의 번호는 입력의 NumberStations=12와 맞는다. MATLAB 사용법 자체는 FV2-111과 같은 H 범위다. 문서의 파일 철자는 `cmop_series.m` 그대로 보존한다. |

funwave_tvd_2.1_manual.pdf p.49의 인쇄식 (79)은 다음과 같다.

$$
\begin{aligned}
\mathrm{skew} &= \frac{<\eta^3>}{<\eta^2>^{3/2}} \\
\mathrm{asym} &= \frac{<H(\eta)^3>}{<\eta^2>^{3/2}}
\end{aligned}\tag{79}
$$

3.0은 같은 식을 `funwave_tvd_3.0.pdf p.48`의 식 (106)으로 인쇄한다.
식의 지수와 Hilbert 변환의 적용 대상은 같다.

#### 2.4.2 천퇴·원뿔섬·천해붕

| 행 ID | 문서 원문 | 코드 원문 | 판정 | 이유 |
|---|---|---|---|---|
| FV2-120 | funwave_tvd_2.1_manual.pdf p.53: `an elliptic shoal resting on a plane beach with a constant slope 1/50.`; `20° to the y axis`; `period of 1s and amplitude of 2.32cm`; `x = −10m`; `y = −10m and y=10m` | `src/io.F:486` `CALL READ_STRING(DEPTH_FILE,FILE_NAME,'DEPTH_FILE',ierr)`; `:1428` `CALL READ_FLOAT(Xc_WK,FILE_NAME,'Xc_WK',ierr)` 2.1 p.54·56은 `DEPTH_TYPE = DATA`와 `Xc_WK = 3.0`을 지정한다. `src/io.F:485–486·1427–1428`이 DATA·WK_REG 입력을 읽고 `src/init.F:701–707`이 수심 배열을 읽는다. | 일치 | 일치는 지형 파일과 모델 좌표의 Xc_WK를 읽는 경로에 한정한다. 실험의 조파 위치 x=−10 m와 모델 입력 Xc_WK=3.0은 서로 다른 좌표 표기다. 실험 배치·파고·주기는 문서의 사례 조건으로 적는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-121 | funwave_tvd_2.1_manual.pdf p.53–54: `two sponge layers with a width of 2m sitting behind wavemaker and on the end of the beach.`; `Thirty waves are simulated`; `the last 5 seconds (5 wave periods)`; `calcheight.m and showheight.m` | `src/io.F:603` `CALL READ_FLOAT(TOTAL_TIME,FILE_NAME,'TOTAL_TIME',ierr)`; `:1458` `CALL READ_FLOAT(Tperiod,FILE_NAME,'Tperiod',ierr)` | 문서에만 — D | 30초와 1초 주기는 30개 주기 설정에 대응한다. 마지막 5초의 파고 계산은 MATLAB 후처리다. 이 행의 D는 SPONGE_ON=T로 두 완충층을 켤 수 없다는 차이다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-122 | funwave_tvd_2.1_manual.pdf p.54 그림 9: `Experiment layout for wave focusing experiment of Berkhoff et al. (1982).`; p.55 그림 10: `Comparisons of wave height along specified sections between the model (solid lines) and experiment data (circles).` | 해당 없음 | 코드 대조 대상 아님 — H | 그림 9는 등수심선과 8개 측선이다. 그림 10은 측선별 파고 결과다. 관측과 잘 맞고 이전 FUNWAVE와 유사하다는 p.54의 평가는 H다. |
| FV2-123 | funwave_tvd_2.1_manual.pdf p.57: `a 30m-wide, 25m-long, and 60cm-deep wave basin`; `a 62.5cm-high, 7.2m toe-diameter, and 2.2m crest-diameter circular island with a 1:4 slope`; `depth of 32cm`; `H/d=0.045, 0.091, 0.181`; `27 wave gages` | 해당 없음 | 코드 대조 대상 아님 — H | Briggs 실험 조건이다. 섬 후면의 처오름·침수 높이가 입사파고를 넘을 수 있다는 현상 설명도 H다. Synolakis et al. (2007) Appendix A §3.3과 Liu·Chen의 검증 사례는 외부 사례 인용이다. |
| FV2-124 | funwave_tvd_2.1_manual.pdf p.58 그림 11: `View of conical island(top) and basin(bottom)(from Synolakis et al (2007, Figure A16)).` | 해당 없음 | 불일치 — B | 2.1 p.58 그림 11은 Gauge 6·9·16·22의 네 곡선 패널이다. 3.0 p.65 그림 15에도 같은 전경 캡션과 곡선 그림의 충돌이 있다. `funwave_tvd_3.0.tex` 1984–1985행은 caseA.pdf와 전경 캡션을 결합한다. 그림 11의 전경 캡션은 실제 관측점별 곡선 그림과 맞지 않는 문서 편집 오류다. 그림 12·13에도 같은 종류의 오류가 있다(FV2-125·126). [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-125 | funwave_tvd_2.1_manual.pdf p.58 그림 12: `Definition sketch for conical island. All dimensions are in cm (from Synolakis et al (2007, Figure A17)).` | 해당 없음 | 불일치 — B | 2.1 p.58 그림 12는 Gauge 6·9·16·22의 네 곡선 패널이다. 3.0 p.66 그림 16도 치수 정의도 캡션 아래 같은 종류의 곡선을 싣는다. `funwave_tvd_3.0.tex` 1991–1992행은 caseB.pdf와 정의도 캡션을 결합한다. 그림 12의 치수 정의도 캡션은 실제 관측점별 곡선 그림과 맞지 않는 문서 편집 오류다(FV2-124·126). [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-126 | funwave_tvd_2.1_manual.pdf p.59 그림 13: `Schematic gauge locations around the conical island(from Synolakis et al (2007, Figure A18)).` | 해당 없음 | 불일치 — B | 2.1 p.59 그림 13은 Gauge 6·9·16·22의 네 곡선 패널이다. 3.0 p.66 그림 17도 관측점 배치도 캡션 아래 같은 종류의 곡선을 싣는다. `funwave_tvd_3.0.tex` 1998–1999행은 caseC.pdf와 배치도 캡션을 결합한다. 그림 13의 관측점 배치도 캡션은 실제 관측점별 곡선 그림과 맞지 않는 문서 편집 오류다(FV2-124·125). [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-127 | funwave_tvd_2.1_manual.pdf p.59 표 1: `Percent error of predicted maximum runup calculated for each gauge in conical island test.`; 열 `H/d`, `6`, `9`, `16`, `22`; 행 0.045 행의 셀 `6.0`·`13.2`·`0.1`·`18.9`; 0.091 행의 셀 `3.2`·`16.6`·`11.6`·`0.26`; 0.181 행의 셀 `1.6`·`13.33`·`13.8`·`13.3` | 해당 없음 | 코드 대조 대상 아님 — H | 최대 처오름의 백분율 오차다. 표의 값을 새 계산 결과로 사용하지 않는다. |
| FV2-128 | funwave_tvd_2.1_manual.pdf p.60 그림 14: `Comparison of computed and measured time series of free surface for H/d = 0.045.Solid lines: measured, Dashed lines: Computed.` | 해당 없음 | 코드 대조 대상 아님 — H | Gauge 6·9·16·22의 시계열 결과다. p.57은 기슭의 Gauge 6과 해안선 부근 Gauge 9·16·22를 비교 위치로 지정한다. |
| FV2-129 | funwave_tvd_2.1_manual.pdf p.61 그림 15: `Comparison of computed and measured time series of free surface for H/d = 0.091.Solid lines: measured, Dashed lines: Computed.` | 해당 없음 | 코드 대조 대상 아님 — H | 두 번째 파고의 시계열 결과다. |
| FV2-130 | funwave_tvd_2.1_manual.pdf p.61 그림 16: `Comparison of computed and measured time series of free surface for H/d = 0.181.Solid lines: measured, Dashed lines: Computed.` | 해당 없음 | 코드 대조 대상 아님 — H | 세 번째 파고의 시계열 결과다. |
| FV2-131 | funwave_tvd_2.1_manual.pdf p.62: `The results of surface elevation at seven gauges are saved as sta_0001 ... sta_0016 as specified in input.txt.`; `sta_0001 (gauge 6), sta_0002 (gauge 9), sta_0008 (gauge16), sta_0022 (gauge 22).` | `src/io.F:3843` `do i=1,NumberStations`; `:3855` `write(file_name(1:4),'(I4.4)') i`; `:3856` `TMP_NAME = TRIM(FDIR)//'sta_'//TRIM(FILE_NAME)`; `:3866–3875`는 내부 격자 소속 조건을 통과한 관측점만 파일로 연다. | 불일치 — B | NumberStations=16이면 파일에 쓸 관측점 순번은 1–16이다. 내부 격자에 속한 관측점만 파일을 만든다. 같은 문장의 seven gauges는 NumberStations=16과 맞지 않는다. 같은 쪽의 seven gauges는 입력 개수와 다르다. sta_0022는 이 순번 범위 밖이다. Gauge 22는 실험 이름이며 출력 순번과 구별해야 한다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-132 | funwave_tvd_2.1_manual.pdf p.62: `A post-processing MATLAB script called plot_comparison.m can be used for model/data comparisons.` | 해당 없음 | 코드 대조 대상 아님 — H | 외부 후처리 도구 사용법이다. |
| FV2-133 | funwave_tvd_2.1_manual.pdf p.62–63: `The basin is 48.8 m long, 26.5 m wide, and 2.1 m deep.`; `a 1:30 slope planar beach connected to a triangle shaped shelf and a conical island`; 그림 17: `Bathymetry contours (in meters) and measurement locations used in model/data comparisons. Circles: pressure gauges, triangles: ADV.` | 해당 없음 | 코드 대조 대상 아님 — H | OSU 실험 배치다. Gauge 1–9 좌표는 (7.5,0.0), (13.0,0.0), (21.0,0.0), (7.5,5.0), (13.0,5.0), (21.0,5.0), (25.0,0.0), (25.0,5.0), (25.0,10.0)이다. ADV 1–3 좌표는 (13.0,0.0), (21.0,0.0), (21.0,−5.0)이다. 이 좌표 목록은 모델 입력 키 목록이 아니다. |
| FV2-134 | funwave_tvd_2.1_manual.pdf p.64 그림 18: `Modeled water surface at (top) t=6.4 s, (middle) t=8.4 s, (bottom) t=14.4 s.` | 해당 없음 | 코드 대조 대상 아님 — H | 수면 결과 그림만 있는 쪽이다. 급한 파면·산란·천해붕 쇄파를 재현했다는 p.65의 설명은 결과 평가다. |
| FV2-135 | funwave_tvd_2.1_manual.pdf p.62·65: `combining the measured data of the shelf and the analytical equation of the cone`; `from x = 0.0 m to -5.0 m with a` / p.65 `constant water depth of 0.78 m`; `Grid spacing used in the model is 0.1 m in both directions.`; `The wave height is 0.39 m` | `src/io.F:486` `CALL READ_STRING(DEPTH_FILE,FILE_NAME,'DEPTH_FILE',ierr)`; `:1132` `CALL READ_FLOAT(AMP_SOLI,FILE_NAME,'AMP',ierr)`; `:1147` `CALL READ_FLOAT(DEP_SOLI,FILE_NAME,'DEP',ierr)` | 일치 | 파일 지형과 초기 고립파 수심·파고 입력이 대응한다. 실험 지형의 합성과 수조 폭 자체는 외부 설정이다. |
| FV2-136 | funwave_tvd_2.1_manual.pdf p.65: `with centroid located at x = 5.0`; p.68: `XWAVEMAKER = 10.0 ! note that means x = 5 m because the domain starts at x = -5` | `src/samples.F:548` `SC=1.0_SP/COSH(B*(I-Xwavemaker/DX-1)*DX)`; `src/init.F:577` `Xco(Ibeg) = ZERO`; `src/misc.F:171` `Ibeg=Nghost+1`; `src/mod_global.F:129` `INTEGER, PARAMETER :: Nghost = 3`; `src/init.F:907–909`의 `IF(WaveMaker(1:7)=='INI_SOL') THEN`이 이 초기화를 호출한다. `src/samples.F:542`는 `! start from ghost cell`이라고 적는다. 최초 `cab9425:samples.F:507`도 같은 직렬식이다. `a99e3f8`(2018-01-25)은 병렬 원점만 iista로 바꿨다. | 불일치 — E（중간） | 직교 INI_SOL 중심은 Xco 원점에서 XWAVEMAKER보다 3DX만큼 왼쪽이다. p.68의 DX=0.1을 대입하면 모델 좌표는 9.7 m다. 실험 좌표로 옮기면 4.7 m다. ghost 시작 주석을 반대 증거로 반영하여 강도를 중간으로 낮춘다. 구면의 변동 DX에는 전 영역의 일정 3DX 차이를 일반화하지 않는다. [git 판정 근거](FUNWAVE-git-verify-E2.md). [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-137 | funwave_tvd_2.1_manual.pdf p.65 그림 19: `Time step variation.`; `The time step dropped to a minimum, at around t = 6.5 s`; `The local Froude number reached a maximum at t = 6.5 s` | 해당 없음 | 코드 대조 대상 아님 — H | 시간간격 결과와 Froude 수의 결과 해석이다. 현재 `ESTIMATE_DT` 구현을 실행 결과의 재검증으로 대체하지 않는다. |
| FV2-138 | funwave_tvd_2.1_manual.pdf p.66 그림 20: `Model/data comparisons of time series of surface elevation at (top) Gauge 1 - Gauge 9. Solid line: model, stars: data.`; p.65: `over-predicts the peak of wave runup.` | 해당 없음 | 불일치 — B | 2.1 p.66의 내부 범례는 실선 data·파선 model이다. 그림에는 캡션의 별표가 없다. 3.0 p.73 그림 23도 같은 충돌을 보인다. `funwave_tvd_3.0.tex` 2136행은 충돌하는 캡션을 유지한다. B는 캡션과 범례의 충돌에 한정한다. 인용 시 내부 범례의 실선 data·파선 model을 명시한다. Gauge 3의 처오름 첨두 과대 예측과 Gauge 5·6·8·9의 굴절·쇄파 평가는 본문의 결과 주장으로 적는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-139 | funwave_tvd_2.1_manual.pdf p.67 그림 21: `Solid line: model, dashed line: data.`; p.68: `An underprediction of the seaward velocity is found at ADV 2.`; `The velocity in the y-direction was not compared at ADV1 and ADV2 because the measured values were too small.` | 해당 없음 | 불일치 — B | 2.1 p.67의 내부 범례는 실선 data·파선 model이다. 캡션은 두 선의 의미를 반대로 적는다. 3.0 p.74 그림 24와 `funwave_tvd_3.0.tex` 2143행에도 같은 충돌이 있다. B는 캡션과 범례의 충돌에 한정한다. 인용 시 내부 범례의 실선 data·파선 model을 명시한다. 본문은 ADV 2의 해향 유속을 과소 예측했다고 보고한다. ADV 1·2의 y 유속은 측정값이 너무 작아 비교에서 제외했다고 적는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-140 | funwave_tvd_2.1_manual.pdf p.69: `read_result.m`; `plot_WG.m`; `plot_ADV_AB.m`; `plot_ADV_C.m` | 해당 없음 | 코드 대조 대상 아님 — H | 9개 압력계의 η와 3개 ADV의 u·v를 추출하고 비교하는 MATLAB 후처리 절차다. |

#### 2.4.3 중첩 예제

| 행 ID | 문서 원문 | 코드 원문 | 판정 | 이유 |
|---|---|---|---|---|
| FV2-141 | funwave_tvd_2.1_manual.pdf p.69: `a solitary wave of permanent form is undistorted as it moves from a large domain Grid_A to a smaller scale grid Grid_B.` | 해당 없음 | 코드 대조 대상 아님 — H | 파형 유지에 대한 결과 주장이다. |
| FV2-142 | funwave_tvd_2.1_manual.pdf p.69: `the computational domain is 6000m long with 10 m constant water depth. Grid size is 4 m.`; `Grid_B, with a grid size of dx=2m`; `The nesting boundary is at x=2000.0m in Grid_A.`; `The spherical mode is used` | `src/init.F:379` `Dx(I,J) = R_earth*Dphi_r*COS(Lat_theta(I,J))`; `src/io.F:495` `CALL READ_FLOAT(DEPTH_FLAT,FILE_NAME,'DEPTH_FLAT',ierr)` | 일치 | 10 m와 약 4 m·2 m 간격은 입력에 대응한다. 6000 m 길이와 경계 위치를 정하는 Mglob·Nglob·station.txt의 실제 내용은 입력 발췌에 없다. 그 실행 전제는 FV2-310에 적었다. |
| FV2-143 | funwave_tvd_2.1_manual.pdf p.69: `An initial solitary wave with an amplitude of 1m is centered at x=1000.0 m.`; p.70: `AMP = 0.1` | `src/io.F:1132` `CALL READ_FLOAT(AMP_SOLI,FILE_NAME,'AMP',ierr)` | 불일치 — B | 본문의 진폭 1 m와 입력의 0.1 m가 열 배 다르다. 초기 파고를 10배로 바꾸는 입력 보정은 없다. 그림 22의 세로축 첨두는 0.1이다. 3.0도 같은 모순을 유지한다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-144 | funwave_tvd_2.1_manual.pdf p.69: `output at gauges at x=2000.0m (i = 500, where i is grid number in x direction in Grid_A).` | `src/io.F:4032` `ista(i) = Nghost+dum1`; `src/misc.F:171` `Ibeg=Nghost+1`; `src/init.F:577` `Xco(Ibeg) = ZERO`; `:584` `Xco(I) = Xco(I-1)+DX(1,1)` | 불일치 — B | i,j 관측점 경로의 입력 i=500은 0부터 시작한 물리 좌표의 499번째 간격이다. 4 m를 쓰면 1996 m다. 2000 m에 해당하는 1부터 시작한 지점 번호는 501이다. 실제 각도 격자의 환산 오차는 이 한 격자 차이와 별개다. 구면 기본 관측점 경로의 조건은 FV2-311에 적었다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-145 | funwave_tvd_2.1_manual.pdf p.69–70: `/examples/sph_nesting /`; `/grid_A/`; `/make_nest_file/`; `/grid_B/`; `generate nesting input file using convert.f in /make_nest_file/.`; `use plot_ab.m to plot results.` | 해당 없음 | 코드 대조 대상 아님 — H | 사례 묶음의 디렉터리 안내·전처리·후처리 사용법이다. 이 보고서는 변환 프로그램의 내부를 모델 코드 완료 조건으로 추가하지 않는다. |
| FV2-146 | funwave_tvd_2.1_manual.pdf p.73 그림 22: `Solitary wave calculated in a larger domain Grid_A (upper) and in a nested smaller domain Grid_B (lower) at t=100s, 200s, 300s, and 400s.` | 해당 없음 | 코드 대조 대상 아님 — H | 두 영역의 결과 그림만 있는 쪽이다. [10-18 결론 검증 정정] |
| FV2-147 | funwave_tvd_2.1_manual.pdf p.70 절차 1: `the executive file should be compiled with ’-DCOUPLING’ turned OFF`; 절차 3: `the executive file should be compiled with ’-DCOUPLING’ turned ON` | `src/init.F:1168` `# if defined (COUPLING)`; `:1170` `CALL COUPLING_INITIAL`; `src/main.F:237–239` `# if defined (COUPLING)` / `TIME=TIME_COUPLING_1` / `# endif` | 일치 | 부모 영역은 결합 파일을 읽지 않는다. 자식 영역은 결합 파일의 첫 시각으로 모델 시계를 설정한다. 빌드 파일 위치의 현재 차이는 FV2-312에 적었다. |

### 2.5 참고문헌의 모든 항목

참고문헌 목록의 56개 항목을 p.72·74–77에서 셌다.
다음 행은 서지의 저자·연도와 제목을 식별한다.
제목 안의 수학 표기도 코드 방정식의 구현 주장으로 해석하지 않는다.
각 행의 판정은 H다.
이 판정은 논문 원문의 식·표·계수를 확인했다는 뜻이 아니다.
이 과제에는 외부 논문의 계수를 알아야만 나눌 코드 판정이 남지 않는다.

| 행 ID | 문서 원문 | 코드 | 판정 | 이유 |
|---|---|---|---|---|
| FV2-150 | funwave_tvd_2.1_manual.pdf p.72: Agnon, Madsen and Schäffer (1999), `A new approach to high-order Boussinesq models`, J. Fluid Mech. 399, 319–333 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-151 | funwave_tvd_2.1_manual.pdf p.72: Berkhoff, Booy and Radder (1982), `Verification of numerical wave propagation models for simple harmonic linear water waves`, Coast. Engrg. 6, 255–279 | 해당 없음 | 코드 대조 대상 아님 — H | §5.3 실험의 서지 항목이다. |
| FV2-152 | funwave_tvd_2.1_manual.pdf p.72: Bermùdez and Vàzquez (1994), `Upwind methods for hyperbolic conservation laws with source terms`, Comput. Fluids 23 (8), 1049–1071 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. [10-18 결론 검증 정정] |
| FV2-153 | funwave_tvd_2.1_manual.pdf p.72: Briggs, Synolakis and Harkins (1994), `Tsunami run- up on a conical island`, Proc., Waves-Physical and Numerical Modelling, 446–455 | 해당 없음 | 코드 대조 대상 아님 — H | §5.4 본문의 Briggs et al. (1995)와 이 항목의 연도는 다르다. 서지 차이는 코드 입력 판정과 분리한다. |
| FV2-154 | funwave_tvd_2.1_manual.pdf p.72: Brown et al. (2009), `Surf zone diffusivity on a rip-channeled beach`, J. Geophys. Res. 114, C11015, doi:10.1029/2008JC005158 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-155 | funwave_tvd_2.1_manual.pdf p.72: Chen et al. (1999), `Boussinesq modelling of a rip current system`, J. Geophys. Res. 104, 20,617–20,637 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-156 | funwave_tvd_2.1_manual.pdf p.72: Chen et al. (2000), `Boussinesq modeling of wave transformation, breaking and runup. II: 2D`, J. Waterway, Port, Coastal and Ocean Engineering 126, 48–56 | 해당 없음 | 코드 대조 대상 아님 — H | 원뿔섬 검증 설명이 인용한 서지다. |
| FV2-157 | funwave_tvd_2.1_manual.pdf p.74: Chen et al. (2003), `Boussinesq modeling of longshore currents`, Journal of Geophysical Research 108(C11), 3362, doi:10.1029/2002JC001308 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-158 | funwave_tvd_2.1_manual.pdf p.74: Chen, Kaihatu and Hwang (2004), `Incorporation of Wind Effects Into Boussinesq Wave Models`, J. Waterway, Port, Coastal and Ocean Engineering 130, 312–321 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-159 | funwave_tvd_2.1_manual.pdf p.74: Chen (2006), `Fully nonlinear Boussinesq-type equations for waves and currents over porous beds`, Journal of Engineering Mechanics 132 (2), 220–230 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-160 | funwave_tvd_2.1_manual.pdf p.74: Erduran, Ilic and Kutija (2005), `Hybrid finite-volume finite-difference scheme for the solution of Boussinesq equations`, Int. J. Numer. Meth. Fluid. 49, 1213–1232 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-161 | funwave_tvd_2.1_manual.pdf p.74: Gobbi, Kirby and Wei (2000), `A fully nonlinear Boussinesq model for surface waves. II. Extension to` $O(kh^4)$, Journal of Fluid Mechanics 405, 181–210 | 해당 없음 | 코드 대조 대상 아님 — H | 제목의 차수 표기는 수학적 서지 정보다. |
| FV2-162 | funwave_tvd_2.1_manual.pdf p.74: Gottlieb, Shu and Tadmore (2001), `Strong stability-preserving high-order time discretization methods`, SIAM Review 43 (1), 89–112 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. 저자 철자 Tadmore는 인쇄본을 보존했다. |
| FV2-163 | funwave_tvd_2.1_manual.pdf p.74: Hansen and Svendsen (1979), `Regular waves in shoaling water: Experimental data`, Tech. Rep. ISVA Ser. 21, Technical Univ. of Denmark | 해당 없음 | 코드 대조 대상 아님 — H | §5.1 실험의 서지다. |
| FV2-164 | funwave_tvd_2.1_manual.pdf p.74: Kennedy et al. (2000), `Boussinesq modeling of wave transformation, breaking and runup. I: 1D`, J. Waterway, Port, Coastal and Ocean Engineering 126, 39–47 | 해당 없음 | 코드 대조 대상 아님 — H | 쇄파 모형 논문의 서지 항목이다. [10-18 결론 검증 정정] |
| FV2-165 | funwave_tvd_2.1_manual.pdf p.74: Kennedy et al. (2001), `Boussinesq-type equations with improved nonlinear performance`, Wave Motion 33, 225–243 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-166 | funwave_tvd_2.1_manual.pdf p.74: Kim, Cho and Kim (2008), `Well-balanced scheme between flux and source terms for computation of shallow-water equations over irregular bathymetry`, Journal of Engineering Mechanics 134, 277–290 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-167 | funwave_tvd_2.1_manual.pdf p.74: Kim, Lynett and Socolofsky (2009), `A depth-integrated model for weakly dispersive, turbulent, and rotational fluid flows`, Ocean Modeling 27, 198–214 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. [10-18 결론 검증 정정] |
| FV2-168 | funwave_tvd_2.1_manual.pdf p.74: Kim (2009), `Turbulent flow and transport modeling by long waves and currents`, Ph.D. dissertation, Texas A&M University | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-169 | funwave_tvd_2.1_manual.pdf p.74: Kirby et al. (1998), `FUNWAVE 1.0, Fully nonlinear Boussinesq wave model. Documentation and users manual`, Report CACR-98-06 | 해당 없음 | 코드 대조 대상 아님 — H | 예제 계보를 설명한 이전 매뉴얼의 서지다. |
| FV2-170 | funwave_tvd_2.1_manual.pdf p.74: Kirby et al. (2004), `Propagation of short dispersive tsunami waves in ocean basins`, EOS Transactions of the AGU 85 (47), Abstract OS21E-02 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. [10-18 결론 검증 정정] |
| FV2-171 | funwave_tvd_2.1_manual.pdf p.75: Kirby et al. (2012), `Sensitivity analysis of trans-oceanic tsunami propagation to dispersive and Coriolis effects`, Ocean Modelling, `under revision` | 해당 없음 | 코드 대조 대상 아님 — H | 출판 상태는 이 인쇄본의 서지 정보다. |
| FV2-172 | funwave_tvd_2.1_manual.pdf p.75: Liang and Marche (2009), `Numerical resolution of well-balanced shallow water equations with complex source terms`, Advances in Water Resources 32, 873–884 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-173 | funwave_tvd_2.1_manual.pdf p.75: Long and Kirby (2006), `Boussinesq modeling of waves, currents and sediment transport`, Research Report CACR-06-02 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-174 | funwave_tvd_2.1_manual.pdf p.75: Lynett, Wu and Liu (2002), `Modeling wave runup with depth-integrated equations`, Coastal Engineering 46, 89–107 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-175 | funwave_tvd_2.1_manual.pdf p.75: Madsen and Srensen (1992), `A new form of the Boussinesq equations with improved linear dispersion characteristics. Part 2. A slowly-varying bathymetry`, Coastal Engineering 18 (3-4), 183–204 | 해당 없음 | 코드 대조 대상 아님 — H | 인쇄 저자 철자 Srensen을 보존했다. |
| FV2-176 | funwave_tvd_2.1_manual.pdf p.75: Mase and Kirby (1992), `Hybrid frequency-domain KdV equation for random wave transformation`, Proc., 23rd Int. Conf. Coast. Eng., 474–487 | 해당 없음 | 코드 대조 대상 아님 — H | §5.2 실험의 서지다. |
| FV2-177 | funwave_tvd_2.1_manual.pdf p.75: Naik, Naik and Nicoules (1993), `Parallelization of a class of implicit finite difference schemes in computational fluid dynamics`, International Journal of High Speed Computing 5, 1–50 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-178 | funwave_tvd_2.1_manual.pdf p.75: Ning et al. (2008), `Boussinesq cut-cell model for non-linear wave interaction with coastal structures`, International Journal for Numerical Methods in Fluids 57 (10), 1459–1483 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-179 | funwave_tvd_2.1_manual.pdf p.75: Nwogu (1993), `An alternative form of the Boussinesq equations for nearshore wave propagation`, Journal of Waterway, Port, Coastal and Ocean Engineering 119 (6), 618–638 | 해당 없음 | 코드 대조 대상 아님 — H | 초기 고립파 설명이 가리키는 이론 계보의 서지다. |
| FV2-180 | funwave_tvd_2.1_manual.pdf p.75: Nwogu and Demirbilek (2001), `BOUSS-2D: A Boussinesq wave model for coastal regions and harbors`, ERDC/CHL TR-01-25 | 해당 없음 | 코드 대조 대상 아님 — H | 다른 모델의 보고서 서지다. |
| FV2-181 | funwave_tvd_2.1_manual.pdf p.75: Roeber, Cheung and Kobayashi (2010), `Shock-capturing Boussinesq-type model for nearshore wave processes`, Coastal Engineering 57, 407–423 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-182 | funwave_tvd_2.1_manual.pdf p.75: Rogers, Borthwick and Taylor (2003), `Mathematical balancing of flux gradient and source terms prior to using Roe’s approximate Riemann solver`, Journal of Computational Physics 192, 422–451 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-183 | funwave_tvd_2.1_manual.pdf p.75: Shi et al. (2012 a), `A high-order adaptive time-stepping TVD solver for Boussinesq modeling of breaking waves and coastal inundation`, Ocean Modelling 43-44, 36–51 | 해당 없음 | 코드 대조 대상 아님 — H | 본 모델의 이론·수치해법 계보에 관한 서지다. |
| FV2-184 | funwave_tvd_2.1_manual.pdf p.76: Shi, Kirby and Tehranirad (2012 b), `Tsunami benchmark results for spherical coordinate`, CACR 2012-02 | 해당 없음 | 코드 대조 대상 아님 — H | 구면 벤치마크 보고서의 서지다. |
| FV2-185 | funwave_tvd_2.1_manual.pdf p.76: Shi et al. (2011), `FUNWAVE-TVD, Version 1.0, users’ manual and benchmark tests`, CACR 2011-04 | 해당 없음 | 코드 대조 대상 아님 — H | 이전 매뉴얼의 서지다. |
| FV2-186 | funwave_tvd_2.1_manual.pdf p.76: Shi et al. (2001), `A fully nonlinear Boussinesq model in generalized curvilinear coordinates`, Coastal Engineering 42, 337–358 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-187 | funwave_tvd_2.1_manual.pdf p.76: Shiach and Mingham (2009), `A temporally second-order accurate Godunov-type scheme for solving the extended Boussinesq equations`, Coastal Engineering 56, 32–45 | 해당 없음 | 코드 대조 대상 아님 — H | §5.1의 선행 연구 서지다. |
| FV2-188 | funwave_tvd_2.1_manual.pdf p.76: Sitanggang and Lynett (2005), `Parallel computation of a highly nonlinear Boussinesq equation model through domain decomposition`, Int. J. Num. Meth. Fluids 49, 57–74 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-189 | funwave_tvd_2.1_manual.pdf p.76: Smagorinsky (1963), `General circulation experiments with the primitive equations. I. The basic experiment`, Mon. Weather Rev. 91, 99–165 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-190 | funwave_tvd_2.1_manual.pdf p.76: Swigler and Lynett (2011), `Laboratory study of the three-dimensional turbulence and kinematic properties associated with a solitary wave traveling over an alongshore-variable, shallow shelf`, `in review` | 해당 없음 | 코드 대조 대상 아님 — H | §5.5 실험의 서지다. |
| FV2-191 | funwave_tvd_2.1_manual.pdf p.76: Synolakis et al. (2007), `Standards, criteria, and procedures for NOAA evaluation of tsunami numerical models`, NOAA Tech. Memo. OAR PMEL-135 | 해당 없음 | 코드 대조 대상 아님 — H | §5.4가 Appendix A §3.3을 가리킨다. 이 행은 그 인용의 서지 항목이다. [10-18 결론 검증 정정] |
| FV2-192 | funwave_tvd_2.1_manual.pdf p.76: Tehranirad et al. (2011), `Tsunami benchmark results for fully nonlinear Boussinesq wave model FUNWAVE-TVD, Version 1.0`, CACR-11-02 | 해당 없음 | 코드 대조 대상 아님 — H | 5장 서문의 벤치마크 서지다. |
| FV2-193 | funwave_tvd_2.1_manual.pdf p.76: Tehranirad et al. (2013), `Tsunami benchmark results for fully nonlinear Boussinesq wave model FUNWAVE-TVD, Version 2.1`, CACR-13-10 | 해당 없음 | 코드 대조 대상 아님 — H | Version 2.1 벤치마크 서지다. |
| FV2-194 | funwave_tvd_2.1_manual.pdf p.76: Tehranirad, Shi and Kirby (2012 b), `Tsunami benchmark results for spherical coordinate`, CACR 2013-10 | 해당 없음 | 코드 대조 대상 아님 — H | 인쇄 연도·보고서 번호를 그대로 기록했다. FV2-184와 저자·연도·번호의 대응이 다르다. 이를 코드 동작 차이로 바꾸지 않는다. |
| FV2-195 | funwave_tvd_2.1_manual.pdf p.76: Ting and Kirby (1994), `Observation of undertow and turbulence in a laboratory surf zone`, Coast. Eng. 24, `5180` | 해당 없음 | 코드 대조 대상 아님 — H | 인쇄 쪽 표기 5180을 그대로 보존했다. |
| FV2-196 | funwave_tvd_2.1_manual.pdf p.76: Tonelli and Petti (2009), `Hybrid finite volume - finite difference scheme for 2DH improved Boussinesq equations`, Coast. Engrng. 56, 609–620 | 해당 없음 | 코드 대조 대상 아님 — H | §5.1의 선행 연구 서지다. |
| FV2-197 | funwave_tvd_2.1_manual.pdf p.77: Tonelli and Petti (2010), `Finite volume scheme for the solution of 2D extended Boussinesq equations in the surf zone`, Ocean Engrg. 37, 567–582 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. [10-18 결론 검증 정정] |
| FV2-198 | funwave_tvd_2.1_manual.pdf p.77: Toro (2009), `Riemann solvers and numerical methods for fluid dynamics: a practical introduction`, Third edition, Springer, New York | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-199 | funwave_tvd_2.1_manual.pdf p.77: Wei et al. (1995), `A fully nonlinear Boussinesq model for surface waves: Part I. Highly nonlinear unsteady waves`, Journal of Fluid Mechanics 294, `7192` | 해당 없음 | 코드 대조 대상 아님 — H | 인쇄 쪽 표기 7192를 보존했다. |
| FV2-200 | funwave_tvd_2.1_manual.pdf p.77: Wei and Kirby (1995), `A time-dependent numerical code for extended Boussinesq equations`, Journal of Waterway, Port, Coastal and Ocean Engineering 120, 251–261 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. 예제 주석의 Wei and Kirby 1999와 이 항목의 1995를 같은 서지라고 단정하지 않는다. |
| FV2-201 | funwave_tvd_2.1_manual.pdf p.77: Yamamoto and Daiguji (1993), `Higher-order-accurate upwind schemes for solving the compressible Euler and NavierStokes equations`, Computers and Fluids 22 (2/3), `529270` | 해당 없음 | 코드 대조 대상 아님 — H | 인쇄 저자·쪽 표기를 보존했다. [10-18 결론 검증 정정] |
| FV2-202 | funwave_tvd_2.1_manual.pdf p.77: Yamamoto, Kano and Daiguji (1998), `An efficient CFD approach for simulating unsteady hypersonic shockshock interference flows`, Computers and Fluids 27 (56), 571–580 | 해당 없음 | 코드 대조 대상 아님 — H | 인쇄 제목·권호 표기를 보존했다. |
| FV2-203 | funwave_tvd_2.1_manual.pdf p.77: Zelt (1991), `The runup of nonbreaking and breaking solitary waves`, Coastal Engineering 15, 205–246 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-204 | funwave_tvd_2.1_manual.pdf p.77: Zhen (2004), `On the numerical properties of staggered vs. non-staggered grid schemes for a Boussinesq equation model`, MCE Thesis, University of Delaware | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |
| FV2-205 | funwave_tvd_2.1_manual.pdf p.77: Zhou et al. (2001), `The surface gradient method for the treatment of source terms in the shallow-water equations`, Journal of Computational Physics 168, 1–25 | 해당 없음 | 코드 대조 대상 아님 — H | 서지 항목이다. |

### 2.6 같은 예제의 3.0 문서와의 차이

여기서 예제 설정값의 변경은 H다.
이 변경을 코드 판 차이 A로 세지 않는다.
A는 실제 구현 변경 커밋을 확인한 행에만 적용한다.
다음 표에 적지 않은 입력 키·값은 §2.3의 같은 사례와 같다.
3.0의 새 사례인 Vincent–Briggs와 수중 사주는 2.1의 같은 예제가 아니므로 이 대조의 대상에 추가하지 않는다.

| 행 ID | 같은 예제 | 두 문서의 원문과 차이 | 코드와 판정 |
|---|---|---|---|
| FV2-260 | 해빈 | funwave_tvd_2.1_manual.pdf p.43–48 §5.1은 권파형·붕파형과 세 해상도를 설명한다. funwave_tvd_3.0.pdf p.45–47 §5.1은 권파형 한 해상도에서 shock-capturing과 eddy-viscosity를 비교한다. 3.0은 `Xslp = 30.0`, `Mglob = 2000`, `AMP_WK = 0.018`, `Delta_WK = 0.5`, `DIRECT_SPONGE = T`, `Sponge_west_width = 12.0`, `R_sponge = 0.85`, `HIGH_ORDER = THIRD`로 바꾼다. 3.0은 2.1의 `Time_ramp = 1.0` 줄을 싣지 않는다. 3.0은 `RESULT_FOLDER = your output folder`, `VISCOSITY_BREAKING = F ! switch to T for the other case`, `Cbrk1 = 0.65`, `Cbrk2 = 0.15`, `WAVEMAKER_Cbrk = 0.65`, `Friction_Matrix=F`, `Cd_file= cd.txt`, `NumberStations = 119`, `STATIONS_FILE = gauge.txt`를 추가한다. 진폭 주석은 `this value is smaller than the report of Hansen and Svendsen, but matches the measured data`다. | C 문서 누락 — C는 3.0 p.45–46 발췌의 Time_ramp 생략에 한정한다. 3.0 p.37은 이 키를 WK_REG의 필요 입력으로 적는다. `src/io.F:1517–1519`는 누락 시 0을 넣고 `src/sources.F:109–110`은 그 값을 분모에 사용한다. 3.0 해빈은 사례 설정과 비교할 쇄파 방식을 바꿨다. 현재 코드와 대조한 차이는 Time_ramp 생략이다(FV2-321). Cbrk2 기본값 주장은 FV2-266의 B로, 마찰 키 변경은 FV2-267의 A로 구분한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-261 | 불규칙파 | funwave_tvd_2.1_manual.pdf p.45·49–53 §5.2와 funwave_tvd_3.0.pdf p.47–52 §5.2는 같은 사례다. 3.0 p.51은 `DIRECT_SPONGE = T`로 바꾼다. 3.0 p.52는 `HIGH_ORDER = THRID`로 인쇄한다. 식 (79)는 3.0 p.48에서 식 (106)이 된다. 2.1 p.45와 3.0 p.48의 파고계 수심 목록은 모두 30 cm를 포함한다. 3.0 p.49 그림 5에도 `h=30.0cm` 패널이 있다. | B 문서 오기 — 3.0 p.48의 수심 목록에도 `h=47, 35, 30, 25, 20, 17.5, 15, 12.5, 10, 7.5, 5, and 2.5 cm`가 있다. 30 cm 누락이라는 기존 판단을 정정한다. `src/fluxes.F:101–103`은 THRID를 기본 구성으로 보낸다. B는 3.0 p.52의 THRID 오기에 한정한다(FV2-270). 두 문서의 파고계 수심 목록에는 모두 30 cm가 있다. 2.1 p.53의 실제 입력은 FOURTH이며, 3.0의 THRID는 현재 코드에서 기본 구성 경로로 간다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-262 | 천퇴 | funwave_tvd_2.1_manual.pdf p.53–57 §5.3과 funwave_tvd_3.0.pdf p.52–56 §5.3은 같은 사례다. 3.0 p.55는 `SPONGE_ON = T`를 `DIRECT_SPONGE = T`로 바꾼다. 다른 키와 값은 같다. 그림 번호는 9·10에서 7·8로 바뀐다. | 일치 — `src/io.F:2285`는 DIRECT_SPONGE를 읽는다. `src/init.F:966–970`의 `IF(DIRECT_SPONGE)THEN`은 직접 감쇠층을 초기화한다. 3.0 천퇴의 DIRECT_SPONGE=T는 실제 읽기와 초기화 조건에 맞는다. 2.1의 SPONGE_ON은 FV2-049·121의 D와 같다. 그 밖의 입력값은 두 문서에서 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-263 | 원뿔섬 | funwave_tvd_2.1_manual.pdf p.57–62 §5.4는 funwave_tvd_3.0.pdf p.65–70 §5.6으로 이동한다. 2.1 p.60과 3.0 p.69의 사례 A 입력은 모두 `AMP = 0.0144`다. 3.0은 `DIRECT_SPONGE = F`, `FRICTION_SPONGE = F`, `DIFFUSION_SPONGE = F`를 명시한다. 3.0은 나머지 설정값·LAGTIME·관측점 설명을 유지한다. 그림 번호는 11–16에서 15–20으로 바뀐다. 3.0 p.65–66도 전경·정의도·배치도 캡션 아래 시계열 곡선을 싣는다. 표 1의 12개 오차 값은 같다. | 일치 — `src/io.F:1101·1132`는 INI_SOL의 AMP를 읽는다. `:2280–2293`은 세 완충층 스위치를 읽으며 `src/init.F:966–989`의 초기화는 각 참 조건에 따른다. 두 판의 사례 A 진폭 0.0144 m는 INI_SOL의 AMP 입력과 맞는다. 3.0의 세 완충층 F는 각 초기화 분기를 끈다. 다른 별도 차이는 LAGTIME의 FV2-047, 관측점 설명의 FV2-131, 그림 편집의 FV2-124–126과 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-264 | 천해붕 | funwave_tvd_2.1_manual.pdf p.62–69 §5.5는 funwave_tvd_3.0.pdf p.70–76 §5.7로 이동한다. 3.0 p.75–76은 `DIRECT_SPONGE = F`, `FRICTION_SPONGE = F`, `DIFFUSION_SPONGE = F`를 명시한다. 나머지 입력 키와 값은 같다. 3.0은 2.1의 그림 19 시간간격 곡선과 6.5초 Froude 설명을 싣지 않는다. 3.0 p.73–74의 수면·유속 그림 캡션과 실제 범례의 차이는 2.1 p.66–67과 같다. | 일치 — `src/io.F:2280–2293`은 세 스위치를 읽고 각각 누락 시 거짓으로 둔다. `src/init.F:966–989`은 각 참 조건에서만 완충층 초기화를 시작한다. 3.0 천해붕의 DIRECT_SPONGE·FRICTION_SPONGE·DIFFUSION_SPONGE=F는 세 완충층을 끄는 코드 조건과 맞는다. 초기 중심의 별도 결함 후보는 FV2-136의 중간 강도 E다. 그림 캡션 충돌은 FV2-138·139의 B와 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-265 | 중첩 | funwave_tvd_2.1_manual.pdf p.69–73 §5.6은 funwave_tvd_3.0.pdf p.76–80 §5.8로 이동한다. Grid_A·Grid_B 입력의 키와 값은 같다. 본문의 `amplitude of 1m`도 남는다. 그림 22는 그림 25가 된다. 3.0도 COUPLING을 부모에서 끄고 자식에서 켜라고 적는다. | H — 절·그림 번호와 배치가 바뀐다. 입력값과 코드 적용 조건은 FV2-079–085·FV2-143–147과 같다. |
| FV2-266 | 3.0 해빈의 기본값 주장 | funwave_tvd_3.0.pdf p.45: `we adopted Cbrk1 =0.65 and Cbrk2=0.15, which are default values from Kennedy et al and this model.`; p.46: `Cbrk1 = 0.65`, `Cbrk2 = 0.15` | 불일치 — B. `src/io.F:3079` `CALL READ_FLOAT(Cbrk1,FILE_NAME,'Cbrk1',ierr)` 뒤 `:3081` `Cbrk1 = 0.65_SP`는 일치한다. `:3101` `CALL READ_FLOAT(Cbrk2,FILE_NAME,'Cbrk2',ierr)` 뒤 `:3103` `Cbrk2 = 0.35_SP`는 다르다. 문서 저장 시점의 선언도 0.35다. 명시 입력 0.15 자체는 정상적으로 읽는다. 이 B는 본 모델의 누락 기본값 주장에만 적용한다. Kennedy 원논문의 기본값은 여기서 판정하지 않는다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-267 | 3.0 해빈의 마찰 키 | funwave_tvd_3.0.pdf p.46: `Friction_Matrix=F`, `Cd_file= cd.txt` | 불일치 — A. `src/io.F:2738` `CALL READ_LOGICAL(IN_Cd,FILE_NAME,'FRICTION_MATRIX',ierr)`와 `:2753` `CALL READ_STRING(CD_FILE,FILE_NAME,'FRICTION_FILE',ierr)`가 실제 키다. 파서는 대소문자를 구별한다. 현재 TVD는 예제의 두 키를 읽지 않는다. 문서 시점 코드는 두 키를 읽었다. 2019-07-25의 9bae2f6이 이름을 바꿨다. GPU 코드는 이전 키를 유지한다. FRICTION_MATRIX의 누락 기본값이 거짓이라 이 사례에서는 고정 Cd 경로가 우연히 유지된다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-268 | 3.0 천퇴의 줄 형식 | funwave_tvd_3.0.pdf p.56의 연속 두 줄: `NumberStations = 0` / `DEPTH_OUT = T` | 일치. 원해상도 이미지와 PDF 글자 기준선 y=288.292630·301.841630에서 두 줄을 확인했다. 2.1 p.57도 두 줄이다. `src/mod_input.F:287` `READ(10,'(A)',END=100) TEXT_READ`와 맞는다. |
| FV2-269 | 3.0 출력 파일 이름 | funwave_tvd_3.0.pdf p.44: `sta_00001, sta_00002 ....`; funwave_tvd_2.1_manual.pdf p.43: `sta_0001, sta_0002 ....` | 불일치 — B. 현재 `src/io.F:3869` `write(file_name(1:4),'(I4.4)') i`는 네 자리다. 3.0의 문서 시점 코드도 네 자리다. 3.0은 장 출력 이름을 다섯 자리로 고쳤지만 관측점 이름도 다섯 자리로 적었다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-270 | 3.0 불규칙파의 옵션 철자 | funwave_tvd_3.0.pdf p.52: `HIGH_ORDER = THRID`; 2.1 p.53: `HIGH_ORDER = FOURTH` | 불일치 — B. THRID는 THIRD의 철자 오기다. `24a88c3:src/fluxes.F:73–75`의 `ELSE` / `CALL DelxyFun` / `CALL CONSTRUCTION`은 THRID도 기본 분기로 보낸다. 현재 `src/fluxes.F:101–103`도 같은 기본 분기다. 따라서 현재 실행 경로는 THIRD와 같지만 THRID라는 별도 수치법은 아니다. 2.1의 실제 대조 원문은 p.53 `HIGH_ORDER = FOURTH`다. git 판정 파일의 p.52 `THIRD` 인용은 쪽 이미지와 달라 바로잡는다. B 판정은 유지한다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |

## 3 코드에만 있는 처리

이 절은 대상 예제를 읽거나 실행 경로를 선택할 때 영향을 주는 추가 처리를 모은다.
선박·기상·표사 같은 별도 예제를 새 대조 대상으로 추가하지 않는다.
`코드에만`은 이 과제의 p.43–77 예제 설명에 빠졌다는 뜻이다.
다른 장에도 설명이 전혀 없다는 뜻은 아니다.

FV2-302의 직접 완충층은 `src/main.F:483–485`의 다음 조건에서 적용한다.

```fortran
       IF(DIRECT_SPONGE)THEN
           CALL SPONGE_DAMPING
       ENDIF
```

`src/sponge.F:58–62`의 적용 원문은 다음과 같다.

```fortran
      IF(MASK(I,J)>ZERO)THEN
       ETA(I,J)=ETA(I,J)/SPONGE(I,J)
      ENDIF
       U(I,J)=U(I,J)/SPONGE(I,J)
       V(I,J)=V(I,J)/SPONGE(I,J)
```

FV2-120의 양쪽 측벽은 비주기·비결합 직교 경계와 대응한다.
`src/bc.F:166–167`은 `Q(I,Jbeg)=ZERO`와 `Fy(I,Jbeg)=ZERO`다.
`src/bc.F:199–200`은 `Q(I,Jend1)=ZERO`와 `Fy(I,Jend1)=ZERO`다.
이 대응은 천퇴 자료 파일이 실험 지형과 같다는 검증이 아니다.

FV2-266·FV2-403의 계수는 `src/breaker.F:124–126`에서 다음 임계값에 들어간다.

```fortran
     tmp3=SQRT(GRAV*MAX(MinDepthFrc,H(I,J)))
     tmp1=Cbrk1*tmp3
     tmp2=Cbrk2*tmp3
```

| 행 ID | 문서와의 관계 | 코드 원문 | 판정 | 영향 |
|---|---|---|---|---|
| FV2-300 | 입력 블록은 키 형식 검사의 세부 규칙을 쓰지 않는다. | `src/mod_input.F:297` `IF(ADJUSTL(TRIM(TMPV_NEXT)) == TRIM(MatchCharacter))THEN`; `:340` `DotLocation = index(VREAD,".")`; `:341–345` `IF(DotLocation .NE. 0) then` / `VTYPE = "float"` / `ELSE` / `VTYPE = "INTEGER"` / `ENDIF` | 코드에만 — C | 대소문자 구분은 2.1 p.34·3.0 p.34와 `funwave_tvd_3.0.tex` 1061–1062행에 이미 명시되어 있다. 누락은 한 줄의 첫 `=`를 기준으로 읽는 규칙과 실수형 판별 규칙이다. `src/mod_input.F:295–298`과 `:156–164`가 각각 이를 적용한다. 입력은 한 줄에 한 대입문으로 적는다. 대소문자 구분은 두 매뉴얼의 명시 규칙이다. 현재 READ_FLOAT는 소수점이 없는 값을 float로 판정하지 않고 중단하므로 예제 실수의 소수점을 보존한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-301 | 2.1 예제는 VISCOSITY_BREAKING을 명시하지 않는다. p.44는 Boussinesq에서 NSWE로 전환했다고 설명한다. | `src/io.F:2689` `CALL READ_LOGICAL(VISCOSITY_BREAKING,FILE_NAME,'VISCOSITY_BREAKING',ierr)`; `:2691` `VISCOSITY_BREAKING = .TRUE.`; `src/masks.F:177–180` `IF(VISCOSITY_BREAKING)THEN` / `! dont use mask9 for viscosity breaking` / `MASK9tmp(I,J)= 1` / `ELSE` | 코드에만 — A | 현재 TVD 기본값은 점성 쇄파다. 이 분기는 SWE_ETA_DEP 전환 검사를 우회한다. 문서 저장 시점에는 기본값이 거짓이었다. 2019-06-16 변경 커밋은 §5에 적었다. GPU 기본값은 거짓이다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-302 | SPONGE_ON만 있는 예제는 현재 세 완충층을 구분하지 않는다. | `src/io.F:2280–2293`의 READ_LOGICAL 뒤 `DIFFUSION_SPONGE = .FALSE.`, `DIRECT_SPONGE = .FALSE.`, `FRICTION_SPONGE = .FALSE.`; `:2320` `CALL READ_FLOAT(Csp,FILE_NAME,'Csp',ierr)`; `:2322` `Csp = 0.1_SP`; `:2353` `CALL READ_FLOAT(CDsponge,FILE_NAME,'CDsponge',ierr)`; `:2355` `CDsponge = 5.0_SP` | 코드에만 — C | 세 완충층과 Csp·CDsponge의 의미는 3.0 p.39 및 `funwave_tvd_3.0.tex` 1270–1278행에 있다. 누락은 2.1 예제의 현행 스위치 구분과 누락 기본값이다. `src/init.F:966–989`는 각 스위치가 참인 경우에 대응 완충층을 초기화한다. 2.1 예제의 SPONGE_ON 대신 3.0 p.39의 세 스위치를 사용한다(FV2-049). 세 스위치의 누락 기본값은 거짓이다. DIFFUSION_SPONGE가 참이면 Csp를 읽고 누락 시 0.1을 쓴다. FRICTION_SPONGE가 참이면 CDsponge를 읽고 누락 시 5를 쓴다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-303 | 예제의 폭과 R_sponge·A_sponge는 지정값이다. | `src/io.F:2377` `Sponge_west_width = 0.0_SP`; `:2391` `Sponge_east_width = 0.0_SP`; `:2405` `Sponge_south_width = 0.0_SP`; `:2419` `Sponge_north_width = 0.0_SP`; `:2433` `R_sponge = 0.85_SP`; `:2447` `A_sponge = 5.0_SP` | 코드에만 — C | 2.1 p.38·3.0 p.39·Intro-TN p.12 및 `funwave_tvd_3.0.tex` 1280–1290행은 폭·감쇠율·최대 감쇠를 설명한다. R_sponge의 0.85–0.95 범위와 A_sponge의 약 5.0은 명시된 기본값과 구별한다. 읽기 조건은 `src/io.F:2374` `IF(DIFFUSION_SPONGE.OR.DIRECT_SPONGE.OR.FRICTION_SPONGE)THEN`이다. 세 완충층 중 하나를 켠 경우 네 폭과 R_sponge·A_sponge를 읽는다. 이 읽기 구간의 누락 기본값은 네 폭 0, R_sponge 0.85, A_sponge 5다. C는 이 누락 기본값 설명에 한정한다. [10-18 결론 검증 보완] |
| FV2-304 | funwave_tvd_2.1_manual.pdf p.49는 `The toe of the slope starts at x = 10 m.`라고 적는다. 예제는 SLP·Xslp를 같은 지형 설정으로 쓴다. | 직교 병렬 `src/init.F:732–734` `DO I=INT(Xslp/DX)+1,Mglob` / `VarGlob(I,J) = Depth_Flat-SLP*(I-(INT(Xslp/DX)+1))*DX` / `ENDDO`; 직교 직렬 `:767–769` `DO I=INT(Xslp/DX)+1+Ibeg,Iend` / `Depth(I,J) = Depth_Flat-SLP*(I-(INT(Xslp/DX)+1+Ibeg))*DX` / `ENDDO` | 불일치 — E（강함） | 해석: 같은 Xslp를 준 직교 직렬 경로의 경사 영점은 병렬보다 DX만큼 오른쪽이다. ghost 원점을 맞춘 뒤에도 차이가 남는다. 불규칙파의 정밀 산술값은 병렬 10.00 m와 직렬 10.04 m다. 두 값은 입력 DX=0.04와 두 코드 식에서 계산했다. 반대 근거 검색은 §5에 적었다. 최초 `cab9425:init.F:559·591`부터 이 차이가 있다. `436e692`(2020-05-18)의 ghost 처리 수정은 경사 원점 식을 바꾸지 않았다. `TVD/Makefile:5`의 `PARALLEL    = true`와 `TVD/GNUMake/Makefile:5`의 `PARALLEL    = false`에서 각각 두 경로가 선택된다. [git 판정 근거](FUNWAVE-git-verify-E2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-305 | p.52·56은 Ywidth_WK를 수조 폭보다 크게 주라고 적는다. Yc_WK는 예제에 없다. | `src/io.F:1011` 및 `:1443` `CALL READ_FLOAT(Yc_WK,FILE_NAME,'Yc_WK',ierr)`; `:1013` 및 `:1445` `Yc_WK = ZERO`; `src/init.F:1253` `IF(ABS(ymk_wk(J)-Yc_WK)<Ywidth_WK/2.0_SP) THEN`; `:1264` `IF(ABS(xmk_wk(I)-Xc_WK)<Width_WK) THEN` | 코드에만 — C | Yc_WK 자체는 2.1 p.37·3.0 p.37에 있다. C는 2.1 p.52·56 예제에 없는 Yc_WK 기본값과 엄격한 범위 조건에 한정한다. `src/init.F:1253`의 `<`는 경계를 포함하지 않는다. WK_TIME_SERIES·WK_REG의 Yc_WK 누락 기본값은 0이다. y 방향 활성 격자는 `IF(ABS(ymk_wk(J)-Yc_WK)<Ywidth_WK/2.0_SP) THEN`으로 고른다. 폭의 절반과 같은 거리에 있는 점은 제외한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-306 | 예제는 MinDepth와 MinDepthFrc를 독립된 입력 줄로 쓴다. | `src/io.F:2947` `!  merge two parameters into the minimum one, change to min according to Harris 11/13/2023`; `:2948` `MinDepthFrc=MIN(MinDepthFrc,MinDepth)`; `:2949` `MinDepth=MinDepthFrc` | 코드에만 — A | 현재 TVD는 두 수심을 작은 값 하나로 병합한다. 모든 0.001·0.001 예제 값은 바뀌지 않는다. GPU는 MAX로 병합한다. 서로 다른 값을 쓰는 경우의 판 차이는 §5의 이력으로 확인했다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-307 | 공간 마찰장은 2.1 p.39·3.0 p.40·Intro-TN p.12 및 `funwave_tvd_3.0.tex` 1317–1326행에 있다. MANNING 조건은 2.1 p.9·34와 3.0 p.10·34에 있다. | `src/io.F:2738` `CALL READ_LOGICAL(IN_Cd,FILE_NAME,'FRICTION_MATRIX',ierr)`; `:2740` `IN_Cd = .FALSE.`; `:2753` `CALL READ_STRING(CD_FILE,FILE_NAME,'FRICTION_FILE',ierr)`; `:2779` `Cd_fixed = 0.0_SP`; `src/init.F:884` `ELSE`; `:887` `Cd(I,J) = Cd_fixed` | 일치 | FRICTION_MATRIX가 참이면 FRICTION_FILE의 공간 마찰장을 읽는다(`src/init.F:854–858`). 거짓이면 고정 Cd를 배포한다(`:884–887`). `src/sources.F:237–242`의 MANNING 분기는 같은 배열을 Manning 계수로 쓴다. 이 기능과 조건은 일반 입력·빌드 절에 설명되어 있으므로 문서 전체의 누락으로 분류하지 않는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-308 | FOURTH·THIRD 예제는 현재 활성 구성법의 내부 선택을 적지 않는다. | `src/fluxes.F:58–62` `! for the fourth-order, Choi used 4th + combined minmod and van leer` / `! it is more stable than 4th + minmod` / 빈 줄 / `CALL CONSTRUCTION_HO   ! note choi used the name construction_ho_vanleer` / `! I changed back for consistency`; `:101–103` `ELSE` / `CALL DelxyFun` / `CALL CONSTRUCTION` | 코드에만 — C | 결합 limiter는 3.0 p.23·81 및 `funwave_tvd_3.0.tex` 629–630·2389–2390행에 설명된다. code_analysis p.15도 두 limiter의 호출 구조를 싣는다. C는 예제에 없는 접두어 선택과 기본 분기에 한정한다. `src/fluxes.F:56·71·81·89·101`은 FOU·FMI·WEN·MLP와 ELSE를 구분한다. FOURTH는 결합 minmod·van Leer 구성으로 들어간다. 이 구성 자체는 3.0에 설명되어 있다. 예제에 빠진 조건은 FOU·FMI·WEN·MLP 접두어에 해당하지 않는 문자열이 ELSE의 기본 구성으로 간다는 점이다(FV2-270). [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-309 | 예제는 Time_Scheme=Runge_Kutta를 지정한다. | `src/main.F:379` `! 3-ORDER RUNGE-KUTTA TIME STEPPING`; `:380` `DO ISTAGE=1,3` | 코드에만 — C | 2.1 p.39·3.0 p.40·Intro-TN p.13 및 `funwave_tvd_3.0.tex` 1331행은 시간 적분 옵션을 설명한다. C는 Time_Scheme 읽기와 현재 실행 분기가 연결되지 않는다는 조건에 한정한다. src 전체의 Time_Scheme 검색은 선언·입력·로그·주석을 찾고 실행 선택 조건을 찾지 않는다. 현재 main은 Time_Scheme 문자열로 분기하지 않고 `DO ISTAGE=1,3`을 실행한다. 예제의 Runge_Kutta는 이 경로와 맞는다. 다른 문자열을 입력해 Predictor_Corrector를 선택하는 기능은 이 읽기에서 생기지 않는다. [10-18 결론 검증 보완] |

FV2-307의 `src/sources.F:236–243`은 다음과 같다.
전처리 조건을 포함하여 이어진 대입문 전체를 인용한다.

```fortran
       FrcInsX(I,J) = &
# if defined (MANNING)
                   -(GRAV*Cd(I,J)**2/  &
                   Max(H(I,J),MinDepthFrc)**(0.333333_SP))  &
                   *U(I,J)*SQRT(U(I,J)*U(I,J)+V(I,J)*V(I,J))
# else
                   -Cd(I,J)*U(I,J)*SQRT(U(I,J)*U(I,J)+V(I,J)*V(I,J))
# endif
```

| 행 ID | 문서와의 관계 | 코드 원문 | 판정 | 영향 |
|---|---|---|---|---|
| FV2-310 | p.44는 `Some necessary definitions`라고 입력 발췌를 소개한다. Grid_A·Grid_B 목록에는 Mglob·Nglob가 없다. | `src/io.F:248` `CALL READ_INTEGER(Mglob,FILE_NAME,'Mglob',ierr)` 뒤 `:260` `STOP`; `:263` `CALL READ_INTEGER(Nglob,FILE_NAME,'Nglob',ierr)` 뒤 `:275` `STOP`; `:603` `CALL READ_FLOAT(TOTAL_TIME,FILE_NAME,'TOTAL_TIME',ierr)` 뒤 `:616` `STOP`; 병렬 `:223` `CALL READ_INTEGER(PX,FILE_NAME,'PX',ierr)` 뒤 `:225` `PX = 1`; `:229` `CALL READ_INTEGER(PY,FILE_NAME,'PY',ierr)` 뒤 `:231` `PY = 1` | 코드에만 — C | Mglob·Nglob·TOTAL_TIME의 설명은 2.1 p.35–36·3.0 p.35–36 및 `funwave_tvd_3.0.tex` 1117–1129행에 있다. C는 2.1 p.70–72의 중첩 입력 발췌에서 격자 수를 생략한 범위에 한정한다. 중첩 예제의 입력 발췌에는 Mglob·Nglob가 빠져 있다. 두 값은 코드에서 없으면 중단하므로 별도로 지정한다. 일반 입력 절은 이미 이 키를 설명한다. 병렬 PX·PY의 누락 기본값은 각각 1이다. [10-18 결론 검증 보완] |
| FV2-311 | 중첩 예제는 구면 모드에서 i,j 관측점을 설명한다. | `src/io.F:84–89` `# if defined (SPHERICAL_IJ_STATION)` / `! use IJ for coupling purpose` / `CALL STATIONS_SPHERICAL_IJ` / `# else` / `CALL STATIONS` / `# endif`; 기본 구면 직렬 경로 `:4197` `ista(i) = Nghost+1+nint((dum2-Lon_West)/Dphi)`; `:4198` `jsta(i) = Nghost+1+nint((dum1-Lat_South)/Dtheta)` | 코드에만 — C | 기본 구면 관측점의 Lat/Lon 입력은 2.1 p.9·3.0 p.10 및 `funwave_tvd_3.0.tex` 177행에 있다. C는 2.1 p.69–72·3.0 p.76–79 중첩 예제에 없는 SPHERICAL_IJ_STATION 조건에 한정한다. 기본 구면 관측점 파일은 위도·경도 순이다. i,j 파일은 SPHERICAL_IJ_STATION 분기에서 읽는다. COUPLING만으로 이 분기가 선택되지는 않는다(FV2-144). [10-18 결론 검증 보완] |
| FV2-312 | p.70의 빌드 위치 설명은 `Makefile in /src/`다. | `b9c035d:src/Makefile:17` `#             FLAG_8 = -DCOUPLING`; 현재 `TVD/Makefile:11` `#  FLAG_1  = -DCOUPLING`; `:35` `include $(FUNWAVE_DIR)/GNUMake/Essential/Make_Essential` | 코드에만 — A | 현재 기본 빌드는 TVD 루트의 Makefile과 GNUMake를 쓴다. 2019-07-19 ca113a8이 새 구성을 추가했다. 2019-07-24 7776fa5가 src/Makefile을 삭제했다. COUPLING의 대문자 이름은 유지한다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-313 | p.43은 결합 파일 지정 절차만 이어서 제시한다. | `src/nesting.F:58` `INQUIRE(FILE=TRIM(COUPLING_FILE),EXIST=FILE_EXIST)`; `:67` `STOP`; `:93` `READ(11,*) TIME_COUPLING_1`; `:95` `TIME_COUPLING_2 = TIME_COUPLING_1`; `:371–372` `READ(11,*,IOSTAT=IOstatus) TIME_COUPLING_2` / `IF (IOstatus < 0) GOTO 120`; `:489–492` `IF(TIME_COUPLING_1.EQ.TIME_COUPLING_2)THEN` / `! no more data` / `tmp2=ZERO` / `tmp1=ZERO` | 코드에만 — C | 2.1 p.42·3.0 p.44는 중첩 자료와 첫 시각 초기화를 설명한다. C는 파일 끝과 같은 두 시각의 가중치 처리에 한정한다. `src/nesting.F:367–372·483–496`는 자료 갱신·EOF 이동과 `IF(TIME>TIME_COUPLING_1)THEN` 안의 가중치 조건을 보인다. COUPLING 파일이 없으면 중단한다. 두 시각이 다르면 그 사이의 값을 선형 보간한다. 자료 끝에서 두 시각이 같고 TIME이 그 시각보다 크면 tmp1·tmp2를 0으로 둔다. 첫 자료 시각으로 시작하는 동작은 매뉴얼에 이미 설명되어 있다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-314 | p.43은 RESULT_FOLDER를 결과 디렉터리로 설명한다. | `src/io.F:3341` `MKFOLDER = "mkdir -p "//TRIM(RESULT_FOLDER)`; `:4327` `FDIR=TRIM(RESULT_FOLDER)`; `:4372` `TMP_NAME = TRIM(FDIR)//'eta_'//TRIM(FILE_NAME)` | 코드에만 — C | 3.0 p.44도 RESULT_FOLDER를 설명한다. `funwave_tvd_3.0.tex` 1113행 예시는 끝 `/`를 포함하지만 Intro-TN p.17 예시는 포함하지 않는다. C는 이 구분자 결합 조건의 설명에 한정한다. 파일 경로는 RESULT_FOLDER 뒤에 eta_ 등의 이름을 직접 붙여 만든다. 디렉터리 안에 저장하려면 `./output/`처럼 끝 `/`를 포함한다. 디렉터리 생성 명령은 그 구분자를 대신 붙이지 않는다. [10-18 결론 검증 보완] |
| FV2-315 | p.43은 ASCII와 수심 자료 형식만 설명한다. | 병렬 `src/io.F:3330` `CALL READ_STRING(FIELD_IO_TYPE,FILE_NAME,'FIELD_IO_TYPE',ierr)` 뒤 `:3332` `IF(ierr.EQ.1) FIELD_IO_TYPE = 'ASCII'`; `:3365` `CALL READ_INTEGER(OUTPUT_RES,FILE_NAME,'OUTPUT_RES',ierr)` 뒤 `:3367` `OUTPUT_RES = 1`; `:4876–4877` `CASE ('BINARY' , 'binary' )` / `Call PutFileBinary(FILE_NAME,PHI)` | 코드에만 — C | 2.1 p.43·3.0 p.44의 출력 절에는 FIELD_IO_TYPE·OUTPUT_RES 선택이 없다. `src/io.F:4894–4920`의 직렬 PutFile은 ASCII를 쓰며 내부 격자를 OUTPUT_RES 간격으로 순회한다. 병렬 필드 출력은 FIELD_IO_TYPE으로 ASCII 또는 BINARY를 고른다. 누락 기본값은 ASCII다. 직렬 PutFile은 ASCII를 쓴다. OUTPUT_RES의 기본값 1은 내부 격자를 한 점 간격으로 출력하며, 이 값을 키우면 출력 점을 건너뛴다. [10-18 결론 검증 보완] |
| FV2-316 | INI_SOL 예제는 진행 방향 선택을 싣지 않는다. | `src/io.F:1103–1104` `CALL READ_LOGICAL(SolitaryPositiveDirection,FILE_NAME,  &` / `'SolitaryPositiveDirection',ierr)`; `:1107` `SolitaryPositiveDirection = .TRUE.`; `src/samples.F:561–565` `IF(SolitaryPositiveDirection)THEN` / `U(I,J)=A*SC*SC` / `ELSE` / `U(I,J)=-A*SC*SC` / `ENDIF` | 코드에만 — C | 2.1 p.60·68·70–72와 3.0의 대응 INI_SOL 예제에는 이 방향 입력이 없다. 입력 분기는 `src/io.F:1101` `IF(WaveMaker(1:7)=='INI_SOL')THEN`이다. `src/init.F:907–909`가 초기 고립파 루틴을 호출한다. INI_SOL의 SolitaryPositiveDirection 누락 기본값은 참이다. `src/samples.F:561–565`에서 참이면 초기 u에 `U(I,J)=A*SC*SC`를, 거짓이면 `U(I,J)=-A*SC*SC`를 대입한다. 이 옵션은 LAGTIME과 별개다. [10-18 결론 검증 보완] |
| FV2-317 | p.70은 관측점 출력을 매 시간 단계에 만들라고 적는다. | `src/io.F:664` `CALL READ_INTEGER(StationOutputBuffer,FILE_NAME,'StationOutputBuffer',ierr)` 뒤 `:666` `StationOutputBuffer = 1000`; `:3905` `IF(BufferCount(i)<StationOutputBuffer.AND.TIME<TOTAL_TIME)THEN`; `:3907–3910` `ZUV_BUFFER(BufferCount(i),i,1)=time` / `ZUV_BUFFER(BufferCount(i),i,2)=eta_sta` / `ZUV_BUFFER(BufferCount(i),i,3)=u_sta` / `ZUV_BUFFER(BufferCount(i),i,4)=v_sta` | 코드에만 — C | 2.1 p.70·3.0 p.77의 매 시간 단계 출력 설명에는 버퍼 조건이 없다. `src/io.F:82–90`는 출력 간격·NumberStations 조건으로 호출한다. `:3916–3929`의 ELSE는 기존 버퍼를 쓴 뒤 개수를 0으로 재설정한다. 구면 i,j 경로의 같은 처리는 `:4073–4097`이다. NumberStations가 양수이고 출력 간격 조건을 만족할 때 관측점 루틴을 호출한다. StationOutputBuffer의 누락 기본값은 1000이다. 버퍼를 채우는 분기와 기존 버퍼를 파일에 쓰는 분기는 따로 있다. PLOT_INTV_STATION=0.0의 호출 선택을 매 단계 즉시 파일 쓰기와 동일시하지 않는다. [10-18 결론 검증 보완] |
| FV2-318 | 예제는 건조 관측점의 값을 설명하지 않는다. | `src/io.F:3885–3888` `IF(mask(ista(i),jsta(i))<1)THEN` / `eta_sta=ZERO` / `u_sta=ZERO` / `v_sta=ZERO` | 코드에만 — C | C는 2.1 p.62·70 및 3.0 p.70·77의 관측점 출력 설명에 없는 건조점 처리에 한정한다. `src/io.F:3843–3875`는 내부 격자에 속한 관측점을 고른다. 구면 i,j의 `:4053–4056`과 기본 구면의 `:4220–4223`에도 같은 0 처리가 있다. 내부 격자에 속한 출력 관측점에서 `IF(mask(ista(i),jsta(i))<1)THEN`이면 eta_sta·u_sta·v_sta를 ZERO로 대입한다. 이 처리는 직교·구면 i,j·기본 구면 관측점 경로에 공통이다. [10-18 결론 검증 보완] |
| FV2-319 | 예제는 출력 시작과 고정 시간간격 선택을 싣지 않는다. | `src/io.F:619` `CALL READ_FLOAT(PLOT_START_TIME,FILE_NAME,'PLOT_START_TIME',ierr)` 뒤 `:622` `PLOT_START_TIME = 0.0`; `:2883` `CALL READ_FLOAT(DT_fixed,FILE_NAME,'DT_fixed',ierr)`; `:2884–2885` `IF (ierr.ne.1) THEN` / `FIXED_DT = .TRUE.`; `:2898` `CALL READ_FLOAT(FroudeCap,FILE_NAME,'FroudeCap',ierr)` 뒤 `:2900` `FroudeCap = 3.0_SP` | 코드에만 — C | C는 예제의 PLOT_START_TIME·DT_fixed 생략에 한정한다. `src/io.F:94` `IF(TIME>=PLOT_START_TIME)THEN`은 필드 출력을 제한한다. `src/misc.F:281–290`는 CFL의 DT_tmp를 계산하고 FIXED_DT일 때 `DT = DT_fixed` 뒤 `DO WHILE (DT > DT_tmp)` 안에서 `DT=DT/2.0_SP`를 수행한다. PLOT_START_TIME의 누락 기본값은 0초이며 필드 출력의 시작 조건이다. DT_fixed를 제공하면 FIXED_DT를 켜지만 CFL 상한보다 큰 동안 시간간격을 반씩 줄인다. FroudeCap=10은 중첩 예제 지정값이고 현재 누락 기본값은 3이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-320 | 예제는 조파원 내부의 평균 흐름 보정 입력을 싣지 않는다. | `src/io.F:2479` `CALL READ_FLOAT(WaveMakerCd,FILE_NAME,'WaveMakerCd',ierr)`; `:2481` `WaveMakerCurrentBalance=.FALSE.`; `:2488` `WaveMakerCurrentBalance=.TRUE.` | 코드에만 — C | C는 2.1 예제 입력에 없는 WaveMakerCd 조건에 한정한다. `src/sources.F:274–285`의 `IF(WaveMakerCurrentBalance)THEN` 안에서 x·y 조파원 범위를 검사한 뒤 `-WaveMakerCd*U(I,J)*SQRT(U(I,J)*U(I,J)+V(I,J)*V(I,J))`를 쓴다. WaveMakerCd를 읽으면 WaveMakerCurrentBalance를 참으로 둔다. 실제 추가 마찰은 sources.F의 조파원 범위 조건을 통과한 점에 적용한다. 입력이 없으면 이 선택을 끈다. 계수 0은 선택이 켜져도 해당 마찰항을 0으로 만든다. [10-18 결론 검증 보완] |

FV2-313의 `src/nesting.F:494–496`은 시간 보간 가중치를 다음과 같이 계산한다.

```fortran
      tmp2=(TIME_COUPLING_2-TIME) &
            /MAX(SMALL, ABS(TIME_COUPLING_2-TIME_COUPLING_1))
      tmp1=1.0_SP - tmp2;
```

같은 파일의 `:509–516`은 서쪽 가상 셀에 다음 값을 넣는다.

```fortran
        ETA(I,J)=Z_COUPLING_WEST(J-Nghost+Kshift_WEST,2)*tmp1&
                +Z_COUPLING_WEST(J-Nghost+Kshift_WEST,1)*tmp2
        U(I,J)=U_COUPLING_WEST(J-Nghost+Kshift_WEST,2)*tmp1&
                +U_COUPLING_WEST(J-Nghost+Kshift_WEST,1)*tmp2
        V(I,J)=V_COUPLING_WEST(J-Nghost+Kshift_WEST,2)*tmp1&
                +V_COUPLING_WEST(J-Nghost+Kshift_WEST,1)*tmp2
        HU(I,J)=(Depth(I,J)+ETA(I,J))*U(I,J)
        HV(I,J)=(Depth(I,J)+ETA(I,J))*V(I,J)
```

FV2-321은 3.0 해빈에서 빠진 Time_ramp 줄의 누락 기본값을 보완한다.

| 행 ID | 문서의 대응 범위 | 코드 원문 | 판정 | 이유 |
|---|---|---|---|---|
| FV2-321 | 2.1 p.44는 `Time_ramp = 1.0`을 명시한다. 같은 3.0 p.45–46 해빈 발췌는 이 줄을 싣지 않는다. | `src/io.F:1517` `CALL READ_FLOAT(Time_ramp,FILE_NAME,'Time_ramp',ierr)` 뒤 `:1519` `Time_ramp = 0.0_SP`; `src/sources.F:110` `AA = TANH(PI/(Time_ramp*Tperiod)*TIME)*D_gen` | 코드에만 — C | 3.0 p.37 및 `funwave_tvd_3.0.tex` 1185행은 WK_REG에 Time_ramp가 필요하다고 적는다. C는 3.0 p.45–46 해빈 입력 발췌의 생략에 한정한다. `src/sources.F:109` `IF(WAVEMAKER(1:6)=='WK_REG')THEN` 아래 식으로 도달한다. 2.1 p.44는 Time_ramp=1.0을 지정하지만 3.0 해빈 발췌는 생략한다. 현재 WK_REG 읽기는 누락 시 0.0_SP를 대입한다. 이어 `AA = TANH(PI/(Time_ramp*Tperiod)*TIME)*D_gen`의 분모가 0이 된다. 3.0 일반 입력 절의 필수 항목을 예제에도 명시한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |

## 4 노트 대조와 수정안

이 절은 현재 노트를 수정하지 않고 수정안만 제시한다.
노트 원문의 축약 기호는 인용 안에서 보존한다.
수정안은 문서의 설정값과 현재 코드 기본값을 분리한다.

| 행 ID | 노트 파일:줄과 원문 | 대조 판정·근거 | 노트 수정안 |
|---|---|---|---|
| FV2-400 | `models/FUNWAVE/manual-notes/funwave-user-manual-full.md:238`의 `핵심 input.txt verbatim 발췌:`; `:241` `DEPTH TYPE = SLOPE ; DEPTH FLAT = 0.36 ; SLP = 0.0292 ; Xslp = 30.0`; `:243` `WAVEMAKER = WK REG ; Xc WK = 45.0 ; Tperiod = 3.33`; `:250` `MinDepth=0.001 ; MinDepthFrc=0.001`; 같은 노트 `:205`의 `Cd fixed`; `:224`의 `STATION FILE`·`HMAX` | 불일치 — B. PDF는 밑줄을 포함한 키를 각각 다른 줄에 인쇄한다. 현재 `src/mod_input.F:297`은 키를 정확히 비교한다. `:298`은 첫 등호 뒤의 전체를 값으로 둔다. | `verbatim` 표현을 삭제한다. 아래의 정규화된 입력 발췌로 교체한다. 이 발췌를 완전한 실행 입력이라고 부르지 않는다. 관련 입력 목록의 Cd fixed·STATION FILE·HMAX도 실제 키 Cd·STATIONS_FILE·Hmax로 고친다. 근거는 FV2-064·072·076이다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-401 | `models/FUNWAVE/manual-notes/funwave-user-manual-full.md:232` `station은`·`sta_00001`·`그외 포맷 개발중 (p.44).` 부분 | B 문서 오기. 문서의 3.0 p.44 관측점 이름은 다섯 자리다. 현재 `src/io.F:3869` `write(file_name(1:4),'(I4.4)') i`는 네 자리다. 3.0 p.44와 같은 이름 오기를 옮긴 노트다. 문서 시점에도 `24a88c3:src/io.F:1022`는 `write(file_name(1:4),'(I4.4)') i`를 쓴다. 같은 사실의 판정은 FV2-269와 B로 통일한다. | 노트의 sta_00001은 sta_0001로 고친다. 관측점 순번은 네 자리이고 장 출력 순번은 다섯 자리다. RESULT_FOLDER의 끝 `/` 조건은 FV2-314에 따른다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-402 | `models/FUNWAVE/manual-notes/funwave-user-manual-full.md:218`의 `Kennedy(2000) C1·C2 (default 0.65 / 0.15)`; `:253`의 `Cbrk1=0.65·Cbrk2=0.15는 Kennedy et al. 및 본 모델 기본값` | 불일치 — B. `src/io.F:3081` `Cbrk1 = 0.65_SP`; `:3103` `Cbrk2 = 0.35_SP`가 현재 기본값이다. FV2-266은 문서 시점 코드도 대조했다. | “3.0 해빈 예제는 Cbrk1=0.65와 Cbrk2=0.15를 명시한다. 현재 코드의 누락 기본값은 0.65와 0.35다. 이 판정은 본 모델의 누락 기본값에 한정한다.”라고 쓴다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-403 | `models/FUNWAVE/source-analysis/funwave-physics-sources.md:17`의 `tmp1=Cbrk1√(gh)` 뒤의 `(개시~0.45)`와 `tmp2=Cbrk2√(gh)` 뒤의 `(지속~0.35)` 부분 | 불일치 — B. 현재 Cbrk1 누락 기본값은 `src/io.F:3081`의 `Cbrk1 = 0.65_SP`다. | “개시·지속 계수는 입력 Cbrk1·Cbrk2다. 현재 누락 기본값은 각각 0.65·0.35다.”라고 쓴다. 0.45를 코드 기본값으로 표시하지 않는다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-404 | `models/FUNWAVE/source-analysis/funwave-physics-sources.md:29`의 `시계열(T,A,phase)` | C 문서 누락. `src/wavemaker.F:354` `READ(1,*)(WAVE_COMP(J,I),I=1,3)`가 성분 자료를 읽는다. `src/sources.F:138`은 셋째 열을 위상으로 쓴다. 누락 범위는 이 분석 노트의 '시계열' 표현이다. 2.1 p.37·49와 3.0 p.37–38은 이미 FFT로 구한 성분 자료라고 설명한다. `src/wavemaker.F:351–354·2435–2437`과 `src/sources.F:135–143`은 WK_TIME 분기·주기 변환·성분 합성을 보인다. | WK_TIME_SERIES는 성분별 주기(s)·진폭(m)·위상(rad)의 세 열을 읽는다. 원시 수면 시계열의 FFT는 문서의 MATLAB 전처리 단계다. 모델 안의 성분 합성과 전처리를 구분한다. [10-18 결론 검증 보완] |
| FV2-405 | `models/FUNWAVE/source-analysis/funwave-infrastructure.md:39`의 `INITIAL_SOLITARY_WAVE(:511, INI_SOL Nwogu)+SUB_SLTRY(:582 Newton 계수)` 부분 | C 문서 누락. FV2-047은 LAGTIME의 적용 범위를 확인했다. FV2-136은 초기 중심의 가상 셀 좌표 차이를 확인했다. 누락 범위는 이 분석 노트의 초기 고립파 적용 조건이다. `src/io.F:890·924·1101–1162`와 `src/init.F:907–909`가 LAGTIME 읽기 분기와 INI_SOL 초기 호출을 구분한다. 중심 식의 반대 근거는 `src/samples.F:542` `! start from ghost cell`이다. | INI_SOL은 초기 고립파를 배치한다. LAGTIME은 LEF_SOL에서만 읽는다(FV2-047). 직교 INI_SOL의 중심은 Xco 원점 기준 XWAVEMAKER보다 3DX 왼쪽이다. 의도 주석을 반영한 코드 결함 후보의 강도는 중간이다(FV2-136). [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-406 | `models/FUNWAVE/source-analysis/funwave-infrastructure.md:43`의 `parent grid 경계 시계열 선형보간→ghost (one-way nesting)` | C 문서 누락. `src/main.F:238` `TIME=TIME_COUPLING_1`; `src/io.F:84` `# if defined (SPHERICAL_IJ_STATION)`; `src/io.F:3885–3888`의 건조 관측점 0 처리 누락 범위는 이 분석 노트의 초기 시각·관측점 분기·건조점 조건이다. 첫 결합 시각 초기화는 2.1 p.42·3.0 p.44에 이미 있다. 구면 i,j 경로의 `src/io.F:4053–4056·4085–4097`이 건조값과 FOAM별 출력 열을 보인다. | COUPLING 자식은 결합 자료의 첫 시각에서 시작한다. 구면 부모가 i,j 파일을 쓰려면 SPHERICAL_IJ_STATION을 정의한다. FOAM 미정의 시 관측점 파일은 time·η·u·v의 네 열이다. FOAM 정의 시 세 열을 더 쓴다. 건조 관측점의 η·u·v는 0이다(FV2-311·317·318). [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-407 | `models/FUNWAVE/manual-notes/funwave-validation-cases.md:85`의 `funwave_tvd_2.1_manual.pdf line 2813–2817`; `입사파고 3 케이스(A/B/C), Cartesian·spherical 좌표 양쪽 실행.` | 코드 대조 대상 아님 — H. 노트는 원뿔섬 사례 A·B·C와 Cartesian·spherical 결과를 목록으로 정리한다. 원문 인용 범위는 2.1 p.57–62다. 2.1 p.60과 3.0 p.69의 입력 진폭은 0.0144·0.02912·0.05792 m다. | 원뿔섬 노트의 PDF 줄 번호 인용을 2.1 p.57–62로 바꾼다. 두 좌표계 항목은 노트에 수록한 사례 목록으로 적는다. 세 입력 진폭은 원문의 사례 A·B·C와 대응한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-408 | `models/FUNWAVE/manual-notes/funwave-validation-cases.md:98`의 `one-way nesting 검증`과 `메뉴얼 §5.6 nesting case 대응`; `models/FUNWAVE/manual-notes/funwave-user-manual-full.md:255`의 `나머지 예제(p.47~78)`와 `5.8 nesting (TOC p.45).` | 불일치 — B. 노트가 가리킨 중첩 예제는 2.1 p.69–73 §5.6과 3.0 p.76–80 §5.8이다. 3.0의 마지막 결과 그림은 p.80의 그림 25다. | 노트는 두 판의 중첩 예제와 결과 그림을 식별한 기록이다. 3.0 예제 목록의 끝 쪽은 p.78이 아니라 p.80이다. 본문 1 m와 입력 0.1 m의 차이는 FV2-143에 따른다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-409 | `models/FUNWAVE/source-analysis/funwave-physics-sources.md:48`의 `Cd 기본값 = 0.0(마찰 완전 off, 2026-07-12 확인)` 부분과 `Cd 카드 미지정 시 io.F:2777-2783 이 Cd_fixed=0.0 대입` 부분 | C 문서 누락. `src/io.F:2779` `Cd_fixed = 0.0_SP`와 `src/init.F:884–887`의 고정 마찰 분기가 대응한다. 누락 범위는 이 분석 노트의 '마찰 완전 off'에 빠진 적용 조건이다. 일반 공간 마찰 설명은 2.1 p.39·3.0 p.40·Intro-TN p.12에 있다. `src/sources.F:237–242·262–265·274–285`는 바닥 마찰·마찰 완충층·조파원 마찰을 구분한다. | FRICTION_MATRIX가 거짓인 고정 마찰 경로에서는 Cd 누락 기본값 0이 바닥 마찰항을 0으로 만든다. 공간 마찰장은 파일 배열을 쓴다. FRICTION_SPONGE와 WaveMakerCd에 의한 추가 마찰은 별도 조건이다(FV2-307·320). [10-18 결론 검증 보완] |
| FV2-410 | `models/FUNWAVE/README.md:18`의 `TVD shock-capturing(쇄파를 bore로 처리, hybrid FV/FD)` 부분 | C 문서 누락. 이 설명만으로 현재 입력 생략 시의 쇄파 방식을 알 수 없다. `src/io.F:2691` `VISCOSITY_BREAKING = .TRUE.`가 현재 기본값이다. 누락 범위는 README의 기본 쇄파 선택 설명이다. 2.1 p.39·3.0 p.40의 기본 충격 포착 설명과 현재 코드 기본값의 이력 차이는 FV2-301의 A 판정이다. `src/io.F:2689`는 VISCOSITY_BREAKING을 읽고 `src/masks.F:177–185`는 이 값에 따라 MASK9 경로를 나눈다. | TVD 플럭스와 쇄파 방식 선택을 구분한다. 현재 TVD는 VISCOSITY_BREAKING을 생략하면 참으로 둔다. 예제의 NSWE 전환 경로를 선택하려면 거짓을 지정하고 실제 MASK9 분기 조건을 적용한다(FV2-301·107). [10-18 결론 검증 보완] |
| FV2-411 | `models/FUNWAVE/manual-notes/funwave-user-manual-full.md:88`의 `Shock-capturing (default)`; `:201`의 `default는 shock-capturing` | 불일치 — A. `b9c035d:src/mod_global.F:382`의 `LOGICAL :: VISCOSITY_BREAKING = .FALSE.`는 당시 설명과 맞는다. 2019-06-16 6233886이 누락 기본값을 참으로 바꿨다. 현재 `src/io.F:2691`은 `VISCOSITY_BREAKING = .TRUE.`다. | “문서는 shock-capturing을 기본값으로 설명한다. 현재 TVD의 누락 기본값은 점성 쇄파다. shock-capturing 전환을 쓰려면 VISCOSITY_BREAKING=F를 명시한다.”라고 문서 요약과 현재 코드 조건을 구분한다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |

FV2-400의 입력 수정안은 다음과 같다.
이 블록은 3.0 문서의 예제 설정을 현재 TVD의 키와 줄 형식으로 정리한 AI 수정안이다.
3.0 문서의 직접 인용 블록이 아니다.
마찰 키 이름은 현재 TVD에 맞게 바꿨다.
Cbrk2=0.15는 예제 지정값으로 유지했다.
Time_ramp=1.0은 2.1 p.44의 명시값을 보완한 줄이다.
3.0의 같은 발췌에는 이 줄이 없다.
시간·병렬 분할·완전한 실행 자료는 이 발췌에 포함하지 않는다.

```text
DEPTH_TYPE = SLOPE
DEPTH_FLAT = 0.36
SLP = 0.0292
Xslp = 30.0
Mglob = 2000
Nglob = 3
DX = 0.025
DY = 0.2
WAVEMAKER = WK_REG
Xc_WK = 45.0
Tperiod = 3.33
AMP_WK = 0.018
DEP_WK = 0.36
Theta_WK = 0.0
Time_ramp = 1.0
Delta_WK = 0.5
DIRECT_SPONGE = T
Sponge_west_width = 12.0
Sponge_east_width = 0.0
Sponge_south_width = 0.0
Sponge_north_width = 0.0
R_sponge = 0.85
A_sponge = 5.0
DISPERSION = T
Gamma1 = 1.0
Gamma2 = 1.0
Gamma3 = 1.0
Beta_ref = -0.531
SWE_ETA_DEP = 0.8
VISCOSITY_BREAKING = F
Cbrk1 = 0.65
Cbrk2 = 0.15
WAVEMAKER_Cbrk = 0.65
FRICTION_MATRIX = F
Cd = 0.0
Time_Scheme = Runge_Kutta
HIGH_ORDER = THIRD
CONSTRUCTION = HLLC
CFL = 0.5
MinDepth = 0.001
MinDepthFrc = 0.001
NumberStations = 119
STATIONS_FILE = gauge.txt
DEPTH_OUT = T
ETA = T
MASK = T
```

## 5 차이 결론

### 5.1 판 차이를 가르는 기준

2.1 표지는 `Revision: September 2013`이라고 적는다.
제공된 전체 git 이력은 2016-03-02 cab9425에서 시작한다.
이 보고서는 2013년의 코드 작업 트리를 복원했다고 주장하지 않는다.
2.1 PDF가 저장소에 들어간 커밋은 2016-11-03 b9c035d다.
B의 역사 대조 기준은 이 PDF와 함께 저장된 코드다.
3.0 LaTeX의 마지막 변경은 2016-11-18 24a88c3다.
3.0 PDF의 마지막 변경은 2018-02-24 fef45a7다.
3.0의 B는 원고 시점 코드와 PDF 저장 시점 코드에서 해당 차이를 확인한다.
현재 TVD는 HEAD b4c322e의 src와 같다.
`src/main.F:47`의 판 주석은 `!    VERSION 3.0`이다.
`TVD/README.md:2`는 `This version is a beta version. Please report any bugs if you find in your case.`라고 적는다.
이 두 문구만으로 현재 작업 트리를 2016년 원고와 같은 코드라고 간주하지 않는다.

| A 행 | 문서 시점 코드 원문 | 바뀐 커밋과 날짜 | 현재 차이 |
|---|---|---|---|
| FV2-267 | `24a88c3:src/io.F:750` `CALL READ_LOGICAL(IN_Cd,FILE_NAME,'Friction_Matrix',ierr)`; `24a88c3:src/io.F:751` `CALL READ_STRING(CD_FILE,FILE_NAME,'Cd_file',ierr)` | 9bae2f6, 2019-07-25. 새 원문은 `9bae2f6:src/io.F:2660` `CALL READ_LOGICAL(IN_Cd,FILE_NAME,'FRICTION_MATRIX',ierr)`와 `9bae2f6:src/io.F:2675` `CALL READ_STRING(CD_FILE,FILE_NAME,'FRICTION_FILE',ierr)`다. | 현재 TVD는 대문자 FRICTION_MATRIX·FRICTION_FILE을 읽는다. `GPU/src/io.F:2649`와 `:2664`는 문서의 이전 키를 유지한다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-301 | `b9c035d:src/mod_global.F:382` `LOGICAL :: VISCOSITY_BREAKING = .FALSE.`; 명시 누락 기본값을 추가한 `285a6f6:src/io.F:2357`도 `VISCOSITY_BREAKING = .FALSE.`다. | 6233886, 2019-06-16. `6233886:src/io.F:2597`은 `VISCOSITY_BREAKING = .TRUE.`로 바뀐다. | 현재 `src/io.F:2691`은 참이다. `GPU/src/io.F:2604`는 거짓이다. `src/masks.F:177–180`의 참 분기는 MASK9를 1로 두므로 비율 전환을 검사하지 않는다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-306 | `b9c035d:src/io.F:822` `CALL READ_FLOAT(MinDepth,FILE_NAME,'MinDepth',ierr)`; `b9c035d:src/io.F:828` `CALL READ_FLOAT(MinDepthFrc,FILE_NAME,'MinDepthFrc',ierr)` 뒤에는 병합이 없다. | 285a6f6, 2017-05-01은 `285a6f6:src/io.F:2612`의 `MinDepthFrc=MIN(MinDepthFrc,MinDepth)`를 추가한다. d69acc3, 2018-05-25는 MIN을 MAX로 바꾼다. 93c0053, 2023-11-13은 `93c0053:src/io.F:2947`의 `MinDepthFrc=MIN(MinDepthFrc,MinDepth)`로 다시 바꾼다. | 현재 `src/io.F:2948–2949`는 MIN으로 병합한다. `GPU/src/io.F:2859–2860`은 MAX로 병합한다. 예제의 두 값이 같은 경우에는 이 변경이 값을 바꾸지 않는다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-312 | `b9c035d:src/Makefile:17` `#             FLAG_8 = -DCOUPLING` | ca113a8, 2019-07-19는 루트 Makefile과 GNUMake 구성을 추가한다. 7776fa5, 2019-07-24는 src/Makefile을 삭제한다. | 현재 `TVD/Makefile:11` `#  FLAG_1  = -DCOUPLING`과 `:35` `include $(FUNWAVE_DIR)/GNUMake/Essential/Make_Essential`을 쓴다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |

### 5.2 D의 전체 검색

FV2-049·FV2-110·FV2-121의 D는 SPONGE_ON이라는 입력 스위치의 구현 여부다.
동명 선언이 없다는 주장은 아니다.
검색어는 대소문자를 무시한 `SPONGE_ON`이다.
원자료 검색 명령은 다음과 같다.

```sh
rg -i -n 'SPONGE_ON' models/FUNWAVE/raw/source_code -g '!**/simple_cases/**' -g '!**/benchmarks/**'
```

검색은 네 줄을 찾았다.
`TVD/src/mod_global.F:389`의 원문은 `LOGICAL :: SPONGE_ON=.FALSE.`다.
`GPU/src/mod_global.F:361`의 원문도 `LOGICAL :: SPONGE_ON=.FALSE.`다.
`GPU/src/global.mod:2539`의 전체 원문은 `S 2186 6 4 0 0 18 2187 624 17683 80000c 0 A 0 0 0 0 B 0 319 0 0 0 268 0 0 0 0 0 0 2340 0 0 0 0 0 0 0 0 0 0 624 0 0 0 0 sponge_on`이다.
`GPU/src/tags:687`의 전체 원문은 `SPONGE_ON	mod_global.F	/^       LOGICAL :: SPONGE_ON=/;"	v	module:GLOBAL`이다.
READ_LOGICAL 호출과 실행 조건은 없었다.

git 검색 명령은 다음과 같다.

```sh
git -C _staging/recovery/extract/FUNWAVE/external/tvd log --all --format='%h %ad %s' --date=short -S 'SPONGE_ON' -- . ':(exclude)simple_cases/**' ':(exclude)benchmarks/**'
git -C _staging/recovery/extract/FUNWAVE/external/tvd log --all --format='%h %ad %s' --date=short -p -S 'SPONGE_ON' -- '*.F' '*Makefile*'
```

첫 검색은 cab9425(2016-03-02), b9c035d(2016-11-03), 8d5a857(2016-11-03), c249880(2017-05-01), 347793e(2021-08-02), 5311c8e(2022-07-09)를 찾았다.
c249880은 `examples/` 아래 SPONGE_ON을 적은 입력 파일 97개의 삭제다.
이 97개는 `git show --name-only -S 'SPONGE_ON' c249880`의 파일 경로 수다.
그 커밋에서 검색에 걸린 Fortran 파일은 없다.
둘째 검색의 다섯 패치는 모두 `LOGICAL :: SPONGE_ON=.FALSE.` 선언의 추가 또는 삭제다.
`b9c035d:src/mod_global.F:337`에도 이 선언만 있다.
제공된 이력에서 입력 스위치의 읽기·감쇠 적용 구현은 나오지 않았다.
따라서 A로 분류할 과거 구현 변경은 없다.
해석: 예제의 T가 완충층을 켠다는 동작은 제공된 코드와 이력에 없다.
현재 활성화 키는 FV2-302의 세 스위치다.

### 5.3 E의 반대 근거와 근거 강도

FV2-136의 반대 근거를 먼저 찾았다.
`src/samples.F:542`는 `! start from ghost cell`이라고 적는다.
2018-01-25 a99e3f8은 병렬 오프셋을 `npx*Mglob/px`에서 `iista - 1`로 바꿨다.
그러나 이 변경은 Nghost를 빼지 않는다.
`rg -ni 'xwavemaker' TVD/src/*.F`는 입력·출력·선언·초기화 호출·SC 계산을 찾았다.
호출 전에 Xwavemaker에 가상 셀 폭을 더하는 대입문은 없었다.
직교·구면 및 직렬·병렬 분기는 모두 같은 국소 I 오프셋을 쓴다.
GPU 호스트의 같은 초기화 식도 이 반대 근거를 제공하지 않는다.

서로 독립된 두 코드 좌표 근거는 다음과 같다.
`src/misc.F:171`은 `Ibeg=Nghost+1`이다.
`src/mod_global.F:129`는 `INTEGER, PARAMETER :: Nghost = 3`이다.
`src/init.F:577`은 직렬 내부 첫 점에 `Xco(Ibeg) = ZERO`를 준다.
`src/samples.F:315`의 다른 초기 파형은 `xr=(I-1)*DX-Nghost*DX`로 가상 셀을 뺀다.
그러나 `src/samples.F:548`은 `SC=1.0_SP/COSH(B*(I-Xwavemaker/DX-1)*DX)`다.
해석: 이 초기 고립파의 중심은 내부 좌표에서 Xwavemaker−3DX다.
2.1 p.62·65는 계산 영역을 x=0.0 m에서 −5.0 m까지 확장했다고 적는다.
2.1 p.65는 고립파 중심을 x=5.0에 놓았다고 적는다.
2.1 p.68의 주석은 `! note that means x = 5 m because the domain starts at x = -5`다.
p.68의 XWAVEMAKER=10.0과 DX=0.1을 현재 식에 넣으면 모델 좌표 중심은 9.7 m다.
같은 원점 변환을 적용한 실험 좌표 중심은 4.7 m다.
9.7과 4.7은 인용한 식과 입력에서 계산한 정적 산술값이다.
`b9c035d:src/samples.F:507`에도 `SC=1.0_SP/COSH(B*(I-Xwavemaker/DX-1)*DX)`가 있다.
E의 근거 강도는 강함이다.
이 판정은 실행 결과의 이동량을 측정한 판정이 아니다.

FV2-304의 반대 근거도 먼저 찾았다.
현재 기본 Makefile은 PARALLEL을 켠다.
따라서 기본 빌드는 문서의 경사 영점에 맞는 병렬 식을 쓴다.
직렬 식 위 `src/init.F:752`의 `! dont need this`는 Xslp 범위 검사 주석이다.
2017-06-07 2fcff96은 이 범위 검사를 주석으로 바꿨다.
이 주석은 경사 위치를 DX만큼 옮길 의도를 설명하지 않는다.
2021-10-31 2e17d92의 공백을 제외한 변경은 조파원 범위 계산이다.
`rg -ni 'Xslp|slope.*shift|shift.*slope' TVD/src/*.F`는 두 지형 분기와 입력·선언을 찾았다.
분기의 위치 차이를 보정하는 처리는 없었다.

병렬 전역 점 I의 내부 좌표는 (I−1)DX다.
직렬 국소 점 I의 내부 좌표는 (I−Ibeg)DX다.
`src/init.F:733`과 `:768`을 이 좌표로 각각 바꾸면 직렬 경사식의 영점이 병렬보다 DX만큼 오른쪽이다.
`b9c035d:src/init.F:550`과 `b9c035d:src/init.F:582`에도 두 식이 각각 있다.
해석: 같은 Xslp·DX·SLP가 빌드의 PARALLEL 여부에 따라 다른 지형을 만든다.
이는 같은 코드의 두 실행 경로 및 2.1 p.49의 x=10 m 설명과 모순한다.
E의 근거 강도는 강함이다.
이 보고서는 직렬·병렬 모델을 실행하여 지형 파일을 비교하지 않았다.

### 5.4 입력·구현·노트 차이의 최종 분류

각 행은 결론을 하나만 가진다.
일치 행은 이 표에 다시 넣지 않는다.
H 행은 §5.5에 같은 형식으로 적는다.
FV2-270의 PDF 저장 시점 기본 분기도 `fef45a7:src/fluxes.F:73–75`의 `ELSE` / `CALL DelxyFun` / `CALL CONSTRUCTION`이다.
따라서 이 철자 오기는 2016년 원고 시점과 2018년 PDF 저장 시점 모두에서 별도 옵션이 아니다.

| 행 ID | 항목 | 결론 | 근거(원문 인용) | 노트에 쓸 결론 문장 |
|---|---|---|---|---|
| FV2-005 | 2.1 장 출력 이름 | B 문서 오기 | 2.1 p.43 `eta_0001, eta_0002, ....`; `b9c035d:src/io.F:1305` `itmp1=mod(icount/10000,10)`; `b9c035d:src/io.F:1315` `write(file_name(5:5),'(I1)')itmp5   !ykchoi`. 현재 `src/io.F:4357`도 다섯째 자리를 쓴다. | 2.1 p.43의 장 출력 이름은 네 자리로 인쇄되었다. PDF와 함께 저장된 코드와 현재 코드는 eta_00001처럼 다섯 자리를 쓴다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-047 | INI_SOL의 LAGTIME | B 문서 오기 | 2.1 p.60·68 `LAGTIME = 5.0`; p.70·71 `LAGTIME = 0.0`. `b9c035d:src/io.F:336` `IF(WaveMaker(1:7)=='LEF_SOL')THEN` 아래 `b9c035d:src/io.F:339`만 `CALL READ_FLOAT(LAG_SOLI,FILE_NAME,'LAGTIME',ierr)`다. INI_SOL의 `b9c035d:src/io.F:377–380`은 AMP·DEP·XWAVEMAKER를 읽는다. | 이 예제의 INI_SOL은 LAGTIME을 읽지 않는다. LAGTIME은 LEF_SOL에서만 적용한다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-049 | SPONGE_ON 입력 | D 문서에만 있음 | 2.1 p.45·52·56 `SPONGE_ON = T`; p.60·68 `SPONGE_ON = F`. §5.2의 전체 rg -i와 git log -S 결과는 미사용 선언과 입력 예시만 찾았다. `src/io.F:2285`의 실제 읽기는 `CALL READ_LOGICAL(DIRECT_SPONGE,FILE_NAME,'DIRECT_SPONGE',ierr)`다. | SPONGE_ON은 제공된 코드 이력에서 입력 스위치로 구현되지 않았다. 현재 세 완충층 중 필요한 스위치를 명시해야 한다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-059 | 구면 Gamma2 | B 문서 오기 | 2.1 p.70·72 `Gamma2 = 0.0`. `b9c035d:src/io.F:704` `# if defined (CARTESIAN)` 아래 `b9c035d:src/io.F:705`가 `CALL READ_FLOAT(Gamma2,FILE_NAME,'Gamma2',ierr)`다. 현재 `src/io.F:2605–2634`도 같은 전처리 조건이다. | 구면 빌드는 Gamma2=0.0을 읽어 약비선형식을 선택하지 않는다. 이 줄은 구면 예제에서 적용되지 않는다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-062 | 구면 Beta_ref 조건 | C 문서 누락 | 2.1 p.71·72 `Beta_ref=-0.531`; `src/io.F:2635` `# if defined (ZALPHA)`; `src/io.F:2636` `CALL READ_FLOAT(Beta_ref,FILE_NAME,'Beta_ref',ierr)`. 2.1 p.8과 3.0 p.9는 `-DZALPHA`를 설명한다. `funwave_tvd_3.0.tex` 173행도 같은 플래그를 적는다. C의 범위는 2.1 p.71–72 입력 발췌에 Beta_ref 읽기의 ZALPHA 조건을 연결하지 않은 점이다. | 구면에서 Beta_ref 입력은 ZALPHA 분기에만 적용한다. 플래그 자체는 2.1 p.8·3.0 p.9에 설명되어 있다. 중첩 입력 발췌에 이 조건을 함께 적는다. [10-18 결론 검증 보완] |
| FV2-110 | 불규칙파의 왼쪽 완충층 | D 문서에만 있음 | 2.1 p.49 `A sponge layer is specified at the left side boundary`; p.52 `SPONGE_ON = T`. §5.2의 SPONGE_ON 전체 검색 결과에 입력 구현이 없다. `src/io.F:2374` `IF(DIFFUSION_SPONGE.OR.DIRECT_SPONGE.OR.FRICTION_SPONGE)THEN`은 세 실제 스위치를 검사한다. | 예제의 SPONGE_ON=T만으로 왼쪽 완충층은 켜지지 않는다. 폭 2 m를 적용하려면 현재 완충층 스위치를 명시해야 한다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-121 | 천퇴의 양쪽 완충층 | D 문서에만 있음 | 2.1 p.53–54 `two sponge layers with a width of 2m`; p.56 `SPONGE_ON = T`. §5.2의 rg -i·git log -S 결과에 이 입력의 적용 구현이 없다. | 천퇴 예제의 SPONGE_ON=T만으로 두 완충층은 켜지지 않는다. 3.0은 이 줄을 DIRECT_SPONGE=T로 바꾼다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-131 | 원뿔섬 관측점 수와 파일 | B 문서 오기 | 2.1 p.62 `NumberStations = 16`과 `seven gauges`, `sta_0022`가 함께 나온다. `b9c035d:src/io.F:999` `do i=1,NumberStations`; `b9c035d:src/io.F:1007` `write(file_name(1:4),'(I4.4)') i`. 현재 `src/io.F:3843`도 같은 루프다. `src/io.F:3866–3875`는 내부 격자 소속 조건으로 파일 생성을 제한한다. | NumberStations=16인 입력의 관측점 순번 범위는 1–16이다. 내부 격자에 속한 관측점만 파일을 만든다. 같은 문장의 seven gauges는 NumberStations=16과 맞지 않는다. Gauge 22라는 실험 이름을 sta_0022라는 출력 순번과 동일시하면 안 된다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-136 | 초기 고립파 중심 | E 코드 결함 후보 — 중간 | 2.1 p.65의 중심 5 m 및 p.68 `XWAVEMAKER = 10.0`; `src/samples.F:548` `SC=1.0_SP/COSH(B*(I-Xwavemaker/DX-1)*DX)`; `src/samples.F:315` `xr=(I-1)*DX-Nghost*DX`. §5.3은 의도 주석·2018년 병렬 보정·네 전처리 분기를 먼저 확인했다. `src/init.F:907–909`는 INI_SOL을 직접 호출한다. `src/samples.F:542` `! start from ghost cell`는 반대 근거다. 최초 `cab9425:samples.F:507`부터 같은 직렬식이다. `a99e3f8`(2018-01-25)은 병렬 분할 원점을 바꿨지만 Nghost를 차감하지 않았다. | 직교 INI_SOL 중심은 Xco 원점에서 XWAVEMAKER보다 3DX만큼 왼쪽이다. ghost 시작 주석을 반대 증거로 반영하여 강도를 중간으로 낮춘다. 구면의 변동 DX에는 일정 3DX 차이를 일반화하지 않는다. [git 판정 근거](FUNWAVE-git-verify-E2.md). [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-143 | 중첩 파 진폭 | B 문서 오기 | 2.1 p.69 `amplitude of 1m`; p.70·71 `AMP = 0.1`; `b9c035d:src/io.F:378` `CALL READ_FLOAT(AMP_SOLI,FILE_NAME,'AMP',ierr)`. 현재 `src/io.F:1132`도 같은 키다. | 중첩 예제의 실제 지정 진폭은 0.1 m다. 본문 1 m는 입력과 열 배 다르다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-144 | 중첩 관측점 i=500 | B 문서 오기 | 2.1 p.69 `x=2000.0m (i = 500`; `b9c035d:src/io.F:1108` `ista(i) = Nghost+dum1`; `b9c035d:src/misc.F:111` `Ibeg=Nghost+1`. 현재 `src/io.F:4032`와 `src/init.F:577`도 내부 첫 점을 1번·0 m에 대응시킨다. | i,j 관측점 경로에서 4 m 간격의 2000 m 지점은 i=501이다. 문서의 i=500은 한 격자 작다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-266 | 3.0 Cbrk2 기본값 | B 문서 오기 | 3.0 p.45 `Cbrk2=0.15, which are default values from Kennedy et al and this model.`; `24a88c3:src/mod_global.F:372` `REAL(SP) :: Cbrk1=0.65,Cbrk2=0.35,T_brk`; `fef45a7:src/io.F:2812` `Cbrk2 = 0.35_SP`; 현재 `src/io.F:3103`도 0.35다. | 3.0 해빈의 Cbrk2=0.15는 예제 지정값이다. 당시 코드와 현재 코드의 누락 기본값은 0.35다. Kennedy 원논문의 값은 이 판정에 포함하지 않는다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-267 | 3.0 공간 마찰 키 | A 판 차이 | `24a88c3:src/io.F:750` `CALL READ_LOGICAL(IN_Cd,FILE_NAME,'Friction_Matrix',ierr)`; `24a88c3:src/io.F:751` `CALL READ_STRING(CD_FILE,FILE_NAME,'Cd_file',ierr)`. 2019-07-25 9bae2f6은 현재의 FRICTION_MATRIX·FRICTION_FILE로 바꿨다. 변경 뒤 줄 원문은 §5.1에 있다. | 3.0 해빈의 마찰 키는 문서 시점에는 유효했다. 현재 TVD 입력에는 FRICTION_MATRIX와 FRICTION_FILE을 써야 한다. GPU는 이전 키를 유지한다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-269 | 3.0 관측점 파일 이름 | B 문서 오기 | 3.0 p.44 `sta_00001, sta_00002 ....`; `24a88c3:src/io.F:1022`와 `fef45a7:src/io.F:3253`의 원문은 각각 `write(file_name(1:4),'(I4.4)') i`다. 현재 `src/io.F:3869`도 네 자리다. | 3.0 관측점 이름의 다섯 자리 표기는 당시 코드와 다르다. 실제 이름은 sta_0001처럼 네 자리다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-270 | 3.0 THRID 철자 | B 문서 오기 | 3.0 p.52 `HIGH_ORDER = THRID`; `24a88c3:src/fluxes.F:73–75`의 원문은 `ELSE` / `CALL DelxyFun` / `CALL CONSTRUCTION`이다. 현재 `src/fluxes.F:101–103`도 이 기본 분기다. | THRID는 THIRD의 철자 오기다. 현재 파서는 이를 거부하지 않으며 THIRD와 같은 기본 구성 경로로 보낸다. 2.1의 실제 대조 원문은 p.53 `HIGH_ORDER = FOURTH`다. git 판정 파일의 p.52 `THIRD` 인용은 쪽 이미지와 달라 바로잡는다. B 판정은 유지한다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-300 | 입력 줄 형식·대소문자 | C 문서 누락 | `src/mod_input.F:287` `READ(10,'(A)',END=100) TEXT_READ`; `src/mod_input.F:297` `IF(ADJUSTL(TRIM(TMPV_NEXT)) == TRIM(MatchCharacter))THEN`; `src/mod_input.F:340` `DotLocation = index(VREAD,".")`. 대소문자 구분은 2.1 p.34·3.0 p.34와 `funwave_tvd_3.0.tex` 1061–1062행에 이미 명시되어 있다. 누락은 한 줄의 첫 `=`를 기준으로 읽는 규칙과 실수형 판별 규칙이다. `src/mod_input.F:295–298`과 `:156–164`가 각각 이를 적용한다. | 입력은 한 줄에 한 대입문으로 적는다. 대소문자 구분은 두 매뉴얼의 명시 규칙이다. 현재 READ_FLOAT는 소수점이 없는 값을 float로 판정하지 않고 중단하므로 예제 실수의 소수점을 보존한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-301 | 쇄파 기본 경로 | A 판 차이 | `b9c035d:src/mod_global.F:382` `LOGICAL :: VISCOSITY_BREAKING = .FALSE.`; 2019-06-16 6233886이 참으로 바꿨다. `6233886:src/io.F:2597` `VISCOSITY_BREAKING = .TRUE.`; 현재 `src/masks.F:179` `MASK9tmp(I,J)= 1`. | 2.1처럼 VISCOSITY_BREAKING을 생략하면 현재 TVD는 점성 쇄파를 선택한다. NSWE 전환 예제와 같은 경로에는 VISCOSITY_BREAKING=F를 명시해야 한다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-302 | 세 완충층 스위치 | C 문서 누락 | `src/io.F:2282` `DIFFUSION_SPONGE = .FALSE.`; `src/io.F:2287` `DIRECT_SPONGE = .FALSE.`; `src/io.F:2292` `FRICTION_SPONGE = .FALSE.`; `src/io.F:2322` `Csp = 0.1_SP`; `src/io.F:2355` `CDsponge = 5.0_SP`. 세 완충층과 Csp·CDsponge의 의미는 3.0 p.39 및 `funwave_tvd_3.0.tex` 1270–1278행에 있다. 누락은 2.1 예제의 현행 스위치 구분과 누락 기본값이다. `src/init.F:966–989`는 각 스위치가 참인 경우에 대응 완충층을 초기화한다. | 2.1 예제의 SPONGE_ON 대신 3.0 p.39의 세 스위치를 사용한다(FV2-049). 세 스위치의 누락 기본값은 거짓이다. DIFFUSION_SPONGE가 참이면 Csp를 읽고 누락 시 0.1을 쓴다. FRICTION_SPONGE가 참이면 CDsponge를 읽고 누락 시 5를 쓴다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-303 | 완충층 기본 수치 | C 문서 누락 | `src/io.F:2377` `Sponge_west_width = 0.0_SP`; `src/io.F:2391` `Sponge_east_width = 0.0_SP`; `src/io.F:2405` `Sponge_south_width = 0.0_SP`; `src/io.F:2419` `Sponge_north_width = 0.0_SP`; `src/io.F:2433` `R_sponge = 0.85_SP`; `src/io.F:2447` `A_sponge = 5.0_SP`. 2.1 p.38·3.0 p.39·Intro-TN p.12 및 `funwave_tvd_3.0.tex` 1280–1290행은 폭·감쇠율·최대 감쇠를 설명한다. R_sponge의 0.85–0.95 범위와 A_sponge의 약 5.0은 명시된 기본값과 구별한다. 읽기 조건은 `src/io.F:2374` `IF(DIFFUSION_SPONGE.OR.DIRECT_SPONGE.OR.FRICTION_SPONGE)THEN`이다. | 세 완충층 중 하나를 켠 경우 네 폭과 R_sponge·A_sponge를 읽는다. 이 읽기 구간의 누락 기본값은 네 폭 0, R_sponge 0.85, A_sponge 5다. C는 이 누락 기본값 설명에 한정한다. [10-18 결론 검증 보완] |
| FV2-304 | 직렬·병렬 경사 지형 | E 코드 결함 후보 — 강함 | `src/init.F:733` `VarGlob(I,J) = Depth_Flat-SLP*(I-(INT(Xslp/DX)+1))*DX`; `src/init.F:768` `Depth(I,J) = Depth_Flat-SLP*(I-(INT(Xslp/DX)+1+Ibeg))*DX`. §5.3은 기본 PARALLEL 설정·범위 검사 주석·수정 이력을 먼저 확인했다. | 같은 Xslp를 주어도 직교 직렬 SLOPE의 영점은 병렬보다 DX만큼 오른쪽이다. ghost 원점을 맞춘 뒤에도 차이가 남는다. 정적 근거 강도는 강함이다. 최초 `cab9425:init.F:559·591`부터 이 차이가 있다. `436e692`(2020-05-18)의 ghost 처리 수정은 경사 원점 식을 바꾸지 않았다. `TVD/Makefile:5`의 `PARALLEL    = true`와 `TVD/GNUMake/Makefile:5`의 `PARALLEL    = false`에서 각각 두 경로가 선택된다. [git 판정 근거](FUNWAVE-git-verify-E2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-305 | 조파원의 y 중심·범위 | C 문서 누락 | `src/io.F:1013`과 `src/io.F:1445` `Yc_WK = ZERO`; `src/init.F:1253` `IF(ABS(ymk_wk(J)-Yc_WK)<Ywidth_WK/2.0_SP) THEN`. Yc_WK 자체는 2.1 p.37·3.0 p.37에 있다. C는 2.1 p.52·56 예제에 없는 Yc_WK 기본값과 엄격한 범위 조건에 한정한다. `src/init.F:1253`의 `<`는 경계를 포함하지 않는다. | WK_TIME_SERIES·WK_REG의 Yc_WK 누락 기본값은 0이다. y 방향 활성 격자는 `IF(ABS(ymk_wk(J)-Yc_WK)<Ywidth_WK/2.0_SP) THEN`으로 고른다. 폭의 절반과 같은 거리에 있는 점은 제외한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-306 | 두 최소 수심의 병합 | A 판 차이 | `b9c035d:src/io.F:822`와 `b9c035d:src/io.F:828`은 두 입력을 따로 읽는다. 2017-05-01 285a6f6의 MIN 추가·2018-05-25 d69acc3의 MAX 변경·2023-11-13 93c0053의 MIN 복귀는 §5.1에 적었다. 현재 `src/io.F:2948` `MinDepthFrc=MIN(MinDepthFrc,MinDepth)`. | 현재 TVD는 두 최소 수심을 작은 값으로 병합한다. GPU는 큰 값으로 병합한다. 예제처럼 두 입력이 0.001로 같으면 값 차이는 없다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-307 | 공간 마찰장·Manning | 일치 | `src/io.F:2738` `CALL READ_LOGICAL(IN_Cd,FILE_NAME,'FRICTION_MATRIX',ierr)`; `src/io.F:2753` `CALL READ_STRING(CD_FILE,FILE_NAME,'FRICTION_FILE',ierr)`; `src/init.F:887` `Cd(I,J) = Cd_fixed`. MANNING별 전체 식은 §3에 인용했다. 공간 마찰장은 2.1 p.39·3.0 p.40·Intro-TN p.12 및 `funwave_tvd_3.0.tex` 1317–1326행에 있다. MANNING 조건은 2.1 p.9·34와 3.0 p.10·34에 있다. | FRICTION_MATRIX가 참이면 FRICTION_FILE의 공간 마찰장을 읽는다(`src/init.F:854–858`). 거짓이면 고정 Cd를 배포한다(`:884–887`). `src/sources.F:237–242`의 MANNING 분기는 같은 배열을 Manning 계수로 쓴다. 이 기능과 조건은 일반 입력·빌드 절에 설명되어 있으므로 문서 전체의 누락으로 분류하지 않는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-308 | 공간 구성법 선택 | C 문서 누락 | `src/fluxes.F:58` `! for the fourth-order, Choi used 4th + combined minmod and van leer`; `src/fluxes.F:61` `CALL CONSTRUCTION_HO   ! note choi used the name construction_ho_vanleer`; `src/fluxes.F:103` `CALL CONSTRUCTION`. 결합 limiter는 3.0 p.23·81 및 `funwave_tvd_3.0.tex` 629–630·2389–2390행에 설명된다. code_analysis p.15도 두 limiter의 호출 구조를 싣는다. C는 예제에 없는 접두어 선택과 기본 분기에 한정한다. `src/fluxes.F:56·71·81·89·101`은 FOU·FMI·WEN·MLP와 ELSE를 구분한다. | FOURTH는 결합 minmod·van Leer 구성으로 들어간다. 이 구성 자체는 3.0에 설명되어 있다. 예제에 빠진 조건은 FOU·FMI·WEN·MLP 접두어에 해당하지 않는 문자열이 ELSE의 기본 구성으로 간다는 점이다(FV2-270). [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-309 | 시간 적분 문자열 | C 문서 누락 | `src/io.F:2806` `CALL READ_STRING(Time_Scheme,FILE_NAME,'Time_Scheme',ierr)`; `src/main.F:379` `! 3-ORDER RUNGE-KUTTA TIME STEPPING`; `src/main.F:380` `DO ISTAGE=1,3`. 2.1 p.39·3.0 p.40·Intro-TN p.13 및 `funwave_tvd_3.0.tex` 1331행은 시간 적분 옵션을 설명한다. C는 Time_Scheme 읽기와 현재 실행 분기가 연결되지 않는다는 조건에 한정한다. src 전체의 Time_Scheme 검색은 선언·입력·로그·주석을 찾고 실행 선택 조건을 찾지 않는다. | 현재 main은 Time_Scheme 문자열로 분기하지 않고 `DO ISTAGE=1,3`을 실행한다. 예제의 Runge_Kutta는 이 경로와 맞는다. 다른 문자열을 입력해 Predictor_Corrector를 선택하는 기능은 이 읽기에서 생기지 않는다. [10-18 결론 검증 보완] |
| FV2-310 | 필수 입력의 생략 | C 문서 누락 | `src/io.F:248` `CALL READ_INTEGER(Mglob,FILE_NAME,'Mglob',ierr)` 뒤 `src/io.F:260` `STOP`; `src/io.F:263`의 Nglob 뒤 `src/io.F:275` `STOP`; `src/io.F:603`의 TOTAL_TIME 뒤 `src/io.F:616` `STOP`. Mglob·Nglob·TOTAL_TIME의 설명은 2.1 p.35–36·3.0 p.35–36 및 `funwave_tvd_3.0.tex` 1117–1129행에 있다. C는 2.1 p.70–72의 중첩 입력 발췌에서 격자 수를 생략한 범위에 한정한다. | 중첩 예제의 입력 발췌에는 Mglob·Nglob가 빠져 있다. 두 값은 코드에서 없으면 중단하므로 별도로 지정한다. 일반 입력 절은 이미 이 키를 설명한다. 병렬 PX·PY의 누락 기본값은 각각 1이다. [10-18 결론 검증 보완] |
| FV2-311 | 구면 i,j 관측점 조건 | C 문서 누락 | `src/io.F:84` `# if defined (SPHERICAL_IJ_STATION)`; `src/io.F:86` `CALL STATIONS_SPHERICAL_IJ`; 기본 경로의 `src/io.F:4197` `ista(i) = Nghost+1+nint((dum2-Lon_West)/Dphi)`. 기본 구면 관측점의 Lat/Lon 입력은 2.1 p.9·3.0 p.10 및 `funwave_tvd_3.0.tex` 177행에 있다. C는 2.1 p.69–72·3.0 p.76–79 중첩 예제에 없는 SPHERICAL_IJ_STATION 조건에 한정한다. | 기본 구면 관측점 파일은 위도·경도 순이다. i,j 파일은 SPHERICAL_IJ_STATION 분기에서 읽는다. COUPLING만으로 이 분기가 선택되지는 않는다(FV2-144). [10-18 결론 검증 보완] |
| FV2-312 | Makefile 위치 | A 판 차이 | 2.1 p.70 `Makefile in /src/`; `b9c035d:src/Makefile:17` `#             FLAG_8 = -DCOUPLING`. 2019-07-19 ca113a8이 루트 Makefile을 추가했다. 2019-07-24 7776fa5가 src/Makefile을 삭제했다. | 현재 기본 빌드에서는 TVD 루트의 Makefile에서 COUPLING을 설정한다. 문서의 src/Makefile 경로는 이전 빌드 구성이다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-313 | 결합 파일 검사·시간 보간 | C 문서 누락 | `src/nesting.F:58` `INQUIRE(FILE=TRIM(COUPLING_FILE),EXIST=FILE_EXIST)`; `src/nesting.F:93` `READ(11,*) TIME_COUPLING_1`; `src/nesting.F:371` `READ(11,*,IOSTAT=IOstatus) TIME_COUPLING_2`; `src/nesting.F:489` `IF(TIME_COUPLING_1.EQ.TIME_COUPLING_2)THEN`. 보간식의 연속 줄은 §3에 인용했다. 2.1 p.42·3.0 p.44는 중첩 자료와 첫 시각 초기화를 설명한다. C는 파일 끝과 같은 두 시각의 가중치 처리에 한정한다. `src/nesting.F:367–372·483–496`는 자료 갱신·EOF 이동과 `IF(TIME>TIME_COUPLING_1)THEN` 안의 가중치 조건을 보인다. | COUPLING 파일이 없으면 중단한다. 두 시각이 다르면 그 사이의 값을 선형 보간한다. 자료 끝에서 두 시각이 같고 TIME이 그 시각보다 크면 tmp1·tmp2를 0으로 둔다. 첫 자료 시각으로 시작하는 동작은 매뉴얼에 이미 설명되어 있다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-314 | 결과 폴더 끝 구분자 | C 문서 누락 | `src/io.F:4372` `TMP_NAME = TRIM(FDIR)//'eta_'//TRIM(FILE_NAME)`. 3.0 p.44도 RESULT_FOLDER를 설명한다. `funwave_tvd_3.0.tex` 1113행 예시는 끝 `/`를 포함하지만 Intro-TN p.17 예시는 포함하지 않는다. C는 이 구분자 결합 조건의 설명에 한정한다. | 파일 경로는 RESULT_FOLDER 뒤에 eta_ 등의 이름을 직접 붙여 만든다. 디렉터리 안에 저장하려면 `./output/`처럼 끝 `/`를 포함한다. 디렉터리 생성 명령은 그 구분자를 대신 붙이지 않는다. [10-18 결론 검증 보완] |
| FV2-315 | 바이너리·출력 해상도 | C 문서 누락 | `src/io.F:3332` `IF(ierr.EQ.1) FIELD_IO_TYPE = 'ASCII'`; `src/io.F:3367` `OUTPUT_RES = 1`; `src/io.F:4876–4877` `CASE ('BINARY' , 'binary' )` / `Call PutFileBinary(FILE_NAME,PHI)`. 2.1 p.43·3.0 p.44의 출력 절에는 FIELD_IO_TYPE·OUTPUT_RES 선택이 없다. `src/io.F:4894–4920`의 직렬 PutFile은 ASCII를 쓰며 내부 격자를 OUTPUT_RES 간격으로 순회한다. | 병렬 필드 출력은 FIELD_IO_TYPE으로 ASCII 또는 BINARY를 고른다. 누락 기본값은 ASCII다. 직렬 PutFile은 ASCII를 쓴다. OUTPUT_RES의 기본값 1은 내부 격자를 한 점 간격으로 출력하며, 이 값을 키우면 출력 점을 건너뛴다. [10-18 결론 검증 보완] |
| FV2-316 | 초기 고립파 진행 방향 | C 문서 누락 | `src/io.F:1103–1104` `CALL READ_LOGICAL(SolitaryPositiveDirection,FILE_NAME,  &` / `'SolitaryPositiveDirection',ierr)`; `src/io.F:1107` `SolitaryPositiveDirection = .TRUE.`; `src/samples.F:564` `U(I,J)=-A*SC*SC`. 2.1 p.60·68·70–72와 3.0의 대응 INI_SOL 예제에는 이 방향 입력이 없다. 입력 분기는 `src/io.F:1101` `IF(WaveMaker(1:7)=='INI_SOL')THEN`이다. `src/init.F:907–909`가 초기 고립파 루틴을 호출한다. | INI_SOL의 SolitaryPositiveDirection 누락 기본값은 참이다. `src/samples.F:561–565`에서 참이면 초기 u에 `U(I,J)=A*SC*SC`를, 거짓이면 `U(I,J)=-A*SC*SC`를 대입한다. 이 옵션은 LAGTIME과 별개다. [10-18 결론 검증 보완] |
| FV2-317 | 관측점 출력 버퍼 | C 문서 누락 | `src/io.F:666` `StationOutputBuffer = 1000`; `src/io.F:3905` `IF(BufferCount(i)<StationOutputBuffer.AND.TIME<TOTAL_TIME)THEN`; `src/io.F:3907` `ZUV_BUFFER(BufferCount(i),i,1)=time`. 나머지 세 열은 §3에 인용했다. 2.1 p.70·3.0 p.77의 매 시간 단계 출력 설명에는 버퍼 조건이 없다. `src/io.F:82–90`는 출력 간격·NumberStations 조건으로 호출한다. `:3916–3929`의 ELSE는 기존 버퍼를 쓴 뒤 개수를 0으로 재설정한다. 구면 i,j 경로의 같은 처리는 `:4073–4097`이다. | NumberStations가 양수이고 출력 간격 조건을 만족할 때 관측점 루틴을 호출한다. StationOutputBuffer의 누락 기본값은 1000이다. 버퍼를 채우는 분기와 기존 버퍼를 파일에 쓰는 분기는 따로 있다. PLOT_INTV_STATION=0.0의 호출 선택을 매 단계 즉시 파일 쓰기와 동일시하지 않는다. [10-18 결론 검증 보완] |
| FV2-318 | 건조 관측점 | C 문서 누락 | `src/io.F:3885–3888` `IF(mask(ista(i),jsta(i))<1)THEN` / `eta_sta=ZERO` / `u_sta=ZERO` / `v_sta=ZERO`. C는 2.1 p.62·70 및 3.0 p.70·77의 관측점 출력 설명에 없는 건조점 처리에 한정한다. `src/io.F:3843–3875`는 내부 격자에 속한 관측점을 고른다. 구면 i,j의 `:4053–4056`과 기본 구면의 `:4220–4223`에도 같은 0 처리가 있다. | 내부 격자에 속한 출력 관측점에서 `IF(mask(ista(i),jsta(i))<1)THEN`이면 eta_sta·u_sta·v_sta를 ZERO로 대입한다. 이 처리는 직교·구면 i,j·기본 구면 관측점 경로에 공통이다. [10-18 결론 검증 보완] |
| FV2-319 | 출력 시작·고정 시간간격 | C 문서 누락 | `src/io.F:622` `PLOT_START_TIME = 0.0`; `src/io.F:2883` `CALL READ_FLOAT(DT_fixed,FILE_NAME,'DT_fixed',ierr)`; `src/io.F:2885` `FIXED_DT = .TRUE.`; `src/io.F:2900` `FroudeCap = 3.0_SP`. C는 예제의 PLOT_START_TIME·DT_fixed 생략에 한정한다. `src/io.F:94` `IF(TIME>=PLOT_START_TIME)THEN`은 필드 출력을 제한한다. `src/misc.F:281–290`는 CFL의 DT_tmp를 계산하고 FIXED_DT일 때 `DT = DT_fixed` 뒤 `DO WHILE (DT > DT_tmp)` 안에서 `DT=DT/2.0_SP`를 수행한다. | PLOT_START_TIME의 누락 기본값은 0초이며 필드 출력의 시작 조건이다. DT_fixed를 제공하면 FIXED_DT를 켜지만 CFL 상한보다 큰 동안 시간간격을 반씩 줄인다. FroudeCap=10은 중첩 예제 지정값이고 현재 누락 기본값은 3이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-320 | 조파원 평균 흐름 보정 | C 문서 누락 | `src/io.F:2479` `CALL READ_FLOAT(WaveMakerCd,FILE_NAME,'WaveMakerCd',ierr)`; `src/io.F:2481` `WaveMakerCurrentBalance=.FALSE.`; `src/io.F:2488` `WaveMakerCurrentBalance=.TRUE.`. C는 2.1 예제 입력에 없는 WaveMakerCd 조건에 한정한다. `src/sources.F:274–285`의 `IF(WaveMakerCurrentBalance)THEN` 안에서 x·y 조파원 범위를 검사한 뒤 `-WaveMakerCd*U(I,J)*SQRT(U(I,J)*U(I,J)+V(I,J)*V(I,J))`를 쓴다. | WaveMakerCd를 읽으면 WaveMakerCurrentBalance를 참으로 둔다. 실제 추가 마찰은 sources.F의 조파원 범위 조건을 통과한 점에 적용한다. 입력이 없으면 이 선택을 끈다. 계수 0은 선택이 켜져도 해당 마찰항을 0으로 만든다. [10-18 결론 검증 보완] |
| FV2-321 | Time_ramp 누락 기본값 | C 문서 누락 | 3.0 p.45–46 해빈은 Time_ramp 줄을 싣지 않는다. `src/io.F:1519` `Time_ramp = 0.0_SP`; `src/sources.F:110` `AA = TANH(PI/(Time_ramp*Tperiod)*TIME)*D_gen`. 3.0 p.37 및 `funwave_tvd_3.0.tex` 1185행은 WK_REG에 Time_ramp가 필요하다고 적는다. C는 3.0 p.45–46 해빈 입력 발췌의 생략에 한정한다. `src/sources.F:109` `IF(WAVEMAKER(1:6)=='WK_REG')THEN` 아래 식으로 도달한다. | 2.1 p.44는 Time_ramp=1.0을 지정하지만 3.0 해빈 발췌는 생략한다. 현재 WK_REG 읽기는 누락 시 0.0_SP를 대입한다. 이어 `AA = TANH(PI/(Time_ramp*Tperiod)*TIME)*D_gen`의 분모가 0이 된다. 3.0 일반 입력 절의 필수 항목을 예제에도 명시한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-400 | 노트의 verbatim 입력 블록 | B 문서 오기 | `models/FUNWAVE/manual-notes/funwave-user-manual-full.md:241` `DEPTH TYPE = SLOPE ; DEPTH FLAT = 0.36 ; SLP = 0.0292 ; Xslp = 30.0`; `src/mod_input.F:298` `VAL  = ADJUSTL(TEXT(FRONT+1:TEXT_LENGTH))`. 3.0 p.45–46은 밑줄·개별 줄을 쓴다. 같은 노트 `models/FUNWAVE/manual-notes/funwave-user-manual-full.md:205`의 `Cd fixed`와 `models/FUNWAVE/manual-notes/funwave-user-manual-full.md:224`의 `STATION FILE`·`HMAX`도 실제 키와 다르다. | 기존 노트의 블록은 verbatim이 아니다. 밑줄과 한 줄 한 대입문을 복원한 AI 수정안을 원문과 구분한다. 관련 목록에는 Cd·STATIONS_FILE·Hmax를 쓴다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-401 | 노트의 관측점 이름 | B 문서 오기 | `models/FUNWAVE/manual-notes/funwave-user-manual-full.md:232`의 `sta_00001`; `src/io.F:3869` `write(file_name(1:4),'(I4.4)') i`. 3.0 p.44와 같은 이름 오기를 옮긴 노트다. 문서 시점에도 `24a88c3:src/io.F:1022`는 `write(file_name(1:4),'(I4.4)') i`를 쓴다. 같은 사실의 판정은 FV2-269와 B로 통일한다. | 노트의 sta_00001은 sta_0001로 고친다. 관측점 순번은 네 자리이고 장 출력 순번은 다섯 자리다. RESULT_FOLDER의 끝 `/` 조건은 FV2-314에 따른다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-402 | 노트의 Cbrk2 기본값 | B 문서 오기 | `models/FUNWAVE/manual-notes/funwave-user-manual-full.md:253`의 `Cbrk1=0.65·Cbrk2=0.15는 Kennedy et al. 및 본 모델 기본값`; `src/io.F:3103` `Cbrk2 = 0.35_SP`. 당시 원문은 FV2-266에 적었다. | Cbrk2=0.15를 해빈 예제 지정값으로 표시한다. 현재 코드의 누락 기본값은 0.35로 고친다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-403 | 노트의 Cbrk1 기본값 | B 문서 오기 | `models/FUNWAVE/source-analysis/funwave-physics-sources.md:17`의 `(개시~0.45)`; `src/io.F:3081` `Cbrk1 = 0.65_SP`. | 개시 계수의 현재 누락 기본값은 0.65다. 지속 계수의 누락 기본값은 0.35다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FV2-404 | 성분 자료와 원시 시계열 | C 문서 누락 | `models/FUNWAVE/source-analysis/funwave-physics-sources.md:29`의 `시계열(T,A,phase)`; `src/wavemaker.F:354` `READ(1,*)(WAVE_COMP(J,I),I=1,3)`; `src/sources.F:138` `BB1(kf,1) = COS(2.0_SP*PI/WAVE_COMP(kf,1)*TIME-WAVE_COMP(kf,3))`. 누락 범위는 이 분석 노트의 '시계열' 표현이다. 2.1 p.37·49와 3.0 p.37–38은 이미 FFT로 구한 성분 자료라고 설명한다. `src/wavemaker.F:351–354·2435–2437`과 `src/sources.F:135–143`은 WK_TIME 분기·주기 변환·성분 합성을 보인다. | WK_TIME_SERIES는 성분별 주기(s)·진폭(m)·위상(rad)의 세 열을 읽는다. 원시 수면 시계열의 FFT는 문서의 MATLAB 전처리 단계다. 모델 안의 성분 합성과 전처리를 구분한다. [10-18 결론 검증 보완] |
| FV2-405 | 초기 고립파 노트의 조건 | C 문서 누락 | `models/FUNWAVE/source-analysis/funwave-infrastructure.md:39`의 `INI_SOL Nwogu`; `src/io.F:924` `CALL READ_FLOAT(LAG_SOLI,FILE_NAME,'LAGTIME',ierr)`는 LEF_SOL 분기다. 중심 식은 FV2-136에 인용했다. 누락 범위는 이 분석 노트의 초기 고립파 적용 조건이다. `src/io.F:890·924·1101–1162`와 `src/init.F:907–909`가 LAGTIME 읽기 분기와 INI_SOL 초기 호출을 구분한다. 중심 식의 반대 근거는 `src/samples.F:542` `! start from ghost cell`이다. | INI_SOL은 초기 고립파를 배치한다. LAGTIME은 LEF_SOL에서만 읽는다(FV2-047). 직교 INI_SOL의 중심은 Xco 원점 기준 XWAVEMAKER보다 3DX 왼쪽이다. 의도 주석을 반영한 코드 결함 후보의 강도는 중간이다(FV2-136). [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-406 | 중첩 노트의 실행 조건 | C 문서 누락 | `models/FUNWAVE/source-analysis/funwave-infrastructure.md:43`의 `parent grid 경계 시계열 선형보간→ghost (one-way nesting)`; `src/main.F:238` `TIME=TIME_COUPLING_1`; `src/io.F:84` `# if defined (SPHERICAL_IJ_STATION)`. 누락 범위는 이 분석 노트의 초기 시각·관측점 분기·건조점 조건이다. 첫 결합 시각 초기화는 2.1 p.42·3.0 p.44에 이미 있다. 구면 i,j 경로의 `src/io.F:4053–4056·4085–4097`이 건조값과 FOAM별 출력 열을 보인다. | COUPLING 자식은 결합 자료의 첫 시각에서 시작한다. 구면 부모가 i,j 파일을 쓰려면 SPHERICAL_IJ_STATION을 정의한다. FOAM 미정의 시 관측점 파일은 time·η·u·v의 네 열이다. FOAM 정의 시 세 열을 더 쓴다. 건조 관측점의 η·u·v는 0이다(FV2-311·317·318). [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-409 | Cd=0의 적용 범위 | C 문서 누락 | `models/FUNWAVE/source-analysis/funwave-physics-sources.md:48`의 `마찰 완전 off`; `src/io.F:2779` `Cd_fixed = 0.0_SP`; `src/init.F:887` `Cd(I,J) = Cd_fixed`. 누락 범위는 이 분석 노트의 '마찰 완전 off'에 빠진 적용 조건이다. 일반 공간 마찰 설명은 2.1 p.39·3.0 p.40·Intro-TN p.12에 있다. `src/sources.F:237–242·262–265·274–285`는 바닥 마찰·마찰 완충층·조파원 마찰을 구분한다. | FRICTION_MATRIX가 거짓인 고정 마찰 경로에서는 Cd 누락 기본값 0이 바닥 마찰항을 0으로 만든다. 공간 마찰장은 파일 배열을 쓴다. FRICTION_SPONGE와 WaveMakerCd에 의한 추가 마찰은 별도 조건이다(FV2-307·320). [10-18 결론 검증 보완] |
| FV2-410 | 모델 개요의 기본 쇄파 경로 | C 문서 누락 | `models/FUNWAVE/README.md:18`의 `쇄파를 bore로 처리`; `src/io.F:2691` `VISCOSITY_BREAKING = .TRUE.`. 누락 범위는 README의 기본 쇄파 선택 설명이다. 2.1 p.39·3.0 p.40의 기본 충격 포착 설명과 현재 코드 기본값의 이력 차이는 FV2-301의 A 판정이다. `src/io.F:2689`는 VISCOSITY_BREAKING을 읽고 `src/masks.F:177–185`는 이 값에 따라 MASK9 경로를 나눈다. | TVD 플럭스와 쇄파 방식 선택을 구분한다. 현재 TVD는 VISCOSITY_BREAKING을 생략하면 참으로 둔다. 예제의 NSWE 전환 경로를 선택하려면 거짓을 지정하고 실제 MASK9 분기 조건을 적용한다(FV2-301·107). [10-18 결론 검증 보완] |
| FV2-411 | 노트의 쇄파 기본값 | A 판 차이 | `models/FUNWAVE/manual-notes/funwave-user-manual-full.md:201`의 `default는 shock-capturing`; `b9c035d:src/mod_global.F:382` `LOGICAL :: VISCOSITY_BREAKING = .FALSE.`. 2019-06-16 6233886의 `6233886:src/io.F:2597`은 `VISCOSITY_BREAKING = .TRUE.`다. | 문서의 shock-capturing 기본값은 이전 코드 설명이다. 현재 TVD 입력 생략 시에는 점성 쇄파를 선택한다. [git 판정 근거](FUNWAVE-git-verify-AD2.md). [10-18 결론 검증 보완] [10-18 git 이력 판정] |

### 5.5 H의 최종 분류

다음 행은 예제 결과·실험·권고·수학적 정의·외부 도구·서지에 해당한다.
같은 예제의 문서판별 설정 변경도 H로 기록한다.
코드 키의 미구현·오기·변경은 §5.4의 별도 행에 분리했다.

| 행 ID | 항목 | 결론 | 근거(원문 인용) | 노트에 쓸 결론 문장 |
|---|---|---|---|---|
| FV2-008 | 현재 장 출력 형식 | 일치 | funwave_tvd_2.1_manual.pdf p.43: `The NetCDF output format is under development.` `src/io.F:3330–3332·4873–4880`의 병렬 선택기는 ASCII·BINARY와 기본 ASCII 분기를 둔다. 직렬 경로 `:4894–4920`는 ASCII를 쓴다. | 일치는 NetCDF 출력이 이 선택기에 구현되어 있지 않다는 범위다. 2.1의 개발 중 문장을 NetCDF 지원으로 읽지 않는다. 현재 병렬 장 출력은 ASCII·BINARY이고 직렬 장 출력은 ASCII다(FV2-315). [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-100 | 5장 검증 서문 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.43: `The model has been validated extensively using laboratory experiments for wave shoaling and breaking as in the FUNWAVE manual by Kirby et al. (1998).`; `Tests of mass conservation and convergence are included in Tehranirad et al. (2011).` | 기존 검증·질량 보존·수렴성 시험의 서술은 과거 결과 소개다. |
| FV2-101 | 해빈 실험 조건 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.43: `Waves were generated on a flat bottom a 0.36 m depth, and the beach slope was 1:34.26.`; `The wave height and wave period are 4.3 cm and 3.33 s, respectively, for the plunging case, and 6.7 cm and 1.67 s for the spilling case.` | Hansen–Svendsen의 수심·경사·파고·주기는 실험 조건으로 기록한다. |
| FV2-102 | 해빈의 격자 간격 입력 | 일치 | funwave_tvd_2.1_manual.pdf p.43: `we adopted three grid sizes, dx = 0.05 m, 0.025 m and 0.0125 m, respectively, for each cases.` 2.1 p.44의 발췌는 `DX = 0.025`를 지정한다. `src/io.F:284–286`의 CARTESIAN 분기에서 DX를 읽는다. | 일치는 직교 격자 간격을 DX 실수 입력으로 지정하는 경로에 한정한다. p.43의 0.05·0.025·0.0125 m는 문서가 사용했다고 보고한 세 해상도이고, 발췌 입력은 0.025 m 한 값이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-103 | 해빈의 파고·평균수위 결과 | B 문서 오기 | funwave_tvd_2.1_manual.pdf p.43–44: `All three models underpredict the peak wave height at breaking and overpredict wave height inside of the surfzone.`; `About 10% underprediction of peak wave height can be found in our tests with dx = 0.025 m and 0.0125 m`; `The model with a coarser grid (dx = 0.05 m) underpredicted the maximum wave height by 20%.` 2.1 p.44의 두 `dx = 0.25 m` 표기는 p.43의 해상도 목록·p.44 입력 `DX = 0.025`·p.48 그림 5의 `dx = 0.025 m`와 다르다. | B는 결과 설명의 격자 간격 오기에 한정한다. 0.25 m는 0.025 m로 바로잡아 읽는다. 파고 과소·과대 예측과 평균수위 평가는 문서가 보고한 결과다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-104 | 1차원 DY 권고와 입력 | 일치 | funwave_tvd_2.1_manual.pdf p.44: `! give any larger value than DX for 1-D case` 2.1 p.44의 실제 입력은 `DX = 0.025`, `DY = 0.2`다. `src/io.F:286·304`는 두 값을 각각 READ_FLOAT로 읽는다. | DY=0.2는 DX=0.025보다 큰 예제 지정값이다. 코드의 입력 경로는 이 두 값을 각각 읽는다. 문서 주석은 사례의 권고이며 DY와 DX의 크기 비교를 강제하는 입력 조건은 아니다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-105 | 고정 Cd의 입력 적용 | 일치 | funwave_tvd_2.1_manual.pdf p.45: `! Cd is not sensitive for this case`; p.53: `! not sensitive for this case`; p.62: `! note: not sensitive, could give a small value like 0.001` `src/io.F:2738–2740·2777–2779`는 FRICTION_MATRIX와 Cd를 읽는다. `src/init.F:884–887`은 고정 Cd를 배열로 배포한다. `src/sources.F:237–242`가 그 배열을 마찰항에 사용한다. | 일치는 FRICTION_MATRIX가 거짓인 예제에서 Cd를 읽고 마찰항에 적용하는 경로에 한정한다. '민감하지 않다'는 문서의 사례 평가다. 이 표현은 Cd 입력을 생략하거나 무시하는 분기라는 뜻이 아니다(FV2-307·409). [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-106 | 그림 3 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.46 그림 3: `Comparisons of wave height (upper panel) and wave setup (lower panel) between measured data and model results from grid resolutions of dx = 0.0125 m, 0.025 m and 0.050 m, respectively. Case: plunging breaker.` | 그림 3의 파고·평균수위 비교는 기존 결과다. |
| FV2-107 | 그림 4와 전환 시각 | F 표현 차이 | funwave_tvd_2.1_manual.pdf p.47 그림 4: `Snapshots of surface elevation at t = 17.4, 18.6 and 19.9 s from models with grid resolutions of dx = 0.025 (solid lines) and 0.050 m (dashed lines).`; p.44: `the ratio of surface elevation to water depth reached the threshold value of 0.8.` `src/io.F:2689·2713`는 VISCOSITY_BREAKING·SWE_ETA_DEP를 읽는다. `src/masks.F:177–184`는 VISCOSITY_BREAKING이 거짓인 분기에서 임계값을 검사한다. | 문서의 '0.8에 도달'은 전환을 요약한 표현이다. 실제 조건은 `IF(ABS(Eta(I,J))/MAX(DEPTH(I,J),MinDepthFrc)>SWE_ETA_DEP)THEN`이다. 0.8과 같다는 조건이 아니다. 점성 쇄파 선택 시 이 검사는 우회한다(FV2-301). 19.9초는 문서가 보고한 전환 시각이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-108 | 그림 5 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.48 그림 5: `Model/data comparisons of wave height (upper panel) and wave setup (dx = 0.025 m). Case: spilling breaker.` | 그림 5는 붕파형의 결과다. 본문 0.25 m와 그림의 0.025 m를 구분한다. |
| FV2-109 | 불규칙파 실험 조건 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.45: `a constant depth of 0.47 m on the left connects to a constant slope of 1:20 on the right.`; `0.6 Hz (run 1) and 1.0 Hz (run 2)`; `The target incident spectrum was a Pierson-Moskowitz spectrum.` | Mase–Kirby의 수심·경사·스펙트럼·파고계 배치는 실험 조건이다. |
| FV2-111 | FFT 전처리 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.49: `A FFT was used to transform between the time domain and frequency domain data required by the wavemaker.`; `fft4wavemaker.m`; `r2d470.dat`; `wavemk_per_amp_pha.txt`; `The low and high-frequency cutoffs are 0.2 and 10.0 Hz, respectively.` | MATLAB FFT 절차와 주파수 차단값을 Fortran 조파기 내부 처리로 쓰지 않는다. |
| FV2-113 | 식 (79) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.49 식 (79), §2.4.1에 옮긴 인쇄식; `where H denotes the Hilbert transform, <> is the mean operator, and the mean has been removed from the time series of surface elevation.` | 왜도·비대칭도의 식 (79)은 후처리 정의다. 3.0의 같은 식은 (106)이다. |
| FV2-114 | 그림 6 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.50 그림 6: `Experiment layout of Mase and Kirby (1992).` | 그림 6은 실험 배치도다. |
| FV2-115 | 그림 7 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.50 그림 7: `Time series comparison of η between model (dashed lines) and data (solid lines) at 11 wave gauges in Mase and Kirby (1992).`; p.49: `from t = 20 s to t = 40 s` | 11개 파고계의 20–40초 시계열 비교는 기존 결과다. |
| FV2-116 | 그림 8 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.51 그림 8: `Comparison of skewness (◦) and asymmetry (×) at different water depths. Solid lines are experiment data ( Mase and Kirby, 1992). Dashed lines are numerical results` | 왜도·비대칭도 곡선은 기존 결과다. |
| FV2-117 | 불규칙파 통계 결과 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.49: `The model predicted skewness and asymmetry reasonably well with a slightly overprediction of wave skewness inside the surf zone.` | 쇄파대 왜도 과대 예측을 포함한 문서의 통계 평가를 결과 주장으로 인용한다. |
| FV2-118 | 필터 없는 안정성 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.49: `The present model did not encounter any stability problem without filtering.` | 필터 없이 안정했다는 문장은 해당 과거 계산의 결과다. |
| FV2-120 | 천퇴의 지형 파일·조파원 입력 | 일치 | funwave_tvd_2.1_manual.pdf p.53: `an elliptic shoal resting on a plane beach with a constant slope 1/50.`; `20° to the y axis`; `period of 1s and amplitude of 2.32cm`; `x = −10m`; `y = −10m and y=10m` 2.1 p.54·56은 `DEPTH_TYPE = DATA`와 `Xc_WK = 3.0`을 지정한다. `src/io.F:485–486·1427–1428`이 DATA·WK_REG 입력을 읽고 `src/init.F:701–707`이 수심 배열을 읽는다. | 일치는 지형 파일과 모델 좌표의 Xc_WK를 읽는 경로에 한정한다. 실험의 조파 위치 x=−10 m와 모델 입력 Xc_WK=3.0은 서로 다른 좌표 표기다. 실험 배치·파고·주기는 문서의 사례 조건으로 적는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-122 | 그림 9·10 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.54 그림 9: `Experiment layout for wave focusing experiment of Berkhoff et al. (1982).`; p.55 그림 10: `Comparisons of wave height along specified sections between the model (solid lines) and experiment data (circles).` | 천퇴 배치도와 8개 측선의 파고 비교는 실험·기존 결과 자료다. |
| FV2-123 | 원뿔섬 실험 조건 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.57: `a 30m-wide, 25m-long, and 60cm-deep wave basin`; `a 62.5cm-high, 7.2m toe-diameter, and 2.2m crest-diameter circular island with a 1:4 slope`; `depth of 32cm`; `H/d=0.045, 0.091, 0.181`; `27 wave gages` | 원뿔섬 형상·수심·세 입사 파고비·27개 파고계는 실험 조건이다. |
| FV2-124 | 그림 11 캡션 | B 문서 오기 | funwave_tvd_2.1_manual.pdf p.58 그림 11: `View of conical island(top) and basin(bottom)(from Synolakis et al (2007, Figure A16)).` 2.1 p.58 그림 11은 Gauge 6·9·16·22의 네 곡선 패널이다. 3.0 p.65 그림 15에도 같은 전경 캡션과 곡선 그림의 충돌이 있다. `funwave_tvd_3.0.tex` 1984–1985행은 caseA.pdf와 전경 캡션을 결합한다. | 그림 11의 전경 캡션은 실제 관측점별 곡선 그림과 맞지 않는 문서 편집 오류다. 그림 12·13에도 같은 종류의 오류가 있다(FV2-125·126). [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-125 | 그림 12 캡션 | B 문서 오기 | funwave_tvd_2.1_manual.pdf p.58 그림 12: `Definition sketch for conical island. All dimensions are in cm (from Synolakis et al (2007, Figure A17)).` 2.1 p.58 그림 12는 Gauge 6·9·16·22의 네 곡선 패널이다. 3.0 p.66 그림 16도 치수 정의도 캡션 아래 같은 종류의 곡선을 싣는다. `funwave_tvd_3.0.tex` 1991–1992행은 caseB.pdf와 정의도 캡션을 결합한다. | 그림 12의 치수 정의도 캡션은 실제 관측점별 곡선 그림과 맞지 않는 문서 편집 오류다(FV2-124·126). [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-126 | 그림 13 캡션 | B 문서 오기 | funwave_tvd_2.1_manual.pdf p.59 그림 13: `Schematic gauge locations around the conical island(from Synolakis et al (2007, Figure A18)).` 2.1 p.59 그림 13은 Gauge 6·9·16·22의 네 곡선 패널이다. 3.0 p.66 그림 17도 관측점 배치도 캡션 아래 같은 종류의 곡선을 싣는다. `funwave_tvd_3.0.tex` 1998–1999행은 caseC.pdf와 배치도 캡션을 결합한다. | 그림 13의 관측점 배치도 캡션은 실제 관측점별 곡선 그림과 맞지 않는 문서 편집 오류다(FV2-124·125). [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-127 | 표 1 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.59 표 1: `Percent error of predicted maximum runup calculated for each gauge in conical island test.`; 열 `H/d`, `6`, `9`, `16`, `22`; 행 0.045 행의 셀 `6.0`·`13.2`·`0.1`·`18.9`; 0.091 행의 셀 `3.2`·`16.6`·`11.6`·`0.26`; 0.181 행의 셀 `1.6`·`13.33`·`13.8`·`13.3` | 최대 처오름 오차 12개는 문서의 기존 결과다. |
| FV2-128 | 그림 14 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.60 그림 14: `Comparison of computed and measured time series of free surface for H/d = 0.045.Solid lines: measured, Dashed lines: Computed.` | H/d=0.045의 Gauge 6·9·16·22 시계열은 기존 결과다. |
| FV2-129 | 그림 15 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.61 그림 15: `Comparison of computed and measured time series of free surface for H/d = 0.091.Solid lines: measured, Dashed lines: Computed.` | H/d=0.091의 시계열은 기존 결과다. |
| FV2-130 | 그림 16 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.61 그림 16: `Comparison of computed and measured time series of free surface for H/d = 0.181.Solid lines: measured, Dashed lines: Computed.` | H/d=0.181의 시계열은 기존 결과다. |
| FV2-132 | 원뿔섬 후처리 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.62: `A post-processing MATLAB script called plot_comparison.m can be used for model/data comparisons.` | plot_comparison.m 사용법은 외부 후처리 절차다. |
| FV2-133 | 천해붕 실험·그림 17 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.62–63: `The basin is 48.8 m long, 26.5 m wide, and 2.1 m deep.`; `a 1:30 slope planar beach connected to a triangle shaped shelf and a conical island`; 그림 17: `Bathymetry contours (in meters) and measurement locations used in model/data comparisons. Circles: pressure gauges, triangles: ADV.` | 천해붕의 실험 수조·지형·파고계·ADV 배치는 실험 조건이다. |
| FV2-134 | 그림 18 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.64 그림 18: `Modeled water surface at (top) t=6.4 s, (middle) t=8.4 s, (bottom) t=14.4 s.` | 수면변위 순간장은 문서의 기존 결과다. |
| FV2-137 | 그림 19·Froude 결과 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.65 그림 19: `Time step variation.`; `The time step dropped to a minimum, at around t = 6.5 s`; `The local Froude number reached a maximum at t = 6.5 s` | 시간간격 곡선과 약 6.5초의 Froude 제한은 과거 계산의 결과다. |
| FV2-138 | 그림 20 | B 문서 오기 | funwave_tvd_2.1_manual.pdf p.66 그림 20: `Model/data comparisons of time series of surface elevation at (top) Gauge 1 - Gauge 9. Solid line: model, stars: data.`; p.65: `over-predicts the peak of wave runup.` 2.1 p.66의 내부 범례는 실선 data·파선 model이다. 그림에는 캡션의 별표가 없다. 3.0 p.73 그림 23도 같은 충돌을 보인다. `funwave_tvd_3.0.tex` 2136행은 충돌하는 캡션을 유지한다. | B는 캡션과 범례의 충돌에 한정한다. 인용 시 내부 범례의 실선 data·파선 model을 명시한다. Gauge 3의 처오름 첨두 과대 예측과 Gauge 5·6·8·9의 굴절·쇄파 평가는 본문의 결과 주장으로 적는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-139 | 그림 21 | B 문서 오기 | funwave_tvd_2.1_manual.pdf p.67 그림 21: `Solid line: model, dashed line: data.`; p.68: `An underprediction of the seaward velocity is found at ADV 2.`; `The velocity in the y-direction was not compared at ADV1 and ADV2 because the measured values were too small.` 2.1 p.67의 내부 범례는 실선 data·파선 model이다. 캡션은 두 선의 의미를 반대로 적는다. 3.0 p.74 그림 24와 `funwave_tvd_3.0.tex` 2143행에도 같은 충돌이 있다. | B는 캡션과 범례의 충돌에 한정한다. 인용 시 내부 범례의 실선 data·파선 model을 명시한다. 본문은 ADV 2의 해향 유속을 과소 예측했다고 보고한다. ADV 1·2의 y 유속은 측정값이 너무 작아 비교에서 제외했다고 적는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-140 | 천해붕 후처리 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.69: `read_result.m`; `plot_WG.m`; `plot_ADV_AB.m`; `plot_ADV_C.m` | MATLAB 파일 사용법은 외부 후처리 절차다. |
| FV2-141 | 중첩 파형 유지 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.69: `a solitary wave of permanent form is undistorted as it moves from a large domain Grid_A to a smaller scale grid Grid_B.` | 큰 영역에서 작은 영역으로 옮겨도 파형이 유지된다는 문장은 결과 주장이다. |
| FV2-145 | 중첩 디렉터리·변환 절차 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.69–70: `/examples/sph_nesting /`; `/grid_A/`; `/make_nest_file/`; `/grid_B/`; `generate nesting input file using convert.f in /make_nest_file/.`; `use plot_ab.m to plot results.` | convert.f와 plot_ab.m 사용법은 사례 전처리·후처리 안내다. |
| FV2-146 | 그림 22 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.73 그림 22: `Solitary wave calculated in a larger domain Grid_A (upper) and in a nested smaller domain Grid_B (lower) at t=100s, 200s, 300s, and 400s.` | 100·200·300·400초의 두 영역 파형은 문서의 기존 결과다. [10-18 결론 검증 정정] |
| FV2-150 | 참고문헌 — Agnon, Madsen and Schäffer (1999) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.72: Agnon, Madsen and Schäffer (1999), `A new approach to high-order Boussinesq models`, J. Fluid Mech. 399, 319–333 | Agnon, Madsen and Schäffer (1999)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-151 | 참고문헌 — Berkhoff, Booy and Radder (1982) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.72: Berkhoff, Booy and Radder (1982), `Verification of numerical wave propagation models for simple harmonic linear water waves`, Coast. Engrg. 6, 255–279 | Berkhoff, Booy and Radder (1982)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-152 | 참고문헌 — Bermùdez and Vàzquez (1994) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.72: Bermúdez and Vázquez (1994), `Upwind methods for hyperbolic conservation laws with source terms`, Comput. Fluids 23 (8), 1049–1071 | Bermúdez and Vázquez (1994)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. [10-18 결론 검증 정정] |
| FV2-153 | 참고문헌 — Briggs, Synolakis and Harkins (1994) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.72: Briggs, Synolakis and Harkins (1994), `Tsunami run- up on a conical island`, Proc., Waves-Physical and Numerical Modelling, 446–455 | Briggs, Synolakis and Harkins (1994)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-154 | 참고문헌 — Brown et al. (2009) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.72: Brown et al. (2009), `Surf zone diffusivity on a rip-channeled beach`, J. Geophys. Res. 114, C11015, doi:10.1029/2008JC005158 | Brown et al. (2009)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-155 | 참고문헌 — Chen et al. (1999) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.72: Chen et al. (1999), `Boussinesq modelling of a rip current system`, J. Geophys. Res. 104, 20,617–20,637 | Chen et al. (1999)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-156 | 참고문헌 — Chen et al. (2000) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.72: Chen et al. (2000), `Boussinesq modeling of wave transformation, breaking and runup. II: 2D`, J. Waterway, Port, Coastal and Ocean Engineering 126, 48–56 | Chen et al. (2000)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-157 | 참고문헌 — Chen et al. (2003) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.74: Chen et al. (2003), `Boussinesq modeling of longshore currents`, Journal of Geophysical Research 108(C11), 3362, doi:10.1029/2002JC001308 | Chen et al. (2003)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-158 | 참고문헌 — Chen, Kaihatu and Hwang (2004) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.74: Chen, Kaihatu and Hwang (2004), `Incorporation of Wind Effects Into Boussinesq Wave Models`, J. Waterway, Port, Coastal and Ocean Engineering 130, 312–321 | Chen, Kaihatu and Hwang (2004)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-159 | 참고문헌 — Chen (2006) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.74: Chen (2006), `Fully nonlinear Boussinesq-type equations for waves and currents over porous beds`, Journal of Engineering Mechanics 132 (2), 220–230 | Chen (2006)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-160 | 참고문헌 — Erduran, Ilic and Kutija (2005) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.74: Erduran, Ilic and Kutija (2005), `Hybrid finite-volume finite-difference scheme for the solution of Boussinesq equations`, Int. J. Numer. Meth. Fluid. 49, 1213–1232 | Erduran, Ilic and Kutija (2005)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-161 | 참고문헌 — Gobbi, Kirby and Wei (2000) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.74: Gobbi, Kirby and Wei (2000), `A fully nonlinear Boussinesq model for surface waves. II. Extension to` $O(kh^4)$, Journal of Fluid Mechanics 405, 181–210 | Gobbi, Kirby and Wei (2000)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-162 | 참고문헌 — Gottlieb, Shu and Tadmore (2001) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.74: Gottlieb, Shu and Tadmore (2001), `Strong stability-preserving high-order time discretization methods`, SIAM Review 43 (1), 89–112 | Gottlieb, Shu and Tadmore (2001)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-163 | 참고문헌 — Hansen and Svendsen (1979) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.74: Hansen and Svendsen (1979), `Regular waves in shoaling water: Experimental data`, Tech. Rep. ISVA Ser. 21, Technical Univ. of Denmark | Hansen and Svendsen (1979)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-164 | 참고문헌 — Kennedy et al. (2000) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.74: Kennedy et al. (2000), `Boussinesq modeling of wave transformation, breaking and runup. I: 1D`, J. Waterway, Port, Coastal and Ocean Engineering 126, 39–47 | Kennedy et al. (2000)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-165 | 참고문헌 — Kennedy et al. (2001) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.74: Kennedy et al. (2001), `Boussinesq-type equations with improved nonlinear performance`, Wave Motion 33, 225–243 | Kennedy et al. (2001)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-166 | 참고문헌 — Kim, Cho and Kim (2008) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.74: Kim, Cho and Kim (2008), `Well-balanced scheme between flux and source terms for computation of shallow-water equations over irregular bathymetry`, Journal of Engineering Mechanics 134, 277–290 | Kim, Cho and Kim (2008)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-167 | 참고문헌 — Kim, Lynett and Socolofsky (2009) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.74: Kim, Lynett and Socolofsky (2009), `A depth-integrated model for weakly dispersive, turbulent, and rotational fluid flows`, Ocean Modeling 27, 198–214 | Kim, Lynett and Socolofsky (2009)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. [10-18 결론 검증 정정] |
| FV2-168 | 참고문헌 — Kim (2009) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.74: Kim (2009), `Turbulent flow and transport modeling by long waves and currents`, Ph.D. dissertation, Texas A&M University | Kim (2009)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-169 | 참고문헌 — Kirby et al. (1998) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.74: Kirby et al. (1998), `FUNWAVE 1.0, Fully nonlinear Boussinesq wave model. Documentation and users manual`, Report CACR-98-06 | Kirby et al. (1998)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-170 | 참고문헌 — Kirby et al. (2004) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.74: Kirby et al. (2004), `Propagation of short dispersive tsunami waves in ocean basins`, EOS Transactions of the AGU 85 (47), Abstract OS21E-02 | Kirby et al. (2004)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. [10-18 결론 검증 정정] |
| FV2-171 | 참고문헌 — Kirby et al. (2012) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.75: Kirby et al. (2012), `Sensitivity analysis of trans-oceanic tsunami propagation to dispersive and Coriolis effects`, Ocean Modelling, `under revision` | Kirby et al. (2012)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-172 | 참고문헌 — Liang and Marche (2009) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.75: Liang and Marche (2009), `Numerical resolution of well-balanced shallow water equations with complex source terms`, Advances in Water Resources 32, 873–884 | Liang and Marche (2009)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-173 | 참고문헌 — Long and Kirby (2006) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.75: Long and Kirby (2006), `Boussinesq modeling of waves, currents and sediment transport`, Research Report CACR-06-02 | Long and Kirby (2006)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-174 | 참고문헌 — Lynett, Wu and Liu (2002) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.75: Lynett, Wu and Liu (2002), `Modeling wave runup with depth-integrated equations`, Coastal Engineering 46, 89–107 | Lynett, Wu and Liu (2002)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-175 | 참고문헌 — Madsen and Srensen (1992) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.75: Madsen and Srensen (1992), `A new form of the Boussinesq equations with improved linear dispersion characteristics. Part 2. A slowly-varying bathymetry`, Coastal Engineering 18 (3-4), 183–204 | Madsen and Srensen (1992)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-176 | 참고문헌 — Mase and Kirby (1992) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.75: Mase and Kirby (1992), `Hybrid frequency-domain KdV equation for random wave transformation`, Proc., 23rd Int. Conf. Coast. Eng., 474–487 | Mase and Kirby (1992)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-177 | 참고문헌 — Naik, Naik and Nicoules (1993) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.75: Naik, Naik and Nicoules (1993), `Parallelization of a class of implicit finite difference schemes in computational fluid dynamics`, International Journal of High Speed Computing 5, 1–50 | Naik, Naik and Nicoules (1993)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-178 | 참고문헌 — Ning et al. (2008) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.75: Ning et al. (2008), `Boussinesq cut-cell model for non-linear wave interaction with coastal structures`, International Journal for Numerical Methods in Fluids 57 (10), 1459–1483 | Ning et al. (2008)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-179 | 참고문헌 — Nwogu (1993) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.75: Nwogu (1993), `An alternative form of the Boussinesq equations for nearshore wave propagation`, Journal of Waterway, Port, Coastal and Ocean Engineering 119 (6), 618–638 | Nwogu (1993)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-180 | 참고문헌 — Nwogu and Demirbilek (2001) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.75: Nwogu and Demirbilek (2001), `BOUSS-2D: A Boussinesq wave model for coastal regions and harbors`, ERDC/CHL TR-01-25 | Nwogu and Demirbilek (2001)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-181 | 참고문헌 — Roeber, Cheung and Kobayashi (2010) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.75: Roeber, Cheung and Kobayashi (2010), `Shock-capturing Boussinesq-type model for nearshore wave processes`, Coastal Engineering 57, 407–423 | Roeber, Cheung and Kobayashi (2010)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-182 | 참고문헌 — Rogers, Borthwick and Taylor (2003) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.75: Rogers, Borthwick and Taylor (2003), `Mathematical balancing of flux gradient and source terms prior to using Roe’s approximate Riemann solver`, Journal of Computational Physics 192, 422–451 | Rogers, Borthwick and Taylor (2003)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-183 | 참고문헌 — Shi et al. (2012 a) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.75: Shi et al. (2012 a), `A high-order adaptive time-stepping TVD solver for Boussinesq modeling of breaking waves and coastal inundation`, Ocean Modelling 43-44, 36–51 | Shi et al. (2012 a)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-184 | 참고문헌 — Shi, Kirby and Tehranirad (2012 b) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.76: Shi, Kirby and Tehranirad (2012 b), `Tsunami benchmark results for spherical coordinate`, CACR 2012-02 | Shi, Kirby and Tehranirad (2012 b)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-185 | 참고문헌 — Shi et al. (2011) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.76: Shi et al. (2011), `FUNWAVE-TVD, Version 1.0, users’ manual and benchmark tests`, CACR 2011-04 | Shi et al. (2011)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-186 | 참고문헌 — Shi et al. (2001) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.76: Shi et al. (2001), `A fully nonlinear Boussinesq model in generalized curvilinear coordinates`, Coastal Engineering 42, 337–358 | Shi et al. (2001)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-187 | 참고문헌 — Shiach and Mingham (2009) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.76: Shiach and Mingham (2009), `A temporally second-order accurate Godunov-type scheme for solving the extended Boussinesq equations`, Coastal Engineering 56, 32–45 | Shiach and Mingham (2009)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-188 | 참고문헌 — Sitanggang and Lynett (2005) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.76: Sitanggang and Lynett (2005), `Parallel computation of a highly nonlinear Boussinesq equation model through domain decomposition`, Int. J. Num. Meth. Fluids 49, 57–74 | Sitanggang and Lynett (2005)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-189 | 참고문헌 — Smagorinsky (1963) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.76: Smagorinsky (1963), `General circulation experiments with the primitive equations. I. The basic experiment`, Mon. Weather Rev. 91, 99–165 | Smagorinsky (1963)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-190 | 참고문헌 — Swigler and Lynett (2011) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.76: Swigler and Lynett (2011), `Laboratory study of the three-dimensional turbulence and kinematic properties associated with a solitary wave traveling over an alongshore-variable, shallow shelf`, `in review` | Swigler and Lynett (2011)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-191 | 참고문헌 — Synolakis et al. (2007) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.76: Synolakis et al. (2007), `Standards, criteria, and procedures for NOAA evaluation of tsunami numerical models`, NOAA Tech. Memo. OAR PMEL-135 | Synolakis et al. (2007)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-192 | 참고문헌 — Tehranirad et al. (2011) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.76: Tehranirad et al. (2011), `Tsunami benchmark results for fully nonlinear Boussinesq wave model FUNWAVE-TVD, Version 1.0`, CACR-11-02 | Tehranirad et al. (2011)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-193 | 참고문헌 — Tehranirad et al. (2013) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.76: Tehranirad et al. (2013), `Tsunami benchmark results for fully nonlinear Boussinesq wave model FUNWAVE-TVD, Version 2.1`, CACR-13-10 | Tehranirad et al. (2013)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-194 | 참고문헌 — Tehranirad, Shi and Kirby (2012 b) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.76: Tehranirad, Shi and Kirby (2012 b), `Tsunami benchmark results for spherical coordinate`, CACR 2013-10 | Tehranirad, Shi and Kirby (2012 b)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-195 | 참고문헌 — Ting and Kirby (1994) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.76: Ting and Kirby (1994), `Observation of undertow and turbulence in a laboratory surf zone`, Coast. Eng. 24, `5180` | Ting and Kirby (1994)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-196 | 참고문헌 — Tonelli and Petti (2009) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.76: Tonelli and Petti (2009), `Hybrid finite volume - finite difference scheme for 2DH improved Boussinesq equations`, Coast. Engrng. 56, 609–620 | Tonelli and Petti (2009)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-197 | 참고문헌 — Tonelli and Petti (2010) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.77: Tonelli and Petti (2010), `Finite volume scheme for the solution of 2D extended Boussinesq equations in the surf zone`, Ocean Engrg. 37, 567–582 | Tonelli and Petti (2010)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. [10-18 결론 검증 정정] |
| FV2-198 | 참고문헌 — Toro (2009) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.77: Toro (2009), `Riemann solvers and numerical methods for fluid dynamics: a practical introduction`, Third edition, Springer, New York | Toro (2009)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-199 | 참고문헌 — Wei et al. (1995) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.77: Wei et al. (1995), `A fully nonlinear Boussinesq model for surface waves: Part I. Highly nonlinear unsteady waves`, Journal of Fluid Mechanics 294, `7192` | Wei et al. (1995)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-200 | 참고문헌 — Wei and Kirby (1995) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.77: Wei and Kirby (1995), `A time-dependent numerical code for extended Boussinesq equations`, Journal of Waterway, Port, Coastal and Ocean Engineering 120, 251–261 | Wei and Kirby (1995)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-201 | 참고문헌 — Yamamoto and Daiguji (1993) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.77: Yamamoto and Daiguji (1993), `Higher-order-accurate upwind schemes for solving the compressible Euler and NavierStokes equations`, Computers and Fluids 22 (2/3), `529270` | Yamamoto and Daiguji (1993)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. [10-18 결론 검증 정정] |
| FV2-202 | 참고문헌 — Yamamoto, Kano and Daiguji (1998) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.77: Yamamoto, Kano and Daiguji (1998), `An efficient CFD approach for simulating unsteady hypersonic shockshock interference flows`, Computers and Fluids 27 (56), 571–580 | Yamamoto, Kano and Daiguji (1998)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-203 | 참고문헌 — Zelt (1991) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.77: Zelt (1991), `The runup of nonbreaking and breaking solitary waves`, Coastal Engineering 15, 205–246 | Zelt (1991)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-204 | 참고문헌 — Zhen (2004) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.77: Zhen (2004), `On the numerical properties of staggered vs. non-staggered grid schemes for a Boussinesq equation model`, MCE Thesis, University of Delaware | Zhen (2004)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-205 | 참고문헌 — Zhou et al. (2001) | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.77: Zhou et al. (2001), `The surface gradient method for the treatment of source terms in the shallow-water equations`, Journal of Computational Physics 168, 1–25 | Zhou et al. (2001)의 서지 정보다. 논문 식·계수의 코드 검증 근거로 쓰지 않는다. |
| FV2-260 | 3.0 해빈의 Time_ramp 생략 | C 문서 누락 | funwave_tvd_2.1_manual.pdf p.43–48 §5.1은 권파형·붕파형과 세 해상도를 설명한다. funwave_tvd_3.0.pdf p.45–47 §5.1은 권파형 한 해상도에서 shock-capturing과 eddy-viscosity를 비교한다. 3.0은 `Xslp = 30.0`, `Mglob = 2000`, `AMP_WK = 0.018`, `Delta_WK = 0.5`, `DIRECT_SPONGE = T`, `Sponge_west_width = 12.0`, `R_sponge = 0.85`, `HIGH_ORDER = THIRD`로 바꾼다. 3.0은 2.1의 `Time_ramp = 1.0` 줄을 싣지 않는다. 3.0은 `RESULT_FOLDER = your output folder`, `VISCOSITY_BREAKING = F ! switch to T for the other case`, `Cbrk1 = 0.65`, `Cbrk2 = 0.15`, `WAVEMAKER_Cbrk = 0.65`, `Friction_Matrix=F`, `Cd_file= cd.txt`, `NumberStations = 119`, `STATIONS_FILE = gauge.txt`를 추가한다. 진폭 주석은 `this value is smaller than the report of Hansen and Svendsen, but matches the measured data`다. C는 3.0 p.45–46 발췌의 Time_ramp 생략에 한정한다. 3.0 p.37은 이 키를 WK_REG의 필요 입력으로 적는다. `src/io.F:1517–1519`는 누락 시 0을 넣고 `src/sources.F:109–110`은 그 값을 분모에 사용한다. | 3.0 해빈은 사례 설정과 비교할 쇄파 방식을 바꿨다. 현재 코드와 대조한 차이는 Time_ramp 생략이다(FV2-321). Cbrk2 기본값 주장은 FV2-266의 B로, 마찰 키 변경은 FV2-267의 A로 구분한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-261 | 3.0 불규칙파의 입력 철자 | B 문서 오기 | funwave_tvd_2.1_manual.pdf p.45·49–53 §5.2와 funwave_tvd_3.0.pdf p.47–52 §5.2는 같은 사례다. 3.0 p.51은 `DIRECT_SPONGE = T`로 바꾼다. 3.0 p.52는 `HIGH_ORDER = THRID`로 인쇄한다. 식 (79)는 3.0 p.48에서 식 (106)이 된다. 2.1 p.45와 3.0 p.48의 파고계 수심 목록은 모두 30 cm를 포함한다. 3.0 p.49 그림 5에도 `h=30.0cm` 패널이 있다. 3.0 p.48의 수심 목록에도 `h=47, 35, 30, 25, 20, 17.5, 15, 12.5, 10, 7.5, 5, and 2.5 cm`가 있다. 30 cm 누락이라는 기존 판단을 정정한다. `src/fluxes.F:101–103`은 THRID를 기본 구성으로 보낸다. | B는 3.0 p.52의 THRID 오기에 한정한다(FV2-270). 두 문서의 파고계 수심 목록에는 모두 30 cm가 있다. 2.1 p.53의 실제 입력은 FOURTH이며, 3.0의 THRID는 현재 코드에서 기본 구성 경로로 간다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-262 | 3.0 천퇴의 완충층 입력 | 일치 | funwave_tvd_2.1_manual.pdf p.53–57 §5.3과 funwave_tvd_3.0.pdf p.52–56 §5.3은 같은 사례다. 3.0 p.55는 `SPONGE_ON = T`를 `DIRECT_SPONGE = T`로 바꾼다. 다른 키와 값은 같다. 그림 번호는 9·10에서 7·8로 바뀐다. `src/io.F:2285`는 DIRECT_SPONGE를 읽는다. `src/init.F:966–970`의 `IF(DIRECT_SPONGE)THEN`은 직접 감쇠층을 초기화한다. | 3.0 천퇴의 DIRECT_SPONGE=T는 실제 읽기와 초기화 조건에 맞는다. 2.1의 SPONGE_ON은 FV2-049·121의 D와 같다. 그 밖의 입력값은 두 문서에서 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-263 | 3.0 원뿔섬의 진폭·완충층 입력 | 일치 | funwave_tvd_2.1_manual.pdf p.57–62 §5.4는 funwave_tvd_3.0.pdf p.65–70 §5.6으로 이동한다. 2.1 p.60과 3.0 p.69의 사례 A 입력은 모두 `AMP = 0.0144`다. 3.0은 `DIRECT_SPONGE = F`, `FRICTION_SPONGE = F`, `DIFFUSION_SPONGE = F`를 명시한다. 3.0은 나머지 설정값·LAGTIME·관측점 설명을 유지한다. 그림 번호는 11–16에서 15–20으로 바뀐다. 3.0 p.65–66도 전경·정의도·배치도 캡션 아래 시계열 곡선을 싣는다. 표 1의 12개 오차 값은 같다. `src/io.F:1101·1132`는 INI_SOL의 AMP를 읽는다. `:2280–2293`은 세 완충층 스위치를 읽으며 `src/init.F:966–989`의 초기화는 각 참 조건에 따른다. | 두 판의 사례 A 진폭 0.0144 m는 INI_SOL의 AMP 입력과 맞는다. 3.0의 세 완충층 F는 각 초기화 분기를 끈다. 다른 별도 차이는 LAGTIME의 FV2-047, 관측점 설명의 FV2-131, 그림 편집의 FV2-124–126과 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-264 | 3.0 천해붕의 완충층 입력 | 일치 | funwave_tvd_2.1_manual.pdf p.62–69 §5.5는 funwave_tvd_3.0.pdf p.70–76 §5.7로 이동한다. 3.0 p.75–76은 `DIRECT_SPONGE = F`, `FRICTION_SPONGE = F`, `DIFFUSION_SPONGE = F`를 명시한다. 나머지 입력 키와 값은 같다. 3.0은 2.1의 그림 19 시간간격 곡선과 6.5초 Froude 설명을 싣지 않는다. 3.0 p.73–74의 수면·유속 그림 캡션과 실제 범례의 차이는 2.1 p.66–67과 같다. `src/io.F:2280–2293`은 세 스위치를 읽고 각각 누락 시 거짓으로 둔다. `src/init.F:966–989`은 각 참 조건에서만 완충층 초기화를 시작한다. | 3.0 천해붕의 DIRECT_SPONGE·FRICTION_SPONGE·DIFFUSION_SPONGE=F는 세 완충층을 끄는 코드 조건과 맞는다. 초기 중심의 별도 결함 후보는 FV2-136의 중간 강도 E다. 그림 캡션 충돌은 FV2-138·139의 B와 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-265 | 3.0 중첩의 사례 변경 | H 코드 대조 대상 아님 | funwave_tvd_2.1_manual.pdf p.69–73 §5.6은 funwave_tvd_3.0.pdf p.76–80 §5.8로 이동한다. Grid_A·Grid_B 입력의 키와 값은 같다. 본문의 `amplitude of 1m`도 남는다. 그림 22는 그림 25가 된다. 3.0도 COUPLING을 부모에서 끄고 자식에서 켜라고 적는다. | 3.0 중첩은 같은 입력값과 COUPLING 절차를 유지한다. 절·그림 번호를 구분해 인용한다. |
| FV2-407 | 노트의 원뿔섬 결과 카탈로그 | H 코드 대조 대상 아님 | `models/FUNWAVE/manual-notes/funwave-validation-cases.md:85`의 `funwave_tvd_2.1_manual.pdf line 2813–2817`; `입사파고 3 케이스(A/B/C), Cartesian·spherical 좌표 양쪽 실행.` 노트는 원뿔섬 사례 A·B·C와 Cartesian·spherical 결과를 목록으로 정리한다. 원문 인용 범위는 2.1 p.57–62다. 2.1 p.60과 3.0 p.69의 입력 진폭은 0.0144·0.02912·0.05792 m다. | 원뿔섬 노트의 PDF 줄 번호 인용을 2.1 p.57–62로 바꾼다. 두 좌표계 항목은 노트에 수록한 사례 목록으로 적는다. 세 입력 진폭은 원문의 사례 A·B·C와 대응한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FV2-408 | 노트의 중첩 결과 카탈로그 | B 문서 오기 | `models/FUNWAVE/manual-notes/funwave-validation-cases.md:98`의 `one-way nesting 검증`과 `메뉴얼 §5.6 nesting case 대응`; `models/FUNWAVE/manual-notes/funwave-user-manual-full.md:255`의 `나머지 예제(p.47~78)` 노트가 가리킨 중첩 예제는 2.1 p.69–73 §5.6과 3.0 p.76–80 §5.8이다. 3.0의 마지막 결과 그림은 p.80의 그림 25다. | 노트는 두 판의 중첩 예제와 결과 그림을 식별한 기록이다. 3.0 예제 목록의 끝 쪽은 p.78이 아니라 p.80이다. 본문 1 m와 입력 0.1 m의 차이는 FV2-143에 따른다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |

### 5.6 집계와 확인 범위

§2–4의 고유 행 ID는 224개다.
일치 75행은 §5의 차이 표에서 제외했다.
남은 149행은 §5.4–5.5에서 각각 한 번씩 최종 분류했다.
참고문헌 56행은 H 102행에 포함한다.
예제의 과거 결과는 모두 H다.
외부 논문의 식·계수가 있어야만 나눌 코드 차이는 이 과제에 남지 않았다.
현재 노트 파일은 변경하지 않았다.
노트 수정안은 §4에만 적었다.
모델·전처리 도구·후처리 도구는 실행하지 않았다.
이 보고서는 입력 예제를 완전한 실행 패키지로 검증한 결과가 아니다.

분류별 개수: A 5, B 12, C 25, D 3, E 2, F 0, H 102, X 0. 일치 75. 합계 224행. 열지 못한 파일: 없음.

## 전수 검증 기록 (10-18, FV2-267–FV2-408)

검증 대상은 사용자가 지정한 고유 행 ID 149개다. 각 ID의 §5 결론과 본문 표를 함께 대조했다.
검증 149행, 정정 42행, 보완 66행이다. 정정과 보완은 같은 ID에서 중복 집계한다. 분류 문자가 바뀐 행은 20개다.
코드·빌드 파일의 인용 줄과 PDF의 인용 쪽을 직접 열었다. 식·수치·그림이 판정을 좌우하는 쪽은 이미지로 대조했다.
C·B 판정은 2.1·3.0·Intro-TN·funwave_code_analysis의 전체 판독 기록과 3.0 tex 기록을 rg -i로 교차 검색했다.
[E2](FUNWAVE-git-verify-E2.md)·[AD2](FUNWAVE-git-verify-AD2.md)의 같은 ID 22개는 공개 저장소 사본의 읽기 전용 이력과 대조했다. 해당 행에는 git 이력 판정 태그를 붙였다.

분류 변경 목록:

- FV2-008: H→일치
- FV2-102: H→일치
- FV2-103: H→B
- FV2-104: H→일치
- FV2-105: H→일치
- FV2-107: H→F
- FV2-120: H→일치
- FV2-124: H→B
- FV2-125: H→B
- FV2-126: H→B
- FV2-138: H→B
- FV2-139: H→B
- FV2-260: H→C
- FV2-261: H→B
- FV2-262: H→일치
- FV2-263: H→일치
- FV2-264: H→일치
- FV2-307: C→일치
- FV2-401: C→B
- FV2-408: H→B

강도 변경은 FV2-136의 E(강함)→E(중간)이다. 분류 문자 E는 유지하므로 위 20개에 포함하지 않는다. 근거는 samples.F:542의 ghost 시작 주석이다. FV2-304는 E(강함)을 유지한다.
FV2-136에 관한 최신 판정은 수정한 본문·결론 행의 E(중간)이다. 기존 요약·§5.3의 강함 표기는 이 기록으로 정정한다. 표의 기존 위치와 관계없이 각 행의 최신 분류를 적용한다.
FV2-270은 AD2의 보조 인용을 바로잡았다. 2.1 쪽 이미지의 실제 입력은 p.53의 `HIGH_ORDER = FOURTH`다. AD2에 적힌 p.52의 THIRD와 다르며, 3.0의 THRID에 대한 B 판정은 유지한다.
FV2-131은 순번 범위 1–16과 실제 파일 생성 조건을 구분했다. io.F:3866–3875는 내부 격자에 속한 관측점만 파일을 만든다.
FV2-261의 30 cm 누락 주장은 원문과 달라 삭제했다. 3.0 p.48의 수심 목록에도 30 cm가 있다.
[외부 원문 판정](FUNWAVE-external-sources.md)의 Beta_2 공통 원인도 대조했다. 이 목록의 E 두 행은 각각 초기 중심 좌표와 SLOPE 원점 차이에서 나온다. init.F:664의 Beta_2 배수에서 나온 E 행은 이 목록에 없다.
요청한 149개 행에는 X·G가 남지 않았다. 본문 표와 §5의 같은 ID는 같은 분류다. 파일 전체의 절대 홈 경로 링크는 0개다.

## 최종 집계 (10-18, Claude가 차이 결론 절의 결론 열에서 셈)

- 차이 결론 149행: A 5, B 21, C 24, D 3, E 2, F 1, H 84, 일치 9. G·X 0. 이 집계가 앞의 분류별 개수 줄보다 우선한다.
