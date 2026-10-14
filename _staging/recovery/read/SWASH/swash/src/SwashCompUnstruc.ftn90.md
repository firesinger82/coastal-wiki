---
file: models/SWASH/raw/source_code/swash/src/SwashCompUnstruc.ftn90
lines: 116
sha256: cb79d6b57d25c1cbcf267521aa455f8f39342b45eed4d617c54ade6bf1a1a133
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashCompUnstruc.ftn90 — 판독 구간 기록

구간은 1행부터 116행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–41 | `SwashCompUnstruc` 입구(1). 기관·저작권 2010–2026·GPL 3 이상·무보증 주석(3–27), 작성자·2017년 신설(30–36). 비구조 격자(unstructured grid)에서 한 전체 계산 단계를 수행한다는 목적(38–40). |
| 42–63 | 시작 시 1행 루틴 안. ocpcomm4·SwashCommdata3·SwashFlowdata 사용(44–46). `integer, save :: ient = 0 ! number of entries in this subroutine` (52), STPNOW 선언(54), 구조·소스 구분 주석(56–61). `if (ltrace) call strace (ient,'SwashCompUnstruc')` (62). |
| 64–81 | 시작 시 1행 루틴 안. 흐름 계산: `!TIMG    call SWTSTA(51)` (66), `if ( .not.momskip ) call SwashCompUFlow` (67), `!TIMG    call SWTSTO(51)` (68), `if (STPNOW()) return` (69). 수심 갱신: `!TIMG    call SWTSTA(52)` (73), `if ( kmax == 1 ) then` (74)은 `call SwashUpdateUDepths ( u1 )` (75), `else` (76)는 `call SwashUpdateUDepths ( udep )` (77), `!TIMG    call SWTSTO(52)` (79), `if (STPNOW()) return` (80). 이 구간의 !TIMG 행은 swash/switch.pl 57행 규칙으로 -timg에서 표시가 제거될 때 실행 코드가 된다. |
| 82–101 | 시작 시 1행 루틴 안. 층 경계면(layer interfaces) 갱신: `!TIMG    call SWTSTA(53)` (84), `if ( kmax > 1 ) call SwashLayUIntfaces` (85), `!TIMG    call SWTSTO(53)` (86). 젖음·마름(wetting and drying) 마스크 갱신: `!TIMG    call SWTSTA(54)` (90), `call SwashUDryWet` (91), `!TIMG    call SWTSTO(54)` (92), `if (STPNOW()) return` (93). 쇄파(wave breaking) 마스크 갱신: `!TIMG    call SWTSTA(54)` (97), `if ( isurf /= 0 ) call SwashUBreakPoint` (98), `!TIMG    call SWTSTO(54)` (99), `if (STPNOW()) return` (100). 이 구간의 !TIMG 세 쌍은 -timg에서 실행 코드가 된다(switch.pl:57). |
| 102–116 | 시작 시 1행 루틴 안. 수송(transport) 계산: `!TIMG    call SWTSTA(101)` (104), `if ( itrans /= 0 ) call SwashCompUTrans` (105), `!TIMG    call SWTSTO(101)` (106), `if (STPNOW()) return` (107). 3차원 난류(turbulence) 계산: `!TIMG    call SWTSTA(102)` (111), `if ( iturb /= 0 ) call SwashCompUTurb` (112), `!TIMG    call SWTSTO(102)` (113), `if (STPNOW()) return` (114). 이 구간의 !TIMG 행도 -timg에서 실행 코드가 된다(switch.pl:57). 루틴 종료(116). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 90–99: 젖음·마름 갱신과 쇄파 마스크 갱신의 시간 측정은 같은 타이머 번호 54를 사용한다.
- 67·73–114: momskip 조건은 SwashCompUFlow 호출에만 적용된다. 수심·층 경계면·젖음·마름·쇄파·수송·난류의 후속 경로에는 momskip 검사가 없다.
