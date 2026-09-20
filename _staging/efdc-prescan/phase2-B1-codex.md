# EFDC phase2 B1 — Codex semantic-review 제안

대상: old `3ed76b6eb1263921ba99bf23b66bb85c1a5feac1` → new `3b382fd0b5222a8ed0bac6d2cfc9a7877062db27` (v12.5). 날짜: 2026-09-20. **Claude 최종 판정 전 초안**.

범위는 `phase2-B1.json`의 17개 candidate ID로 고정했다. 판정 단위는 개별 노트 문장과 지정된 인용 구간이다. 같은 문장의 다른 구간, 같은 기능군 또는 노트 전체로 분류를 전파하지 않았다. 사용자 분류 기준을 우선하고 `_staging/model-migration-framework/DESIGN-v2-DRAFT.md:82-102,195-217`을 대조했다. 새 규칙은 만들지 않았다.

## 집계

| Proposed classification | 개수 |
|---|---:|
| UPDATE_REQUIRED | 1 |
| REVIEW_ONLY | 12 |
| NO_ACTION | 4 |
| UNRESOLVED_RULE_GAP | 0 |
| UNRESOLVED_SOURCE_REFERENCE | 0 |

UPDATE_REQUIRED: **B1-1**, `models/EFDC/manual-notes/efdc-user-manual-r850.md:104` — C6 3번째 더미가 실제 `ISQUICK` 입력으로 바뀌어 v12.5 차이를 명시해야 한다.

UNRESOLVED: 없음. 모든 후보가 인용하는 `EFDC/input.f90`를 old/new 로컬 파일에서 찾았다.

## 검증 및 읽기 전용 확인

- 17개 입력 wiki_claim과 현재 note_line의 원문이 모두 정확히 일치한다.
- `compare.json`의 EFDC/input.f90 patch와 로컬 patch가 동일하다. patch를 old 파일에 메모리 안에서 적용한 전체 결과가 new 파일의 모든 행과 일치한다. 따라서 범위 내부 차이를 누락한 truncated patch에 의존하지 않는다.
- 모든 citation interval과 모든 old-side hunk interval의 교집합을 계산했다. hunk의 context와 실제 삭제/교체행을 구분하고, 동일성 판정은 전체 인용 구간을 비교했다. 삽입은 해당 hunk의 new-side 코드와 대조했다.
- `NO_ACTION` 4건은 인용 전체 내용 동일성이 확인된 개별 후보이다. 줄 번호의 기계적 재매핑까지 불필요하다는 뜻도, 노트 전체 검증 완료라는 뜻도 아니다.
- `REVIEW_ONLY` 12건은 내부 변경을 기록하고 claim의 거짓 여부를 따로 대조했다. 각 행에 Claude 대기 disposition을 기록했으며 최종 승인으로 처리하지 않았다.
- 네트워크·sudo·git 명령을 사용하지 않았다. 쓰기는 이 CSV/Markdown 두 파일에만 수행했다.
- `models/` 82,159개 항목의 경로·mode·size·mtime_ns·ctime_ns 집계 SHA-256이 작업 전후 동일: `bf47d0bcb67427f10f12127f3f682518e2ea243f58934a0f0cc1876f2e00e18f`. 접근시각은 제외했다. 이는 파일 내용 전체 해시 검사는 아니며, 본 작업의 models/ 쓰기는 0건이다.

## 개별 판정

### B1-1 — UPDATE_REQUIRED

- Note: `models/EFDC/manual-notes/efdc-user-manual-r850.md:104`
- Section/line: EFDC+ Documentation Release 8.5.0 — User Manual (L18) > 3. 챕터별 활용 가이드 (L65) > 3.3 §1.3 Input Files (p.15-73) — 운영 핵심 (L84) / claim L104
- Confidence: HIGH (분류 제안에 대한 확신; 모델 실행 검증 아님)
- Decision: `needs_claude_review` — Claude 최종 판정 대기; Codex 제안만 기록. 

**Current wiki claim (원문)**

```text
> - **C6**: 3·6·7·8번째 슬롯(`ISCDCA` 등)은 `ldum` 더미로 버려짐 (`input.f90:306`).
```

**Old source evidence**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:303-314
303:   if( process_id == master_id )then
304:     call SEEK('C6',0)
305:     do NS = 0,8
306:       read(1,*,IOSTAT = ISO) ISTRAN(NS), ISTOPT(NS), ldum, ISADAC(NS), ISFCT(NS), ldum, ldum, ldum, ISCI(NS), ISCO(NS)
307:       write(mpi_efdc_out_unit,1002) NCARD
308:       write(mpi_efdc_out_unit,*) ISTRAN(NS), ISTOPT(NS), ldum, ISADAC(NS), ISFCT(NS), ldum, ldum, ldum, ISCI(NS), ISCO(NS)
309:       if( ISO > 0 ) GOTO 100
310:     enddo
311:   endif
312: 
313:   call Broadcast_Array(ISTRAN, master_id)
314:   call Broadcast_Array(ISTOPT, master_id)
```

**New source evidence**

```fortran
_staging/efdc-prescan/new/EFDC__input.f90:308-325
308:   if( process_id == master_id )then
309:     call SEEK('C6',0)
310:     do NS = 0,8
311:       read(1,*,IOSTAT = ISO) ISTRAN(NS), ISTOPT(NS), ISQUICK, ISADAC(NS), ISFCT(NS), ldum, ldum, ldum, ISCI(NS), ISCO(NS)
312:       if( ISO > 0 ) GOTO 100
313:     enddo
314:   endif
315:   
316:   call Broadcast_Scalar(ISQUICK, master_id)   ! *** Using a scalar var for ISQUICK in EFDC+ 12.x - DKT
317: 
318:   ! *** Sanitize ISQUICK: this C6 column was unused prior to EFDC+ 12.x and legacy decks may contain other values
319:   if( ISQUICK /= 0 .and. ISQUICK /= 1 )then
320:     if( process_id == master_id )then
321:       PRINT *,'*** WARNING: INVALID ISQUICK ON CARD C6.  RESETTING TO 0 (UPWIND SCHEME)'
322:       write(mpi_efdc_out_unit,*) '*** WARNING: INVALID ISQUICK ON CARD C6.  RESETTING TO 0 (UPWIND SCHEME):', ISQUICK
323:     endif
324:     ISQUICK = 0
325:   endif

_staging/efdc-prescan/new/EFDC__Transport__calconc.f90:197-204
197:     ! *** Dispatch to appropriate transport scheme
198:     if( ISQUICK == 1 )then
199:       ! *** QUICKEST scheme with ULTIMATE limiter
200:       call CALTRAN_QUICKEST( IACTIVEWC1(IW), IACTIVEWC2(IW), WCV(IW).VAL0, WCV(IW).VAL1, IW, IT, WCV(IW).WCLIMIT, ISKIP(IW) )
201:     else
202:       ! *** Original upwind scheme
203:       call CALTRAN( IACTIVEWC1(IW), IACTIVEWC2(IW), WCV(IW).VAL0, WCV(IW).VAL1, IW, IT, WCV(IW).WCLIMIT, ISKIP(IW) )
204:     endif
```

**Triggering upstream change**: C6 세 번째 입력 슬롯 ldum → scalar ISQUICK; broadcast 및 0/1 검증 추가.

**Changed file**: `EFDC/input.f90`

**Changed hunk (@@), citation intersection, exact evidence**

```text
@@ -303,12 +308,21 @@ SUBROUTINE INPUT() | citation∩old-hunk=306-306; deleted/replaced old lines inside citation=306; new hunk=308-328
Full citation content identity: NO; interval includes edits (not endpoint-only comparison).
```

**Semantic delta**: 종전 더미 슬롯이 transport scheme parameter가 됨. 6·7·8번째 슬롯은 여전히 ldum.

**Reason**: 노트 101행은 v12.4 역사적 검증이라는 문맥이지만, snapshot v12.5 전환 시 세 번째 슬롯까지 버려진다는 안내를 현재 baseline으로 재사용할 수 없다. 사용자 기준의 dummy→실제 parameter 및 version-specific 문구 갱신 대상. 역사적 v12.4 사실을 거짓으로 취급하지 말고 v12.5 차이를 구분할 필요가 있다.

### B1-2 — REVIEW_ONLY

- Note: `models/EFDC/source-analysis/efdc_boundary_conditions.md:19`
- Section/line: Source basis (L17) / claim L19
- Confidence: HIGH (분류 제안에 대한 확신; 모델 실행 검증 아님)
- Decision: `needs_claude_review` — Claude 최종 판정 대기; Codex 제안만 기록. 내부 변경의 claim 영향 검토 및 인용 재매핑 여부 확인.

**Current wiki claim (원문)**

```text
- `input.f90:264, 548, 732-754, 852-867, 870-1321, 1352-1378, 2721-2995, 3656-3705, 5650-5685, 5717-5755, 5858-6277` — input cards C5, C11, C14–C24, time series headers.
```

**Old source evidence**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:870-889
870:   !C16*  READ SURFACE ELEVATION OR PRESSURE BOUNDARY CONDITION parameterS
871:   NCARD = '16'
872:   ! *** ********************************************************
873:   if( process_id == master_id )then
874:     call SEEK('C16',0)
875:     read(1,*,IOSTAT = ISO) NPBS, NPBW, NPBE, NPBN, NPFOR_Readin, NPFORT, NPSER, PDGINIT
876: 
877:     write(mpi_efdc_out_unit,1002) NCARD
878:     write(mpi_efdc_out_unit,*) NPBS, NPBW, NPBE, NPBN, NPFOR_Readin, NPFORT, NPSER, PDGINIT
879:     if( ISO > 0 ) GOTO 100
880:   endif
881: 
882:   call Broadcast_Scalar(NPBS        , master_id)
883:   call Broadcast_Scalar(NPBW        , master_id)
884:   call Broadcast_Scalar(NPBE        , master_id)
885:   call Broadcast_Scalar(NPBN        , master_id)
886:   call Broadcast_Scalar(NPFOR_Readin, master_id)
887:   call Broadcast_Scalar(NPFORT      , master_id)
888:   call Broadcast_Scalar(NPSER       , master_id)
889:   call Broadcast_Scalar(PDGINIT     , master_id)

models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:904-927
904:       do NP = 1,NPFOR_Readin
905:         do M = 1,MTIDE
906:           if( NPFORT == 0 )then
907:             read(1,*,IOSTAT = ISO)NDUM,CDUM,PFAM(NP,M),PFPH(NP,M)
908:             write(mpi_efdc_out_unit,1002) NCARD
909:             write(mpi_efdc_out_unit,*) NDUM, CDUM, PFAM(NP,M), PFPH(NP,M)
910:             if( ISO > 0 ) GOTO 100
911:           elseif( NPFORT >= 1 )then
912:             read(1,*,IOSTAT = ISO) NDUM, CDUM, PFAM(NP,M), PFPH(NP,M)
913:             RAD = PI2*PFPH(NP,M)/TCP(M)
914:             CPFAM0(NP,M) = PFAM(NP,M)*COS(RAD)
915:             SPFAM0(NP,M) = PFAM(NP,M)*SIN(RAD)
916:             write(mpi_efdc_out_unit,1002) NCARD
917:             write(mpi_efdc_out_unit,*) NDUM, CDUM, PFAM(NP,M), PFPH(NP,M), CPFAM0(NP,M), SPFAM0(NP,M)
918:             if( ISO > 0 ) GOTO 100
919:             read(1,*,IOSTAT = ISO) NDUM, CDUM, PFAM(NP,M), PFPH(NP,M)
920:             RAD = PI2*PFPH(NP,M)/TCP(M)
921:             CPFAM1(NP,M) = PFAM(NP,M)*COS(RAD)-CPFAM0(NP,M)
922:             SPFAM1(NP,M) = PFAM(NP,M)*SIN(RAD)-SPFAM0(NP,M)
923:             write(mpi_efdc_out_unit,1002) NCARD
924:             write(mpi_efdc_out_unit,*) NDUM, CDUM, PFAM(NP,M), PFPH(NP,M), CPFAM1(NP,M), SPFAM1(NP,M)
925:             CPFAM2(NP,M) = 0.0
926:             SPFAM2(NP,M) = 0.0
927:           elseif( NPFORT == 2 )then

models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:980-985
980:           do M = 1,MTIDE
981:             if( NPFORS == 0) exit
982:             RAD = PI2*PFPH(NPFORS,M)/TCP(M)
983:             AMP = G*PFAM(NPFORS,M)
984:             PCBS_GL(L,M) = AMP*COS(RAD)
985:             PSBS_GL(L,M) = AMP*SIN(RAD)
```

**New source evidence**

