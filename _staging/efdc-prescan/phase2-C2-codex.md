# EFDC BATCH C2 semantic-review 판정안

old `3ed76b6e` → new `3b382fd0` (v12.5). 입력 12건만 검토한 Codex 제안이며 최종 판정은 Claude가 한다. 네트워크 없이 로컬 전문·patch·compare.json과 실제 노트 문맥을 대조했다.

기준: DESIGN-v2-DRAFT.md:82-103과 현재 사용자 지시. 코드의 의미 변화와 해당 wiki claim의 불일치를 구분한다. C1 기록의 공통 해석만 참고하고 개별 판정은 전파하지 않았다. REVIEW_ONLY는 문장 유지 및 필요한 인용 maintenance 검토 제안이며 모두 Claude 검토 대기다. 자동 수정·노트 전체 검증·migration 완료를 뜻하지 않는다.

집계: UPDATE_REQUIRED 4 / REVIEW_ONLY 7 / NO_ACTION 1 / UNRESOLVED_RULE_GAP 0.

## IINTPG 핵심 결론

공통 게이트는 `BSC>1.E-6 .and. KC>1`로 동일하다. 그 안에서 `IGRIDV==1`, `IGRIDV>1` 계산은 동일하다. 두 SGZ 조건이 거짓인 경로(문서의 표준 sigma `IGRIDV=0`; 코드 논리상 IGRIDV<=0)에 대한 비교다.

| 후보 | old | new | 제안 |
|---|---|---|---|
| C2-4 / 0 | IINTPG==0에서 표준식 | IINTPG 무관 else에서 동일 표준식 | UPDATE_REQUIRED: 계산 동일, 조건·선택 의미 확대 |
| C2-5 / 1 | 별도 JACOBIAN stencil | 전용 블록 삭제, 표준식 실행 | UPDATE_REQUIRED: 계산·실행 경로 변경 |
| C2-6 / 2 | 별도 FINITE VOLUME 식 | 전용 블록 삭제, 표준식 실행 | UPDATE_REQUIRED: 계산·실행 경로 변경 |

세 행 모두 SEMANTIC_CHANGE. C2-4는 IINTPG=0 결과가 바뀌었다는 판정이 아니다. 표 전체가 암시하는 IINTPG별 선택 구조가 더 이상 실제 로직을 표현하지 못한다는 판정이다. IINTPG가 모델 전체에서 무효라는 주장은 하지 않는다.

## C2-1 — NO_ACTION

- 노트: `models/EFDC/source-analysis/efdc_wetdry.md:48`
- 원문: - `HWET` = minimum operational depth for QSER withdrawals and structures, **not** the central rewetting threshold (`mod_var_global.f90:1053`).
- old 근거: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mod_var_global.f90:1048-1054
- new 근거: _staging/efdc-prescan/new/EFDC__mod_var_global.f90:1049-1055
- 변경 hunk (context 포함): @@ -1049,29 +1050,29 @@ MODULE GLOBAL [old intersection 1053-1053]
- 실제 변경: HWET 인용은 hunk의 context. 실제 변경은 인접 HMIN=0.01 초기값과 다른 선언 주석 정렬.
- 의미 차이: HWET 선언·withdrawal 최소 수심 의미 불변.
- 판정 이유: HWET old:1053=new:1054 동일. 이 변경은 HWET를 rewetting threshold로 바꾸지 않으며 structures 포함 기존 주장의 변경 근거도 없다. 해당 후보에 의미 수정 불필요.
- 신뢰도: high. 최종 disposition: Claude 검토 대기.

```text
old:1048:   real :: HDRY           !< If ISDRY > 0, this is the depth to control wetting and drying (m)
old:1049:   real :: HDRYMOVE       !< If ISDRY > 0, if this depth is > 0.0, then this is the minimum depth allowed for QSER inflows into a cell (m)
old:1050:   real :: HDRYWAV
old:1051:   real :: HDRYICE
old:1052:   real :: HMIN           !< Minimum water depth for initial conditions
old:1053:   real :: HWET           !< Minimum water depth to allow for QSER withdrawals
old:1054:   
new:1049:   real :: HDRY           !< If ISDRY > 0, this is the depth to control wetting and drying (m)
new:1050:   real :: HDRYMOVE       !< If ISDRY > 0, if this depth is > 0.0, then this is the minimum depth allowed for QSER inflows into a cell (m)
new:1051:   real :: HDRYWAV
new:1052:   real :: HDRYICE
new:1053:   real :: HMIN = 0.01    !< Minimum water depth for initial conditions
new:1054:   real :: HWET           !< Minimum water depth to allow for QSER withdrawals
new:1055:   
```

## C2-2 — REVIEW_ONLY

- 노트: `models/EFDC/source-analysis/efdc_vertical.md:21`
- 원문: - `aaefdc.f90:1294, 1308, 1323, 1332, 1341, 1435, 1443, 1448, 1492, 1497, 2382, 2592, 2610, 2820, 2944` — layer setup, SGZ allocation, face metrics.
- old 근거: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/aaefdc.f90:1301-1312
- new 근거: _staging/efdc-prescan/new/EFDC__aaefdc.f90:1302-1314
- 변경 hunk (context 포함): @@ -1301,10 +1302,11 @@ PROGRAM EFDC [old intersection 1308-1308]
- 실제 변경: SGZ 초기화 앞 master 전용 CONFIGURING HYDRODYNAMIC VARIABLES 출력 추가와 주석 대소문자 변경.
- 의미 차이: IGRIDV>0 조건 및 HMP 초기화 불변; old:1308→new:1310.
- 판정 이유: layer setup·SGZ allocation·face metrics라는 근거 설명은 유지된다. 인접 echo 추가 및 줄 이동만 반영 검토; 문장 유지 제안.
- 신뢰도: high. 최종 disposition: Claude 검토 대기.

```text
old:1301:   enddo
old:1302: 
old:1303:   ! ***************************************************************************
old:1304:   ! *** BEGIN SIGMA-Z VARIABLE INITIALIZATION (SGZ)
old:1305:   ! ***
old:1306:   ! *** Use ORIGINAL DEPTH FROM DXDY (HMP) SO KSZ'S ARE CONSISTENT FOR COLD START,
old:1307:   ! ***   RESTART AND CONTINUATION RUNS
old:1308:   if( IGRIDV > 0 )then
old:1309:     do L = 2,LA
old:1310:       HMP(L) = HP(L) + SGZHPDELTA
old:1311:     enddo
old:1312:   endif
new:1302:   enddo
new:1303: 
new:1304:   ! ***************************************************************************
new:1305:   ! *** Begin Sigma-Z variable initialization (SGZ)
new:1306:   ! ***
new:1307:   ! *** Use ORIGINAL DEPTH FROM DXDY (HMP) SO KSZ'S ARE CONSISTENT FOR COLD START,
new:1308:   ! ***   RESTART AND CONTINUATION RUNS
new:1309:   if( process_id == master_id ) write(*,'(A)')'CONFIGURING HYDRODYNAMIC VARIABLES'
new:1310:   if( IGRIDV > 0 )then
new:1311:     do L = 2,LA
new:1312:       HMP(L) = HP(L) + SGZHPDELTA
new:1313:     enddo
new:1314:   endif
```

## C2-3 — REVIEW_ONLY

- 노트: `models/EFDC/source-analysis/efdc_vertical.md:24`
- 원문: - `calexp.f90:243-406, 1152, 1169-1265` — vertical advection and PGF branches.
- old 근거: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1167-1170; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1187-1189; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1207-1208; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1225-1228; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1265-1268
- new 근거: _staging/efdc-prescan/new/EFDC__calexp.f90:1167-1170; _staging/efdc-prescan/new/EFDC__calexp.f90:1187-1189; _staging/efdc-prescan/new/EFDC__calexp.f90:1206-1222
- 변경 hunk (context 포함): @@ -1203,9 +1203,8 @@ SUBROUTINE CALEXP [old intersection 1203-1211]; @@ -1215,67 +1214,11 @@ SUBROUTINE CALEXP [old intersection 1215-1265]
- 실제 변경: IINTPG==0을 else로 교체하고 IINTPG==1/2 계산 블록 삭제.
- 의미 차이: 내부 PGF 선택 알고리즘은 변경됨. 다만 이 행은 vertical advection and PGF branches라는 일반 source-basis 문장이다.
- 판정 이유: 일반 근거 설명은 여전히 성립한다. 원래 범위 전체는 동일하지 않으므로 자동 줄 치환 금지. 구체적 0/1/2 선택 주장 수정은 별도 후보 C2-4/5/6에서 판정하며 이 행으로 전파하지 않는다. 문장 유지·인용 범위 재검토 제안.
- 신뢰도: high. 최종 disposition: Claude 검토 대기.

