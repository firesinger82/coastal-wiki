# EFDC snapshot 전환 — 고위험 20건 판정 후보

대상: `3ed76b6e` → `3b382fd0` (v12.5). 로컬 `phase1-candidates.json`의 ID 1–20만 검토했다. 이 문서는 Codex의 AI 분석이며 원문 인용·코드 증거와 구분한다. 최종 판정자는 Claude다.

## 판정 기준과 범위

`semantic_meaning_changed`는 해당 인용 지점의 주장 관련 실행 조건·입력 규약·릴리스 의미가 바뀌었는지를 나타낸다. `yes`라도 원문의 포괄적 설명이 여전히 참이면 `REVIEW_ONLY`다. `NO_ACTION`은 의미 불일치 관점의 판정으로, 줄번호가 그대로라는 뜻이 아니다. 명시적인 v12.4 과거 검증 표기는 그 자체로 오류로 보지 않고 새 snapshot에 적용할 때의 실질적 주장 불일치를 판단했다.

입력 JSON의 일부 wiki_claim은 잘려 있어 노트의 지정 줄 전체를 다시 읽어 CSV·본문에 원문 그대로 수록했다. 같은 노트·줄이 반복돼도 old 인용 범위가 다른 후보는 각각 유지했다. 주변 문장은 해석에만 사용했고 새 후보로 승격하지 않았다. ID 10은 교차 대상 input.f90의 위상 변환에 대한 전환 영향 판정이며 다른 파일의 전체 합성 경로를 재검증했다는 뜻이 아니다.

신규 `caltran_quickest.f90`·`mod_quickest.f90` 전문은 `new/`에 없었다. 로컬 `compare.json`과 파일별 patch가 동일하고 added hunk가 각각 503·115줄 전체를 포함함을 확인한 뒤 메모리에서 줄번호를 복원했다. 복원 파일은 쓰지 않았다.

## 결과

20건: UPDATE_REQUIRED 3 / REVIEW_ONLY 5 / NO_ACTION 12. `unclear` 및 판정 불가 건 0. confidence는 모두 high이며 최종 승인 여부를 뜻하지 않는다.

