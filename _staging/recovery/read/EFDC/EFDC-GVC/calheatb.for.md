---
file: models/EFDC/raw/source_code/EFDC-GVC/calheatb.for
lines: 213
sha256: d52229bdb39ffadaa78fc9fe2b459f9523de80d5534887b2f239efc3bfc4f610
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# calheatb.for — 판독 구간 기록

구간은 1행부터 213행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | `SUBROUTINE CALHEATB(ISTL)` (6). 열 모의(thermal simulation)를 위한 바닥 온도 분포를 계산한다는 주석(21–22). 머리말·수정 기록·구분 주석을 포함한다. `INCLUDE 'EFDC.PAR'` (26), `INCLUDE 'EFDC.CMN'` (27). BETABED·BETBED·DIFFTIMI는 (LCM), 삼중대각(tridiagonal) 계수·우변·해·작업 배열은 (LCM,KBHM), DISTINT는 (LCM,KBHM-1)로 선언한다(30–33). |
| 37–64 | 시작 시 6행 CALHEATB 루틴 안. 37행 DELT=DT2는 주석이다. 기본값 `DELT=FLOAT(NTSTBC)*DT` (38); `S3TL=1.0` (39); `S2TL=0.0` (40); `NVAL=NTSTBC-1` (41). `IF(IS2TIM.EQ.1)THEN` (42)이면 NVAL=1(43), `IF(ISDYNSTP.EQ.0)THEN` (44)이면 DELT=DT(45), `ELSE` (46)이면 DELT=DTDYN(47). 같은 IS2TIM 참 분기에서 `S3TL=0.0` (49); `S2TL=1.0` (50). 바닥 고도(bed elevation) 극값 초기값 `BELTMPMAX=-1.E6` (53); `BELTMPMIN=1.E6` (54). L=1..LA에서 `BELTMPMAX=MAX(BELTMPMAX,BELV(L))     ! *** DSI BUG FIX` (57); `BELTMPMIN=MIN(BELTMPMIN,BELV(L))` (58). 56행 대체 극값식은 주석이다. 두께 보정 계수 `RBADJ=1.0` (61), 고도차 `BELVDIF=ABS(BELTMPMAX-BELTMPMIN)` (62), 조건부 설정 `IF(BELVDIF.GT.DABEDT) RBADJ=0.0` (63). 차이가 DABEDT보다 크면 보정을 끈다. |
| 65–90 | 시작 시 6행 CALHEATB 루틴 안. 바닥 온도 초기화 주석(67). `IF(ISBEDTEMI.EQ.1.AND.N.EQ.NVAL)THEN` (69)이면 L=1..LA에서 `TMPVAL = SQRT(10.03823E+6*HTBED2)` (72); `BETABED(L)=(DABEDT+RBADJ*(BELV(L)-BELTMPMIN))/TMPVAL` (73). 수직 간격·시작 위치 `DZBED=1./FLOAT(KBH-1)` (76); `ZVAL=-0.5*DZBED` (77). K=1..KBH-1에서 `ZVAL=ZVAL+DZBED` (79), L=2..LA에서 `DISTINT(L,K)=EXP(BETABED(L)*(ZVAL-1.))` (81)로 지수 분포를 계산한다. 다음 같은 K·L 범위에서 `TEMB(L,K)=TBEDIT(L)+(TEM(L,1)-TBEDIT(L))*DISTINT(L,K)` (87)로 바닥 초기 온도를 설정한다. 두 루프 종료(88–89). 초기화 조건은 다음 구간으로 이어진다. |
| 91–106 | 시작 시 6행 CALHEATB 루틴·69행 바닥 온도 초기화 참 분기 안. TEMBINIT.OUT을 열고 N·NVAL·DELT를 출력한다(91–92). L=2..LA에서 `TMPTHICK=DABEDT+RBADJ*(BELV(L)-BELTMPMIN)` (94), L·IL·JL·최하층 수온·TBEDIT·KBH-1개 TEMB·TMPTHICK을 기록한다(95–96). 파일·조건 종료(97–100). `101 FORMAT(2I5,E13.4)` (102), `111 FORMAT(3I5,32F10.3)` (103). 구분 주석을 포함한다. |
| 107–127 | 시작 시 6행 CALHEATB 루틴 안. 삼중대각 방정식 계수 설정 주석(107). 고정 물 열 확산계수(thermal diffusivity)·바닥 수직 간격 `DIFTW=1.4e-7` (109); `DZBED=1./FLOAT(KBH-1)` (110). L=2..LA에서 `DIFFTIMI(L)=HTBED2/((DABEDT+RBADJ*(BELV(L)-BELTMPMIN))*DZBED)**2` (113). 주석은 HTBED2를 바닥 열 확산계수 M**2/SEC로 설명한다(116). 첫 바닥 층의 하부 대각 계수 `ABEDTEM(L,1)=-DIFFTIMI(L)` (119), K=2..KBH-1·L=2..LA에서 `ABEDTEM(L,K)=-DIFFTIMI(L)` (124). 루프·주석을 포함한다. |
| 128–151 | 시작 시 6행 CALHEATB 루틴 안. L=2..LA에서 바닥·물 층 두께, 두께비 및 전도(conduction) 계수 `THICKBED=DZBED*(DABEDT+RBADJ*(BELV(L)-BELTMPMIN))` (129); `THICKWAT=DZC(1)*HP(L)` (130); `RATIO=THICKBED/THICKWAT` (131); `TMPCOND=2.*DIFTW/(THICKBED*THICKWAT)` (132). 바닥 평균 속도·속력 `UBED=0.5*( U(L,1)+U(L+1,1) )` (133); `VBED=0.5*( V(L,1)+V(LNC(L),1) )` (134); `USPD=SQRT( UBED*UBED+VBED*VBED )` (135), 대류(convection) 계수 및 결합 대각 계수 `TMPCONV=HTBED1*USPD/THICKBED` (136); `ABEDTEM(L,KBH)=-RATIO*(TMPCOND+TMPCONV)` (137); `CBEDTEM(L,KBH-1)=-(TMPCOND+TMPCONV)` (138). HTBED1은 무차원 대류 계수라는 주석(140). K=1..KBH-2·L=2..LA에서 `CBEDTEM(L,K)=-DIFFTIMI(L)` (144). 물 층 끝의 CBEDTEM은 0으로 설정한다(148–150). 루프·주석을 포함한다. |
| 152–173 | 시작 시 6행 CALHEATB 루틴 안. K=1..KBH·L=2..LA에서 주대각 계수 `BBEDTEM(L,K)=(1./DELT)-ABEDTEM(L,K)-CBEDTEM(L,K)` (154). L=2..LA의 첫 층 우변 `RBEDTEM(L,1)=(1./DELT)*TEMB(L,1)+DIFFTIMI(L)*TBEDIT(L)` (159). K=2..KBH-1·L=2..LA의 우변 `RBEDTEM(L,K)=(1./DELT)*TEMB(L,K)` (164). L=2..LA의 물 층 우변 `RBEDTEM(L,KBH)=(1./DELT)*TEM(L,1)` (169). 루프 종료·구분 주석을 포함한다. |
| 174–197 | 시작 시 6행 CALHEATB 루틴 안. 삼중대각 방정식을 직접 푼다(174행 주석). L=2..LA에서 BETBED에 첫 주대각 계수를 복사하고(177) 첫 해 `UBEDTEM(L,1)=RBEDTEM(L,1)/BETBED(L)` (178). K=2..KBH·L=2..LA에서 전진 소거(forward elimination) 식 `GBEDTEM(L,K)=CBEDTEM(L,K-1)/BETBED(L)` (183); `BETBED(L)=BBEDTEM(L,K)-ABEDTEM(L,K)*GBEDTEM(L,K)` (184); `UBEDTEM(L,K)=(RBEDTEM(L,K)-ABEDTEM(L,K)*UBEDTEM(L,K-1))` (185); `&                /BETBED(L)` (186). K=KBH-1..1의 역순·L=2..LA에서 후진 대입(back substitution) 식 `UBEDTEM(L,K)=UBEDTEM(L,K)-GBEDTEM(L,K+1)*UBEDTEM(L,K+1)` (192). 루프 종료·구분 주석을 포함한다. |
| 198–213 | 시작 시 6행 CALHEATB 루틴 안. 새 바닥·최하층 수온 설정 주석(198). K=1..KBH·L=2..LA에서 UBEDTEM을 TEMB에 복사한다(200–204). L=2..LA에서 UBEDTEM(L,KBH)를 TEM(L,1)에 복사한다(206–208). 구분 주석 뒤 `RETURN` (212), `END` (213). 이 파일에는 실행 CALL 문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·38–51: 인수 ISTL은 선언 이후 이 파일에서 사용하지 않는다. S3TL·S2TL은 설정 이후 이 파일에서 사용하지 않는다.
- 109·132: 물의 열 확산계수 DIFTW는 매 호출 1.4e-7로 고정한다. TMPCOND는 이 값을 사용한다.
- 72–76·109–113·129–137: HTBED2의 제곱근, KBH-1, 보정 바닥 두께 및 THICKWAT가 계산에 사용된다. THICKWAT는 DZC(1)*HP(L)다. 해당 계산 앞에는 이 파일의 양수 조건 검사가 없다.
- 178–186: 삼중대각 풀이에서 BETBED로 나눈다. 이 풀이 블록에는 BETBED=0 검사나 피벗(pivot) 교환 분기가 없다.
