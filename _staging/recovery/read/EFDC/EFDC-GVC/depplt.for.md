---
file: models/EFDC/raw/source_code/EFDC-GVC/depplt.for
lines: 67
sha256: a42204e8274e1ead6016575afb7c0c56e39417330a5d32cfee367a8ababd4963
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# depplt.for — 판독 구간 기록

구간은 1행부터 67행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | 구분 주석과 `SUBROUTINE DEPPLT` (6) 선언. 수심 등치선(depth contour) 출력 목적 주석(8), EFDC-FULL 1.0a·2001-11-01 수정 표기(10–12), 빈 변경 이력 양식(16–19). EFDC.PAR·EFDC.CMN 포함(23–24), 길이 80 문자열 TITLE 선언(28). 구분 주석 포함. |
| 32–54 | 시작 시 6행 DEPPLT 루틴 안. BELVCON.OUT을 장치 1로 열고 삭제한 뒤 다시 연다: `OPEN(1,FILE='BELVCON.OUT',STATUS='UNKNOWN')` (32); `CLOSE(1,STATUS='DELETE')` (33); `OPEN(1,FILE='BELVCON.OUT',STATUS='UNKNOWN')` (34). TITLE='BOTTOM ELEVATION CONTOURS'(36). 출력 머리값 `NTIME=1` (38); `LINES=LA-1` (39); `LEVELS=1` (40); `DBS=0.` (41). TITLE·LINES/LEVELS·DBS·NTIME를 각각 FORMAT 99/101/250/100으로 쓴다(43–47). L=2..LA 루프(49)에서 `WRITE(1,200)IL(L),JL(L),DLON(L),DLAT(L),BELV(L)` (50)로 I/J·DLON/DLAT·BELV 출력. 루프 종료·CLOSE(1)·주석(51–54). |
| 55–67 | 시작 시 6행 DEPPLT 루틴 안. 구분 주석(55–56). FORMAT 99=A80, 100=I10, 101=2I10(57–59). 셀 자료 FORMAT `200 FORMAT(2I4,1X,2F15.3,F10.3)` (60), 대체 FORMAT은 주석(61). DBS FORMAT `250 FORMAT(12F10.6)` (62). 끝 구분 주석·RETURN·END(63–67). 조건 분기·외부 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8·36·50: 목적 주석은 수심 등치선 출력이라고 적는다. 출력 제목은 BOTTOM ELEVATION CONTOURS이며 셀별 출력 값은 BELV(L)이다.
- 32–34: 출력 준비는 BELVCON.OUT을 연 뒤 STATUS='DELETE'로 닫고 같은 이름으로 다시 여는 순서이다. 이 판독에서는 루틴을 실행하지 않았다.