```fortran
_staging/efdc-prescan/new/EFDC__input.f90:903-922
903:   !C16*  READ SURFACE ELEVATION OR PRESSURE BOUNDARY CONDITION parameterS
904:   NCARD = '16'
905:   ! *** ********************************************************
906:   if( process_id == master_id )then
907:     call SEEK('C16',0)
908:     read(1,*,IOSTAT = ISO) NPBS, NPBW, NPBE, NPBN, NPFOR_Readin, NPFORT, NPSER, PDGINIT
909:     if( ISO > 0 ) GOTO 100
910:   endif
911: 
912:   call Broadcast_Scalar(NPBS        , master_id)
913:   call Broadcast_Scalar(NPBW        , master_id)
914:   call Broadcast_Scalar(NPBE        , master_id)
915:   call Broadcast_Scalar(NPBN        , master_id)
916:   call Broadcast_Scalar(NPFOR_Readin, master_id)
917:   call Broadcast_Scalar(NPFORT      , master_id)
918:   call Broadcast_Scalar(NPSER       , master_id)
919:   call Broadcast_Scalar(PDGINIT     , master_id)
920: 
921:   write(mpi_efdc_out_unit,1002) NCARD
922:   write(mpi_efdc_out_unit,*) NPBS, NPBW, NPBE, NPBN, NPFOR_Readin, NPFORT, NPSER, PDGINIT

_staging/efdc-prescan/new/EFDC__input.f90:937-957
937:       do NP = 1,NPFOR_Readin
938:         do M = 1,MTIDE
939:           if( NPFORT == 0 )then
940:             read(1,*,IOSTAT = ISO) IECHO(M), CECHO(M),PFAM(NP,M),PFPH(NP,M)
941:             if( ISO > 0 ) GOTO 100
942:           elseif( NPFORT >= 1 )then
943:             read(1,*,IOSTAT = ISO) IECHO(M), CECHO(M), PFAM(NP,M), PFPH(NP,M)
944:             RAD = PI2*PFPH(NP,M)/TCP(M)
945:             CPFAM0(NP,M) = PFAM(NP,M)*COS(RAD)
946:             SPFAM0(NP,M) = PFAM(NP,M)*SIN(RAD)
947:             if( ISO > 0 ) GOTO 100
948:             read(1,*,IOSTAT = ISO) IECHO(M), CECHO(M), PFAM(NP,M), PFPH(NP,M)
949:             RAD = PI2*PFPH(NP,M)/TCP(M)
950:             CPFAM1(NP,M) = PFAM(NP,M)*COS(RAD)-CPFAM0(NP,M)
951:             SPFAM1(NP,M) = PFAM(NP,M)*SIN(RAD)-SPFAM0(NP,M)
952:             CPFAM2(NP,M) = 0.0
953:             SPFAM2(NP,M) = 0.0
954:           elseif( NPFORT == 2 )then
955:             read(1,*,IOSTAT = ISO) IECHO(M), CECHO(M),PFAM(NP,M),PFPH(NP,M),PFX2(NP,M)
956:             RAD = PI2*PFPH(NP,M)/TCP(M)
957:             if( PFX2(NP,M)>0.0 )then

_staging/efdc-prescan/new/EFDC__input.f90:990-1003
990: 
991:     do NP = 1,NPFOR_Readin
992:       do M = 1,MTIDE
993:         if( NPFORT == 0 )then
994:           write(mpi_efdc_out_unit,1002) NCARD
995:           write(mpi_efdc_out_unit,*) IECHO(M), CECHO(M), PFAM(NP,M), PFPH(NP,M)
996:         elseif( NPFORT >= 1 )then
997:           write(mpi_efdc_out_unit,1002) NCARD
998:           write(mpi_efdc_out_unit,*) IECHO(M), CECHO(M), PFAM(NP,M), PFPH(NP,M), CPFAM0(NP,M), SPFAM0(NP,M)
999:           write(mpi_efdc_out_unit,1002) NCARD
1000:           write(mpi_efdc_out_unit,*) IECHO(M), CECHO(M), PFAM(NP,M), PFPH(NP,M), CPFAM1(NP,M), SPFAM1(NP,M)
1001:         elseif( NPFORT == 2 )then
1002:           write(mpi_efdc_out_unit,1002) NCARD
1003:           write(mpi_efdc_out_unit,*) IECHO(M), CECHO(M), PFAM(NP,M), PFPH(NP,M), CPFAM2(NP,M), SPFAM2(NP,M), PFX2(NP,M)

_staging/efdc-prescan/new/EFDC__input.f90:1021-1026
1021:           do M = 1,MTIDE
1022:             if( NPFORS == 0) exit
1023:             RAD = PI2*PFPH(NPFORS,M)/TCP(M)
1024:             AMP = G*PFAM(NPFORS,M)
1025:             PCBS_GL(L,M) = AMP*COS(RAD)
1026:             PSBS_GL(L,M) = AMP*SIN(RAD)
```

**Triggering upstream change**: C16–C21 echo를 master read 내부에서 밖으로 이동; C17 NDUM/CDUM → IECHO/CECHO; FORMAT 제거.

**Changed file**: `EFDC/input.f90`

**Changed hunk (@@), citation intersection, exact evidence**

```text
@@ -849,22 +878,26 @@ SUBROUTINE INPUT() | citation∩old-hunk=870-870; deleted/replaced old lines inside citation=none; new hunk=878-903
@@ -873,9 +906,6 @@ SUBROUTINE INPUT() | citation∩old-hunk=873-881; deleted/replaced old lines inside citation=876,877,878; new hunk=906-911
@@ -888,6 +918,9 @@ SUBROUTINE INPUT() | citation∩old-hunk=888-893; deleted/replaced old lines inside citation=none; new hunk=918-926
@@ -904,28 +937,22 @@ SUBROUTINE INPUT() | citation∩old-hunk=904-931; deleted/replaced old lines inside citation=907,908,909,912,916,917,919,923,924,928; new hunk=937-958
@@ -961,6 +988,22 @@ SUBROUTINE INPUT() | citation∩old-hunk=961-966; deleted/replaced old lines inside citation=none; new hunk=988-1009
@@ -973,8 +1016,6 @@ SUBROUTINE INPUT() | citation∩old-hunk=973-980; deleted/replaced old lines inside citation=976,977; new hunk=1016-1021
@@ -989,10 +1030,8 @@ SUBROUTINE INPUT() | citation∩old-hunk=989-998; deleted/replaced old lines inside citation=992,993,994; new hunk=1030-1037
@@ -1009,10 +1048,8 @@ SUBROUTINE INPUT() | citation∩old-hunk=1009-1018; deleted/replaced old lines inside citation=1012,1013,1014; new hunk=1048-1055
@@ -1036,9 +1073,6 @@ SUBROUTINE INPUT() | citation∩old-hunk=1036-1044; deleted/replaced old lines inside citation=1039,1040,1041; new hunk=1073-1078
@@ -1052,6 +1086,26 @@ SUBROUTINE INPUT() | citation∩old-hunk=1052-1057; deleted/replaced old lines inside citation=none; new hunk=1086-1111
@@ -1064,8 +1118,6 @@ SUBROUTINE INPUT() | citation∩old-hunk=1064-1071; deleted/replaced old lines inside citation=1067,1068; new hunk=1118-1123
@@ -1079,10 +1131,8 @@ SUBROUTINE INPUT() | citation∩old-hunk=1079-1088; deleted/replaced old lines inside citation=1082,1083,1084; new hunk=1131-1138
@@ -1100,10 +1150,8 @@ SUBROUTINE INPUT() | citation∩old-hunk=1100-1109; deleted/replaced old lines inside citation=1103,1104,1105; new hunk=1150-1157
@@ -1141,6 +1189,25 @@ SUBROUTINE INPUT() | citation∩old-hunk=1141-1146; deleted/replaced old lines inside citation=none; new hunk=1189-1213
@@ -1152,10 +1219,8 @@ SUBROUTINE INPUT() | citation∩old-hunk=1152-1161; deleted/replaced old lines inside citation=1155,1156,1157; new hunk=1219-1226
@@ -1168,10 +1233,8 @@ SUBROUTINE INPUT() | citation∩old-hunk=1168-1177; deleted/replaced old lines inside citation=1171,1172,1173; new hunk=1233-1240
@@ -1189,10 +1252,8 @@ SUBROUTINE INPUT() | citation∩old-hunk=1189-1198; deleted/replaced old lines inside citation=1192,1193,1194; new hunk=1252-1259
@@ -1230,6 +1291,25 @@ SUBROUTINE INPUT() | citation∩old-hunk=1230-1235; deleted/replaced old lines inside citation=none; new hunk=1291-1315
@@ -1242,10 +1322,8 @@ SUBROUTINE INPUT() | citation∩old-hunk=1242-1251; deleted/replaced old lines inside citation=1245,1246,1247; new hunk=1322-1329
@@ -1258,10 +1336,8 @@ SUBROUTINE INPUT() | citation∩old-hunk=1258-1267; deleted/replaced old lines inside citation=1261,1262,1263; new hunk=1336-1343
@@ -1279,10 +1355,8 @@ SUBROUTINE INPUT() | citation∩old-hunk=1279-1288; deleted/replaced old lines inside citation=1282,1283,1284; new hunk=1355-1362
@@ -1320,6 +1394,25 @@ SUBROUTINE INPUT() | citation∩old-hunk=1320-1321; deleted/replaced old lines inside citation=none; new hunk=1394-1418
Full citation content identity: NO; interval includes edits (not endpoint-only comparison).
```

**Semantic delta**: 입력 카드·조석 계수 계산 위치라는 broad source-basis는 유지되지만 452행 내부에 다수의 출력/저장 변경이 있다.

**Reason**: 19행은 카드·시계열 코드의 포괄적 근거 목록이지 각 echo/배열의 동작 설명이 아니다. 내부 hunk 전부를 검사했으며 claim 불일치는 확정하지 못했다. >60행 내부 변경 및 broad citation 규칙에 따라 Claude 검토로 남긴다.

### B1-3 — REVIEW_ONLY

- Note: `models/EFDC/source-analysis/efdc_boundary_conditions.md:19`
- Section/line: Source basis (L17) / claim L19
- Confidence: HIGH (분류 제안에 대한 확신; 모델 실행 검증 아님)
- Decision: `needs_claude_review` — Claude 최종 판정 대기; Codex 제안만 기록. 내부 변경의 claim 영향 검토 및 인용 재매핑 여부 확인.

**Current wiki claim (원문)**

```text
- `input.f90:264, 548, 732-754, 852-867, 870-1321, 1352-1378, 2721-2995, 3656-3705, 5650-5685, 5717-5755, 5858-6277` — input cards C5, C11, C14–C24, time series headers.
```

