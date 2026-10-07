---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/ChemFate/partmix.f90
lines: 168
sha256: 2916041229202c970bf336ede3a9e96be12309cc3739ce11df154a57336a7bd4
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# partmix.f90 — 판독 구간 기록

구간은 1행부터 168행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | EFDC+ 안내와 DSI 저작권·GPLv2 머리말이 있다(1–8). PARTMIX(NT)를 시작한다(9). 저질 상층 PMXDEPTH 범위의 독성물질 입자 혼합(particle mixing)을 계산한다는 주석이다(13–14). 변경 이력·GLOBAL·implicit none·지역 정수와 실수·PARTMIXAVG(KBM)를 선언한다(18–30). |
| 32–50 | 시작 시 9행 PARTMIX 루틴 안. OpenMP 병렬 영역을 열고 ND별 저질 목록 LF·LL을 계산한다(33–38). K=1..KB와 LP=LF..LL에서 PARTMIXZ를 0으로 초기화한다(40–47). 이전 입자 혼합 방식은 ISPMXZ=2라는 주석과 빈 줄을 포함한다(49–50). 원문: `do ND = 1,NDM` (36); `LF = (ND-1)*LDMSED+1` (37); `LL = min(LF+LDMSED-1,LASED)` (38); `do K = 1,KB` (40); `do LP = LF,LL` (41); `L = LSED(LP)` (42); `PARTMIXZ(L,K) = 0.0` (43). |
| 51–76 | 시작 시 9행 PARTMIX 루틴·33행 OpenMP 병렬 영역 안. ISPMXZ(NT)=2이면 ND·저질 LP를 순회하고 DEPINBED=0, 영역 인덱스 LZ=LPMXZ(L)를 설정한다(51–61). KBT>2이면 K=KBT..2를 역순으로 내려가며 KM=K-1과 누적 깊이를 계산한다(63–66). NP=1..NPMXPTS-1에서 깊이가 표의 반열린 구간에 들어갈 때 WT1·WT2와 깊이 간격 TMPVAL로 PMXCOEF를 선형 보간(linear interpolation)하여 PARTMIXZ(L,KM)에 넣는다(67–76). 원문: `if( ISPMXZ(NT) == 2 )then` (51); `do ND = 1,NDM` (54); `LF = (ND-1)*LDMSED+1` (55); `LL = min(LF+LDMSED-1,LASED)` (56); `do LP = LF,LL` (58); `L = LSED(LP)` (59); `DEPINBED = 0.` (60); `LZ = LPMXZ(L)` (61); `if( KBT(L) > 2 )then` (63); `do K = KBT(L),2,-1` (64); `KM = K-1` (65); `DEPINBED = DEPINBED+HBED(L,K)` (66); `do NP = 1,NPMXPTS-1` (67); `NDP = NP+1` (68); `if( DEPINBED >= PMXDEPTH(NP,LZ) .and. DEPINBED < PMXDEPTH(NDP,LZ) )then` (69); `WT1 = DEPINBED-PMXDEPTH(NP,LZ)` (70); `WT2 = PMXDEPTH(NDP,LZ)-DEPINBED` (71); `TMPVAL = PMXDEPTH(NP+1,LZ)-PMXDEPTH(NP,LZ)` (72); `PARTMIXZ(L,KM) = (WT2*PMXCOEF(NP,LZ) + WT1*PMXCOEF(NDP,LZ))/TMPVAL` (73). |
| 77–104 | 시작 시 9행 PARTMIX 루틴·33행 OpenMP 병렬 영역·51행 ISPMXZ=2 분기·54행 ND 루프·58행 LP 루프·63행 KBT 조건 분기 안. else에서는 K=KBT와 KM=K-1 한 경계에 같은 표 보간을 적용한다(77–90). LP 루프 종료 뒤 새 LP·K=KBT..2 루프에서 2-두 층 TOXPFTB+1.E-12를 분모로 PARTMIXZ를 보정한다(93–99). ND·OpenMP DO·옵션 분기를 닫는다(100–103). 원문: `else` (77); `K  = KBT(L)` (78); `KM = K-1` (79); `DEPINBED = DEPINBED + HBED(L,K)` (80); `do NP = 1,NPMXPTS-1` (81); `NDP = NP+1` (82); `if( DEPINBED >= PMXDEPTH(NP,LZ) .and. DEPINBED < PMXDEPTH(NDP,LZ) )then` (83); `WT1 = DEPINBED-PMXDEPTH(NP,LZ)` (84); `WT2 = PMXDEPTH(NDP,LZ)-DEPINBED` (85); `TMPVAL = PMXDEPTH(NP+1,LZ)-PMXDEPTH(NP,LZ)` (86); `PARTMIXZ(L,KM) = (WT2*PMXCOEF(NP,LZ) + WT1*PMXCOEF(NDP,LZ))/TMPVAL` (87); `do LP = LF,LL` (93); `L = LSED(LP)` (94); `do K = KBT(L),2,-1` (95); `KM = K-1` (96); `PARTMIXZ(L,KM) = 2.*PARTMIXZ(L,KM)/(2.0-TOXPFTB(L,K,NT)-TOXPFTB(L,KM,NT)+1.E-12)` (97). |
| 105–140 | 시작 시 9행 PARTMIX 루틴·33행 OpenMP 병렬 영역 안. 새 방식 ISPMXZ(NT)=1에서 ND·LP를 순회하고 영역 LZ를 정한다(107–116). PARTMIXAVG와 PARTMIXZ를 K=1..KB에서 0으로 만든다(118–121). K=KBT..1을 역순으로 순회하며 HBED/10의 소구간(subinterval) 10개에서 깊이를 누적한다(123–127). 각 표 구간에 들어간 보간값을 PARTMIXAVG(K)에 더하고 10으로 나누어 층 평균을 구한다(128–139). 원문: `if( ISPMXZ(NT) == 1 )then` (107); `do ND = 1,NDM` (110); `LF = (ND-1)*LDMSED+1` (111); `LL = min(LF+LDMSED-1,LASED)` (112); `do LP = LF,LL` (114); `L = LSED(LP)` (115); `LZ = LPMXZ(L)` (116); `do K = 1,KB` (118); `PARTMIXAVG(K) = 0.0` (119); `PARTMIXZ(L,K) = 0.0` (120); `DEPINBED = 0.` (123); `do K = KBT(L),1,-1` (124); `DELHBED = HBED(L,K)/10.` (125); `do KK = 1,10` (126); `DEPINBED = DEPINBED+DELHBED` (127); `do NP = 1,NPMXPTS-1` (128); `NDP = NP+1` (129); `if( DEPINBED >= PMXDEPTH(NP,LZ) .and. DEPINBED < PMXDEPTH(NDP,LZ) )then` (130); `WT1 = DEPINBED-PMXDEPTH(NP,LZ)` (131); `WT2 = PMXDEPTH(NDP,LZ)-DEPINBED` (132); `TMPVAL = PMXDEPTH(NP+1,LZ)-PMXDEPTH(NP,LZ)` (133); `PARTMIXAVG(K) = PARTMIXAVG(K) + (WT2*PMXCOEF(NP,LZ)+WT1*PMXCOEF(NDP,LZ))/TMPVAL` (134); `PARTMIXAVG(K) = PARTMIXAVG(K)/10.` (138). |
| 141–168 | 시작 시 9행 PARTMIX 루틴·33행 OpenMP 병렬 영역·107행 ISPMXZ=1 분기·110행 ND 루프·114행 LP 루프 안. K=1..KBT-1에서 두 층 HBED/PARTMIXAVG와 두께 합으로 경계 PARTMIXZ를 계산한다(141–146). 새 LP·K 역순 루프에서 두 층 TOXPFTB와 1.E-12로 이전 방식과 같은 보정을 적용한다(150–156). ND·OpenMP DO·옵션 조건과 병렬 영역을 닫고 return·END·마지막 빈 줄을 포함한다(157–168). 원문: `do K = 1,KBT(L)-1` (141); `TERM1 = HBED(L,K)/PARTMIXAVG(K)` (142); `TERM2 = HBED(L,K+1)/PARTMIXAVG(K+1)` (143); `TERM3 = HBED(L,K)+HBED(L,K+1)` (144); `PARTMIXZ(L,K) = TERM3/(TERM1+TERM2)` (145); `do LP = LF,LL` (150); `L = LSED(LP)` (151); `do K = KBT(L),2,-1` (152); `KM = K-1` (153); `PARTMIXZ(L,KM) = 2.*PARTMIXZ(L,KM)/(2.0-TOXPFTB(L,K,NT)-TOXPFTB(L,KM,NT)+1.E-12)` (154). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28·67·81·128: NPMXPTS는 지역 정수로 선언한다. 세 표 보간 루프는 NPMXPTS-1을 상한으로 사용한다. 이 파일에는 NPMXPTS 대입문이나 입력문이 없다.
- 30·33·109·118–145: PARTMIXAVG(KBM)는 지역 배열이다. OpenMP 병렬 지시문은 DEFAULT(SHARED)이며 새 방식 DO의 PRIVATE 목록에 PARTMIXAVG가 없다. 해당 DO 안에서 배열을 초기화·누적·나눗셈·참조한다.
- 77–87: KBT>2 조건의 else는 K=KBT와 KM=K-1을 사용한다. 이 else 안에는 KM의 하한 검사문이 없다.
- 118–138·141–145: PARTMIXAVG는 0으로 시작하고 깊이 표 구간에 들어간 경우에만 보간값을 더한다. 이후 HBED/PARTMIXAVG 계산 앞에는 PARTMIXAVG>0 검사문이 없다.
- 125–138·97·154: 새 방식은 각 층을 10개 소구간으로 나누고 누적값을 10으로 나눈다. 두 방식의 입자분율 보정 분모에는 1.E-12가 고정으로 더해진다.
