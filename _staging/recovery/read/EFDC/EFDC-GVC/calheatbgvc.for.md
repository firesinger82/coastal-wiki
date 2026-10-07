---
file: models/EFDC/raw/source_code/EFDC-GVC/calheatbgvc.for
lines: 202
sha256: 883b330b4f45b74f1f5924caedcfcbf2cabfb357dddaa377e50f456b4e540308
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# calheatbgvc.for — 판독 구간 기록

구간은 1행부터 202행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | `SUBROUTINE CALHEATBGVC(ISTL)` (6). 21행 설명 주석은 CALHEATB라는 이름으로 바닥 온도 분포 계산을 적는다. 머리말·수정 기록·구분 주석을 포함한다. `INCLUDE 'EFDC.PAR'` (26), `INCLUDE 'EFDC.CMN'` (27). BETABED·BETBED·DIFFTIMI는 (LCM), 삼중대각(tridiagonal) 계수·우변·해·작업 배열은 (LCM,KBHM), DISTINT는 (LCM,KBHM-1)로 선언한다(30–33). |
| 37–59 | 시작 시 6행 CALHEATBGVC 루틴 안. 37행 DELT=DT2는 주석이다. 기본 설정 `DELT=FLOAT(NTSTBC)*DT` (38); `S3TL=1.0` (39); `S2TL=0.0` (40); `NVAL=NTSTBC-1` (41). `IF(IS2TIM.EQ.1)THEN` (42)이면 NVAL=N(43), `IF(ISDYNSTP.EQ.0)THEN` (44)이면 DELT=DT(45), `ELSE` (46)이면 DELT=DTDYN(47). 같은 바깥 참 분기에서 `S3TL=0.0` (49); `S2TL=1.0` (50). 최소 바닥 고도(bed elevation) 초기값 `BELTMPMIN=1.E6` (53), L=1..LA에서 `BELTMPMIN=MIN(BELTMPMIN,BELV(L))` (55). 루프·구분 주석을 포함한다. |
| 60–83 | 시작 시 6행 CALHEATBGVC 루틴 안. 바닥 온도 초기화 주석(60). `IF(ISBEDTEMI.EQ.1.AND.N.EQ.NVAL)THEN` (62)이면 L=1..LA에서 `BETABED(L)=(DABEDT+BELV(L)-BELTMPMIN)/SQRT(10.03823E+6*HTBED2)` (65). 수직 간격·시작 위치 `DZBED=1./FLOAT(KBH-1)` (68); `ZVAL=-0.5*DZBED` (69). K=1..KBH-1에서 `ZVAL=ZVAL+DZBED` (71), L=2..LA에서 지수 분포 `DISTINT(L,K)=EXP(BETABED(L)*(ZVAL-1.))` (73). 다음 동일 K·L 범위에서 `TEMB(L,K)=TBEDIT(L)+(TEM(L,KGVCP(L))-TBEDIT(L))*DISTINT(L,K)` (79)로 바닥 초기 온도를 설정한다. 물 층 온도는 셀별 KGVCP(L)를 사용한다. 두 루프·빈 주석을 포함한다. |
| 84–96 | 시작 시 6행 CALHEATBGVC 루틴·62행 바닥 초기화 참 분기 안. TEMBINIT.OUT을 연다(84). L=2..LA에서 두께식 `TMPTHICK=DABEDT+BELV(L)-BELTMPMIN` (86), L·IL·JL·KBH-1개 TEMB·TMPTHICK을 기록한다(87). 루프·파일·조건 종료(88–91). `111 FORMAT(3I5,32F10.3)` (93)과 구분 주석을 포함한다. |
| 97–115 | 시작 시 6행 CALHEATBGVC 루틴 안. 삼중대각 계수 설정 주석(97). 고정 물 열 확산계수(thermal diffusivity)·바닥 수직 간격 `DIFTW=1.4e-7` (99); `DZBED=1./FLOAT(KBH-1)` (100). L=2..LA에서 `DIFFTIMI(L)=HTBED2/((DABEDT+BELV(L)-BELTMPMIN)*DZBED)**2` (102). HTBED2는 바닥 열 확산계수 M**2/SEC라는 주석(104). 첫 층 하부 대각 계수 `ABEDTEM(L,1)=-DIFFTIMI(L)` (107), K=2..KBH-1·L=2..LA에서 `ABEDTEM(L,K)=-DIFFTIMI(L)` (112). 루프·주석을 포함한다. |
| 116–140 | 시작 시 6행 CALHEATBGVC 루틴 안. L=2..LA에서 KBOT=KGVCP(L)(117). 바닥 두께·물 층 두께·두께비·전도(conduction) 계수 `THICKBED=DZBED*(DABEDT+BELV(L)-BELTMPMIN)` (118); `THICKWAT=DZC(KBOT)*GVCSCLP(L)*HP(L)` (119); `RATIO=THICKBED/THICKWAT` (120); `TMPCOND=2.*DIFTW/(THICKBED*THICKWAT)` (121). 평균 바닥 속도·속력 `UBED=0.5*( U(L,KBOT)+U(L+1,KBOT) )` (122); `VBED=0.5*( V(L,KBOT)+V(LNC(L),KBOT) )` (123); `USPD=SQRT( UBED*UBED+VBED*VBED )` (124), 대류(convection) 계수·결합 계수 `TMPCONV=HTBED1*USPD/THICKBED` (125); `ABEDTEM(L,KBH)=-RATIO*(TMPCOND+TMPCONV)` (126); `CBEDTEM(L,KBH-1)=-(TMPCOND+TMPCONV)` (127). HTBED1은 무차원 대류 계수라는 주석(129). K=1..KBH-2·L=2..LA에서 `CBEDTEM(L,K)=-DIFFTIMI(L)` (133), 물 층 끝의 CBEDTEM=0(137–139). 루프·주석을 포함한다. |
| 141–160 | 시작 시 6행 CALHEATBGVC 루틴 안. K=1..KBH·L=2..LA에서 주대각 계수 `BBEDTEM(L,K)=(1./DELT)-ABEDTEM(L,K)-CBEDTEM(L,K)` (143). L=2..LA의 첫 층 우변 `RBEDTEM(L,1)=(1./DELT)*TEMB(L,1)+DIFFTIMI(L)*TBEDIT(L)` (148), K=2..KBH-1·L=2..LA의 우변 `RBEDTEM(L,K)=(1./DELT)*TEMB(L,K)` (153), L=2..LA의 물 층 우변 `RBEDTEM(L,KBH)=(1./DELT)*TEM(L,KGVCP(L))` (158). 물 층 온도는 KGVCP(L)로 선택한다. 각 루프를 닫고 주석을 포함한다. |
| 161–186 | 시작 시 6행 CALHEATBGVC 루틴 안. 구분 주석·삼중대각 풀이 주석(161–164). L=2..LA에서 BETBED에 첫 주대각을 복사하고(166), 첫 해 `UBEDTEM(L,1)=RBEDTEM(L,1)/BETBED(L)` (167). K=2..KBH·L=2..LA에서 전진 소거(forward elimination) `GBEDTEM(L,K)=CBEDTEM(L,K-1)/BETBED(L)` (172); `BETBED(L)=BBEDTEM(L,K)-ABEDTEM(L,K)*GBEDTEM(L,K)` (173); `UBEDTEM(L,K)=(RBEDTEM(L,K)-ABEDTEM(L,K)*UBEDTEM(L,K-1))` (174); `&                /BETBED(L)` (175). K=KBH-1..1 역순·L=2..LA에서 후진 대입(back substitution) `UBEDTEM(L,K)=UBEDTEM(L,K)-GBEDTEM(L,K+1)*UBEDTEM(L,K+1)` (181). 루프 종료·구분 주석을 포함한다. |
| 187–202 | 시작 시 6행 CALHEATBGVC 루틴 안. 새 바닥·최하층 수온 설정 주석(187). K=1..KBH·L=2..LA에서 UBEDTEM을 TEMB에 복사한다(189–193). L=2..LA에서 UBEDTEM(L,KBH)를 TEM(L,KGVCP(L))에 복사한다(195–197). 구분 주석 뒤 `RETURN` (201), `END` (202). 이 파일에는 실행 CALL 문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·38–51: 인수 ISTL은 선언 이후 이 파일에서 사용하지 않는다. S3TL·S2TL은 설정 이후 이 파일에서 사용하지 않는다.
- 42–43·62–91: IS2TIM=1이면 NVAL에 현재 N을 복사한다. 뒤의 초기화 조건은 ISBEDTEMI=1 및 N=NVAL이다. 이 파일에는 ISBEDTEMI를 변경하는 대입이 없다.
- 99·121: 물의 열 확산계수 DIFTW는 매 호출 1.4e-7로 고정한다. TMPCOND는 이 값을 사용한다.
- 65·68·100–102·118–126: HTBED2의 제곱근, KBH-1, 바닥 두께 및 THICKWAT가 계산에 사용된다. THICKWAT는 DZC(KBOT)*GVCSCLP(L)*HP(L)다. 해당 계산 앞에는 이 파일의 양수 조건 검사가 없다.
- 167–175: 삼중대각 풀이에서 BETBED로 나눈다. 이 풀이 블록에는 BETBED=0 검사나 피벗(pivot) 교환 분기가 없다.