**Old source evidence**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:1352-1378
1352:   !C23*  READ VELOCITY, VOL SOUR/SINK, FLOW CONTROL, & WITHDRAW/RETURN DATA
1353:   NCARD = '23'
1354:   ! *** ********************************************************
1355:   if( process_id == master_id )then
1356:     call SEEK('C23',0)
1357:     read(1,*,IOSTAT = ISO) NQSIJ, NQJPIJ, NQSER, NQCTL, NQCTLT, NHYDST, NQWR, NQWRSR, ISDIQ, NQCTLSER, NQCTRULES
1358: 
1359:     write(mpi_efdc_out_unit,1002) NCARD
1360:     write(mpi_efdc_out_unit,*) NQSIJ, NQJPIJ, NQSER, NQCTL, NQCTLT, NHYDST, NQWR, NQWRSR, ISDIQ, NQCTLSER, NQCTRULES
1361:     if( ISO > 0 ) GOTO 100
1362:   endif
1363:   ! *** Broadcast in Scan_EFDC
1364: 
1365:   NGRPID = 0
1366:   if( NQSIJ > 0 )then
1367:     !C24*  READ VOLUME SOURCE/SINK LOCATIONS, MAGNITUDES, & VOL & CONC SERIES
1368:     NCARD = '24'
1369:     if( process_id == master_id )then
1370:       call SEEK('C24',0)
1371:       do NS = 1,NQSIJ
1372:         read(1,*,IOSTAT = ISO) BCPS_GL(NS).I, BCPS_GL(NS).J, BCPS_GL(NS).QSSE, BCPS_GL(NS).NQSMUL, BCPS_GL(NS).NQSMF, BCPS_GL(NS).NQSERQ,   BCPS_GL(NS).NCSERQ(1), BCPS_GL(NS).NCSERQ(2), BCPS_GL(NS).NCSERQ(3), BCPS_GL(NS).NCSERQ(4), BCPS_GL(NS).NCSERQ(5),  &
1373:           BCPS_GL(NS).NCSERQ(6), BCPS_GL(NS).NCSERQ(7), BCPS_GL(NS).QWIDTH,   BCPS_GL(NS).QFACTOR,  BCPS_GL(NS).GRPID
1374: 
1375:         write(mpi_efdc_out_unit,1002) NCARD
1376:         write(mpi_efdc_out_unit,*) BCPS_GL(NS).I, BCPS_GL(NS).J, BCPS_GL(NS).QSSE, BCPS_GL(NS).NQSMUL, BCPS_GL(NS).NQSMF, BCPS_GL(NS).NQSERQ,   BCPS_GL(NS).NCSERQ(1), BCPS_GL(NS).NCSERQ(2), BCPS_GL(NS).NCSERQ(3), BCPS_GL(NS).NCSERQ(4), BCPS_GL(NS).NCSERQ(5),  &
1377:           BCPS_GL(NS).NCSERQ(6), BCPS_GL(NS).NCSERQ(7), BCPS_GL(NS).QWIDTH,   BCPS_GL(NS).QFACTOR,  BCPS_GL(NS).GRPID
1378:         if( ISO > 0 ) GOTO 100
```

**New source evidence**

```fortran
_staging/efdc-prescan/new/EFDC__input.f90:1445-1470
1445:   !C23*  READ VELOCITY, VOL SOUR/SINK, FLOW CONTROL, & WITHDRAW/RETURN DATA
1446:   NCARD = '23'
1447:   ! *** ********************************************************
1448:   if( process_id == master_id )then
1449:     call SEEK('C23',0)
1450:     read(1,*,IOSTAT = ISO) NQSIJ, NQJPIJ, NQSER, NQCTL, NQCTLT, NHYDST, NQWR, NQWRSR, ISDIQ, NQCTLSER, NQCTRULES
1451:     if( ISO > 0 ) GOTO 100
1452:   endif
1453: 
1454:   write(mpi_efdc_out_unit,1002) NCARD
1455:   write(mpi_efdc_out_unit,*) NQSIJ, NQJPIJ, NQSER, NQCTL, NQCTLT, NHYDST, NQWR, NQWRSR, ISDIQ, NQCTLSER, NQCTRULES
1456: 
1457:   NGRPID = 0
1458:   if( NQSIJ > 0 )then
1459:     !C24*  READ VOLUME SOURCE/SINK LOCATIONS, MAGNITUDES, & VOL & CONC SERIES
1460:     NCARD = '24'
1461:     if( process_id == master_id )then
1462:       call SEEK('C24',0)
1463:       do NS = 1,NQSIJ
1464:         read(1,*,IOSTAT = ISO) BCPS_GL(NS).I, BCPS_GL(NS).J, BCPS_GL(NS).QSSE, BCPS_GL(NS).NQSMUL, BCPS_GL(NS).NQSMF, BCPS_GL(NS).NQSERQ,   BCPS_GL(NS).NCSERQ(1), BCPS_GL(NS).NCSERQ(2), BCPS_GL(NS).NCSERQ(3), BCPS_GL(NS).NCSERQ(4), BCPS_GL(NS).NCSERQ(5),  &
1465:           BCPS_GL(NS).NCSERQ(6), BCPS_GL(NS).NCSERQ(7), BCPS_GL(NS).QWIDTH,   BCPS_GL(NS).QFACTOR,  BCPS_GL(NS).GRPID
1466: 
1467:         write(mpi_efdc_out_unit,1002) NCARD
1468:         write(mpi_efdc_out_unit,*) BCPS_GL(NS).I, BCPS_GL(NS).J, BCPS_GL(NS).QSSE, BCPS_GL(NS).NQSMUL, BCPS_GL(NS).NQSMF, BCPS_GL(NS).NQSERQ,   BCPS_GL(NS).NCSERQ(1), BCPS_GL(NS).NCSERQ(2), BCPS_GL(NS).NCSERQ(3), BCPS_GL(NS).NCSERQ(4), BCPS_GL(NS).NCSERQ(5),  &
1469:           BCPS_GL(NS).NCSERQ(6), BCPS_GL(NS).NCSERQ(7), BCPS_GL(NS).QWIDTH,   BCPS_GL(NS).QFACTOR,  BCPS_GL(NS).GRPID
1470:         if( ISO > 0 ) GOTO 100
```

**Triggering upstream change**: C23 echo를 master-only 블록 밖으로 이동하고 Broadcast in Scan_EFDC 주석 제거.

**Changed file**: `EFDC/input.f90`

**Changed hunk (@@), citation intersection, exact evidence**

```text
@@ -1355,12 +1448,11 @@ SUBROUTINE INPUT() | citation∩old-hunk=1355-1366; deleted/replaced old lines inside citation=1358,1359,1360,1363; new hunk=1448-1458
Full citation content identity: NO; interval includes edits (not endpoint-only comparison).
```

**Semantic delta**: C23 read 목록 및 C24 필드/루프는 유지; C23 진단 출력 실행 위치만 달라짐.

**Reason**: 19행 source-basis의 C23/C24 근거 역할은 유지되나 범위 내부 출력 변경이 존재한다. claim 자체의 불일치는 없으며 자동 line-only 처리하지 않고 범위 내부 변경 영향 없음으로 검토를 남긴다.

### B1-4 — REVIEW_ONLY

- Note: `models/EFDC/source-analysis/efdc_boundary_conditions.md:19`
- Section/line: Source basis (L17) / claim L19
- Confidence: HIGH (분류 제안에 대한 확신; 모델 실행 검증 아님)
- Decision: `needs_claude_review` — Claude 최종 판정 대기; Codex 제안만 기록. 내부 변경의 claim 영향 검토 및 인용 재매핑 여부 확인.

**Current wiki claim (원문)**

```text
- `input.f90:264, 548, 732-754, 852-867, 870-1321, 1352-1378, 2721-2995, 3656-3705, 5650-5685, 5717-5755, 5858-6277` — input cards C5, C11, C14–C24, time series headers.
```

**Old source evidence**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:3656-3687
3656:   ! *** OPEN FILE MODCHAN.INP TO INSERT SUBGRID CHANNELS INTO HOST CELLS
3657:   MDCHH = 0
3658:   if( ISCHAN > 0 )then
3659:     if( process_id == master_id )then
3660:       write(*,'(A)')'READING MODCHAN.INP'
3661:       open(1,FILE = 'modchan.inp',STATUS = 'UNKNOWN')
3662: 
3663:       ! *** SKIP OVER TITLE AND AND HEADER LINES
3664:       STR = READSTR(1)
3665:       if( ISCHAN == 1 )then
3666:         read(1,*) MDCHH, ldum, ldum
3667:         read(1,*) ldum, ldum, QCHERR
3668:         if( MDCHH >= 1 )then
3669:           do NMD = 1,MDCHH
3670:             read(1,*)MDCHTYP(NMD),IMDCHH(NMD),JMDCHH(NMD),IMDCHU(NMD),JMDCHU(NMD),IMDCHV(NMD),JMDCHV(NMD)
3671:             QCHANU(NMD) = 0.
3672:             QCHANUN(NMD) = 0.
3673:             QCHANV(NMD) = 0.
3674:             QCHANVN(NMD) = 0.
3675:           enddo
3676:         endif
3677:       endif
3678:       if( ISCHAN == 2 )then
3679:         read(1,*) MDCHH, ldum, ldum
3680:         read(1,*) ldum, ldum, QCHERR
3681:         if( MDCHH >= 1 )then
3682:           do NMD = 1,MDCHH
3683:             read(1,*)MDCHTYP(NMD),IMDCHH(NMD),JMDCHH(NMD),IMDCHU(NMD),JMDCHU(NMD),IMDCHV(NMD),JMDCHV(NMD),CHANLEN(NMD),PMDCH(NMD)
3684:             QCHANU(NMD) = 0.
3685:             QCHANUN(NMD) = 0.
3686:             QCHANV(NMD) = 0.
3687:             QCHANVN(NMD) = 0.

models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:3692-3705
3692:       if( MDCHH >= 1 )then
3693:         do NMD = 1,MDCHH
3694:           LMDCHH(NMD) = LIJ(IMDCHH(NMD),JMDCHH(NMD))
3695:           if( IMDCHU(NMD) == 1 .and. JMDCHU(NMD) == 1 )then
3696:             LMDCHU(NMD) = 1
3697:           else
3698:             LMDCHU(NMD) = LIJ(IMDCHU(NMD),JMDCHU(NMD))
3699:           endif
3700:           if( IMDCHV(NMD) == 1 .and. JMDCHV(NMD) == 1 )then
3701:             LMDCHV(NMD) = 1
3702:           else
3703:             LMDCHV(NMD) = LIJ(IMDCHV(NMD),JMDCHV(NMD))
3704:           endif
3705:         enddo
```

**New source evidence**

```fortran
_staging/efdc-prescan/new/EFDC__input.f90:3753-3784
3753:   ! *** OPEN FILE MODCHAN.INP TO INSERT SUBGRID CHANNELS INTO HOST CELLS
3754:   MDCHH = 0
3755:   if( ISCHAN > 0 )then
3756:     if( process_id == master_id )then
3757:       write(*,'(A)')'READING MODCHAN.INP'
3758:       open(1,FILE = 'modchan.inp',STATUS = 'UNKNOWN')
3759: 
3760:       ! *** SKIP OVER TITLE AND AND HEADER LINES
3761:       STR = READSTR(1)
3762:       if( ISCHAN == 1 )then
3763:         read(1,*) MDCHH, ldum, ldum
3764:         read(1,*) ldum, ldum, QCHERR
3765:         if( MDCHH >= 1 )then
3766:           do NMD = 1,MDCHH
3767:             read(1,*)MDCHTYP(NMD),IMDCHH(NMD),JMDCHH(NMD),IMDCHU(NMD),JMDCHU(NMD),IMDCHV(NMD),JMDCHV(NMD)
3768:           enddo
3769:         endif
3770:       endif
3771:       if( ISCHAN == 2 )then
3772:         read(1,*) MDCHH, ldum, ldum
3773:         read(1,*) ldum, ldum, QCHERR
3774:         if( MDCHH >= 1 )then
3775:           do NMD = 1,MDCHH
3776:             read(1,*)MDCHTYP(NMD),IMDCHH(NMD),JMDCHH(NMD),IMDCHU(NMD),JMDCHU(NMD),IMDCHV(NMD),JMDCHV(NMD),CHANLEN(NMD),PMDCH(NMD)
3777:           enddo
3778:         endif
3779:       endif
3780:       close(1)
3781:     endif
3782: 
3783:     call Broadcast_Scalar(MDCHH  , master_id)
3784:     call Broadcast_Scalar(QCHERR , master_id)

_staging/efdc-prescan/new/EFDC__input.f90:3796-3810
3796:     ! *** Map the global channel data to the local subdomain
3797:     MDCHH_GL = MDCHH
3798:     MDCHH = 0
3799:     do NMD = 1,MDCHH_GL
3800:       if( LIJ_Global(IMDCHH(NMD),JMDCHH(NMD)) < 2 )then
3801:         if( process_id == master_id )then
3802:           write(6,*) 'ERROR!  HOST CELL IS NOT IN THE GLOBAL DOMAIN FOR SUBGRID CHANNEL: ',NMD
3803:         endif
3804:         call STOPP('', 1)
3805:       endif
3806: 
3807:       ! *** Local host cell indices
3808:       ITMP = IG2IL(IMDCHH(NMD))
3809:       JTMP = JG2JL(JMDCHH(NMD))
3810:       INHOST = ITMP > 0 .and. ITMP <= IC .and. JTMP > 0 .and. JTMP <= JC

_staging/efdc-prescan/new/EFDC__input.f90:3817-3825
3817:         ITMPU = IG2IL(IMDCHU(NMD))
3818:         JTMPU = JG2JL(JMDCHU(NMD))
3819:         INCHNU = ITMPU > 0 .and. ITMPU <= IC .and. JTMPU > 0 .and. JTMPU <= JC
3820:         if( INHOST .neqv. INCHNU )then
3821:           write(6,*) 'ERROR!  HOST AND U CHANNEL CELLS ARE NOT IN THE SAME SUBDOMAIN FOR SUBGRID CHANNEL: ',NMD
3822:           call STOPP('', 1)
3823:         endif
3824:       endif
3825: 

_staging/efdc-prescan/new/EFDC__input.f90:3830-3844
3830:       if( .not. (IMDCHV(NMD) == 1 .and. JMDCHV(NMD) == 1) )then
3831:         ITMPD = IG2IL(IMDCHV(NMD))
3832:         JTMPD = JG2JL(JMDCHV(NMD))
3833:         INCHNV = ITMPD > 0 .and. ITMPD <= IC .and. JTMPD > 0 .and. JTMPD <= JC
3834:         if( INHOST .neqv. INCHNV )then
3835:           write(6,*) 'ERROR!  HOST AND V CHANNEL CELLS ARE NOT IN THE SAME SUBDOMAIN FOR SUBGRID CHANNEL: ',NMD
3836:           call STOPP('', 1)
3837:         endif
3838:       endif
3839: 
3840:       ! *** Keep the channels in the current subdomain
3841:       if( INHOST )then
3842:         MDCHH = MDCHH + 1
3843: 
3844:         MDCHTYP(MDCHH) = MDCHTYP(NMD)

_staging/efdc-prescan/new/EFDC__input.f90:3867-3872
3867: 
3868:         QCHANU (MDCHH) = 0.
3869:         QCHANUN(MDCHH) = 0.
3870:         QCHANV (MDCHH) = 0.
3871:         QCHANVN(MDCHH) = 0.
3872:       endif
```

