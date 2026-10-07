---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/subchan.f90
lines: 130
sha256: db2ac11446a8c122f9d1bbe1dd08db5f6a8fb04cb0e30d5a4b0a923cea9eddc5
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# subchan.f90 — 판독 구간 기록

구간은 1행부터 130행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | EFDC+·저작권·GPLv2 머리말(1–8). `SUBROUTINE SUBCHAN(QCHANUT,QCHANVT,IACTIVE,DE_T)` (9). 주석은 하위 격자 수로(subgrid channel) 상호작용을 계산하며 CALPUV2C/CALPUV9C에서 호출된다고 적는다(11–13). GLOBAL 사용·implicit none·NCHANM 크기의 IACTIVE/QCHANUT/QCHANVT와 지역변수 선언(15–23). RLAMN=QCHERR(25), `RLAMO = 1.-RLAMN` (26). |
| 28–55 | 시작 시 9행 SUBCHAN 안. `do NMD = 1,MDCHH` (28)에서 CCCCHU/CCCCHV/CCCCHH=0, LHOST/LCHNU/LCHNV 인덱스 복사(29–34). X 방향 `if( MDCHTYP(NMD) == 1 )then` (37)에서 IACTIVE=0, `SRFHOST = H1P(LHOST)+BELV(LHOST)` (39), `SRFCHAN = H1P(LCHNU)+BELV(LCHNU)` (40). `if( SRFCHAN > SRFHOST )then` (41)의 `if( H1P(LCHNU) > HDRY )then` (42)은 활성값 1(43). 별도 `if( SRFHOST > SRFCHAN )then` (46)의 `if( H1P(LHOST) > HDRY )then` (47)도 활성값 1(48). `if( HP(LHOST) <= 0.0 .or. HP(LCHNU) <= 0.0 )then` (51)의 `if( IACTIVE(NMD) == 1 )then` (52)은 활성값 0(53). |
| 56–68 | 시작 시 9행 SUBCHAN·28행 NMD 루프·37행 X 방향 분기 안. `if( IACTIVE(NMD) == 1 )then` (56)에서 WCHAN=DXP(LCHNU)(57), `RLCHN = 0.5*DYP(LCHNU)+CHANLEN(NMD)` (58), `HCHAN = 0.5*DYP(LCHNU)*H1P(LCHNU)+CHANLEN(NMD)*H1P(LHOST)` (59), `HCHAN = HCHAN/RLCHN` (60). `if( HCHAN > 0. )then` (61)에서 `TMPVAL = CHANFRIC(NMD)*DE_T/(HCHAN*HCHAN*WCHAN)` (62), `CCCCHU(NMD) = 1./(1.+TMPVAL*ABS(QCHANUT(NMD)))` (63), `CCCCHV(NMD) = DE_T*HCHAN*WCHAN/RLCHN` (64). 수심·활성·X 방향 분기 종료(65–67). |
| 69–94 | 시작 시 9행 SUBCHAN·28행 NMD 루프 안. Y 방향 `if( MDCHTYP(NMD) == 2 )then` (70)에서 IHCHMX/IHCHMN/IACTIVE=0(71–73), `SRFHOST = H1P(LHOST)+BELV(LHOST)` (74), `SRFCHAN = H1P(LCHNV)+BELV(LCHNV)` (75). `if( SRFCHAN > SRFHOST )then` (76)의 `if( H1P(LCHNV) > HDRY )then` (77)은 `HCHNMX = -H1P(LCHNV)` (78), IHCHMX=1·활성값 1(79–80). 별도 `if( SRFHOST > SRFCHAN )then` (83)의 `if( H1P(LHOST) > HDRY )then` (84)은 HCHNMN=H1P(LHOST)·IHCHMN=1·활성값 1(85–87). `if( HP(LHOST) <= 0.0 .or. HP(LCHNU) <= 0.0 )then` (90)의 `if( IACTIVE(NMD) == 1 )then` (91)은 활성값 0(92). |
| 95–109 | 시작 시 9행 SUBCHAN·28행 NMD 루프·70행 Y 방향 분기 안. `if( IACTIVE(NMD) == 1 )then` (95)에서 WCHAN=DYP(LCHNV)(96), `RLCHN = 0.5*DXP(LCHNV)+CHANLEN(NMD)` (97), `HCHAN = 0.5*DXP(LCHNV)*H1P(LCHNV)+CHANLEN(NMD)*H1P(LHOST)` (98), `HCHAN = HCHAN/RLCHN` (99). `if( IHCHMX == 1 ) HCHAN = max(HCHAN,HCHNMX)` (100), `if( IHCHMN == 1 ) HCHAN = min(HCHAN,HCHNMN)` (101). `if( HCHAN > 0. )then` (102)은 `TMPVAL = CHANFRIC(NMD)*DE_T/(HCHAN*HCHAN*WCHAN)` (103), `CCCCHU(NMD) = 1./(1.+TMPVAL*ABS(QCHANVT(NMD)))` (104), `CCCCHV(NMD) = DE_T*HCHAN*WCHAN/RLCHN` (105). 수심·활성·Y 방향 분기 종료(106–108). |
| 110–130 | 시작 시 9행 SUBCHAN·28행 NMD 루프 안. `CC(LHOST) = CC(LHOST)+G*RLAMN*RLAMN*CCCCHU(NMD)*CCCCHV(NMD)` (110), `CCCCHH(NMD)         = G*RLAMN*RLAMN*CCCCHU(NMD)*CCCCHV(NMD)` (111). `if( MDCHTYP(NMD) == 1 )then` (113)은 `CC(LCHNU) = CC(LCHNU)+G*RLAMN*RLAMN*CCCCHU(NMD)*CCCCHV(NMD)` (114), `TMPVAL = G*(RLAMO+RLAMN*CCCCHU(NMD))*QCHANUT(NMD) - G*RLAMN*RLAMO*CCCCHU(NMD)*CCCCHV(NMD)*(P1(LHOST) - P1(LCHNU))` (115), `FP(LHOST) = FP(LHOST)+TMPVAL` (116), `FP(LCHNU) = FP(LCHNU)-TMPVAL` (117). 별도 `if( MDCHTYP(NMD) == 2 )then` (120)은 `CC(LCHNV) = CC(LCHNV)+G*RLAMN*RLAMN*CCCCHU(NMD)*CCCCHV(NMD)` (121), `TMPVAL = G*(RLAMO+RLAMN*CCCCHU(NMD))*QCHANVT(NMD) - G*RLAMN*RLAMO*CCCCHU(NMD)*CCCCHV(NMD)*(P1(LHOST) - P1(LCHNV))` (122), `FP(LHOST) = FP(LHOST)+TMPVAL` (123), `FP(LCHNV) = FP(LCHNV)-TMPVAL` (124). NMD 루프 종료·return·END(127–130). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 70·75·77·90·96–99: Y 방향의 수위·수심·폭·길이 계산은 LCHNV를 쓴다. 90행의 비양수 수심 검사는 LCHNU를 쓴다.
- 78·100: HCHNMX는 -H1P(LCHNV)로 설정된다. 활성 Y 방향의 수심 제한은 max(HCHAN,HCHNMX)를 쓴다.
- 28–38·70–73·110–125: IACTIVE의 초기화는 유형 1·2 분기 안에만 있다. CCCCHU/CCCCHV/CCCCHH는 모든 NMD에서 먼저 0으로 설정된다. 이 파일에는 다른 유형에 대한 IACTIVE 대입이나 유형 오류 분기가 없다.