| ID | 분류 후보 | 의미 변경 | 한 줄 근거 |
|---|---|---|---|
| 1 | UPDATE_REQUIRED | yes | old calconc:193의 무조건 CALTRAN 호출은 new :198-204에서 ISQUICK==1이면 CALTRAN_QUICKEST, 그 외 CALTRAN으로 분기하므로 “CALTRAN transports every active constituent”는 새 snapshot 전체에 성립하지 않는다. |
| 2 | UPDATE_REQUIRED | yes | aaefdc:22 RELEASE가 EFDCPlus_12.4에서 EFDCPlus_12.5로, :30 DATE가 2025-12-29에서 2026-05-26으로 바뀌어 현행 snapshot을 12.4로 명시한 주장과 불일치한다. |
| 3 | NO_ACTION | no | C12A read는 old input:646과 new :669에서 동일한 9개 슬롯(첫 ISTOPT(0), 마지막 BC_EDGEFACTOR); hunk는 echo write를 이동하며 슬롯 주장을 바꾸지 않는다. |
| 4 | NO_ACTION | no | old input:913-915와 new :944-946의 RAD=PI2*PFPH/TCP 및 COS/SIN 변환은 동일; hunk의 dummy 식별자·echo 변경은 인용된 위상 단위 주장과 무관하다. |
| 5 | REVIEW_ONLY | yes | new calconc:228에 ISQUICK==0 조건이 추가되지만 :230의 anti-diffusion 호출명 CALTRAN_AD는 유지되므로 인용된 짧은 주장 자체의 불일치는 확정하지 않는다. |
| 6 | NO_ACTION | no | old input:387와 new :404의 C8 read 목록은 동일(TIDALP 3번째, CF 4번째); ISO 오류 분기 위치 변경은 이름·슬롯 주장을 바꾸지 않는다. |
| 7 | NO_ACTION | no | C12A의 ISTOPT(0) 첫 슬롯과 BC_EDGEFACTOR 9번째 슬롯은 old input:646 → new :669에 그대로 있고 echo 위치만 변경된다. |
| 8 | NO_ACTION | no | old input:3941-3944 → new :4090-4093의 shellfish 조건·READ_SHELLFISH_JSON 호출은 동일; C22B SEEK는 양쪽 input에 없고 교차 hunk는 앞선 body-force 정리 구문이다. (양쪽 input.f90 전체의 call SEEK(C22B) 검색 0건.) |
| 9 | NO_ACTION | no | old input:3942-3943와 new :4091-4092에서 ISFFARM>0 및 NSF>0의 JSON 호출이 동일하며 양쪽 input에 C22B SEEK가 없으므로 인용 주장은 유지된다. (양쪽 input.f90 전체의 call SEEK(C22B) 검색 0건.) |
| 10 | NO_ACTION | no | 교차 대상인 input의 CPFAM0/SPFAM0 위상 변환은 old :913-915와 new :944-946에서 동일; 이 hunk는 TIMESEC 합성 규약을 변경하는 근거가 아니다(다른 파일의 합성 경로 전체 재검증은 범위 밖). |
| 11 | UPDATE_REQUIRED | yes | old input:306의 C6 3번째 ldum이 new :311에서 scalar ISQUICK으로 읽히고 :316-325에서 broadcast·0/1 검사를 거치므로 “3번째 슬롯은 읽고 버린다”는 새 snapshot에 불일치한다. |
| 12 | NO_ACTION | no | C8 read는 old input:387 → new :404에서 그대로이며 TIDALP/CF의 슬롯 변경은 없다; ISO 오류 검사 이동은 해당 이름·파일 슬롯 호환 주장과 무관하다. |
| 13 | NO_ACTION | no | 교차 hunk 변경은 앞선 GOTM 난류 수송부에 있고 frazil 조건·CALTRANICE(old :296-307 → new :308-319), heat 조건·CALHEAT(old :467-473 → new :479-485)는 동일하다. |
| 14 | REVIEW_ONLY | yes | new calconc:198-204의 수송 분기 및 :228의 ISQUICK==0 제한은 변경됐지만 CALCONC의 transport coupling과 CALTRAN_AD 호출 자체(:230)는 유지되어 원문 목록 설명은 여전히 성립한다. |
| 15 | REVIEW_ONLY | no | old calconc:483의 propwash 조건이 new :495-503에서 퇴적물 비활성/시간 조건으로 나뉘지만 CALHEAT·CALDYE 및 SSEDTOX 결합은 존속하므로 “transport coupling” 주장은 유지된다. |
| 16 | REVIEW_ONLY | yes | new calconc:117이 upwind 사전지정에 ISQUICK==0 또는 shellfish/frazil 조건을 추가하지만 :118-133의 LUPU/LUPV 계산은 유지되므로 인용된 항목 자체를 곧바로 거짓으로 보지 않는다. |
| 17 | REVIEW_ONLY | yes | new calconc:198-204의 scheme 분기와 :228/:250의 보정 제한이 추가됐어도 WCV 수송과 SSEDTOX(:520/:533) 결합은 유지되므로 포괄적 coupling 목록 주장은 성립한다. |
| 18 | NO_ACTION | no | old input:547-548와 new :569-570의 C11 SEEK·read는 동일; ISO 오류 검사 위치 변경은 입력 카드 목록 주장과 무관하다. |
| 19 | NO_ACTION | no | C14 SEEK·11개 read 슬롯은 old input:736-737 → new :759-760에 동일; 교차 hunks는 echo 이동·추가여서 입력 카드 목록 주장을 바꾸지 않는다. |
| 20 | NO_ACTION | no | MTIDE>0의 C15 SEEK 및 SYMBOL/TCP read는 old input:852-866 → new :884-895에서 유지; write echo의 broadcast 뒤 이동은 카드 목록 주장과 무관하다. |

## UPDATE_REQUIRED 근거 상세

### ID 1 — `models/EFDC/source-analysis/sediment/efdc_sediment.md:205`

**판정 후보:** UPDATE_REQUIRED / semantic_meaning_changed=yes / confidence=high

**위키 원문 인용**

CALTRAN transports every active constituent through `WCV` (`Transport/calconc.f90:188-193`); anti-diffusion at `:213-219`.

