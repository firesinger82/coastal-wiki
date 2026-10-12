SWAN `swanimp.pdf` 1–35쪽 전수 검증 기록.

검증일은 2026-10-13이다.
원문은 두 기록의 frontmatter `file:`이 지정한 [swanimp.pdf](../../../../../models/SWAN/raw/manuals/pdfs/swanimp.pdf)이다.
쪽 번호는 PDF의 물리 쪽 번호이다.

지정된 300 dpi 쪽 이미지를 1–35쪽까지 모두 열어 대조했다.
이미지 경로는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/swpages/swanimp-01.png`부터 `swanimp-35.png`까지이다.
각 쪽 행의 문장과 원문 전체를 대조했다.
수식·기본값·숫자·단위·명령 문법·조건·부정·불확실성·귀속·절 번호·제목을 확인했다.
아래 원문 행은 해당 이미지의 위치와 인용으로 식별했다.

| 기록 | 대조 구간 | 대조한 행 수 | 변경한 행 수 | 이상 없음 행 수 |
|---|---|---:|---:|---:|
| [p001-018.md](../manuals/pdfs/swanimp.pdf/p001-018.md) | p.1–18 | 18 | 6 | 12 |
| [p019-035.md](../manuals/pdfs/swanimp.pdf/p019-035.md) | p.19–35 | 17 | 14 | 3 |
| 합계 | p.1–35 | 35 | 20 | 15 |

이상 없음 행은 `p001-018.md`의 p.1–7, p.12–16이다.
이상 없음 행은 `p019-035.md`의 p.30–31, p.35이다.

정정·보완 수는 아래 목록의 항목 수로 집계했다.
같은 쪽의 별도 오류는 별도 항목으로 집계했다.
이상 없음 수는 수정하지 않은 쪽 행 수로 집계했다.
정정·보완 표시는 해당 쪽 행 끝에 붙였다.
두 기록의 frontmatter는 유지됐다.
두 기록의 쪽 행 수와 순서는 유지됐다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| p001-018.md:p.8 (정정) | 쪽에 없는 Introduction 제목을 Chapter 1에 붙였다. | 쪽에 인쇄된 머리말 Chapter 1만 적었다. | p.8 상단: `2` / `Chapter 1`. |
| p001-018.md:p.8 (보완) | 구현을 위한 소스 코드·추가 파일 접근 설명이 없었다. | SWAN 소스 코드와 시험용 파일 같은 추가 파일에 접근할 수 있다는 설명을 넣었다. | p.8 본문 둘째 문단: “For the purpose of implementation, you have access to the source code of SWAN and additional files, e.g. for testing SWAN.” |
| p001-018.md:p.9 (정정) | 쪽에 없는 §1.1 The material을 표시했다. | 인쇄된 머리말 Introduction과 소스 파일 목록의 연속만 적었다. | p.9 상단: `Introduction` / `3`. 본문 첫 행: `service routines : swanser.ftn`. |
| p001-018.md:p.10 (정정) | 쪽에 없는 §1.1 The material과 첫 세 파일의 분류 라벨을 적었다. | 머리말 Chapter 1을 적었다. 첫 파일명들은 분류 라벨 없이 이어진다고 적었다. | p.10 상단: `Chapter 1`. 첫 목록 행들: `SwanFindObstacles.ftn90`, `SwanCrossObstacle.ftn90`, `SwanComputeForce.ftn90`. |
| p001-018.md:p.11 (정정) | 쪽에 없는 §1.1 The material을 표시했다. | 인쇄된 머리말 Introduction을 적었다. | p.11 상단: `Introduction` / `5`. |
| p001-018.md:p.17 (정정) | 쪽에 없는 §3.2.1 Configuring the build를 표시했다. | 인쇄된 머리말 Installation을 적었다. | p.17 상단: `Installation` / `11`. 이 쪽의 절 제목은 `3.2.2 Building SWAN using GNU make`이다. |
| p001-018.md:p.17 (정정) | 직렬 실행 조건을 정상 계산과 소규모 계산으로 나눴다. 병렬화 대상의 예시를 대상 자체로 적었다. | 직렬 실행 조건을 정상적이고 규모가 작은 계산으로 적었다. 비정상·격자 중첩 계산이 큰 CPU 요구 계산의 예시임을 밝혔다. | p.17 첫 문단: “For stationary and small-scale computations, it may be sufficient to choose the serial mode”; “for relatively large CPU-demanding calculations (e.g., instationary or nesting ones)” |
| p001-018.md:p.18 (정정) | IMPORTANT NOTES에 쪽에 없는 §3.2.2 제목을 붙였다. | Chapter 3 머리말과 IMPORTANT NOTES 시작을 적었다. 본문에 인쇄된 §3.2.2 참조는 유지했다. | p.18 상단: `Chapter 3` / `IMPORTANT NOTES:`. §3.2.3 첫 문장은 `Section 3.2.2`를 참조한다. |
| p019-035.md:p.19 (정정) | 쪽에 없는 제3장 번호와 §3.2.3 제목을 표시했다. 쪽 끝의 미완성 문장을 파일 열기 문제로 규정했다. | 인쇄된 머리말 Installation을 적었다. 마지막 문장은 Windows systems have에서 이어진다고 적었다. | p.19 상단: `Installation` / `13`. 마지막 행 끝: `Windows systems have`. |
| p019-035.md:p.19 (정정) | several parts를 각 부분으로 적었다. 병렬 효율 감소의 작은 정도를 어느 정도로 적었다. | 여러 부분의 상세 시간으로 고쳤다. 병렬 효율이 소폭 낮아진다고 적었다. | p.19 -f95: “detailed timings of several parts of the SWAN calculation”. -jac: “reduces parallel efficiency to a lesser extent”. |
| p019-035.md:p.19 (보완) | 블록 Jacobi 전략의 상대적 단순성 설명이 없었다. | 원문이 해당 전략을 가장 단순한 전략으로 설명한다는 문장을 넣었다. | p.19 -jac: “The simplest strategy consists in treating the data on subdomain interfaces explicitly”. |
| p019-035.md:p.20 (정정) | 쪽에 없는 Installation·§3.2.3 제목과 -cvis 라벨을 붙였다. 첫 문장의 운영체제를 Windows로 명시했다. | 머리말 Chapter 3과 실제 소제목만 적었다. 첫 문장의 쪽 밖 귀속을 제거했다. | p.20 머리말: `Chapter 3`. 첫 행: “a well-known problem of the inability of opening a file by multiple SWAN executables.” |
| p019-035.md:p.20 (보완) | 파일 열기 문제가 잘 알려져 있다는 표현이 없었다. ANSI Fortran 90 준수와 예외의 소수 한정이 없었다. | 잘 알려진 문제라는 표현을 넣었다. 몇 가지 예외를 제외한 표준 준수 설명을 넣었다. | p.20 첫 행: “a well-known problem”. 마지막 행: “The SWAN source code complies with the ANSI Fortran 90 standard, except for a few”. |
| p019-035.md:p.21 (정정) | 쪽에 없는 제3장 번호와 §3.2.3 제목을 표시했다. 앞 쪽의 ANSI Fortran 90 표준명을 반복했다. | 머리말 Installation을 적었다. 첫 문장과 표준명은 이 쪽에 보이는 19행 제한과 ANSI 표준으로 적었다. | p.21 상단: `Installation`. 첫 두 행: “cases, where the limit of 19 continuation lines is violated”; “this violation of the ANSI standard”. |
| p019-035.md:p.21 (보완) | 컴파일·링크 명령이 앞선 예시에 대한 명령이라는 한정이 없었다. | 앞선 예시를 참조하여 제시한 명령이라고 밝혔다. | p.21 명령 앞 행: “Referring to the previous example, compilation and linking may be done as follows:”. |
| p019-035.md:p.22 (정정) | 쪽에 인쇄되지 않은 장 제목 Installation을 붙였다. | 인쇄된 머리말 Chapter 3을 적었다. | p.22 상단: `16` / `Chapter 3`. |
| p019-035.md:p.22 (보완) | netCDF 설치 상세 안내의 참조명이 없었다. | netCDF downloads 참조를 넣었다. | p.22 §3.2.6 1단계: “For details, consult netCDF downloads.” |
| p019-035.md:p.23 (정정) | 쪽에 없는 제3장 번호와 §3.2.6 제목을 표시했다. | 머리말 Installation과 인쇄된 단계 번호 2·3만 적었다. | p.23 상단: `Installation` / `17`. 단계 첫머리: `2. Define the variable NETCDFROOT`, `3. Build SWAN as usual`. |
| p019-035.md:p.24 (정정) | 쪽에 인쇄되지 않은 장 제목 Installation을 붙였다. | 인쇄된 머리말 Chapter 3을 적었다. | p.24 상단: `18` / `Chapter 3`. |
| p019-035.md:p.24 (보완) | CMake 설치 지침 참조와 Ninja의 산출물·다운로드 안내가 없었다. 두 명령이면 충분할 것이라는 표현이 없었다. | download 페이지 참조를 넣었다. Ninja의 실행 파일·라이브러리 생성과 자체 git 저장소 다운로드를 적었다. 두 명령에 관한 should suffice의 뜻을 넣었다. | p.24 §3.3: “See the download page for installation instructions”; “to create executable files and libraries from source code”; “Ninja can be downloaded from its git repository.” 3단계: “The following two CMake commands should suffice to build SWAN”. |
| p019-035.md:p.25 (정정) | 쪽에 없는 제3장 번호와 §3.3.1 제목을 표시했다. | 인쇄된 머리말 Installation과 §3.3.2 제목만 적었다. | p.25 상단: `Installation` / `19`. 절 제목: `3.3.2 Configuring the build`. |
| p019-035.md:p.25 (보완) | 설치 산출물의 디렉터리가 하위 디렉터리라는 설명이 없었다. | 설치 후 여러 하위 디렉터리가 생성된다는 문장을 넣었다. | p.25 설치 경로 예시 아래: “After installation a number of subdirectories are created.” |
| p019-035.md:p.26 (정정) | 쪽에 없는 Installation·§3.3.2 제목을 붙였다. | 머리말 Chapter 3과 인쇄된 §3.3.3 제목만 적었다. | p.26 상단: `Chapter 3`. 절 제목: `3.3.3 Clean up the build files`. |
| p019-035.md:p.26 (정정) | 경로 지정의 목적을 이렇게 해야 찾을 수 있다는 필수 조건으로 적었다. | CMake가 라이브러리를 찾을 수 있도록 하는 목적을 적었다. | p.26 netCDF 명령 아래: “so that CMake can find the libraries.” |
| p019-035.md:p.27 (정정) | 각 항목의 설명이 p.28–29에 이어진다고 단정했다. | 이 쪽에 제시된 내용이 예시라는 설명만 남겼다. | p.27 예시 앞 행: “A typical initialisation file swaninit may look like:”. 이 쪽에는 모든 항목의 후속 설명을 안내하는 문장이 없다. |
| p019-035.md:p.28 (정정) | 쪽에 없는 제4장 제목을 표시했다. | 머리말 Chapter 4와 소제목 Explanation:을 적었다. | p.28 상단: `Chapter 4` / `Explanation:`. |
| p019-035.md:p.28 (정정) | VAX를 운영체제 예시로 적었다. 첫 구분 문자의 위치를 입력 파일로 적었다. | VAX를 컴퓨터 시스템 예시로 적었다. 첫 구분 문자는 swaninit의 첫 설정 항목임을 밝혔다. | p.28 주석 문단: “on some computer system”; “(e.g., VAX systems)”. 구분 문자 문단: “the first directory separation character in swaninit, as used in the input file”. |
| p019-035.md:p.28 (보완) | 기관명 문자열의 대상 설명이 없었다. 출력 기록 파일에 종료 원인 정보가 있을 것으로 기대한다는 조건이 없었다. | 계산 수행 또는 소스 수정 기관의 이름이라는 설명을 넣었다. 화면 출력이 유용한 상황의 기대 조건을 넣었다. | p.28 기관명 문단: “the name of the institute that may carry out the computations or modifying the source code”. 장치 번호 문단: “while information about the reason is expected to be in the print file”. |
| p019-035.md:p.29 (정정) | 쪽에 없는 제4장 번호를 제목에 붙였다. | 실제로 인쇄된 머리말 제목만 적었다. | p.29 상단: `User dependent changes and the file swaninit` / `23`. |
| p019-035.md:p.32 (정정) | 쪽 제목을 제5장 Run instructions로 적었다. MPI 실행 프로그램이 대신 필요할 수 있다는 표현을 생략했다. | 실제 머리말 Chapter 5를 적었다. mpirun 또는 mpiexec가 대신 필요할 수 있다고 적었다. | p.32 머리말: “Chapter 5”. 첫 문단: “For parallel MPI runs, the program mpirun or mpiexec may be needed instead (usually provided in an MPI distribution).” |
| p019-035.md:p.33 (정정) | 머리말에 제5장을 붙였다. 쪽 첫머리의 명령에 Windows 라벨을 붙였다. | 머리말은 Run instructions로 적었다. 이 쪽에 없는 첫 명령의 Windows 귀속을 제거했다. | p.33 머리말: “Run instructions”. 쪽 첫 행: “swanrun filename [nprocs]”. 첫 명령 앞에는 Windows 라벨이 없다. |
| p019-035.md:p.33 (보완) | 노드별 코어 수를 지정하는 용도를 생략했다. | 이 지정이 다중 코어 프로세서 등에 유용하다는 설명을 추가했다. | p.33 machinefile 문단: “This is useful e.g., for multi-core processors.” |
| p019-035.md:p.34 (정정) | 쪽에 없는 Run instructions 제목을 붙였다. self-contained input file을 자체 입력 파일로 적었다. | 실제 머리말 Chapter 5를 적었다. hcat.nml이 자체적으로 완결된 입력 파일이라는 뜻을 명시했다. | p.34 머리말: “Chapter 5”. 끝 문단: “A self-contained input file hcat.nml is provided in the SWAN package.” |

정정 24, 보완 9, 이상 없음 15
