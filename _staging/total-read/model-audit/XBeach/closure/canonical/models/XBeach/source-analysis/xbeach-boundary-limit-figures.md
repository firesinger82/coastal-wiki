---
title: "XBeach 경계 수심 도해의 변수와 해석 범위"
canonical_source: self
layer: 2
depends_on: []
citation_status: verified
has_source_needed: false
verification_by: "Codex source cross-ref; Claude Sonnet adversarial review"
verification_date: 2026-09-09
verification_method: "Source and referenced-note cross-reference; independent MSI identity/disassembly where applicable"
note_author: "Codex"
note_date: 2026-09-09
---

# XBeach 경계 수심 도해의 변수와 해석 범위

동봉된 `boundaries_SB`, `boundaries_NH`, `boundaries_NH2`, `boundaries_NHplus`, `boundaries_NHplus2` 도해는 경계 수심을 검토하는 설명용 그림이다. 생성 코드도 이를 “illustrative plots”라고 설명한다. 색 경계를 특정 모델 설정의 검증 오차 한계로 해석하지 않는다. (원본: `trunk/doc/misc/generate_boundary_condition_limits_figures.m:1-3,69-73,133-136,165-170,231-234,263-268`.)

이 노트의 `trunk/`는 `models/XBeach/raw/source_code/` 기준이다. 아래는 생성 코드의 AI 해석이며 원본 도해·배열값과 구분한다.

## 공통 좌표와 무차원수

| 항목 | 생성 코드의 값 | 원본 라인 |
|---|---|---|
| 파고 표본 | 2–8 m, 간격 0.1 m | `generate_boundary_condition_limits_figures.m:8` |
| 수심 표본 | 0–40 m, 간격 1 m | 같은 파일 `:9` |
| 주기 표본 | 6–18 s, 간격 0.25 s | 같은 파일 `:10` |
| 상대 파고 | `HiD=HD./DH`, 그림 축은 Hs/h | 같은 파일 `:12-16,34-37` |
| 군속도/위상속도 비 | `CgiC=cg./c`, n=cg/c | 같은 파일 `:17-18,52-55` |
| 상대수심 | `KH=k.*DT`, 중력가속도 9.81을 넘겨 k 계산 | 같은 파일 `:19-20` |
| 주기 축 라벨 | Tm−1,0 ≈ Tp/1.1 | 같은 파일 `:55,101,119,199,217` |

위 표의 축약 파일명은 모두 `trunk/doc/misc/generate_boundary_condition_limits_figures.m`이다. 0 수심이 격자에 들어 있으므로 `HiD`는 그 경계에서 나눗셈 특이점이 있고, 코드가 명시적으로 대체하는 것은 `CgiC`의 NaN뿐이다. 이 그림의 표본범위를 계산 가능 수심의 보증으로 쓰지 않는다. (원본: 같은 파일 `:8-20`.)

## 모드별 등고 수준

| 도해 | 생성 코드에 지정된 수준 | 원본 |
|---|---|---|
| SB 상대 파고 | 1, 1/2, 1/3, 1/4, 1/5, 0 | 생성 코드 `:34` |
| SB n=cg/c | 0.95부터 0.60까지 0.05 간격, 마지막 0 | 생성 코드 `:52` |
| NH kh | 0.5, 1, 1.1, 1.25, 2 | 생성 코드 `:116` |
| NHplus kh | 0.5, 1, 2, 3, 3.5, 4, 5 | 생성 코드 `:214` |

NH와 NHplus의 차이는 kh 등고 수준과 색 배열로 명시된다. 단순히 “NH는 kh≤1.1, NHplus는 kh≤3.5이면 유효”라고 이분법적으로 옮기면 색 전이·파고/수심 조건·주기 조건을 잃는다. 실제 입력 선택 시에는 [모드별 구현](xbeach_mode_dispatch.md)과 [비정수압 모델](xbeach_nonh.md)의 적용범위를 함께 본다. (원본: 생성 코드 `:80-119,178-217`.)

`NH2`와 `NHplus2`는 세 번째 패널의 line/patch 객체를 두 번째 패널로 복사하고 세 번째 패널을 제거한 합성 그림이다. 별도 solver 모드나 추가 실험 결과가 아니다. (원본: 생성 코드 `:138-170,236-268`.)

- [SB 원본 도해](../raw/source_code/trunk/doc/misc/boundaries_SB.png)
- [NH 원본 도해](../raw/source_code/trunk/doc/misc/boundaries_NH.png), [NH 합성 도해](../raw/source_code/trunk/doc/misc/boundaries_NH2.png)
- [NHplus 원본 도해](../raw/source_code/trunk/doc/misc/boundaries_NHplus.png), [NHplus 합성 도해](../raw/source_code/trunk/doc/misc/boundaries_NHplus2.png)