**old 소스 증거**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Transport/calconc.f90:188-193
188:   ! *** 3D ADVECTI0N-DIFFUSION TRANSPORT FOR ALL WATER COLUMN CONSITUENTS (SEE VARINIT FOR WCV INITIALIZATION)
189:   !$OMP PARALLEL DEFAULT(SHARED)
190:   !$OMP DO PRIVATE(IW,IT,L) SCHEDULE(STATIC,1)
191:   do IW = 1,NACTIVEWC
192:     !$  IT = OMP_GET_THREAD_NUM() + 1
193:     call CALTRAN( IACTIVEWC1(IW), IACTIVEWC2(IW), WCV(IW).VAL0, WCV(IW).VAL1, IW, IT, WCV(IW).WCLIMIT, ISKIP(IW) )

models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Transport/calconc.f90:213-219
213:   ! *** APPLY ANTI-DIFFUSION AND FLUX CORRECTOR
214:   !$OMP DO PRIVATE(IW,IT) SCHEDULE(STATIC,1)
215:   do IW = 1,NACTIVEWC
216:     if( ISKIP(IW) == 0 )then
217:       !$  IT = OMP_GET_THREAD_NUM() + 1
218:       call CALTRAN_AD( IACTIVEWC1(IW), IACTIVEWC2(IW), WCV(IW).VAL0, WCV(IW).VAL1, IW, IT )
219:     endif
```

**new 소스 증거**

```fortran
_staging/efdc-prescan/new/EFDC__Transport__calconc.f90:191-204
191:   ! *** 3D ADVECTI0N-DIFFUSION TRANSPORT FOR ALL WATER COLUMN CONSITUENTS (SEE VARINIT FOR WCV INITIALIZATION)
192:   !$OMP PARALLEL DEFAULT(SHARED)
193:   !$OMP DO PRIVATE(IW,IT,L) SCHEDULE(STATIC,1)
194:   do IW = 1,NACTIVEWC
195:     !$  IT = OMP_GET_THREAD_NUM() + 1
196: 
197:     ! *** Dispatch to appropriate transport scheme
198:     if( ISQUICK == 1 )then
199:       ! *** QUICKEST scheme with ULTIMATE limiter
200:       call CALTRAN_QUICKEST( IACTIVEWC1(IW), IACTIVEWC2(IW), WCV(IW).VAL0, WCV(IW).VAL1, IW, IT, WCV(IW).WCLIMIT, ISKIP(IW) )
201:     else
202:       ! *** Original upwind scheme
203:       call CALTRAN( IACTIVEWC1(IW), IACTIVEWC2(IW), WCV(IW).VAL0, WCV(IW).VAL1, IW, IT, WCV(IW).WCLIMIT, ISKIP(IW) )
204:     endif

_staging/efdc-prescan/new/EFDC__Transport__calconc.f90:224-231
224:   ! *** APPLY ANTI-DIFFUSION AND FLUX CORRECTOR
225:   ! *** Skip for QUICKEST scheme (limiter is built-in)
226:   !$OMP DO PRIVATE(IW,IT) SCHEDULE(STATIC,1)
227:   do IW = 1,NACTIVEWC
228:     if( ISKIP(IW) == 0 .AND. ISQUICK == 0 )then
229:       !$  IT = OMP_GET_THREAD_NUM() + 1
230:       call CALTRAN_AD( IACTIVEWC1(IW), IACTIVEWC2(IW), WCV(IW).VAL0, WCV(IW).VAL1, IW, IT )
231:     endif

new EFDC/Transport/caltran_quickest.f90:14-18 (출처 _staging/efdc-prescan/patches/EFDC__Transport__caltran_quickest.f90.patch, @@ -0,0 +1,503 @@의 +행을 메모리에서 복원; new/ 실파일 없음)
14:   SUBROUTINE CALTRAN_QUICKEST (MVAR, MO, CON, CON1, IW, IT, WCCUTOFF, ISKIP)
15: 
16:   ! *** Subroutine CALTRAN_QUICKEST calculates the advective transport of dissolved 
17:   ! *** or suspended constituent M leading to a new value at time level (n+1) 
18:   ! *** using the QUICKEST scheme

