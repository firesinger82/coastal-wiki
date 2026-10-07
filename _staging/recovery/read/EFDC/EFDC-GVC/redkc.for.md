---
file: models/EFDC/raw/source_code/EFDC-GVC/redkc.for
lines: 157
sha256: 16c0e5d4aa3040e6f5d2acbb26b5971b3b9089466315ca5fe008ebdf2be766d5
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# redkc.for — 판독 구간 기록

구간은 1행부터 157행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | 구분 주석과 REDKC 선언(1–6). EFDC-FULL 1.0a·2001-11-01 수정 머리말 및 수직층 수를 절반으로 줄인다는 설명(8–20). EFDC.PAR·EFDC.CMN 포함(23–24). KCD2를 계산하고 전체 셀 처리 주석으로 이어진다(28–35). 원문: `KCD2=KC/2` (28). |
| 36–60 | 시작 시 6행 REDKC 루틴 안. L=2..LA 루프를 연다(36). K=2..KC의 짝수 층에서 UHDY·VHDX의 두 원소 합을 BH에 보관하고 1..KCD2에 복사한다(38–45·50–57). U·V를 계산하여 U1·V1에 복사한다(46–47·58–59). 인덱스 순서와 U·V 계산 계수는 아래 원문 그대로이다. 원문: `DO L=2,LA` (36) / `DO K=2,KC,2` (38) / `KM=K-1` (39) / `KK=K/2` (40) / `BH(L,KK)=UHDY(L,K)+UHDY(KM,L)` (41) / `DO K=1,KCD2` (43) / `UHDY(L,K)=BH(L,K)` (44) / `UHDY(L,K)=UHDY(L,K)` (45) / `U(L,K)=0.5*DZI*UHDY(L,K)/(HU(L)*DYU(L))` (46) / `U1(L,K)=U(L,K)` (47) / `DO K=2,KC,2` (50) / `KM=K-1` (51) / `KK=K/2` (52) / `BH(L,KK)=VHDX(L,K)+VHDX(KM,L)` (53) / `DO K=1,KCD2` (55) / `VHDX(L,K)=BH(L,K)` (56) / `VHDX(L,K)=VHDX(L,K)` (57) / `V(L,K)=0.5*VHDX(L,K)/(HV(L)*DXV(L))` (58) / `V1(L,K)=V(L,K)` (59). |
| 61–89 | 시작 시 6행 REDKC 루틴 안. 시작 시 36행 L 루프 안. 짝수 층마다 UUU·VVV의 두 원소 평균을 BH에 보관한 뒤 1..KCD2에 복사한다(62–78). 염분(salinity) SAL은 K와 K−1 층을 평균하고 SAL·SAL1에 같은 값을 저장한다(80–88). 원문: `DO K=2,KC,2` (62) / `KM=K-1` (63) / `KK=K/2` (64) / `BH(L,KK)=0.5*(UUU(L,K)+UUU(KM,L))` (65) / `DO K=1,KCD2` (67) / `UUU(L,K)=BH(L,K)` (68) / `DO K=2,KC,2` (71) / `KM=K-1` (72) / `KK=K/2` (73) / `BH(L,KK)=0.5*(VVV(L,K)+VVV(KM,L))` (74) / `DO K=1,KCD2` (76) / `VVV(L,K)=BH(L,K)` (77) / `DO K=2,KC,2` (80) / `KM=K-1` (81) / `KK=K/2` (82) / `BH(L,KK)=0.5*(SAL(L,K)+SAL(L,K-1))` (83) / `DO K=1,KCD2` (85) / `SAL(L,K)=BH(L,K)` (86) / `SAL1(L,K)=BH(L,K)` (87). |
| 90–103 | 시작 시 6행 REDKC 루틴 안. 시작 시 36행 L 루프 안. K=2..KC−2의 짝수 층 W를 BH에 보관하여 K=1..KCD2−1의 W·W1에 복사한다(90–99). 각 루프의 KM·KP·KK 설정도 포함한다. KCD2 층의 W를 0으로 두고 W1에 복사한다(100–102). 원문: `DO K=2,KC-2,2` (90) / `KM=K-1` (91) / `KP=K+1` (92) / `KK=K/2` (93) / `BH(L,KK)=W(L,K)` (94) / `DO K=1,KCD2-1` (96) / `W(L,K)=BH(L,K)` (97) / `W1(L,K)=W(L,K)` (98) / `K=KCD2` (100) / `W(L,K)=0.` (101) / `W1(L,K)=W(L,K)` (102). |
| 104–133 | 시작 시 6행 REDKC 루틴 안. 시작 시 36행 L 루프 안. ISFILAB를 1로 설정한다(104). ISFILAB=0 분기는 짝수 층 AB를 복사하고 끝 원소를 ABO로 설정한다(105–116). ELSE 분기는 세 AB 원소의 역수를 사용한 가중 조화 평균(weighted harmonic mean)을 계산하여 복사하고 끝 원소를 ABO로 설정한다(118–129). 조건을 닫고 L 루프를 끝낸다(131–133). 원문: `ISFILAB=1` (104) / `IF(ISFILAB.EQ.0)THEN` (105) / `DO K=2,KC-2,2` (107) / `KM=K-1` (108) / `KP=K+1` (109) / `KK=K/2` (110) / `BH(L,KK)=AB(L,K)` (111) / `DO K=1,KCD2-1` (113) / `AB(L,K)=BH(L,K)` (114) / `AB(KCD2,L)=ABO` (116) / `ELSE` (118) / `DO K=2,KC-2,2` (120) / `KM=K-1` (121) / `KP=K+1` (122) / `KK=K/2` (123) / `BH(L,KK)=4./(1./AB(L,K-1)+2./AB(L,K)+1./AB(KP,L))` (124) / `DO K=1,KCD2-1` (126) / `AB(L,K)=BH(L,K)` (127) / `AB(KCD2,L)=ABO` (129). |
| 134–157 | 시작 시 6행 REDKC 루틴 안. KC를 KCD2로 바꾸고 KS를 계산하며 KS가 0이면 1로 바꾼다(137–140). DZI·DZIS·DZISD4 재설정은 주석이다(142–144). DZ·DZ2·DZS·DZDKC·DZDDT·DZDDT2·DZSDDT를 계산한다(145–152). 구분 주석·RETURN·END를 포함한다(154–157). 원문: `KC=KCD2` (137) / `KS=KC-1` (138) / `IF(KS.EQ.0) KS=1` (140) / `DZ=1./DZI` (145) / `DZ2=2.*DZ` (146) / `DZS=DZ*DZ` (147) / `DZDKC=DZ/FLOAT(KC)` (148) / `DZDDT=DZ/DT` (150) / `DZDDT2=0.5*DZ/DT` (151) / `DZSDDT=DZ*DZ/DT` (152). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41·53·65·74·124: 두 층을 합치거나 평균하는 식에 UHDY(KM,L)·VHDX(KM,L)·UUU(KM,L)·VVV(KM,L)·AB(KP,L)이 등장한다. 같은 식의 다른 원소는 배열의 첫 인덱스에 L을 사용한다.
- 46·58: U 계산식에는 0.5·DZI가 곱해진다. V 계산식에는 0.5만 곱해지며 DZI는 등장하지 않는다.
- 45·57: UHDY(L,K)와 VHDX(L,K)에 각각 같은 원소를 다시 대입하는 문장이 있다.
- 104–105·118–131: ISFILAB를 매 셀에서 1로 대입한 직후 ISFILAB=0을 검사한다. 이 파일의 해당 두 문장 사이에는 ISFILAB를 변경하는 문장이 없다.
- 114–116·127–129: AB 복사 루프는 AB(L,K)에 저장한다. 끝 원소 설정은 두 분기 모두 AB(KCD2,L)=ABO를 사용한다.
- 137–152: KC는 절반 층 수로 갱신한다. DZI·DZIS·DZISD4 갱신문은 주석 처리되어 있다. 실행 중인 DZ 및 시간 계수 계산은 DZI를 참조한다.
- 28·38·50·62·71·80: KCD2는 KC/2로 계산한다. 병합 루프의 층 범위는 2..KC, 증가량은 2이다. KC의 짝수 여부를 검사하는 분기는 이 파일에 없다.