**Triggering upstream change**: MODCHAN read 직후 유량 초기화·master LIJ 매핑 삭제; scalar broadcast와 하위도메인 매핑/검증/초기화 추가.

**Changed file**: `EFDC/input.f90`

**Changed hunk (@@), citation intersection, exact evidence**

```text
@@ -3668,10 +3765,6 @@ SUBROUTINE INPUT() | citation∩old-hunk=3668-3677; deleted/replaced old lines inside citation=3671,3672,3673,3674; new hunk=3765-3770
@@ -3681,32 +3774,15 @@ SUBROUTINE INPUT() | citation∩old-hunk=3681-3705; deleted/replaced old lines inside citation=3684,3685,3686,3687,3692,3693,3694,3695,3696,3697,3698,3699,3700,3701,3702,3703,3704,3705; new hunk=3774-3788
Full citation content identity: NO; interval includes edits (not endpoint-only comparison).
```

**Semantic delta**: 입력 필드 구조는 유지하되 글로벌 I/J를 로컬로 변환하고 host/U/V의 동일 subdomain 조건을 검사하며 MDCHH를 로컬 개수로 재구성.

**Reason**: 후보는 19행의 broad source-basis이다. 해당 문장이 master-only 직접 매핑이나 모든 채널 허용을 단언하지 않으므로 알고리즘 변경을 이 후보의 UPDATE_REQUIRED로 자동 전파하지 않는다. 새 매핑 조건을 포함한 근거 범위 조정은 Claude 검토 사항이다.

### B1-5 — REVIEW_ONLY

- Note: `models/EFDC/source-analysis/efdc_boundary_conditions.md:85`
- Section/line: C. NQSER (flow time series, river discharge) (L83) / claim L85
- Confidence: HIGH (분류 제안에 대한 확신; 모델 실행 검증 아님)
- Decision: `needs_claude_review` — Claude 최종 판정 대기; Codex 제안만 기록. 내부 변경의 claim 영향 검토 및 인용 재매핑 여부 확인.

**Current wiki claim (원문)**

```text
Card C23 reads `NQSIJ` and `NQSER` counts (`input.f90:1352-1360`).
```

**Old source evidence**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:1352-1363
1352:   !C23*  READ VELOCITY, VOL SOUR/SINK, FLOW CONTROL, & WITHDRAW/RETURN DATA
1353:   NCARD = '23'
1354:   ! *** ********************************************************
1355:   if( process_id == master_id )then
1356:     call SEEK('C23',0)
1357:     read(1,*,IOSTAT = ISO) NQSIJ, NQJPIJ, NQSER, NQCTL, NQCTLT, NHYDST, NQWR, NQWRSR, ISDIQ, NQCTLSER, NQCTRULES
1358: 
1359:     write(mpi_efdc_out_unit,1002) NCARD
1360:     write(mpi_efdc_out_unit,*) NQSIJ, NQJPIJ, NQSER, NQCTL, NQCTLT, NHYDST, NQWR, NQWRSR, ISDIQ, NQCTLSER, NQCTRULES
1361:     if( ISO > 0 ) GOTO 100
1362:   endif
1363:   ! *** Broadcast in Scan_EFDC
```

**New source evidence**

```fortran
_staging/efdc-prescan/new/EFDC__input.f90:1445-1455
1445:   !C23*  READ VELOCITY, VOL SOUR/SINK, FLOW CONTROL, & WITHDRAW/RETURN DATA
1446:   NCARD = '23'
1447:   ! *** ********************************************************
1448:   if( process_id == master_id )then
1449:     call SEEK('C23',0)
1450:     read(1,*,IOSTAT = ISO) NQSIJ, NQJPIJ, NQSER, NQCTL, NQCTLT, NHYDST, NQWR, NQWRSR, ISDIQ, NQCTLSER, NQCTRULES
1451:     if( ISO > 0 ) GOTO 100
1452:   endif
1453: 
1454:   write(mpi_efdc_out_unit,1002) NCARD
1455:   write(mpi_efdc_out_unit,*) NQSIJ, NQJPIJ, NQSER, NQCTL, NQCTLT, NHYDST, NQWR, NQWRSR, ISDIQ, NQCTLSER, NQCTRULES
```

**Triggering upstream change**: C23 echo의 master-only 경계 밖 이동.

**Changed file**: `EFDC/input.f90`

**Changed hunk (@@), citation intersection, exact evidence**

```text
@@ -1355,12 +1448,11 @@ SUBROUTINE INPUT() | citation∩old-hunk=1355-1360; deleted/replaced old lines inside citation=1358,1359,1360; new hunk=1448-1458
Full citation content identity: NO; interval includes edits (not endpoint-only comparison).
```

**Semantic delta**: NQSIJ·NQSER를 포함한 read 목록·순서·오류 검사는 유지; 출력 실행 위치는 변경.

**Reason**: 85행의 counts를 읽는다는 문장은 그대로 참이다. 인용 내부 echo 삭제/이동이 실제 있으므로 순수 줄 이동으로 처리하지 않으며, 범위 내부 변경이 이 claim에 영향 없음으로 제안한다.

### B1-6 — NO_ACTION

- Note: `models/EFDC/source-analysis/efdc_boundary_conditions.md:88`
- Section/line: C. NQSER (flow time series, river discharge) (L83) / claim L88
- Confidence: HIGH (분류 제안에 대한 확신; 모델 실행 검증 아님)
- Decision: `needs_claude_review` — Claude 최종 판정 대기; Codex 제안만 기록. 

**Current wiki claim (원문)**

```text
`I, J, QSSE, NQSMUL, NQSMF, NQSERQ, NCSERQ(1:7), QWIDTH, QFACTOR, GRPID` (`input.f90:1365-1378`).
```

**Old source evidence**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:1365-1378
1365:   NGRPID = 0
1366:   if( NQSIJ > 0 )then
1367:     !C24*  READ VOLUME SOURCE/SINK LOCATIONS, MAGNITUDES, & VOL & CONC SERIES
1368:     NCARD = '24'
1369:     if( process_id == master_id )then
1370:       call SEEK('C24',0)
1371:       do NS = 1,NQSIJ
1372:         read(1,*,IOSTAT = ISO) BCPS_GL(NS).I, BCPS_GL(NS).J, BCPS_GL(NS).QSSE, BCPS_GL(NS).NQSMUL, BCPS_GL(NS).NQSMF, BCPS_GL(NS).NQSERQ,   BCPS_GL(NS).NCSERQ(1), BCPS_GL(NS).NCSERQ(2), BCPS_GL(NS).NCSERQ(3), BCPS_GL(NS).NCSERQ(4), BCPS_GL(NS).NCSERQ(5),  &
1373:           BCPS_GL(NS).NCSERQ(6), BCPS_GL(NS).NCSERQ(7), BCPS_GL(NS).QWIDTH,   BCPS_GL(NS).QFACTOR,  BCPS_GL(NS).GRPID
1374: 
1375:         write(mpi_efdc_out_unit,1002) NCARD
1376:         write(mpi_efdc_out_unit,*) BCPS_GL(NS).I, BCPS_GL(NS).J, BCPS_GL(NS).QSSE, BCPS_GL(NS).NQSMUL, BCPS_GL(NS).NQSMF, BCPS_GL(NS).NQSERQ,   BCPS_GL(NS).NCSERQ(1), BCPS_GL(NS).NCSERQ(2), BCPS_GL(NS).NCSERQ(3), BCPS_GL(NS).NCSERQ(4), BCPS_GL(NS).NCSERQ(5),  &
1377:           BCPS_GL(NS).NCSERQ(6), BCPS_GL(NS).NCSERQ(7), BCPS_GL(NS).QWIDTH,   BCPS_GL(NS).QFACTOR,  BCPS_GL(NS).GRPID
1378:         if( ISO > 0 ) GOTO 100
```

**New source evidence**

```fortran
_staging/efdc-prescan/new/EFDC__input.f90:1457-1470
1457:   NGRPID = 0
1458:   if( NQSIJ > 0 )then
1459:     !C24*  READ VOLUME SOURCE/SINK LOCATIONS, MAGNITUDES, & VOL & CONC SERIES
1460:     NCARD = '24'
1461:     if( process_id == master_id )then
1462:       call SEEK('C24',0)
1463:       do NS = 1,NQSIJ
1464:         read(1,*,IOSTAT = ISO) BCPS_GL(NS).I, BCPS_GL(NS).J, BCPS_GL(NS).QSSE, BCPS_GL(NS).NQSMUL, BCPS_GL(NS).NQSMF, BCPS_GL(NS).NQSERQ,   BCPS_GL(NS).NCSERQ(1), BCPS_GL(NS).NCSERQ(2), BCPS_GL(NS).NCSERQ(3), BCPS_GL(NS).NCSERQ(4), BCPS_GL(NS).NCSERQ(5),  &
1465:           BCPS_GL(NS).NCSERQ(6), BCPS_GL(NS).NCSERQ(7), BCPS_GL(NS).QWIDTH,   BCPS_GL(NS).QFACTOR,  BCPS_GL(NS).GRPID
1466: 
1467:         write(mpi_efdc_out_unit,1002) NCARD
1468:         write(mpi_efdc_out_unit,*) BCPS_GL(NS).I, BCPS_GL(NS).J, BCPS_GL(NS).QSSE, BCPS_GL(NS).NQSMUL, BCPS_GL(NS).NQSMF, BCPS_GL(NS).NQSERQ,   BCPS_GL(NS).NCSERQ(1), BCPS_GL(NS).NCSERQ(2), BCPS_GL(NS).NCSERQ(3), BCPS_GL(NS).NCSERQ(4), BCPS_GL(NS).NCSERQ(5),  &
1469:           BCPS_GL(NS).NCSERQ(6), BCPS_GL(NS).NCSERQ(7), BCPS_GL(NS).QWIDTH,   BCPS_GL(NS).QFACTOR,  BCPS_GL(NS).GRPID
1470:         if( ISO > 0 ) GOTO 100
```

**Triggering upstream change**: 인접 C23 echo 재배치 hunk의 말미 context가 C24 범위 시작과 겹침.

**Changed file**: `EFDC/input.f90`

**Changed hunk (@@), citation intersection, exact evidence**

```text
@@ -1355,12 +1448,11 @@ SUBROUTINE INPUT() | citation∩old-hunk=1365-1366; deleted/replaced old lines inside citation=none; new hunk=1448-1458
Full citation content identity: YES; old 1365-1378 == new 1457-1470
```

**Semantic delta**: C24 NGRPID 초기화부터 ISO 검사까지 14행 전체 및 나열된 필드가 정확히 동일.

**Reason**: 교집합 1365–1366은 변경행이 아닌 context이다. 전체 인용 1365–1378 = new 1457–1470을 행별 동일성으로 확인했다. 88행의 C24 필드 설명은 유지되며 C23 판정을 전파하지 않는다.

### B1-7 — REVIEW_ONLY

- Note: `models/EFDC/source-analysis/efdc_boundary_conditions.md:110`
- Section/line: D. NPBS / NPBE / NPBN / NPBW (pressure BC indices) (L108) / claim L110
- Confidence: HIGH (분류 제안에 대한 확신; 모델 실행 검증 아님)
- Decision: `needs_claude_review` — Claude 최종 판정 대기; Codex 제안만 기록. 내부 변경의 claim 영향 검토 및 인용 재매핑 여부 확인.

**Current wiki claim (원문)**

```text
C16 reads counts: `NPBS, NPBW, NPBE, NPBN, NPFOR, NPFORT, NPSER, PDGINIT` (`input.f90:870-889`).
```