```text
old:1167:   if( BSC > 1.E-6 .and. KC > 1 )then
old:1168: 
old:1169:     if( IGRIDV == 1 )then
old:1170:       ! *** SIGMA-ZED BOUYANCY SHEARS
old:1187:     elseif( IGRIDV > 1 )then
old:1188:       ! *** SIGMA-ZED BOUYANCY SHEARS
old:1189:       !$OMP DO PRIVATE(ND,K,LP,L,LS,LW) 
old:1207:     elseif( IINTPG == 0 )then  
old:1208:       ! *** IINTPG = 0  
old:1225:     elseif( IINTPG == 1 )then
old:1226:       ! *** JACOBIAN
old:1227:       !$OMP SINGLE
old:1228:       K = 1
old:1265:     elseif( IINTPG == 2 )then
old:1266:       ! *** FINITE VOLUME
old:1267:       !$OMP SINGLE
old:1268:       do K = 1,KS
new:1167:   if( BSC > 1.E-6 .and. KC > 1 )then
new:1168: 
new:1169:     if( IGRIDV == 1 )then
new:1170:       ! *** SIGMA-ZED BOUYANCY SHEARS
new:1187:     elseif( IGRIDV > 1 )then
new:1188:       ! *** SIGMA-ZED BOUYANCY SHEARS
new:1189:       !$OMP DO PRIVATE(ND,K,LP,L,LS,LW) 
new:1206:     else
new:1207:       ! *** STANDARD-SIGMA BOUYANCY SHEARS
new:1208:       !$OMP DO PRIVATE(ND,LF,LL,K,LP,L,LS,LW) 
new:1209:       do ND = 1,NDM  
new:1210:         do K = 1,KS  
new:1211:         do LP = 1,LLWET(K,ND)
new:1212:           L  = LKWET(LP,K,ND)  
new:1213:             LS = LSC(L)
new:1214:             LW = LWC(L)
new:1215:             FBBX(L,K) = ROLD*FBBX(L,K) + RNEW*SBX(L)*GP*HU(L)*( HU(L)*( (B(L,K+1)-B(LW,K+1))*DZCK(K+1) + (B(L,K)-B(LW,K))*DZCK(K) ) - (B(L,K+1)-B(L,K)+B(LW,K+1)-B(LW,K))*(BELV(L)-BELV(LW)+Z(L,K)*(HP(L)-HP(LW))) )
new:1216:             FBBY(L,K) = ROLD*FBBY(L,K) + RNEW*SBY(L)*GP*HV(L)*( HV(L)*( (B(L,K+1)-B(LS,K+1))*DZCK(K+1) + (B(L,K)-B(LS,K))*DZCK(K) ) - (B(L,K+1)-B(L,K)+B(LS,K+1)-B(LS,K))*(BELV(L)-BELV(LS)+Z(L,K)*(HP(L)-HP(LS))) )
new:1217:           enddo
new:1218:         enddo
new:1219:       enddo
new:1220:       !$OMP END DO  
new:1221: 
new:1222:     endif
```

## C2-4 — UPDATE_REQUIRED

- 노트: `models/EFDC/source-analysis/efdc_vertical.md:80`
- 원문: | `0` | Standard density Jacobian | `calexp.f90:1207` |
- old 근거: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1167-1169; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1187-1188; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1207-1223
- new 근거: _staging/efdc-prescan/new/EFDC__calexp.f90:1167-1169; _staging/efdc-prescan/new/EFDC__calexp.f90:1187-1188; _staging/efdc-prescan/new/EFDC__calexp.f90:1206-1222
- 변경 hunk (context 포함): @@ -1203,9 +1203,8 @@ SUBROUTINE CALEXP [old intersection 1207-1207]
- 실제 변경: elseif(IINTPG==0)→IGRIDV 조건 체인의 else; 기존 표준 FBBX/FBBY 식 유지.
- 의미 차이: IINTPG=0, IGRIDV=0에서 계산은 동일하나 표준식의 실행 조건이 IINTPG와 무관하게 확대됨.
- 판정 이유: SEMANTIC_CHANGE: 조건식·분기 의미가 바뀌었다. old는 SGZ 두 조건 실패 AND IINTPG==0, new는 SGZ 두 조건 실패만 요구한다. 표의 0 전용 선택 구조는 독자를 오도한다(사용자 기준 ⑵·⑶). 0 입력에서 식이 같다는 사실만으로 줄 이동으로 분류할 수 없다.
- 신뢰도: high. 최종 disposition: Claude 검토 대기.

```text
old:1167:   if( BSC > 1.E-6 .and. KC > 1 )then
old:1168: 
old:1169:     if( IGRIDV == 1 )then
old:1187:     elseif( IGRIDV > 1 )then
old:1188:       ! *** SIGMA-ZED BOUYANCY SHEARS
old:1207:     elseif( IINTPG == 0 )then  
old:1208:       ! *** IINTPG = 0  
old:1209:       !$OMP DO PRIVATE(ND,LF,LL,K,LP,L,LS,LW) 
old:1210:       do ND = 1,NDM  
old:1211:         do K = 1,KS  
old:1212:         do LP = 1,LLWET(K,ND)
old:1213:           L  = LKWET(LP,K,ND)  
old:1214:             LS = LSC(L)
old:1215:             LW = LWC(L)
old:1216:             FBBX(L,K) = ROLD*FBBX(L,K) + RNEW*SBX(L)*GP*HU(L)*( HU(L)*( (B(L,K+1)-B(LW,K+1))*DZCK(K+1) + (B(L,K)-B(LW,K))*DZCK(K) ) - (B(L,K+1)-B(L,K)+B(LW,K+1)-B(LW,K))*(BELV(L)-BELV(LW)+Z(L,K)*(HP(L)-HP(LW))) )
old:1217:             FBBY(L,K) = ROLD*FBBY(L,K) + RNEW*SBY(L)*GP*HV(L)*( HV(L)*( (B(L,K+1)-B(LS,K+1))*DZCK(K+1) + (B(L,K)-B(LS,K))*DZCK(K) ) - (B(L,K+1)-B(L,K)+B(LS,K+1)-B(LS,K))*(BELV(L)-BELV(LS)+Z(L,K)*(HP(L)-HP(LS))) )
old:1218:             !FBBX(L,K) = SUBD(L)*FBBX(L,K)                                    
old:1219:             !FBBY(L,K) = SVBD(L)*FBBY(L,K)                                    
old:1220:           enddo
old:1221:         enddo
old:1222:       enddo
old:1223:       !$OMP END DO  
new:1167:   if( BSC > 1.E-6 .and. KC > 1 )then
new:1168: 
new:1169:     if( IGRIDV == 1 )then
new:1187:     elseif( IGRIDV > 1 )then
new:1188:       ! *** SIGMA-ZED BOUYANCY SHEARS
new:1206:     else
new:1207:       ! *** STANDARD-SIGMA BOUYANCY SHEARS
new:1208:       !$OMP DO PRIVATE(ND,LF,LL,K,LP,L,LS,LW) 
new:1209:       do ND = 1,NDM  
new:1210:         do K = 1,KS  
new:1211:         do LP = 1,LLWET(K,ND)
new:1212:           L  = LKWET(LP,K,ND)  
new:1213:             LS = LSC(L)
new:1214:             LW = LWC(L)
new:1215:             FBBX(L,K) = ROLD*FBBX(L,K) + RNEW*SBX(L)*GP*HU(L)*( HU(L)*( (B(L,K+1)-B(LW,K+1))*DZCK(K+1) + (B(L,K)-B(LW,K))*DZCK(K) ) - (B(L,K+1)-B(L,K)+B(LW,K+1)-B(LW,K))*(BELV(L)-BELV(LW)+Z(L,K)*(HP(L)-HP(LW))) )
new:1216:             FBBY(L,K) = ROLD*FBBY(L,K) + RNEW*SBY(L)*GP*HV(L)*( HV(L)*( (B(L,K+1)-B(LS,K+1))*DZCK(K+1) + (B(L,K)-B(LS,K))*DZCK(K) ) - (B(L,K+1)-B(L,K)+B(LS,K+1)-B(LS,K))*(BELV(L)-BELV(LS)+Z(L,K)*(HP(L)-HP(LS))) )
new:1217:           enddo
new:1218:         enddo
new:1219:       enddo
new:1220:       !$OMP END DO  
new:1221: 
new:1222:     endif
```

