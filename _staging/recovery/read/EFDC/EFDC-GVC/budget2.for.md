---
file: models/EFDC/raw/source_code/EFDC-GVC/budget2.for
lines: 158
sha256: 790f15522e1e3aa3f0679f7d77c9bca0f8cb4171092c17b629aaa73f6660aea4
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# budget2.for — 판독 구간 기록

구간은 1행부터 158행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | BUDGET2 입구와 작성자·버전·수정 이력(6–19). 전체 퇴적물(sediment) 수지(budget) 목적(23). EFDC.PAR·EFDC.CMN 포함(27–28). 개방 경계(open boundary) 플럭스(flux) 누적 주석(32–35). |
| 36–62 | 시작 시 6행 BUDGET2 루틴 안. 수층(water column) K=1..KC·남쪽 경계 LL=1..NCBS를 반복한다(36–39). L=LCBS·LN=LNC를 사용한다(38–39). VHDX2(LN,K)*DZC를 VOLMOUT에서 뺀다(41). MIN·MAX로 유속 부호에 따라 SAL1의 LN 또는 L 값을 골라 SMASSOUT에 반영한다(42–43). NSED·NSND별 SED1·SND1도 같은 부호 방식으로 SEDOUT에 반영한다(49–59). 원문: `L=LCBS(LL)` (38). `LN=LNC(L)` (39). `VOLMOUT=VOLMOUT-VHDX2(LN,K)*DZC(K)` (41). `SMASSOUT=SMASSOUT-MIN(VHDX2(LN,K),0.)*SAL1(LN,K)*DZC(K)` (42); `&             -MAX(VHDX2(LN,K),0.)*SAL1(L,K)*DZC(K)` (43). `SEDOUT=SEDOUT-MIN(VHDX2(LN,K),0.)*SED1(LN,K,NT)*DZC(K)` (50); `&               -MAX(VHDX2(LN,K),0.)*SED1(L,K,NT)*DZC(K)` (51). `SEDOUT=SEDOUT-MIN(VHDX2(LN,K),0.)*SND1(LN,K,NT)*DZC(K)` (54); `&               -MAX(VHDX2(LN,K),0.)*SND1(L,K,NT)*DZC(K)` (55). |
| 63–87 | 시작 시 6행 BUDGET2 루틴 안. K=1..KC·서쪽 경계 LL=1..NCBW·L=LCBW를 반복한다(63–65). UHDY2(L+1,K)*DZC를 VOLMOUT에서 뺀다(67). MIN·MAX에 따라 L+1 또는 L의 SAL1·SED1·SND1을 사용해 염분(salt)과 퇴적물 질량 플럭스를 더한다(68–84). 원문: `L=LCBW(LL)` (65). `VOLMOUT=VOLMOUT-UHDY2(L+1,K)*DZC(K)` (67). `SMASSOUT=SMASSOUT-MIN(UHDY2(L+1,K),0.)*SAL1(L+1,K)*DZC(K)` (68); `&             -MAX(UHDY2(L+1,K),0.)*SAL1(L,K)*DZC(K)` (69). `SEDOUT=SEDOUT-MIN(UHDY2(L+1,K),0.)*SED1(L+1,K,NT)*DZC(K)` (75); `&               -MAX(UHDY2(L+1,K),0.)*SED1(L,K,NT)*DZC(K)` (76). `SEDOUT=SEDOUT-MIN(UHDY2(L+1,K),0.)*SND1(L+1,K,NT)*DZC(K)` (79); `&               -MAX(UHDY2(L+1,K),0.)*SND1(L,K,NT)*DZC(K)` (80). |
| 88–111 | 시작 시 6행 BUDGET2 루틴 안. K=1..KC·동쪽 경계 LL=1..NCBE·L=LCBE를 반복한다(88–90). UHDY2(L,K)*DZC를 VOLMOUT에 더한다(92). MIN은 L의 이전 농도, MAX는 L-1의 이전 농도를 사용한다(93–104). 종류별 수송량과 경계 루프가 끝난다(105–108). 원문: `L=LCBE(LL)` (90). `VOLMOUT=VOLMOUT+UHDY2(L,K)*DZC(K)` (92). `SMASSOUT=SMASSOUT+MIN(UHDY2(L,K),0.)*SAL1(L,K)*DZC(K)` (93); `&             +MAX(UHDY2(L,K),0.)*SAL1(L-1,K)*DZC(K)` (94). `SEDOUT=SEDOUT+MIN(UHDY2(L,K),0.)*SED1(L,K,NT)*DZC(K)` (99); `&               +MAX(UHDY2(L,K),0.)*SED1(L-1,K,NT)*DZC(K)` (100). `SEDOUT=SEDOUT+MIN(UHDY2(L,K),0.)*SND1(L,K,NT)*DZC(K)` (103); `&               +MAX(UHDY2(L,K),0.)*SND1(L-1,K,NT)*DZC(K)` (104). |
| 112–136 | 시작 시 6행 BUDGET2 루틴 안. K=1..KC·북쪽 경계 LL=1..NCBN을 반복한다(112–113). L=LCBN·LS=LSC를 정한다(114–115). VHDX2(L,K)*DZC를 VOLMOUT에 더한다(117). MIN은 L, MAX는 LS의 SAL1·SED1·SND1을 사용해 염분·퇴적물 플럭스를 반영한다(118–133). 원문: `L=LCBN(LL)` (114). `LS=LSC(L)` (115). `VOLMOUT=VOLMOUT+VHDX2(L,K)*DZC(K)` (117). `SMASSOUT=SMASSOUT+MIN(VHDX2(L,K),0.)*SAL1(L,K)*DZC(K)` (118); `&             +MAX(VHDX2(L,K),0.)*SAL1(LS,K)*DZC(K)` (119). `SEDOUT=SEDOUT+MIN(VHDX2(L,K),0.)*SED1(L,K,NT)*DZC(K)` (124); `&               +MAX(VHDX2(L,K),0.)*SED1(LS,K,NT)*DZC(K)` (125). `SEDOUT=SEDOUT+MIN(VHDX2(L,K),0.)*SND1(L,K,NT)*DZC(K)` (128); `&               +MAX(VHDX2(L,K),0.)*SND1(LS,K,NT)*DZC(K)` (129). |
| 137–158 | 시작 시 6행 BUDGET2 루틴 안. 주석은 하상(sediment bed)에서 수층으로의 양의 퇴적물 플럭스 누적을 설명한다(137). SEDF·SNDF를 VOLBW3에 더하는 두 종류·K·L 루프는 전부 주석 처리되어 있다(139–153). 마지막 주석·RETURN·END로 끝난다(154–158). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41–43·50–55·67–80·92–104·117–129: 경계 누적식에는 DT 또는 DELT 곱셈이 없다. 이 파일은 UHDY2·VHDX2의 정의를 포함하지 않는다.
- 137–153: 하상·수층 교환량 VOLBW3 누적 블록은 전부 주석이다.
- 1–158: 이 파일에는 NBUD 또는 ISTRAN을 검사하는 조건문이 없다. 네 경계 집계는 해당 경계 수와 종류 수 반복 범위로 실행 여부를 정한다.

