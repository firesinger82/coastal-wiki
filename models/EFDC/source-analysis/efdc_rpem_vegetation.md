---
title: "EFDC+ RPEM 해초/SAV 모델 source-analysis — mod_rpem.f90 (shoot/root/epiphyte/detritus, 성장 limitation triad + implicit Euler)"
topic: efdc-rpem-vegetation
canonical_source: self
citation_status: verified
verification_method: "EFDC+ Stable(12.4, sha 3ed76b6) raw source 직접 read: Eutrophication/mod_rpem.f90(1413) — shoot growth EQ5(:299)·implicit update EQ1(:360-363) file:line 직접 검증. WQ3D dispatch(mod_wq.f90:361). 범위=driver CAL_RPEM + shoot 성장 프로세스(roots/epiphytes/detritus 요약). [[efdc_water_quality]] 는 filename/future-task 로만 언급."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-04
verification_by: "Claude Opus 4.8 (1M context) — mod_rpem.f90:296-309·358-364 직접 read 검증"
verification_date: 2026-07-04
related:
  - models/EFDC/source-analysis/efdc_water_quality.md
  - models/EFDC/source-analysis/efdc_linkages.md
  - models/EFDC/source-analysis/sediment/efdc_sedzlj.md
last_source_check: 2026-10-08 (recovery 재판독 대조)
---

# EFDC+ RPEM 해초/SAV 모델 — `mod_rpem.f90`

> 소스: [`Eutrophication/mod_rpem.f90`](../raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_rpem.f90) (1413, `WQ_RPEM_MODULE`). EFDC+ Stable = 12.4.
> **정체**: **Rooted Plant and Epiphyte Model** — 침수식생(seagrass/macrophyte, SAV) 4구획(shoot·root·epiphyte·shoot detritus). 연안 서식지·퇴적안정·영양염순환 관련 1급 기능이나 미커버([[efdc_water_quality]]:23 filename·:219 future task 만, [[efdc_linkages]] 는 출력 payload 만). 범위=driver + shoot 성장(roots/epiphytes/detritus 요약).
> dispatch: `mod_wq.f90:361 call CAL_RPEM`, `ISRPEM>0` 게이트. **저층 `K=KSZ(L)` 만**(:115). 바닥 diagenesis 풀 `SM2NH4/NO3/PO4` 읽음(`use WQ_DIAGENESIS`).

## 0. 구조 + 상태변수

| 서브루틴 | 라인 | 역할 |
|---|---|---|
| `CAL_RPEM` | 88-725 | kinetics driver: limitation → 성장/호흡 → root↔shoot translocation → 4 상태변수 갱신 → 수관 WQ 풀 반환 |
| `RPEMINP_JNP` | 742-1317 | JSON 입력(`fson_get "rooted_plant.…"`) + MPI broadcast + **온도 lookup 테이블(Gaussian) 구성** |
| `INIT_RPEMVARS` | 1327-1411 | 배열 할당·초기화 |

상태변수(저층 biomass, :59): `WQRPS` shoots·`WQRPR` roots·`WQRPE` epiphytes·`WQRPD` shoot detritus.

## 1. 성장 limitation triad (F3·F1·F2)

- **F3(T) 온도** lookup(`TWQ(L)` 인덱스, :171-178): `XLIMTPRPS`(shoot 성장)·`XLIMTRRPR`(root 호흡) 등.
- **F1(N) 영양염** EQ6(:186-192): 수관 `WQV(INHX/INOX/PO4D)` + 바닥 `SM2NH4/NO3/PO4` 를 half-sat 비 `RATION=RKHNRPS/RKHNRPR` 로 가중 → `min(N,P)`.
- **F2(I) 광** EQ7-9(:249-253): 층 상/하 depth-integrated Beer-Lambert `XLIMLRPS=2.718/(RKESSAVG·Z·H)·(exp(ALPHABOT)-exp(ALPHATOP))`. **epiphyte self-shading** EQ10(:237): 소광에 `RKERPE·WQRPE/CCHLRPE` 가산. 가중 광이력 EQ12(:214) `WQAVGIO=WQCIA·WQI0+WQCIB·WQI1+WQCIC·WQI2`.

