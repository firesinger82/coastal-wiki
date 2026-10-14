# ROMS 노트 전수 대조 기록 4

- 대상 노트: `models/ROMS/source-analysis/roms_io_netcdf-differences.md`.
- 대조 범위: 새 파일의 전체 298줄. 줄 수는 대조 시작 시 원본 파일에서 집계했다. frontmatter와 빈 줄을 포함한다.
- 판정 기준: 현재 코드, 인용된 과거 코드, 저장된 위키 원문, 보고서의 최종 전수 검증 기록.
- 진행 상태: 대조 중. 노트의 전체 대조가 끝나면 완료 결과를 아래에 덧붙인다.

## roms_io_netcdf-differences.md — 완료

대상은 [models/ROMS/source-analysis/roms_io_netcdf-differences.md](../../../models/ROMS/source-analysis/roms_io_netcdf-differences.md)이다. 아래 줄 번호는 정정 후 노트의 줄 번호이다. 정정 전후 줄 수는 모두 298줄이다.

- 대조한 줄 수: 298줄. 새 파일의 전체 줄을 셌다. frontmatter와 빈 줄을 포함했다.
- 정정 수: 9줄. `[10-14 전수 검증 정정]`이 붙은 서로 다른 줄을 셌다.
- 보완 수: 1줄. `[10-14 전수 검증 보완]`이 붙은 줄을 셌다.
- 정정 항목 수: 10건. 204줄의 잘못 연결된 인용 두 건은 각각 기록했다.
- 미해결 항목: 없음.

| 대조 범위 | 줄 수 | 대조 내용 |
|---|---:|---|
| 1–21 | 21 | frontmatter의 모델·계층·작성자·날짜·검증 방법을 확인했다. 의존 노트와 관련 파일의 경로를 확인했다. |
| 22–32 | 11 | 제목·부모 링크·판본 설명·표 머리말을 확인했다. manifest의 수집일과 코드 HEAD 및 버전 문자열을 대조했다. |
| 33–269 | 237 | 모든 행의 분류·결론·원문 인용을 최종 보고서와 대조했다. 부정·조건·수량·단위·부호를 대조했다. |
| 270–282 | 13 | 수정안 문장 10개를 보고서 수정안과 최종 결론에 대조했다. |
| 283–298 | 16 | 결론 출처 목록의 보고서 파일과 절 링크를 확인했다. |

차이 표의 고유 행 ID 237개는 [note-job-1.tsv](../assign/note-job-1.tsv)의 배정과 일치한다. 행 ID의 누락·추가·중복은 없다. [ROMS-notes-apply-1.md](ROMS-notes-apply-1.md)의 반영 범위와도 일치한다.

분류와 결론 문장은 13개 보고서의 최종 결론 표와 일치한다. 각 보고서 끝의 전수 검증 기록을 적용했다. 표에서 센 분류는 A 37행, B 85행, C 67행, D 27행, E 5행, F 16행이다. A의 해시·날짜는 해당 git 판정과 최종 보고서에 일치한다. RT1-255의 A 판정은 testcases 보고서의 최종 정정을 따른다. RTG-061의 SGRID-0.3 추가 시점은 tools-guides 보고서의 최종 정정을 따른다.

E의 강도는 RF2-029·OMD-K030이 중간이다. RI1-0630·RI1-0983·RTG-1970의 강도는 강함이다. OMD-K030의 PIO 조건은 outputs-metadata 보고서의 최종 정정에 따라 `IF (latt.gt.0) THEN`으로 유지했다.

### 정정 목록

노트 위치의 파일명은 위 대상 노트를 뜻한다. 코드 경로는 `models/ROMS/raw/source_code/roms/` 기준이다. 위키 경로는 `models/ROMS/raw/manuals/wiki/wikitext/` 기준이다. 정정한 표 행의 결론 문장 칸 끝에 정정 태그를 붙였다. 결론의 분류와 문장은 유지했다.

