---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Propwash/Det_Adjacent_Cells.f90
lines: 51
sha256: fd56f15154ef596d8a97d3961f8b75b02c968b5bcbbc2586ea55597e20c6e82c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Det_Adjacent_Cells.f90 — 판독 구간 기록

구간은 1행부터 51행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | EFDC+·GPLv2·저작권 머리말(1–8), 주어진 셀의 인접 셀(adjacent cell) 결정 주석(9–14). Det_Adjacent_Cells 시작(15), GLOBAL·Variables_Propwash 사용(17–18), implicit none·L 선언(20–25). adjacent_l(9,0:LA)을 할당(27)하고 전체 0 초기화(29). 원문: `adjacent_l = 0` (29). |
| 31–51 | 시작 시 15행 Det_Adjacent_Cells 안. L=2..LA 루프(31). 3×3 셀 순서는 위쪽 1·2·3, 중앙 4·5·6, 아래쪽 7·8·9라는 주석(32–35). 중심 번호 5에는 L을 저장(38). 대각 셀 1·3·7·9는 각각 두 경로의 SUBO+SVBO 합 중 하나가 1.5보다 크면 북서·북동·남서·남동 인덱스를 저장(40–43). 직접 이웃 2·4·6·8은 해당 면의 SVBO 또는 SUBO가 0.5보다 크면 북·서·동·남 인덱스를 저장(45–48). 루프·루틴 종료와 빈 줄(49–51). 별도 루틴 호출은 없다. 원문: `adjacent_l(5,L) = L` (38); `if( SUBO(L)     +SVBO(LNWC(L)) > 1.5 .or. SVBO(LNC(L))+SUBO(LNC(L))  > 1.5 ) adjacent_l(1,L) = LNWC(L)` (40); `if( SVBO(LNC(L))+SUBO(LNEC(L)) > 1.5 .or. SUBO(LEC(L))+SVBO(LNEC(L)) > 1.5 ) adjacent_l(3,L) = LNEC(L)` (41); `if( SUBO(L)     +SVBO(LWC(L))  > 1.5 .or. SVBO(L)     +SUBO(LSC(L))  > 1.5 ) adjacent_l(7,L) = LSWC(L)` (42); `if( SVBO(L)     +SUBO(LSEC(L)) > 1.5 .or. SUBO(LEC(L))+SVBO(LEC(L))  > 1.5 ) adjacent_l(9,L) = LSEC(L)` (43); `if( SVBO(LNC(L)) > 0.5 ) adjacent_l(2,L) = LNC(L)` (45); `if( SUBO(L) > 0.5 )      adjacent_l(4,L) = LWC(L)` (46); `if( SUBO(LEC(L)) > 0.5 ) adjacent_l(6,L) = LEC(L)` (47); `if( SVBO(L) > 0.5 )      adjacent_l(8,L) = LSC(L)` (48). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–29: adjacent_l을 조건 없이 할당한다. 이 루틴에는 allocated 검사나 deallocate 문장이 없다.
