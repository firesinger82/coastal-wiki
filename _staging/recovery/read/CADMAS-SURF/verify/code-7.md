# CADMAS-SURF code-7 전수 대조

각 기록의 `file:` 원문을 구간별로 `nl -ba`와 `sed -n`으로 열어 대조했다.
대조한 원문 행 수에는 빈 행과 주석을 포함한다.
대상 19개 기록의 139개 구간 행을 완료했다.
대조한 원문은 아래 표의 합계인 5,183행이다.
각 기록 끝의 코드 사실도 대조했다.
정정과 보완은 해당 표식을 붙인 행 수로 집계했다.
정정에는 `vf_pmgst2.f.md`의 코드 사실 한 행을 포함했다.
두 표식이 있는 구간 행은 정정과 보완에 각각 집계했다.
이상 없음은 두 표식이 모두 없는 구간 행 수이다.

| 기록 | 대조한 구간 행 수 | 대조한 원문 행 수 | 상태 |
|---|---:|---:|---|
| vf_p3srd1.f.md | 5 | 181 | 완료 |
| vf_p3srd2.f.md | 5 | 205 | 완료 |
| vf_p3sri1.f.md | 5 | 181 | 완료 |
| vf_p3sri2.f.md | 5 | 205 | 완료 |
| vf_pcdc2p.f.md | 8 | 300 | 완료 |
| vf_pcdp2c.f.md | 8 | 278 | 완료 |
| vf_pmgbc0.f.md | 7 | 224 | 완료 |
| vf_pmgc2p.f.md | 21 | 870 | 완료 |
| vf_pmgc2p_cf.f.md | 6 | 207 | 완료 |
| vf_pmgflx.f.md | 3 | 65 | 완료 |
| vf_pmgfly.f.md | 3 | 65 | 완료 |
| vf_pmgggt.f.md | 6 | 307 | 완료 |
| vf_pmggpt.f.md | 6 | 228 | 완료 |
| vf_pmginp.f.md | 7 | 194 | 완료 |
| vf_pmgp2c.f.md | 12 | 489 | 완료 |
| vf_pmgp2c_cf.f.md | 4 | 138 | 완료 |
| vf_pmgp2c_pf.f.md | 8 | 309 | 완료 |
| vf_pmgset.f.md | 16 | 656 | 완료 |
| vf_pmgst2.f.md | 4 | 81 | 완료 |

기록 파일의 공통 경로는 `_staging/recovery/read/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/`이다.
원문 파일의 공통 경로는 `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/`이다.

원문 인용문과 행 번호의 일치를 확인했다.
빈 행을 제외한 모든 원문 행의 인용을 확인했다.
Markdown 표의 `\|`는 원문의 `|`를 표시하기 위한 이스케이프로 취급했다.
frontmatter와 구간 경계는 작업 시작본과 같다.
원문의 SHA-256은 각 기록의 frontmatter 값과 같다.
모델은 실행하지 않았다.
원문·노트·git은 수정하지 않았다.

