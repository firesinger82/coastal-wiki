---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wetcells.F90
lines: 146
sha256: f1a55183428c7d940ddc5cd13d26bcbbc093d6e223ea451ba277f5a2064b462b
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# wetcells.F90 — 판독 구간 기록

구간은 1행부터 146행까지 빈틈없이 이어진다. 범위 표시는 실제로 열린 제어 블록을 바깥에서 안쪽 순서로 적는다. 참·else if·else는 해당 원문 조건의 분기이며, where의 마스크와 do·forall의 반복 범위를 함께 적용한다. 같은 select의 case는 병렬 분기다. 원문 연속행은 각 행의 코드와 행 번호를 그대로 나열한다.

| 구간 | 내용 |
|---|---|
| 1–7 | `wetcells_module`의 implicit none·save·private와 공개 `compute_wetcells`, contains·서브루틴 진입(1–7). 구간 첫 줄의 제어 범위: 열린 제어 블록 없음. |
| 8–33 | UNESCO-IHE 등 저작권·주소·LGPL 2.1 이상·보증 부인 주석(8–33). 구간 첫 줄의 제어 범위: 열린 제어 블록 없음. |
| 34–59 | params/spaceparamsdef/paramsconst import, s·par·i/j·upwinddist·save된 weteb 배열·numeps 선언(34–47). 미할당 weteb만 nx+1×ny+1 할당(49). hu/hum의 병렬 이웃 교환 필요성 주석이며 실제 MPI 호출은 이 구간에 없음(51–59). 구간 첫 줄의 제어 범위: 열린 제어 블록 없음. 원문 조건·식·호출: <br>범위: 열린 제어 블록 없음. `real*8,parameter                        :: numeps = epsilon(0.d0)` (47); `if(.not.allocated(weteb)) allocate(weteb(s%nx+1,s%ny+1))` (49) |
| 60–81 | 전 격자점 루프에서 u점 평균수심 hum을 hh 양쪽 평균과 par%eps의 max로 계산(60–68). 별도 루프의 hu 및 hum이 eps+numeps보다 모두 큰 조건에서 wetu=1, else는 0(73–81). 구간 첫 줄의 제어 범위: 열린 제어 블록 없음. 원문 조건·식·호출: <br>범위: 열린 제어 블록 없음. `do j=1,s%ny+1` (60); <br>범위: 60행 do. `do i=1,s%nx+1` (61); <br>범위: 60행 do → 61행 do. `s%hum(i,j)=max(.5d0*(s%hh(i,j)+s%hh(min(s%nx,i)+1,j)),par%eps)` (66); <br>범위: 60행 do. `end do` (67); <br>범위: 열린 제어 블록 없음. `end do` (68); `do j=1,s%ny+1` (73); <br>범위: 73행 do. `do i=1,s%nx+1` (74); <br>범위: 73행 do → 74행 do. `if(s%hu(i,j)>par%eps+numeps .and. s%hum(i,j)>par%eps+numeps) then` (75); <br>범위: 73행 do → 74행 do → 75행 if 참. `s%wetu(i,j)=1` (76); <br>범위: 73행 do → 74행 do. `else` (77); <br>범위: 73행 do → 74행 do → 75행 if의 else(77행, 앞 분기 불성립). `s%wetu(i,j)=0` (78); <br>범위: 73행 do → 74행 do. `end if` (79); <br>범위: 73행 do. `end do` (80); <br>범위: 열린 제어 블록 없음. `end do` (81) |
| 82–102 | hv/hvm의 병렬 교환 주석(82–86). v점 평균수심 hvm을 hh 양쪽 평균과 eps의 max로 계산(87–92). 별도 루프에서 hv 및 hvm이 eps+numeps보다 모두 클 때 wetv=1, else 0(94–102). 구간 첫 줄의 제어 범위: 열린 제어 블록 없음. 원문 조건·식·호출: <br>범위: 열린 제어 블록 없음. `do j=1,s%ny+1` (87); <br>범위: 87행 do. `do i=1,s%nx+1` (88); <br>범위: 87행 do → 88행 do. `s%hvm(i,j)=max(.5d0*(s%hh(i,j)+s%hh(i,min(s%ny,j)+1)),par%eps)` (90); <br>범위: 87행 do. `end do` (91); <br>범위: 열린 제어 블록 없음. `end do` (92); `do j=1,s%ny+1` (94); <br>범위: 94행 do. `do i=1,s%nx+1` (95); <br>범위: 94행 do → 95행 do. `if(s%hv(i,j)>par%eps+numeps .and. s%hvm(i,j)>par%eps+numeps) then` (96); <br>범위: 94행 do → 95행 do → 96행 if 참. `s%wetv(i,j)=1` (97); <br>범위: 94행 do → 95행 do. `else` (98); <br>범위: 94행 do → 95행 do → 96행 if의 else(98행, 앞 분기 불성립). `s%wetv(i,j)=0` (99); <br>범위: 94행 do → 95행 do. `end if` (100); <br>범위: 94행 do. `end do` (101); <br>범위: 열린 제어 블록 없음. `end do` (102) |
| 103–115 | eta점 wet 여부: 주변 속도점 기반 대안은 주석(106–107). 실행 코드는 hh>eps+numeps이면 wetz=1, else 0(108–112); 전 nx+1×ny+1 루프(104–114). 구간 첫 줄의 제어 범위: 열린 제어 블록 없음. 원문 조건·식·호출: <br>범위: 열린 제어 블록 없음. `do j=1,s%ny+1` (104); <br>범위: 104행 do. `do i=1,s%nx+1` (105); <br>범위: 104행 do → 105행 do. `if(s%hh(i,j)>par%eps+numeps) then` (108); <br>범위: 104행 do → 105행 do → 108행 if 참. `s%wetz(i,j)=1` (109); <br>범위: 104행 do → 105행 do. `else` (110); <br>범위: 104행 do → 105행 do → 108행 if의 else(110행, 앞 분기 불성립). `s%wetz(i,j)=0` (111); <br>범위: 104행 do → 105행 do. `end if` (112); <br>범위: 104행 do. `end do` (113); <br>범위: 열린 제어 블록 없음. `end do` (114) |
| 116–129 | 파랑 젖음 where는 hh+delta*H>eps 또는 wetz=1이면 wete=1, elsewhere 0(117–121). where 밖에서 weteb=0(123). scheme=SCHEME_UPWIND_1이면 주변거리 1, 그 외 2(125–129). 구간 첫 줄의 제어 범위: 열린 제어 블록 없음. 원문 조건·식·호출: <br>범위: 열린 제어 블록 없음. `where(s%hh+par%delta*s%H>par%eps .or. s%wetz==1)` (117); <br>범위: 117행 where 마스크 참. `s%wete = 1` (118); <br>범위: 열린 제어 블록 없음. `elsewhere` (119); <br>범위: 117행 where의 elsewhere(119행, 앞 마스크 제외). `s%wete = 0` (120); <br>범위: 열린 제어 블록 없음. `endwhere` (121); `weteb = 0` (123); `if (par%scheme==SCHEME_UPWIND_1) then` (125); <br>범위: 125행 if 참. `upwinddist = 1` (126); <br>범위: 열린 제어 블록 없음. `else` (127); <br>범위: 125행 if의 else(127행, 앞 분기 불성립). `upwinddist = 2` (128); <br>범위: 열린 제어 블록 없음. `endif` (129) |
| 130–146 | wete=0인 점만 forall 처리: ±upwinddist의 x/y wetz와 바로 이웃 wetu/wetv의 maxval 중 max를 weteb에 저장(130–135). wete 기반 대안식은 주석(136–139). forall 종료 뒤 별도 where(wete==0)에서 weteb로 대체(141–143). 루틴·모듈 끝(145–146). 구간 첫 줄의 제어 범위: 열린 제어 블록 없음. 원문 조건·식·호출: <br>범위: 열린 제어 블록 없음. `forall(i=1:s%nx+1,j=1:s%ny+1,s%wete(i,j)==0)` (130); <br>범위: 130행 forall. `weteb(i,j) = max(   maxval(  s%wetz( max(i-upwinddist,1):min(i+upwinddist,s%nx+1) ,j )   ), &` (131), `maxval(  s%wetz( i, max(j-upwinddist,1):min(j+upwinddist,s%ny+1) )   ), &` (132), `maxval(  s%wetu( max(i-1,1):min(i,s%nx+1) ,j                     )   ), &` (133), `maxval(  s%wetv( i, max(j-1,1):min(j,s%ny+1)                     )   ) &` (134), `)` (135); <br>범위: 열린 제어 블록 없음. `endforall` (140); `where(s%wete==0)` (141); <br>범위: 141행 where 마스크 참. `s%wete=weteb` (142); <br>범위: 열린 제어 블록 없음. `endwhere` (143) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 46·49: weteb는 allocatable,save이며 미할당일 때만 현재 nx+1×ny+1로 할당한다. 재호출 때 격자 크기 변경을 확인하는 조건은 없다.
- 51–59·69–71·82–86: hu/hum·hv/hvm의 병렬 이웃 교환 필요성을 설명하는 주석은 있으나 이 파일에는 MPI 호출이 없다.
- 106–108: 주변 속도점 중 하나라도 젖으면 eta점이 젖는다는 주석과 주석 처리된 대안식 다음에, 실행 코드는 hh>eps+numeps 기준으로 wetz를 설정한다.