## 2. Shoot 성장/호흡 + 저면 ramp (:299-311)
```fortran
PRPS(L) = PMRPS*XLIMTPRPS*XLIMNRPS*XLIMLRPS*EXP(-RKSH*WQRPS(L))   ! :299 EQ5 (★self-shading exp, JI 7/4/04)
RRPS(L) = RMRPS*XLIMTRRPS(L)                                       ! :301 EQ15 호흡
RATIOHP = min((max(HP-HDRY,0.))/HDRY2, 1.0) ; PRPS *= RATIOHP      ! :308 저면 wetting ramp
```
root 호흡 EQ18(:317)·epiphyte 성장 EQ19(:324).

## 3. Root↔Shoot translocation (`IJRPRS` 3택, :335-349)
코드 선형 이동식은 RKRPORS·(ROSR·RPR−RPS)이다. (`Eutrophication/mod_rpem.f90:342` — `RJRPRS(L) = RKRPORS*(ROSR*WQRPR(L)-WQRPS(L))`; EFDC_Theory_Document_Ver_12.pdf, PDF 206쪽·인쇄 193쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 197쪽·인쇄 184쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 214쪽·인쇄 201쪽) Theory 식 8.155는 KRPO_RS·(RPR−RORS·RPS)이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 206쪽·인쇄 193쪽, 식 8.155) 코드 광 의존 이동식은 RKRPRS·RISS/(RISS+RISSS)이다. (`Eutrophication/mod_rpem.f90:349` — `RJRPRS(L) = RKRPRS*RISS(L)/(RISS(L)+RISSS+1E-18)`; EFDC_Theory_Document_Ver_12.pdf, PDF 206쪽·인쇄 193쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 197쪽·인쇄 184쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 214쪽·인쇄 201쪽) Theory 식 8.157은 RPR을 추가로 곱한다. (EFDC_Theory_Document_Ver_12.pdf, PDF 206쪽·인쇄 193쪽, 식 8.157) 이 노트의 EQ1–45는 코드 주석 번호이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 206쪽·인쇄 193쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 197쪽·인쇄 184쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 214쪽·인쇄 201쪽) Theory v12의 해당 번호 범위는 식 8.124–8.197이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 197쪽·인쇄 184쪽, 식 8.124; EFDC_Theory_Document_Ver_12.pdf, PDF 214쪽·인쇄 201쪽, 식 8.197)

## 4. ★Shoot biomass 갱신 — implicit Euler + seed floor (:360-363)
```fortran
SOURSINK = (1.-FPRPR)*PRPS(L) - RRPS(L) - RLRPS            ! :360 EQ1 (성장-호흡-loss)
FACIMP   = 1./(1.-DTWQ*SOURSINK)                           ! :361 implicit Euler
WQRPS(L) = FACIMP*(WQRPS(L) + DTWQ*RJRPRS(L))              ! :362
WQRPS(L) = max(WQRPS(L), 0.2)   ! ★"KEEP THE 'SEED'…IF RPS=0 IT WILL NEVER GROW AGAIN"  :363
```
코드는 FRPSD·RLRPS·RPS를 쇄설물 공급으로 사용한다. (`Eutrophication/mod_rpem.f90:392` — `WQRPD(L) = FACIMP*(WQRPD(L)+DTWQ*FRPSD*RLRPS*WQRPS(L))`; EFDC_Theory_Document_Ver_12.pdf, PDF 199쪽·인쇄 186쪽) 코드는 쇄설물 RPD에 손실률을 곱한다. (`Eutrophication/mod_rpem.f90:388` — `SOURSINK = -RLRPD                                                    ! EQ. (4)  RLRPD-Loss rate for plant detritus at bottom of water column (/day)`; EFDC_Theory_Document_Ver_12.pdf, PDF 199쪽·인쇄 186쪽) Theory 식 8.127은 PRPS·RPS를 공급으로 인쇄한다. (`Eutrophication/mod_rpem.f90:392` — `WQRPD(L) = FACIMP*(WQRPD(L)+DTWQ*FRPSD*RLRPS*WQRPS(L))`; EFDC_Theory_Document_Ver_12.pdf, PDF 199쪽·인쇄 186쪽, 식 8.127) Theory 식 8.127의 감쇠항은 RPS를 사용한다. (EFDC_Theory_Document_Ver_12.pdf, PDF 199쪽·인쇄 186쪽, 식 8.127)

