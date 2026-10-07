---
file: models/EFDC/raw/source_code/EFDC-GVC/depsmth.for
lines: 172
sha256: 43d1316fcfbc61482665aef4fccee46d5bfde537e1cb5cd8e663dd3d00cb797b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# depsmth.for — 판독 구간 기록

구간은 1행부터 172행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | 구분 주석과 `SUBROUTINE DEPSMTH` (6) 입구. EFDC-FULL 1.0a·2001-11-01 수정 표기, 빈 변경 이력 양식(8–17). EFDC.PAR·EFDC.CMN 포함(21–22). 구분 주석 포함. |
| 26–59 | 시작 시 6행 DEPSMTH 루틴 안. `IF(WSMH.GT.0.) GOTO 1000` (26)은 양의 WSMH에서 94행 표지로 이동한다. 이동하지 않는 경로는 바닥 표고(bottom elevation) 평활화(smoothing) 표제(28)와 `WSMH=-WSMH` (30). NSM=1..NSHMAX 바깥 루프(32)의 첫 L=2..LA 루프(34)에서 `IF(LCT(L).GT.0.AND.LCT(L).LT.9)THEN` (35), I/J 복사(36–37), 북·남 BELV를 HTN/HTS에 복사(38–39). `IF(IJCT(I,J+1).EQ.9) HTN=BELV(L)` (40); `IF(IJCT(I,J-1).EQ.9) HTS=BELV(L)` (41); `HTMP(L)=(1.-WSMH)*BELV(L)+0.5*WSMH*(HTN+HTS)` (42). 두 번째 L 루프(46)에서 `IF(LCT(L).GT.0.AND.LCT(L).LT.9)THEN` (47), I/J·동서 HTMP 복사(48–51), `IF(IJCT(I+1,J).EQ.9) HTE=HTMP(L)` (52); `IF(IJCT(I-1,J).EQ.9) HTW=HTMP(L)` (53); `BELV(L)=(1.-WSMH)*HTMP(L)+0.5*WSMH*(HTE+HTW)` (54). 남북 평균 뒤 동서 평균을 적용한다. 조건·루프 종료·주석(43–45·55–59). |
| 60–93 | 시작 시 6행 DEPSMTH 루틴 안. 26행 조건에서 1000 표지로 이동하지 않은 경로. 수심(depth) 평활화 표제(60), NSM=1..NSHMAX(62). 첫 L=2..LA 루프(64)에서 `IF(LCT(L).GT.0.AND.LCT(L).LT.9)THEN` (65), I/J·북남 HMP 복사(66–69), `IF(IJCT(I,J+1).EQ.9) HTN=HMP(L)` (70); `IF(IJCT(I,J-1).EQ.9) HTS=HMP(L)` (71); `HTMP(L)=(1.-WSMH)*HMP(L)+0.5*WSMH*(HTN+HTS)` (72). 두 번째 L 루프(76)에서 `IF(LCT(L).GT.0.AND.LCT(L).LT.9)THEN` (77), I/J·동서 HTMP 복사(78–81), `IF(IJCT(I+1,J).EQ.9) HTE=HTMP(L)` (82); `IF(IJCT(I-1,J).EQ.9) HTW=HTMP(L)` (83); `HMP(L)=(1.-WSMH)*HTMP(L)+0.5*WSMH*(HTE+HTW)` (84). 남북 평균 뒤 동서 평균을 적용한다. 종료·주석(73–75·85–89), GOTO 2000(90)은 양의 WSMH용 블록을 건너뛴다. 구분 주석(91–93). |
| 94–125 | 시작 시 6행 DEPSMTH 루틴 안. 1000 CONTINUE 표지(94), 바닥 표고 평활화 표제(96). L=2..LA에 HTMP=BELV 복사(98–100). NSM=1..NSHMAX(102)·L=2..LA(104)에서 `IF(LCT(L).GT.0.AND.LCT(L).LT.9)THEN` (105), I/J·북남동서 HTMP 복사(106–111). `IF(IJCT(I  ,J+1).EQ.9) HTN=HTMP(L)` (112); `IF(IJCT(I  ,J-1).EQ.9) HTS=HTMP(L)` (113); `IF(IJCT(I+1,J  ).EQ.9) HTE=HTMP(L)` (114); `IF(IJCT(I-1,J  ).EQ.9) HTW=HTMP(L)` (115); `BELV(L)=(1.-WSMH)*HTMP(L)+0.25*WSMH*(HTN+HTS+HTE+HTW)` (116). IJCT=9인 이웃은 자기 값으로 대체하고 네 이웃에 각각 0.25*WSMH 가중치를 준다. 조건·L 루프 종료(117–118), HTMP=BELV 재복사 루프(120–122), NSM 루프 종료·주석(124–125). |
| 126–157 | 시작 시 6행 DEPSMTH 루틴 안. 수심 평활화 표제(126). L=2..LA에 HTMP=HMP 복사(128–130). NSM=1..NSHMAX(132)·L=2..LA(134)에서 `IF(LCT(L).GT.0.AND.LCT(L).LT.9)THEN` (135), I/J·북남동서 HTMP 복사(136–141). `IF(IJCT(I  ,J+1).EQ.9) HTN=HTMP(L)` (142); `IF(IJCT(I  ,J-1).EQ.9) HTS=HTMP(L)` (143); `IF(IJCT(I+1,J  ).EQ.9) HTE=HTMP(L)` (144); `IF(IJCT(I-1,J  ).EQ.9) HTW=HTMP(L)` (145); `HMP(L)=(1.-WSMH)*HTMP(L)+0.25*WSMH*(HTN+HTS+HTE+HTW)` (146). 조건·L 루프 종료(147–148), HTMP=HMP 재복사 루프(150–152), NSM 루프 종료와 구분 주석(154–157). |
| 158–172 | 시작 시 6행 DEPSMTH 루틴 안. 2000 CONTINUE 표지(158). NEWDXDY.INP을 장치 1로 열고 삭제한 뒤 다시 연다: `OPEN(1,FILE='NEWDXDY.INP',STATUS='UNKNOWN')` (160); `CLOSE(1,STATUS='DELETE')` (161); `OPEN(1,FILE='NEWDXDY.INP',STATUS='UNKNOWN')` (162). L=2..LA(163)에 `WRITE(1,339)IL(L),JL(L),DXP(L),DYP(L),HMP(L),BELV(L),` (164); `&              ZBR(L)` (165)로 I/J·DXP/DYP·HMP/BELV·ZBR 출력. 종료·CLOSE(1)(166–167), FORMAT 339의 2개 I5와 5개 E12.4 및 간격(169), 주석·RETURN·END(168–172). 외부 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26–30·158–172: 양의 WSMH는 1000 표지로 이동한다. 그 밖의 경로는 WSMH=-WSMH를 실행한다. 이 파일에는 반환 전에 원래 WSMH 부호로 복원하는 대입이 없다.
- 42·54·72·84·116·146: 평균 가중치에는 WSMH를 그대로 사용한다. 이 파일에는 WSMH 범위를 검사하거나 제한하는 조건이 없다.
- 34–54·64–84·98–100·128–130: 처음 두 방향별 평활화 경로는 LCT>0이고 LCT<9인 셀에만 HTMP를 대입한다. 1000 표지 뒤 경로는 먼저 L=2..LA 전체에 HTMP를 복사한다. 이 파일에는 방향별 경로 입구의 HTMP 전체 초기화문이 없다.
- 160–162: 출력 준비는 NEWDXDY.INP을 연 뒤 STATUS='DELETE'로 닫고 같은 이름으로 다시 여는 순서이다. 이 판독에서는 루틴을 실행하지 않았다.

