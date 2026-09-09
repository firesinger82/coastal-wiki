# Claude 적대적 검토 — HG 준비

검토자: Claude Opus 5 · 2026-09-09 · 세션 6591c7fa-8cf6-45db-9e51-10d44e165c08

아래는 Claude 응답 원문이다. 사람 승인이나 게이트 PASS를 부여하는 문서가 아니다. 후속 반영 내역은 HG-REVIEW 및 PROGRESS에 기록한다.

## 판정

**승인 보류 권고.** 사람 승인은 부여하지 않았고(권한 밖), 아래 2건은 승인 전 수정이 필요한 차단 사유다.

## 통과 확인한 것

- **기존 60 승인 보존** — 현재 `decisions.json` 60 approved / 43 pending. 구 26개 crosswalk 해시가 정확히 60회 등장하고, `source_span_hash` 집계가 `/tmp` 원본과 동일(30/29), 중복 해시 위치(673·748·853·868행)까지 일치. 헤더·`approver`·`approved_at`·scope 문자열 무변경. testgenmodule B8 의 별도 P0-개정 scope 도 보존됨(`XBeach-supplement-decisions.json:1413-1427`). scope 의 "59-supplement" 표기는 오류가 아니라 59 batch + P0 개정 1건 구조.
- **43건 커버리지 1:1** — B00/B01/D00/V00 `confirmed_delta` 43 = pending 영수증 43 = HG-REVIEW 행 43. shard 집계 4·16·20·3 일치.
- **승인 범위 문장**(`HG-REVIEW-20260909.md:5`)은 명확하고 자기승인 회피도 지켜짐.
- 원문 대조 표본 #01·#02·#10·#11·#12·#13·#38 모두 소스에서 성립. 예: `libtool.m4:5157` 대문자 F 대입 vs `:6128` 소문자 선언, `libtool.m4:7537` 좌변에만 `x` 접두, `texinfo.tex` 에 `00B1/00B5/00D7/00F7` 매핑 부재.

## 차단 사유

### B1. texinfo.tex 9건 라인번호 +1 오프셋 — **준비 회귀**

`texinfo.tex:7882` 에 form feed(`\x0c`)가 있다. 정규화 스크립트(`HANDOFF-CODEX.md:72`)의 `str.splitlines()` 는 form feed 에서도 분할하므로 7882행 이후 번호가 1 밀린다. 게다가 스크립트(`HANDOFF-CODEX.md:68`)는 `verified_at_lines`(밀린 값)를 `lines`(리포터의 정확한 값)보다 우선했다.

crosswalk 에 증거가 남아 있다 — 7882행 이전 11건은 `claimed_lines == verified_at_lines`, 이후 9건만 정확히 1 차이:

| HG-REVIEW | 표기 라인 | 실제 라인 | crosswalk |
|---|---|---|---|
| 32·33·34·35·36 | 7943·8055·8249·8432·8883 | 7942·8054·8248·8431·8882 | `XBeach-D00/trunk__config__texinfo.tex.crosswalk.json:428,460,492,524,556` |
| 37·38·39·40 | 9189·9156·9420·9643 | 9188·9155·9419·9642 | 같은 파일 `:588,620,652,684` |

