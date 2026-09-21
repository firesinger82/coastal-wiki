# Delft3D Phase 2 의미 검토

입력 41건(11개 노트)을 고정 커밋 513eccd → 231bbf2로 대조했다. 위키 수정 제안 없이 행별 판정과 소스 근거를 반환한다. models/·노트·snapshot·권한은 변경하지 않았다.

| 배치 | UPDATE_REQUIRED | REVIEW_ONLY | NO_ACTION | UNRESOLVED | 합계 |
|---|---:|---:|---:|---:|---:|
| B | 4 | 11 | 4 | 0 | 19 |
| C | 0 | 13 | 1 | 0 | 14 |
| D | 1 | 2 | 2 | 1 | 6 |
| Z | 0 | 2 | 0 | 0 | 2 |
| 전체 | 5 | 28 | 7 | 1 | 41 |


**배치별 핵심 결과**

- **B (19)**: D2-2는 Stokes RHS에 식생 frL이 포함되도록 순서가 바뀌었다. D2-11은 offline의 clip/변환 순서와 필요 입력별 분기, D2-13은 유한 force limit의 적용 조건, D2-14는 표면력·체적력 합산/제한 순서가 달라졌다. 3D 최상층 표면력과 균일 체적력 배치는 유지된다. Hsig/√2 변환 계수 자체(D2-12)는 유지된다.
- **C (14)**: DAD wrapper/call-site, cohesive→erosilt 및 sand→eqtran 라우팅, fraction별 bed 누적, Van Rijn dispatch와 보정 곱 주장은 유지된다. hdtmor=0, morft/bed-property 인자 추가, getfrac guard 제거, mud 교정값의 bed-property 곱은 실제 소스 변화로 기록했다. 이 행들이 주장한 역할·목록·출력 변수 관계를 곧바로 부정하지 않으므로 REVIEW_ONLY로 반환한다.
- **D (6)**: D2-38의 생성 명령은 BOUN WWIII → BOUN WW3로 변경됐다. WAQ 시간루프 골격은 유지되며 volume-update 호출의 num_cells 인자가 제거됐다. swan_tot의 교차 변화는 콘솔 시각 표시 폭이다. D2-34의 모든 writer에 대한 보장은 미해결이다.
- **Z (2)**: heat dispatch는 주변 활성 heatu 호출로 확인했다. iform=-3은 여전히 Partheniades-Krone이며 기본값도 rdtrafrm의 실행 대입으로 확인했다. -5 추가와 계수 변화를 -3 매핑 소멸로 해석하지 않았다.

**판정 경계**

판정 단위는 입력 행의 ref가 뒷받침하는 주장이다. broad 인용은 해당 문장과 직접 이어지는 표·식·설명을 함께 읽었다. 같은 줄의 다른 ref와 인접 코드 변경을 자동 전파하지 않았다. semantic_meaning_changed는 true/false/unknown이다. false는 해당 주장이 유지된다는 뜻이며 파일 전체의 동작 동등성을 보장하지 않는다.

REVIEW_ONLY는 실행 근거 재지정·인용 표현 검토·주장에 명시되지 않은 인접 변화가 있는 경우다. NO_ACTION은 해당 주장에 의미 조치가 불필요하다는 뜻으로 옛 좌표의 유효성을 보장하지 않는다. HIGH는 직접 소스로 판정 근거가 확인된 경우, MEDIUM은 일부 근거만 확인되고 전역 단언이 남는 경우다.