**Old source evidence**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:870-889
870:   !C16*  READ SURFACE ELEVATION OR PRESSURE BOUNDARY CONDITION parameterS
871:   NCARD = '16'
872:   ! *** ********************************************************
873:   if( process_id == master_id )then
874:     call SEEK('C16',0)
875:     read(1,*,IOSTAT = ISO) NPBS, NPBW, NPBE, NPBN, NPFOR_Readin, NPFORT, NPSER, PDGINIT
876: 
877:     write(mpi_efdc_out_unit,1002) NCARD
878:     write(mpi_efdc_out_unit,*) NPBS, NPBW, NPBE, NPBN, NPFOR_Readin, NPFORT, NPSER, PDGINIT
879:     if( ISO > 0 ) GOTO 100
880:   endif
881: 
882:   call Broadcast_Scalar(NPBS        , master_id)
883:   call Broadcast_Scalar(NPBW        , master_id)
884:   call Broadcast_Scalar(NPBE        , master_id)
885:   call Broadcast_Scalar(NPBN        , master_id)
886:   call Broadcast_Scalar(NPFOR_Readin, master_id)
887:   call Broadcast_Scalar(NPFORT      , master_id)
888:   call Broadcast_Scalar(NPSER       , master_id)
889:   call Broadcast_Scalar(PDGINIT     , master_id)
```

**New source evidence**

```fortran
_staging/efdc-prescan/new/EFDC__input.f90:903-922
903:   !C16*  READ SURFACE ELEVATION OR PRESSURE BOUNDARY CONDITION parameterS
904:   NCARD = '16'
905:   ! *** ********************************************************
906:   if( process_id == master_id )then
907:     call SEEK('C16',0)
908:     read(1,*,IOSTAT = ISO) NPBS, NPBW, NPBE, NPBN, NPFOR_Readin, NPFORT, NPSER, PDGINIT
909:     if( ISO > 0 ) GOTO 100
910:   endif
911: 
912:   call Broadcast_Scalar(NPBS        , master_id)
913:   call Broadcast_Scalar(NPBW        , master_id)
914:   call Broadcast_Scalar(NPBE        , master_id)
915:   call Broadcast_Scalar(NPBN        , master_id)
916:   call Broadcast_Scalar(NPFOR_Readin, master_id)
917:   call Broadcast_Scalar(NPFORT      , master_id)
918:   call Broadcast_Scalar(NPSER       , master_id)
919:   call Broadcast_Scalar(PDGINIT     , master_id)
920: 
921:   write(mpi_efdc_out_unit,1002) NCARD
922:   write(mpi_efdc_out_unit,*) NPBS, NPBW, NPBE, NPBN, NPFOR_Readin, NPFORT, NPSER, PDGINIT
```

**Triggering upstream change**: C16 echo를 broadcast 뒤로 이동.

**Changed file**: `EFDC/input.f90`

**Changed hunk (@@), citation intersection, exact evidence**

```text
@@ -849,22 +878,26 @@ SUBROUTINE INPUT() | citation∩old-hunk=870-870; deleted/replaced old lines inside citation=none; new hunk=878-903
@@ -873,9 +906,6 @@ SUBROUTINE INPUT() | citation∩old-hunk=873-881; deleted/replaced old lines inside citation=876,877,878; new hunk=906-911
@@ -888,6 +918,9 @@ SUBROUTINE INPUT() | citation∩old-hunk=888-889; deleted/replaced old lines inside citation=none; new hunk=918-926
Full citation content identity: NO; interval includes edits (not endpoint-only comparison).
```

**Semantic delta**: NPBS/NPBW/NPBE/NPBN/NPFOR_Readin/NPFORT/NPSER/PDGINIT 입력과 broadcast 유지.

**Reason**: 110행은 C16의 입력 목록 설명이며 echo 위치를 주장하지 않는다. 노트 NPFOR와 실제 NPFOR_Readin의 명칭 차이는 old에도 존재해 이번 upstream delta가 아니다. 내부 출력 이동은 검토로 남기되 입력 필드 의미 변경으로 분류하지 않는다.

### B1-8 — REVIEW_ONLY

- Note: `models/EFDC/source-analysis/efdc_boundary_conditions.md:137`
- Section/line: F. SUBCHAN (subgrid channel) (L135) / claim L137
- Confidence: HIGH (분류 제안에 대한 확신; 모델 실행 검증 아님)
- Decision: `needs_claude_review` — Claude 최종 판정 대기; Codex 제안만 기록. 내부 변경의 claim 영향 검토 및 인용 재매핑 여부 확인.

**Current wiki claim (원문)**

```text
`MODCHAN.INP` read when `ISCHAN > 0`. Supplies `MDCHH, QCHERR, channel type, host cell, U/V channel cells`, plus channel length/friction for `ISCHAN==2` (`input.f90:3656-3689`).
```

**Old source evidence**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:3656-3689
3656:   ! *** OPEN FILE MODCHAN.INP TO INSERT SUBGRID CHANNELS INTO HOST CELLS
3657:   MDCHH = 0
3658:   if( ISCHAN > 0 )then
3659:     if( process_id == master_id )then
3660:       write(*,'(A)')'READING MODCHAN.INP'
3661:       open(1,FILE = 'modchan.inp',STATUS = 'UNKNOWN')
3662: 
3663:       ! *** SKIP OVER TITLE AND AND HEADER LINES
3664:       STR = READSTR(1)
3665:       if( ISCHAN == 1 )then
3666:         read(1,*) MDCHH, ldum, ldum
3667:         read(1,*) ldum, ldum, QCHERR
3668:         if( MDCHH >= 1 )then
3669:           do NMD = 1,MDCHH
3670:             read(1,*)MDCHTYP(NMD),IMDCHH(NMD),JMDCHH(NMD),IMDCHU(NMD),JMDCHU(NMD),IMDCHV(NMD),JMDCHV(NMD)
3671:             QCHANU(NMD) = 0.
3672:             QCHANUN(NMD) = 0.
3673:             QCHANV(NMD) = 0.
3674:             QCHANVN(NMD) = 0.
3675:           enddo
3676:         endif
3677:       endif
3678:       if( ISCHAN == 2 )then
3679:         read(1,*) MDCHH, ldum, ldum
3680:         read(1,*) ldum, ldum, QCHERR
3681:         if( MDCHH >= 1 )then
3682:           do NMD = 1,MDCHH
3683:             read(1,*)MDCHTYP(NMD),IMDCHH(NMD),JMDCHH(NMD),IMDCHU(NMD),JMDCHU(NMD),IMDCHV(NMD),JMDCHV(NMD),CHANLEN(NMD),PMDCH(NMD)
3684:             QCHANU(NMD) = 0.
3685:             QCHANUN(NMD) = 0.
3686:             QCHANV(NMD) = 0.
3687:             QCHANVN(NMD) = 0.
3688:           enddo
3689:         endif
```

**New source evidence**

```fortran
_staging/efdc-prescan/new/EFDC__input.f90:3753-3779
3753:   ! *** OPEN FILE MODCHAN.INP TO INSERT SUBGRID CHANNELS INTO HOST CELLS
3754:   MDCHH = 0
3755:   if( ISCHAN > 0 )then
3756:     if( process_id == master_id )then
3757:       write(*,'(A)')'READING MODCHAN.INP'
3758:       open(1,FILE = 'modchan.inp',STATUS = 'UNKNOWN')
3759: 
3760:       ! *** SKIP OVER TITLE AND AND HEADER LINES
3761:       STR = READSTR(1)
3762:       if( ISCHAN == 1 )then
3763:         read(1,*) MDCHH, ldum, ldum
3764:         read(1,*) ldum, ldum, QCHERR
3765:         if( MDCHH >= 1 )then
3766:           do NMD = 1,MDCHH
3767:             read(1,*)MDCHTYP(NMD),IMDCHH(NMD),JMDCHH(NMD),IMDCHU(NMD),JMDCHU(NMD),IMDCHV(NMD),JMDCHV(NMD)
3768:           enddo
3769:         endif
3770:       endif
3771:       if( ISCHAN == 2 )then
3772:         read(1,*) MDCHH, ldum, ldum
3773:         read(1,*) ldum, ldum, QCHERR
3774:         if( MDCHH >= 1 )then
3775:           do NMD = 1,MDCHH
3776:             read(1,*)MDCHTYP(NMD),IMDCHH(NMD),JMDCHH(NMD),IMDCHU(NMD),JMDCHU(NMD),IMDCHV(NMD),JMDCHV(NMD),CHANLEN(NMD),PMDCH(NMD)
3777:           enddo
3778:         endif
3779:       endif

_staging/efdc-prescan/new/EFDC__input.f90:3796-3810
3796:     ! *** Map the global channel data to the local subdomain
3797:     MDCHH_GL = MDCHH
3798:     MDCHH = 0
3799:     do NMD = 1,MDCHH_GL
3800:       if( LIJ_Global(IMDCHH(NMD),JMDCHH(NMD)) < 2 )then
3801:         if( process_id == master_id )then
3802:           write(6,*) 'ERROR!  HOST CELL IS NOT IN THE GLOBAL DOMAIN FOR SUBGRID CHANNEL: ',NMD
3803:         endif
3804:         call STOPP('', 1)
3805:       endif
3806: 
3807:       ! *** Local host cell indices
3808:       ITMP = IG2IL(IMDCHH(NMD))
3809:       JTMP = JG2JL(JMDCHH(NMD))
3810:       INHOST = ITMP > 0 .and. ITMP <= IC .and. JTMP > 0 .and. JTMP <= JC

_staging/efdc-prescan/new/EFDC__input.f90:3838-3844
3838:       endif
3839: 
3840:       ! *** Keep the channels in the current subdomain
3841:       if( INHOST )then
3842:         MDCHH = MDCHH + 1
3843: 
3844:         MDCHTYP(MDCHH) = MDCHTYP(NMD)

_staging/efdc-prescan/new/EFDC__input.f90:3867-3872
3867: 
3868:         QCHANU (MDCHH) = 0.
3869:         QCHANUN(MDCHH) = 0.
3870:         QCHANV (MDCHH) = 0.
3871:         QCHANVN(MDCHH) = 0.
3872:       endif
```

**Triggering upstream change**: MODCHAN 읽기 루프의 QCHAN* 초기화를 새 로컬 매핑 뒤로 이동.

**Changed file**: `EFDC/input.f90`

**Changed hunk (@@), citation intersection, exact evidence**

```text
@@ -3668,10 +3765,6 @@ SUBROUTINE INPUT() | citation∩old-hunk=3668-3677; deleted/replaced old lines inside citation=3671,3672,3673,3674; new hunk=3765-3770
@@ -3681,32 +3774,15 @@ SUBROUTINE INPUT() | citation∩old-hunk=3681-3689; deleted/replaced old lines inside citation=3684,3685,3686,3687; new hunk=3774-3788
Full citation content identity: NO; interval includes edits (not endpoint-only comparison).
```

**Semantic delta**: ISCHAN>0 파일 열기 및 ISCHAN 1/2별 입력 목록, ISCHAN==2의 CHANLEN/PMDCH는 유지; 후속 MPI 매핑 조건 추가.

**Reason**: 137행은 파일을 여는 조건과 공급 필드만 설명하므로 새 후처리 조건 때문에 거짓이 되지는 않는다. 인용 내부 초기화 삭제가 있고 설명이 후속 제약을 담지 않으므로 REVIEW_ONLY. 139행 매핑 문장을 별도 후보로 늘리지 않는다.

### B1-9 — REVIEW_ONLY

- Note: `models/EFDC/source-analysis/efdc_boundary_conditions.md:152`
- Section/line: G. Tide harmonic synthesis (MTIDE, NPFOR) (L148) / claim L152
- Confidence: HIGH (분류 제안에 대한 확신; 모델 실행 검증 아님)
- Decision: `needs_claude_review` — Claude 최종 판정 대기; Codex 제안만 기록. 내부 변경의 claim 영향 검토 및 인용 재매핑 여부 확인.

**Current wiki claim (원문)**

```text
- C14 reads `MTIDE` (`input.f90:732-754`).
```