소스 확인: `texinfo.tex:9419-9420` 이 `{0162}{\cedilla{t}}`/`{0163}{\cedilla{T}}`(#39 가 9420-9421 로 표기), `texinfo.tex:8248-8253` 이 `\def\loop{%`…(#34 가 8249-8254 로 표기). 원래 적대검증 레코드는 올바른 값을 갖고 있다 — `XBeach-D00.span-verdicts.json:206` = `L9642-L9643`.

결과적으로 HG-REVIEW 행 32~40 의 `file:line` 표기와 `#L` 앵커가 모두 한 줄씩 어긋난다. 인용문 자체는 맞으므로 결함 주장은 유효하나, **승인 대상 레코드에 잘못된 위치가 고정된다.** manifest 에도 그대로 들어가 있다(`XBeach-supplement-manifest.json:4063` = `"9643-9644"`).

### B2. 적대검증 NARROWED 6건 미공시 — **준비 결함**

43건 중 6건의 adversarial verdict 가 `STANDS` 가 아니라 `NARROWED` 인데, HG-REVIEW 는 이를 표시하지 않고 축소 전 주장으로 한국어 요약을 썼다.

- **#05·#06·#07·#08 (netCDF)** — `netcdff90__Makefile.am.crosswalk.json:68`: "not on the supplied XBeach build path: configure.ac generates only the src makefiles, and the Windows static-library project compiles netcdf.f90 directly." 즉 XBeach 빌드에서는 재현되지 않는다는 것이 감사 자신의 최종 판정인데, 요약은 무조건형이다.
- **#09 (fortranextra.m4)** — `:120`: XBeach 는 `AC_FC_LINE_LENGTH([unlimited])` 를 1회만 호출하므로 캐시 오재사용은 추가 호출 전제.
- **#21 (texinfo.tex B0)** — `texinfo.tex.crosswalk.json:79`: 기본값이 bottom marks 라 비기본 설정 전제.

승인 요약이 감사 최종 판정과 어긋난 상태로 레코드에 편입된다. 표에 verdict 열을 넣거나 요약에 축소 조건을 반영해야 한다.

## 그 외 (차단 아님, 승인 전 정정 권고)

**준비 측**
- **제3자 귀속 오류**: #09 `trunk/m4/fortranextra.m4` 는 Autoconf 의 `AC_FC_LINE_LENGTH` 원문(`fortranextra.m4:1-31` 주석 헤더)이다. "빌드·배포 도구"가 아니라 외부. `HG-REVIEW:9` 의 30/13 분할은 31/12 가 맞다.
- **중복 계상 미공시**: #07·#08 은 automake 가 `Makefile.am`(#05·#06)에서 생성한 `Makefile.in` 의 동일 결함이다. "43건"이 서로 다른 문제 43개를 뜻하지 않음을 밝히지 않았다.
- **CRLF 라벨**: #03 은 주장 전체가 CR 바이트에 걸려 있는데 `quote_source` 가 LF 정규화본을 "authoritative" 로 표기한다(`create-keys.sh.crosswalk.json:83`). `reported_quote` 에 `\r\n` 이 보존되고 적대검증 바이트 검사도 STANDS 라 증거 소실은 없으나, 라벨이 사실과 다르다. `quote_encoding` 필드 분리 권고.
- **인용 구간이 주장을 뒷받침하지 못하는 행**: #01 의 소스 인용은 `build_configuration.bat:59` 한 줄뿐인데, 결함 성립에 필요한 내부 따옴표는 `:21-37`(있음) 대 `:42`(VS2017, 없음) 대비에서 나온다. 주장 자체는 성립하나 제시된 인용만으로는 판단 불가.
- **영수증이 제시 문서에 묶이지 않음**: pending 항목에 `scope` 가 없고 승인 시 기입될 문자열이 HG-REVIEW 해시를 참조하지 않는다. `HG-REVIEW-20260909.md` sha256 을 scope 에 넣기를 권고.
- **HANDOFF 잠재 사고**: `HANDOFF-CODEX.md:133-134` 의 재생성 스크립트는 기존 60건 scope 를 일괄 `"...presented 2026-09-07"` 로 덮어써 59-batch / P0-개정 구분을 파괴한다. 이번엔 Codex 가 이탈해 원문을 보존했으나(옳은 판단), 문서를 고치지 않으면 다음 실행자가 밟는다.
- **V00 shard 구성**: `teamcity-distribute-windows.py`(#41, XBeach 자체 파일)가 vendor shard V00 에 있다. 이월된 shard 기반 vendor 태깅 시 오태깅 위험.

**기존 findings 측 (준비 회귀 아님, 이월 사항)**
- vendor 태깅 미완, REFUTED 인용 미검증 10건, conflict 3건 — `HANDOFF-CODEX.md:207-211` 에 이미 이월 명시됨.
- 승인 표에 severity 가 없다. HIGH 는 #01·#03 둘뿐이고 나머지는 MED/LOW 인데 표만 보면 알 수 없다.

## 한계

- 이 세션은 **Bash 가 비활성**이다. 따라서 (a) bound_files 3건의 sha256 재계산, (b) `verify_crosswalk.py`·`verify_supplement_modelaudit.py` 재실행, (c) 보존된 60건의 진짜 byte diff 를 수행하지 못했다. "crosswalk 13/13 PASS, mechanical_fails=0"은 `HG-PREPARATION-CHECKS-20260909.json` 의 자기보고를 그대로 인용한 것이며 독립 검증이 아니다. 60건 보존은 필드·개수·행위치 대조로 근사했다.
- 43건 중 원문 재대조한 것은 #01·#02·#03·#10·#11·#12·#13·#30·#34·#37·#38·#39·#40 이다. 나머지 항목의 의미 판정은 새로 수행하지 않았다(요청대로 bounded packet review).
- B1 의 오프셋 검사는 `\x0c` 존재 여부로 스캔했다. trunk 내 form feed 보유 파일은 `texinfo.tex`(1개)와 `LICENSE`(9개, 43건에 미포함)뿐이며, 나머지 42건은 `claimed_lines == verified_at_lines` 로 확인했다.