- D2-3: furu_structures는 구판의 kmx==0 내부에서 신판의 2D/3D·경계 처리 뒤로 이동했다. 조건·순서는 바뀌지만 노트의 두 구조물 루틴 호출이라는 문장은 유지된다.
- D2-11/D2-12: 구판 compute_wave_parameters:105의 clip 뒤 :111-116 변환이 hwav를 다시 출력하며, 신판은 helper :181-188에서 변환 후 clip한다. Hsig/√2 변환 계수는 동일해 clip 순서와 변환 계수를 별도로 판정했다.
- D2-15: 가속도 변환 계수 min(huvli,hminlwi)/rhomean은 유지된다. 새 local 변수, 합성 force 제한 및 말미 fforc 배율은 근거에 기록했다. 이 ref의 단위 변환과 전체 force 산출의 동등성을 혼동하지 않았다.
- D2-24: hdtmor=hdt*morfac → 0, morft=-999 인자 추가는 실제 변화다. 노트는 updmorlyr의 앞 세 인자와 dumping administration 역할만 주장하고 나머지를 ...로 생략했으므로 그 역할에 대한 REVIEW_ONLY다.
- D2-30: getfrac의 lsedtot>1 guard 제거는 실제 호출 범위 확대다. 노트에 이 guard가 명시돼 있지 않고 fraction 취득 역할이 유지되어 REVIEW_ONLY다.
- D2-32: tcrero/eropar에 bed-property 곱이 추가됐다. 노트의 교정 대상 네 변수 목록은 유지되며 par 직접 매핑을 주장하지 않는다. 따라서 이 행의 REVIEW_ONLY를 교정값 불변으로 해석하면 안 된다.
- D2-22: main/bott3d.f90라는 노트 경로는 신구 모두 실제 compute_sediment/bott3d.f90와 다르다. 기존 경로 불일치도 기록했다.

**UNRESOLVED 목록**

| ID | 노트 | 확인한 사실 | 남은 불확실성 |
|---|---|---|---|
| D2-34 | delft3d_flow2d3d_io.md:207 | wrh_main:327-328 파일 종류, :363-372 DEFINE/WRITE, :380-405 두 백엔드와 CF-1.6; wrtarray:132-152 putelt/nf90_put_var | 이 인용들로 모든 writer의 공통 2-pass/두 백엔드 지원을 입증할 수 없음. 전수 writer 조사로 확대하지 않고 반환. |

이 미해결은 새 커밋에서 출력 포맷이 바뀌었다는 판정이 아니다. 해당 교차 hunk는 wrihis의 namsed 인자 제거이며 확인한 출력 분기는 유지된다.

CSV의 wiki_claim은 원문 전체 줄이다. 입력에서 잘린 D2-6, D2-10, D2-14, D2-15, D2-39를 복원했고 D2-36의 원래 들여쓰기도 보존했다.

**UPDATE_REQUIRED 근거**

| ID | reason_type | 판정 근거 |
|---|---|---|
| D2-2 | BEHAVIOR_CHANGE | du 보정이 식생 frL 가산 전에서 후로 이동했다. (jaBaptist>=2 또는 trachy_resistance)일 때 새 du에는 alfav*hypot(Eulerian velocity)*ustokes까지 들어가므로 동일 문자열의 이동만으로 볼 수 없는 RHS 값 변경이다. |
| D2-11 | BEHAVIOR_CHANGE | offline 처리가 입력 요구량별 helper 분기로 바뀌었다. 완전 H/T/방향 입력 경로에서 구판은 gammax clip 뒤 transform_wave_physics_hp가 hwav를 다시 썼지만, 신판은 변환 뒤 clip한다. H가 불필요한 경로와 결측·건조 셀은 0 처리된다. 따라서 compute_wave_parameters에서 항상 같은 clip을 적용한다는 포괄 설명은 조건·적용 순서를 재검토해야 한다. |
| D2-13 | BEHAVIOR_CHANGE | fmax 식은 get_maximum_wave_force로 이동했으며 조건부가 됐다. offline radiation-stress 입력이고 period가 불필요하면 limit_wave_forces=false로 maximum_force=huge(1.0_dp)를 반환한다. 기존 유한 한계식을 항상 적용한다는 의미는 유지되지 않는다. |
| D2-14 | BEHAVIOR_CHANGE | 구판은 표면력과 체적력의 norm을 각각 제한한 다음 더했다. 신판은 먼저 합산한 벡터를 투영하고 그 합성 norm을 한 번 제한한다. 벡터 제한이라는 원리는 유지되나 노트에 기술된 제한 후 합산 순서와 결과값은 달라진다. |
| D2-38 | INTERFACE_CHANGE | bndtyp==5의 실제 출력 명령 문자열이 BOUN WWIII에서 BOUN WW3로 바뀌었다. FREE OPEN은 유지되며 BOUN NEST와 BOUN SHAPE도 남아 있다. 노트 표가 인용한 명령 토큰이 달라진 명시적 인터페이스 변경이다. |