**Old source evidence**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:732-754
732:   !C14*  READ TIDAL & ATMOSPHERIC FORCING, GROUND WATER AND SUBGRID CHANNEL parameterS
733:   NCARD = '14'
734:   ! *** ********************************************************
735:   if( process_id == master_id )then
736:     call SEEK('C14',0)
737:     read(1,*,IOSTAT = ISO) MTIDE, NWSER, NASER, ISGWIT, ISCHAN, ISWAVE, ITIDASM, ISPERC, ISBODYF, ISPNHYDS, ISPROPWASH
738: 
739:     write(mpi_efdc_out_unit,1002) NCARD
740:     write(mpi_efdc_out_unit,*) MTIDE, NWSER, NASER, ISGWIT, ISCHAN, ISWAVE, ITIDASM, ISPERC, ISBODYF, ISPNHYDS, ISPROPWASH
741:     if( ISO > 0 ) GOTO 100
742:   endif
743: 
744:   call Broadcast_Scalar(MTIDE     , master_id)
745:   call Broadcast_Scalar(NWSER     , master_id)
746:   call Broadcast_Scalar(NASER     , master_id)
747:   call Broadcast_Scalar(ISGWIT    , master_id)
748:   call Broadcast_Scalar(ISCHAN    , master_id)
749:   call Broadcast_Scalar(ISWAVE    , master_id)
750:   call Broadcast_Scalar(ITIDASM   , master_id)
751:   call Broadcast_Scalar(ISPERC    , master_id)
752:   call Broadcast_Scalar(ISBODYF   , master_id)
753:   call Broadcast_Scalar(ISPNHYDS  , master_id)
754:   call Broadcast_Scalar(ISPROPWASH, master_id)
```

**New source evidence**

```fortran
_staging/efdc-prescan/new/EFDC__input.f90:755-778
755:   !C14*  READ TIDAL & ATMOSPHERIC FORCING, GROUND WATER AND SUBGRID CHANNEL parameterS
756:   NCARD = '14'
757:   ! *** ********************************************************
758:   if( process_id == master_id )then
759:     call SEEK('C14',0)
760:     read(1,*,IOSTAT = ISO) MTIDE, NWSER, NASER, ISGWIT, ISCHAN, ISWAVE, ITIDASM, ISPERC, ISBODYF, ISPNHYDS, ISPROPWASH
761:     if( ISO > 0 ) GOTO 100
762:   endif
763: 
764:   call Broadcast_Scalar(MTIDE     , master_id)
765:   call Broadcast_Scalar(NWSER     , master_id)
766:   call Broadcast_Scalar(NASER     , master_id)
767:   call Broadcast_Scalar(ISGWIT    , master_id)
768:   call Broadcast_Scalar(ISCHAN    , master_id)
769:   call Broadcast_Scalar(ISWAVE    , master_id)
770:   call Broadcast_Scalar(ITIDASM   , master_id)
771:   call Broadcast_Scalar(ISPERC    , master_id)
772:   call Broadcast_Scalar(ISBODYF   , master_id)
773:   call Broadcast_Scalar(ISPNHYDS  , master_id)
774: 
775:   write(mpi_efdc_out_unit,1002) NCARD
776:   write(mpi_efdc_out_unit,*) MTIDE, NWSER, NASER, ISGWIT, ISCHAN, ISWAVE, ITIDASM, ISPERC, ISBODYF, ISPNHYDS, ISPROPWASH
777: 
778:   call Broadcast_Scalar(ISPROPWASH, master_id)
```

**Triggering upstream change**: C14 echo를 master read 블록 밖으로 이동.

**Changed file**: `EFDC/input.f90`

**Changed hunk (@@), citation intersection, exact evidence**

```text
@@ -729,15 +749,15 @@ SUBROUTINE INPUT() | citation∩old-hunk=732-743; deleted/replaced old lines inside citation=738,739,740; new hunk=749-763
@@ -751,6 +771,10 @@ SUBROUTINE INPUT() | citation∩old-hunk=751-754; deleted/replaced old lines inside citation=none; new hunk=771-780
Full citation content identity: NO; interval includes edits (not endpoint-only comparison).
```

**Semantic delta**: MTIDE는 여전히 C14 첫 입력이며 Broadcast_Scalar(MTIDE) 유지.

**Reason**: 152행의 MTIDE read 설명은 유지된다. 23행 인용 내부 write 이동이 있으므로 line-only 자동 판정 없이 범위 내부 변경 영향 없음으로 남긴다.

### B1-10 — REVIEW_ONLY

- Note: `models/EFDC/source-analysis/efdc_boundary_conditions.md:157`
- Section/line: G. Tide harmonic synthesis (MTIDE, NPFOR) (L148) / claim L157
- Confidence: HIGH (분류 제안에 대한 확신; 모델 실행 검증 아님)
- Decision: `needs_claude_review` — Claude 최종 판정 대기; Codex 제안만 기록. 내부 변경의 claim 영향 검토 및 인용 재매핑 여부 확인.

**Current wiki claim (원문)**

```text
- South `input.f90:980-1005`.
```

**Old source evidence**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:980-1005
980:           do M = 1,MTIDE
981:             if( NPFORS == 0) exit
982:             RAD = PI2*PFPH(NPFORS,M)/TCP(M)
983:             AMP = G*PFAM(NPFORS,M)
984:             PCBS_GL(L,M) = AMP*COS(RAD)
985:             PSBS_GL(L,M) = AMP*SIN(RAD)
986:           enddo
987:         enddo
988: 
989:       elseif( NPFORT == 1 )then
990:         do L = 1,NPBS
991:           read(1,*,IOSTAT = ISO) IPBS_GL(L), JPBS_GL(L), ISPBS_GL(L), ISPRS_GL(L), NPFORS, NPSERS_GL(L), NPSERS1_GL(L), TPCOORDS_GL(L)
992: 
993:           write(mpi_efdc_out_unit,1002) NCARD
994:           write(mpi_efdc_out_unit,*) IPBS_GL(L), JPBS_GL(L), ISPBS_GL(L), ISPRS_GL(L), NPFORS, NPSERS_GL(L), NPSERS1_GL(L), TPCOORDS_GL(L)
995:           if( ISO > 0 ) GOTO 100
996:           do M = 1,MTIDE
997:             if( NPFORS == 0) exit
998:             PCBS_GL(L,M) = CPFAM0(NPFORS,M)+TPCOORDS_GL(L)*CPFAM1(NPFORS,M) + TPCOORDS_GL(L)*TPCOORDS_GL(L)*CPFAM2(NPFORS,M)
999:             PSBS_GL(L,M) = SPFAM0(NPFORS,M)+TPCOORDS_GL(L)*SPFAM1(NPFORS,M) + TPCOORDS_GL(L)*TPCOORDS_GL(L)*SPFAM2(NPFORS,M)
1000:             TMPAMP = SQRT(PCBS(L,M)*PCBS(L,M)+PSBS_GL(L,M)*PSBS_GL(L,M))
1001:             TMPPHS = ATAN2(PSBS_GL(L,M),PCBS_GL(L,M))
1002:             TMPPHS = TMPPHS*TCP(M)/PI2
1003:             if( TMPPHS<0.0)TMPPHS = TMPPHS+TCP(M)
1004:             PCBS_GL(L,M) = G*PCBS_GL(L,M)
1005:             PSBS_GL(L,M) = G*PSBS_GL(L,M)
```

**New source evidence**

```fortran
_staging/efdc-prescan/new/EFDC__input.f90:1021-1044
1021:           do M = 1,MTIDE
1022:             if( NPFORS == 0) exit
1023:             RAD = PI2*PFPH(NPFORS,M)/TCP(M)
1024:             AMP = G*PFAM(NPFORS,M)
1025:             PCBS_GL(L,M) = AMP*COS(RAD)
1026:             PSBS_GL(L,M) = AMP*SIN(RAD)
1027:           enddo
1028:         enddo
1029: 
1030:       elseif( NPFORT == 1 )then
1031:         do L = 1,NPBS
1032:           read(1,*,IOSTAT = ISO) IPBS_GL(L), JPBS_GL(L), ISPBS_GL(L), ISPRS_GL(L), NPFORS, NPSERS_GL(L), NPSERS1_GL(L), TPCOORDS_GL(L)
1033:           if( ISO > 0 ) GOTO 100
1034:           
1035:           do M = 1,MTIDE
1036:             if( NPFORS == 0) exit
1037:             PCBS_GL(L,M) = CPFAM0(NPFORS,M)+TPCOORDS_GL(L)*CPFAM1(NPFORS,M) + TPCOORDS_GL(L)*TPCOORDS_GL(L)*CPFAM2(NPFORS,M)
1038:             PSBS_GL(L,M) = SPFAM0(NPFORS,M)+TPCOORDS_GL(L)*SPFAM1(NPFORS,M) + TPCOORDS_GL(L)*TPCOORDS_GL(L)*SPFAM2(NPFORS,M)
1039:             TMPAMP = SQRT(PCBS(L,M)*PCBS(L,M)+PSBS_GL(L,M)*PSBS_GL(L,M))
1040:             TMPPHS = ATAN2(PSBS_GL(L,M),PCBS_GL(L,M))
1041:             TMPPHS = TMPPHS*TCP(M)/PI2
1042:             if( TMPPHS<0.0)TMPPHS = TMPPHS+TCP(M)
1043:             PCBS_GL(L,M) = G*PCBS_GL(L,M)
1044:             PSBS_GL(L,M) = G*PSBS_GL(L,M)
```

**Triggering upstream change**: NPFORT==1 남쪽 C18 echo 삭제 후 broadcast 뒤에 재배치.

**Changed file**: `EFDC/input.f90`

**Changed hunk (@@), citation intersection, exact evidence**

```text
@@ -973,8 +1016,6 @@ SUBROUTINE INPUT() | citation∩old-hunk=980-980; deleted/replaced old lines inside citation=none; new hunk=1016-1021
@@ -989,10 +1030,8 @@ SUBROUTINE INPUT() | citation∩old-hunk=989-998; deleted/replaced old lines inside citation=992,993,994; new hunk=1030-1037
Full citation content identity: NO; interval includes edits (not endpoint-only comparison).
```

**Semantic delta**: RAD/AMP cos-sin 및 CPFAM/SPFAM 다항 합성, 마지막 G 곱은 그대로 유지.

**Reason**: 157행은 156행의 boundary harmonics → PCB/PSB (×G)를 남쪽 코드에 연결한다. 실제 수식·조건은 유지되지만 인용 내부 echo 변경이 있으므로 REVIEW_ONLY. 입력/출력 주변 수정과 합성 알고리즘 변경을 혼동하지 않는다.

### B1-11 — REVIEW_ONLY

- Note: `models/EFDC/source-analysis/efdc_ice.md:19`
- Section/line: Source basis (L17) / claim L19
- Confidence: HIGH (분류 제안에 대한 확신; 모델 실행 검증 아님)
- Decision: `needs_claude_review` — Claude 최종 판정 대기; Codex 제안만 기록. 내부 변경의 claim 영향 검토 및 인용 재매핑 여부 확인.

**Current wiki claim (원문)**

```text
- `input.f90:2524-2530, 6888-6911, 7000-7099` — `ISICE`, ice series readers.
```

**Old source evidence**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:7000-7024
7000:   ! *** Read in externally specified ice cover from the file ISER.INP
7001:   if( ISICE == 1 .and. NISER >= 1 )then
7002:     if( process_id == master_id )then
7003:       write(*,'(A)')'READING ISER.INP'
7004:       open(1,FILE = 'iser.inp')
7005:       STR = READSTR(1)
7006: 
7007:       do NS = 1,NISER
7008:         RICECOVT(NS) = 0.
7009:         RICETHKT(NS) = 0.
7010:         MITLAST(NS)  = 2
7011: 
7012:         read(1,*,IOSTAT = ISO) M,TSICE(NS).TMULT,TOFFSET,RMULADJCOV
7013:         if( ISO > 0 ) CALL STOPP('ISER.INP: READING ERROR')
7014: 
7015:         do M = 1,TSICE(NS).NREC
7016:           ! *** TSICE(NS).VAL(M,1) ice on/off flag.
7017:           ! *** TSICE(NS).VAL(M,2) is ice thickness, a legacy approach that was never used in EFDC
7018:           read(1,*,IOSTAT = ISO) TSICE(NS).TIM(M),TSICE(NS).VAL(M,1)
7019: 
7020:           if( TSICE(NS).VAL(M,1) > 0.0 )then    ! *** VAL(M,2) is not used, for display only
7021:             TSICE(NS).VAL(M,2) = RICETHK0       ! *** VAL(M,2) is not used, for display only
7022:           else                                  ! *** VAL(M,2) is not used, for display only
7023:             TSICE(NS).VAL(M,2) = 0.0            ! *** VAL(M,2) is not used, for display only
7024:           endif                                 ! *** VAL(M,2) is not used, for display only

models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:7034-7042
7034: 
7035:       close(1)
7036:     endif
7037: 
7038:   elseif( ISICE == 2 )then
7039:     if( process_id == master_id )then
7040:       write(*,'(A)')'READING ISTAT.INP'
7041:       open(1,FILE = 'istat.inp')
7042:       STR = READSTR(1)

models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:7068-7074
7068:   if( ISICE == 1 .and. NISER > 1 )then
7069:     ! *** Read ice time series weighting
7070:     if(process_id == master_id )then
7071:       write(*,'(A)')'READING ICEMAP.INP'
7072:       open(1,FILE = 'icemap.inp')
7073:       STR = READSTR(1)
7074:       read(1,*) NICEMAP

models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:7093-7099
7093:         RICEWHT(:,L,:) = RICEWHT_GLOBAL(:,LG,:)
7094:       endif
7095:     enddo
7096: 
7097:     if( process_id == master_id )then
7098:       close(1)
7099:     endif
```

**New source evidence**

```fortran
_staging/efdc-prescan/new/EFDC__input.f90:7152-7175
7152:   ! *** Read in externally specified ice cover from the file ISER.INP
7153:   if( ISICE == 1 .and. NISER >= 1 )then
7154:     if( process_id == master_id )then
7155:       write(*,'(A)')'READING ISER.INP'
7156:       open(1,FILE = 'iser.inp')
7157:       STR = READSTR(1)
7158: 
7159:       do NS = 1,NISER
7160:         RICECOVT(NS) = 0.
7161:         MITLAST(NS)  = 2
7162: 
7163:         read(1,*,IOSTAT = ISO) M,TSICE(NS).TMULT,TOFFSET,RMULADJCOV
7164:         if( ISO > 0 ) CALL STOPP('ISER.INP: READING ERROR')
7165: 
7166:         do M = 1,TSICE(NS).NREC
7167:           ! *** TSICE(NS).VAL(M,1) ice on/off flag.
7168:           ! *** TSICE(NS).VAL(M,2) is ice thickness, a legacy approach that was never used in EFDC
7169:           read(1,*,IOSTAT = ISO) TSICE(NS).TIM(M),TSICE(NS).VAL(M,1)
7170: 
7171:           if( TSICE(NS).VAL(M,1) > 0.0 )then    ! *** VAL(M,2) is not used, for display only
7172:             TSICE(NS).VAL(M,2) = RICETHK0       ! *** VAL(M,2) is not used, for display only
7173:           else                                  ! *** VAL(M,2) is not used, for display only
7174:             TSICE(NS).VAL(M,2) = 0.0            ! *** VAL(M,2) is not used, for display only
7175:           endif                                 ! *** VAL(M,2) is not used, for display only