new EFDC/Transport/caltran_quickest.f90:32-33 (출처 _staging/efdc-prescan/patches/EFDC__Transport__caltran_quickest.f90.patch, @@ -0,0 +1,503 @@의 +행을 메모리에서 복원; new/ 실파일 없음)
32:   use GLOBAL
33:   use MOD_QUICKEST

new EFDC/Transport/caltran_quickest.f90:167-185 (출처 _staging/efdc-prescan/patches/EFDC__Transport__caltran_quickest.f90.patch, @@ -0,0 +1,503 @@의 +행을 메모리에서 복원; new/ 실파일 없음)
167:       if( UHDY2(L,K) >= 0.0 )then
168:         ! *** Positive U flow (eastward)
169:         Lu = LWC(LWC(L))   ! 2 cells upstream (west)
170: 
171:         ! *** Check if we have enough wet cells for QUICKEST stencil
172:         ! *** SUB(LWC(L)) is the face between the upstream (Lu) and center (LWC(L)) cells
173:         if( SUB(LWC(L)) > 0.5 )then
174:           ! *** Use QUICKEST scheme
175:           CONC_U = CON1(Lu,K)        ! Upstream
176:           CONC_C = CON1(LWC(L),K)    ! Center
177:           CONC_D = CON1(L,K)         ! Downstream
178: 
179:           ! *** QUICKEST face concentration
180:           face_conc = QUICKEST_FACE(CONC_U, CONC_C, CONC_D, CFL_U)
181:           FUHUD(L,K,IW) = UHDY2(L,K) * face_conc
182:         else
183:           ! *** Near boundary or dry cell - use upwind
184:           FUHUD(L,K,IW) = UHDY2(L,K) * CON1(LWC(L),K)
185:         endif

new EFDC/Transport/mod_quickest.f90:40-47 (출처 _staging/efdc-prescan/patches/EFDC__Transport__mod_quickest.f90.patch, @@ -0,0 +1,115 @@의 +행을 메모리에서 복원; new/ 실파일 없음)
40:   REAL(RKD) FUNCTION QUICKEST_FACE(Cu, Cc, Cd, cfl)
41:     IMPLICIT NONE
42: 
43:     ! Arguments
44:     REAL(RKD), INTENT(IN) :: Cu    ! Upstream concentration
45:     REAL(RKD), INTENT(IN) :: Cc    ! Center concentration
46:     REAL(RKD), INTENT(IN) :: Cd    ! Downstream concentration
47:     REAL(RKD), INTENT(IN) :: cfl   ! Courant number (positive)

new EFDC/Transport/mod_quickest.f90:80-101 (출처 _staging/efdc-prescan/patches/EFDC__Transport__mod_quickest.f90.patch, @@ -0,0 +1,115 @@의 +행을 메모리에서 복원; new/ 실파일 없음)
80:     ! *** Compute ULTIMATE QUICKEST limiter (P2_PDM from GOTM)
81:     !     This is Leonard's (1991) ULTIMATE limiter applied to QUICKEST
82: 
83:     ! QUICKEST polynomial correction parameter
84:     x = (1.0_RKD - 2.0_RKD*cfl_safe) / 6.0_RKD
85: 
86:     ! Third-order QUICKEST limiter
87:     limiter = (0.5_RKD + x) + (0.5_RKD - x) * ratio
88: 
89:     ! Apply ULTIMATE monotonicity constraints
90:     ! Limiter must satisfy all three conditions to ensure TVD property:
91:     !   1. limiter <= 2*ratio/cfl        (prevents undershoot on upstream side)
92:     !   2. limiter <= 2/(1-cfl)          (prevents overshoot on downstream side)
93:     !   3. limiter as computed by QUICKEST formula
94:     limiter = MIN(2.0_RKD * ratio / (cfl_safe + EPSILON), limiter)
95:     limiter = MIN(limiter, 2.0_RKD / (1.0_RKD - cfl_safe))
96: 
97:     ! Ensure limiter is non-negative (positivity preserving)
98:     limiter = MAX(limiter, 0.0_RKD)
99: 
100:     ! *** Compute face concentration using limited QUICKEST scheme
101:     QUICKEST_FACE = Cc + 0.5_RKD * limiter * (1.0_RKD - cfl_safe) * deltaf
```

**교차 changed hunk**

출처: `_staging/efdc-prescan/patches/EFDC__Transport__calconc.f90.patch`

```diff
@@ -190,7 +193,15 @@ SUBROUTINE CALCONC
   !$OMP DO PRIVATE(IW,IT,L) SCHEDULE(STATIC,1)
   do IW = 1,NACTIVEWC
     !$  IT = OMP_GET_THREAD_NUM() + 1
