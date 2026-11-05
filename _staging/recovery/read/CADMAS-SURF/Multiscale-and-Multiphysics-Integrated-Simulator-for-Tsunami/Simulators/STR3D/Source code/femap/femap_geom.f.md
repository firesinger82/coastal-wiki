---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/femap/femap_geom.f
lines: 62
sha256: d26f2885dcd25c5307a99141341274108ed5eaa7217d7a770334f256be059a23
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# femap_geom.f — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | FEMAP_GEOM은 M_VAL의 자료를 사용하여 FEMAP 기하(geometry) 파일을 쓴다. KK는 가변 길이 배열이다. BLK_S·BLK_E로 블록 100을 열고 닫으며 제품명과 버전 문자열 9.31을 기록한다. 원문: `      SUBROUTINE FEMAP_GEOM(KK,IFL)` (1); `      USE M_VAL` (3); `      DIMENSION KK(*)` (5); `!     --- HEADER ---` (7); `      CALL BLK_S(100,IFL)` (9); `      WRITE(IFL,'(A)') 'ASTEA MECHANICAL'` (11); `      WRITE(IFL,'(A)') '9.31,'` (13); `      CALL BLK_E(IFL)` (15) |
| 17–37 | 절점(node)은 KK(8)개를 FMP_NODE로 출력한다. 요소(element)는 KK(12)개를 FMP_ELEM으로 출력한다. 요소 호출의 32–33행은 고정형식 연속문이다. 각각 블록 번호는 403과 404이다. 원문: `!     --- NODES ---` (17); `      CALL BLK_S(403,IFL)` (19); `      DO I = 1, KK(8)` (21); `        CALL FMP_NODE(INDG(I),GRID(1,I),IFL)` (22); `      ENDDO` (23); `      CALL BLK_E(IFL)` (25); `!     --- ELEMENTS ---` (27); `      CALL BLK_S(404,IFL)` (29); `      DO I = 1, KK(12)` (31); `        CALL FMP_ELEM(KK(11),KK(15),IELM(1,I),IELM(2,I),IELM(4,I)` (32); `     &               ,IELM(5,I),IELM(3,I),IELM(8,I),INDG,IFL)` (33); `      ENDDO` (34); `      CALL BLK_E(IFL)` (36) |
| 38–62 | 속성(property) 블록 402에서 첫 KK(11)개는 유형 25로, 이후 KK(15)+KK(17)개는 유형 1로 FMP_PROP에 넘긴다. 재료(material) 블록 601은 같은 전체 범위에 FMP_MAT를 호출한다. 각 블록을 닫고 루틴을 끝낸다. 원문: `!     --- PROPERTIES ---` (38); `      CALL BLK_S(402,IFL)` (40); `      DO I = 1, KK(11)` (42); `        CALL FMP_PROP(I,25,IFL)` (43); `      ENDDO` (44); `      DO I = KK(11) + 1, KK(11) + KK(15) + KK(17)` (46); `        CALL FMP_PROP(I,1,IFL)` (47); `      ENDDO` (48); `      CALL BLK_E(IFL)` (50); `!     --- MATERIALS ---` (52); `      CALL BLK_S(601,IFL)` (54); `      DO I = 1, KK(11) + KK(15) + KK(17)` (56); `        CALL FMP_MAT(I,IFL)` (57); `      ENDDO` (58); `      CALL BLK_E(IFL)` (60); `      END` (62) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–13·43·47: 제품명·버전 문자열과 속성 유형 25·1을 이 루틴에서 고정하여 출력한다.
