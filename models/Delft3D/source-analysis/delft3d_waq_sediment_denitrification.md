---
title: "Delft3D WAQ 저니 탈질 source-analysis — densed.f90 (0차+1차 온도보정 N sink, bottom-layer)"
model: Delft3D
component: waq-process
canonical_source: self
citation_status: verified
verification_method: "Delft3D raw 직접 read: src/engines_gpl/waq/waq_process/densed.f90(158) 전수 — flux식·온도게이트·bottom-layer 게이트(IKMRK2∈{0,3})·공간균일 최적화 file:line 직접 검증(2026-07-07). 수주탈질 짝 denwat 는 [[delft3d_waq_process_library]] 커버."
note_author: "Claude Fable 5"
note_date: 2026-07-07
related:
  - models/Delft3D/source-analysis/delft3d_waq_process_library.md
  - models/Delft3D/source-analysis/delft3d_waq_sediment_oxygen_demand.md
  - models/Delft3D/source-analysis/delft3d_waq_ph_carbonate.md
---

# Delft3D WAQ 저니 탈질 — `densed.f90` (SUBROUTINE DENSED)

> 소스: `.../src/engines_gpl/waq/waq_process/densed.f90` (158줄, `module m_densed`).
> **정체**: 저니(sediment)에서의 **탈질(denitrification) — NO3⁻ → N2 제거 flux**. 하구·연안 부영양화 완화의 최대 질소 sink. 위키가 커버한 **수주 탈질 `denwat`([[delft3d_waq_process_library]])의 저니 대응짝** → 질소순환 sink 완결. SOD 노트(탄소·산소 diagenesis)와 인접하되 N 화학은 미겹침(상보).

## 0. flux process — 상태변수 구동
`phcarb`(진단, flux 0)과 달리 **flux를 실제 갱신**: `FL(1+IFLUX)`에 탈질률 기입(:138) → NO3 상태변수를 감소시킴. active + **bottom 층만** 처리.

## 1. 탈질 flux 식 (0차 + 1차 온도보정)
```fortran
TEMP20 = TEMP - 20.0
TEMFAK = DENRC * DENTC ** TEMP20                 ! :99-100 1차율 온도보정
NO3    = MAX(0.0, process_space_real(IP2))       ! :128 음수 클램프
FL(1+IFLUX) = (DENR + TEMFAK * NO3) / DEPTH       ! :138 [gN/m3/d]
```
- **0차항** `DENR` [gN/m²/d] — NO3 농도 무관 상시 탈질(저니 공급 제한 영역).
- **1차항** `TEMFAK·NO3` — NO3 1차율 `DENRC` [m/d] × Arrhenius형 온도계수 `DENTC^(T−20)`.
- **`/DEPTH`** — 면적률[/m²]을 셀 체적률[/m³]로 정규화(면 flux → 부피 소스).

## 2. 온도 게이트
```fortran
IF (TEMP <= CRTEMP) THEN
    TEMFAK = 0.0          ! :94-95 임계온도 이하 1차 탈질 정지
```
`CRTEMP` 이하에서 **1차항만 차단**(TEMFAK=0) — 0차항 `DENR`은 여전히 활성(식 :138에 DENR 상시 포함). 즉 저온에서도 0차 탈질은 계속됨.

## 3. bottom-layer 게이트
```fortran
IF (BTEST(IKNMRK(ISEG), 0)) THEN                  ! :110 active 셀
    CALL extract_waq_attribute(2, IKNMRK(ISEG), IKMRK2)  ! :111 2번째 속성
    IF ((IKMRK2==0).OR.(IKMRK2==3)) THEN          ! :112 단일층(0) 또는 바닥층(3)
```
탈질은 저니 가정이므로 **수주 중간층(IKMRK2=1,2)은 제외**, 연직구조 없는 단일층(0) 또는 3D 최하층(3)에서만. 저니 탈질을 수주 전체에 잘못 걸지 않는 물리 게이트.

## 4. ★공간균일 최적화 (성능 트릭)
```fortran
IF (IN1==0 .AND. IN3==0 .AND. IN4==0 .AND. IN5==0 .AND. IN6==0) THEN
    ... TEMFAK 1회 계산 ...
    TMPOPT = .FALSE.       ! :89-102 입력 전부 공간상수 → 루프 밖 1회
ELSE
    TMPOPT = .TRUE.        ! :104 하나라도 공간변화 → 매 셀 재계산
```
INCREM(=IN)이 0이면 그 입력이 공간불변 → DENR·DENRC·DENTC·TEMP·CRTEMP 가 모두 상수면 `TEMFAK`를 셀 루프 진입 전 1회만 계산(:118-125 재계산 스킵). 대형 격자에서 `DENTC^(T−20)` pow 연산 절약.

## 5. ★주요 findings
- **★0차+1차 혼합 kinetics**: 순수 1차(Michaelis 없음)가 아니라 NO3-무관 `DENR` 바닥항 + NO3-비례 `TEMFAK·NO3` — NO3가 0이어도 0차 탈질 지속(저니 유기물 공급 제한 가정). 캘리브레이션 시 두 knob 분리.
- **★저온 = 1차만 정지, 0차 잔존**: `CRTEMP` 게이트가 TEMFAK만 0으로(:95), DENR은 식에 상시 → 겨울철에도 0차 탈질 flux 유지. "임계온도 이하 탈질 정지"로 오해 금지.
- **★bottom-layer 전용**: IKMRK2∈{0,3} 게이트로 수주 중간층 제외 — 3D 성층 run에서 저니 탈질을 표층·중층에 안 걺. denwat(수주 탈질)과 층위로 분리.
- **DEPTH 정규화 주의**: flux가 [gN/m³/d]로 나오려면 면적률을 셀(=저층) 두께로 나눔 — 저층 두께가 얇으면 부피 농도 변화율이 커짐(얕은 bottom 셀 민감).
- **NO3 음수 클램프**(:128): 수치 언더슈트 방지.

## 6. Primary sources
- Delft3D-WAQ Processes Library — 탈질 process 정의(`DenSed`/`DenWat`). in-code 인용 없음(단순 kinetics), 파라미터 정의는 [[delft3d_waq_process_library]].
- 짝 process: 수주 탈질 `denwat` — [[delft3d_waq_process_library]] 커버.

## 7. 관련
- [[delft3d_waq_process_library]] — 수주 탈질 denwat·질화 nitrif·호출 규약(IKMRK 속성)
- [[delft3d_waq_sediment_oxygen_demand]] — 저층 diagenesis(탄소·산소, N과 상보)
- [[delft3d_waq_ph_carbonate]] — 인접 WAQ process(진단형과 대조: 본 노트는 flux형)
