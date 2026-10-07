---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Mapping/Setup_MapBackToGlobal.f90
lines: 45
sha256: 44aad5967e7348a7cabd932b7e07bdf300e35b05456041c72d62f66f2d691dcf
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Setup_MapBackToGlobal.f90 — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | EFDC+ 출처·저작권·GPLv2 머리말(1–8). 고스트 셀(ghost cell)을 제외한 유효 L 인덱스의 시작·끝을 알아낸다는 설명과 저자·날짜 주석(9–18). 빈 줄 포함. |
| 20–32 | `Get_LA_Local_No_Ghost()` 시작(20). GLOBAL·Variables_MPI·Variables_MPI_Mapping·MPI 사용(22–25). implicit none(27). 지역 정수 I·J·L 및 ierr 선언(29–31). 빈 줄 포함. |
| 33–45 | 시작 시 20행 Get_LA_Local_No_Ghost 루틴 안. L=0(33). `do J = 3,JC-2` (34), `do I = 3,IC-2` (35). `if( LIJ(I,J) > 0 )then` (36)이면 `L = L + 1` (37). 조건·루프 종료(38–40). 고스트 영역 밖 활성 셀(active cell) 수라는 주석(42)과 LA_Local_no_ghost=L 대입(43). 루틴 종료·빈 줄(44–45). 외부 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 25·31: MPI 모듈을 사용하고 ierr를 선언하지만 이 파일에는 MPI 호출이나 ierr 참조가 없다.
- 34–35: 반복 범위는 각 방향에서 3부터 IC/JC-2까지이다. 고스트 셀 제외 폭을 정하는 상수 3·2는 실행문에 직접 적혀 있다.
- 12–13·33–43: 설명 주석은 유효 L 인덱스의 시작·끝을 알아낸다고 적는다. 실행문은 LIJ>0인 셀 수를 세어 LA_Local_no_ghost에 저장한다.
