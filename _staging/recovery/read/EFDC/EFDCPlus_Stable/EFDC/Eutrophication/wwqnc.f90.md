---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/wwqnc.f90
lines: 63
sha256: 231b3ddf48d52359a1681b54706446e272b7d848981586570d886c41cb360d95
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# wwqnc.f90 — 판독 구간 기록

구간은 1행부터 63행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | EFDC+ 안내·저작권·GPLv2 머리말(1–8). WWQNC는 음수 농도 수질 상태변수 정보를 출력한다는 주석을 둔다(9–12). GLOBAL·Variables_WQ를 사용하고 implicit none을 지정한다(14–17). 인덱스·IFLAG와 `character*5 :: WQVN(23)` (20)을 선언한다. DATA의 성분명은 BC·BD·BG·RPOC·LPOC·DOC·RPOP·LPOP·DOP·PO4T·RPON·LPON·DON·NH4·NO3·SU·SA·COD·O2·TAM·FCB·CO2·MALG이다(22–24). 빈 줄(25)까지 포함한다. |
| 26–41 | 시작 시 9행 WWQNC 안. `open(1,FILE = OUTDIR//'WQ3DNC.LOG',STATUS = 'UNKNOWN',POSITION = 'APPEND')` (26)으로 로그를 덧붙이기 모드로 연다. IFLAG=0, L=2..LA·K=1..KC·NW=1..NWQV 루프를 돈다(28–31). 조건 원문은 `if( WQV(L,K,NW) < 0.0 )then` (32)이다. 참이면 성분명·수질 계산 횟수 ITNWQ·셀 L·IL/JL·층 K·농도를 출력하고 IFLAG=1로 설정한다(33–34). 루프 종료·close(1), `90 FORMAT(A5, I8, 4I5, E11.3)` (40)과 빈 줄(41)을 포함한다. |
| 42–58 | 시작 시 9행 WWQNC 안이며 로그 루프 밖. 음수 농도 제거 조건은 `if( IWQNC > 1 .and. IFLAG == 1 )then` (43)이다. 참이면 OpenMP 병렬 반복문과 ND·K·LP·L·NW private 지정(44), 영역·층·젖은 셀(wet cell) 루프(45–49)에서 LKWET로 셀을 찾는다(48). `if( ISKINETICS(NW) > 0 )then` (50) 안의 원문은 `if( WQV(L,K,NW) < 0.0 ) WQV(L,K,NW) = 0.0` (51)이다. 조건·루프·OpenMP·바깥 조건을 끝낸다(52–58). |
| 59–63 | 시작 시 9행 WWQNC 안이며 음수 제거 조건 밖. 빈 줄·return·빈 줄·END·마지막 빈 줄을 포함한다(59–63). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12·26·33: 주석은 출력 장치를 IWQONC라고 적는다. 실제 open·write·close의 장치 번호는 1이다(26·33·39).
- 20·31–33: 성분명 배열 크기는 23이다. 로그 루프는 NWQV까지 WQVN(NW)를 참조하며 이 접근 앞에 NW<=23 검사는 없다.
- 29–38·43–56: 로그 검사는 L=2..LA와 모든 NW=1..NWQV를 대상으로 한다. 농도 0 설정은 LKWET로 찾은 셀 중 ISKINETICS(NW)>0인 성분에만 수행한다.
