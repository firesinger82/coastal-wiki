# Claude Sonnet 적대적 검토 3

## 검토 결과 (승인 아님)

### 1. 핵심 정정 주장 — 독립 재현으로 지지됨

MSI `!_Columns` 스키마를 직접 디코드해 `!File` 테이블(60행, row_width=18바이트)을 재구성한 결과, extractor 코드를 신뢰하지 않고도 동일한 결론에 도달했습니다.

- `_1BE96E15F472462586C19E8C77FF7927` → `mpich2nemesisp.dll` (size 2089984, seq 6)
- `_7D9F6BC68D3B438D9D6834EF34F3754F` → `mpich2mpi.dll` (size 230912, seq 36)

캐비닛 멤버 해시도 `/tmp/xbeach-mpich-identity/`의 기추출 파일과 재계산 SHA-256이 일치했고, `cxx.lib`는 저장소 원본과 바이트 단위 동일(`6fd6a3e6...`)함을 재확인했습니다. **README와 extraction-record.json의 identity 정정은 정확합니다.**

### 2. mpich2mpi.dll 실제 디스패치 경로 — 독립 objdump로 확인

`objdump -p`로 EAT를 직접 열거해 `MPI_Comm_dup`(인덱스 60→RVA 0x97a0), `PMPI_Comm_dup`(인덱스359→RVA 0x10f30)을 확인했고, 두 함수 모두 동일한 구조의 지연-바인딩 트램폴린이었습니다:

```
전역 함수포인터 슬롯(0x180037c78) 검사
  널이면: call 0x180007b30 (초기화/해석 루틴)
    반환값(eax)==0 → eax=0x10 설정 후 즉시 ret   ← 출력 포인터(RDX) 미접촉
    반환값!=0 → 슬롯 재적재
  성공 시: 원래 인자(RCX/RDX) 복원 후 jmp *rax (테일콜, 실제 백엔드로 위임)
```

이는 README의 "초기 전달 함수 설정 실패 시 출력 포인터를 쓰지 않고 0x10 반환" 주장과 정확히 일치합니다. 정적 실패 분기(초기화 실패)와, 초기화 성공 후 실제 백엔드로 위임되는 경로는 코드 구조상 명확히 분리되어 있으며, 이 분리는 README가 정확히 서술한 그대로입니다.

**추가로 독립 확인한 사실 (README에 명시되지 않았으나 중요한 근거):** `mpi.lib`를 `objdump -x`로 직접 열람하면 import descriptor가 `__IMPORT_DESCRIPTOR_mpich2mpi` 하나뿐입니다. 즉 XBeach가 링크하는 MPI 심볼은 정적으로 `mpich2mpi.dll`에서만 임포트되며, `mpich2nemesisp.dll`은 로더가 직접 바인딩하지 않습니다. 이는 "실제 로드 여부는 입증하지 않는다"는 README의 신중한 태도가 옳다는 것과 별개로, **정정된 mpich2mpi.dll이 XBeach 실행 시 프로세스 로드시점에 바인딩되는 실제 진입점 DLL**이라는, 시나리오의 개연성을 높이는 사실입니다. 이 부분은 evidence로 기록해 둘 가치가 있습니다.

### 3. 원본 XB-HARD-04 디스어셈블리 — mpich2nemesisp.dll에서 재현됨(라벨만 오류)

`mpich2nemesisp.dll`에서 `MPI_Comm_dup`/`PMPI_Comm_dup` 둘 다 RVA 0x6fb20(EAT 인덱스 58/356)로 확인했고, 그 함수를 직접 역어셈블해 원본 hard-resolutions.json이 인용한 지점을 모두 재현했습니다:
- `0x6fee0`: `movl $0x4000000,(%r12)` — 에러 경로에서 출력 포인터에 리터럴 저장 (MPI_COMM_NULL)
- `0x6fe5a`: `mov %ecx,(%r12)` — 성공 경로 핸들 저장
- `0x700c7`: `ret` — 공유 반환점

즉 원래 XB-HARD-04의 반증 근거 자체는 조작되거나 허위가 아니라, **실재하는 디스어셈블리를 잘못된 파일명으로 라벨링**한 것입니다. 정정의 스코프 진술("이는 반증을 깨지만 XBeach가 이 DLL을 로드했다는 뜻은 아니다")은 두 개의 서로 다른 코드 경로(진짜 mpich2mpi.dll의 디스패치 실패 vs. mpich2nemesisp.dll의 실제 구현부)를 혼동하지 않고 정확히 구분하고 있습니다.

### 4. XB-HARD-05 (cxx.lib NULL_COPY_FN 치환) — 독립 objdump -dr로 확인