-    call CALTRAN( IACTIVEWC1(IW), IACTIVEWC2(IW), WCV(IW).VAL0, WCV(IW).VAL1, IW, IT, WCV(IW).WCLIMIT, ISKIP(IW) )
+
+    ! *** Dispatch to appropriate transport scheme
+    if( ISQUICK == 1 )then
+      ! *** QUICKEST scheme with ULTIMATE limiter
+      call CALTRAN_QUICKEST( IACTIVEWC1(IW), IACTIVEWC2(IW), WCV(IW).VAL0, WCV(IW).VAL1, IW, IT, WCV(IW).WCLIMIT, ISKIP(IW) )
+    else
+      ! *** Original upwind scheme
+      call CALTRAN( IACTIVEWC1(IW), IACTIVEWC2(IW), WCV(IW).VAL0, WCV(IW).VAL1, IW, IT, WCV(IW).WCLIMIT, ISKIP(IW) )
+    endif
     
     if( ISICE > 2 .and. IACTIVEWC1(IW) == 8 .and. IACTIVEWC2(IW) == MSVDOX .and. ISKIP(IW) == 0 )then
       ! *** ZERO SURFACE MELT FLUX
```

**판정 근거:** old calconc:193의 무조건 CALTRAN 호출은 new :198-204에서 ISQUICK==1이면 CALTRAN_QUICKEST, 그 외 CALTRAN으로 분기하므로 “CALTRAN transports every active constituent”는 새 snapshot 전체에 성립하지 않는다.

**로직 분리 확인:** 새 `calconc.f90:198-204`는 기존 CALTRAN 호출을 else 경로로 보존하고 QUICKEST 경로를 추가한다. 신규 `caltran_quickest.f90:180-181`은 `QUICKEST_FACE`로 면 농도를 구해 flux를 계산하고, 신규 `mod_quickest.f90:80-101`에 limiter 계산이 있다. 따라서 CALCONC driver 전체가 신규 파일로 이동한 것은 아니며, 별도 scheme 및 그 보조 함수가 추가·분리된 구조다. 기존 WCV 결합은 유지되지만 모든 성분이 CALTRAN만 통과한다는 단정은 성립하지 않는다.

### ID 2 — `models/EFDC/manifest.md:17`

**판정 후보:** UPDATE_REQUIRED / semantic_meaning_changed=yes / confidence=high

**위키 원문 인용**

- **EFDCPlus_Stable = `EFDCPlus_12.4`** (릴리스 헤더 `EFDC/aaefdc.f90:22` "RELEASE: EFDCPlus_12.4", DATE 2025-12-29; 솔루션 파일명 `EFDCPlus_MPI_12.sln` 정합). clone HEAD sha **`3ed76b6eb1263921ba99bf23b66bb85c1a5feac1`** (2026-04-02 "update readme"). 12.4 릴리스 피처(헤더 verbatim): MPI Domain Decomposition · Propeller Wash · 신 WQ kinetics(사용자 정의 algal groups+zooplankton) · 3TL 동적 timestep · GOTM · **SIGMA-Zed(SGZ)**. → **위키 EFDC source-analysis 전체 = EFDC+ 12.4 기준.**

**old 소스 증거**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/aaefdc.f90:22-30
22: !  RELEASE:         EFDCPlus_12.4
23: !                   Domain Decomposition with MPI
24: !                   Propeller Wash 
25: !                   New WQ kinetics with user defined algal groups and zooplankton
26: !                   Dynamic time stepping adjustment for 3TL solution
27: !                   General Ocean Turbulence Model (GOTM)
28: !                   SIGMA-Zed (SGZ) Vertical Layering
29: !
30: !  DATE:            2025-12-29
```