_staging/efdc-prescan/new/EFDC__input.f90:7185-7205
7185: 
7186:       close(1)
7187:     endif
7188:     
7189:     ! *** send to all other processes
7190:     call Broadcast_Array(MITLAST,   master_id)
7191:     call Broadcast_Array(RICECOVT,  master_id)
7192:     
7193:     do NS = 1, NISER
7194:       call Broadcast_Scalar(TSICE(NS).NREC    , master_id)
7195:       call Broadcast_Scalar(TSICE(NS).TMULT   , master_id)
7196: 
7197:       call Broadcast_Array(TSICE(NS).TIM, master_id)
7198:       call Broadcast_Array(TSICE(NS).VAL, master_id)
7199:     enddo
7200:     
7201:   elseif( ISICE == 2 )then
7202:     if( process_id == master_id )then
7203:       write(*,'(A)')'READING ISTAT.INP'
7204:       open(1,FILE = 'istat.inp')
7205:       STR = READSTR(1)

_staging/efdc-prescan/new/EFDC__input.f90:7231-7237
7231:   if( ISICE == 1 .and. NISER > 1 )then
7232:     ! *** Read ice time series weighting
7233:     if(process_id == master_id )then
7234:       write(*,'(A)')'READING ICEMAP.INP'
7235:       open(1,FILE = 'icemap.inp')
7236:       STR = READSTR(1)
7237:       read(1,*) NICEMAP

_staging/efdc-prescan/new/EFDC__input.f90:7256-7262
7256:         RICEWHT(:,L,:) = RICEWHT_GLOBAL(:,LG,:)
7257:       endif
7258:     enddo
7259: 
7260:     if( process_id == master_id )then
7261:       close(1)
7262:     endif
```

**Triggering upstream change**: ISER 초기화에서 RICETHKT=0 삭제; MITLAST/RICECOVT 및 TSICE NREC/TMULT/TIM/VAL broadcast 추가.

**Changed file**: `EFDC/input.f90`

**Changed hunk (@@), citation intersection, exact evidence**

```text
@@ -7006,7 +7158,6 @@ SUBROUTINE INPUT() | citation∩old-hunk=7006-7012; deleted/replaced old lines inside citation=7009; new hunk=7158-7163
@@ -7034,7 +7185,19 @@ SUBROUTINE INPUT() | citation∩old-hunk=7034-7040; deleted/replaced old lines inside citation=none; new hunk=7185-7203
Full citation content identity: NO; interval includes edits (not endpoint-only comparison).
```

**Semantic delta**: 입력 reader 역할·ISICE 분기는 유지되며 ISICE==1 자료의 MPI 전달 경로가 추가됨.

**Reason**: 19행은 100행의 ice readers broad source-basis이다. 내부 초기화와 호출 변경이 있지만 기존 문장이 MPI 전달 부재나 RICETHKT 사용을 단언하지 않는다. broad citation 및 내부 변경으로 Claude 검토 대상이며 자동 NO_ACTION/line-only가 아니다.

### B1-12 — REVIEW_ONLY

- Note: `models/EFDC/source-analysis/efdc_ice.md:128`
- Section/line: H. Input data (L124) / claim L128
- Confidence: HIGH (분류 제안에 대한 확신; 모델 실행 검증 아님)
- Decision: `needs_claude_review` — Claude 최종 판정 대기; Codex 제안만 기록. 내부 변경의 claim 영향 검토 및 인용 재매핑 여부 확인.

**Current wiki claim (원문)**

```text
| `1` | `iser.inp` | `VAL(M,1)` = ice on/off or cover; `VAL(M,2)` = thickness (legacy/display only) (`input.f90:7000-7031`) |
```

**Old source evidence**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:7000-7031
7000:   ! *** Read in externally specified ice cover from the file ISER.INP
7001:   if( ISICE == 1 .and. NISER >= 1 )then
7002:     if( process_id == master_id )then
7003:       write(*,'(A)')'READING ISER.INP'
7004:       open(1,FILE = 'iser.inp')
7005:       STR = READSTR(1)
7006: 
7007:       do NS = 1,NISER
7008:         RICECOVT(NS) = 0.
7009:         RICETHKT(NS) = 0.
7010:         MITLAST(NS)  = 2
7011: 
7012:         read(1,*,IOSTAT = ISO) M,TSICE(NS).TMULT,TOFFSET,RMULADJCOV
7013:         if( ISO > 0 ) CALL STOPP('ISER.INP: READING ERROR')
7014: 
7015:         do M = 1,TSICE(NS).NREC
7016:           ! *** TSICE(NS).VAL(M,1) ice on/off flag.
7017:           ! *** TSICE(NS).VAL(M,2) is ice thickness, a legacy approach that was never used in EFDC
7018:           read(1,*,IOSTAT = ISO) TSICE(NS).TIM(M),TSICE(NS).VAL(M,1)
7019: 
7020:           if( TSICE(NS).VAL(M,1) > 0.0 )then    ! *** VAL(M,2) is not used, for display only
7021:             TSICE(NS).VAL(M,2) = RICETHK0       ! *** VAL(M,2) is not used, for display only
7022:           else                                  ! *** VAL(M,2) is not used, for display only
7023:             TSICE(NS).VAL(M,2) = 0.0            ! *** VAL(M,2) is not used, for display only
7024:           endif                                 ! *** VAL(M,2) is not used, for display only
7025:           if( ISO > 0 ) CALL STOPP('ISER.INP: READING ERROR')
7026:         enddo
7027: 
7028:         do M = 1,TSICE(NS).NREC
7029:           TSICE(NS).TIM(M)   = TSICE(NS).TIM(M) + TOFFSET
7030:           TSICE(NS).VAL(M,1) = RMULADJCOV*TSICE(NS).VAL(M,1)
7031:         enddo
```

**New source evidence**

```fortran
_staging/efdc-prescan/new/EFDC__input.f90:7152-7182
7152:   ! *** Read in externally specified ice cover from the file ISER.INP
7153:   if( ISICE == 1 .and. NISER >= 1 )then
7154:     if( process_id == master_id )then
7155:       write(*,'(A)')'READING ISER.INP'
7156:       open(1,FILE = 'iser.inp')
7157:       STR = READSTR(1)
7158: 
7159:       do NS = 1,NISER
7160:         RICECOVT(NS) = 0.
7161:         MITLAST(NS)  = 2
7162: 
7163:         read(1,*,IOSTAT = ISO) M,TSICE(NS).TMULT,TOFFSET,RMULADJCOV
7164:         if( ISO > 0 ) CALL STOPP('ISER.INP: READING ERROR')
7165: 
7166:         do M = 1,TSICE(NS).NREC
7167:           ! *** TSICE(NS).VAL(M,1) ice on/off flag.
7168:           ! *** TSICE(NS).VAL(M,2) is ice thickness, a legacy approach that was never used in EFDC
7169:           read(1,*,IOSTAT = ISO) TSICE(NS).TIM(M),TSICE(NS).VAL(M,1)
7170: 
7171:           if( TSICE(NS).VAL(M,1) > 0.0 )then    ! *** VAL(M,2) is not used, for display only
7172:             TSICE(NS).VAL(M,2) = RICETHK0       ! *** VAL(M,2) is not used, for display only
7173:           else                                  ! *** VAL(M,2) is not used, for display only
7174:             TSICE(NS).VAL(M,2) = 0.0            ! *** VAL(M,2) is not used, for display only
7175:           endif                                 ! *** VAL(M,2) is not used, for display only
7176:           if( ISO > 0 ) CALL STOPP('ISER.INP: READING ERROR')
7177:         enddo
7178: 
7179:         do M = 1,TSICE(NS).NREC
7180:           TSICE(NS).TIM(M)   = TSICE(NS).TIM(M) + TOFFSET
7181:           TSICE(NS).VAL(M,1) = RMULADJCOV*TSICE(NS).VAL(M,1)
7182:         enddo
```

**Triggering upstream change**: ISER 루프에서 RICETHKT(NS)=0 초기화 제거.

**Changed file**: `EFDC/input.f90`

**Changed hunk (@@), citation intersection, exact evidence**

```text
@@ -7006,7 +7158,6 @@ SUBROUTINE INPUT() | citation∩old-hunk=7006-7012; deleted/replaced old lines inside citation=7009; new hunk=7158-7163
Full citation content identity: NO; interval includes edits (not endpoint-only comparison).
```

**Semantic delta**: TIM/VAL(M,1) read와 VAL(M,2)=RICETHK0 또는 0의 display-only 생성, 시간 offset·cover 배율 적용은 동일.

**Reason**: 128행의 VAL(1) cover/on-off 및 VAL(2) legacy/display-only 의미는 new 주석과 대입문에도 유지된다. RICETHKT 초기화 삭제는 VAL(2)가 실제 parameter가 된 증거가 아니다. 인용 내부 변경이 있으나 해당 필드 의미에 영향 없음으로 REVIEW_ONLY.

### B1-13 — NO_ACTION

- Note: `models/EFDC/source-analysis/efdc_dispersion.md:23`
- Section/line: Source basis (L17) / claim L23
- Confidence: HIGH (분류 제안에 대한 확신; 모델 실행 검증 아님)
- Decision: `needs_claude_review` — Claude 최종 판정 대기; Codex 제안만 기록. 

**Current wiki claim (원문)**

```text
- `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:621, 3722-3795` — Card C12 read + spatially-variable mapping logic.
```

**Old source evidence**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:621-621
621:     read(1,*,IOSTAT = ISO) AHO, AHD, AVO, ABO, AVMX, ABMX, VISMUD, AVCON, ZBRWALL
```

**New source evidence**

```fortran
_staging/efdc-prescan/new/EFDC__input.f90:643-643
643:     read(1,*,IOSTAT = ISO) AHO, AHD, AVO, ABO, AVMX, ABMX, VISMUD, AVCON, ZBRWALL
```

**Triggering upstream change**: C12 주변 echo 재배치 hunk에 동일 read 행이 context로 포함됨.

**Changed file**: `EFDC/input.f90`

**Changed hunk (@@), citation intersection, exact evidence**

```text
@@ -603,25 +625,22 @@ SUBROUTINE INPUT() | citation∩old-hunk=621-621; deleted/replaced old lines inside citation=none; new hunk=625-646
Full citation content identity: YES; old 621-621 == new 643-643
```

**Semantic delta**: 9개 C12 필드 read 행은 문자 단위로 동일.

**Reason**: 후보 범위는 단일 행 621이며 new 643과 정확히 같다. 23행의 다른 인용 3722–3795는 B1-14에서 별도 판정한다. 이 후보에 공간 매핑 변경 판정을 자동 전파하지 않는다.

### B1-14 — REVIEW_ONLY

- Note: `models/EFDC/source-analysis/efdc_dispersion.md:23`
- Section/line: Source basis (L17) / claim L23
- Confidence: HIGH (분류 제안에 대한 확신; 모델 실행 검증 아님)
- Decision: `needs_claude_review` — Claude 최종 판정 대기; Codex 제안만 기록. 내부 변경의 claim 영향 검토 및 인용 재매핑 여부 확인.

**Current wiki claim (원문)**

```text
- `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:621, 3722-3795` — Card C12 read + spatially-variable mapping logic.
```

**Old source evidence**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:3722-3745
3722:   ! *** ENABLE SPATIALLY VARIABLE BACKGROUND AHO
3723:   if( AHO < 0. )then
3724:     AHMAX = ABS(AHO)
3725:     AHMIN = 1.0E32
3726:     do L = 2,LA
3727:       AHOXY(L) = ABS(AHO)*DXP(L)*DYP(L)
3728:       AHMAX    = max(AHOXY(L),AHMAX)
3729:       AHMIN    = min(AHOXY(L),AHMIN)
3730:     enddo
3731: 
3732:     if( process_id == master_id )then
3733:       PRINT '(A,2E16.5)','VARIABLE AHO USED (MIN,MAX): ', AHMIN, AHMAX
3734:     endif
3735: 
3736:   else
3737:     AHOXY = AHO
3738:   endif
3739: 
3740:   ! *** SMAGORINSKY AND BACKGROUND DIFFUSIVITY
3741:   ! *** Constant and/or default values
3742:   AHO = ABS(AHO)
3743: 
3744:   ! *** ENABLE SPATIALLY VARIABLE SMAGORINSKY AND BACKGROUND DIFFUSIVITY
3745:   if( AHD < 0. )then

models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:3761-3786
3761:       do LL = 2,LA_Global
3762:         read(1,*,END = 200) LG, ITMP, JTMP, T1, T2
3763: 
3764:         R2D_Global(LG,1) = T1
3765:         R2D_Global(LG,2) = T2
3766:       enddo
3767: 200   close(1)
3768:     endif
3769: 
3770:     call Broadcast_Array(R2D_Global, master_id)
3771: 
3772:     ! *** Map to Local Domain
3773:     do LG = 2,LA_GLOBAL
3774:       L = Map2Local(LG).LL
3775:       if( L > 1 )then
3776:         if( R2D_Global(LG,1) < 0. )then
3777:           AHOXY(L) = ABS(R2D_Global(LG,1))*DXP(L)*DYP(L)
3778:         else
3779:           AHOXY(L) = R2D_Global(LG,1)
3780:         endif
3781:         AHDXY(L) = R2D_Global(LG,2)
3782: 
3783:         AHMAX = max(AHOXY(L),AHMAX)
3784:         AHMIN = min(AHOXY(L),AHMIN)
3785:         ADMAX = max(AHDXY(L),ADMAX)
3786:         ADMIN = min(AHDXY(L),ADMIN)

models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:3789-3795
3789:     deallocate(R2D_Global)
3790: 
3791:     AHD = ABS(AHD)
3792:     PRINT '(A,4E12.4)','VARIABLE AHO & AHD USED (MIN,MAX): ',AHMIN,AHMAX,ADMIN,ADMAX
3793:   else
3794:     AHDXY = AHD       ! *** Constant value
3795:   endif
```

