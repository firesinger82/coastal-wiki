---
file: models/EFDC/raw/source_code/EFDC-GVC/partmix.for
lines: 195
sha256: 3f65da1a5849c5f7edfcfaf8873d5beae8f978a955bb5620a45e3d34bae1e70b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# partmix.for — 판독 구간 기록

구간은 1행부터 195행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | 구분 주석과 `SUBROUTINE PARTMIX(NT)` 입구(1–6). EFDC-FULL 1.0a·수정일·변경 이력 주석(8–16). 비점착성 퇴적물(noncohesive sediment)의 침강(settling)·퇴적(deposition)·재부유(resuspension)를 계산하는 CALSND라는 설명 주석(20–21). EFDC.PAR·EFDC.CMN 포함(25–26). PMC COMMON과 TMPVAL/DSTAR/CCUSTAR 선언은 czzdiff 주석이다(28–31). 포함 파일 내부는 판독하지 않았다. |
| 33–77 | 시작 시 6행 PARTMIX 안. SSEDTOX1에는 셀별 전단(shear)·속도·유량(flow rate)·독성물질(toxicant) 수지 작업 배열과 종류별 SEDFPA/SNDFPA를 선언한다(33–42). SSEDTOX1A는 퇴적층(sediment bed) 분율·전단·유량 작업 배열이다(44–46). SSEDTOX2는 수층/퇴적층 감쇠(decay)·응력(stress)·수리(hydraulic)·압력(pressure)·입경(particle diameter) 작업 배열이다(48–55). SSEDTOX3은 층 연립계 작업 배열이며 일부 배열은 0:KBM 범위를 갖는다(57–60). SSEDTOX4는 침강 및 수층/퇴적층 농도 배열이다(62–65). SSEDTOX5는 NSP2·DERRB·STRESSS(0:KSM), SSEDTOX6은 시간·입경 계수, SSEDTOX7은 ISTL/IS2TL/ISUD를 선언한다(67–72). PARTMIXAVG(KBM)와 구분 주석을 포함한다(74–77). |
| 78–89 | 시작 시 6행 PARTMIX 안. K=1..KB·L=2..LA 루프에서 PARTMIXZ를 0으로 초기화한다(78–82). 이전 입자 혼합(particle mixing) 방식의 옵션은 ISPMXZ=2라는 주석(86). `IF(ISPMXZ(NT).EQ.2)THEN` (88)을 연다. |
| 90–108 | 시작 시 6행 PARTMIX·88행 ISPMXZ(NT)=2 분기 안. L 루프에서 DEPINBED=0·LZ=LPMXZ(L)을 설정한다(90–92). `IF(KBT(L).GT.2)THEN` (93)의 K=KBT(L)..2 내림차순 루프(94)에서 `KM=K-1` (95), `DEPINBED=DEPINBED+HBED(L,K)` (96). ND=1..NPMXPTS−1 루프(97)의 `NDP=ND+1` (98), `IF(DEPINBED.GE.PMXDEPTH(ND,LZ).AND.` (99), `&           DEPINBED.LT.PMXDEPTH(NDP,LZ))THEN` (100)에서 하한 포함·상한 제외 깊이 구간을 찾는다. 보간식은 `WT1=DEPINBED-PMXDEPTH(ND,LZ)` (101), `WT2=PMXDEPTH(NDP,LZ)-DEPINBED` (102), `TMPVAL=PMXDEPTH(ND+1,LZ)-PMXDEPTH(ND,LZ)` (103), `PARTMIXZ(L,KM)=(WT2*PMXCOEF(ND,LZ)` (104), `&                        +WT1*PMXCOEF(NDP,LZ))/TMPVAL` (105). ND·K 루프를 닫는다(107–108). |
| 109–126 | 시작 시 6행 PARTMIX·88행 옵션 2·90행 L 루프·93행 KBT>2 조건 안. `ELSE` (109)에서는 K=KBT(L)을 사용하고 `KM=K-1` (111), `DEPINBED=DEPINBED+HBED(L,K)` (112)를 계산한다. ND 루프(113)의 `NDP=ND+1` (114) 뒤 조건은 `IF(DEPINBED.GE.PMXDEPTH(ND,LZ).AND.` (115), `&         DEPINBED.LT.PMXDEPTH(NDP,LZ))THEN` (116). 식은 `WT1=DEPINBED-PMXDEPTH(ND,LZ)` (117), `WT2=PMXDEPTH(NDP,LZ)-DEPINBED` (118), `TMPVAL=PMXDEPTH(ND+1,LZ)-PMXDEPTH(ND,LZ)` (119), `PARTMIXZ(L,KM)=(WT2*PMXCOEF(ND,LZ)` (120), `&                        +WT1*PMXCOEF(NDP,LZ))/TMPVAL` (121). 조건·ND 루프·KBT 분기·L 루프를 닫는다(122–125). |
| 127–140 | 시작 시 6행 PARTMIX·88행 옵션 2 분기 안. L·K=KBT(L)..2 내림차순 루프(127–128)에서 `KM=K-1` (129), `PARTMIXZ(L,KM)=2.*PARTMIXZ(L,KM)/` (130), `&      (2.0-TOXPFTB(L,K,NT)-TOXPFTB(L,KM,NT))` (131)로 혼합 계수를 보정한다. 루프와 옵션 2 조건을 닫는다(132–135). 새 혼합 방식의 옵션은 ISPMXZ=1이라는 주석과 구분 주석을 포함한다(137–140). |
| 141–170 | 시작 시 6행 PARTMIX 안. `IF(ISPMXZ(NT).EQ.1)THEN` (141)의 L 루프에서 LZ를 찾고 K=1..KB의 PARTMIXAVG/PARTMIXZ를 0으로 초기화한다(143–149). DEPINBED=0 뒤 K=KBT(L)..1 내림차순 루프(151–152)의 `DELHBED=HBED(L,K)/10.` (153)을 계산한다. KK=1..10 루프(154)의 `DEPINBED=DEPINBED+DELHBED` (155). ND 루프의 `NDP=ND+1` (157), `IF(DEPINBED.GE.PMXDEPTH(ND,LZ).AND.` (158), `&          DEPINBED.LT.PMXDEPTH(NDP,LZ))THEN` (159)에서 구간을 찾는다. 식은 `WT1=DEPINBED-PMXDEPTH(ND,LZ)` (160), `WT2=PMXDEPTH(NDP,LZ)-DEPINBED` (161), `TMPVAL=PMXDEPTH(ND+1,LZ)-PMXDEPTH(ND,LZ)` (162), `PARTMIXAVG(K)=PARTMIXAVG(K)` (163), `&             +(WT2*PMXCOEF(ND,LZ)+WT1*PMXCOEF(NDP,LZ))/TMPVAL` (164). ND·KK 루프 뒤 `PARTMIXAVG(K)=PARTMIXAVG(K)/10.` (168)로 평균한다. K 루프를 닫는다(169). |
| 171–179 | 시작 시 6행 PARTMIX·141행 옵션 1·143행 L 루프 안. K=1..KBT(L)−1 루프(171)의 `TERM1=HBED(L,K)/PARTMIXAVG(K)` (172), `TERM2=HBED(L,K+1)/PARTMIXAVG(K+1)` (173), `TERM3=HBED(L,K)+HBED(L,K+1)` (174), `PARTMIXZ(L,K)=TERM3/(TERM1+TERM2)` (175)로 인접 층 계수를 결합한다. K·L 루프를 닫는다(176–178). |
| 180–195 | 시작 시 6행 PARTMIX·141행 옵션 1 분기 안. L·K=KBT(L)..2 내림차순 루프(180–181)의 `KM=K-1` (182), `PARTMIXZ(L,KM)=2.*PARTMIXZ(L,KM)/` (183), `&      (2.0-TOXPFTB(L,K,NT)-TOXPFTB(L,KM,NT))` (184)로 계수를 보정한다. 루프·빈 줄·옵션 1 조건을 닫는다(185–189). 구분 주석·RETURN·END·마지막 주석으로 끝난다(190–195). 외부 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·20–21: 루틴 이름은 PARTMIX이다. 설명 주석은 CALSND와 SSEDTOX 호출을 적고 있다.
- 99–105·115–121·158–164: 깊이 구간 조건은 하한 포함·상한 제외이다. PMXDEPTH의 마지막 점과 같은 깊이를 별도 처리하는 조건은 이 파일에 없다.
- 153–168: 새 방식은 각 층을 고정된 10개 증가분으로 나눈다. 각 표본의 깊이는 DELHBED를 더한 뒤 평가한다. 구간 조건을 만족하지 않은 표본도 평균의 분모 10에 포함한다.
- 103–105·119–121·130–131·162–175·183–184: 보간 깊이 차·PARTMIXAVG·TERM1+TERM2·2−TOXPFTB 두 항의 합을 분모로 사용한다. 각 나눗셈 전에 분모의 0 여부를 검사하는 조건은 이 파일에 없다.