| 노트:줄 | 전 → 후 | 근거 원문 |
|---|---|---|
| `roms_io_netcdf-differences.md:191` | `ROMS/Utility/set_diags.F:125` 단독 인용 → 삭제. | 125줄은 빈 줄이다. 누적 초기화 조건은 121–124줄이다. 평균 조건은 374–377줄이다. 이 조건 인용은 유지했다. 보고서 근거는 `roms-outputs-metadata-vs-code.md:4238`의 OMD-K004이다. |
| `roms_io_netcdf-differences.md:203` | `ROMS/Utility/get_state.F:556` 단독 인용 → 삭제. | 556줄은 빈 줄이다. 표준편차 헤더의 전처리 조건은 557줄이다. 모델 번호 조건은 563–566줄이다. 이 조건 인용은 유지했다. 보고서 근거는 `roms-outputs-metadata-vs-code.md:4258`의 OMD-K024이다. |
| `roms_io_netcdf-differences.md:204` | `ROMS/Utility/def_var.F:1821` 뒤의 `Vinfo(6)='nulvar'` → 잘못 연결된 중복 인용 삭제. | 실제 대입은 `ROMS/Utility/get_metadata.F:1011`의 `Vinfo(6)='nulvar'`이다. 이 직접 인용은 같은 행에 유지했다. `def_var.F:1821`은 `Vinfo(21)(1:latt)`를 전달한다. 보고서 `roms-outputs-metadata-vs-code.md:4264`는 해당 문자열을 별도의 `git log -S` 검색식으로 적는다. |
| `roms_io_netcdf-differences.md:204` | `ROMS/Utility/def_var.F:1821` 뒤의 `Vinfo(21)(1:6).ne.'nulval'` → 잘못 연결된 중복 인용 삭제. | 실제 비교는 `ROMS/Utility/def_var.F:364`의 `IF (latt.gt.0.and.(Vinfo(21)(1:6).ne.'nulval')) THEN`이다. 이 직접 인용은 같은 행에 유지했다. PIO의 1819줄은 `IF (latt.gt.0) THEN`이다. 보고서 근거는 `roms-outputs-metadata-vs-code.md:4264`의 OMD-K030이다. |
| `roms_io_netcdf-differences.md:242` | `Applications.wiki:2` 뒤의 `!  ROMS/TOMS IO NetCDF variables.` → `d2530aaa^:ROMS/External/varinfo.dat:2`로 경로·판 수정. | `Applications.wiki:2`는 빈 줄이다. `git show d2530aaa^:ROMS/External/varinfo.dat`의 2줄이 인용문과 일치한다. 보고서 `roms-testcases-vs-code.md:2933`의 RT1-255도 이 과거 판을 인용한다. |
| `roms_io_netcdf-differences.md:243` | `ROMS/Utility/read_phypar.F:6851` 뒤의 `# ifdef AVERAGES` → 잘못 연결된 중복 인용 삭제. | 실제 지시문은 `ROMS/Nonlinear/output.F:430`이다. 이 직접 인용은 같은 행에 유지했다. `read_phypar.F:6851`은 `'Write out averaged free-surface.'`를 전달한다. 보고서 근거는 `roms-testcases-vs-code.md:3230`의 RT1-672이다. |
| `roms_io_netcdf-differences.md:249` | `TIME_REF.wiki:17` 단독 인용 → 삭제. | 17줄은 빈 줄이다. `TIME_REF=-2` 설명은 16줄이다. `units` 예시는 18줄이다. 두 내용 인용은 유지했다. |
| `roms_io_netcdf-differences.md:250` | `TIME_REF.wiki:21` 단독 인용 → 삭제. | 21줄은 빈 줄이다. `TIME_REF=-1` 설명은 20줄이다. `units` 예시는 22줄이다. 두 내용 인용은 유지했다. |
| `roms_io_netcdf-differences.md:251` | `TIME_REF.wiki:25` 단독 인용 → 삭제. | 25줄은 빈 줄이다. `TIME_REF=0` 설명은 24줄이다. `units` 예시는 26줄이다. 두 내용 인용은 유지했다. |
| `roms_io_netcdf-differences.md:266` | `ROMS/Utility/get_2dfld.F:333` 뒤의 `wrk(i)=Ascl*(Afactor*wrk(i)+Aoffset)` → 잘못 연결된 중복 인용 삭제. | 실제 식은 `ROMS/Utility/nf_fread2d.F:370`과 499줄이다. 두 직접 인용은 같은 행에 유지했다. `get_2dfld.F:333`은 `Fscale(ifield,ng), Fmin, Fmax`를 전달한다. 보고서 근거는 `roms-tools-guides-vs-code.md:2287`의 RTG-1962이다. |

### 보완 목록

