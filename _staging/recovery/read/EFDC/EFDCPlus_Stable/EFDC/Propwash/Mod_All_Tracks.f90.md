---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Propwash/Mod_All_Tracks.f90
lines: 83
sha256: 70355c85b400607b2f07d92e517bc2c94b1c15efd92e2d536ab1f1b4a626b36a
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Mod_All_Tracks.f90 — 판독 구간 기록

구간은 1행부터 83행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | EFDC+·GPLv2·저작권 머리말(1–8), 위치 배열에 관한 주석(9–12). mod_all_tracks 시작(13), Mod_Position·Mod_Position_Cell·GLOBAL의 RKD/RK4 사용(15–17), implicit none(19). all_tracks 형식은 position_cell의 allocatable track_pos(:)와 기본값 0인 num_positions를 가진다(21–24). 형식 결합 절차(type bound procedure)는 get_start_time·get_end_time·del_all_tracks(26–30). 형식 종료·모듈 contains·빈 줄(32–34). 원문: `integer :: num_positions = 0 !> keeps track of the number of positions the current track` (24). |
| 35–50 | 시작 시 13행 mod_all_tracks 안. 최종 시각을 구한다는 주석(35–38), get_start_time 시작(39). 입력 self와 inout start_time 선언(44–45). 첫 항적 점의 time을 start_time에 복사(47). 루틴 종료·빈 줄(49–50). 원문: `real(kind = RKD), intent(inout) :: start_time` (45); `start_time = self.track_pos(1).time` (47). |
| 51–68 | 시작 시 13행 mod_all_tracks 안. 최종 시각 목적 주석과 get_end_time 시작(51–55). 입력 self와 inout final_time 선언(60–61). track_pos(self.num_positions).time을 final_time에 복사(64). 루틴 종료·빈 줄(67–68). 원문: `real(kind = RKD), intent(inout) :: final_time !> final time for a given track` (61); `final_time = self.track_pos( self.num_positions ).time` (64). |
| 69–83 | 시작 시 13행 mod_all_tracks 안. 항적 배열 해제 주석과 del_all_tracks 시작(69–73). inout self 선언(77), deallocate(self.track_pos)(79). 루틴 종료·모듈 종료·빈 줄(81–83). 이 파일에는 조건 분기가 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 36·39·47: get_start_time의 목적 주석은 최종 시각으로 적는다. 실행문은 track_pos(1).time을 복사한다.
- 24·47·64: num_positions 기본값은 0이다. 두 시각 조회 루틴에는 track_pos 할당 여부나 num_positions 범위 검사 없이 배열을 참조하는 대입문이 있다.
