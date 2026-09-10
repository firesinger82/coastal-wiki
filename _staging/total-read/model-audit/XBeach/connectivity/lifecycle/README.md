# XBeach 생명주기·상태·인터페이스 연결 원장

이 디렉터리는 `models/XBeach/raw/source_code/trunk`의 **생명주기 범위**만 다룬다. XBeach 전체 모델 분석 완료를 뜻하지 않는다. 현재 소스 연결은 원문과 빌드 명세로 검증했지만, 상위 전체자료 판독 게이트가 닫혀 있으므로 `edges.json`은 최종 확정이 아닌 `source_verified_candidate_pending_parent_full_read_gate` 상태다.

## 확인된 실행 흐름

독립 실행 파일은 `readinput()` 뒤 `init()`을 호출하고, `t < tstop` 동안 `executestep()` → 현재 시간 재조회 → `outputext()`를 반복한 다음 `final()`을 호출한다. `init()`은 입력·격자·시간·hotstart·물리 모듈·MPI 분배·출력을 순서대로 구성한다. `executestep()`은 wet-cell 계산과 시간 선택을 먼저 하고 출력 시각을 갱신한 뒤, 오류가 없을 때 경계조건·파랑·흐름·표사·지형 갱신을 실행한다.

MPI 빌드에서는 세계 rank 0이 출력 전용 `xomaster`, 세계 rank 1이 계산 master다. 출력 rank는 최초 `output()` 호출 안의 영속 루프에 머물다가 계산 rank의 `final()` 신호를 받아 같은 루프 안에서 `MPI_Finalize`와 `stop`을 수행한다. 계산 rank는 로그를 닫고 별도로 `MPI_Finalize`를 호출한다. 직렬 분기에서는 `xmaster`, `xomaster`, `xcompute`가 모두 참인 상수다.

Autotools의 독립 실행 대상은 `src/xbeach/xbeach.F90`을 `libxbeach.la`에 연결한다. 현재 라이브러리 명세는 `xbeach_bmi.f90`, `xmpi.F90`, `general_mpi.F90`을 포함한다. `libxbeach_dynamic.F90`은 별도 Visual Fortran dynamic 프로젝트에서만 확인된다. `xmpinew.F90`, `general_mpi_new.F90`, 네 `wave_boundary_*` 파일은 확인한 현재 빌드 명세에 포함되지 않아 legacy/prototype 후보로 분리했다. 특히 `wave_boundary_init.f90`은 한 줄의 빈 파일이다.

`edges.json`에는 호출·빌드 연결 53개와 정의 앵커 31개가 있다. 각 연결은 1-based 물리 LF 행, 해당 행의 정확한 원문, 소스 SHA-256, 조건부 컴파일·실행 guard, 상태 생산/소비 설명을 포함한다.

## 중요한 상태 계약

`state-contracts.json`의 12개 검사는 다음 사실을 고정한다.

- 코어 상태는 Fortran 모듈의 `save` 변수에 저장되는 프로세스 전역 단일 인스턴스다. 추적한 진입점에는 재초기화 guard나 상태 deallocate/reset 절차가 없다.
- BMI `initialize(configfile)`는 문자열을 변환하지만 사용하지 않고, 코어는 현재 작업 디렉터리의 `params.txt`를 읽는다.
- `par%hotstart`는 기본값 `-123`인 상태에서 `depfile` 필요 여부를 먼저 결정하고, 뒤에서야 `params.txt`에서 읽힌다. 이 순서에서는 일반적인 `setbathy != 1` hotstart도 depfile 요구를 피하지 못한다.
- `hotstart_init_1`이 읽은 `uu`·`vv`는 뒤의 `flow_init`에서 0으로 덮이고, `hotstart_init_2`는 이를 다시 읽지 않는다.
- `timestep_init`은 hotstart 전에 시간을 0으로 만든다. hotstart가 시간 원점을 0으로 재기준화하려는 설계인지, 저장 시간을 복원해야 하는지는 소스만으로 확정하지 않았다.
- `executestep()`은 저장 오류가 0이 아니면 물리 계산을 건너뛰어도 카운터를 증가시키고 0을 반환한다. `outputext()`는 오류 0과 1에만 반환값을 대입한다.
- BMI `update()`는 `executestep()` 반환값을 뒤의 `outputext()` 반환값으로 덮는다. BMI `get_time_step()`은 단순 조회가 아니라 `compute_dt()`를 호출해 `par%dt`를 바꾸고 MPI collective 경로를 탈 수 있다.
- USEMPI 라이브러리는 host의 MPI 상태를 확인하지 않고 `MPI_Init`/`MPI_Finalize`를 직접 소유한다.
- 0 step에서 `final()`을 호출하면 로그의 `t/n`이 0으로 나뉜다. USEMPI에서는 두 번째 `executestep()` 전에 종료하면 `t01`이 대입되지 않은 채 로그 계산에 전달된다.
- Python `XBeach.finalize()`는 native `finalize()`를 호출하지 않고 공유 라이브러리를 unload한다. 생성자가 바꾼 현재 작업 디렉터리도 복구하지 않는다.

위 항목 중 코드 대입·호출 순서에서 직접 따라오는 결과는 `static_consequence`, 설계 의도를 추가로 알아야 하는 부분은 `unresolved`로 구분했다. 실제 실행 재현이나 수정 권고를 사실처럼 섞지 않았다.

## 보충자료 판독과 판정 경계

`embedded-perl-read.json`은 Win32/x64 `jumpshot.jar`가 전체 SHA-256까지 동일하고, 누락됐던 `html/internals.pl` 206행과 `html/labels.pl` 469행도 동일 member bytes임을 기록한다. 두 파일은 LaTeX2HTML의 내부 링크·라벨 lookup 데이터를 반환하는 Perl fragment이며 XBeach 실행 진입점은 확인되지 않았다.

`parallel-report-read.json`은 동일 SHA-256의 두 `Parallellization_report.pdf` 사본 14페이지를 모두 렌더링해 시각 판독한 기록이다. 2008년 보고서의 단일 master 입출력 설명은 현재 소스의 출력 전용 rank 분리보다 오래된 설계다. 현재 연결 판정에는 체크한 소스와 빌드 명세를 우선했고, 보고서는 역사적 배경으로만 사용했다. 모든 페이지를 읽었지만 성능 그래프의 개별 좌표는 수치화하지 않았다.

## 산출물

- `edges.json`: 호출자/피호출자, 정확한 행·인용·SHA, guard, 상태 흐름을 가진 기계 판독 연결 원장
- `state-contracts.json`: 핵심 상태 계약, 정적 결과, 미해결 의미론을 분리한 원장
- `embedded-perl-read.json`: JAR 내부 Perl 2개 전량 판독·동일성 증거
- `parallel-report-read.json`: 병렬화 PDF 14페이지 전량 시각 판독·사본 동일성 증거

검증 시점에는 네 JSON의 문법, `edges.json`의 53개 인용과 31개 정의 앵커, `state-contracts.json`의 29개 인용, 기록된 소스 SHA가 모두 현재 원문과 일치했다. 상위 전체자료 판독 게이트가 열린 뒤에만 이 후보 상태를 최종 연결 판정으로 승격할 수 있다.