## C2-5 — UPDATE_REQUIRED

- 노트: `models/EFDC/source-analysis/efdc_vertical.md:81`
- 원문: | `1` | Improved sigma-slope correction | `calexp.f90:1225` |
- old 근거: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1225-1236; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1239-1242; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1252-1265
- new 근거: _staging/efdc-prescan/new/EFDC__calexp.f90:1206-1222
- 변경 hunk (context 포함): @@ -1215,67 +1214,11 @@ SUBROUTINE CALEXP [old intersection 1225-1225]
- 실제 변경: IINTPG==1 JACOBIAN 전용 계산 및 OMP SINGLE 블록 삭제.
- 의미 차이: 표준 sigma에서 IINTPG=1도 기존 0의 DZCK 기반 표준식 실행; 기존 별도 stencil 선택 소멸.
- 판정 이유: SEMANTIC_CHANGE: Improved sigma-slope correction을 IINTPG=1로 선택한다는 표의 주장이 새 CALEXP와 불일치. 기존 K+2 등을 포함하는 계산이 이동한 것이 아니라 삭제됐다. 이 명칭의 기존 타당성 자체는 재판정하지 않는다.
- 신뢰도: high. 최종 disposition: Claude 검토 대기.

```text
old:1225:     elseif( IINTPG == 1 )then
old:1226:       ! *** JACOBIAN
old:1227:       !$OMP SINGLE
old:1228:       K = 1
old:1229:       do L = 2,LA
old:1230:         LW = LWC(L)
old:1231:         LS = LSC(L)
old:1232:         FBBX(L,K) = ROLD*FBBX(L,K) + RNEW*SBX(L)*GP*HU(L)*( 0.5*HU(L)*( (B(L,K+2)-B(LW,K+2))*DZC(L,K+2)+(B(L,K+1)-B(LW,K+1))*DZC(L,K+1)+(B(L,K  )-B(LW,K  ))*DZC(L,K  )+(B(L,K  )-B(LW,K  ))*DZC(L,K  ) ) &
old:1233:                    -0.5*(B(L,K+2)-B(L,K+1)+B(LW,K+2)-B(LW,K+1))*(BELV(L)-BELV(LW)+Z(L,K+1)*(HP(L)-HP(LW)))-0.5*(B(L,K  )-B(L,K  )+B(LW,K  )-B(LW,K  ))*(BELV(L)-BELV(LW)+Z(L,K-1)*(HP(L)-HP(LW))) )
old:1234:   
old:1235:         FBBY(L,K) = ROLD*FBBY(L,K) + RNEW*SBY(L)*GP*HV(L)*( 0.5*HV(L)*( (B(L,K+2)-B(LS ,K+2))*DZC(L,K+2)+(B(L,K+1)-B(LS ,K+1))*DZC(L,K+1)+(B(L,K  )-B(LS ,K  ))*DZC(L,K  )+(B(L,K  )-B(LS ,K  ))*DZC(L,K  ) ) &
old:1236:                    -0.5*(B(L,K+2)-B(L,K+1)+B(LS ,K+2)-B(LS ,K+1))*(BELV(L)-BELV(LS)+Z(L,K+1)*(HP(L)-HP(LS)))-0.5*(B(L,K  )-B(L,K  )+B(LS ,K  )-B(LS ,K  ))*(BELV(L)-BELV(LS )+Z(L,K-1)*(HP(L)-HP(LS ))) )
old:1239:       if( KC > 2 )then
old:1240:         K = KS
old:1241:         do L = 2,LA
old:1242:           LW = LWC(L)
old:1252:         do K = 1,KS
old:1253:           do L = 2,LA
old:1254:             LW = LWC(L)
old:1255:             LS = LSC(L)
old:1256:             FBBX(L,K) = ROLD*FBBX(L,K) + RNEW*SBX(L)*GP*HU(L)*( 0.5*HU(L)*( (B(L,K+2)-B(LW,K+2))*DZC(L,K+2)+(B(L,K+1)-B(LW,K+1))*DZC(L,K+1)+(B(L,K  )-B(LW,K  ))*DZC(L,K  )+(B(L,K-1)-B(LW,K-1))*DZC(L,K-1) ) &
old:1257:                        -0.5*(B(L,K+2)-B(L,K+1)+B(LW,K+2)-B(LW,K+1))*(BELV(L)-BELV(LW)+Z(L,K+1)*(HP(L)-HP(LW)))-0.5*(B(L,K  )-B(L,K-1)+B(LW,K  )-B(LW,K-1))*(BELV(L)-BELV(LW)+Z(L,K-1)*(HP(L)-HP(LW))) )
old:1258:             FBBY(L,K) = ROLD*FBBY(L,K) + RNEW*SBY(L)*GP*HV(L)*( 0.5*HV(L)*( (B(L,K+2)-B(LS ,K+2))*DZC(L,K+2)+(B(L,K+1)-B(LS ,K+1))*DZC(L,K+1)+(B(L,K  )-B(LS ,K  ))*DZC(L,K  )+(B(L,K-1)-B(LS ,K-1))*DZC(L,K-1) ) &
old:1259:                        -0.5*(B(L,K+2)-B(L,K+1)+B(LS ,K+2)-B(LS ,K+1))*(BELV(L)-BELV(LS)+Z(L,K+1)*(HP(L)-HP(LS)))-0.5*(B(L,K  )-B(L,K-1)+B(LS ,K  )-B(LS ,K-1))*(BELV(L)-BELV(LS )+Z(L,K-1)*(HP(L)-HP(LS ))) )
old:1260:           enddo
old:1261:         enddo
old:1262:       endif
old:1263:       !$OMP END SINGLE
old:1264:         
old:1265:     elseif( IINTPG == 2 )then
new:1206:     else
new:1207:       ! *** STANDARD-SIGMA BOUYANCY SHEARS
new:1208:       !$OMP DO PRIVATE(ND,LF,LL,K,LP,L,LS,LW) 
new:1209:       do ND = 1,NDM  
new:1210:         do K = 1,KS  
new:1211:         do LP = 1,LLWET(K,ND)
new:1212:           L  = LKWET(LP,K,ND)  
new:1213:             LS = LSC(L)
new:1214:             LW = LWC(L)
new:1215:             FBBX(L,K) = ROLD*FBBX(L,K) + RNEW*SBX(L)*GP*HU(L)*( HU(L)*( (B(L,K+1)-B(LW,K+1))*DZCK(K+1) + (B(L,K)-B(LW,K))*DZCK(K) ) - (B(L,K+1)-B(L,K)+B(LW,K+1)-B(LW,K))*(BELV(L)-BELV(LW)+Z(L,K)*(HP(L)-HP(LW))) )
new:1216:             FBBY(L,K) = ROLD*FBBY(L,K) + RNEW*SBY(L)*GP*HV(L)*( HV(L)*( (B(L,K+1)-B(LS,K+1))*DZCK(K+1) + (B(L,K)-B(LS,K))*DZCK(K) ) - (B(L,K+1)-B(L,K)+B(LS,K+1)-B(LS,K))*(BELV(L)-BELV(LS)+Z(L,K)*(HP(L)-HP(LS))) )
new:1217:           enddo
new:1218:         enddo
new:1219:       enddo
new:1220:       !$OMP END DO  
new:1221: 
new:1222:     endif
```

## C2-6 — UPDATE_REQUIRED

- 노트: `models/EFDC/source-analysis/efdc_vertical.md:82`
- 원문: | `2` | Finite-volume formulation | `calexp.f90:1265` |
- old 근거: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1265-1279
- new 근거: _staging/efdc-prescan/new/EFDC__calexp.f90:1206-1222
- 변경 hunk (context 포함): @@ -1215,67 +1214,11 @@ SUBROUTINE CALEXP [old intersection 1265-1265]
- 실제 변경: IINTPG==2 FINITE VOLUME 전용 계산 및 OMP SINGLE 블록 삭제.
- 의미 차이: 표준 sigma에서 IINTPG=2도 표준식 실행; HP*B와 ZZ를 사용하는 기존 finite-volume 식 선택 소멸.
- 판정 이유: SEMANTIC_CHANGE: IINTPG=2로 finite-volume formulation을 선택한다는 주장이 새 CALEXP와 불일치. 독립 분기와 계산이 삭제돼 실행 경로가 달라졌다.
- 신뢰도: high. 최종 disposition: Claude 검토 대기.