## 5. 수관 반환 (:454-529)
- 코드는 WQRPDLN을 0으로 초기화한다. (`Eutrophication/mod_rpem.f90:1379` — `WQRPDLN  = 0`; EFDC_Theory_Document_Ver_12.pdf, PDF 213쪽·인쇄 200쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 214쪽·인쇄 201쪽) 확인한 mod_rpem.f90에는 이 변수의 추가 갱신 대입이 없다. (`Eutrophication/mod_rpem.f90:1379` — `WQRPDLN  = 0`; EFDC_Theory_Document_Ver_12.pdf, PDF 213쪽·인쇄 200쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 214쪽·인쇄 201쪽) 수주 RPON·LPON·DON·NH4 반환식은 WQRPDLN을 사용한다. (`Eutrophication/mod_rpem.f90:1379` — `WQRPDLN  = 0`; `Eutrophication/mod_rpem.f90:483` — `+ FNRRPE*WQRPERN(L) + FNRLRPE*WQRPELN(L) + FNRLRPD*WQRPDLN(L) )`; `Eutrophication/mod_rpem.f90:487` — `+ FNLRPE*WQRPERN(L) + FNLLRPE*WQRPELN(L) + FNLLRPD*WQRPDLN(L) )`; `Eutrophication/mod_rpem.f90:491` — `+ FNDRPE*WQRPERN(L) + FNDLRPE*WQRPELN(L) + FNDLRPD*WQRPDLN(L) )`; `Eutrophication/mod_rpem.f90:495` — `+ FNIRPE*WQRPERN(L) + FNILRPE*WQRPELN(L) + FNILRPD*WQRPDLN(L) )`; EFDC_Theory_Document_Ver_12.pdf, PDF 213쪽·인쇄 200쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 214쪽·인쇄 201쪽)
- 영양염 흡수 water-vs-bed split: PO4 fraction EQ38(:508)·DIN fraction EQ45(:527) + ammonia preference EQ44A `PNRPS`(:536).
- 지상부 생산과 지상부·뿌리 호흡의 코드 온도함수는 음의 이차 지수함수이다. (`Eutrophication/mod_rpem.f90:1250` — `RPEMTPrps(NT) = EXP(-rKTP1RPS*(WTEMP-TP1RPS)*(WTEMP-TP1RPS) )`; `Eutrophication/mod_rpem.f90:1268` — `RPEMTRrps(NT) = EXP(-rKTR1RPS*(WTEMP-TR1RPS)*(WTEMP-TR1RPS) )`; `Eutrophication/mod_rpem.f90:1286` — `RPEMTRrpr(NT) = EXP(-rKTR1RPR*(WTEMP-TR1RPR)*(WTEMP-TR1RPR) )`; EFDC_Theory_Document_Ver_12.pdf, PDF 204쪽·인쇄 191쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 205쪽·인쇄 192쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 207쪽·인쇄 194쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 209쪽·인쇄 196쪽) Theory 식 8.150, 8.153, 8.158은 기준온도에 대한 선형 지수함수이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 204쪽·인쇄 191쪽, 식 8.150; EFDC_Theory_Document_Ver_12.pdf, PDF 205쪽·인쇄 192쪽, 식 8.153; EFDC_Theory_Document_Ver_12.pdf, PDF 207쪽·인쇄 194쪽, 식 8.158) Theory 식 8.168의 양의 이차 지수는 코드의 음의 이차 지수와 다르다. (`Eutrophication/mod_rpem.f90:1277` — `RPEMTRrpe(NT) = EXP(-rKTR1RPE*(WTEMP-TR1RPE)*(WTEMP-TR1RPE) )`; EFDC_Theory_Document_Ver_12.pdf, PDF 209쪽·인쇄 196쪽, 식 8.168)

