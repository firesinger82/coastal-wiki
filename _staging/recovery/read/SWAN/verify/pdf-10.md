# SWAN PDF 전수 검증 — pdf-10

검증일은 2026-10-13이다.
원문은 두 기록의 `file:`에 지정된 `models/SWAN/raw/manuals/pdfs/swanuse.pdf`이다.
PDF 91–126쪽의 각 300dpi 이미지를 직접 열어 대상 쪽 행 전체와 대조했다.
이미지 경로는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/swpages/swanuse-NNN.png`이다.
`NNN`은 세 자리 PDF 쪽 번호이다.
추출 텍스트는 p.105의 명령 키워드 대소문자를 판독할 때만 보조로 사용했다.
판정 기준은 쪽 이미지이다.

수식의 첨자·부호·지수·분모를 확인했다.
기본값·숫자·단위와 명령 구문을 확인했다.
조건·부정·불확실성 표현의 의미를 확인했다.
해당 쪽에 없는 귀속·절 번호·제목이 들어갔는지 확인했다.
각 수정은 해당 쪽 행에 반영했다.
frontmatter와 쪽 행 밖의 내용은 유지했다.

집계 단위는 기록의 PDF 쪽 행이다.
한 쪽 행에서 같은 유형을 여러 번 수정한 경우 해당 유형을 1건으로 집계했다.
p.109·p.118·p.119에는 정정과 보완이 함께 있다.
이 세 행은 두 유형에 각각 집계했다.

| 기록 | 대조한 쪽 행 수 | 정정 | 보완 | 이상 없음 |
|---|---:|---:|---:|---:|
| [p091-108.md](../manuals/pdfs/swanuse.pdf/p091-108.md) | 18 | 14 | 0 | 4 |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md) | 18 | 17 | 3 | 1 |
| 합계 | 36 | 31 | 3 | 5 |

이상 없음으로 집계한 행은 p.92·p.96·p.97·p.102·p.123이다.
p.123–126의 기록에 있는 수식은 이미지와 일치했다.
p.126의 Table A.1 값도 이미지와 일치했다.

아래 원문 행은 PDF 쪽 번호와 인쇄 쪽 번호로 위치를 표시했다.
해당 행의 문구를 함께 적었다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [p091-108.md](../manuals/pdfs/swanuse.pdf/p091-108.md):p.91 (정정) | ‘적용 가능한 경우에만’을 INPGRID CURRENT 참조의 조건으로 해석했다. | ‘후자’에 대한 적용 조건으로 고쳤다. INPGRID CURRENT 참조는 별도로 기록했다. | p.91(인쇄 83), 첫 괄호 행: `(the latter only if applicable; see command INPGRID CURRENT)`. |
| [p091-108.md](../manuals/pdfs/swanuse.pdf/p091-108.md):p.93 (정정) | 이 쪽에 인쇄되지 않은 ‘4.5.5 Numerics’를 붙였다. | 수치 명령 설명의 계속으로 고쳤다. 이 쪽에는 절 번호·제목이 없다고 기록했다. | p.93(인쇄 85), 본문 첫 행 `In the computation with unstructured meshes`부터 NUMeric·STOPC 설명까지. 절 번호·제목은 없다. |
| [p091-108.md](../manuals/pdfs/swanuse.pdf/p091-108.md):p.94 (정정) | 이 쪽에 인쇄되지 않은 ‘4.5.5 Numerics’를 붙였다. | 수치 명령 매개변수 설명의 계속으로 고쳤다. 이 쪽에는 절 번호·제목이 없다고 기록했다. | p.94(인쇄 86), 첫 문단 `With respect to the QC modelling`부터 SIGIMPL 설명까지. 절 번호·제목은 없다. |
| [p091-108.md](../manuals/pdfs/swanuse.pdf/p091-108.md):p.95 (정정) | 인쇄되지 않은 ‘4.5.5 Numerics’를 붙였다. 문장 중간에서 시작하는 첫 행을 SIGIMPL의 SIP 적용 조건으로 완성했다. | 절 번호·제목이 없음을 기록했다. 첫 행은 이 쪽에 인쇄된 괄호의 끝만 기록했다. | p.95(인쇄 87), 첫 행 `of currents or time varying depth).` 다음에 CTHETA 항목이 시작한다. 이 쪽 첫 행에는 SIGIMPL·SIP가 없다. |
| [p091-108.md](../manuals/pdfs/swanuse.pdf/p091-108.md):p.98 (정정) | 이 쪽에 인쇄되지 않은 ‘4.6.1 Output locations’를 붙였다. | 출력 위치 명령 설명의 계속으로 고쳤다. 이 쪽에는 절 번호·제목이 없다고 기록했다. | p.98(인쇄 90), 첫 구문 `GROUP ’sname’ SUBGrid`부터 CURve 설명까지. 절 번호·제목은 없다. |
| [p091-108.md](../manuals/pdfs/swanuse.pdf/p091-108.md):p.99 (정정) | 인쇄되지 않은 ‘4.6.1 Output locations’를 붙였다. 끝 행에 아직 없는 ‘다음 기준 직선’을 보충해 정의를 완성했다. | 절 번호·제목이 없음을 기록했다. 끝 행의 미완성 정의는 이 쪽에서 확인되는 부분까지만 기록했다. | p.99(인쇄 91), TABLE 예부터 RAY 설명까지 절 제목은 없다. 마지막 행은 `[int] number of subdivisions between the previous master ray and the`로 끝난다. |
| [p091-108.md](../manuals/pdfs/swanuse.pdf/p091-108.md):p.100 (정정) | 인쇄되지 않은 ‘4.6.1 Output locations’를 붙였다. 문장 중간에서 시작하는 첫 행에 앞쪽의 RAY·[int] 정의를 다시 붙였다. | 절 번호·제목이 없음을 기록했다. 첫 행은 후속 기준 직선과 분할 수에 관해 이 쪽에 보이는 내용만 기록했다. | p.100(인쇄 92), 첫 두 행: `following master ray defined by the following data (number of subdivisions is one more than the number of interpolated rays)`. |
| [p091-108.md](../manuals/pdfs/swanuse.pdf/p091-108.md):p.101 (정정) | 인쇄되지 않은 ‘4.6.1 Output locations’를 붙였다. BLOCK으로 생성하지 않는 대상을 위치 집합으로 적었다. | 절 번호·제목이 없음을 기록했다. BLOCK으로 생성하지 않는 대상은 후속 중첩 실행의 데이터로 고쳤다. | p.101(인쇄 93), NGRID 구문과 둘째 문단: `to generate some data for the (subsequent) nested run (not with command BLOCK because a set of locations of the type NGRID does represent an outline and not a geographic region)`. |
| [p091-108.md](../manuals/pdfs/swanuse.pdf/p091-108.md):p.103 (정정) | 이 쪽에 인쇄되지 않은 ‘4.6.2 Write or plot computed quantities’를 붙였다. | QUANTITY 설명으로 고쳤다. 이 쪽에는 절 번호·제목이 없다고 기록했다. | p.103(인쇄 95), QUANTity 구문과 출력 매개변수 설명. 절 번호·제목은 없다. |
| [p091-108.md](../manuals/pdfs/swanuse.pdf/p091-108.md):p.104 (정정) | 이 쪽에 인쇄되지 않은 ‘4.6.2 Write or plot computed quantities’를 붙였다. | 출력량 설정 설명의 계속으로 고쳤다. 이 쪽에는 절 번호·제목이 없다고 기록했다. | p.104(인쇄 96), 첫 행 `The following data are accepted only in combination with some specific output quantities.`부터 Examples까지. 절 번호·제목은 없다. |
| [p091-108.md](../manuals/pdfs/swanuse.pdf/p091-108.md):p.105 (정정) | 이 쪽에 인쇄되지 않은 ‘4.6.2 Write or plot computed quantities’를 붙였다. | QUANTITY 예의 계속으로 고쳤다. 이 쪽에는 절 번호·제목이 없다고 기록했다. | p.105(인쇄 97), QUANTITY 예부터 OUTPUT OPTIONS·BLOck 구문까지. 절 번호·제목은 없다. |
| [p091-108.md](../manuals/pdfs/swanuse.pdf/p091-108.md):p.106 (정정) | 이 쪽에 인쇄되지 않은 ‘4.6.2 Write or plot computed quantities’를 붙였다. | 출력 명령 구문의 계속으로 고쳤다. 이 쪽에는 절 번호·제목이 없다고 기록했다. | p.106(인쇄 98), RTP부터 PROPTheta 구문. 절 번호·제목은 없다. |
| [p091-108.md](../manuals/pdfs/swanuse.pdf/p091-108.md):p.107 (정정) | 이 쪽에 인쇄되지 않은 ‘4.6.2 Write or plot computed quantities’를 붙였다. | 출력 명령 구문의 계속으로 고쳤다. 이 쪽에는 절 번호·제목이 없다고 기록했다. | p.107(인쇄 99), PROPSigma부터 URMS 및 [unit]·OUTput 구문. 절 번호·제목은 없다. |
| [p091-108.md](../manuals/pdfs/swanuse.pdf/p091-108.md):p.108 (정정) | 이 쪽에 인쇄되지 않은 ‘4.6.2 Write or plot computed quantities’를 붙였다. | 출력 명령 구문의 계속으로 고쳤다. 이 쪽에는 절 번호·제목이 없다고 기록했다. | p.108(인쇄 100), TMBOT부터 PTSTEEpne 구문. 절 번호·제목은 없다. |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.109 (정정) | 쪽에 없는 제4장 번호를 붙였다. 다음 쪽의 ‘격자 유형’을 문장 끝에 미리 붙였다. | 실제 쪽 머리글만 기록했다. XML 형식 설명은 이 쪽에서 확인되는 부분까지만 기록했다. | p.109(인쇄 101), 머리글 `Description of commands`. 마지막 행은 `but SWAN will generate various XML-based file formats depending on`으로 끝난다. |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.109 (보완) | ASCII 파일의 이용 방법과 netCDF의 데이터 교환 기능을 생략했다. Paraview의 성격과 지원 운영체제를 생략했다. | ASCII의 편집·열람 방법을 추가했다. 응용 프로그램 사이의 netCDF 데이터 교환 설명을 추가했다. Paraview의 성격과 운영체제를 추가했다. | p.109(인쇄 101), 파일 형식 문단: `open and edit in any text editor`; `viewed in Matlab or Excel`; `using output from one application as input to another`; `an open-source, general-purpose visualization package, available for Windows, Mac and Linux`. |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.110 (정정) | 이 쪽에 없는 머리글 ‘Description of commands’를 붙였다. | 실제 쪽 머리글 Chapter 4를 기록했다. | p.110(인쇄 102), 머리글 `Chapter 4`. 본문은 `the grid types`로 시작한다. |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.111 (정정) | 이 쪽에 없는 제4장 번호를 붙였다. | 실제 쪽 머리글 Description of commands만 기록했다. | p.111(인쇄 103), 머리글 `Description of commands`. 본문은 TMM10 설명으로 시작한다. |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.112 (정정) | 이 쪽에 없는 머리글 ‘Description of commands’를 붙였다. | 실제 쪽 머리글 Chapter 4를 기록했다. | p.112(인쇄 104), 머리글 `Chapter 4`. 본문은 PROPXY 설명으로 시작한다. |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.113 (정정) | 쪽에 없는 제4장 번호를 붙였다. 마찰값 0 설정의 should를 강제 조건으로 적었다. at most를 ‘최대한’으로 옮겼다. | 실제 쪽 머리글만 기록했다. 마찰값 설정의 권고 강도를 보존했다. DHSIGN·DRTM01은 기껏해야 최종값과의 차이를 가늠하는 지표라는 한계를 보존했다. | p.113(인쇄 105), UBOT·URMS: `then one should use the command FRICTION with the value of the friction set to zero`. DHSIGN·DRTM01: `at most an indication of this difference`. 머리글은 `Description of commands`이다. |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.114 (정정) | 이 쪽에 없는 장 제목을 붙였다. 첫 문장에 앞쪽의 ‘풍파’를 붙였다. PARTIT의 should not을 강제 표현으로 적었다. 5 position integer를 ‘5자리 정수’로 적었다. | 실제 머리글을 기록했다. 첫 문장은 이 쪽의 ‘나머지 분할’을 기준으로 기록했다. 결합하지 않으라는 권고를 보존했다. 정수 출력의 필드 폭이 5칸임을 명시했다. | p.114(인쇄 106), 머리글 `Chapter 4`. 첫 행 `the remaining partitions are the swell`. PARTIT: `should not be combined`. [unit]: `value is written as a 5 position integer`. |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.115 (정정) | 쪽에 없는 제4장 번호를 붙였다. 쪽 첫 시간 단위에 앞쪽의 BLOCK 명령명을 붙였다. INDEXED의 should를 강제 표현으로 적었다. | 실제 쪽 머리글을 기록했다. 첫 부분은 인쇄된 시간 단위만 기록했다. TABLE 명령 두 개를 주라는 권고 강도를 보존했다. | p.115(인쇄 107), 머리글 `Description of commands`. 첫 세 행은 MIN·HR·DAY 설명이다. INDEXED: `The user should give two TABLE commands`. |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.116 (정정) | 이 쪽에 없는 머리글 ‘Description of commands’를 붙였다. | 실제 쪽 머리글 Chapter 4를 기록했다. | p.116(인쇄 108), 머리글 `Chapter 4`. 본문에는 TABLE의 OUTPUT 설명과 SPECout 구문이 있다. |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.117 (정정) | 이 쪽에 없는 제4장 번호를 붙였다. | 실제 쪽 머리글 Description of commands만 기록했다. | p.117(인쇄 109), 머리글 `Description of commands`. 본문은 SPEC2D 설명으로 시작한다. |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.118 (정정) | 이 쪽의 장 제목을 제4장 Description of commands로 적었다. 마지막 문장에 다음 쪽의 ‘제어 지속’을 미리 붙였다. | 실제로 인쇄된 쪽 머리글 Chapter 4만 적었다. 마지막 문장은 이 쪽의 A TEST command까지만 기록했다. | PDF p.118(인쇄 110) 쪽 머리글: Chapter 4. 이 쪽의 새 절 제목은 4.6.3 Write or plot intermediate results이다. 마지막 행은 A TEST command에서 끊긴다. |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.118 (보완) | NESTOUT의 선택 명령이라는 한정이 없었다. | NESTOUT은 선택 명령이라고 명시했다. | PDF p.118(인쇄 110) 첫 문단: With this optional command the user indicates that the 2D spectra along a nest boundary … |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.119 (정정) | 이 쪽에 없는 4.6.3 절 번호·제목을 붙였다. 시간 출력용 itest 설정의 should를 강제 표현으로 적었다. | 실제 머리글 Description of commands를 기록했다. itest = 1 설정의 권고 강도를 보존했다. | p.119(인쇄 111), 머리글 Description of commands. [itest]: for this [itest] should be set to 1. |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.119 (보완) | S2D 설명이 다음 쪽으로 이어진다고만 적었다. | 이 쪽 끝에 인쇄된 S2D 키워드 조건과 분산 밀도·원천항 6개를 보완했다. | p.119(인쇄 111), 마지막 행: S2D if the keyword S2D appears variance densities and 6 source terms (see end of |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.120 (정정) | 이 쪽에 없는 4.6.3 절 번호·제목을 붙였다. 쪽 첫 문장에 앞쪽의 주어와 대상을 붙였다. 마지막 문장에 다음 쪽의 ‘실행 구성’을 붙였다. 정상 MODE의 should를 강제 표현으로 적었다. | 실제 머리글 Chapter 4를 기록했다. 첫 문장과 마지막 문장은 이 쪽에 인쇄된 범위로 한정했다. COMPUTE만 지정하라는 원문의 표현에 should를 명시했다. | p.120(인쇄 112), 머리글 Chapter 4. 첫 문장은 this list of options) as computed will be printed as 2D …로 시작한다. 본문: only the command COMPUTE should be given here (no options!). 마지막 문장은 This enables the user to에서 끊긴다. |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.121 (정정) | 이 쪽에 없는 4.7 절 번호·제목을 붙였다. 첫 문장에 앞쪽의 여러 COMPUTE 사용 조건을 붙였다. and/or를 ‘거나’로만 적었다. Courant 수 기준의 should를 강제 표현으로 적었다. | 실제 머리글을 기록했다. 첫 문장은 이 쪽에 인쇄된 절로 한정했다. and/or의 동시 적용 가능성과 시간 단계 선택의 권고 강도를 보존했다. | p.121(인쇄 113), 머리글 Description of commands. 첫 문단: make a stationary computation … and/or to change the computational time step … . 본문: the time step should be chosen such that the Courant number is smaller than 10 … . |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.122 (정정) | 이 쪽에 없는 4.7 절 번호·제목을 붙였다. 이진 파일의 much faster를 ‘더 빨리’로 적었다. ABI 규약의 should를 강제 표현으로 적었다. | 실제 머리글 Chapter 4를 기록했다. ‘훨씬 더 빨리’와 should의 표현 강도를 보존했다. | p.122(인쇄 114), 머리글 Chapter 4. 이진 파일 문단: much faster than an ASCII file; your compiler and OS should follow the same ABI … conventions. |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.124 (정정) | 이 쪽에 없는 Definitions of variables 제목을 붙였다. 마지막 문장에 다음 쪽의 기본값과 조건별 관계를 붙였다. | 실제 머리글 Appendix A만 기록했다. 마지막 문장이 QUANTITY에서 다음 쪽으로 이어진다고 기록했다. | p.124(인쇄 116), 머리글 Appendix A. 마지막 행: The power p can be chosen by the user by means of the QUANTITY |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.125 (정정) | 이 쪽에 없는 Appendix A 라벨을 붙였다. MS 설명에 이 쪽에 없는 ‘다음 쪽 표’를 붙였다. | 실제 머리글 Definitions of variables만 기록했다. MS와 DSPR의 관계 설명이 다음 쪽으로 이어진다고 기록했다. | p.125(인쇄 117), 머리글 Definitions of variables. 마지막 문장: This number is related to the one-sided directional spread of the waves (DSPR) as follows: |
| [p109-126.md](../manuals/pdfs/swanuse.pdf/p109-126.md):p.126 (정정) | 이 쪽에 없는 Definitions of variables 제목을 붙였다. | 실제 머리글 Appendix A만 기록했다. | p.126(인쇄 118), 머리글 Appendix A. 실제 표 캡션은 Table A.1: Directional distribution.이다. |

정정 31, 보완 3, 이상 없음 5
