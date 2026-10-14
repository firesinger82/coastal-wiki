---
file: models/SWASH/raw/source_code/swash/Makefile
lines: 41
sha256: ed2f05e688e4dfe8f42cdbfe466f90ed37c93f2a92e065f15f5a547c84fe13ac
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# Makefile — 판독 구간 기록

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | 머리말은 SWASH 구성·빌드·설치용 Makefile이라고 적는다(1). 특별 타깃 선언은 `.PHONY: allclean build clobber config help install uninstall` (3)과 `.SILENT:` (4)이다. 선언은 나열한 타깃을 가상 타깃(phony target)으로 지정하고 명령 표시를 억제한다(3–4). 빈 줄을 포함한다(2·5). |
| 6–16 | 기본 구성 플래그는 `CMAKE_FLAGS = -G Ninja` (6)이다. 조건 `ifneq ($(fc),)` (7)이 참이면 `    CMAKE_FLAGS += -DCMAKE_Fortran_COMPILER=$(fc)` (8)로 컴파일러 플래그를 추가하고 `endif`로 닫는다(9). 조건 `ifneq ($(prefix),)` (10)이 참이면 `    CMAKE_FLAGS += -DCMAKE_INSTALL_PREFIX=$(prefix)` (11)로 설치 경로 플래그를 추가하고 `endif`로 닫는다(12). 조건 `ifneq ($(mpi),)` (13)이 참이면 `    CMAKE_FLAGS += -DMPI=$(mpi)` (14)로 MPI 플래그를 추가하고 `endif`로 닫는다(15). 각 조건은 해당 make 변수의 값이 빈 문자열과 다른지를 검사한다(7·10·13). 빈 줄을 포함한다(16). |
| 17–26 | `build:`의 실행 명령은 `	cmake --build build` (18)이다(17). `help:`는 구성·기본 빌드·설치·정리·제거 명령을 출력한다(20). 출력 명령은 `	@echo "make config    - configures the SWASH build"` (21), `	@echo "make           - builds the SWASH software"` (22), `	@echo "make install   - installs the SWASH package"` (23), `	@echo "make clobber   - removes the build files"` (24), `	@echo "make uninstall - uninstalls the SWASH package"` (25)이다. 빈 줄을 포함한다(19·26). |
| 27–35 | `allclean:`은 `	cmake -P clobber.cmake` (28)을 실행한다(27). `clobber:`도 `	cmake -P clobber.cmake` (31)을 실행한다(30). 구성 타깃 선언은 `config: clobber` (33)이다. 이 선언은 `clobber`를 선행 조건으로 둔다(33). 구성 실행 명령은 `	mkdir build` (34)와 `	cd build && cmake $(CURDIR) $(CMAKE_FLAGS)` (35)이다. 두 번째 명령은 `build`로 이동한 뒤 make의 현재 작업 디렉터리 `$(CURDIR)`와 `$(CMAKE_FLAGS)`를 CMake에 전달한다(35). 빈 줄을 포함한다(29·32). [10-15 전수 검증 정정] |
| 36–41 | 빈 줄 뒤 `install:` 타깃은 `	cmake --install build` (38)을 실행한다(36–37). `uninstall:` 타깃은 `	cat build/install_manifest.txt \| xargs rm -vf` (41)을 실행한다(40). 제거 명령은 `build/install_manifest.txt`의 내용을 파이프(pipe)로 `xargs rm -vf`에 전달한다(41). 타깃 사이 빈 줄을 포함한다(39). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6: 기본 `CMAKE_FLAGS`의 생성기(generator)는 `-G Ninja`로 고정되어 있다.
- 17–18·33–38: `config`는 `clobber`를 선행 조건으로 둔다. `build`와 `install`의 타깃 선언에는 `config` 선행 조건이 없다.