**New source evidence**

```fortran
_staging/efdc-prescan/new/EFDC__input.f90:3877-3900
3877:   ! *** ENABLE SPATIALLY VARIABLE BACKGROUND AHO
3878:   if( AHO < 0. )then
3879:     AHMAX = ABS(AHO)
3880:     AHMIN = 1.0E32
3881:     do L = 2,LA
3882:       AHOXY(L) = ABS(AHO)*DXP(L)*DYP(L)
3883:       AHMAX    = max(AHOXY(L),AHMAX)
3884:       AHMIN    = min(AHOXY(L),AHMIN)
3885:     enddo
3886: 
3887:     if( process_id == master_id )then
3888:       PRINT '(A,2E16.5)','VARIABLE AHO USED (MIN,MAX): ', AHMIN, AHMAX
3889:     endif
3890: 
3891:   else
3892:     AHOXY = AHO
3893:   endif
3894: 
3895:   ! *** SMAGORINSKY AND BACKGROUND DIFFUSIVITY
3896:   ! *** Constant and/or default values
3897:   AHO = ABS(AHO)
3898: 
3899:   ! *** ENABLE SPATIALLY VARIABLE SMAGORINSKY AND BACKGROUND DIFFUSIVITY
3900:   if( AHD < 0. )then

_staging/efdc-prescan/new/EFDC__input.f90:3916-3941
3916:       do LL = 2,LA_Global
3917:         read(1,*,END = 200) LG, ITMP, JTMP, T1, T2
3918: 
3919:         R2D_Global(LG,1) = T1
3920:         R2D_Global(LG,2) = T2
3921:       enddo
3922: 200   close(1)
3923:     endif
3924: 
3925:     call Broadcast_Array(R2D_Global, master_id)
3926: 
3927:     ! *** Map to Local Domain
3928:     do LG = 2,LA_GLOBAL
3929:       L = Map2Local(LG).LL
3930:       if( L > 1 )then
3931:         if( R2D_Global(LG,1) < 0. )then
3932:           AHOXY(L) = ABS(R2D_Global(LG,1))*DXP(L)*DYP(L)
3933:         else
3934:           AHOXY(L) = R2D_Global(LG,1)
3935:         endif
3936:         AHDXY(L) = R2D_Global(LG,2)
3937: 
3938:         AHMAX = max(AHOXY(L),AHMAX)
3939:         AHMIN = min(AHOXY(L),AHMIN)
3940:         ADMAX = max(AHDXY(L),ADMAX)
3941:         ADMIN = min(AHDXY(L),ADMIN)

_staging/efdc-prescan/new/EFDC__input.f90:3944-3952
3944:     deallocate(R2D_Global)
3945: 
3946:     AHD = ABS(AHD)
3947:     if( process_id == master_id )then
3948:       PRINT '(A,4E12.4)','VARIABLE AHO & AHD USED (MIN,MAX): ',AHMIN,AHMAX,ADMIN,ADMAX
3949:     endif
3950:   else
3951:     AHDXY = AHD       ! *** Constant value
3952:   endif
```

**Triggering upstream change**: AHO/AHD 최소·최대 PRINT에 master-only 조건 추가. 인접 큰 hunk의 subgrid 채널 변경은 인용 첫 행 context 앞에 위치.

**Changed file**: `EFDC/input.f90`

**Changed hunk (@@), citation intersection, exact evidence**

```text
@@ -3717,6 +3793,85 @@ SUBROUTINE INPUT() | citation∩old-hunk=3722-3722; deleted/replaced old lines inside citation=none; new hunk=3793-3877
@@ -3789,7 +3944,9 @@ SUBROUTINE INPUT() | citation∩old-hunk=3789-3795; deleted/replaced old lines inside citation=3792; new hunk=3944-3952
Full citation content identity: NO; interval includes edits (not endpoint-only comparison).
```

**Semantic delta**: AHO 부호/면적 scaling, AHD<0 AHMAP read, Map2Local/셀별 대입과 AHD=ABS/AHDXY=AHD 유지; 진단 출력 rank만 제한.

**Reason**: 74행 전체를 비교했으며 실제 내부 변경은 PRINT guard이다. 공간 매핑 알고리즘이나 필드 의미가 바뀌었다는 근거는 없다. >60행 내부 변경·broad source-basis 규칙에 따라 REVIEW_ONLY로 남긴다.

### B1-15 — NO_ACTION

- Note: `models/EFDC/source-analysis/efdc_dispersion.md:239`
- Section/line: 6. 입력 파라미터 — Card C12 (L228) / claim L239
- Confidence: HIGH (분류 제안에 대한 확신; 모델 실행 검증 아님)
- Decision: `needs_claude_review` — Claude 최종 판정 대기; Codex 제안만 기록. 

**Current wiki claim (원문)**

```text
| `AHO` | Constant horizontal momentum/mass diffusivity (m²/s) | m²/s | 0 | `input.f90:621` read, `:3737, 3742` use |
```

**Old source evidence**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:621-621
621:     read(1,*,IOSTAT = ISO) AHO, AHD, AVO, ABO, AVMX, ABMX, VISMUD, AVCON, ZBRWALL

models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:3736-3742
3736:   else
3737:     AHOXY = AHO
3738:   endif
3739: 
3740:   ! *** SMAGORINSKY AND BACKGROUND DIFFUSIVITY
3741:   ! *** Constant and/or default values
3742:   AHO = ABS(AHO)
```

**New source evidence**

```fortran
_staging/efdc-prescan/new/EFDC__input.f90:643-643
643:     read(1,*,IOSTAT = ISO) AHO, AHD, AVO, ABO, AVMX, ABMX, VISMUD, AVCON, ZBRWALL

_staging/efdc-prescan/new/EFDC__input.f90:3891-3897
3891:   else
3892:     AHOXY = AHO
3893:   endif
3894: 
3895:   ! *** SMAGORINSKY AND BACKGROUND DIFFUSIVITY
3896:   ! *** Constant and/or default values
3897:   AHO = ABS(AHO)
```

**Triggering upstream change**: C12 echo 이동 hunk의 context에 AHO read가 포함됨.

**Changed file**: `EFDC/input.f90`

**Changed hunk (@@), citation intersection, exact evidence**

```text
@@ -603,25 +625,22 @@ SUBROUTINE INPUT() | citation∩old-hunk=621-621; deleted/replaced old lines inside citation=none; new hunk=625-646
Full citation content identity: YES; old 621-621 == new 643-643
```

**Semantic delta**: 단일 인용 read 행과 AHOXY=AHO, AHO=ABS(AHO) 사용이 동일.

**Reason**: 239행 AHO 설명과 관련된 입력 슬롯/사용 의미는 유지된다. 이 후보는 621행이며 출력 변경행과 직접 교차하지 않는다. default의 외부 출처까지 새로 검증한 결과가 아니라 이 snapshot delta에 대한 NO_ACTION이다.

### B1-16 — NO_ACTION

- Note: `models/EFDC/source-analysis/efdc_dispersion.md:240`
- Section/line: 6. 입력 파라미터 — Card C12 (L228) / claim L240
- Confidence: HIGH (분류 제안에 대한 확신; 모델 실행 검증 아님)
- Decision: `needs_claude_review` — Claude 최종 판정 대기; Codex 제안만 기록. 

**Current wiki claim (원문)**

```text
| `AHD` | Dimensionless Smagorinsky coefficient $C_s$ (ISHDMF>0 필요) | — | 0.025 | `input.f90:621, 3791-3794` |
```

**Old source evidence**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:621-621
621:     read(1,*,IOSTAT = ISO) AHO, AHD, AVO, ABO, AVMX, ABMX, VISMUD, AVCON, ZBRWALL
```

**New source evidence**

```fortran
_staging/efdc-prescan/new/EFDC__input.f90:643-643
643:     read(1,*,IOSTAT = ISO) AHO, AHD, AVO, ABO, AVMX, ABMX, VISMUD, AVCON, ZBRWALL
```

**Triggering upstream change**: C12 echo 이동 hunk에 동일 AHD read 행 포함.

**Changed file**: `EFDC/input.f90`

**Changed hunk (@@), citation intersection, exact evidence**

```text
@@ -603,25 +625,22 @@ SUBROUTINE INPUT() | citation∩old-hunk=621-621; deleted/replaced old lines inside citation=none; new hunk=625-646
Full citation content identity: YES; old 621-621 == new 643-643
```

**Semantic delta**: AHD는 동일 C12 두 번째 필드로 읽힘.

**Reason**: 240행의 입력 AHD에 대한 직접 근거는 old/new 동일하다. 인용의 다른 구간 3791–3794는 B1-17에서 독립 판정한다. C12 echo만으로 계수 단위/default/ISHDMF 조건 변경을 추론하지 않는다.

### B1-17 — REVIEW_ONLY

- Note: `models/EFDC/source-analysis/efdc_dispersion.md:240`
- Section/line: 6. 입력 파라미터 — Card C12 (L228) / claim L240
- Confidence: HIGH (분류 제안에 대한 확신; 모델 실행 검증 아님)
- Decision: `needs_claude_review` — Claude 최종 판정 대기; Codex 제안만 기록. 내부 변경의 claim 영향 검토 및 인용 재매핑 여부 확인.

**Current wiki claim (원문)**

```text
| `AHD` | Dimensionless Smagorinsky coefficient $C_s$ (ISHDMF>0 필요) | — | 0.025 | `input.f90:621, 3791-3794` |
```

**Old source evidence**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:3789-3795
3789:     deallocate(R2D_Global)
3790: 
3791:     AHD = ABS(AHD)
3792:     PRINT '(A,4E12.4)','VARIABLE AHO & AHD USED (MIN,MAX): ',AHMIN,AHMAX,ADMIN,ADMAX
3793:   else
3794:     AHDXY = AHD       ! *** Constant value
3795:   endif
```

**New source evidence**

```fortran
_staging/efdc-prescan/new/EFDC__input.f90:3944-3952
3944:     deallocate(R2D_Global)
3945: 
3946:     AHD = ABS(AHD)
3947:     if( process_id == master_id )then
3948:       PRINT '(A,4E12.4)','VARIABLE AHO & AHD USED (MIN,MAX): ',AHMIN,AHMAX,ADMIN,ADMAX
3949:     endif
3950:   else
3951:     AHDXY = AHD       ! *** Constant value
3952:   endif
```

**Triggering upstream change**: AHD 정규화 직후 PRINT를 process_id==master_id 조건으로 제한.

**Changed file**: `EFDC/input.f90`

**Changed hunk (@@), citation intersection, exact evidence**

```text
@@ -3789,7 +3944,9 @@ SUBROUTINE INPUT() | citation∩old-hunk=3791-3794; deleted/replaced old lines inside citation=3792; new hunk=3944-3952
Full citation content identity: NO; interval includes edits (not endpoint-only comparison).
```

**Semantic delta**: AHD=ABS(AHD) 및 else AHDXY=AHD는 동일하고 계수 계산/상수 할당은 변경 없음.

**Reason**: 240행의 AHD 의미를 부정하는 변경은 없으나 인용 3791–3794 내부에 PRINT guard가 추가되었다. 범위 내부 출력 변경의 영향 없음으로 REVIEW_ONLY이며 B1-16 단일 read의 동일성을 이 범위 전체 동일성으로 확대하지 않는다.