## 6. 주요 findings (code≠manual, 개발자 주석 플래그)
- **"seed" floor**(:363 `max(WQRPS,0.2)`) — 재성장 보존용 수치 floor, 해석식 EQ1 에 없음.
- **total vs dissolved PO4 버그 플래그**(:508 `WQV(L,K,10)`=total PO4, 개발자 주석 "?? BUT (38) MEANS PO4DW, DISSOLVED ONLY").
- 코드는 WQRPDLN을 0으로 초기화한다. (`Eutrophication/mod_rpem.f90:1379` — `WQRPDLN  = 0`; EFDC_Theory_Document_Ver_12.pdf, PDF 213쪽·인쇄 200쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 214쪽·인쇄 201쪽) 확인한 mod_rpem.f90에는 이 변수의 추가 갱신 대입이 없다. (`Eutrophication/mod_rpem.f90:1379` — `WQRPDLN  = 0`; EFDC_Theory_Document_Ver_12.pdf, PDF 213쪽·인쇄 200쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 214쪽·인쇄 201쪽) 수주 RPON·LPON·DON·NH4 반환식은 WQRPDLN을 사용한다. (`Eutrophication/mod_rpem.f90:1379` — `WQRPDLN  = 0`; `Eutrophication/mod_rpem.f90:483` — `+ FNRRPE*WQRPERN(L) + FNRLRPE*WQRPELN(L) + FNRLRPD*WQRPDLN(L) )`; `Eutrophication/mod_rpem.f90:487` — `+ FNLRPE*WQRPERN(L) + FNLLRPE*WQRPELN(L) + FNLLRPD*WQRPDLN(L) )`; `Eutrophication/mod_rpem.f90:491` — `+ FNDRPE*WQRPERN(L) + FNDLRPE*WQRPELN(L) + FNDLRPD*WQRPDLN(L) )`; `Eutrophication/mod_rpem.f90:495` — `+ FNIRPE*WQRPERN(L) + FNILRPE*WQRPELN(L) + FNILRPD*WQRPDLN(L) )`; EFDC_Theory_Document_Ver_12.pdf, PDF 213쪽·인쇄 200쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 214쪽·인쇄 201쪽) 별도 영양염 흡수 경로의 존재만으로 쇄설물 질소 반환이 완결됐다고 판단하지 않는다. (`Eutrophication/mod_rpem.f90:1379` — `WQRPDLN  = 0`; `Eutrophication/mod_rpem.f90:483` — `+ FNRRPE*WQRPERN(L) + FNRLRPE*WQRPELN(L) + FNRLRPD*WQRPDLN(L) )`; `Eutrophication/mod_rpem.f90:487` — `+ FNLRPE*WQRPERN(L) + FNLLRPE*WQRPELN(L) + FNLLRPD*WQRPDLN(L) )`; `Eutrophication/mod_rpem.f90:491` — `+ FNDRPE*WQRPERN(L) + FNDLRPE*WQRPELN(L) + FNDLRPD*WQRPDLN(L) )`; `Eutrophication/mod_rpem.f90:495` — `+ FNIRPE*WQRPERN(L) + FNILRPE*WQRPELN(L) + FNILRPD*WQRPDLN(L) )`; EFDC_Theory_Document_Ver_12.pdf, PDF 213쪽·인쇄 200쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 214쪽·인쇄 201쪽) Theory 식 8.185, 8.187, 8.189, 8.191과 대조하면 쇄설물 질소의 비호흡 반환이 빠진다. (`Eutrophication/mod_rpem.f90:1379` — `WQRPDLN  = 0`; `Eutrophication/mod_rpem.f90:483` — `+ FNRRPE*WQRPERN(L) + FNRLRPE*WQRPELN(L) + FNRLRPD*WQRPDLN(L) )`; `Eutrophication/mod_rpem.f90:487` — `+ FNLRPE*WQRPERN(L) + FNLLRPE*WQRPELN(L) + FNLLRPD*WQRPDLN(L) )`; `Eutrophication/mod_rpem.f90:491` — `+ FNDRPE*WQRPERN(L) + FNDLRPE*WQRPELN(L) + FNDLRPD*WQRPDLN(L) )`; `Eutrophication/mod_rpem.f90:495` — `+ FNIRPE*WQRPERN(L) + FNILRPE*WQRPELN(L) + FNILRPD*WQRPDLN(L) )`; EFDC_Theory_Document_Ver_12.pdf, PDF 213쪽·인쇄 200쪽, 식 8.185; EFDC_Theory_Document_Ver_12.pdf, PDF 213쪽·인쇄 200쪽, 식 8.187; EFDC_Theory_Document_Ver_12.pdf, PDF 213쪽·인쇄 200쪽, 식 8.189; EFDC_Theory_Document_Ver_12.pdf, PDF 214쪽·인쇄 201쪽, 식 8.191)
- **ice 비활성**(:137-142): `ICECELL & HP<3·HDRY & ISICE>2` 시 kinetics off(운영규칙, 이론항 아님).
- **IJRPRS==0 constant 는 N<5 만 seed**(:332), 이후 persistence 의존(미문서).
- 코드는 NH4와 NO3의 선호 계산에 수주와 퇴적층 농도의 합을 사용한다. (`Eutrophication/mod_rpem.f90:536` — `TOP1 = (WQV(L,K,INHX) + SM2NH4(L))*(WQV(L,K,INOX) + SM2NO3(L))                ! WHY USE WATER COLUMN AND BED, BOTH OF THEM?`; EFDC_Theory_Document_Ver_12.pdf, PDF 214쪽·인쇄 201쪽) Theory 식 8.195는 단일 NH4와 NO3를 사용한다. (EFDC_Theory_Document_Ver_12.pdf, PDF 214쪽·인쇄 201쪽, 식 8.195) 코드가 서로 다른 매질의 농도를 합한다는 사실을 별도 기록한다. (`Eutrophication/mod_rpem.f90:536` — `TOP1 = (WQV(L,K,INHX) + SM2NH4(L))*(WQV(L,K,INOX) + SM2NO3(L))                ! WHY USE WATER COLUMN AND BED, BOTH OF THEM?`; EFDC_Theory_Document_Ver_12.pdf, PDF 214쪽·인쇄 201쪽)

