---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/main/part_surf.f
lines: 16
sha256: 62f299a563755cd1a230ddc048d7009fc3a21ff320d55e5ae826581f59493011
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# part_surf.f — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | PART_SURF는 IPFC(1,I)를 IE에 복사한다(5–7). 해석: IPFC는 압력 면 목록이며 첫 성분은 소속 요소 번호로 읽는다. 요소의 유형과 재료를 읽고 유형이 2 또는 6일 때 IP_ENS(I)에 재료 번호를 저장한다(9–12). 전 압력 면을 순회하고 루틴을 종료한다(14–16). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE PART_SURF( IP_ENS, IELM, IPFC, NM, NPFC )` (1) <br> `      DIMENSION IP_ENS(*), IPFC(10,NPFC), IELM(NM,*)` (3) <br> `      DO I = 1, NPFC` (5) <br> `        IE = IPFC(1,I)` (7) <br> `        ITYP = IELM(2,IE)` (9) <br> `        IMAT = IELM(4,IE)` (10) <br> `        IF( ITYP == 2 .OR. ITYP == 6 ) IP_ENS(I) = IMAT` (12) <br> `      ENDDO` (14) <br> `      END` (16) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12: 유형 2·6 이외의 IP_ENS(I)에 값을 설정하는 ELSE 분기나 전체 초기화가 이 파일에 없다.