`cxx.lib`를 직접 `objdump -dr`로 열람해 Comm/Datatype/Win 세 개의 `Create_keyval` 모두에서 relocation `?NULL_COPY_FN@...`/`?NULL_DELETE_FN@...`과 `cmp`+`cmove`(포인터 항등 비교 후 0으로 치환)를 확인했습니다. README·extraction-record.json의 주장과 일치합니다.

### 5. source-analysis 두 파일 — kh 등고선 관련 주장 검증

`generate_boundary_condition_limits_figures.m`을 직접 열어 대조한 결과:
- 주석 "Generates illustrative plots" 그대로 확인 (`:2`)
- `Hrange=[2:0.1:8]`, `Drange=[0:1:40]`, `Trange=[6:0.25:18]`, `KH=k.*DT`, `disper(...,9.81)` 모두 노트 표와 일치 (`:8-20`)
- NH 패널 kh 등고 수준 `[0.5 1 1.1 1.25 2]`(`:116`), NHplus `[0.5 1 2 3 3.5 4 5]`(`:214`) 일치

노트는 이 값들을 "kh≤1.1이면 유효"식 이분법적 검증 임계값으로 옮기지 말라고 명시적으로 경고하며, 실제 코드가 색 배열이 있는 다단계 등고선(gre→yel→ora→red)임을 정확히 반영합니다. **kh 수준이 검증된 임계값이 아니라 설명용 그림이라는 주장은 소스와 일치하며 타당합니다.** `xbeach-first-baseline-case-selection.md`는 자체적으로 kh 주장을 하지 않는 단순 색인 파일이라 별도 결함 없음.

### 발견한 실제 오류 및 최소 수정안

1. **identity-ledger.json 부재**: README.md 마지막 문장이 "검토 결론은 identity-ledger.json에 구조화했다"고 말하지만 해당 파일은 디렉터리에 없습니다(요청 시점 기준). **최소 수정**: README에서 해당 문장을 삭제하거나, 파일을 실제로 작성해 채워 넣어야 합니다. 없는 산출물을 참조하는 진술을 canonical 승인 이전에 남겨두면 향후 재검토자가 혼동합니다.

2. **README의 근거 인용 비대칭**: README는 mpich2mpi.dll 쪽 근거(RVA 0x97a0/0x10f30, 0x10 반환 분기)를 구체적 RVA 없이 산문으로만 서술합니다(extraction-record.json에는 RVA가 있으나 README 본문에는 없음). **최소 수정**: README에 "RVA 0x97a0/0x10f30, 실패 시 반환값 0x10"을 명시해 XB-HARD-04와 같은 수준의 구체성을 맞추면 재현성이 개선됩니다. (경미, 필수는 아님)

3. **범위 진술의 잠재적 과소평가 여지**: mpi.lib import descriptor가 mpich2mpi.dll 단일 대상이라는 사실(제가 독립 확인)은 "실제 로드했다는 뜻은 아니다"라는 README의 조심스러운 문구보다 시나리오 개연성이 실제로는 더 높다는 것을 시사합니다. 오류는 아니지만, 정정 correction이 완전히 최종 채택되기 전에 이 import-descriptor 사실을 evidence로 추가하면 논증이 더 강해집니다. (선택적 보강)

### 리뷰어 한계

- `call 0x180007b30`(지연 초기화/해석 루틴으로 추정) 자체의 내부는 역어셈블하지 않았습니다. LoadLibrary/GetProcAddress 패턴이라는 추정은 같은 바이너리 내 `MPI_DLL_NAME`, `mpich2%s.dll` 등 문자열의 co-location에 근거한 정황일 뿐, 직접 트레이스로 증명하지 않았습니다.
- 정적 분석만 수행했으며 PE를 실행하지 않았습니다(요청된 범위와 일치).
- File 테이블 60행 전체를 원본 `runtime-provenance.json`의 60개 멤버 목록과 1:1 대조하지는 않았고, 문제의 3개 GUID만 대조했습니다.
- `identity-ledger.json`이 존재하지 않아 그 안에 구조화되었다는 최종 결론 문서 자체는 검토하지 못했습니다.

### 결론

핵심 identity 정정(1BE96E...=nemesisp, 7D9F6BC6...=mpi)과 그로부터 도출된 스코프 진술은 모두 독립 재현으로 뒷받침됩니다. kh 등고선 관련 두 source-analysis 파일도 소스와 일치합니다. 발견된 결함은 경미(누락된 참조 파일, 인용 비대칭)하며 승인 여부는 사용자/게이트가 별도로 판단해야 합니다.
