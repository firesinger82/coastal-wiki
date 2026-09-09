---
title: "XBeach 빌드·배포 및 포함 외부 구성요소의 적용 제약"
canonical_source: self
layer: 2
depends_on: []
citation_status: verified
has_source_needed: false
verification_by: "Codex source cross-ref; Claude Sonnet adversarial review"
verification_date: 2026-09-09
verification_method: "Exact source SHA and physical-LF quote cross-reference; scoped adversarial review"
note_author: "Codex"
note_date: 2026-09-09
---

# XBeach 빌드·배포 및 포함 외부 구성요소의 적용 제약

이 노트는 저장소에 포함된 빌드·배포 스크립트와 외부 구성요소의 소스 분석이다. 아래 항목은 AI가 코드로부터 도출한 적용 제약이며, 원본 코드는 각 파일·라인 인용에서 구분한다. `NARROWED`는 반증 검토로 적용 조건을 좁힌 항목, `STANDS`는 검토 후 주장이 유지된 항목이다. 구현 수정 여부나 최신 배포판에 대한 판정은 포함하지 않는다.

특히 포함된 netCDF의 Makefile은 일반 XBeach configure 경로에 등록되지 않고 Windows 프로젝트는 Fortran 파일을 직접 컴파일한다. 따라서 해당 빌드 규칙 문제는 별도 netCDF 빌드에 한정된다. Fortran 줄 길이 매크로도 XBeach에서는 한 번만 호출된다. (원본: `trunk/configure.ac:55-60,89-93`; `trunk/src/xbeachlibrary/xbeachlibrary.vfproj:170-187`.)

파일별 기록을 보존하므로 항목 수는 고유 결함 수와 같지 않다. #07·#08의 `Makefile.in`은 #05·#06의 `Makefile.am`에서 생성된 같은 규칙의 표현이다. (원본: `trunk/lib/win32/netcdff90/Makefile.in:1-3,334-335,602-605`; `trunk/lib/win32/netcdff90/Makefile.am:21-24,65-70`.)

모든 `trunk/` 인용은 `models/XBeach/raw/source_code/` 기준이며 라인은 LF로 구분한 실제 파일 위치다. Texinfo의 form-feed는 새 LF 라인으로 세지 않는다.

## 파일별 제약

