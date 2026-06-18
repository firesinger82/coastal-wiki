# SWAN → SWASH nesting (광역 spectral → nearshore 위상해상 처오름)

> 광역 **SWAN**(위상평균 spectral)으로 외해~연안 파랑장을 계산하고, 그 경계 스펙트럼을 **SWASH**(위상해상 비정수압)에 넘겨 항내/해빈의 개별 파·처오름(runup)을 해상하는 **오프쇼어→니어쇼어 결합 워크플로**. 위상평균 모델의 효율과 위상해상 모델의 해상력을 결합하는 표준 패턴.

## 다루는 개념·모델

- 개념: [`concepts/waves`](../../concepts/waves/)(spectral 파랑·radiation stress) · [`concepts/swash-zone`](../../concepts/swash-zone/)(처오름·wetting-drying)
- 모델: [`models/SWAN`](../../models/SWAN/)(위상평균, 광역) · [`models/SWASH`](../../models/SWASH/)(위상해상, 니어쇼어)
- 결합 메커닉(검수 근거):
  - SWAN writer: [`swan-nesting-io-implementation`](../../models/SWAN/source-analysis/swan-nesting-io-implementation.md) — `NGRID`(nest 격자 정의)+`NESTOUT`(경계 스펙트럼 파일 작성, `swanpre2.ftn:1984`)
  - SWASH reader: [`swash-boundary-spectral-transfer`](../../models/SWASH/source-analysis/swash-boundary-spectral-transfer.md) — `SwashBCspecfile` 의 **SWAN-포맷 분기**(`SwashBCspecfile.ftn90:281-911`, `lnest` SWAN nesting flag)
  - 명령 reference: [`swan-command-setup-grid-reference §4.3`](../../models/SWAN/manual-notes/swan-command-setup-grid-reference.md) · [`swash-user-manual BOUNDCOND §4.5.3`](../../models/SWASH/manual-notes/swash-user-manual.md)

## 워크플로 (실행 순서)

```
1. SWAN 광역 run (coarse)
   code/swan_coarse.swn
   - CGRID 광역 격자 + 바람·경계파 입력
   - NGRID 'nst' : SWASH 도메인 위치에 nest 출력격자 정의
   - NESTOUT 'nst' 'swan_spec.dat' : 경계 스펙트럼 파일 작성
   → 산출: swan_spec.dat (SWAN-포맷 2D 스펙트럼, 시간열)

2. SWASH 니어쇼어 run (fine)
   code/swash_nearshore.sws
   - CGRID 고해상 니어쇼어 격자 (수 m 격자)
   - VERTICAL <K> : 다층(분산 표현)
   - BOUNDCOND ... 'swan_spec.dat' : 1단계 SWAN 스펙트럼을 경계조건으로 read
   → 산출: 개별 파 시계열, runup, 침수, 항내 파고
```

## 재현 조건

- **실행 환경**: SWAN ≥41.51, SWASH ≥v9 (본 위키는 SWASH v12.01 소스 기준). MPI 빌드 권장.
- **격자 정합**: SWAN `NGRID` 의 위치·범위가 SWASH `CGRID` 경계와 일치해야 함. SWASH 가 SWAN 격자 위 스펙트럼을 경계점으로 보간(`SwashBCspecfile` nesting 좌표 매칭, §2.1 노트).
- **좌표계**: 두 모델 모두 동일 좌표(Cartesian 또는 spherical). SWAN 방향관례(nautical/cartesian)와 SWASH 일치 필요.
- ⚠ **본 예제는 검수된 명령 reference·source-analysis 기반 템플릿**(데이터·실행값은 placeholder). 실제 케이스는 도메인·수심·바람 입력으로 대체. 정량 결과 run 은 미수록(reproducible 절차만 제공).

## 파일

| 파일 | 내용 |
|---|---|
| [`code/swan_coarse.swn`](code/swan_coarse.swn) | SWAN 광역 run — NGRID+NESTOUT |
| [`code/swash_nearshore.sws`](code/swash_nearshore.sws) | SWASH 니어쇼어 run — BOUNDCOND SWAN 스펙트럼 read |
| [`results/README.md`](results/README.md) | 기대 I/O·검증 포인트 |

## 한국 적용 맥락

광역 SWAN(한국 연안 풍파, [[../../concepts/waves/06-model-application]]) → 항만/해빈 SWASH(정온도·처오름)는 한국 항만설계 정온도 분석([`harbor-tranquility-kds64`](../../concepts/waves/harbor-tranquility-kds64.md))의 위상해상 정밀화 경로. SWAN·SWASH 모두 TU Delft 동일 그룹·OCP 인프라 공유라 nesting 자연스러움.