```text
old:1265:     elseif( IINTPG == 2 )then
old:1266:       ! *** FINITE VOLUME
old:1267:       !$OMP SINGLE
old:1268:       do K = 1,KS
old:1269:         do L = 2,LA
old:1270:           LW = LWC(L)
old:1271:           LS = LSC(L)
old:1272:           FBBX(L,K) = ROLD*FBBX(L,K) + RNEW*SBX(L)*GP*HU(L)*( ( HP(L)*B(L,K+1)-HP(LW)*B(LW,K+1) )*DZC(L,K+1)+( HP(L)*B(L,K  )-HP(LW)*B(LW,K  ) )*DZC(L,K  ) )-RNEW*SBX(L)*GP*(BELV(L)-BELV(LW)) &
old:1273:                      *( HP(L)*B(L,K+1)-HP(L)*B(L,K)+HP(LW)*B(LW,K+1)-HP(LW)*B(LW,K) )   - RNEW*SBX(L)*GP*(HP(L)-HP(LW))*( HP(L)*ZZ(L,K+1)*B(L,K+1)-HP(L)*ZZ(L,K)*B(L,K)+HP(LW)*ZZ(L,K+1)*B(LW,K+1)-HP(LW)*ZZ(L,K)*B(LW,K) )
old:1274:           FBBY(L,K) = ROLD*FBBY(L,K) + RNEW*SBY(L)*GP*HV(L)*( ( HP(L)*B(L,K+1)-HP(LS )*B(LS ,K+1) )*DZC(L,K+1)+( HP(L)*B(L,K  )-HP(LS )*B(LS ,K  ) )*DZC(L,K  ) )-RNEW*SBY(L)*GP*(BELV(L)-BELV(LS )) &
old:1275:                      *( HP(L)*B(L,K+1)-HP(L)*B(L,K)+HP(LS)*B(LS ,K+1)-HP(LS)*B(LS ,K) ) - RNEW*SBY(L)*GP*(HP(L)-HP(LS ))*( HP(L)*ZZ(L,K+1)*B(L,K+1)-HP(L)*ZZ(L,K)*B(L,K)+HP(LS)*ZZ(L,K+1)*B(LS ,K+1)-HP(LS)*ZZ(L,K)*B(LS ,K) )
old:1276:         enddo
old:1277:       enddo
old:1278:       !$OMP END SINGLE
old:1279:     endif
new:1206:     else
new:1207:       ! *** STANDARD-SIGMA BOUYANCY SHEARS
new:1208:       !$OMP DO PRIVATE(ND,LF,LL,K,LP,L,LS,LW) 
new:1209:       do ND = 1,NDM  
new:1210:         do K = 1,KS  
new:1211:         do LP = 1,LLWET(K,ND)
new:1212:           L  = LKWET(LP,K,ND)  
new:1213:             LS = LSC(L)
new:1214:             LW = LWC(L)
new:1215:             FBBX(L,K) = ROLD*FBBX(L,K) + RNEW*SBX(L)*GP*HU(L)*( HU(L)*( (B(L,K+1)-B(LW,K+1))*DZCK(K+1) + (B(L,K)-B(LW,K))*DZCK(K) ) - (B(L,K+1)-B(L,K)+B(LW,K+1)-B(LW,K))*(BELV(L)-BELV(LW)+Z(L,K)*(HP(L)-HP(LW))) )
new:1216:             FBBY(L,K) = ROLD*FBBY(L,K) + RNEW*SBY(L)*GP*HV(L)*( HV(L)*( (B(L,K+1)-B(LS,K+1))*DZCK(K+1) + (B(L,K)-B(LS,K))*DZCK(K) ) - (B(L,K+1)-B(L,K)+B(LS,K+1)-B(LS,K))*(BELV(L)-BELV(LS)+Z(L,K)*(HP(L)-HP(LS))) )
new:1217:           enddo
new:1218:         enddo
new:1219:       enddo
new:1220:       !$OMP END DO  
new:1221: 
new:1222:     endif
```

## C2-7 — REVIEW_ONLY

- 노트: `models/EFDC/source-analysis/efdc_sediment_diagenesis.md:21`
- 원문: > ★**line range 정정**: water_quality:21 은 `mod_diagen.f90:9-1031` 이라 했으나 module `END`는 :1107, **flux kernel(SEDFLUXNEW/ZBRENT/SOLVSMBE)은 :1121-1393** — stale 인용은 solver 전체를 놓침.
- old 근거: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:164-169; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:336-341; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:1105-1108; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:1121-1122; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:1391-1394
- new 근거: _staging/efdc-prescan/new/EFDC__Eutrophication__mod_diagen.f90:164-168; _staging/efdc-prescan/new/EFDC__Eutrophication__mod_diagen.f90:335-339; _staging/efdc-prescan/new/EFDC__Eutrophication__mod_diagen.f90:1103-1106; _staging/efdc-prescan/new/EFDC__Eutrophication__mod_diagen.f90:1119-1120; _staging/efdc-prescan/new/EFDC__Eutrophication__mod_diagen.f90:1389-1392
- 변경 hunk (context 포함): @@ -164,7 +164,6 @@ SUBROUTINE SMRIN1_JNP [old intersection 164-170]; @@ -336,7 +335,6 @@ SUBROUTINE SMRIN1_JNP [old intersection 336-342]
- 실제 변경: 인용 broad span에서 write_restart_option→ISMRST 읽기 및 broadcast 삭제.
- 의미 차이: 입력 schema 변화는 있으나 이 후보 주장은 module END와 외부 flux kernel 위치에 대한 인용 범위 정정이다. kernel 전문은 동일하고 -2줄 이동.
- 판정 이유: old:340-1394=new:338-1392 동일. module END 1107→1105, kernel 1121-1393→1119-1391. 기존 9-1031 범위가 solver를 놓친다는 요지는 유지된다. 입력 schema 판정을 이 범위 정정 문장으로 전파하지 않으며 좌표 maintenance 검토 제안.
- 신뢰도: high. 최종 disposition: Claude 검토 대기.

```text
old:164:     call fson_get(json_data, "title", TITLE)
old:165:     call fson_get(json_data, "initial_condition_option", ISMICI)
old:166:     call fson_get(json_data, "number_of_spatial_zones", ISMZ)
old:167:     call fson_get(json_data, "write_restart_option", ISMRST)
old:168:     call fson_get(json_data, "sediment_temperature_diffusion_coef", SMDIFT)
old:169:     call fson_get(json_data, "stoichiometric_coef_for_carbon_diagenesis.nitrification", SMO2NH4)
old:336:   call Broadcast_Scalar(ISMZ,     master_id)
old:337:   call Broadcast_Scalar(NSMZ,     master_id)
old:338:   call Broadcast_Scalar(ISMICI,   master_id)
old:339:   call Broadcast_Scalar(ISMRST,   master_id)
old:340:   call Broadcast_Scalar(ISMHYST,  master_id)
old:341:   call Broadcast_Scalar(ISMZB,    master_id)
old:1105:   END SUBROUTINE SMMBE
old:1106: 
old:1107:   END MODULE WQ_DIAGENESIS
old:1108:   
old:1121:   SUBROUTINE SOLVSMBE(SMV1,SMV2,SMA11,SMA22,SMA1,SMA2,SMB11,SMB22)  
old:1122: 
old:1391: 
old:1392:   return
old:1393:   END
old:1394: 
new:164:     call fson_get(json_data, "title", TITLE)
new:165:     call fson_get(json_data, "initial_condition_option", ISMICI)
new:166:     call fson_get(json_data, "number_of_spatial_zones", ISMZ)
new:167:     call fson_get(json_data, "sediment_temperature_diffusion_coef", SMDIFT)
new:168:     call fson_get(json_data, "stoichiometric_coef_for_carbon_diagenesis.nitrification", SMO2NH4)
new:335:   call Broadcast_Scalar(ISMZ,     master_id)
new:336:   call Broadcast_Scalar(NSMZ,     master_id)
new:337:   call Broadcast_Scalar(ISMICI,   master_id)
new:338:   call Broadcast_Scalar(ISMHYST,  master_id)
new:339:   call Broadcast_Scalar(ISMZB,    master_id)
new:1103:   END SUBROUTINE SMMBE
new:1104: 
new:1105:   END MODULE WQ_DIAGENESIS
new:1106:   
new:1119:   SUBROUTINE SOLVSMBE(SMV1,SMV2,SMA11,SMA22,SMA1,SMA2,SMB11,SMB22)  
new:1120: 
new:1389: 
new:1390:   return
new:1391:   END
new:1392: 
```

