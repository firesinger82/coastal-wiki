---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-Original/fsedmode.f90
lines: 85
sha256: 1ee3ccd370812d89a8c15624dba85e49a9929c4a33144b75ca1a530a4ace542a
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# fsedmode.f90 — 판독 구간 기록

구간은 1행부터 85행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | EFDC+·저작권·GPLv2 머리말(1–8). FSEDMODE 입구(9). IMODE=1은 소류사(bedload), IMODE=2는 부유사(suspended load)의 무차원 수송 분율(transport fraction)이라는 주석(11–12). WS·USTOT·USGRN은 m/s, RSNDM은 USTAR/WSET의 이진 전환(binary switch) 기준값이라고 설명한다(14–17). 인수·지역변수 선언 뒤 WS=0이면 0을 반환하고 종료한다(19–27). 조건·계산·호출 원문: `if( WS == 0. )then` (24). |
| 29–43 | 시작 시 9행 FSEDMODE 안. ISNDM2=0이면 총응력(total stress) 마찰속도 USTOT를, else이면 입자응력(grain stress) 마찰속도 USGRN을 선택한다(29–35). USDWS=US/WS를 계산한다(36). ISNDM1=0은 소류사와 부유사 모두 분율 1.0을 반환한다(40–42). 조건·계산·호출 원문: `if( ISNDM2 == 0 )then` (31); `else` (33); `USDWS = US/WS` (36); `if( ISNDM1 == 0 )then` (40); `FSEDMODE = 1.0` (42). |
| 44–63 | 시작 시 9행 FSEDMODE·40행 모드 선택 블록 안. ISNDM1=1은 0에서 시작한다(44–46). IMODE=1이면 1, else이면 USDWS>=RSNDM일 때 1로 설정한다(47–51). ISNDM1=2는 IMODE=1에 1을 반환하고 else에서 (USDWS-0.4)/9.6을 0..1로 제한한다(53–62). 조건·계산·호출 원문: `elseif( ISNDM1 == 1 )then` (44); `if( IMODE == 1 )then` (47); `FSEDMODE = 1.0` (48); `else` (49); `if( USDWS >= RSNDM ) FSEDMODE = 1.` (50); `elseif( ISNDM1 == 2 )then` (53); `if( IMODE == 1 )then` (55); `FSEDMODE = 1.0` (56); `else` (57); `TMPVAL = ((USDWS)-0.4)/9.6` (58); `TMPVAL = min(TMPVAL,1.0)` (59); `TMPVAL = max(TMPVAL,0.0)` (60). |
| 64–85 | 시작 시 9행 FSEDMODE·40행 모드 선택 블록 안. ISNDM1=3은 0에서 시작한다(64–66). IMODE=1이면 USDWS<RSNDM일 때 1, else이면 USDWS>=RSNDM일 때 1을 반환한다(67–71). ISNDM1=4는 선형 분율을 0..1로 제한한다(73–77). IMODE=1이면 그 보수, else이면 분율 자체를 반환한다(78–82). 선택 블록과 함수를 종료한다(83–85). 조건·계산·호출 원문: `elseif( ISNDM1 == 3 )then` (64); `if( IMODE == 1 )then` (67); `if( USDWS < RSNDM ) FSEDMODE = 1.` (68); `else` (69); `if( USDWS >= RSNDM ) FSEDMODE = 1.` (70); `elseif( ISNDM1 == 4 )then` (73); `TMPVAL = ((USDWS)-0.4)/9.6` (75); `TMPVAL = min(TMPVAL,1.0)` (76); `TMPVAL = max(TMPVAL,0.0)` (77); `if( IMODE == 1 )then` (78); `FSEDMODE = 1.-TMPVAL` (79); `else` (80). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24–27·40–83: WS=0이면 모드와 관계없이 0을 반환한다. WS가 0이 아닌 경우 ISNDM1=0..4 밖의 값을 처리하는 기본 분기는 없다.
- 47–51·55–62·67–71·78–82: IMODE=1 이외의 모든 값은 else의 부유사 경로를 사용한다. IMODE=2인지 검사하는 조건은 없다.
- 31–35: ISNDM2=0 이외의 모든 값은 USGRN을 사용한다.

