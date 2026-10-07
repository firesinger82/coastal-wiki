---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Mapping/Create_List_No_Ghost_Cells.f90
lines: 54
sha256: 15afd3e7455693e33628d423d24a39fe9b8603fdaddd6056e4eb8fd8b8a91646
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Create_List_No_Ghost_Cells.f90 — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | EFDC+·저작권·GPLv2 머리말과 고스트 셀(ghost cell)을 제외한 활성 셀 L 목록 생성 목적·작성자·날짜 주석(1–16). `Create_List_No_Ghost_Cells`를 시작한다(17). GLOBAL·Variables_MPI_Mapping·MPI를 사용하고 implicit none·정수 I/J/L을 선언한다(19–26). 빈 줄을 포함한다. |
| 28–38 | 시작 시 17행 Create_List_No_Ghost_Cells 안. `if(.not.allocated(NoGhost) )then` (28)이면 NoGhost·IsGhost·GhostMask를 각각 LCM 크기로 할당한다(29–31). 조건 밖에서 IsGhost=.TRUE.·GhostMask=0.0·NoGhost=0·NNoGhost=0으로 초기화한다(35–38). 주석·빈 줄을 포함한다(33–34). |
| 39–54 | 시작 시 17행 Create_List_No_Ghost_Cells 안. `do J = 3,JC-2` (39), `do I = 3,IC-2` (40)에서 L=LIJ(I,J)를 복사한다(41). `if( L > 0 )then ! *** Only records the active cells` (42)이면 `NNoGhost = NNoGhost + 1` (43), NoGhost 목록의 해당 위치에 L 복사(44), IsGhost(L)=.FALSE.·GhostMask(L)=1.0 설정(45–46). 조건·루프 종료(47–49). LA_Local_no_ghost에 NNoGhost를 복사하고 루틴을 닫는다(51–54). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28–32: 세 배열 할당 여부를 결정하는 검사는 NoGhost 한 배열에만 있다.
- 39–40: 고스트 영역 제외 범위는 양쪽 두 행을 제외하는 3..JC-2·3..IC-2로 고정되어 있다. 이 파일에는 n_ghost_rows 참조가 없다.
- 41–46: 셀 접근 조건은 L>0이다. 이 블록에는 L<=LCM 또는 NNoGhost<=LCM 검사가 없다.