## C2-8 — REVIEW_ONLY

- 노트: `models/EFDC/source-analysis/efdc_hydro_core.md:79`
- 원문: - CALEXP adds non-hydrostatic pressure-gradient term (`calexp.f90:1010, 1052-1055`).
- old 근거: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1010-1028; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1052-1055
- new 근거: _staging/efdc-prescan/new/EFDC__calexp.f90:1010-1028; _staging/efdc-prescan/new/EFDC__calexp.f90:1052-1055
- 변경 hunk (context 포함): @@ -1008,10 +1008,10 @@ SUBROUTINE CALEXP [old intersection 1010-1010]
- 실제 변경: 비정수압 DZPC 경계 계산의 LLWET/LKWET 인덱스 K→KC; 첫 OMP PRIVATE에서 K 제거.
- 의미 차이: 경계 계산 대상 셀 선택은 변경됐다. KC>1 AND ISPNHYDS>=1 게이트와 FX/FY 압력구배 가산식은 동일.
- 판정 이유: 노트는 특정 wet-list 인덱스나 계산 정확성을 주장하지 않고 비정수압 항을 가산한다고 설명한다. 가산 동작은 유지되므로 문장 유지 제안. new:1014의 유효성 미검증 주석도 보존하며 수치적 bugfix 성공을 단정하지 않는다.
- 신뢰도: high. 최종 disposition: Claude 검토 대기.

```text
old:1010:   if( KC > 1 .and. ISPNHYDS >= 1 )then
old:1011:     !$OMP DO PRIVATE(ND,L,LP,K,TMPVAL) 
old:1012:     do ND = 1,NDM  
old:1013:       do LP = 1,LLWET(K,ND)
old:1014:         L = LKWET(LP,K,ND)  
old:1015:         TMPVAL    = 2./( DZC(L,KSZ(L)) + DZC(L,KSZ(L)+1) )
old:1016:         DZPC(L,1) = TMPVAL*(PNHYDS(L,2)-PNHYDS(L,1))
old:1017:       enddo
old:1018:     enddo  
old:1019:     !$OMP END DO
old:1020:   
old:1021:     !$OMP DO PRIVATE(ND,L,LP,TMPVAL) 
old:1022:     do ND = 1,NDM  
old:1023:       do LP = 1,LLWET(K,ND)
old:1024:         L = LKWET(LP,K,ND)  
old:1025:         TMPVAL     = 2./( DZC(L,KC) + DZC(L,KC-1) )
old:1026:         DZPC(L,KC) = TMPVAL*(PNHYDS(L,KC)-PNHYDS(L,KC-1))
old:1027:       enddo
old:1028:     enddo  
old:1052:           DZPU = 0.5*(DZPC(L,K)+DZPC(LW,K))
old:1053:           DZPV = 0.5*(DZPC(L,K)+DZPC(LS,K))
old:1054:           FX(L,K) = FX(L,K) + SUB3D(L,K)*DYU(L)*( HU(L)*(PNHYDS(L,K)-PNHYDS(LW,K) ) - ( BELV(L)-BELV(LW) + ZZ(L,K) *(HP(L)-HP(LW)) )*DZPU )
old:1055:           FY(L,K) = FY(L,K) + SVB3D(L,K)*DXV(L)*( HV(L)*(PNHYDS(L,K)-PNHYDS(LS,K) ) - ( BELV(L)-BELV(LS) + ZZ(LS,K)*(HP(L)-HP(LS)) )*DZPV )
new:1010:   if( KC > 1 .and. ISPNHYDS >= 1 )then
new:1011:     !$OMP DO PRIVATE(ND,L,LP,TMPVAL) 
new:1012:     do ND = 1,NDM  
new:1013:       do LP = 1,LLWET(KC,ND)
new:1014:         L = LKWET(LP,KC,ND)     ! Kien - I don't think this is valid but we don't have a test case to check
new:1015:         TMPVAL    = 2./( DZC(L,KSZ(L)) + DZC(L,KSZ(L)+1) )
new:1016:         DZPC(L,1) = TMPVAL*(PNHYDS(L,2)-PNHYDS(L,1))
new:1017:       enddo
new:1018:     enddo  
new:1019:     !$OMP END DO
new:1020:   
new:1021:     !$OMP DO PRIVATE(ND,L,LP,TMPVAL) 
new:1022:     do ND = 1,NDM  
new:1023:       do LP = 1,LLWET(KC,ND)
new:1024:         L = LKWET(LP,KC,ND)  
new:1025:         TMPVAL     = 2./( DZC(L,KC) + DZC(L,KC-1) )
new:1026:         DZPC(L,KC) = TMPVAL*(PNHYDS(L,KC)-PNHYDS(L,KC-1))
new:1027:       enddo
new:1028:     enddo  
new:1052:           DZPU = 0.5*(DZPC(L,K)+DZPC(LW,K))
new:1053:           DZPV = 0.5*(DZPC(L,K)+DZPC(LS,K))
new:1054:           FX(L,K) = FX(L,K) + SUB3D(L,K)*DYU(L)*( HU(L)*(PNHYDS(L,K)-PNHYDS(LW,K) ) - ( BELV(L)-BELV(LW) + ZZ(L,K) *(HP(L)-HP(LW)) )*DZPU )
new:1055:           FY(L,K) = FY(L,K) + SVB3D(L,K)*DXV(L)*( HV(L)*(PNHYDS(L,K)-PNHYDS(LS,K) ) - ( BELV(L)-BELV(LS) + ZZ(LS,K)*(HP(L)-HP(LS)) )*DZPV )
```

## C2-9 — UPDATE_REQUIRED

- 노트: `models/EFDC/source-analysis/efdc_baroclinic_eos.md:75`
- 원문: ## 4. 내부모드 buoyancy shear FBBX/FBBY (calexp.f90:1162-1352)
- old 근거: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1162-1169; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1187-1188; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1207-1208; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1225-1228; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1265-1270; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calexp.f90:1350-1352
- new 근거: _staging/efdc-prescan/new/EFDC__calexp.f90:1162-1169; _staging/efdc-prescan/new/EFDC__calexp.f90:1187-1188; _staging/efdc-prescan/new/EFDC__calexp.f90:1206-1222; _staging/efdc-prescan/new/EFDC__calexp.f90:1293-1295
- 변경 hunk (context 포함): @@ -1203,9 +1203,8 @@ SUBROUTINE CALEXP [old intersection 1203-1211]; @@ -1215,67 +1214,11 @@ SUBROUTINE CALEXP [old intersection 1215-1281]
- 실제 변경: 내부 buoyancy shear의 IINTPG 3-way sigma 선택 삭제.
- 의미 차이: 해당 절 note:77-83은 IINTPG 0/1/2를 서로 다른 형식으로 명시. 새 분기는 IGRIDV에 따라 SGZ 둘과 표준 sigma else로 구성.
- 판정 이유: SEMANTIC_CHANGE: 제목 아래 실질 주장(note:77-83)의 IINTPG 3형식 선택이 새 소스와 불일치. 표준식은 유지되나 1/2 전용 계산은 삭제되므로 절의 선택 구조 설명 수정 필요. note:90은 같은 주장의 문맥이며 별도 후보로 확대하지 않는다.
- 신뢰도: high. 최종 disposition: Claude 검토 대기.

