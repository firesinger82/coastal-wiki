---
file: models/EFDC/raw/source_code/EFDC-GVC/caldisp2.for
lines: 336
sha256: be079610aab7df04054eee86f2fd99f661f17134fbc6269eca458b2b49ba129f
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# caldisp2.for — 판독 구간 기록

구간은 1행부터 336행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | 구분 주석·`SUBROUTINE CALDISP2` 선언(6), EFDC-FULL 1.0a·수정·빈 변경 기록(8–19). `EFDC.PAR`·`EFDC.CMN`을 포함한다(21–22). UP/VP(KCM), CDISP(MGM,MGM), CDISPT/CDISPI/CCTMP(KCM,KCM), CCUTMP/CCVTMP(KCM), CRHS/CSOL/WTMP(MGM), VVTMP(MGM,MGM), SVAL(KCM,LCM)을 선언한다(26–28). 선언 연속행과 구분·빈 주석을 포함한다. |
| 32–69 | 시작 시 6행 CALDISP2 루틴 안. DELT=DT(32). 최초 호출 초기화 제목 뒤 `IF(N.EQ.NDISP)THEN` (38)에서 L=1..LC·K/KK=1..KC의 BDISP를 0으로 초기화한다(40–46). L/K 루프에서 `BDISP(K,K,L)=1.` (50)으로 대각값을 1로 설정하고 FUDISP/FVDISP를 0으로 초기화한다(48–54). L=1..LC의 DXXTCA/DXYTCA/DYXTCA/DYYTCA도 0으로 초기화한다(56–61). 조건 종료(63)와 수직 확산(vertical diffusion) 행렬·역행렬(matrix inverse) 및 분산 계수(dispersion coefficient) 누적 제목(67–68). |
| 70–115 | 시작 시 6행 CALDISP2 루틴 안. L=2..LA에서 `IF(LCT(L).EQ.5.AND.SPB(L).NE.0.)THEN` (71)인 셀만 계산한다. LN=LNC(L)(72), K=1..KC의 셀 중심 속도는 `UP(K)=0.5*(U(L,K)+U(L+1,K))` (75); `VP(K)=0.5*(V(L,K)+V(LN,K))` (76). UAVG/VAVG=0(79–80) 뒤 `UAVG=UAVG+DZC(K)*UP(K)` (82); `VAVG=VAVG+DZC(K)*VP(K)` (83)로 DZC 가중 평균을 누적한다. 속도 편차는 `UP(K)=UP(K)-UAVG` (87); `VP(K)=VP(K)-VAVG` (88). CDISP의 K/KK=1..KC를 0으로 초기화한다(91–95). 하부층 계수·행렬값은 `CUTMP=-DELT*CDZKK(1)*AB(L,1)*HPI(L)` (97); `CMTMP=1.-CUTMP` (98); `CDISP(1,1)=CMTMP*DZC(1)` (99); `CDISP(1,2)=CUTMP*DZC(1)` (100). K=2..KS의 내부층 식은 `CLTMP=-DELT*CDZKMK(K)*AB(L,K-1)*HPI(L)` (103); `CUTMP=-DELT*CDZKK(K)*AB(L,K)*HPI(L)` (104); `CMTMP=1.-CLTMP-CUTMP` (105); `CDISP(K,K-1)=CLTMP*DZC(K)` (106); `CDISP(K,K)=CMTMP*DZC(K)` (107); `CDISP(K,K+1)=CUTMP*DZC(K)` (108). 상부층 식은 `CLTMP=-DELT*CDZKMK(KC)*AB(L,KS)*HPI(L)` (111); `CMTMP=1.-CLTMP` (112); `CDISP(KC,KS)=CLTMP*DZC(KC)` (113); `CDISP(KC,KC)=CMTMP*DZC(KC)` (114). |
| 116–145 | 시작 시 6행 CALDISP2 루틴·70행 L 루프·71행 LCT=5·SPB≠0 참 분기 안. `CALL SVDCMP(CDISP,KC,KC,MGM,MGM,WTMP,VVTMP)` (116)로 특이값 분해(singular value decomposition)를 호출한다. K/KK=1..KC에서 CDISPT(K,KK)=CDISP(KK,K) 전치 복사(118–122). 특이값으로 나누는 식은 `CDISPT(K,KK)=CDISPT(K,KK)/WTMP(K)` (126). 각 K/KK에서 CTMP=0(132), KT=1..KC의 곱 합은 `CTMP=CTMP+VVTMP(K,KT)*CDISPT(KT,KK)` (134), CDISPI=CTMP 복사(136). 역행렬 계수의 층 가중은 `CDISPI(K,KK)=CDISPI(K,KK)*DZC(K)` (142). 각 루프 종료와 주석을 포함한다. |
| 146–177 | 시작 시 6행 CALDISP2 루틴·70행 L 루프·71행 셀 선택 참 분기 안. K/KK=1..KC에서 CTMP=0, KT=1..KC의 `CTMP=CTMP+CDISPI(K,KT)*BDISP(KT,KK,L)` (150)로 기존 BDISP와의 행렬곱을 계산한다. CCTMP에 저장한 뒤 BDISP로 복사한다(152–160). K=1..KC의 속도 강제항(forcing term)은 `CCUTMP(K)=FUDISP(K,L)-DT*UP(K)/HMIN` (163); `CCVTMP(K)=FVDISP(K,L)-DT*VP(K)/HMIN` (164). K마다 CCUU/CCVV=0, KK=1..KC의 누적은 `CCUU=CCUU+CDISPI(K,KK)*CCUTMP(KK)` (171); `CCVV=CCVV+CDISPI(K,KK)*CCVTMP(KK)` (172). FUDISP/FVDISP에 결과를 복사한다(174–175). |
| 178–208 | 시작 시 6행 CALDISP2 루틴·70행 L 루프·71행 셀 선택 참 분기 안. CCUU/CCVV/CCUV/CCVU=0(178–181) 뒤 K=1..KC의 속도 편차와 응답 곱을 `CCUU=CCUU+DZC(K)*UP(K)*FUDISP(K,L)` (183); `CCUV=CCUV+DZC(K)*UP(K)*FVDISP(K,L)` (184); `CCVU=CCVU+DZC(K)*VP(K)*FUDISP(K,L)` (185); `CCVV=CCVV+DZC(K)*VP(K)*FVDISP(K,L)` (186)로 적분한다. 분산 성분 누적은 `DXXTCA(L)=DXXTCA(L)+CCUU*HP(L)` (188); `DXYTCA(L)=DXYTCA(L)+CCUV*HP(L)` (189); `DYXTCA(L)=DYXTCA(L)+CCVU*HP(L)` (190); `DYYTCA(L)=DYYTCA(L)+CCVV*HP(L)` (191). K=1..KC마다 CCUU/CCVV=0(194–195), KK=1..KC에서 `CCUU=CCUU+DZC(KK)*UP(KK)*BDISP(KK,K,L)` (197); `CCVV=CCVV+DZC(KK)*VP(KK)*BDISP(KK,K,L)` (198). 후속 계산용 값은 `CUDISPT(K,L)=CCUU*HP(L)` (200); `CVDISPT(K,L)=CCVV*HP(L)` (201). 셀 조건·L 루프를 종료한다(204–205). `IF(N.LT.NTS) RETURN` (207)이면 루틴에서 돌아간다. |
| 209–236 | 시작 시 6행 CALDISP2 루틴 안. 분산 계수 완성 제목. L=2..LA의 `IF(LCT(L).EQ.5.AND.SPB(L).NE.0.)THEN` (214)에서 K/KK=1..KC에 `CDISP(K,KK)=-BDISP(K,KK,L)` (218)을 대입한다. 대각 보정은 `CDISP(K,K)=1.+CDISP(K,K)` (223). `CALL SVDCMP(CDISP,KC,KC,MGM,MGM,WTMP,VVTMP)` (226), K=1..KC의 SVAL(K,L)=WTMP(K) 저장(228–230). 작은 특이값 제거 블록은 주석이며 원문 식·조건은 `C     AWTMP=ABS(WTMP(K))` (233); `C     IF(AWTMP.LT.0.001) WTMP(K)=0.` (234)이다. 바깥 L 루프·셀 조건은 다음 구간까지 이어진다. |
| 237–265 | 시작 시 6행 CALDISP2 루틴·213행 L 루프·214행 셀 선택 참 분기 안. K=1..KC에서 CRHS=FUDISP 복사(237–239), `CALL SVBKSB(CDISP,WTMP,VVTMP,KC,KC,MGM,MGM,CRHS,CSOL)` (240). CCUU/CCVU=0 후 `CCUU=CCUU+CUDISPT(K,L)*CSOL(K)` (244); `CCVU=CCVU+CVDISPT(K,L)*CSOL(K)` (245)를 누적한다. 최종 xx·yx 성분은 `DXXTCA(L)=-(DXXTCA(L)+CCUU)*HMIN/TPN` (247); `DYXTCA(L)=-(DYXTCA(L)+CCVU)*HMIN/TPN` (248). CRHS=FVDISP 복사(250–252) 후 같은 `SVBKSB` 호출(253), CCVV/CCUV=0 뒤 `CCVV=CCVV+CVDISPT(K,L)*CSOL(K)` (257); `CCUV=CCUV+CUDISPT(K,L)*CSOL(K)` (258)를 누적한다. yy·xy 성분은 `DYYTCA(L)=-(DYYTCA(L)+CCVV)*HMIN/TPN` (260); `DXYTCA(L)=-(DXYTCA(L)+CCUV)*HMIN/TPN` (261). 셀 조건·L 루프 종료(263–264). |
| 266–288 | 시작 시 6행 CALDISP2 루틴 안. L=2..LA 전체의 수심 정규화(depth normalization)는 `DXXTCA(L)=DXXTCA(L)/HLPF(L)` (267); `DXYTCA(L)=DXYTCA(L)/HLPF(L)` (268); `DYXTCA(L)=DYXTCA(L)/HLPF(L)` (269); `DYYTCA(L)=DYYTCA(L)/HLPF(L)` (270). DISTEN.OUT를 열어 삭제한 뒤 다시 연다(277–279). 표제 출력(280) 뒤 모든 L=2..LA에서 IL/JL·DLON/DLAT·DXXTCA/DXYTCA/DYXTCA/DYYTCA를 출력한다(282–285). CLOSE(287), 제목·구분·빈 주석을 포함한다. |
| 289–312 | 시작 시 6행 CALDISP2 루틴 안. UVTSC.OUT를 STATUS='UNKNOWN'으로 열고 표제를 쓴다(289–290). L=2..LA에서 `AMCPT=AMCP(L)*GI` (293); `AMSPT=AMSP(L)*GI` (294)를 계산한다. 격자 인덱스·좌표·변환한 두 값과 AMCUE/AMSUE/AMCVE/AMSVE를 출력하고 닫는다(295–299). UVERV.OUT는 삭제 후 재생성한다(301–303). 표제 뒤 L=2..LA의 HLPF·UELPF·VELPF·최하층/최상층 SALLPF와 인덱스·좌표를 출력한다(304–309). CLOSE·주석(311–312). |
| 313–336 | 시작 시 6행 CALDISP2 루틴 안. SINVAL.OUT를 삭제 후 재생성한다(313–315). L=2..LA의 IL/JL과 K=1..KC의 SVAL을 출력하고 닫는다(317–321). 881/882/883 표제 FORMAT와 2011/2012/2013 자료 FORMAT를 선언한다(323–331). 2013은 `2013 FORMAT(2I4,8(2X,E12.4))` (331)이다. 구분·빈 주석(332–334), RETURN(335)·END(336). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 38–63: 초기화 실행 조건은 N=NDISP이다. 이 파일에는 최초 호출 여부를 별도로 저장하는 플래그나 N<NDISP 조기 반환문이 없다.
- 97–114: 하부층 행렬은 CDISP(1,2)를 설정한다(100). 이 파일에는 KC=1을 검사하여 해당 대입을 건너뛰는 분기가 없다.
- 116–126·226–235: 첫 SVDCMP 뒤 CDISPT는 WTMP(K)로 직접 나눈다(126). 작은 특이값을 0으로 설정하는 0.001 검사문은 두 번째 SVDCMP 뒤의 주석 블록에만 있다(232–235). SVDCMP·SVBKSB 내부는 이 파일 판독 범위에 포함하지 않았다.
- 163–164·247–261·267–270: HMIN·TPN·HLPF(L)을 분모에 사용하는 계산식이 있다. 이 루틴에는 이 값들의 0 검사문이 없다.
- 207·247–270: 최종 계산의 조기 반환 조건은 N<NTS이다(207). N>=NTS일 때 최종 계수 변환을 수행한다. 이 파일에는 최종 계산을 한 번만 수행하게 하는 별도 조건이 없다.
- 70–71·213–214·228–230·266–270·317–319: BDISP 기반 계산과 SVAL 대입은 LCT=5·SPB≠0 셀에서만 수행한다. HLPF 정규화와 파일 출력은 L=2..LA 전체에서 수행한다. 이 파일에는 SVAL 전체 초기화가 없다.
- 277–279·289·301–303·313–315: DISTEN.OUT·UVERV.OUT·SINVAL.OUT는 삭제 후 다시 연다. UVTSC.OUT는 STATUS='UNKNOWN'으로 한 번 열며 대응하는 삭제문이 없다.