**재앵커 19건**

모두 주석이 아닌 대응 실행문을 확인했다. 아래 파일명은 축약이며 CSV에 커밋과 저장소 상대 전체 경로가 있다. exact_evidence는 이유와 신구 원문을 담은 JSON이다. 새 좌표는 일괄 치환안이 아니라 검토 근거다.

| ID | 파일 | 원 범위 | 새 실행 근거 | 판정 |
|---|---|---|---|---|
| D2-2 | furu.f90 | 170-181 | 171-187 | UPDATE_REQUIRED |
| D2-3 | furu.f90 | 269-269 | 90-90;267-282;364-369 | REVIEW_ONLY |
| D2-6 | ini_transport.f90 | 160-160 | 152-158 | NO_ACTION |
| D2-8 | m_fm_bott3d.f90 | 1146-1146 | 1177-1177;1198-1200 | NO_ACTION |
| D2-11 | compute_wave_parameters.f90 | 105-105 | 99-112;163-232 | UPDATE_REQUIRED |
| D2-12 | compute_wave_parameters.f90 | 101-101 | 175-188;198-222 | REVIEW_ONLY |
| D2-13 | setwavfu.f90 | 108-108 | 87-89;118-119;157-159;214-223 | UPDATE_REQUIRED |
| D2-14 | setwavfu.f90 | 99-127 | 94-134 | UPDATE_REQUIRED |
| D2-15 | setwavfu.f90 | 130-131 | 125-134;207-208 | REVIEW_ONLY |
| D2-16 | setwavfu.f90 | 159-159 | 161-196 | REVIEW_ONLY |
| D2-18 | wave_comp_stokes_velocities.f90 | 81-81 | 80-86 | NO_ACTION |
| D2-19 | setwavfu.f90 | 159-159 | 192-204 | REVIEW_ONLY |
| D2-25 | trisol.f90 | 1968-3279 | 1974-1982;2166-2169;2206-2212;3047-3055;3280-3286 | REVIEW_ONLY |
| D2-28 | eqtran.f90 | 304-420 | 326-364;395-404;442-447 | REVIEW_ONLY |
| D2-30 | erosed.f90 | 629-635 | 652-658 | REVIEW_ONLY |
| D2-32 | erosilt.f90 | 160-203 | 170-198;209-217 | REVIEW_ONLY |
| D2-33 | eqtran.f90 | 722-743 | 749-770 | NO_ACTION |
| D2-38 | swan_input.f90 | 3223-3223;3233-3233;3248-3248 | 3453-3477 | UPDATE_REQUIRED |
| D2-41 | erosilt.f90 | 160-160 | 170-198 | REVIEW_ONLY |

- D2-3: call furu_structures()는 :368에 살아 있다. 호출 조건·순서까지 읽었다.
- D2-16/D2-19: 옛 주석 블록의 wavfu 텍스트에 정박하지 않았다. 신판 :195-196이 최상층 실행 대입이고 :199-204가 균일 body-force 실행 루프다. as in D3D라는 옛 설명 문구는 삭제되어 인용 표현 검토가 필요하다.
- D2-28: 새 eqtran:400-404의 tranb3는 주석이다. 해당 후보의 Van Rijn 표는 활성 :330, :355, :446 호출로 확인했다. 주석화된 Ackers-White를 실행 근거로 쓰거나 후보를 추가하지 않았다.
- D2-41: erosilt의 Default 주석은 없어졌지만 rdtrafrm:342의 미지정 cohesive iform=-3 대입이 살아 있다. 주석 삭제만으로 기본값 변경을 주장하지 않았다.
- D2-40은 입력상 REANCHOR가 아니지만 원 끝줄 :1604가 주석이다. 주변 같은 heat signature의 활성 call heatu(:1610-1617)로 근거를 보완했다.

