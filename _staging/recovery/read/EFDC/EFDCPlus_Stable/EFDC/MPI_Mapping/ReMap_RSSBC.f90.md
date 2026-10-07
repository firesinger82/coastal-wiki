---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Mapping/ReMap_RSSBC.f90
lines: 113
sha256: feda3dbf1bbc89e562bc5eb227cd9a6666e5887fb6d906954c7c479446756172
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# ReMap_RSSBC.f90 — 판독 구간 기록

구간은 1행부터 113행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–46 | EFDC+ 출처·저작권·GPLv2 머리말(1–8). SETBCS에서 지역(local) RSSBC* 값을 전역(global) 값으로 옮긴다는 설명·저자·변경 기록 주석(9–24). `ReMap_RSSBC` 시작(25). GLOBAL·MPI 변수·출력·매핑 및 Mod_Map_Soln·Mod_Gather_Soln·Mod_Sort_Global_Soln 사용(27–33). implicit none(35). 기본 Real의 Local_1D·Global_1D, integer 매핑 배열 두 개와 지역 정수 선언(39–45). 빈 줄 포함. |
| 47–58 | 시작 시 25행 ReMap_RSSBC 루틴 안. 지역 해·Mapping_Local은 LA_Local_no_ghost 크기로 할당한다(48·50). 전역 해·Mapping_Global은 LCM_Global 크기로 할당한다(49·51). 두 해를 0.0, 두 매핑을 0으로 초기화한다(53–57). |
| 59–72 | 시작 시 25행 ReMap_RSSBC 루틴 안. 동쪽 RSSBCE 처리 주석(59–61). `Map_Soln(LCM, RSSBCE, LA_Local_no_ghost, Local_1D, Mapping_Local)` 호출(62). `Gather_Soln(LA_Local_no_ghost, Local_1D, LCM_Global, Global_1D, Mapping_Local, Mapping_Global )` 호출(64). `Sort_Global_Soln(LCM_Global, LCM_Global, Global_1D, Mapping_Global, RSSBCE_Global)` 호출(66). 세 호출에 조건 분기는 없다. 네 임시 배열을 다시 0으로 초기화한다(68–71). |
| 73–85 | 시작 시 25행 ReMap_RSSBC 루틴 안. 서쪽 RSSBCW의 `Map_Soln` 호출은 LCM 크기 입력과 LA_Local_no_ghost 크기 출력을 전달한다(73–75). `Gather_Soln` 호출은 지역/전역 해와 매핑을 전달한다(77). `Sort_Global_Soln` 호출의 두 크기 인수는 LCM_Global이며 결과는 RSSBCW_Global이다(79). 네 임시 배열을 다시 0으로 초기화한다(81–84). 주석·빈 줄 포함. |
| 86–98 | 시작 시 25행 ReMap_RSSBC 루틴 안. 북쪽 RSSBCN의 `Map_Soln` 호출(88), 같은 지역/전역 크기의 `Gather_Soln` 호출(90), RSSBCN_Global을 대상으로 하는 `Sort_Global_Soln` 호출(92). 네 임시 배열을 다시 0으로 초기화한다(94–97). 북쪽 처리·수집·정렬 주석과 빈 줄 포함(86–98). |
| 99–113 | 시작 시 25행 ReMap_RSSBC 루틴 안. 남쪽 RSSBCS의 `Map_Soln` 호출(101), 같은 지역/전역 크기의 `Gather_Soln` 호출(103), RSSBCS_Global을 대상으로 하는 `Sort_Global_Soln` 호출(105). 끝 주석 뒤 Local_1D·Global_1D·Mapping_Local·Mapping_Global을 해제한다(107–111). 루틴 종료·빈 줄(112–113). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 44–45: num_active_l_local_1d·l은 선언 뒤 이 파일에서 사용되지 않는다.
- 62–66·75–79·88–92·101–105: 네 방향 모두 Map_Soln·Gather_Soln·Sort_Global_Soln을 조건 없이 호출한다. 이 루틴에는 process_id 또는 master_id 조건식이 없다.
- 63–64·76–77·89–90·102–103: 수집 앞 주석은 gather 3d와 둘째 변수의 값 1을 적는다. 실제 Gather_Soln 호출은 여섯 인수를 전달하며 리터럴 1을 전달하지 않는다.