**new 소스 증거**

```fortran
_staging/efdc-prescan/new/EFDC__aaefdc.f90:22-30
22: !  RELEASE:         EFDCPlus_12.5
23: !                   Domain Decomposition with MPI
24: !                   Propeller Wash 
25: !                   New WQ kinetics with user defined algal groups and zooplankton
26: !                   Dynamic time stepping adjustment for 3TL solution
27: !                   General Ocean Turbulence Model (GOTM)
28: !                   SIGMA-Zed (SGZ) Vertical Layering
29: !
30: !  DATE:            2026-05-26
```

**교차 changed hunk**

출처: `_staging/efdc-prescan/patches/EFDC__aaefdc.f90.patch`

```diff
@@ -19,15 +19,15 @@
 ! along with this program.  If not, see <http://www.gnu.org/licenses/>.
 !----------------------------------------------------------------------!
 !
-!  RELEASE:         EFDCPlus_12.4
+!  RELEASE:         EFDCPlus_12.5
 !                   Domain Decomposition with MPI
 !                   Propeller Wash 
 !                   New WQ kinetics with user defined algal groups and zooplankton
 !                   Dynamic time stepping adjustment for 3TL solution
 !                   General Ocean Turbulence Model (GOTM)
 !                   SIGMA-Zed (SGZ) Vertical Layering
 !
-!  DATE:            2025-12-29
+!  DATE:            2026-05-26
 !  BY:              DSI, LLC
 !                   EDMONDS, WASHINGTON  98020
 !                   USA
```

**판정 근거:** aaefdc:22 RELEASE가 EFDCPlus_12.4에서 EFDCPlus_12.5로, :30 DATE가 2025-12-29에서 2026-05-26으로 바뀌어 현행 snapshot을 12.4로 명시한 주장과 불일치한다.

**버전 표기 해석:** 원문의 clone SHA·12.4 설명은 old snapshot의 역사 기록으로는 유효하지만 새 snapshot의 현행 manifest 설명으로는 RELEASE·DATE가 맞지 않는다. 새 SHA 자체를 소스 헤더가 증명한다고 보지 않으며, 여기서는 제공된 전환 대상과 로컬 헤더 차이를 근거로 한다.

### ID 11 — `models/EFDC/manual-notes/efdc-implementation-guide.md:193`

**판정 후보:** UPDATE_REQUIRED / semantic_meaning_changed=yes / confidence=high

**위키 원문 인용**

> ⚠️ **v12.4 소스 드리프트 (검증 2026-07)**: v12.4의 C6 read는 `ISTRAN(NS), ISTOPT(NS), ldum, ISADAC(NS), ISFCT(NS), ldum, ldum, ldum, ISCI(NS), ISCO(NS)` (`input.f90:306`) — **3·6·7·8번째 슬롯은 더미(`ldum`)로 읽고 버린다**. 즉 매뉴얼이 3번째 슬롯에 문서화한 `ISCDCA` 등은 v12.4에서 **무시**된다 (자리는 유지해야 파싱이 맞음).

**old 소스 증거**

```fortran
models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:300-312
300:   NCARD = '6'
301: 
302:   ! *** ********************************************************
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
```

**new 소스 증거**

```fortran
_staging/efdc-prescan/new/EFDC__input.f90:304-325
304:   !C6**  DISSOLVED AND SUSPENDED CONSTITUENT TRANSPORT SWITCHES
305:   NCARD = '6'
306: 
307:   ! *** ********************************************************
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
```

**교차 changed hunk**

출처: `_staging/efdc-prescan/patches/EFDC__input.f90.patch`

