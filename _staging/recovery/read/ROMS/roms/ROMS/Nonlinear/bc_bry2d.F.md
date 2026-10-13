---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/bc_bry2d.F
lines: 235
sha256: 51a9dad71893077f1ba7e3452164a1bce6523364d595d14d438e5ee83efac2db
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# bc_bry2d.F — 판독 구간 기록

구간은 1행부터 235행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | 시작 시 열린 바깥 블록 없음. cppdefs.h를 포함하는 bc_bry2d_mod 모듈이다(1–2). 머리말은 일반 2차원 경계장(boundary field)에 기울기(gradient) 조건을 적용한다고 적고 RHO/U/V 격자점(grid point) 루틴을 열거한다(11–18). implicit none·CONTAINS와 빈 줄·주석을 포함한다(22–25). 조건·반복·대입·호출 및 전처리 원문: `#include "cppdefs.h"` (1). |
| 26–47 | 시작 시 열린 바깥 블록 없음. bc_r2d_bry_tile의 인수 ng/tile/boundary/LBij/UBij와 모듈 선언이다(27–38). A는 경계를 따라 놓인 1차원 배열이며 ASSUMED_SHAPE에 따라 형상을 나눈다(40–44). set_bounds.h를 포함한다(46). 조건·반복·대입·호출 및 전처리 원문: `#ifdef ASSUMED_SHAPE` (40); `#else` (42); `#endif` (44); `#include "set_bounds.h"` (46). |
| 48–94 | 시작 시 루틴 `SUBROUTINE bc_r2d_bry_tile (ng, tile, boundary,                   &` (27) 안. RHO점의 네 boundary 값을 독립 IF로 검사한다(52·61·74·83). 서·동 경계의 남북 모서리에서 Jstr-1/Jend+1에 Jstr/Jend를 복사한다(54·57·63·66). 남·북 경계의 서동 모서리에서 Istr-1/Iend+1에 Istr/Iend를 복사한다(76·79·85·88). DOMAIN의 해당 모서리를 확인하며 루틴을 종료한다(53–93). 조건·반복·대입·호출 및 전처리 원문: `IF (boundary.eq.iwest) THEN` (52); `IF (DOMAIN(ng)%SouthWest_Corner(tile)) THEN` (53); `A(Jstr-1)=A(Jstr)` (54); `IF (DOMAIN(ng)%NorthWest_Corner(tile)) THEN` (56); `A(Jend+1)=A(Jend)` (57); `IF (boundary.eq.ieast) THEN` (61); `IF (DOMAIN(ng)%SouthEast_Corner(tile)) THEN` (62); `A(Jstr-1)=A(Jstr)` (63); `IF (DOMAIN(ng)%NorthEast_Corner(tile)) THEN` (65); `A(Jend+1)=A(Jend)` (66); `IF (boundary.eq.isouth) THEN` (74); `IF (DOMAIN(ng)%SouthWest_Corner(tile)) THEN` (75); `A(Istr-1)=A(Istr)` (76); `IF (DOMAIN(ng)%SouthEast_Corner(tile)) THEN` (78); `A(Iend+1)=A(Iend)` (79); `IF (boundary.eq.inorth) THEN` (83); `IF (DOMAIN(ng)%NorthWest_Corner(tile)) THEN` (84); `A(Istr-1)=A(Istr)` (85); `IF (DOMAIN(ng)%NorthEast_Corner(tile)) THEN` (87); `A(Iend+1)=A(Iend)` (88). |
| 95–117 | 시작 시 열린 바깥 블록 없음. bc_u2d_bry_tile의 모듈·인수·1차원 A 형상 선언이다(97–114). set_bounds.h를 포함한다(116). 조건·반복·대입·호출 및 전처리 원문: `#ifdef ASSUMED_SHAPE` (110); `#else` (112); `#endif` (114); `#include "set_bounds.h"` (116). |
| 118–164 | 시작 시 루틴 `SUBROUTINE bc_u2d_bry_tile (ng, tile, boundary,                   &` (97) 안. U점의 서·동 경계는 남북 모서리에서 Jstr-1/Jend+1에 인접 값을 복사한다(122–138). 남·북 경계는 서쪽 IstrU-1에 IstrU를 복사하고 동쪽 Iend+1에 Iend를 복사한다(144–160). 각 대입은 boundary와 DOMAIN 모서리 조건 안에 있다. RETURN·루틴 종료와 빈 줄을 포함한다(162–164). 조건·반복·대입·호출 및 전처리 원문: `IF (boundary.eq.iwest) THEN` (122); `IF (DOMAIN(ng)%SouthWest_Corner(tile)) THEN` (123); `A(Jstr-1)=A(Jstr)` (124); `IF (DOMAIN(ng)%NorthWest_Corner(tile)) THEN` (126); `A(Jend+1)=A(Jend)` (127); `IF (boundary.eq.ieast) THEN` (131); `IF (DOMAIN(ng)%SouthEast_Corner(tile)) THEN` (132); `A(Jstr-1)=A(Jstr)` (133); `IF (DOMAIN(ng)%NorthEast_Corner(tile)) THEN` (135); `A(Jend+1)=A(Jend)` (136); `IF (boundary.eq.isouth) THEN` (144); `IF (DOMAIN(ng)%SouthWest_Corner(tile)) THEN` (145); `A(IstrU-1)=A(IstrU)` (146); `IF (DOMAIN(ng)%SouthEast_Corner(tile)) THEN` (148); `A(Iend+1)=A(Iend)` (149); `IF (boundary.eq.inorth) THEN` (153); `IF (DOMAIN(ng)%NorthWest_Corner(tile)) THEN` (154); `A(IstrU-1)=A(IstrU)` (155); `IF (DOMAIN(ng)%NorthEast_Corner(tile)) THEN` (157); `A(Iend+1)=A(Iend)` (158). |
| 165–187 | 시작 시 열린 바깥 블록 없음. bc_v2d_bry_tile의 모듈·인수·1차원 A 형상 선언이다(167–184). set_bounds.h를 포함한다(186). 조건·반복·대입·호출 및 전처리 원문: `#ifdef ASSUMED_SHAPE` (180); `#else` (182); `#endif` (184); `#include "set_bounds.h"` (186). |
| 188–209 | 시작 시 루틴 `SUBROUTINE bc_v2d_bry_tile (ng, tile, boundary,                   &` (167) 안. V점 서·동 경계의 남북 모서리 기울기 복사이다(192–208). 남쪽 JstrV-1에 JstrV를, 북쪽 Jend+1에 Jend를 복사한다(194·197·203·206). boundary와 DOMAIN 모서리 조건을 검사한다. 조건·반복·대입·호출 및 전처리 원문: `IF (boundary.eq.iwest) THEN` (192); `IF (DOMAIN(ng)%SouthWest_Corner(tile)) THEN` (193); `A(JstrV-1)=A(JstrV)` (194); `IF (DOMAIN(ng)%NorthWest_Corner(tile)) THEN` (196); `A(Jend+1)=A(Jend)` (197); `IF (boundary.eq.ieast) THEN` (201); `IF (DOMAIN(ng)%SouthEast_Corner(tile)) THEN` (202); `A(JstrV-1)=A(JstrV)` (203); `IF (DOMAIN(ng)%NorthEast_Corner(tile)) THEN` (205); `A(Jend+1)=A(Jend)` (206). |
| 210–235 | 시작 시 루틴 `SUBROUTINE bc_v2d_bry_tile (ng, tile, boundary,                   &` (167) 안. V점 남·북 경계의 서동 모서리 기울기 복사이다(214–230). Istr-1에 Istr를, Iend+1에 Iend를 복사한다(216·219·225·228). RETURN·bc_v2d_bry_tile 종료·bc_bry2d_mod 모듈 종료이다(232–235). 조건·반복·대입·호출 및 전처리 원문: `IF (boundary.eq.isouth) THEN` (214); `IF (DOMAIN(ng)%SouthWest_Corner(tile)) THEN` (215); `A(Istr-1)=A(Istr)` (216); `IF (DOMAIN(ng)%SouthEast_Corner(tile)) THEN` (218); `A(Iend+1)=A(Iend)` (219); `IF (boundary.eq.inorth) THEN` (223); `IF (DOMAIN(ng)%NorthWest_Corner(tile)) THEN` (224); `A(Istr-1)=A(Istr)` (225); `IF (DOMAIN(ng)%NorthEast_Corner(tile)) THEN` (227); `A(Iend+1)=A(Iend)` (228). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 52–90·122–160·192–230: 세 루틴의 대입 조건은 boundary 번호와 DOMAIN 모서리 플래그이다. 이 파일에는 EWperiodic·NSperiodic·LBC_apply를 검사하는 실행문이나 exchange 루틴 호출이 없다.