## 7. Primary sources (equation 구조 기반, 소스는 "JI"=Zhen-Gang Ji 크레딧)
- **Cerco & Moore 2001** — SAV/epiphyte submodel(Chesapeake CE-QUAL-ICM, RPOC/LPOC/DOC 유기물 분배·epiphyte 구획의 직접 계보).
- **Madden & Kemp 1996** — 침수 macrophyte 생산 모델(shoot/root translocation·광적분).
- **Bowie et al. 1985**(EPA/600/3-85/040)·**Chapra 1997** — rate coefficient·kinetic form.
- 이 노트의 EQ1–45는 코드 주석 번호이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 206쪽·인쇄 193쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 197쪽·인쇄 184쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 214쪽·인쇄 201쪽) Theory v12의 해당 번호 범위는 식 8.124–8.197이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 197쪽·인쇄 184쪽, 식 8.124; EFDC_Theory_Document_Ver_12.pdf, PDF 214쪽·인쇄 201쪽, 식 8.197)

## 8. 관련
- [[efdc_water_quality]] — WQSKE1 eutrophication kinetics(RPEM 은 별 SAV submodel, 본 노트가 채움)
- [[efdc_linkages]] — RPEM 출력 payload(EE binary·HFRERPEMOUT)
- [[efdc_sedzlj]] — 바닥 diagenesis 풀 SM2NH4/NO3/PO4(F1 영양염·유기물 반환 결합)
