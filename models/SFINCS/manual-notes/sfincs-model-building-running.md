---
title: "SFINCS 모델 구축·실행 환경 — 공식 readthedocs RST 발췌 (example.rst)"
model: SFINCS
doc: "docs/example.rst (readthedocs source) — 'Setting up models' / 'Executable' / 'Compiling yourself' / 'Running SFINCS'"
canonical_source: manual
citation_status: verified
verification_method: >
  /home/firesinger/coastal-wiki/models/SFINCS/raw/source_code/sfincs/docs/example.rst
  1개 RST 파일을 직접 Read (195 lines). 인용한 모든 section heading·도구명·URL·명령·DOI는
  작성 전 해당 RST 본문에서 직접 확인. RST 는 page 가 없으므로 section heading 으로 인용.
  라이브 매핑: docs/example.rst → https://sfincs.readthedocs.io/en/latest/example.html.
  범위 결정(검증된 관찰): 같은 docs/ 의 singularity.rst(519 lines)는 Deltares **사내** 빌드/배포
  문서(내부 클러스터 v-hydrax001·TeamCity·개인 계정 willem@deltares-test 다수)로,
  Diátaxis how-to·내부 운영 성격이라 canonical 재사용가치가 낮아 **의도적으로 미추출**(CLAUDE.md #8).
  singularity 의 사용자 대상 run 명령은 본 노트 §4 에 example.rst 근거로 이미 포함.
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-03
related:
  - "[[sfincs-parameters-io-reference]]"
  - "[[sfincs-numerical-implementation]]"
  - models/SFINCS/manual-notes/sfincs-v2.4.0-galibier-changelog-known-issues.md
  - "[[../source-analysis/sfincs_io_data]]"
---

# SFINCS 모델 구축·실행 환경 (공식 문서)

공식 readthedocs `docs/example.rst`("Setting up models") 발췌·정리. **입력파일을 무엇으로 만들고**(전처리 도구), **실행파일을 어디서 얻고/직접 빌드하고**, **어떤 플랫폼에서 돌리는지**를 다룬다. 입력파일 *포맷* 자체는 [[sfincs-parameters-io-reference]], 수치이론은 [[sfincs-numerical-implementation]] 참조.

> 이 문서는 how-to(실행 절차)와 reference(도구·URL) 가 섞인 벤더 공식 매뉴얼이다. 아래는 **공식 문서가 단언한 사실**(도구명·권장·URL·명령)만 인용한다. 개인 실행결과·calibration·특정 프로젝트 운영지침은 포함하지 않는다(CLAUDE.md #8, 위키=공급원).

---

## 1. 모델 구축 도구 (`§Introduction`, `§HydroMT-SFINCS`, `§Delft Dashboard`)

`docs/example.rst §Introduction` 의 핵심 단언(verbatim 요지):
- SFINCS 입력은 **단순 ascii 텍스트 및/또는 바이너리 파일**이며, 사용자가 편한 아무 플랫폼에서 생성 가능. 모델 자체는 Fortran 이지만 **입력 생성은 텍스트 에디터·Matlab·Python 무엇이든 무방**.
- 기본 모델 구축을 쉽게 하기 위해 여러 오픈소스 옵션 제공:

| 도구 | 성격 | 문서가 명시한 상태 (verbatim) |
|---|---|---|
| **HydroMT** + 플러그인 **`hydromt_sfincs`** | Python 스크립트 프레임워크 | **"highly recommended to use since 2023"** |
| **Delft Dashboard** (Matlab DDB GUI) | 대화형 GUI | "currently **depricated**" (원문 오타 그대로) |
| **Delft Dashboard Python** | 대화형 GUI | "currently being developed" |
| **Open Earth Toolbox** (Matlab OET scripts) | Matlab 스크립트 툴박스 | "currently **depricated**" |

출처: `docs/example.rst §Introduction`.

### 1.1 HydroMT-SFINCS (`§HydroMT-SFINCS`)

- HydroMT: **Eilander et al. 2022** (<https://doi.org/10.5194/egusphere-2022-149>), Python 기반 command-line 대안.
- 전역 가용 DEM 외에, **landuse 맵 기반으로 공간변화 infiltration·manning roughness** 도 취득. **강 burn-in**, 수문모델 **Wflow 과 offline coupled** 구성(하천 discharge 경계 제공) 가능.
- ⭐ **HydroMT-SFINCS v2.0.0 이후 component 기반 아키텍처** (문서 NOTE verbatim): 구 `setup_*` 메서드(`setup_grid`, `setup_dep`)가 **component 메서드**(`sf.grid.create()`, `sf.elevation.create()`)로 **대체**됨. migration guide 참조.
- 링크: 플러그인 <https://deltares.github.io/hydromt_sfincs/> · HydroMT 일반 <https://deltares.github.io/hydromt/>.

출처: `docs/example.rst §HydroMT-SFINCS` (Eilander 2022 DOI·v2.0 component API NOTE 모두 본문에서 직접 확인).

> **코드 대응**: SFINCS 솔버 측 입력파일 소비·BMI 인터페이스는 [[../source-analysis/sfincs_io_data]]. HydroMT 이 생성하는 파일들(`sfincs.inp`·`.msk`·`.ind`·`.dep`·subgrid `.nc` 등)의 *포맷* 은 [[sfincs-parameters-io-reference]] §입력파일. (전처리 도구 HydroMT 자체 API 는 별도 저장소이며 위키 SFINCS 모델 canonical 범위 밖 — 여기서는 공식 example.rst 가 SFINCS 매뉴얼로 단언한 사실만 인용.)

### 1.2 Delft Dashboard (`§Delft Dashboard`)

- **Van Ormondt et al. 2020** (<https://doi.org/10.2166/hydro.2020.092>). 수리동역학 모델 quick set-up GUI, SFINCS 구축 포함. Matlab 또는 standalone exe 로 실행, 전역 DEM 으로 대화형 기본모델 구축. 진행 중 작업으로 **Python 기반 GUI 로 전환** 중.

출처: `docs/example.rst §Delft Dashboard`.

---

## 2. 실행파일 배포 (`§Executable`)

공식 사전컴파일 배포 2경로:

| 플랫폼 | 경로 |
|---|---|
| Windows | <https://download.deltares.nl/en/sfincs> |
| 플랫폼 독립 (Windows/linux/singularity/HPC) | Docker: <https://hub.docker.com/r/deltares/sfincs-cpu> |

출처: `docs/example.rst §Executable`.

> 배포 exe 라이선스는 Deltares Freeware, 소스는 GPL-3.0 (모델 identity 는 [README](../README.md)·[manifest](../manifest.md)). v2.4.0 Galibier 의 정확한 배포/provenance 는 [changelog·known-issues 노트](sfincs-v2.4.0-galibier-changelog-known-issues.md) 및 [manifest](../manifest.md).

---

## 3. 직접 컴파일 (`§Compiling yourself`)

문서가 명시한 **공식 tested·free 조합** (verbatim):
- **Visual Studio Community 2022** — <https://visualstudio.microsoft.com/vs/community/>
- **Intel Fortran Compiler Classic + Intel Fortran Compiler for Windows 2022.1.0** — <https://www.intel.com/content/www/us/en/developer/articles/tool/oneapi-standalone-components.html>
- 체크아웃 후 VS 솔루션 파일: <https://github.com/Deltares/SFINCS/blob/main/source/sfincs.sln>
- GPL-3.0 하에 개선은 GitHub pull request 로 공유 권장.

출처: `docs/example.rst §Compiling yourself`.

> **provenance 대응**: 위키가 실제로 v2.4.0 Galibier 소스를 VS2022+Intel oneAPI 로 빌드해 `diff=0` 확정한 기록은 [manifest §docs](../manifest.md) (Windows 빌드 노하우 자체는 위키 canonical 아님 — Claude 메모리 참조, manifest 규약). 공식 문서의 권장 조합과 위키 실증 조합이 정합.

---

## 4. 실행 방법 (`§Running SFINCS`)

문서: SFINCS 는 local·HPC·cloud 다중 플랫폼에서 실행 가능. 가장 단순한 방식은 Windows batch-file.

### 4.1 Windows 표준 (`§On windows (standard)`)
- batch 파일을 **입력파일이 있는 폴더에 복사**, exe 를 호출하고 일반 출력 텍스트를 `sfincs_log.txt` 로 리다이렉트.

```text
:: run.bat
call "<exe_folder>\sfincs.exe">sfincs_log.txt
```
출처: `docs/example.rst §On windows (standard)` code-block. 원문은 exe 폴더 자리에 `<drive>:\..\folder_where_exe_is_located` 형태의 **placeholder**(실경로 아님)를 쓰며, 본 노트는 그 자리만 `<exe_folder>` 로 치환하고 나머지(`call "..."<sfincs.exe">sfincs_log.txt`)는 verbatim.

### 4.2 Linux (`§On linux`)
- HPC(Linux)에서는 일반적으로 **Docker 또는 Singularity 실행이 가장 범용·안정**. 전용 Linux 빌드가 필요하면 Deltares 에 요청(자체 클러스터 경험 있음).

### 4.3 Docker (`§Using Docker`)
- 항상 최신 빌드를 Windows/Mac/Linux/cloud 에서 쓰는 편의 방식. Docker Desktop(<https://www.docker.com/products/docker-desktop>) 설치 후:

```text
docker pull deltares/sfincs-cpu
docker run -vC:/Users/../SFINCS:/data deltares/sfincs-cpu
```
- ⚠ **반드시 full path**(상대경로 불가). Linux/Mac 은 `/Users/../SFINCS/` 형식.
- 최신 자동빌드 대신 **검증된 태그 릴리스** pull 가능 (문서 예: `docker pull deltares/sfincs-cpu:sfincs-v2.0.3-Cauberg`). 태그 목록 <https://hub.docker.com/r/deltares/sfincs-cpu/tags>.

출처: `docs/example.rst §Using Docker` (code-block·경고·태그 예 verbatim).

> v2.4.0 Galibier 의 Docker 태그는 `deltares/sfincs-cpu:sfincs-v2.4.0-Galibier-Release` ([manifest §docs](../manifest.md)).

### 4.4 Singularity (`§Using Singularity`)
- Surfsara/Azure/Amazon 등 **singularity 지원 cloud 클러스터**에서 Docker 컨테이너를 직접 실행. 반복 실행 시 한 번 pull 해 이미지로 저장 후 재사용 권장(매번 컨테이너 로딩 방지).

```text
:: 즉시 pull & run
singularity run -B$(pwd):/data --nv docker://deltares/sfincs-cpu

:: 먼저 이미지 생성 후 실행
singularity pull docker://deltares/sfincs-cpu sfincs-cpu.img
singularity run -B$(pwd):/data sfincs-cpu.img
```
- 여기서도 태그 릴리스(`sfincs-v2.0.3-Cauberg` 등) 지정 가능.

출처: `docs/example.rst §Using Singularity` (code-block verbatim).

---

## 5. 지원·기여 (`§Courses`, `§Questions and support`, `§Contributing`)

문서가 명시한 사실(요지만):
- **교육**: DSD(Deltares Software Days) 연례 SFINCS 트레이닝(<https://softwaredays.deltares.nl/welcome>), 미/캐 대상 Deltares USA 온라인(<https://www.deltares-usa.us/book-online>).
- **지원**: 무료 제공 모델이라 지원 한계 명시. 구조적 문의는 Software Service Package, 문의 `software@deltares.nl` / 협업 `sfincs@deltares.nl`.
- **기여**: 문서 소스 <https://github.com/Deltares/SFINCS/docs>, **코드는 2022-11-16 오픈소스화**(GPL-3.0), 개선은 GitHub PR.

출처: `docs/example.rst §Courses learning SFINCS`, `§Questions and support`, `§Contributing`.

> 코드 오픈소스화 날짜(2022-11-16)는 [[sfincs-numerical-implementation]] §5 의 v2.0.0 Alpe d'Huez(2022-11-16 오픈소스화)와 정합.

---

## 6. 검증 메모

- 인용한 모든 section heading·도구명·DOI·URL·명령은 `docs/example.rst` 직접 Read(195줄)로 확인.
- 원문 오타("depricated", "cmpiled", "unnesissarily", "becuase")는 인용 시 verbatim 표기하거나 [원문] 주석 — 사실 왜곡 아님.
- **범위 결정**: `docs/singularity.rst`(519줄)는 Deltares 사내 클러스터 빌드 자동화 문서(내부 호스트·TeamCity·개인 계정)로 canonical 미추출(§frontmatter verification_method). `numerical_implementation.rst`·`validation.rst` 는 **여전히 heading-only skeleton**(WIP)이라 추출 대상 없음([[sfincs-numerical-implementation]] §문서 상태 경고에서 이미 기록). → 이로써 `docs/*.rst` 중 **사용자 대상 실질 내용이 있는 RST 는 전부 manual-notes 커버**(overview·developments·numerical_implementation·input·input_forcing·input_structures·parameters·output·waves·example).

## 7. readthedocs 라이브 사이트

- example → <https://sfincs.readthedocs.io/en/latest/example.html>

→ 로컬 RST(`raw/source_code/sfincs/docs/example.rst`, 버전 고정·재현)를 1차, readthedocs URL 을 라이브 참조로 병기. 둘은 동일 repo `docs/` 빌드라 동치.