**Broad 인용 15건**

span>60 전체 행에서 범위 내 신구 차이를 확인했다. 제공 hunk는 일부만 발췌돼 있어 대소문자·공백·주석을 제외한 비교도 보조로 사용했고 최종 판단은 원문과 분기·호출 문맥으로 했다.

| ID | span | 주장과 변화의 경계 |
|---|---:|---|
| D2-1 | 126 | 2D 운동량 루프·계수 유지; 구체 Stokes 변화는 D2-2. |
| D2-5 | 243 | qin/dd 및 mba 누적 유지; 비활성 lateral 층의 재배정 변경. |
| D2-7 | 97 | 확산식·조건 유지; 파티션별 경고 카운터 조건. |
| D2-20 | 1516 | DAD 모듈 역할 유지; implicit none/use 정리. |
| D2-21 | 137 | FLOW wrapper 유지; 내부 dt=0/morft 변화는 별도 기록. |
| D2-22 | 511 | dredge_d3d4 활성 call 유지; fluff_burial/updmorlyr 인자 변화. |
| D2-23 | 62 | dbodsd→updmorlyr→depchg 유지; dunelength 및 morft 변화. |
| D2-25 | 1312 | 두 erosed/bott3d call sequence 확인; 인자와 역할 분리. |
| D2-27 | 110 | sand의 eqtran 경로 유지; D50 검사 표현 변경. |
| D2-28 | 117 | -1/-2/-4/7 활성 dispatch 확인; 비대상 iform=3 주석 제외. |
| D2-31 | 117 | lsedtot별 dbodsd 누적 유지; fluff flux 저장 추가. |
| D2-34 | 206 | history writer/generic 출력 확인; 모든 writer 보장은 미해결. |
| D2-35 | 197 | ACTION/시간루프/호출 순서 유지; volume-update 인자 제거. |
| D2-36 | 197 | 예시 process/transport/explicit update 연결 유지. |
| D2-40 | 446 | inctem/heatu dispatch 확인; dens 인자 변화와 분리. |

**노트의 파일 수·줄 수 대조**

사용자 지시에 따라 같은 11개 노트의 파일 수·파일 길이 표기도 확인했다. 아래는 수치 대조 부록으로 후보 행을 추가하거나 다른 ref에 판정을 전파하지 않았다. Z의 REVIEW_ONLY가 노트의 낡은 줄 수까지 유지된다는 뜻은 아니다.

| 노트의 수치 표기 | 513eccd | 231bbf2 | 수치 판정 |
|---|---:|---:|---|
| dflowfm_waves.md:24 compute_waves 루트 25개 | 24 | 24 | 신구 모두 24개: 기존 불일치, snapshot 변경 아님 |
| 같은 줄 surfbeat 13파일·약 16k줄 | 13 / 16,040 | 13 / 16,057 | 13파일과 약 16k 근사 유지 |
| sediment_transport_formulae.md:7·22 erosilt.f90 269줄 | 269 | 290 | 파일 길이 수치 변경 확인 |
| sediment_transport_formulae.md:7·81 eqtran.f90 834줄 | 834 | 863 | 파일 길이 수치 변경 확인 |
| sediment_transport_formulae.md:7·111 compbsskin.f90 312줄 | 312 | 317 | 파일 길이 수치 변경 확인 |