```text
old:1162:   ! *** CALCULATE EXPLICIT INTERNAL BUOYANCY FORCINGS CENTERED AT N FOR
old:1163:   ! *** THREE TIME LEVEL STEP AND AT (N+1/2) FOR TWO TIME LEVEL STEP
old:1164:   ! *** SBX = SBX*0.5*DYU & SBY = SBY*0.5*DXV
old:1165:   !
old:1166:   !----------------------------------------------------------------------C
old:1167:   if( BSC > 1.E-6 .and. KC > 1 )then
old:1168: 
old:1169:     if( IGRIDV == 1 )then
old:1187:     elseif( IGRIDV > 1 )then
old:1188:       ! *** SIGMA-ZED BOUYANCY SHEARS
old:1207:     elseif( IINTPG == 0 )then  
old:1208:       ! *** IINTPG = 0  
old:1225:     elseif( IINTPG == 1 )then
old:1226:       ! *** JACOBIAN
old:1227:       !$OMP SINGLE
old:1228:       K = 1
old:1265:     elseif( IINTPG == 2 )then
old:1266:       ! *** FINITE VOLUME
old:1267:       !$OMP SINGLE
old:1268:       do K = 1,KS
old:1269:         do L = 2,LA
old:1270:           LW = LWC(L)
old:1350:     endif
old:1351: 
old:1352:   endif  ! *** END OF BOUYANCY
new:1162:   ! *** CALCULATE EXPLICIT INTERNAL BUOYANCY FORCINGS CENTERED AT N FOR
new:1163:   ! *** THREE TIME LEVEL STEP AND AT (N+1/2) FOR TWO TIME LEVEL STEP
new:1164:   ! *** SBX = SBX*0.5*DYU & SBY = SBY*0.5*DXV
new:1165:   !
new:1166:   !----------------------------------------------------------------------C
new:1167:   if( BSC > 1.E-6 .and. KC > 1 )then
new:1168: 
new:1169:     if( IGRIDV == 1 )then
new:1187:     elseif( IGRIDV > 1 )then
new:1188:       ! *** SIGMA-ZED BOUYANCY SHEARS
new:1206:     else
new:1207:       ! *** STANDARD-SIGMA BOUYANCY SHEARS
new:1208:       !$OMP DO PRIVATE(ND,LF,LL,K,LP,L,LS,LW) 
new:1209:       do ND = 1,NDM  
new:1210:         do K = 1,KS  
new:1211:         do LP = 1,LLWET(K,ND)
new:1212:           L  = LKWET(LP,K,ND)  
new:1213:             LS = LSC(L)
new:1214:             LW = LWC(L)
new:1215:             FBBX(L,K) = ROLD*FBBX(L,K) + RNEW*SBX(L)*GP*HU(L)*( HU(L)*( (B(L,K+1)-B(LW,K+1))*DZCK(K+1) + (B(L,K)-B(LW,K))*DZCK(K) ) - (B(L,K+1)-B(L,K)+B(LW,K+1)-B(LW,K))*(BELV(L)-BELV(LW)+Z(L,K)*(HP(L)-HP(LW))) )
new:1216:             FBBY(L,K) = ROLD*FBBY(L,K) + RNEW*SBY(L)*GP*HV(L)*( HV(L)*( (B(L,K+1)-B(LS,K+1))*DZCK(K+1) + (B(L,K)-B(LS,K))*DZCK(K) ) - (B(L,K+1)-B(L,K)+B(LS,K+1)-B(LS,K))*(BELV(L)-BELV(LS)+Z(L,K)*(HP(L)-HP(LS))) )
new:1217:           enddo
new:1218:         enddo
new:1219:       enddo
new:1220:       !$OMP END DO  
new:1221: 
new:1222:     endif
new:1293:     endif
new:1294: 
new:1295:   endif  ! *** END OF BOUYANCY
```

## C2-10 — REVIEW_ONLY

- 노트: `models/EFDC/source-analysis/sediment/efdc_sediment.md:21`
- 원문: - `SedTran-Original/ssedtox.f90:868-1287` — runtime dispatch.
- old 근거: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-Original/ssedtox.f90:868-885; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-Original/ssedtox.f90:1031-1062; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-Original/ssedtox.f90:1078-1100; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-Original/ssedtox.f90:1282-1287
- new 근거: _staging/efdc-prescan/new/EFDC__SedTran-Original__ssedtox.f90:863-880; _staging/efdc-prescan/new/EFDC__SedTran-Original__ssedtox.f90:1026-1053; _staging/efdc-prescan/new/EFDC__SedTran-Original__ssedtox.f90:1069-1091; _staging/efdc-prescan/new/EFDC__SedTran-Original__ssedtox.f90:1273-1278
- 변경 hunk (context 포함): @@ -1031,18 +1026,16 @@ SUBROUTINE SSEDTOX [old intersection 1031-1048]; @@ -1052,11 +1045,9 @@ SUBROUTINE SSEDTOX [old intersection 1052-1062]; @@ -1078,21 +1069,21 @@ SUBROUTINE SSEDTOX [old intersection 1078-1098]
- 실제 변경: HBED/MINTHICK·void ratio 보호의 K==1 제한 제거 및 압밀 후 VDRBED 범위 제한 추가.
- 의미 차이: 퇴적층 보정 동작은 달라졌으나 ISTRAN(6)/LSEDZLJ→SEDZLJ_MAIN 또는 CALSED, ISTRAN(7)→CALSND 호출 관계 유지.
- 판정 이유: runtime dispatch라는 요약과 그 호출 조건은 유지된다. broad span 내부 bed 보정 변경은 기록하되 runtime dispatch 문장 수정 대상으로 전파하지 않는다. 인용 범위 재검토·문장 유지 제안.
- 신뢰도: high. 최종 disposition: Claude 검토 대기.