```diff
@@ -303,12 +308,21 @@ SUBROUTINE INPUT()
   if( process_id == master_id )then
     call SEEK('C6',0)
     do NS = 0,8
-      read(1,*,IOSTAT = ISO) ISTRAN(NS), ISTOPT(NS), ldum, ISADAC(NS), ISFCT(NS), ldum, ldum, ldum, ISCI(NS), ISCO(NS)
-      write(mpi_efdc_out_unit,1002) NCARD
-      write(mpi_efdc_out_unit,*) ISTRAN(NS), ISTOPT(NS), ldum, ISADAC(NS), ISFCT(NS), ldum, ldum, ldum, ISCI(NS), ISCO(NS)
+      read(1,*,IOSTAT = ISO) ISTRAN(NS), ISTOPT(NS), ISQUICK, ISADAC(NS), ISFCT(NS), ldum, ldum, ldum, ISCI(NS), ISCO(NS)
       if( ISO > 0 ) GOTO 100
     enddo
   endif
+  
+  call Broadcast_Scalar(ISQUICK, master_id)   ! *** Using a scalar var for ISQUICK in EFDC+ 12.x - DKT
+
+  ! *** Sanitize ISQUICK: this C6 column was unused prior to EFDC+ 12.x and legacy decks may contain other values
+  if( ISQUICK /= 0 .and. ISQUICK /= 1 )then
+    if( process_id == master_id )then
+      PRINT *,'*** WARNING: INVALID ISQUICK ON CARD C6.  RESETTING TO 0 (UPWIND SCHEME)'
+      write(mpi_efdc_out_unit,*) '*** WARNING: INVALID ISQUICK ON CARD C6.  RESETTING TO 0 (UPWIND SCHEME):', ISQUICK
+    endif
+    ISQUICK = 0
+  endif
 
   call Broadcast_Array(ISTRAN, master_id)
   call Broadcast_Array(ISTOPT, master_id)
```

**판정 근거:** old input:306의 C6 3번째 ldum이 new :311에서 scalar ISQUICK으로 읽히고 :316-325에서 broadcast·0/1 검사를 거치므로 “3번째 슬롯은 읽고 버린다”는 새 snapshot에 불일치한다.

**슬롯 의미:** 6·7·8번째 슬롯은 여전히 ldum이다. 바뀐 것은 3번째 슬롯이며 이름은 ISCDCA의 복원이 아니라 ISQUICK이다. `NS=0,8` 반복에서 배열 원소가 아닌 같은 scalar를 읽고, 반복 뒤 broadcast·유효값 검사(0/1 이외 값은 0)를 수행한다. 이는 단순 변수명 변경이 아니라 종전에 버리던 입력값이 수송 scheme 선택에 사용되는 변경이다.

## REVIEW_ONLY 해석

- ID 5: anti-diffusion의 CALTRAN_AD라는 이름은 유효하지만 호출에 ISQUICK==0 제한이 추가됐다. 주변의 별도 문장을 새 불일치 후보로 추가하지 않았다.
- ID 14·17: transport coupling이라는 목록 설명은 여전히 맞으며, 그 내부 scheme 분기·보정 조건의 변경을 기록했다.
- ID 15: propwash 조건문이 다시 구성됐으나 인용 문장은 일반적인 결합 위치만 설명한다. 임의의 비정상 flag 값까지 조건식의 완전 동치성을 주장하지 않는다.
- ID 16: 노트의 일반 CALCONC dispatch 문맥에서는 적용 조건 검토가 필요하지만, 해당 후보의 원문은 upwind 사전지정의 존재·계산을 가리킨다. 그 계산이 삭제된 것은 아니므로 무조건 수행된다는 별도 단정을 후보 원문에 덧붙여 UPDATE_REQUIRED로 판정하지 않았다.

## 검증·작업 경계

- 20건 모두 필수 11필드를 채웠다. old_excerpt 전부를 old 실파일과 대조했고, 대상 3개 변경 파일은 old + patch를 메모리에서 적용한 결과가 new 전문과 일치했다.
- 추가 후보 발굴·수정 제안·빌드·런타임 검증은 수행하지 않았다. 네트워크와 git 명령은 사용하지 않았다.
- 쓰기는 지정된 `phase1-codex-review.csv`·`phase1-codex-review.md`에만 수행했다. `models/`에 쓰기·잠금 변경을 하지 않았다. 검토 대상 old 소스 3개·노트 8개(총 11파일)의 작업 전후 SHA-256이 모두 동일했다. CSV 20행·11필드·ID 집합·원문 인용·old/new 코드 줄번호·hunk 헤더 및 Markdown 상세 3건의 일치 검사를 통과했다.