줄 수는 마지막 개행이 없는 행도 포함한 물리적 행 수(bytes.splitlines)다. 신판 erosilt/eqtran은 마지막 개행이 없어 wc -l이면 289/862이지만 마지막 소스 행은 290/863이다. compbsskin은 317이다. 파동 루트는 git ls-tree의 compute_waves 직속 파일만 세었으며 surfbeat 디렉터리를 파일에 합산하지 않았다. surfbeat 본문은 기능 조사 없이 수·길이만 집계했다.

**검증·범위 기록**

- 구 snapshot: 513eccdbe249919b3e5e62063dc91eb9fdf2347f
- 신 snapshot: 231bbf266cbb2d6de83a0b63ec8fdbf151a72382
- 입력 CSV SHA-256: 50738ae5703c7bcb7b5561068b8cdbd3bcf5fdda7dbf5c679e5ff1e3ee851cb2

- 입력 41행의 ID·순서·batch·note·note_line, 필수 12열, 분류와 true/false/unknown 정합성, UPDATE_REQUIRED reason_type을 검사했다. 재앵커 19행과 broad 15행을 모두 포함한다.
- 제공 hunk의 신구 발췌 134개를 커밋 원문과 대조했다. 주 소스 21파일과 직접 근거 보조 4파일의 신구 총 50개 blob이 각 snapshot 파일과 바이트 단위로 일치했다. 보조 파일은 network_data(값 3), transform_wave_physics(Hrms 변환), rdtrafrm(default -3), wrtarray(출력 분기)다.
- CSV의 근거 186범위·2,785줄을 커밋에서 직접 추출했고 파일 경계와 재읽기 원문 일치를 검사했다.
- 정적 의미 검토이며 모델 빌드·수치 실행 검증은 수행하지 않았다. 위키 문장 수정안·좌표 일괄 치환·추가 후보를 만들지 않았다. 41건 판정 또는 UNRESOLVED 반환으로 계약 종료 조건을 충족했다.

검토 노트 SHA-256:

- models/Delft3D/source-analysis/delft3d_dflowfm_compute_core.md: f4f5ea32612aabcdb2dca2de2fc633b9a9db7c1ea001c7b4ee33d21952137deb
- models/Delft3D/source-analysis/delft3d_dflowfm_kernel_scheme.md: 892d2e329232f539020b588b02922a1b596496685c1d1cfdbe36b7a9e5c595cd
- models/Delft3D/source-analysis/delft3d_dflowfm_transport_sediment.md: 18cc0e7fc3ecbbe42d5c1e95c6ca3f5871367a1dad0bda7faeec79ad6ffbc6df
- models/Delft3D/source-analysis/delft3d_dflowfm_waves.md: a220490a827101771533f03a7cb149188a6103132b4557c62d4f129caa78a77c
- models/Delft3D/source-analysis/delft3d_dredge_dump.md: e8a5184d4f57f8af586a7d6c200d70a8b7db3dbdf5dc287cf9e5d0b80bc6ba55
- models/Delft3D/source-analysis/sediment/delft3d_sediment.md: 5346afff0f38ebde7dde74fb33c6ba2f9111ae7244cb41abd6b6def8e9cd002c
- models/Delft3D/source-analysis/delft3d_flow2d3d_io.md: eff6f8be820bd51a84df72f2620204dd8662e97f5c0d38d015dca67c7073d5a0
- models/Delft3D/source-analysis/delft3d_waq_kernel_integration.md: bfad2ad7fb5119b0268238a3ab24a8cdc7ef6bb27a2ac2f9e0f0e901cd3c70cb
- models/Delft3D/source-analysis/delft3d_wave_swan_module.md: 0316f405b5b574ea42a2e0ffceb88e0f2ca26c440d6cdb51ab7f2eb44fde5ac7
- models/Delft3D/source-analysis/delft3d_heat.md: 42eff25ee7445a78fa11605e284f7ba1ca826c83d0fc14393a2f4a1d8961a6c7
- models/Delft3D/source-analysis/delft3d_sediment_transport_formulae.md: a09a47e7726506b070fe53ba12ed2f05a70c36bfe96c155f1c3ba7012af70636