```text
old:868:   if( ISTRAN(6) >= 1 )then
old:869:     if( LSEDZLJ )then
old:870:       call SEDZLJ_MAIN
old:871:       GOTO 1000  ! *** BYPASS ORIGINAL BED/WATER INTERFACE CALCULATION
old:872:     else
old:873:       call CALSED
old:874:     endif
old:875:   endif
old:876:                             
old:877:   ! ***********************************************************************C                                                
old:878:   ! *** CALCULATE NONCOHESIVE SEDIMENT BEDLOAD TRANSPORT, SETTLING,                                                       
old:879:   ! *** DEPOSITION AND RESUSPENSION                                                                                       
old:880:   if( ISTRAN(7) >= 1 ) CALL CALSND
old:881:                           
old:882:   ! ***********************************************************************C                                                
old:883:   ! *** CALCULATE BANK EROSION AND ADJUST SEDIMENT AND WATER VOLUME FLUXES                                                                                                            
old:884:   if( ISTRAN(6) >= 1 .or. ISTRAN(7) >= 1 )then
old:885:     if( ISBKERO >= 1 )then
old:1031:         endif
old:1032:       endif
old:1033: 
old:1034:       if( K == 1 )then
old:1035:         if( HBED(L,K) < MINTHICK )then
old:1036:           ! *** ZERO NEGATIVE THICKNESSES
old:1037:           HBED(L,K) = 0.0
old:1038:           VDRBED(L,K) = SNDVDRD
old:1039:           PORBED(L,K) = BEDPORC
old:1040:           STDOCB(L,K) = 0.0
old:1041:           STPOCB(L,K) = 0.0
old:1042:           
old:1043:           SEDB(L,K,:) = 0.0
old:1044:           SNDB(L,K,:) = 0.0
old:1045:         endif
old:1046:       endif
old:1047:       
old:1048:       ! *** Update void ratio with the depositing sediment mass, using the last layer thickness.
old:1049:       ! *** HBED then gets updated in CALBED
old:1050:       TMPVAL = HBED1(L,K)/(1. + VDRBED1(L,K))
old:1051:       TMPVAL = TMPVAL - DTSED*( QSBDTOP(L) - QSSDPA(L) )
old:1052:       if( TMPVAL > 0.0 )then
old:1053:         if( HBED(L,K) > 0.0 )then        
old:1054:           VDRBED(L,K) = (HBED(L,K)/TMPVAL)-1.
old:1055:           if( K == 1 )then
old:1056:             ! *** LIMIT VOID RATIOS TO 0.01 >= N <= 99
old:1057:             if( VDRBED(L,K) < 0.01 .or. VDRBED(L,K) > 99. )then
old:1058:               VDRBED(L,K) = SNDVDRD  
old:1059:             endif
old:1060:           endif
old:1061:         else
old:1062:           ! *** Bed thickness is zero.  Initialize to depositing sediment mass
old:1078:           HBED1(L,K) = HBED(L,K)
old:1079:           VDRBED1(L,K) = VDRBED(L,K)
old:1080:           HBED(L,K) = HBED(L,K) - DTSED*(QSSDPA(L)+QWATPA(L))
old:1081: 
old:1082:           if( K == 1 )then
old:1083:             if( HBED(L,K) < 0.0 )then
old:1084:               ! *** ZERO NEGATIVE THICKNESSES
old:1085:               HBED(L,K) = 0.0
old:1086:               VDRBED(L,K) = SNDVDRD
old:1087:               PORBED(L,K) = BEDPORC
old:1088:               STDOCB(L,K) = 0.0
old:1089:               STPOCB(L,K) = 0.0
old:1090:             endif
old:1091:           endif
old:1092:           TMPVAL = HBED1(L,K)/(1. + VDRBED1(L,K))
old:1093:           TMPVAL = TMPVAL - DTSED*QSSDPA(L)
old:1094:           if( TMPVAL > 0.0 )then
old:1095:             VDRBED(L,K) = (HBED(L,K)/TMPVAL) - 1.
old:1096:           else
old:1097:             VDRBED(L,K) = SNDVDRD
old:1098:           endif
old:1099:         endif
old:1100:       enddo
old:1282:   ! ***********************************************************************C                                                
old:1283:   ! *** UPDATE SEDIMENT BED PHYSICAL PROPERTIES 
old:1284:   ! *** FOR SEDZLJ, THE VARIABLES ARE UPDATED IN S_SEDZLJ.F90
old:1285:   if( .not. LSEDZLJ )then
old:1286:     call CALBED
old:1287:   endif
new:863:   if( ISTRAN(6) >= 1 )then
new:864:     if( LSEDZLJ )then
new:865:       call SEDZLJ_MAIN
new:866:       GOTO 1000  ! *** BYPASS ORIGINAL BED/WATER INTERFACE CALCULATION
new:867:     else
new:868:       call CALSED
new:869:     endif
new:870:   endif
new:871:                             
new:872:   ! ***********************************************************************C                                                
new:873:   ! *** CALCULATE NONCOHESIVE SEDIMENT BEDLOAD TRANSPORT, SETTLING,                                                       
new:874:   ! *** DEPOSITION AND RESUSPENSION                                                                                       
new:875:   if( ISTRAN(7) >= 1 ) CALL CALSND
new:876:                           
new:877:   ! ***********************************************************************C                                                
new:878:   ! *** CALCULATE BANK EROSION AND ADJUST SEDIMENT AND WATER VOLUME FLUXES                                                                                                            
new:879:   if( ISTRAN(6) >= 1 .or. ISTRAN(7) >= 1 )then
new:880:     if( ISBKERO >= 1 )then
new:1026:         endif
new:1027:       endif
new:1028: 
new:1029:       if( HBED(L,K) < MINTHICK )then
new:1030:         ! *** ZERO NEGATIVE THICKNESSES
new:1031:         HBED(L,K) = 0.0
new:1032:         VDRBED(L,K) = SNDVDRD
new:1033:         PORBED(L,K) = BEDPORC
new:1034:         STDOCB(L,K) = 0.0
new:1035:         STPOCB(L,K) = 0.0
new:1036:         
new:1037:         SEDB(L,K,:) = 0.0
new:1038:         SNDB(L,K,:) = 0.0
new:1039:       endif
new:1040:       
new:1041:       ! *** Update void ratio with the depositing sediment mass, using the last layer thickness.
new:1042:       ! *** HBED then gets updated in CALBED
new:1043:       TMPVAL = HBED1(L,K)/(1. + VDRBED1(L,K))
new:1044:       TMPVAL = TMPVAL - DTSED*( QSBDTOP(L) - QSSDPA(L) )
new:1045:       if( TMPVAL > 0.0 )then
new:1046:         if( HBED(L,K) > 0.0 )then        
new:1047:           VDRBED(L,K) = (HBED(L,K)/TMPVAL)-1.
new:1048:           ! *** LIMIT VOID RATIOS TO 0.01 >= N <= 99
new:1049:           if( VDRBED(L,K) < 0.01 .or. VDRBED(L,K) > 99. )then
new:1050:             VDRBED(L,K) = SNDVDRD  
new:1051:           endif
new:1052:         else
new:1053:           ! *** Bed thickness is zero.  Initialize to depositing sediment mass
new:1069:           HBED1(L,K) = HBED(L,K)
new:1070:           VDRBED1(L,K) = VDRBED(L,K)
new:1071:           HBED(L,K) = HBED(L,K) - DTSED*(QSSDPA(L)+QWATPA(L))
new:1072:           if( HBED(L,K) < 0.0 )then
new:1073:             ! *** ZERO NEGATIVE THICKNESSES
new:1074:             HBED(L,K) = 0.0
new:1075:             VDRBED(L,K) = SNDVDRD
new:1076:             PORBED(L,K) = BEDPORC
new:1077:             STDOCB(L,K) = 0.0
new:1078:             STPOCB(L,K) = 0.0
new:1079:           endif
new:1080:           TMPVAL = HBED1(L,K)/(1. + VDRBED1(L,K))
new:1081:           TMPVAL = TMPVAL - DTSED*QSSDPA(L)
new:1082:           if( TMPVAL > 0.0 )then
new:1083:             VDRBED(L,K) = (HBED(L,K)/TMPVAL) - 1.
new:1084:             if( VDRBED(L,K) < 0.01 .or. VDRBED(L,K) > 99. )then
new:1085:               VDRBED(L,K) = SNDVDRD  
new:1086:             endif
new:1087:           else
new:1088:             VDRBED(L,K) = SNDVDRD
new:1089:           endif
new:1090:         endif
new:1091:       enddo
new:1273:   ! ***********************************************************************C                                                
new:1274:   ! *** UPDATE SEDIMENT BED PHYSICAL PROPERTIES 
new:1275:   ! *** FOR SEDZLJ, THE VARIABLES ARE UPDATED IN S_SEDZLJ.F90
new:1276:   if( .not. LSEDZLJ )then
new:1277:     call CALBED
new:1278:   endif
```

## C2-11 — REVIEW_ONLY

- 노트: `models/EFDC/source-analysis/sediment/efdc_sediment.md:178`
- 원문: - `hdmt2t.f90:409-428` — wave-current turbulence for non-SEDZLJ.
- old 근거: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/hdmt2t.f90:409-428
- new 근거: _staging/efdc-prescan/new/EFDC__hdmt2t.f90:409-428
- 변경 hunk (context 포함): @@ -411,7 +411,7 @@ SUBROUTINE HDMT2T [old intersection 411-417]; @@ -420,7 +420,7 @@ SUBROUTINE HDMT2T [old intersection 420-426]
- 실제 변경: TBX 공백 정리 외에 VTMP의 LN→LNC(L), KSZV(LN)→KSZV(LNC(L)) 교체.
- 의미 차이: 현재 셀의 북쪽 이웃을 명시해 VTMP→CURANG→TAUB2→QQ 계산 결과에 영향을 줄 수 있음; 단순 rename 아님.
- 판정 이유: ISWAVE>=1 AND .not.LSEDZLJ 게이트와 wave-current turbulence 역할은 유지된다. 노트는 LN 기반 stencil을 직접 노출하지 않는다. 코드 동작 변화는 인정하되 이 요약 문장에 불일치가 없어 문장 유지 제안.
- 신뢰도: high. 최종 disposition: Claude 검토 대기.

