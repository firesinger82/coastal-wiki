---
file: models/EFDC/raw/source_code/EFDC-GVC/rsurfplt.for
lines: 82
sha256: b2a2407926d61f07bfb0d9f8385a7e948d0ee2bf10f31b134fd34aae15a8b66e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# rsurfplt.for — 판독 구간 기록

구간은 1행부터 82행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | 머리말과 `SUBROUTINE RSURFPLT` (6). 버전·수정일·변경 이력 주석(8–17). 목적 주석은 SURFPLT라는 이름과 자유수면 표고(free surface elevation) 등치선(contour) 파일 작성을 적는다(19–20). EFDC.PAR·EFDC.CMN 포함(24–25), 80자 TITLE 선언(29). 구분 주석 포함. 포함 파일 내부는 판독하지 않았다. |
| 33–51 | 시작 시 6행 RSURFPLT 안. `IF(JSRPPH.NE.1) GOTO 300` (33)이면 초기화를 건너뛴다. 초기화 경로는 RSURFCN.OUT을 단위 10에서 열고 삭제 후 재개방한다(35–37). 제목은 INSTANTANEOUS SURFACE ELEVATION CONTOURS(38). `LINES=LA-1` (40), `LEVELS=1` (41), `DBS=0.` (42). 제목·LINES·LEVELS·DBS 기록 후 CLOSE·JSRPPH=0(44–48). 공통 도착 라벨 300·주석(49–51). |
| 52–68 | 시작 시 6행 RSURFPLT 안. `IF(ISDYNSTP.EQ.0)THEN` (52): `TIME=DT*FLOAT(N)+TCON*TBEGIN` (53), `TIME=TIME/TCON` (54). `ELSE` (55): `TIME=TIMESEC/TCON` (56). 파일을 append로 열어 N·TIME을 쓴다(59–60). L=2..LA에서 `SURFEL=HLPF(L)+BELV(L)` (63), IL·JL·DLON·DLAT·SURFEL 출력(64). 루프 종료·파일 CLOSE·주석(65–68). |
| 69–82 | 시작 시 6행 RSURFPLT 안. 구분 주석(69–70). FORMAT 99는 A80, 100은 I10·F12.4, 101은 2I10, 200은 2I5·1X·6E14.6, 250은 12E12.4(71–75). CMRM 대안 FORMAT은 주석(76–77). 구분 주석·RETURN·END(78–82). 이 파일에는 서브루틴 CALL이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·19·38·63: 루틴 이름은 RSURFPLT이다. 목적 주석은 SURFPLT를 적고 출력 제목은 INSTANTANEOUS를 적는다. 실제 표고 계산은 HLPF(L)+BELV(L)이다.
- 40–45·72–73: LINES·LEVELS를 쓰는 머리말은 FORMAT 100의 I10·F12.4를 사용한다. 두 정수용 FORMAT 101은 선언되어 있으나 이 파일의 WRITE에서 사용되지 않는다.