| 노트:줄 | 전 → 후 | 근거 원문 |
|---|---|---|
| `roms_io_netcdf-differences.md:29` | 판본 설명만 제시 → 코드 판·날짜의 보고서 링크와 현재 버전의 직접 인용 추가. 수정 전 부모 노트 인용의 범위 설명 추가. | `roms-outputs-metadata-vs-code.md:5`는 HEAD와 날짜를 기록한다. `ROMS/Modules/mod_ncparam.F:653`은 `character (len=5  )    :: version = '4.3  '`이다. 부모 노트의 수정 전 문장과 줄 번호는 각 보고서의 수정안 절에 보존돼 있다. 예시는 `roms-build-options-history-vs-code.md:3622`, `roms-outputs-metadata-vs-code.md:3496–3502`, `ROMS-callflow-da.md:3725`이다. |

부모 노트의 인용 16개는 해당 보고서가 보존한 수정 전 문장과 대조했다. 현재 부모 노트의 같은 줄 번호에는 수정 전 문장이 없으므로 인용 범위를 명시했다. 16개는 대상 노트의 부모 파일 인용 위치를 중복을 포함해 센 값이다.

### 기계 확인 후보 판정

아래 5건은 사용자가 지정한 후보 전체이다. 5건 모두 원문 위치가 잘못된 인용이었다. 위키 마크업 차이에 따른 오판은 없었다.

| 후보 | 판정 |
|---|---|
| `ROMS/Utility/def_var.F:1821`의 `Vinfo(6)='nulvar'` | 정정. 실제 위치는 `ROMS/Utility/get_metadata.F:1011`이다. 노트 204줄에서 잘못 연결된 중복 인용을 삭제했다. |
| `ROMS/Utility/def_var.F:1821`의 `Vinfo(21)(1:6).ne.'nulval'` | 정정. 실제 비교는 `ROMS/Utility/def_var.F:364`이다. 노트 204줄에서 잘못 연결된 중복 인용을 삭제했다. |
| `Applications.wiki:2`의 `!  ROMS/TOMS IO NetCDF variables.` | 정정. 위키 2줄은 빈 줄이다. 노트 242줄의 출처를 `d2530aaa^:ROMS/External/varinfo.dat:2`로 바꿨다. |
| `ROMS/Utility/read_phypar.F:6851`의 `# ifdef AVERAGES` | 정정. 실제 지시문은 `ROMS/Nonlinear/output.F:430`이다. 노트 243줄에서 잘못 연결된 중복 인용을 삭제했다. |
| `ROMS/Utility/get_2dfld.F:333`의 `wrk(i)=Ascl*(Afactor*wrk(i)+Aoffset)` | 정정. 실제 식은 `ROMS/Utility/nf_fread2d.F:370`과 499줄이다. 노트 266줄에서 잘못 연결된 중복 인용을 삭제했다. |

### 수정 후 확인

- 원문 경로·줄 인용은 2,891개이다. 수정 후 노트의 인용 위치를 중복을 포함해 셌다. 현재 코드 2,321개, 위키 246개, 과거 코드 308개, 수정 전 부모 노트 16개이다.
- 코드·위키의 직접 인용 2,851개를 원문과 대조했다. 남은 불일치는 없다. 위키 링크·굵게·span과 인용의 줄바꿈 표시는 표시 글자로 대조했다.
- 인용문 없는 코드·위키·과거 코드 위치 24개를 열어 문맥을 확인했다. 빈 줄만 가리키는 단독 인용은 남아 있지 않다.
- 차이 표 237행의 분류와 결론 문장은 최종 보고서와 일치한다. 본문 수정안 10개는 해당 최종 결론과 일치한다. 외부 원문 최종 판정표의 행 ID는 이 노트의 배정과 겹치지 않는다.
- 상대 Markdown 링크 39개의 파일과 절을 확인했다. frontmatter 경로 5개의 파일을 확인했다. 끊어진 링크는 없다.
- frontmatter는 YAML로 해석된다. 메모리에서 Markdown을 HTML로 변환한 표는 본문 237행이다. 각 표 행은 6열이다.
- Mermaid 블록은 0개이다. 노트에는 사용자 홈 절대 경로와 이중 대괄호 문자열이 없다. 사용자가 지정한 한계 문장은 없다.
- 정정 태그는 191·203·204·242·243·249·250·251·266줄에 있다. 보완 태그는 29줄에 있다.

최종 진행 상태: 완료. 대상 노트의 전체 298줄 대조를 마쳤다.