## 정정·보완 목록

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_pcdc2p.f.md:96–127 (보완) | 시작 시 51행 부모 존재 분기·52행 LL 루프 안. | 시작 시 `      IF (MGPRNK.GE.0) THEN` (51) 안이다. 이 분기는 `      ENDIF` (195)에서 닫힌다. `        DO 290 LL=1,4` (52)는 ` 290    CONTINUE` (194)에서 닫힌다. | vf_pcdc2p.f:51–52, 194–195 |
| vf_pcdc2p.f.md:128–159 (보완) | 시작 시 51행 부모 존재 분기·52행 LL 루프 안. | 시작 시 `      IF (MGPRNK.GE.0) THEN` (51) 안이다. 이 분기는 `      ENDIF` (195)에서 닫힌다. `        DO 290 LL=1,4` (52)는 ` 290    CONTINUE` (194)에서 닫힌다. | vf_pcdc2p.f:51–52, 194–195 |
| vf_pcdc2p.f.md:160–196 (보완) | 시작 시 51행 부모 존재 분기·52행 LL 루프 안. | 시작 시 `      IF (MGPRNK.GE.0) THEN` (51) 안이다. 이 분기는 `      ENDIF` (195)에서 닫힌다. `        DO 290 LL=1,4` (52)는 ` 290    CONTINUE` (194)에서 닫힌다. | vf_pcdc2p.f:51–52, 194–195 |
| vf_pcdc2p.f.md:254–292 (보완) | 시작 시 198행 IC 루프·199행 LL 루프 안. | 시작 시 `      DO 600 IC=1,MGCNUM` (198) 안이다. 이 루프는 ` 600  CONTINUE` (291)에서 닫힌다. `        DO 590 LL=1,4` (199)는 ` 590    CONTINUE` (290)에서 닫힌다. | vf_pcdc2p.f:198–199, 290–291 |
| vf_pcdp2c.f.md:102–148 (보완) | 시작 시 51행 IC 루프·52행 LL 루프 안. | 시작 시 `      DO 300 IC=1,MGCNUM` (51) 안이다. 이 루프는 ` 300  CONTINUE` (147)에서 닫힌다. `        DO 290 LL=1,4` (52)는 ` 290    CONTINUE` (146)에서 닫힌다. | vf_pcdp2c.f:51–52, 146–147 |
| vf_pcdp2c.f.md:190–215 (보완) | 시작 시 150행 부모 존재 분기·151행 LL 루프 안. | 시작 시 `      IF (MGPRNK.GE.0) THEN` (150) 안이다. 이 분기는 `      ENDIF` (269)에서 닫힌다. `        DO 590 LL=1,4` (151)는 ` 590    CONTINUE` (268)에서 닫힌다. | vf_pcdp2c.f:150–151, 268–269 |
| vf_pcdp2c.f.md:216–241 (보완) | 시작 시 150행 부모 존재 분기·151행 LL 루프 안. | 시작 시 `      IF (MGPRNK.GE.0) THEN` (150) 안이다. 이 분기는 `      ENDIF` (269)에서 닫힌다. `        DO 590 LL=1,4` (151)는 ` 590    CONTINUE` (268)에서 닫힌다. | vf_pcdp2c.f:150–151, 268–269 |
| vf_pcdp2c.f.md:242–270 (보완) | 시작 시 150행 부모 존재 분기·151행 LL 루프 안. | 시작 시 `      IF (MGPRNK.GE.0) THEN` (150) 안이다. 이 분기는 `      ENDIF` (269)에서 닫힌다. `        DO 590 LL=1,4` (151)는 ` 590    CONTINUE` (268)에서 닫힌다. | vf_pcdp2c.f:150–151, 268–269 |
| vf_pmgbc0.f.md:77–120 (보완) | 시작 시 33행 IC 루프 안. | 시작 시 `      DO 300 IC=1,MGCNUM` (33) 안이다. 이 루프는 ` 300  CONTINUE` (143)에서 닫힌다. | vf_pmgbc0.f:33, 143 |
| vf_pmgbc0.f.md:121–144 (보완) | 시작 시 33행 IC 루프 안. | 시작 시 `      DO 300 IC=1,MGCNUM` (33) 안이다. 이 루프는 ` 300  CONTINUE` (143)에서 닫힌다. | vf_pmgbc0.f:33, 143 |
| vf_pmgbc0.f.md:183–216 (보완) | 시작 시 146행 부모 존재 분기 안. | 시작 시 `      IF (MGPRNK.GE.0) THEN` (146) 안이다. 이 분기는 `      ENDIF` (215)에서 닫힌다. | vf_pmgbc0.f:146, 215 |
| vf_pmgc2p.f.md:100–146 (보완) | 시작 시 85행 부모 존재 분기 안. | 시작 시 `      IF (MGPRNK.GE.0) THEN` (85) 안이다. 이 분기는 `      ENDIF` (294)에서 닫힌다. | vf_pmgc2p.f:85, 294 |
| vf_pmgc2p.f.md:147–193 (보완) | 시작 시 85행 부모 존재 분기 안. | 시작 시 `      IF (MGPRNK.GE.0) THEN` (85) 안이다. 이 분기는 `      ENDIF` (294)에서 닫힌다. | vf_pmgc2p.f:85, 294 |
| vf_pmgc2p.f.md:194–240 (보완) | 시작 시 85행 부모 존재 분기 안. | 시작 시 `      IF (MGPRNK.GE.0) THEN` (85) 안이다. 이 분기는 `      ENDIF` (294)에서 닫힌다. | vf_pmgc2p.f:85, 294 |
| vf_pmgc2p.f.md:241–295 (보완) | 시작 시 85행 부모 존재 분기 안. | 시작 시 `      IF (MGPRNK.GE.0) THEN` (85) 안이다. 이 분기는 `      ENDIF` (294)에서 닫힌다. | vf_pmgc2p.f:85, 294 |
| vf_pmgc2p.f.md:241–295 (정정) | DBUF 전체를 부모에 보내고 완료를 기다린다. | `          CALL VF_ZXMG_ISENDD(DBUF,NN,MGPRNK,IREQ,IERR)` (289)는 DBUF의 처음 NN개 값을 부모에 보낸다. `          CALL VF_ZXMG_WAIT(IREQ,IERR)` (290)로 완료를 기다린다. | vf_pmgc2p.f:283, 289–290 |
| vf_pmgc2p.f.md:354–397 (보완) | 시작 시 317행 IC 루프 안. | 시작 시 `      DO 600 IC=1,MGCNUM` (317) 안이다. 이 루프는 ` 600  CONTINUE` (531)에서 닫힌다. | vf_pmgc2p.f:317, 531 |
| vf_pmgc2p.f.md:398–439 (보완) | 시작 시 317행 IC 루프 안. | 시작 시 `      DO 600 IC=1,MGCNUM` (317) 안이다. 이 루프는 ` 600  CONTINUE` (531)에서 닫힌다. | vf_pmgc2p.f:317, 531 |
| vf_pmgc2p.f.md:440–481 (보완) | 시작 시 317행 IC 루프 안. | 시작 시 `      DO 600 IC=1,MGCNUM` (317) 안이다. 이 루프는 ` 600  CONTINUE` (531)에서 닫힌다. | vf_pmgc2p.f:317, 531 |
| vf_pmgc2p.f.md:482–534 (보완) | 시작 시 317행 IC 루프 안. | 시작 시 `      DO 600 IC=1,MGCNUM` (317) 안이다. 이 루프는 ` 600  CONTINUE` (531)에서 닫힌다. | vf_pmgc2p.f:317, 531 |
| vf_pmgc2p.f.md:588–618 (보완) | 시작 시 539행 부모 존재 분기 안. | 시작 시 `       IF (MGPRNK.GE.0) THEN` (539) 안이다. 이 분기는 `       ENDIF` (689)에서 닫힌다. 앞선 `      IF( ICONWL==0 ) GOTO 9999` (533)가 참이면 이 구간을 건너뛴다. | vf_pmgc2p.f:533, 539, 689 |
| vf_pmgc2p.f.md:619–652 (보완) | 시작 시 539행 부모 존재 분기 안. | 시작 시 `       IF (MGPRNK.GE.0) THEN` (539) 안이다. 이 분기는 `       ENDIF` (689)에서 닫힌다. 앞선 `      IF( ICONWL==0 ) GOTO 9999` (533)가 참이면 이 구간을 건너뛴다. | vf_pmgc2p.f:533, 539, 689 |
| vf_pmgc2p.f.md:653–692 (보완) | 시작 시 539행 부모 존재 분기 안. | 시작 시 `       IF (MGPRNK.GE.0) THEN` (539) 안이다. 이 분기는 `       ENDIF` (689)에서 닫힌다. 앞선 `      IF( ICONWL==0 ) GOTO 9999` (533)가 참이면 이 구간을 건너뛴다. | vf_pmgc2p.f:533, 539, 689 |
| vf_pmgc2p.f.md:727–757 (보완) | 시작 시 695행 IAMPARENT 분기·697행 IC 루프 안. | 시작 시 `      if( IAMPARENT.EQ.1 ) then` (695) 안이다. 이 분기는 `      endif` (858)에서 닫힌다. `      DO 1110 IC=1,MGCNUM` (697)는 ` 1110  CONTINUE` (856)에서 닫힌다. | vf_pmgc2p.f:695, 697, 856–858 |
| vf_pmgc2p.f.md:758–789 (보완) | 시작 시 695행 IAMPARENT 분기·697행 IC 루프 안. | 시작 시 `      if( IAMPARENT.EQ.1 ) then` (695) 안이다. 이 분기는 `      endif` (858)에서 닫힌다. `      DO 1110 IC=1,MGCNUM` (697)는 ` 1110  CONTINUE` (856)에서 닫힌다. | vf_pmgc2p.f:695, 697, 856–858 |
| vf_pmgc2p.f.md:790–821 (보완) | 시작 시 695행 IAMPARENT 분기·697행 IC 루프 안. | 시작 시 `      if( IAMPARENT.EQ.1 ) then` (695) 안이다. 이 분기는 `      endif` (858)에서 닫힌다. `      DO 1110 IC=1,MGCNUM` (697)는 ` 1110  CONTINUE` (856)에서 닫힌다. | vf_pmgc2p.f:695, 697, 856–858 |
| vf_pmgc2p.f.md:822–860 (보완) | 시작 시 695행 IAMPARENT 분기·697행 IC 루프 안. | 시작 시 `      if( IAMPARENT.EQ.1 ) then` (695) 안이다. 이 분기는 `      endif` (858)에서 닫힌다. `      DO 1110 IC=1,MGCNUM` (697)는 ` 1110  CONTINUE` (856)에서 닫힌다. | vf_pmgc2p.f:695, 697, 856–858 |
| vf_pmgc2p.f.md:535–587 (보완) | 부모가 있을 때 서쪽 경계의 ID×JD 영역에서 수직 적분한 수위를 계산한다. | `      IF( ICONWL==0 ) GOTO 9999` (533)는 ` 9999 CONTINUE` (868)로 이동한다. `      ICONWL=0                                                  ! 要修正` (69)이므로 현재 활성 코드에서는 이 수위 연결 구간을 건너뛴다. 해석: 이 우회가 없고 부모가 있을 때 서쪽 경계의 ID×JD 영역에서 수직 적분한 수위를 계산하는 구간이다. | vf_pmgc2p.f:69, 533, 539, 556–586, 868 |
| vf_pmgc2p_cf.f.md:94–130 (정정) | 시작 시 73행 x 방향 분기·76행 KC 루프·77행 JC 루프·94행 일반 면 ELSE 안. 방향성 이동량이 1.0D-20보다 크면 VF_PMGFLX를 호출한다. | 시작 시 `      IF(ABS(IDIR).EQ.1) THEN` (73) 안이다. 방향 분기 사슬은 `      END IF` (190)에서 닫힌다. `        DO 110 KC=KPF(KP-1)+1,KPF(KP)` (76)는 ` 110    CONTINUE` (129)에서 닫힌다. `          DO 100 JC=JPF(JP-1)+1,JPF(JP)` (77)는 ` 100      CONTINUE` (128)에서 닫힌다. 첫 행의 `            ELSE` (94)는 `            IF(L.LT.0) THEN` (83)과 `            ELSE IF(L.GT.0) THEN` (87)가 모두 거짓인 L=0 분기이다. 이 사슬은 `            END IF ` (127)에서 닫힌다. `              IF(IDIR*DTNOW*GGX(IC,JC,KC)*UU(IC,JC,KC).GT.1.0D-20) THEN` (102)이 참이면 VF_PMGFLX를 호출한다. | vf_pmgc2p_cf.f:73, 76–87, 94, 102–129, 190 |
| vf_pmgc2p_cf.f.md:131–160 (보완) | 시작 시 1–5행 VF_PMGC2P_CF 루틴 안이며 73행 IF의 병렬 ELSE IF가 이어진다. | 시작 시 `      IF(ABS(IDIR).EQ.1) THEN` (73)의 분기 사슬 안이다. `      ELSE IF(ABS(IDIR).EQ.2) THEN ` (132)가 이어진다. 이 사슬은 최종 ELSE 없이 `      END IF` (190)에서 닫힌다. | vf_pmgc2p_cf.f:73, 132, 190 |
| vf_pmgc2p_cf.f.md:161–191 (보완) | 시작 시 132행 y 방향 분기·135행 KC 루프·136행 IC 루프·153행 일반 면 ELSE 안. 이동량 조건에 따라 VF_PMGFLY 또는 인접 FF를 쓴다. | 시작 시 `      ELSE IF(ABS(IDIR).EQ.2) THEN ` (132) 안이다. 방향 분기 사슬은 `      END IF` (190)에서 닫힌다. `        DO 210 KC=KPF(KP-1)+1,KPF(KP)` (135)는 ` 210    CONTINUE` (188)에서 닫힌다. `          DO 200 IC=IPF(IP-1)+1,IPF(IP)` (136)는 ` 200      CONTINUE` (187)에서 닫힌다. `            ELSE` (153)는 `            IF(L.LT.0) THEN` (142)과 `            ELSE IF(L.GT.0) THEN` (146)가 모두 거짓인 L=0 분기이다. 이 사슬은 `            END IF` (186)에서 닫힌다. `              IF(IDIR*DTNOW*GGY(IC,JC,KC)*VV(IC,JC,KC).GT.1.0D-20) THEN` (161)에 따라 VF_PMGFLY 또는 인접 FF를 쓴다. | vf_pmgc2p_cf.f:132, 135–153, 161–190 |
| vf_pmgflx.f.md:1–23 (정정) | x 방향 이동량으로 면 VOF 함수를 계산한다. | 호출부는 `vf_pmgc2p_cf.f:104–106`에서 UDT에 DTNOW*GGX(IC,JC,KC)*UU(IC,JC,KC)를 전달한다. 해석: 이 인수를 이동량으로 보고 면의 VOF 함수를 계산하는 루틴으로 읽을 수 있다. | vf_pmgflx.f:1–23; vf_pmgc2p_cf.f:104–106 |
| vf_pmgflx.f.md:24–51 (정정) | UDT 부호에 따라 수용·공여·상류 셀 인덱스(index) LA·LD·LDM과 부호 LSN을 설정한다. NF=-1이면 경계 VOF 함수를 쓰고 그 외에는 셀 VOF 함수와 공극률(porosity)을 사용한다. | UDT가 0 이상이면 LSN=+1, LA=I, LD=I-1, LDM=I-2로 설정한다. 음수이면 LSN=-1, LA=I-1, LD=I, LDM=I+1로 설정한다. `      N = NF(LD,J,K)` (36)으로 검사 대상을 정한다. N=-1이면 `        FD = BCF(INDX(I,J,K))` (43)를 사용한다. N이 -1이 아니면 FD에 FF 값을 넣고 V에 XX(2,LD)*GGV(LD,J,K)를 넣는다. LA 위치의 NF가 -1이면 FA는 FD를 사용한다. 해석: LA·LD·LDM을 각각 수용·공여·상류 인덱스로 읽을 수 있다. | vf_pmgflx.f:24–51 |
| vf_pmgfly.f.md:1–23 (정정) | y 방향 이동량으로 면 VOF 함수를 계산한다. | 호출부는 `vf_pmgc2p_cf.f:163–165`에서 VDT에 DTNOW*GGY(IC,JC,KC)*VV(IC,JC,KC)를 전달한다. 해석: 이 인수를 이동량으로 보고 면의 VOF 함수를 계산하는 루틴으로 읽을 수 있다. | vf_pmgfly.f:1–23; vf_pmgc2p_cf.f:163–165 |
| vf_pmgfly.f.md:24–51 (정정) | VDT 부호에 따라 수용·공여·상류 셀 인덱스(index) LA·LD·LDM과 부호 LSN을 설정한다. NF=-1이면 경계 VOF 함수를 쓰고 그 외에는 셀 VOF 함수와 공극률(porosity)을 사용한다. | VDT가 0 이상이면 LSN=+1, LA=J, LD=J-1, LDM=J-2로 설정한다. 음수이면 LSN=-1, LA=J-1, LD=J, LDM=J+1로 설정한다. `      N = NF(I,LD,K)` (36)으로 검사 대상을 정한다. N=-1이면 `        FD = BCF(INDY(I,J,K))` (43)를 사용한다. N이 -1이 아니면 FD에 FF 값을 넣고 V에 YY(2,LD)*GGV(I,LD,K)를 넣는다. LA 위치의 NF가 -1이면 FA는 FD를 사용한다. 해석: LA·LD·LDM을 각각 수용·공여·상류 인덱스로 읽을 수 있다. | vf_pmgfly.f:24–51 |
| vf_pmgggt.f.md:39–106 (보완) | 모서리 및 방향별 MGPINF=1 조건은 해당 부모 셀의 복사를 건너뛴다. | 73–89행 분기 사슬은 모서리를 먼저 검사한다. 모서리 분기에서는 두 방향의 MGPINF가 모두 1일 때 복사를 건너뛴다. 그 뒤 단일 방향 분기에서는 해당 MGPINF가 1일 때 복사를 건너뛴다. 이 사슬에는 최종 ELSE가 없다. 각 `goto 120`의 대상은 ` 120      CONTINUE` (100)이다. | vf_pmgggt.f:73–100 |
| vf_pmgggt.f.md:107–170 (보완) | 외곽 범위와 MGPINF 조건에 따라 복사를 생략한다. | 129–145행 분기 사슬은 모서리를 먼저 검사한다. 모서리에서는 두 방향의 MGPINF가 모두 1일 때 복사를 생략한다. 그 뒤 단일 방향에서는 해당 MGPINF가 1일 때 복사를 생략한다. 최종 ELSE는 없다. 각 `goto 220`의 대상은 ` 220      CONTINUE` (164)이다. | vf_pmgggt.f:129–164 |
| vf_pmgggt.f.md:171–235 (보완) | 방향·모서리별 생략 조건과 자료 수 검사를 적용한다. | 193–209행 분기 사슬은 모서리를 먼저 검사한다. 모서리에서는 두 방향의 MGPINF가 모두 1일 때 복사를 생략한다. 그 뒤 단일 방향에서는 해당 MGPINF가 1일 때 복사를 생략한다. 최종 ELSE는 없다. 각 `goto 320`의 대상은 ` 320      CONTINUE` (228)이다. 자료 수가 다르면 `        CALL VF_A2ERR('VF_PMGGGT','PROGRAM ERROR(GGY).')` (232)를 호출한다. | vf_pmgggt.f:193–232 |
| vf_pmgggt.f.md:236–274 (보완) | 외곽 부모 셀을 순회하며 방향·모서리별 MGPINF=1 생략 조건을 적용한다. | 외곽 부모 셀을 순회한다. 257–273행 분기 사슬은 모서리를 먼저 검사한다. 모서리에서는 두 방향의 MGPINF가 모두 1일 때 복사를 생략한다. 그 뒤 단일 방향에서는 해당 MGPINF가 1일 때 복사를 생략한다. 최종 ELSE는 없다. 각 `goto 420`의 대상은 ` 420      CONTINUE` (290)이다. | vf_pmgggt.f:242–273, 290 |
| vf_pmgggt.f.md:275–307 (보완) | 시작 시 242행 K 루프·243행 J 루프·244행 I 루프·245행 외곽 조건 안. | 시작 시 `      DO 400 K=1,NZ+1` (242) 안이다. 이 루프는 ` 400  CONTINUE` (292)에서 닫힌다. `        DO 410 J=1,NY` (243)는 ` 410    CONTINUE` (291)에서 닫힌다. `          DO 420 I=1,NX` (244)는 ` 420      CONTINUE` (290)에서 닫힌다. `            IF(I.LE.1 .OR. I.GE.NX .OR. J.LE.1 .OR. J.GE.NY) THEN` (245)는 `            END IF` (289)에서 닫힌다. | vf_pmgggt.f:242–245, 289–292 |
| vf_pmginp.f.md:55–85 (정정) | 부모 연결을 MGARAN-1회 추적하여 순환을 검사한다. | `        IF (N.GT.0) THEN` (69)일 때 부모 연결을 최대 MGARAN-1회 추적한다. `            IF (N.LE.0) GOTO 310` (72)는 ` 310      CONTINUE` (74)로 이동하여 추적을 끝낸다. 추적 뒤에도 N이 양수이면 9040 표지(160)로 이동하여 입력값 오류를 처리한다. | vf_pmginp.f:65–76, 160–166 |
| vf_pmgp2c.f.md:95–135 (보완) | 시작 시 72행 IC 루프 안. | 시작 시 `      DO 300 IC=1,MGCNUM` (72) 안이다. 이 루프는 ` 300  CONTINUE` (266)에서 닫힌다. | vf_pmgp2c.f:72, 266 |
| vf_pmgp2c.f.md:136–176 (보완) | 시작 시 72행 IC 루프 안. | 시작 시 `      DO 300 IC=1,MGCNUM` (72) 안이다. 이 루프는 ` 300  CONTINUE` (266)에서 닫힌다. | vf_pmgp2c.f:72, 266 |
| vf_pmgp2c.f.md:177–217 (보완) | 시작 시 72행 IC 루프 안. | 시작 시 `      DO 300 IC=1,MGCNUM` (72) 안이다. 이 루프는 ` 300  CONTINUE` (266)에서 닫힌다. | vf_pmgp2c.f:72, 266 |
| vf_pmgp2c.f.md:218–267 (보완) | 시작 시 72행 IC 루프 안. | 시작 시 `      DO 300 IC=1,MGCNUM` (72) 안이다. 이 루프는 ` 300  CONTINUE` (266)에서 닫힌다. | vf_pmgp2c.f:72, 266 |
| vf_pmgp2c.f.md:268–305 (정정) | 자식이 있으면 SET_P2C로 자료를 모은다. | `      if( mgcnum.gt.0 ) then` (268) 안에서 `         CALL SET_P2C(rbuf,DBUF,MYRANK,NPROCS)` (269)를 호출한다. 해석: 이어지는 RBUF 송신을 준비하는 호출로 읽을 수 있다. | vf_pmgp2c.f:268–279 |
| vf_pmgp2c.f.md:306–346 (보완) | 시작 시 286행 부모 존재 분기 안. | 시작 시 `      IF (MGPRNK.GE.0) THEN` (286) 안이다. 이 분기는 `      ENDIF` (477)에서 닫힌다. | vf_pmgp2c.f:286, 477 |
| vf_pmgp2c.f.md:347–387 (보완) | 시작 시 286행 부모 존재 분기 안. | 시작 시 `      IF (MGPRNK.GE.0) THEN` (286) 안이다. 이 분기는 `      ENDIF` (477)에서 닫힌다. | vf_pmgp2c.f:286, 477 |
| vf_pmgp2c.f.md:388–428 (보완) | 시작 시 286행 부모 존재 분기 안. | 시작 시 `      IF (MGPRNK.GE.0) THEN` (286) 안이다. 이 분기는 `      ENDIF` (477)에서 닫힌다. | vf_pmgp2c.f:286, 477 |
| vf_pmgp2c.f.md:429–478 (보완) | 시작 시 286행 부모 존재 분기 안. | 시작 시 `      IF (MGPRNK.GE.0) THEN` (286) 안이다. 이 분기는 `      ENDIF` (477)에서 닫힌다. | vf_pmgp2c.f:286, 477 |
| vf_pmgp2c_cf.f.md:66–98 (정정) | VOF 함수는 수직 폭 역수 RDZ로 계산하고 0:1로 제한한다. | `          RDZ = 1.0D0/(ZPF(KC+1) - ZPF(KC))` (80)는 ZPF 차이의 역수이다. 이 차이는 부모 격자에 대한 보간계수의 차이이다(43). BCF는 이 RDZ를 사용하여 계산한 뒤 0과 1 사이로 제한한다. | vf_pmgp2c_cf.f:43, 80, 85–86 |
| vf_pmgp2c_cf.f.md:99–129 (보완) | 시작 시 1–5행 VF_PMGP2C_CF 루틴 안이며 71행 IF의 병렬 ELSE IF가 이어진다. | 시작 시 `      IF(ABS(IDIR).EQ.1) THEN` (71)의 분기 사슬 안이다. `      ELSE IF(ABS(IDIR).EQ.2) THEN ` (100)가 이어진다. 이 사슬은 최종 ELSE 없이 `      END IF` (128)에서 닫힌다. | vf_pmgp2c_cf.f:71, 100, 128 |
| vf_pmgp2c_pf.f.md:96–142 (보완) | 시작 시 66행 x 방향 분기·94행 일반 면 ELSE 안. | 시작 시 `      IF(ABS(IDIR).EQ.1) THEN` (66) 안이다. 방향 분기 사슬은 `      END IF` (299)에서 닫힌다. `        ELSE` (94)는 `        IF(L.LT.0) THEN` (70)과 `        ELSE IF(L.GT.0) THEN` (82)가 모두 거짓인 분기이다. 이 안쪽 사슬은 `        END IF` (180)에서 닫힌다. | vf_pmgp2c_pf.f:66, 70, 82, 94, 180, 299 |
| vf_pmgp2c_pf.f.md:143–181 (보완) | 시작 시 66행 x 방향 분기·94행 일반 면 ELSE 안. | 시작 시 `      IF(ABS(IDIR).EQ.1) THEN` (66) 안이다. 방향 분기 사슬은 `      END IF` (299)에서 닫힌다. `        ELSE` (94)는 `        IF(L.LT.0) THEN` (70)과 `        ELSE IF(L.GT.0) THEN` (82)가 모두 거짓인 분기이다. 이 안쪽 사슬은 `        END IF` (180)에서 닫힌다. | vf_pmgp2c_pf.f:66, 70, 82, 94, 180, 299 |
| vf_pmgp2c_pf.f.md:143–181 (정정) | 방향성 이동량이 -1.0D-20보다 작으면 VF_PMGFLX를 호출한다. | `          IF(IDIR*DTNOW*GGX(I,J,K)*UU(I,J,K).LT.-1.0D-20) THEN` (150)이 참이면 VF_PMGFLX를 호출한다. | vf_pmgp2c_pf.f:150–154 |
| vf_pmgp2c_pf.f.md:182–212 (보완) | 시작 시 1–4행 VF_PMGP2C_PF 루틴 안이며 66행 IF의 병렬 ELSE IF가 이어진다. | 시작 시 `      IF(ABS(IDIR).EQ.1) THEN` (66)의 분기 사슬 안이다. `      ELSE IF(ABS(IDIR).EQ.2) THEN ` (183)가 이어진다. 이 사슬은 최종 ELSE 없이 `      END IF` (299)에서 닫힌다. | vf_pmgp2c_pf.f:66, 183, 299 |
| vf_pmgp2c_pf.f.md:213–259 (보완) | 시작 시 183행 y 방향 분기·211행 일반 면 ELSE 안. | 시작 시 `      ELSE IF(ABS(IDIR).EQ.2) THEN ` (183) 안이다. 방향 분기 사슬은 `      END IF` (299)에서 닫힌다. `        ELSE` (211)는 `        IF(L.LT.0) THEN` (187)과 `        ELSE IF(L.GT.0) THEN` (199)가 모두 거짓인 분기이다. 이 안쪽 사슬은 `        END IF` (297)에서 닫힌다. | vf_pmgp2c_pf.f:183, 187, 199, 211, 297, 299 |
| vf_pmgp2c_pf.f.md:260–300 (보완) | 시작 시 183행 y 방향 분기·211행 일반 면 ELSE 안. | 시작 시 `      ELSE IF(ABS(IDIR).EQ.2) THEN ` (183) 안이다. 방향 분기 사슬은 `      END IF` (299)에서 닫힌다. `        ELSE` (211)는 `        IF(L.LT.0) THEN` (187)과 `        ELSE IF(L.GT.0) THEN` (199)가 모두 거짓인 분기이다. 이 안쪽 사슬은 `        END IF` (297)에서 닫힌다. | vf_pmgp2c_pf.f:183, 187, 199, 211, 297, 299 |
| vf_pmgp2c_pf.f.md:260–300 (정정) | 이동량 조건으로 VF_PMGFLY 호출 여부를 정한다. | `          IF(IDIR*DTNOW*GGY(I,J,K)*VV(I,J,K).LT.-1.0D-20) THEN` (267)이 참이면 VF_PMGFLY를 호출한다. | vf_pmgp2c_pf.f:267–271 |
| vf_pmgset.f.md:143–189 (보완) | 시작 시 107행 IC 루프·109행 부모 값 비영 분기·110행 자기 순위 분기 안. | 시작 시 `      DO 140 IC=0,MGPROC-1` (107) 안이다. 이 루프는 ` 140  CONTINUE` (376)에서 닫힌다. `        IF (MGPARE(IC+1).NE.0) THEN` (109)는 `        ENDIF` (375)에서 닫힌다. `          IF (MGRANK.EQ.IC) THEN` (110)는 `          ENDIF` (189)에서 닫힌다. | vf_pmgset.f:107–110, 189, 375–376 |
| vf_pmgset.f.md:190–226 (보완) | 시작 시 107행 IC 루프·109행 부모 값 비영 분기 안. | 시작 시 `      DO 140 IC=0,MGPROC-1` (107) 안이다. 이 루프는 ` 140  CONTINUE` (376)에서 닫힌다. `        IF (MGPARE(IC+1).NE.0) THEN` (109)는 `        ENDIF` (375)에서 닫힌다. | vf_pmgset.f:107–109, 375–376 |
| vf_pmgset.f.md:227–280 (보완) | 시작 시 107행 IC 루프·109행 부모 값 비영 분기·191행 부모 후보 분기 안. | 시작 시 `      DO 140 IC=0,MGPROC-1` (107) 안이다. 이 루프는 ` 140  CONTINUE` (376)에서 닫힌다. `        IF (MGPARE(IC+1).NE.0) THEN` (109)는 `        ENDIF` (375)에서 닫힌다. `          IF (MGPARE(IC+1).EQ.MGAREA(MGRANK+1)) THEN` (191)는 `          ENDIF` (374)에서 닫힌다. | vf_pmgset.f:107–109, 191, 374–376 |
| vf_pmgset.f.md:281–331 (보완) | 시작 시 107행 IC 루프·109행 부모 값 비영 분기·191행 부모 후보 분기·229–231행 포함 조건 안. | 시작 시 `      DO 140 IC=0,MGPROC-1` (107) 안이다. 이 루프는 ` 140  CONTINUE` (376)에서 닫힌다. `        IF (MGPARE(IC+1).NE.0) THEN` (109)는 `        ENDIF` (375)에서 닫힌다. `          IF (MGPARE(IC+1).EQ.MGAREA(MGRANK+1)) THEN` (191)는 `          ENDIF` (374)에서 닫힌다. 포함 조건은 `            IF ( XMS1.LE.XCS .AND. XCE.LE.XME1 .AND. ` (229), `     &           YMS1.LE.YCS .AND. YCE.LE.YME1 .AND. ` (230), `     &           ZMS .LE.ZCS .AND. ZCE.LE.ZME ) THEN` (231)의 연속 문장이다. 이 분기는 `            ENDIF` (351)에서 닫힌다. | vf_pmgset.f:107–109, 191, 229–231, 351, 374–376 |
| vf_pmgset.f.md:332–377 (보완) | 시작 시 107행 IC 루프·109행 부모 값 비영 분기·191행 부모 후보 분기·229–231행 포함 조건 안. | 시작 시 `      DO 140 IC=0,MGPROC-1` (107) 안이다. 이 루프는 ` 140  CONTINUE` (376)에서 닫힌다. `        IF (MGPARE(IC+1).NE.0) THEN` (109)는 `        ENDIF` (375)에서 닫힌다. `          IF (MGPARE(IC+1).EQ.MGAREA(MGRANK+1)) THEN` (191)는 `          ENDIF` (374)에서 닫힌다. 포함 조건은 `            IF ( XMS1.LE.XCS .AND. XCE.LE.XME1 .AND. ` (229), `     &           YMS1.LE.YCS .AND. YCE.LE.YME1 .AND. ` (230), `     &           ZMS .LE.ZCS .AND. ZCE.LE.ZME ) THEN` (231)의 연속 문장이다. 이 분기는 `            ENDIF` (351)에서 닫힌다. | vf_pmgset.f:107–109, 191, 229–231, 351, 374–376 |
| vf_pmgset.f.md:436–487 (보완) | 시작 시 392행 MGCNUM>0 분기 안. | 시작 시 `      IF( MGCNUM.GT.0 ) THEN` (392) 안이다. 이 분기는 `      ENDIF` (486)에서 닫힌다. | vf_pmgset.f:392, 486 |
| vf_pmgset.f.md:436–487 (정정) | GWRK 배열을 할당하고 SET_GGV_F·SET_GGV_UVW로 공극률(porosity)·상태·면적 투과율(area transmissivity)을 모은다. | GWRKF·GWRKU·GWRKV·GWRKW를 할당한다. SET_GGV_F에 GGV·NF를 전달한다. SET_GGV_UVW에는 GGX·GGY·GGZ를 각각 전달한다. 해석: 이 호출들은 뒤의 VF_PMGGPT 송신용 작업 배열을 준비하는 것으로 읽을 수 있다. | vf_pmgset.f:462–477, 518–520 |
| vf_pmgset.f.md:227–280 (정정) | 전역 x·y 범위 및 z 범위 안에 자식이 들어오면 부모 관계를 등록한다. | 229–231행은 XMS1·XME1·YMS1·YME1과 ZMS·ZME의 포함 조건을 검사한다. 이 조건이 참이면 부모 관계를 등록한다. MYRANK가 0이 아니면 앞선 87–92행에서 x·y 비교 변수 네 개를 0으로 설정한다. | vf_pmgset.f:87–92, 229–247 |
| vf_pmgset.f.md:488–529 (보완) | JSW(IP)가 0이 아닐 때 level=1이면 NF, level=2이면 nfwrk를 VF_PMGGGT에 넘긴다. | VF_PMGGGT 호출은 `        IF (MGPARE(IC+1).NE.0) THEN` (496)과 `          IF (MGRANK.EQ.IC) THEN` (497) 안에 있다. 그 안의 `              IF (JSW(IP).NE.0) THEN` (500)이 참일 때 level=1이면 NF를 넘긴다. 같은 조건에서 level=2이면 nfwrk를 넘긴다. level 검사는 별개의 단문 IF 두 개이며 ELSE는 없다. | vf_pmgset.f:494–507 |
| vf_pmgset.f.md:602–615 (보완) | level=2는 VF_P3SRD2로 GGV·GGX·GGY·GGZ를 각각 ISW=0·1·2·3으로 교환한다. | level=2는 VF_P3SRD2로 GGV·GGX·GGY·GGZ를 각각 ISW=0·1·2·3으로 교환한다. `         IF(LEVEL.EQ.1)THEN` (606)과 `         ELSEIF(LEVEL.EQ.2)THEN` (608)의 사슬은 최종 ELSE 없이 `         ENDIF` (613)에서 닫힌다. | vf_pmgset.f:605–614 |
| vf_pmgst2.f.md:23–43 (정정) | x 방향에서 부모 좌표 평균의 정수부에 1을 더하여 II를 구한다. | x 방향에서는 `        II = INT(0.5D0*(XPF(I)+XPF(I+1))) + 1` (35)로 II를 구한다. XPF의 인수 설명은 부모 격자의 x 방향 보간계수이다(`vf_pmgset.f:38`). | vf_pmgst2.f:35; vf_pmgset.f:38 |
| vf_pmgst2.f.md:44–58 (정정) | y 방향에서도 좌표 평균으로 JJ를 구해 셀 수를 센다. | y 방향에서는 `        JJ = INT(0.5D0*(YPF(J)+YPF(J+1))) + 1` (50)로 JJ를 구해 셀 수를 센다. YPF의 인수 설명은 부모 격자의 y 방향 보간계수이다(`vf_pmgset.f:39`). | vf_pmgst2.f:50–51; vf_pmgset.f:39 |
| vf_pmgst2.f.md:코드 사실 35–36·50–51·65–66 (정정) | 35–36·50–51·65–66: 평균 좌표에서 계산한 II·JJ·KK를 배열 첨자로 직접 사용하며 이 루틴에는 범위 검사 분기가 없다. | 35–36·50–51·65–66: XPF·YPF·ZPF의 인접 값 평균에 INT를 적용한 뒤 1을 더하여 II·JJ·KK를 계산한다. 이 루틴은 이들을 배열 첨자로 직접 사용한다. 이 루틴에는 범위 검사 분기가 없다. | vf_pmgst2.f:35–36, 50–51, 65–66 |

정정 16, 보완 56, 이상 없음 73