```text
old:409:   if( ISWAVE >= 1 .and. .not. LSEDZLJ )then
old:410: 
old:411:     do L = 2,LA
old:412:       TVAR3S(L) = TSY(LNC(L))
old:413:       TVAR3W(L) = TSX(LEC(L))
old:414:       TVAR3E(L) = TBX(LEC(L)   )
old:415:       TVAR3N(L) = TBY(LNC(L))
old:416:     enddo
old:417: 
old:418:     do L = 2,LA
old:419:       TAUBC2 = (RSSBCE(L)*TVAR3E(L)+RSSBCW(L)*TBX(L))**2 + (RSSBCN(L)*TVAR3N(L)+RSSBCS(L)*TBY(L))**2
old:420:       TAUBC = 0.5*SQRT(TAUBC2)   ! *** CURRENT ONLY
old:421:       CTAUC(L) = TAUBC
old:422:       UTMP = 0.5*STCUV(L)*(U(LEC(L),KSZU(LEC(L))) + U(L,KSZU(L)))+1.E-12
old:423:       VTMP = 0.5*STCUV(L)*(V(LN ,KSZV(LN )) + V(L,KSZV(L)))
old:424:       CURANG = ATAN2(VTMP,UTMP)
old:425:       TAUB2 = TAUBC*TAUBC + (QQWV3(L)*QQWV3(L)) + 2.*TAUBC*QQWV3(L)*COS(CURANG-WV(L).DIR)
old:426:       TAUB2 = max(TAUB2,0.)          ! *** CURRENT & WAVE
old:427:       QQ(L,0 ) = CTURB2*SQRT(TAUB2)  ! *** CELL CENTERED TURBULENT INTENSITY DUE TO CURRENTS & WAVES
old:428:       QQ(L,KC) = 0.5*CTURB2*SQRT((TVAR3W(L)+TSX(L))**2 + (TVAR3S(L)+TSY(L))**2)
new:409:   if( ISWAVE >= 1 .and. .not. LSEDZLJ )then
new:410: 
new:411:     do L = 2,LA
new:412:       TVAR3S(L) = TSY(LNC(L))
new:413:       TVAR3W(L) = TSX(LEC(L))
new:414:       TVAR3E(L) = TBX(LEC(L))
new:415:       TVAR3N(L) = TBY(LNC(L))
new:416:     enddo
new:417: 
new:418:     do L = 2,LA
new:419:       TAUBC2 = (RSSBCE(L)*TVAR3E(L)+RSSBCW(L)*TBX(L))**2 + (RSSBCN(L)*TVAR3N(L)+RSSBCS(L)*TBY(L))**2
new:420:       TAUBC = 0.5*SQRT(TAUBC2)   ! *** CURRENT ONLY
new:421:       CTAUC(L) = TAUBC
new:422:       UTMP = 0.5*STCUV(L)*(U(LEC(L),KSZU(LEC(L))) + U(L,KSZU(L)))+1.E-12
new:423:       VTMP = 0.5*STCUV(L)*(V(LNC(L),KSZV(LNC(L))) + V(L,KSZV(L)))
new:424:       CURANG = ATAN2(VTMP,UTMP)
new:425:       TAUB2 = TAUBC*TAUBC + (QQWV3(L)*QQWV3(L)) + 2.*TAUBC*QQWV3(L)*COS(CURANG-WV(L).DIR)
new:426:       TAUB2 = max(TAUB2,0.)          ! *** CURRENT & WAVE
new:427:       QQ(L,0 ) = CTURB2*SQRT(TAUB2)  ! *** CELL CENTERED TURBULENT INTENSITY DUE TO CURRENTS & WAVES
new:428:       QQ(L,KC) = 0.5*CTURB2*SQRT((TVAR3W(L)+TSX(L))**2 + (TVAR3S(L)+TSY(L))**2)
```

## C2-12 — REVIEW_ONLY

- 노트: `models/EFDC/source-analysis/sediment/efdc_sedzlj.md:416`
- 원문: 수평 운동량 확산의 wave breaking 가산항은 본 노트 아닌 [[efdc_dispersion]] §2.3 calhdmf.f90:246-294.
- old 근거: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calhdmf.f90:245-253; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calhdmf.f90:266-269; models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calhdmf.f90:284-287
- new 근거: _staging/efdc-prescan/new/EFDC__calhdmf.f90:245-253; _staging/efdc-prescan/new/EFDC__calhdmf.f90:266-269; _staging/efdc-prescan/new/EFDC__calhdmf.f90:284-287
- 변경 hunk (context 포함): @@ -245,7 +245,7 @@ SUBROUTINE CALHDMF [old intersection 246-251]
- 실제 변경: WVFACT ramp 조건에서 ISWAVE==2 제거: N<NTSWV만 검사.
- 의미 차이: ISWAVE=4도 초기 cosine ramp 적용; ISWAVE=2는 동일. AH wave-breaking 가산 경로와 수식은 유지.
- 판정 이유: 이 후보는 wave-breaking 수평 확산 가산항의 위치를 다른 노트로 안내하며 ramp를 mode 2로 한정하지 않는다. 가산항 위치·역할은 그대로이므로 이 cross-reference 문장 유지 제안. 다른 노트의 별도 후보 판정으로 확대하지 않는다.
- 신뢰도: high. 최종 disposition: Claude 검토 대기.

```text
old:245:     ! ***  CALCULATE HORIZONTAL SMAG DIFFUSION DUE TO WAVE BREAKING
old:246:     if( ISWAVE == 2 .or. ISWAVE == 4 )then
old:247:       if( WVLSH > 0.0 .or. WVLSX > 0.0 )then
old:248:         if( ISWAVE == 2 .and. N < NTSWV )then
old:249:           TMPVAL = FLOAT(N)/FLOAT(NTSWV)
old:250:           WVFACT = 0.5-0.5*COS(PI*TMPVAL)
old:251:         else
old:252:           WVFACT = 1.0
old:253:         endif
old:266:                   TMPVAL = 2.*PI/WV(L).FREQ     ! *** WAVE PERIOD
old:267:                   AHWVX = WVLSX*TMPVAL*TMPVAL
old:268:                   DTMPX = WV(L).DISSIPA(K)/HP(L)
old:269:                   AH(L,K) = AH(L,K)+WVFACT*(WVLSH*DTMPH*HP(L)+AHWVX*DTMPX)
old:284:                 TMPVAL = 2.*PI/WV(L).FREQ
old:285:                 AHWVX = WVLSX*TMPVAL*TMPVAL
old:286:                 DTMPX = WV(L).DISSIPA(K)/HP(L)
old:287:                 AH(L,K) = AH(L,K)+WVFACT*(WVLSH*DTMPH*HP(L)+AHWVX*DTMPX)
new:245:     ! ***  CALCULATE HORIZONTAL SMAG DIFFUSION DUE TO WAVE BREAKING
new:246:     if( ISWAVE == 2 .or. ISWAVE == 4 )then
new:247:       if( WVLSH > 0.0 .or. WVLSX > 0.0 )then
new:248:         if( N < NTSWV )then
new:249:           TMPVAL = FLOAT(N)/FLOAT(NTSWV)
new:250:           WVFACT = 0.5-0.5*COS(PI*TMPVAL)
new:251:         else
new:252:           WVFACT = 1.0
new:253:         endif
new:266:                   TMPVAL = 2.*PI/WV(L).FREQ     ! *** WAVE PERIOD
new:267:                   AHWVX = WVLSX*TMPVAL*TMPVAL
new:268:                   DTMPX = WV(L).DISSIPA(K)/HP(L)
new:269:                   AH(L,K) = AH(L,K)+WVFACT*(WVLSH*DTMPH*HP(L)+AHWVX*DTMPX)
new:284:                 TMPVAL = 2.*PI/WV(L).FREQ
new:285:                 AHWVX = WVLSX*TMPVAL*TMPVAL
new:286:                 DTMPX = WV(L).DISSIPA(K)/HP(L)
new:287:                 AH(L,K) = AH(L,K)+WVFACT*(WVLSH*DTMPH*HP(L)+AHWVX*DTMPX)
```

## 검증 및 범위

- 7개 대상 소스의 patch를 메모리에서 old 전문에 적용한 결과 new 전문과 모두 일치했다. patch 내용은 compare.json의 해당 파일 patch와 모두 일치했다.
- C2-4 표준식 old:1216-1217=new:1215-1216, SGZ old/new:1167-1204 동일성을 확인했다. C2-7 module 뒤 kernel은 -2줄 이동하며 내용 동일하다.
- CSV 첫 열 id, 지정 14개 필드, 12개 ID·순서·원문·note_line 및 모든 필수 값 검증을 통과했다. hunk 교집합은 문맥 포함이며 실제 의미 변경은 별도로 적었다.
- models/에는 쓰기 작업을 하지 않았다. 대상 models/ 노트·old 소스 15개는 산출물 작성 전후 SHA-256이 모두 동일함을 확인했다. 추가 cross-reference 노트는 읽기만 했다.
- 쓰기는 phase2-C2-codex.csv와 phase2-C2-codex.md 두 파일뿐이다. wiki·snapshot·provenance·DESIGN 수정, sudo, 네트워크, git 명령을 수행하지 않았다.
- 런타임 수치 재현·노트 전체 감사·다른 후보 판정은 범위 밖이다. 12건 판정안 작성으로 종료한다.
