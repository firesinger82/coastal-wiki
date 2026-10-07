---
file: models/EFDC/raw/source_code/EFDC-GVC/filtran.for
lines: 236
sha256: cb84b52c1e5d0b4172ea545bdec3102aa741b90dd46be83953e0e22f22c9ad3f
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# filtran.for — 판독 구간 기록

구간은 1행부터 236행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | 구분 주석과 `SUBROUTINE FILTRAN` 선언(1–6). EFDC-FULL 1.0a·수정자·날짜·변경 이력 틀(8–18). 평균 질량수송(mean mass transport) 속도·확산계수(diffusivity)를 공간 필터링(spatial filtering)하고 작은 규모 확산계수를 계산한다는 주석(19–22). AXZ/AYZ 대신 UUU/VVV, UHPF/VHPF 대신 DU/DV를 쓴다고 적는다(21–22). `EFDC.PAR`·`EFDC.CMN` 포함(26–27). 수평 속도의 연직 필터 및 수평 분산(dispersion) 계수 계산 주석(31–35). |
| 36–60 | 시작 시 6행 FILTRAN 루틴 안. `DO L=2,LA` (36)에서 이웃 인덱스 `LE=L+1` (37), `LW=L-1` (38), LN=LNC(L)·LS=LSC(L) 복사(39–40). 연직 양 끝의 식 `ULPF(L,1)=0.25*(3.*UHDY(L,1)+UHDY(L,2))` (44), `VLPF(L,1)=0.25*(3.*VHDX(L,1)+VHDX(L,2))` (45), `ULPF(L,KC)=0.25*(3.*UHDY(L,KC)+UHDY(L,KS))` (46), `VLPF(L,KC)=0.25*(3.*VHDX(L,KC)+VHDX(L,KS))` (47). `DO K=2,KS` (48)에서 `ULPF(L,K)=0.25*(UHDY(L,K-1)+2.*UHDY(L,K)+UHDY(L,K+1))` (49), `VLPF(L,K)=0.25*(VHDX(L,K-1)+2.*VHDX(L,K)+VHDX(L,K+1))` (50). `DO K=1,KC` (53)에서 잔차 `DU(L,K)=UHDY(L,K)-ULPF(L,K)` (54), `DV(L,K)=VHDX(L,K)-VLPF(L,K)` (55). `ISFILAZ=0` (58), 조건 `IF(ISFILAZ.EQ.0)GOTO 100` (59)으로 139행으로 이동한다. |
| 61–95 | 시작 시 6행 FILTRAN 루틴·36행 L 루프 안이며 59행 점프를 하지 않았을 때의 경로. WTB 식은 주석 처리(63). ERU/ERV=0 초기화(65–66). `DO K=1,KC` (67)에서 `DU(L,K)=DU(L,K)*DZIC(K)/(DYU(L)*HU(L))` (68), `DV(L,K)=DV(L,K)*DZIC(K)/(DXV(L)*HV(L))` (69), `ERU=ERU+DU(L,K)` (70), `ERV=ERV+DV(L,K)` (71). `ERU=ERU*DZ` (74), `ERV=ERV*DZ` (75). `DO K=1,KC` (76)에서 `DU(L,K)=DU(L,K)-ERU` (77), `DV(L,K)=DV(L,K)-ERV` (78). FZU/FZV의 0층을 0으로 초기화(81–82). `DO K=1,KS` (84)에서 `FZU(K)=FZU(K-1)+DU(L,K)` (85), `FZV(K)=FZV(K-1)+DV(L,K)` (86). CUB/CLB의 1층을 0으로 초기화(89–90). `DO K=1,KS` (92)에서 `CUB(K+1)=CUB(K)+FZU(K)/(AB(L,K)+AB(L-1,K))` (93), `CLB(K+1)=CLB(K)+FZV(K)/(AB(L,K)+AB(LS,K))` (94). |
| 96–138 | 시작 시 6행 FILTRAN 루틴·36행 L 루프 안이며 59행 점프를 하지 않았을 때의 경로. ERU/ERV=0(97–98). `DO K=1,KC` (99)에서 `ERU=ERU+CUB(K)` (100), `ERV=ERV+CLB(K)` (101). `ERU=ERU*DZ` (104), `ERV=ERV*DZ` (105). `DO K=1,KC` (106)에서 `CUB(K)=CUB(K)-ERU` (107), `CLB(K)=CLB(K)-ERV` (108). AXZEX/AYZEX=0(111–112). `DO K=1,KC` (113)에서 `DU(L,K)=-2.*DZ*DZ*SUB(L)*HU(L)*DU(L,K)*CUB(K)` (114), `DV(L,K)=-2.*DZ*DZ*SVB(L)*HV(L)*DV(L,K)*CLB(K)` (115), `AXZEX=AXZEX+DZ*DU(L,K)` (116), `AYZEX=AYZEX+DZ*DV(L,K)` (117). 필터 식 `UUU(L,1)=0.25*(3.*DU(L,1)+DU(L,1))` (120), `VVV(L,1)=0.25*(3.*DV(L,1)+DV(L,2))` (121), `UUU(L,KC)=0.25*(3.*DU(L,KC)+DU(L,KS))` (122), `VVV(L,KC)=0.25*(3.*DV(L,KC)+DV(L,KS))` (123). `DO K=2,KS` (124)에서 `UUU(L,K)=0.25*(DU(L,K-1)+2.*DU(L,K)+DU(L,K+1))` (125), `VVV(L,K)=0.25*(DV(L,K-1)+2.*DV(L,K)+DV(L,K+1))` (126). `ISAZCON=0` (129), `IF(ISAZCON.EQ.1)THEN` (130) 안 `DO K=1,KC` (131)은 UUU/VVV에 AXZEX/AYZEX를 복사한다(132–134). 조건 종료·구분 주석(135–138). |
| 139–161 | 시작 시 6행 FILTRAN 루틴·36행 L 루프 안. 점프 목적지 `100 CONTINUE` (139). `ISFILUH=0` (143), 조건 `IF(ISFILUH.EQ.1)THEN` (144) 안 `DO K=1,KC` (145)은 UHDY에 ULPF를 복사한다(146). `U(L,K)=UHDY(L,K)/(HU(L)*DYU(L))` (147), U1=U 복사(148), VHDX=VLPF 복사(149), `V(L,K)=VHDX(L,K)/(HV(L)*DXV(L))` (150), V1=V 복사(151). 내부 루프·조건·36행 L 루프를 닫는다(152–157). 구분 주석·빈 줄(158–161). |
| 162–185 | 시작 시 6행 FILTRAN 루틴 안. 동쪽 경계 `DO LL=1,NCBE` (162)에서 L=LCBE(LL)(163), `LE=L+1` (164), `DO K=1,KC` (165). UHDY(LE,K)에 같은 값을 두 번 복사한다(166–167). 속도식 `U(LE,K)=UHDY(L,K)/(HU(L)*DYU(L))` (168), U1 복사(169), 루프 종료(170–171). 북쪽 경계 `DO LL=1,NCBN` (173)에서 L=LCBN(LL)·LN=LNC(L)(174–175), `DO K=1,KC` (176). VHDX(LN,K)에 같은 값을 두 번 복사한다(177–178). 속도식 `V(LN,K)=DZI*VHDX(L,K)/(HV(L)*DXV(L))` (179), V1 복사(180), 루프 종료·구분 주석(181–185). |
| 186–222 | 시작 시 6행 FILTRAN 루틴 안. 수평 분산계수 진단 주석(186–189). 초기값 `AXZMAX=0.` (190), `AXZMIN=100000.` (191), `AYZMAX=0.` (192), `AYZMIN=100000.` (193). `DO L=1,LC` (195), `DO K=1,KC` (196)에서 조건 `IF(UUU(L,K).GT.AXZMAX)THEN` (197)은 AXZMAX와 해당 IL·JL·K를 복사한다(198–201). 조건 `IF(UUU(L,K).LT.AXZMIN)THEN` (203)은 AXZMIN과 위치를 복사한다(204–207). 조건 `IF(VVV(L,K).GT.AYZMAX)THEN` (209)은 AYZMAX와 위치를 복사한다(210–213). 조건 `IF(VVV(L,K).LT.AYZMIN)THEN` (215)은 AYZMIN과 위치를 복사한다(216–219). 조건·루프 종료(220–222). |
| 223–236 | 시작 시 6행 FILTRAN 루틴 안. 진단 최대·최소의 I/J/K와 값을 장치 6에 출력한다(224–227). FORMAT 686–689는 3I10·E12.4 형식을 지정한다(228–231). 구분 주석과 RETURN·END(232–236). 이 루틴에는 외부 루틴 CALL 문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 58–59·129–130·143–144: ISFILAZ·ISAZCON·ISFILUH를 각각 0으로 대입한다. ISFILAZ=0 점프는 65–135행의 계수 계산을 건너뛴다. ISFILUH=1 분기는 이 대입 뒤에 있다.
- 120–121: UUU(L,1) 식은 DU(L,1)을 두 항에 쓴다. 인접한 VVV(L,1) 식의 두 번째 항은 DV(L,2)이다.
- 166–167·177–178: 동쪽 UHDY 경계 복사를 두 번 수행한다. 북쪽 VHDX 경계 복사도 두 번 수행한다.
- 168·179: 동쪽 경계 속도식에는 DZI가 없다. 북쪽 경계 속도식에는 DZI가 곱해진다.
- 190–227: 진단값의 최대·최소에는 초기값이 있다. 해당 I/J/K 변수의 대입은 엄격한 GT/LT 조건 안에만 있고, 출력 앞의 별도 위치 초기화는 이 파일에 없다.
- 44–47: 연직 끝 필터는 2층과 KS층을 직접 참조한다. 이 참조 앞에는 KC에 대한 조건 검사가 없다.