| 번호 | 구성요소 | 심각도 · 적대검증 | 원본 파일 · 실제 라인 · 감사 ID | AI 분석 요약 |
|---|---|---|---|---|
| <a id="xb-build-01"></a>01 | 빌드·배포 도구 | HIGH · STANDS | [trunk/config/build_configuration.bat:59](../raw/source_code/trunk/config/build_configuration.bat#L59) · `B0` | 구버전 분기의 devenv_path 내부 따옴표와 호출부 따옴표가 겹쳐 공백 포함 실행 경로가 깨짐. |
| <a id="xb-build-02"></a>02 | 빌드·배포 도구 | MED · STANDS | [trunk/config/clean_distribute.bat:6-11](../raw/source_code/trunk/config/clean_distribute.bat#L6) · `B0` | 삭제 대상 루트인 %1을 검사하지 않아 인수 누락 시 드라이브 루트의 dist 디렉터리가 삭제 대상이 됨. |
| <a id="xb-build-03"></a>03 | 빌드·배포 도구 | HIGH · STANDS | [trunk/config/create-keys.sh:1-5](../raw/source_code/trunk/config/create-keys.sh#L1) · `B0` | CRLF 줄바꿈 때문에 Unix 직접 실행이 실패하고 Bash 실행에서는 키 유형·호스트 인수에 CR이 붙음. |
| <a id="xb-build-04"></a>04 | 빌드·배포 도구 | MED · STANDS | [trunk/config/teamcity-build.sh:19](../raw/source_code/trunk/config/teamcity-build.sh#L19) · `B1` | 기존 _prev 디렉터리에 cp -r을 반복하면 이전 스냅샷 교체 대신 하위 디렉터리로 복사됨. |
| <a id="xb-build-05"></a>05 | 외부 netCDF | MED · NARROWED | [trunk/lib/win32/netcdff90/Makefile.am:21-24](../raw/source_code/trunk/lib/win32/netcdff90/Makefile.am#L21) · `B0` | Fortran include 의존성이 객체 대신 라이브러리에 걸려 include 변경 시 재컴파일 없이 재링크될 수 있음. 단, 제공된 XBeach 빌드 경로는 이 규칙을 사용하지 않으며 별도 netCDF 빌드에 한정됨. |
| <a id="xb-build-06"></a>06 | 외부 netCDF | MED · NARROWED | [trunk/lib/win32/netcdff90/Makefile.am:65-70](../raw/source_code/trunk/lib/win32/netcdff90/Makefile.am#L65) · `B2` | 동일 소스의 .lo와 .o를 별도로 생성하여 병렬 빌드 시 모듈 파일 쓰기가 경합할 수 있음. 단, 제공된 XBeach 빌드 경로는 이 규칙을 사용하지 않으며 별도 netCDF 빌드에 한정됨. |
| <a id="xb-build-07"></a>07 | 외부 netCDF | MED · NARROWED | [trunk/lib/win32/netcdff90/Makefile.in:334-335](../raw/source_code/trunk/lib/win32/netcdff90/Makefile.in#L334) · `B0` | Fortran include 변경이 객체 재컴파일을 유발하지 않아 오래된 객체로 재링크될 수 있음. 단, 제공된 XBeach 빌드 경로는 이 규칙을 사용하지 않으며 별도 netCDF 빌드에 한정됨. |
| <a id="xb-build-08"></a>08 | 외부 netCDF | MED · NARROWED | [trunk/lib/win32/netcdff90/Makefile.in:602-605](../raw/source_code/trunk/lib/win32/netcdff90/Makefile.in#L602) · `B2` | 모듈용 .o와 라이브러리용 .lo가 동일 소스를 병렬 컴파일하며 모듈 파일 쓰기가 경합할 수 있음. 단, 제공된 XBeach 빌드 경로는 이 규칙을 사용하지 않으며 별도 netCDF 빌드에 한정됨. |
| <a id="xb-build-09"></a>09 | 외부 Autoconf 계열 매크로 | MED · NARROWED | [trunk/m4/fortranextra.m4:48-53](../raw/source_code/trunk/m4/fortranextra.m4#L48) · `B0` | 서로 다른 줄 길이·소스 형식 검사에서 언어별 캐시 키를 공유함. XBeach의 실제 호출은 1회이므로 추가 호출 또는 다른 설정에서 캐시 재사용 시에 한정됨. |
| <a id="xb-build-10"></a>10 | 외부 Libtool | MED · STANDS | [trunk/m4/libtool.m4:1077-1081](../raw/source_code/trunk/m4/libtool.m4#L1077) · `B2` | Darwin 배포 타깃 11 이상에 맞는 undefined-symbol 정책 분기가 없음. |
| <a id="xb-build-11"></a>11 | 외부 Libtool | MED · STANDS | [trunk/m4/libtool.m4:5157](../raw/source_code/trunk/m4/libtool.m4#L5157) · `B4` | OS/2 분기에서 old_archive_from_new_cmds의 F를 대문자로 잘못 써 별도 변수에 대입함. |
| <a id="xb-build-12"></a>12 | 외부 Libtool | LOW · STANDS | [trunk/m4/libtool.m4:6043-6048](../raw/source_code/trunk/m4/libtool.m4#L6043) · `B6` | 전체 host triplet을 sysv4·osf3 단독 패턴과 비교하여 플랫폼 전용 분기를 놓침. |
| <a id="xb-build-13"></a>13 | 외부 Libtool | MED · STANDS | [trunk/m4/libtool.m4:7537-7541](../raw/source_code/trunk/m4/libtool.m4#L7537) · `B7` | 분리된 -L·-R 플래그 비교 시 한쪽에만 x를 붙여 다음 디렉터리 인수를 놓침. |
| <a id="xb-build-14"></a>14 | 빌드·배포 도구 | MED · STANDS | [trunk/src/xbeach/build/distribute.bat:18-19](../raw/source_code/trunk/src/xbeach/build/distribute.bat#L18) · `B0` | 실행파일 후처리가 공용 배포 디렉터리를 삭제하여 라이브러리 후처리가 배치한 DLL도 제거함. |
| <a id="xb-build-15"></a>15 | 빌드·배포 도구 | MED · STANDS | [trunk/src/xbeach/build/distribute.bat:25-26](../raw/source_code/trunk/src/xbeach/build/distribute.bat#L25) · `B2` | 패키징 전 TargetDir을 비우지 않아 이전 실행파일·DLL이 새 배포물에 포함될 수 있음. |
| <a id="xb-build-16"></a>16 | 빌드·배포 도구 | MED · STANDS | [trunk/src/xbeach/build/zip.bat:20-21](../raw/source_code/trunk/src/xbeach/build/zip.bat#L20) · `B1` | 기존 ZIP 갱신 시 소스에서 사라진 항목이 남아 오래된 산출물이 유지될 수 있음. |
| <a id="xb-build-17"></a>17 | 빌드·배포 도구 | LOW · STANDS | [trunk/src/xbeach/build/zip.bat:26](../raw/source_code/trunk/src/xbeach/build/zip.bat#L26) · `B2` | 대상 폴더의 기존 7za.exe를 덮어쓴 뒤 임시 파일과 구분 없이 삭제함. |
| <a id="xb-build-18"></a>18 | 빌드·배포 도구 | MED · STANDS | [trunk/src/xbeachlibrary/Makefile.am:84-87](../raw/source_code/trunk/src/xbeachlibrary/Makefile.am#L84) · `B1` | version.dat에 갱신 의존성이 없어 증분 빌드에서 이전 리비전·빌드 날짜가 유지됨. |
| <a id="xb-build-19"></a>19 | 빌드·배포 도구 | MED · STANDS | [trunk/src/xbeachlibrary/build/distribute.bat:28-29](../raw/source_code/trunk/src/xbeachlibrary/build/distribute.bat#L28) · `B2` | 각 라이브러리 후처리가 TargetDir을 무시하고 양쪽 라이브러리를 배포하여 오래된 상대 바이너리나 경합이 생길 수 있음. |
| <a id="xb-build-20"></a>20 | 빌드·배포 도구 | LOW · STANDS | [trunk/src/xbeachlibrary/includes/version/makeversiondat.bat:13](../raw/source_code/trunk/src/xbeachlibrary/includes/version/makeversiondat.bat#L13) · `B1` | DATE의 고정 위치를 잘라 빌드 날짜를 만들므로 Windows 로캘에 따라 날짜가 깨짐. |
| <a id="xb-build-21"></a>21 | 외부 Texinfo | LOW · NARROWED | [trunk/config/texinfo.tex:294-297](../raw/source_code/trunk/config/texinfo.tex#L294) · `B0` | 목차 뒤 색상·링크 mark가 끼면 첫 장의 머리말 대체 처리가 실패할 수 있음. 기본 bottom marks가 아닌 top marks 설정 및 특정 intervening mark 조건에 한정됨. |
| <a id="xb-build-22"></a>22 | 외부 Texinfo | LOW · STANDS | [trunk/config/texinfo.tex:1120-1124](../raw/source_code/trunk/config/texinfo.tex#L1120) · `B1` | pdfescapestring이 없으면 PDF 특수문자가 포함된 문자열도 이스케이프하지 않음. |
| <a id="xb-build-23"></a>23 | 외부 Texinfo | MED · STANDS | [trunk/config/texinfo.tex:1403-1406](../raw/source_code/trunk/config/texinfo.tex#L1403) · `B2` | URL의 괄호·역슬래시를 PDF 문자열에 직접 넣어 링크가 잘못 생성될 수 있음. |
| <a id="xb-build-24"></a>24 | 외부 Texinfo | MED · STANDS | [trunk/config/texinfo.tex:2057-2061](../raw/source_code/trunk/config/texinfo.tex#L2057) · `B3` | fonttextsize 10을 호출할 때마다 문단 간격이 절반으로 줄어듦. |
| <a id="xb-build-25"></a>25 | 외부 Texinfo | LOW · STANDS | [trunk/config/texinfo.tex:2155-2158](../raw/source_code/trunk/config/texinfo.tex#L2155) · `B4` | reducedfonts가 smallcaps 대신 reducedcaps를 설정하여 축소 문단의 소문자 대문자꼴 크기가 유지됨. |
| <a id="xb-build-26"></a>26 | 외부 Texinfo | MED · STANDS | [trunk/config/texinfo.tex:3366-3370](../raw/source_code/trunk/config/texinfo.tex#L3366) · `B5` | oddfooting·everyfooting을 설정할 때마다 페이지 높이에서 12pt를 추가로 차감함. |
| <a id="xb-build-27"></a>27 | 외부 Texinfo | MED · STANDS | [trunk/config/texinfo.tex:3737-3742](../raw/source_code/trunk/config/texinfo.tex#L3737) · `B6` | 알파벳 목록에서 case-code 대신 itemno를 0과 비교하여 z·Z 이후의 범위 초과 검사가 작동하지 않음. |
| <a id="xb-build-28"></a>28 | 외부 Texinfo | MED · STANDS | [trunk/config/texinfo.tex:3856-3859](../raw/source_code/trunk/config/texinfo.tex#L3856) · `B7` | 중첩 multitable이 전역 열 너비·열 수·비율 모드를 덮어써 바깥 표 상태를 훼손할 수 있음. |
| <a id="xb-build-29"></a>29 | 외부 Texinfo | MED · STANDS | [trunk/config/texinfo.tex:4335-4339](../raw/source_code/trunk/config/texinfo.tex#L4335) · `B8` | novalidate가 스트림 초기화를 생략하지만 일부 닫기·목차 생성·float 메타데이터 쓰기는 계속 실행됨. |
| <a id="xb-build-30"></a>30 | 외부 Texinfo | MED · STANDS | [trunk/config/texinfo.tex:7365-7370](../raw/source_code/trunk/config/texinfo.tex#L7365) · `B9` | 매크로 인수 256개 제한을 숫자 비교 ifnum 대신 문자 비교 if로 검사함. |
| <a id="xb-build-31"></a>31 | 외부 Texinfo | MED · STANDS | [trunk/config/texinfo.tex:7469-7474](../raw/source_code/trunk/config/texinfo.tex#L7469) · `B10` | aa처럼 같은 문자로 시작하는 인수 이름이 sentinel 비교에 걸려 매개변수 처리를 조기 종료할 수 있음. |
| <a id="xb-build-32"></a>32 | 외부 Texinfo | MED · STANDS | [trunk/config/texinfo.tex:7942-7947](../raw/source_code/trunk/config/texinfo.tex#L7942) · `B11` | 외부 파일명 내부 공백은 제거하고 노드 주변 공백은 남겨 PDF 교차참조 대상이 불일치할 수 있음. |
| <a id="xb-build-33"></a>33 | 외부 Texinfo | LOW · STANDS | [trunk/config/texinfo.tex:8054-8059](../raw/source_code/trunk/config/texinfo.tex#L8054) · `B12` | Top 여부를 문자열 대신 출력 너비로 판별하여 같은 너비의 다른 노드도 절 이름이 생략될 수 있음. |
| <a id="xb-build-34"></a>34 | 외부 Texinfo | MED · STANDS | [trunk/config/texinfo.tex:8248-8253](../raw/source_code/trunk/config/texinfo.tex#L8248) · `B13` | 128–255 바이트 catcode 초기화 루프를 정의만 하고 호출하지 않으며 그룹 밖으로 변경도 유지되지 않음. |
| <a id="xb-build-35"></a>35 | 외부 Texinfo | MED · STANDS | [trunk/config/texinfo.tex:8431-8436](../raw/source_code/trunk/config/texinfo.tex#L8431) · `B14` | PDF 이미지 경로에 불필요한 epsfbox가 없다는 이유로 모든 이미지를 거부함. |
| <a id="xb-build-36"></a>36 | 외부 Texinfo | MED · STANDS | [trunk/config/texinfo.tex:8882-8884](../raw/source_code/trunk/config/texinfo.tex#L8882) · `B15` | Latin 인코딩에서 UTF-8로 돌아올 때 덮어쓴 UTF-8 선행 바이트 디코더가 복원되지 않음. |
| <a id="xb-build-37"></a>37 | 외부 Texinfo | LOW · STANDS | [trunk/config/texinfo.tex:9188-9192](../raw/source_code/trunk/config/texinfo.tex#L9188) · `B16` | 4바이트 UTF-8 초기화가 F4 이전에 끝나 최상위 유니코드 평면의 유효 시퀀스를 처리하지 못함. |
| <a id="xb-build-38"></a>38 | 외부 Texinfo | MED · STANDS | [trunk/config/texinfo.tex:9155-9160](../raw/source_code/trunk/config/texinfo.tex#L9155) · `B17` | UTF-8 매핑에 ±·µ·×·÷ 등이 빠져 출력에서 누락되고 로그만 남음. |
| <a id="xb-build-39"></a>39 | 외부 Texinfo | MED · STANDS | [trunk/config/texinfo.tex:9419-9420](../raw/source_code/trunk/config/texinfo.tex#L9419) · `B18` | U+0162와 U+0163의 대소문자 매핑이 서로 바뀜. |
| <a id="xb-build-40"></a>40 | 외부 Texinfo | MED · STANDS | [trunk/config/texinfo.tex:9642-9643](../raw/source_code/trunk/config/texinfo.tex#L9642) · `B19` | U+2192 오른쪽 화살표를 arrow가 아닌 mapsto를 출력하는 expansion으로 매핑함. |
| <a id="xb-build-41"></a>41 | 빌드·배포 도구 | LOW · STANDS | [trunk/config/teamcity-distribute-windows.py:57](../raw/source_code/trunk/config/teamcity-distribute-windows.py#L57) · `B8` | 소스 경로를 TeamCity 메시지에 넣을 때 구분자·줄바꿈을 이스케이프하지 않음. |
| <a id="xb-build-42"></a>42 | 외부 MPICH 예제 | LOW · STANDS | [trunk/lib/win32/mpich/examples/cpilog.c:53-56](../raw/source_code/trunk/lib/win32/mpich/examples/cpilog.c#L53) · `B0` | MPE 상태 반환값을 무시하여 이벤트 ID 할당·로그 쓰기 실패가 정상 수치 출력에 가려질 수 있음. |
| <a id="xb-build-43"></a>43 | 외부 MPICH 예제 | LOW · STANDS | [trunk/lib/win32/mpich/examples/fpilog.f:60-64](../raw/source_code/trunk/lib/win32/mpich/examples/fpilog.f#L60) · `B1` | MPE 반환 코드를 검사하지 않고 덮어써 이벤트 ID·로그 오류가 정상 수치 실행에 가려질 수 있음. |


## 실행 경로를 함께 볼 항목

구버전 Visual Studio 경로는 변수값에 따옴표를 포함하고 실행 시 다시 따옴표로 감싼다. VS2017의 따옴표 없는 대입과 구분해야 한다. (원본: `trunk/config/build_configuration.bat:21-42,59`.)

`create-keys.sh`는 CRLF 원본이다. LF로 정규화한 Markdown 인용만으로 CR 바이트 문제를 입증할 수 없으므로 해당 주장은 원본 바이트에 적용된다. (원본: `trunk/config/create-keys.sh:1-5`, SHA-256 `f9f52ed52b8575fb9c46e4721f0838ab0fb711590a22a1fef7562422775d60e0`.)

Texinfo 머리말 문제(#21)는 기본 bottom marks가 아닌 top marks 경로에서 특정 중간 mark가 있는 경우에 한정된다. 기본값과 fallback 구현을 함께 확인해야 한다. (원본: `trunk/config/texinfo.tex:294-297,3399-3400`.)
