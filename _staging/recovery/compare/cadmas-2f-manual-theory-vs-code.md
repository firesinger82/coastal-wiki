# 2F manual p.1–60와 3D2F 코드 대조

## 1 요약

분류별 개수: 일치 67행, A 8행, B 32행, C 29행, D 3행, E 10행, F 5행, H 7행, X 0행. 집계 대상은 §2·§3의 서로 다른 행 ID 161개이다.

대상은 `CADMAS-SURF-3D2F/Manual/CADMAS-2F_Manural_English.pdf` PDF p.1–60이다.
인쇄 쪽은 463–522이다. 이 보고서에서 `2F manual p.N`과 `3D manual p.N`의 N은 PDF 쪽이다.
인쇄 쪽은 각각의 쪽 이미지 하단에서 확인한다.
매뉴얼 원문과 코드 원문을 구분한다. 한국어 설명과 `해석:` 문장은 AI가 작성했다.
모델은 실행하지 않는다. 실행·수치·물리 검증은 이 보고서의 확인 수준에 포함하지 않는다.
다른 노트의 수정안은 §4에만 기록한다.

EOS와 밀도 반복의 구현은 존재한다. 기상 기본값은 비압축 모드이다.
공통식은 3D manual의 대응 쪽으로 연결했다. 두 매뉴얼에서 같은 인쇄식을 서로 다르다고 읽은 기존 판정은 원해상도 이미지로 바로잡았다.
압축항 부호·스칼라 압축항·밀도 이류 계수·압축 행렬 첨자·확산 호출·표면밀도 복사 방향은 E 후보로 기록한다.
E는 정적 모순의 분류이다. E는 실행으로 확인한 결함 확정이 아니다.

경로 약칭은 다음과 같다.

- `S` = `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators`.
- `2F 파일:줄` = `S/CADMAS-SURF-3D2F/Source code/파일:줄`.
- `3D 파일:줄` = `S/CADMAS-SURF-3D/Source code/파일:줄`.
- `N/파일:줄` = `models/CADMAS-SURF/파일:줄`.
- 이미지 = `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/<접두어>-NNN.png`.

코드 판 근거는 `2F vf_a1main.f:33`의 `C----------------------------------------------------------2016.09 start`이다.
3D 사본의 날짜 표지와 두 사본의 실제 차이를 함께 사용한다.
표지 p.1은 `CADMAS-SURF 3D-2F`만 적는다. 표지는 발행일을 적지 않는다.
인쇄 쪽의 연속성만으로 코드 작성일을 추정하지 않는다.
115개 동일 파일의 목록은 `_staging/recovery/scripts/cadmas-3d2f-identical-to-3d.txt`이다.
동일 파일의 3D 판독 기록은 탐색 색인으로 사용한다. 판정에는 `nl -ba`로 연 코드 원문을 사용한다.

§2의 `일치`는 해당 행에 명시한 조건에서의 정적 대조 결과이다.
같은 식은 3D manual의 해당 쪽과 식 번호를 적고 중복 전사를 생략한다.
식의 차이, 조건의 차이, 문서 내부의 오류는 별도 행으로 적는다.
한 행에 연결한 여러 식은 같은 구현 경로와 같은 판정을 공유한다.
§5는 일치 이외의 행을 하나씩 분류한다.

## 2 대조 표

### 2.1 개요와 물리모델

| 행 ID | 문서 위치와 원문 | 코드 위치와 원문 | 판정 | 이유 |
|---|---|---|---|---|
| KF1-001 | 2F manual p.1(인쇄 463). `CADMAS-SURF 3D-2F`. 제목 외 본문 없음. | 2F vf_a1main.f:5 `CDT   VF_A1MAIN:CADMAS-SURF/3D-2Fのメインルーチン`. 뜻: 3D-2F 메인 루틴. | 일치 | 표지는 발행일·판 번호를 제시하지 않는다. |
| KF1-002 | p.2 개발 동기. `the volume of the isolated gas phase region can not change`. | 2F vf_v1eos.f:67 `IF(ISTATE.EQ.0) RETURN`. | 코드 대조 대상 아님(H) | 비압축 가정에서 고립 기포와 케이슨 충격압에 관한 설명이다. 코드로 적용 성능을 검증하지 않는다. |
| KF1-003 | p.2(a), `Fortran 90`, 동적 배열, 6자 초과 이름, 일반 코딩 `FORTRAN 77`. | 2F vf_a1main.f:9 `CD      (4)言語    :Fortran90(配列の動的アロケートのため)`. 뜻: 동적 배열 할당 때문에 Fortran90. :18 `IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)`. | 일치 | 고정형식과 동적 배열을 함께 사용한다. 전체 언어 준수의 컴파일 검사는 하지 않았다. |
| KF1-004 | p.2(b), 무번호식 \(\rho=\rho(p)\). `the energy equation is not included in the basic equation group`. | 2F user_eos.f:1 `SUBROUTINE USER_EOS(ISTATE,SPARAM,PP,RHOG,DRHODP)`; :33 `RHOG   = (PP + P0)/(RCONS*TCONS)`. | 일치 | 압력으로 기상밀도를 계산한다. 온도 수송을 EOS 에너지 방정식으로 결합하지 않는다. |
| KF1-005 | p.2–3, `SIMPLE method-like method`, 시간 간격 내 수렴 반복·필요할 때 완화계수. | 2F vf_a1main.f:1347 `DO LL=1,MAXITR`; :1363–1364 `RHOG(I,J,K) =        SRELAX *RHOG(I,J,K)`<br>`     &                      + (1.0D0-SRELAX)*WK01(I,J,K)`; :1385 `IF(SERR.LE.SERROR) EXIT`. | 일치 | 반복 상한·판정 대상·완화 전 오차의 세부 동작은 KF1-201에 둔다. |
| KF1-006 | p.3, 시간·이류 밀도항의 1차 Taylor 전개를 압력 Poisson 식에 도입. | 2F vf_vpdrdt.f:81 `C  ρ^new = ρ^old + (dρ/dp)^old*Δp`; :154–156 `AD(I,J,K) = AD(I,J,K) + AVLT*DRHODP(I,J,K)/DTNOW`<br>`AD(I,J,K) = AD(I,J,K) - AVLT*DRHODP(I,J,K)*DRHODT(I,J,K)`<br>`BB(I,J,K) = BB(I,J,K) + AVL*DRHODT(I,J,K)`. | 일치 | 개요의 선형화에 대응한다. 모든 방향 계수의 정확성을 뜻하지 않는다. |
| KF1-007 | p.3, EOS와 압력 미분을 `user function`으로 제공. 동작 확인용 `isothermal process`. | 2F user_eos.f:23 `IF(ISTATE.EQ.1) THEN`; :33–34 `RHOG   = (PP + P0)/(RCONS*TCONS)` / `DRHODP = 1.0D0/(PP + P0)`. | 일치 | 반환 미분은 \((d\rho/dp)/\rho\)이다. 문서는 이 쪽에서 변수형·기본값을 제시하지 않는다. |
| KF1-008 | p.3(c)(d), `Single Program Multiple Data (SPMD)`, 영역 분할·분산 메모리·PC 클러스터·MPI. | 2F vf_a1main.f:31 `INCLUDE  'mpif.h'`; :1369 `CALL VF_P1MAXD(W,SERR)`; vf_v1eos.f:80–81 `CALL VF_P3SRD1(RHOG  ,DBUF,0)` / `CALL VF_P3SRD1(DRHODP,DBUF,0)`. | 일치 | 영역 배열의 교환과 전역 최대값 통신이 있다. 대상 하드웨어의 성능 검증은 아니다. |
| KF1-009 | p.4 그림 0-1-1, `data.in0000-XXXX`, `data.mg`, `data.mtb0000-XXXX`, `data.poro0000-XXXX`, `data.res0000-XXXX`. `MG ファイル` 뜻: MG 파일. | 2F vf_ii1inp.f:128 `     &       FILE=TRIM(MGNAME(MGRANK+1))//'.in',`; vf_ip1inp.f:60 `     &                  FILE=TRIM(MGNAME(MGRANK+1))//'.poro.ascii',`. 완전한 OPEN 문장은 보충 인용에서 확인한다. | 불일치(C) | 그림은 기본 이름 data의 예시이다. 코드는 MG 이름을 사용한다. ASCII 공극률 입력은 그림에 없다. |
| KF1-010 | p.4, `Standard Output`·`List file`·`Graphic file`·`Detail file`·`History file`, 확장자 .list·.grp·.rsl·.tran. | 2F vf_a1main.f:1387–1388 `IF (MYRANK.EQ.0)`<br>`     &      WRITE(6,'(A,I5,A,1PE15.5)') 'ITER=',LL,' SERR=',SERR`. 파일 OPEN 원문은 보충 인용에 둔다. | 일치 | 출력 종류가 대응한다. p.4는 장치 번호·레코드 형식을 제시하지 않는다. 겹쳐 잘린 이름 뒷부분을 추정하지 않는다. |
| KF1-011 | p.4, `Word`·`Spread Sheet`·`Vie Graphic`·`CADMAS-SURF/3D-MP`·`Folder(DataBmp)`·`Viewer`와 .bmp 연결. | 해석 코드의 수치 연산 대상이 아니다. | 코드 대조 대상 아님(H) | 외부 편집·후처리 사용 관계이다. 제외된 후처리기 내부는 열지 않았다. |
| KF1-012 | p.5 표 0-1-1과 p.7·9, `three-dimensional incompressible viscous fluid`. | 2F vf_v1eos.f:67 `IF(ISTATE.EQ.0) RETURN`; user_eos.f:33 `RHOG   = (PP + P0)/(RCONS*TCONS)`. | 불일치(B) | 같은 문서 p.2–3·9가 압축성 기상을 명시한다. 비압축성이라는 무조건 서술은 ISTATE=0 조건이 빠졌다. |
| KF1-013 | p.5, 자유수면 다가함수·직교좌표계·VOF·고 Reynolds 수 \(k-\varepsilon\)·셀 구조물·표면별 경계조건. | 2F vf_a1main.f:7–8 `CD      (2)解析方法:差分法,SMAC法,VOF法` / `CD      (3)座標系  :デカルト座標系`. 뜻: 차분·SMAC·VOF와 직교좌표계. | 일치 | 상세 식과 경계는 각각 뒤에서 판정한다. |
| KF1-014 | p.5·12–13, Stokes 5차·Knoid 3차·흐름함수 B·matrix 자료. | 2F vf_cwmak0.f:33–34 `N=5` / `CALL VF_STK0(N,R4D,R4T,R4H,R4W1,R4E1,R4K,R4L,R4C,R4CC)`; :40–41 `N=3` / `CALL VF_CND0(N,R4D,R4T,R4H,R4W1,R4E1,R4K,R4L,R4C,R4CC)`; :51–52 `CALL vf_sfmb02C(N,R4D,R4T,R4H,R4U,R4A,`<br>`     &                  R4L,R4K,R4HH,ICN,R4E1,MSG)`. | 일치 | 3D manual p.13과 같다. 외부 파형 논문의 모든 계수를 검증한 결과는 아니다. |
| KF1-015 | p.5·14, `Wave source(Unused)`. 식 (2.10)–(2.15)는 3D manual p.14와 같다. 2F는 Unused를 추가한다. | 2F vf_vpcoef.f:429 `CAKIY         IF (IWS.EQ.I) VQ=2.0D0*ZZ(2,K)*WVU(K)`; vf_f1cal.f:143 `CAKIY CALL FGENE(XX,ZZ,FF,WVU,QF,NF)`. | 일치 | CAKIY는 고정형식 주석이다. 조파원은 비활성이다. |
| KF1-016 | p.5, `(Unused)Energy equation`·`(Unused)Multicomponent concentration transport equations`. | 2F vf_a1main.f:1404 `IF (LEQT.NE.0) THEN`; vf_iiequa.f:45–46 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'CALC'  ) THEN` / `LEQT=1`. | 불일치(B) | 사용자가 수송식을 켤 수 있다. p.18·59–60도 수송식을 기술한다. 호출 인수 오류는 KF1-206이다. |
| KF1-017 | p.5–6, 엇갈림 차분·다공성 형상·Euler·SMAC·1차 상류·2차 중앙·DONOR·VOF donor–acceptor. | 2F vf_vflxdu.f:68–69 `SU=SCMVP` / `SC=1.0D0-SCMVP`; :81–83 `FLUU(I,J,K)=FLUU(I,J,K)-SU*( MAX( WIN,0.0D0)*UU(I  ,J,K)`<br>`     &                                    -MAX(-WIN,0.0D0)*UU(I+1,J,K))`<br>`     &                               -SC*FG`. | 일치 | SCMVP=1은 상류이다. SCMVP=0은 중앙이다. 입력 검사는 KF1-208이다. |
| KF1-018 | p.6, `(unused)Method considering inclination of interface`. p.11은 `can also be selected`. | 2F vf_iicomp.f:45–46 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'FF-SLOPE') THEN` / `ISCMFF=1`; vf_f1cal.f:135–138 `CALL VF_FCONVS(XX,YY,ZZ,UU,VV,WW,FF,GGV,GGX,GGY,GGZ,BCF,`<br>`     &                 DBUF,FLFU,FLFV,FLFW,`<br>`     &                 NF,INDX,INDY,INDZ,IBUF,NWK1,`<br>`     &                 WK05,WK06,WK07,WK08)`. | 불일치(B) | 미사용 표시는 같은 문서의 선택 가능 설명과 실제 분기에 모순이다. |
| KF1-019 | p.6·21–22, 표면 속도 외삽·영 기울기·연속식 보정. | 2F vf_v1cal.f:390–392 `C2F   CALL VF_BSUWT (XX,YY,ZZ,UU,VV,WW,DBUF,NF,INDX,INDY,INDZ)`<br>`C2F   CALL VF_BSUWT2(UU,VV,WW,DBUF,NF,INDX,INDY,INDZ,INDS)`<br>`C2F   CALL VF_BSUWN (XX,YY,ZZ,UU,VV,WW,GGX,GGY,GGZ,DBUF,NF,INDS)`. | 불일치(A) | 3D의 자유수면 속도 설정 호출을 2F는 C2F로 끈다. 남은 루틴 본문을 현재 실행으로 해석하지 않는다. |
| KF1-020 | p.6, NASA-VOF3D 방향 결정·TimerDoor·MILU-BiCGSTAB·고정 및 자동 시간 간격. | 2F vf_a2dflt.f:37 `ICGTYP=1`; :52 `CGPARA=0.95D0`; :231 `IDTTYP=1`. NF·TimerDoor·solver·시간 선택의 호출과 입력은 보충 대조에 둔다. | 일치 | 기능 선택이 존재한다. p.63–64의 solver·CFL 이론식은 대상 쪽 밖이다. |
| KF1-021 | p.6, 유속 벡터·등치선·자유수면·유체 채움·`2D only in drawing section`·스프레드시트 시계열. | .grp·.tran 출력은 KF1-010이다. | 코드 대조 대상 아님(H) | 그리기·외부 도구 사용 설명이다. 해석 코드가 그림을 직접 그린다고 해석하지 않는다. |
| KF1-022 | p.6, `◎：今回実現した機能，×：今回は実現しなかった機能`. 뜻: ◎는 이번 구현, ×는 이번 미구현. | 수치 연산 대상이 아니다. | 코드 대조 대상 아님(H) | 기능표의 기호 범례이다. 추출문에 섞인 다른 쪽 격자 숫자는 원문 기능표에 없다. |
| KF1-023 | p.7–8 그림 0-2-1·0-2-2, 셀 중심 스칼라·음측 면 속도·가상 셀. p.8은 그림·캡션만 있음. | 2F vf_vpcoef.f:421–423 `VD= AYZ*(GGX(IP,J,K)*UU(IP,J,K)-GGX(I,J,K)*UU(I,J,K))`<br>`     &           +AXZ*(GGY(I,JP,K)*VV(I,JP,K)-GGY(I,J,K)*VV(I,J,K))`<br>`     &           +AXY*(GGZ(I,J,KP)*WW(I,J,KP)-GGZ(I,J,K)*WW(I,J,K))`. | 일치 | 3D manual p.8–9와 같은 배치이다. |
| KF1-024 | p.9 식 (2.1). 3D manual p.10 식 (2.1)에 추가한 항은 \(-\frac{1-F}{\rho_G}\dot{\rho}_G\). | 2F vf_vpdrdt.f:95 `AVL  = (1.0D0 - FF(I,J,K))*XX(2,I)*YY(2,J)*ZZ(2,K)`; :156 `BB(I,J,K) = BB(I,J,K) + AVL*DRHODT(I,J,K)`. | 일치 | 여기서 체적과 1-F를 곱한다. 행렬 전체의 부호를 반대로 조립한다. 미분계수의 차이는 KF1-056이다. |
| KF1-025 | p.9 식 (2.2). 3D manual p.10 식 (2.2)에 추가한 항은 \(-u\frac{1-F}{\rho_G}\dot{\rho}_G\). | 2F vf_veuler.f:143–145 `DRDTU=XX(6,I)*(XX(2,I  )*DRHODT(I  ,J,K)`<br>`     &                      +XX(2,I-1)*DRHODT(I-1,J,K))`<br>`     &                     *(1.0D0 - FX(I,J,K))*UU(I,J,K)`; :152 `UU(I,J,K)=(GV*UUO(I,J,K)+DTNOW*(DU+DRDTU))/GV0`. | 불일치(E) | 문서는 음의 항이다. 코드는 양의 항이다. §5에서 보존형 식과 반대 근거를 검토한다. |
| KF1-026 | p.9 식 (2.3). 3D manual p.10 식 (2.3)에 추가한 항은 \(-v\frac{1-F}{\rho_G}\dot{\rho}_G\). | 2F vf_veuler.f:209–211 `DRDTV=YY(6,J)*(YY(2,J  )*DRHODT(I,J  ,K)`<br>`     &                      +YY(2,J-1)*DRHODT(I,J-1,K))`<br>`     &                     *(1.0D0 - FY(I,J,K))*VV(I,J,K)`; :218 `VV(I,J,K)=(GV*VVO(I,J,K)+DTNOW*(DV+DRDTV))/GV0`. | 불일치(E) | y 성분도 더한다. |
| KF1-027 | p.9 식 (2.4). 3D manual p.10 식 (2.4)에 추가한 항은 \(-w\frac{1-F}{\rho_G}\dot{\rho}_G\). | 2F vf_veuler.f:275–277 `DRDTW=ZZ(6,K)*(ZZ(2,K  )*DRHODT(I,J,K  )`<br>`     &                      +ZZ(2,K-1)*DRHODT(I,J,K-1))`<br>`     &                     *(1.0D0 - FZ(I,J,K))*WW(I,J,K)`; :284 `WW(I,J,K)=(GV*WWO(I,J,K)+DTNOW*(DW+DRDTW))/GV0`. | 불일치(E) | z 성분도 더한다. |
| KF1-028 | p.9–10의 \(t,x,y,z,u,v,w,\rho,\rho^*,\nu,\nu_t,\nu_e,g,\gamma_v,\gamma_x,\gamma_y,\gamma_z,C_M,D_x,D_y,D_z,S_\rho,S_u,S_v,S_w,C_D,\Delta x,\Delta y,\Delta z\) 정의. | 2F vf_a1main.f:67 `CD    ANU(@FOR-3D@)     : R*8 : 分子動粘性係数と渦動粘性係数の和`. 뜻: 분자 동점성과 와동점성의 합. :78–87의 CM0·CD0·GGV·GGX·GGY·GGZ·GLV·GLX·GLY·GLZ. | 일치 | 3D manual p.10–11과 같다. 문서는 여기서 형·배열 크기·COMMON·파일 번호를 선언하지 않는다. |
| KF1-029 | p.10, `and` 다음 점 없는 \(\rho_G\)를 실질미분으로 정의. | 2F vf_v1eos.f:170–172 `DRHODT(I,J,K) =`<br>`     &         (  GGV(I,J,K)*(RHOG(I,J,K) - RHOGO(I,J,K))/DTNOW`<br>`     &          + WUC*DRHODX + WVC*DRHODY + WWC*DRHODZ)/RHOG(I,J,K)`. | 불일치(B) | p.9·24의 미분 기호는 \(\dot{\rho}_G\)이다. 밀도와 그 미분은 차원이 다르다. |
| KF1-030 | p.10 식 (2.5)의 네 식. 3D manual p.11 식 (2.5)와 같다. | 2F vf_cglxyz.f:65 `GLX(I,J,K)=GGX(I,J,K)+(1.0D0-GGX(I,J,K))*CM`; :77 `GLY(I,J,K)=GGY(I,J,K)+(1.0D0-GGY(I,J,K))*CM`; :89 `GLZ(I,J,K)=GGZ(I,J,K)+(1.0D0-GGZ(I,J,K))*CM`. | 일치 | CM은 면적 보간한다. GLV는 보충 인용에 둔다. |
| KF1-031 | p.10 식 (2.6)의 세 저항식. 3D manual p.11 식 (2.6)와 같다. | 2F vf_vgene.f:125–127 `UVW=SQRT(U*U+V*V+W*W)`<br>`QU(I,J,K)=QU(I,J,K)`<br>`     &                  -0.5D0*CD*XX(5,I)*(1.0D0-GGX(I,J,K))*U*UVW`. | 일치 | 1/2·1-투과율·속도 크기·음의 저항이 대응한다. 면의 간격은 중심 간격이다. |
| KF1-032 | p.10 `エラー! 参照元が見つかりません。`. 뜻: 오류! 참조 원본을 찾을 수 없습니다. p.11 `not fluid / not`. | 2F vf_feuler.f:52 `FF(I,J,K)=(G0*FF(I,J,K)+DF)/GGV(I,J,K)`. | 불일치(B) | 상호참조와 계단함수 설명의 편집 오류이다. F의 계산식을 바꾸지 않는다. |
| KF1-033 | p.11 식 (2.7). 3D manual p.11 식 (2.7)와 같다. 2F는 액상 비압축성 때문에 기상 압축항이 없다고 설명한다. p.12 그림 0-2-3·0-2-4는 F=0.6 분할과 균질한 1-α=0.6을 비교한다. | 2F vf_feuler.f:48–52 `DF=( XX(4,I)*(FLFU(I+1,J,K)-FLFU(I,J,K))`<br>`     &            +YY(4,J)*(FLFV(I,J+1,K)-FLFV(I,J,K))`<br>`     &            +ZZ(4,K)*(FLFW(I,J,K+1)-FLFW(I,J,K))`<br>`     &            +DTNOW*QF(I,J,K)                    )`<br>`FF(I,J,K)=(G0*FF(I,J,K)+DF)/GGV(I,J,K)`. | 일치 | DRHODT를 VOF에 넣지 않는다. 그림은 3D manual p.12와 같다. 0.2·0.2·1.0·1.0의 평균은 0.6이다. |
| KF1-034 | p.13 `the following two wave boundaries and wave-generating sources are adopted`. p.14의 조파원 사용 설명. | 2F vf_f1cal.f:143 `CAKIY CALL FGENE(XX,ZZ,FF,WVU,QF,NF)`. 3D 사본의 활성 문장은 보충 인용이다. | 불일치(A) | 2F는 Unused를 추가했으나 3D manual p.13–14의 사용 문장이 남았다. |
| KF1-035 | p.13 식 (2.8)–(2.9). 3D manual p.13과 같다. \(\eta_0,\eta_s,h,U_0,U,z^*\)로 유량을 맞춘다. | 2F vf_bwuwn.f의 VWS·ZC·WVUN 보정은 보충 인용에 둔다. | 일치 | 수위에 따른 수심비 보정이다. 수직 속도에 같은 배율을 곱한다고 확대하지 않는다. |
| KF1-036 | p.13 조파 경계의 수평 지정 속도·F와 압력 증분의 영 기울기. 3D manual p.14와 같다. | 2F vf_bwff.f:57–59 `ELSEIF (IB.EQ.5) THEN` / `IF     (NS.EQ.1) THEN` / `BCF(L)=FF(I  ,J,K)`; vf_bwuwn.f:346 `BCU(L,2)=UN*VWS*AW*SA`. | 일치 | F는 내부 값을 복사한다. 압력 증분의 Neumann 조건은 벽면 행렬 처리와 대응한다. 압력 자체의 구배가 항상 0이라는 뜻은 아니다. |
| KF1-037 | p.14 식 (2.10)–(2.15), \(S_\rho,S_u,S_v,S_w,S_F,q\), \(x=x_s\) 또는 \(y=y_s\), \(q=2U/\Delta x_s\). 그림 0-2-5의 조파원·조파 경계. 3D manual p.14–15와 같다. | 2F vf_vpcoef.f:429 `CAKIY         IF (IWS.EQ.I) VQ=2.0D0*ZZ(2,K)*WVU(K)`. | 불일치(A) | 같은 식의 3D 활성 조파원에 대응하지만 2F 계산식으로 사용하지 않는다. p.14의 Unused 조건을 유지한다. |
| KF1-038 | p.15 식 (2.16), Sommerfeld의 x·y 식과 미소진폭 파속 C. 3D manual p.15 식 (2.16)와 같다. | 2F vf_bwuwn.f:180 `ELSEIF (IB.EQ.7) THEN`; vf_bwuwt.f:199 `ELSEIF (IB.EQ.7) THEN`. 실제 방사 경계 갱신은 보충 인용이다. | 일치 | 법선과 접선의 수평 외곽 방사 경계를 갖는다. 방향별 전파 부호를 좌표 경계에 맞춘다. |
| KF1-039 | p.15–16, 감쇠대 폭 `1 to 3 wavelengths`·안정적 계산·다양한 파형 적용·추가 계산 영역 필요. 그림 0-2-6. | 코드의 강제 제약이 아니다. | 코드 대조 대상 아님(H) | 권고 폭과 적용 특성 설명이다. 입력 폭을 파장의 1–3배로 강제한다고 쓰지 않는다. |
| KF1-040 | p.15–16 식 (2.17)–(2.19), \(-D_xu,-D_yv,-D_zw\)와 세 D 식. \(h,l,x_0,y_0,N,\theta_{xy},\theta_z\) 정의. 3D manual p.16과 같다. | 2F vf_veuler.f:100–103 `D  =SQRT(GRZ0/DAMP(4,1))` / `W1 =DAMP(3,1)` / `PX1=DBLE(IP1+1)*DAMP(1,1)*D` / `PZ1=DBLE(IP1+1)*DAMP(2,1)*D`; :166 `D=PX1*(1.0D0-D/W1)**IP1`; :192–193 `D=GV0/(GV0+DTNOW*G*DMAX)` / `UU(I,J,K)=UU(I,J,K)*D`. | 일치 | N+1·루트 g/h·멱 N·음의 감쇠를 보존한다. 겹치는 영역은 최대 D를 사용한다. 서로 다른 면별 폭·계수는 KF1-211이다. |
| KF1-041 | p.16 식 (2.20)–(2.21), \(u',v',w'\)로 정의한 난류에너지와 소산. 3D manual p.17과 같다. | 2F vf_cnut0.f:47 `ANUT(I,J,K)=AKCMU*AK(I,J,K)*AK(I,J,K)/W`. | 코드 대조 대상 아님(H) | 변동 속도의 수학적 정의이다. RANS 코드가 순간 변동 속도에서 이 식을 직접 평가하는 것은 아니다. |
| KF1-042 | p.17 식 (2.22)–(2.23). 3D manual p.17 식에 추가한 항은 각각 \(-k\frac{1-F}{\rho_G}\dot\rho_G\), \(-\varepsilon\frac{1-F}{\rho_G}\dot\rho_G\). | 2F vf_k1cal.f:152–153 `CALL VF_SEULER(XX,YY,ZZ,AK,GGV,GGV ,DBUF,FLKU,FLKV,FLKW,QK,NF)` / `CALL VF_SEULER(XX,YY,ZZ,AE,GGV,GGV ,DBUF,FLEU,FLEV,FLEW,QE,NF)`; vf_seuler.f:50–53의 전체 갱신식은 KF1-129에 둔다. | 불일치(E) | 두 호출은 DRHODT를 전달하지 않는다. KGENE의 QK·QE에도 압축 소멸항이 없다. p.57–58 이산식도 이를 빠뜨린다. 기본 ISTATE=0에서는 차이가 소거된다. |
| KF1-043 | p.17 식 (2.24), 평균 속도의 변형률 제곱으로 정의한 \(G_s\). 3D manual p.17과 같다. | 2F vf_kgene.f:161–166 `GS=ANUT(I,J,K)*(2.0D0*( DUDX*DUDX`<br>`     &                               +DVDY*DVDY`<br>`     &                               +DWDZ*DWDZ)`<br>`     &                        +(DUDY+DVDX)**2`<br>`     &                        +(DVDZ+DWDY)**2`<br>`     &                        +(DWDX+DUDZ)**2   )`. | 일치 | 대각 변형률의 계수 2와 세 교차항이 같다. |
| KF1-044 | p.17 식 (2.25), \(G_T=-\nu_t(\rho\sigma_t)^{-1}(g\,\partial\rho^*/\partial z)\). 3D manual p.17과 같다. | 2F vf_kgene.f:168–171 `CAKIY         * GT,RFの計算` / `GT =0.0D0` / `GST=GS+GT` / `RF =-GT/MAX(GST,ZERO)`. 뜻: GT·RF 계산. | 불일치(B) | 문서는 일반 부력생성식을 기술하지만 p.58 식 (3.116)–(3.117)은 GT를 빼고 적는다. 코드는 GT를 0으로 고정한다. 온도·농도 구배로 GT를 계산한다고 쓰지 않는다. |
| KF1-045 | p.17 식 (2.26), \(R_f=-G_T/(G_s+G_T)\). 3D manual p.17과 같다. | 2F vf_kgene.f:170–171 `GST=GS+GT` / `RF =-GT/MAX(GST,ZERO)`. | 불일치(C) | 문서는 분모의 ZERO 하한을 적지 않는다. GT=0인 현재 경로에서 RF도 0이다. |
| KF1-046 | p.17 식 (2.27), \(\nu_t=C_\mu k^2/\varepsilon\). 3D manual p.17과 같다. | 2F vf_cnut0.f:46–47 `W=MAX(AE(I,J,K),AKMINE)` / `ANUT(I,J,K)=AKCMU*AK(I,J,K)*AK(I,J,K)/W`. | 불일치(C) | \(\varepsilon\ge AKMINE\)이면 같다. 분모 하한은 문서 식에 없다. |
| KF1-047 | p.17 식 (2.28)–(2.29). 3D manual p.18과 같다. | 2F vf_k1cal.f:118 `W=1.0D0/AKSGK`; :123–124 `ANU1=FF(I,J,K)*ANU0(1)+(1.D0-FF(I,J,K))*ANU0(2)` / `WKNU(I,J,K)=ANU1+ANUT(I,J,K)*W`; :131 `W=1.0D0/AKSGE`; :137 `WKNU(I,J,K)=ANU1+ANUT(I,J,K)*W`. | 일치 | k와 ε의 확산계수를 각각 계산한다. 분자 점성은 두 상을 F로 혼합한다. |
| KF1-048 | p.17 경험상수 \(C_\mu=0.09,\sigma_k=1.00,\sigma_\varepsilon=1.30,C_1=1.44,C_2=1.92,C_3=0.0\). 3D manual p.18과 같다. | 2F vf_a2dflt.f:182–187 `AKCMU =0.09D0` / `AKSGK =1.0D0` / `AKSGE =1.3D0` / `AKC1  =1.44D0` / `AKC2  =1.92D0` / `AKC3  =0.0D0`. | 일치 | 여섯 수치가 기본 대입과 같다. 문서는 여기서 입력 키워드라고 제시하지 않는다. |
| KF1-049 | p.17–18 식 (2.30)–(2.31), \(\nu_e=\nu+\nu_t\), \(p'=p+\frac23\rho k\). 3D manual p.18과 같다. | 2F vf_cnu00.f:60–64 `ANU2=FF(I,J,K)*ANU0(1)+(1.D0-FF(I,J,K))*ANU0(2)` / `ANU(I,J,K)=ANU2+ANUT(I,J,K)`; vf_vgene.f:114–117 `IF (LEQK.NE.0) THEN`<br>`QU(I,J,K)=QU(I,J,K)`<br>`     &                           +GV*WK*XX(5,I)*(AK(I1,J,K)-AK(I,J,K))`<br>`ENDIF`; :86 `WK=2.0D0/3.0D0`. | 일치 | 점성에 와동점성을 더한다. 운동량에서 \(2k/3\)의 구배를 별도로 더한다. 출력 PP를 자동으로 p′라고 부르지 않는다. |
| KF1-050 | p.18 식 (2.32), 온도 주변수·밀도와 정압비열 변화가 작다는 조건. 3D manual p.18 식에 추가한 항은 \(-T\frac{1-F}{\rho_G}\dot\rho_G\). | 2F vf_t1cal.f:99 `CALL VF_SEULER(XX,YY,ZZ,TT,GGV,GGV ,DBUF,FLTU,FLTV,FLTW,QT,NF)`; :76 `QT  (I,J,K)=0.0D0`; :94 `CAKIY CALL VF_TGENE`. | 불일치(E) | 온도 경로에 압축 소멸항이 없다. p.59 이산식도 이를 빠뜨린다. 현재 코드의 호출 인수 문제는 KF1-206이다. |
| KF1-051 | p.18 식 (2.33), \(\lambda_e=\lambda+\rho c_p\nu_t/\mathrm{Pr}_t\). 3D manual p.18과 같다. | 2F vf_clm00.f:61–62 `W=RI*TCP0/AKPR` / `ALM(I,J,K)=TCN0+ANUT(I,J,K)*W`. RI의 정의는 보충 인용이다. | 일치 | 여기의 RI는 역밀도가 아니라 F 혼합 밀도이다. 기상 상수 RHO0(2)를 사용한다. |
| KF1-052 | p.18 식 (2.34), \(S_T=\rho c_pTq(z,t)\). 3D manual p.18과 같다. | 2F vf_t1cal.f:76 `QT  (I,J,K)=0.0D0`; :94 `CAKIY CALL VF_TGENE`. 3D vf_t1cal.f:91도 `CAKIY CALL VF_TGENE`이다. | 문서에만(D) | 두 코드 사본 모두 온도 소스를 계산하지 않는다. p.5의 Unused 표시를 함께 적용한다. 3D에서 2F로 바뀐 차이라고 단정하지 않는다. 전체 Simulators 검색은 §5에 둔다. |
| KF1-053 | p.18–19 식 (2.35), 오염 농도가 매우 작고 유동 영향 무시. \(c_i\)는 체적분율. 3D manual p.19 식에 추가한 항은 \(-c_i\frac{1-F}{\rho_G}\dot\rho_G\). | 2F vf_s1cal.f:79 `QC  (I,J,K)=0.0D0`; :100 `CAKIY   CALL VF_SGENE`; :105–106 `CALL VF_SEULER(XX,YY,ZZ,CC(1,1,1,LC),`<br>`     &                   GGV,GGV ,DBUF,FLCU,FLCV,FLCW,QC,NF)`. | 불일치(E) | 농도 경로도 압축 소멸항을 전달하지 않는다. p.60 이산식과 기본 ISTATE=0는 반대 근거로 함께 기록한다. |
| KF1-054 | p.18–19 식 (2.36), \(D_{ie}=D_i+\nu_t/S_{CT}\). \(c_i\)는 i번째 성분의 체적분율이다. \(D_i\)는 성분별 확산계수이다. \(S_{CT}\)는 입력값이다. 3D manual p.19와 같다. 식 (2.37)의 소스는 KF1-132에서 함께 판정한다. | 2F vf_cdd00.f:56 `W=1.0D0/AKSM(LC)`; :61 `DD(I,J,K,LC)=CDF0(LC)+ANUT(I,J,K)*W`. | 일치 | 성분별 분자 확산과 난류 확산의 합이다. p.19는 기호 정의만 이어지며 빈 쪽은 아니다. |
| KF1-055 | p.23–24 `2.10 Compressibility of gas phase`, 식 (2.38) \(\rho_G=\rho_G(p)\), 시공간 밀도·사용자 함수. | 2F vf_v1eos.f:73–74 `CALL USER_EOS(ISTATE,SPARAM,PP(I,J,K)`<br>`     &                     ,RHOG(I,J,K),DRHODP(I,J,K))`. | 일치 | 3D manual에는 대응 절이 없다. |
| KF1-056 | p.24 식 (2.39), \(\dot\rho_G=\gamma_v\frac{\partial\rho_G}{\partial t}+\gamma_xu\frac{\partial\rho_G}{\partial x}+\gamma_yv\frac{\partial\rho_G}{\partial y}+\gamma_zw\frac{\partial\rho_G}{\partial z}\). | 2F vf_v1eos.f:118–124 `GV = GGV(I,J,K)/GLV(I,J,K)`<br>`WUC = 0.5D0*( GGX(I+1,J,K)*UU(I+1,J,K)`<br>`     &                     +GGX(I  ,J,K)*UU(I  ,J,K))*GV`<br>`WVC = 0.5D0*( GGY(I,J+1,K)*VV(I,J+1,K)`<br>`     &                     +GGY(I,J  ,K)*VV(I,J  ,K))*GV`<br>`WWC = 0.5D0*( GGZ(I,J,K+1)*WW(I,J,K+1)`<br>`     &                     +GGZ(I,J,K  )*WW(I,J,K  ))*GV`; :170–172은 KF1-029. | 불일치(E) | 코드는 모든 이류 속도에 \(\gamma_v/\lambda_v\)를 추가한다. 문서는 그 인자를 갖지 않는다. 같은 판 연속식의 면 유속과도 다르다. \(\gamma_v=\lambda_v=1\)이면 차이가 소거된다. 강도와 의도 변경 검색은 §5에 둔다. |

### 2.2 경계조건 표의 무번호식

표의 같은 식은 3D manual p.20–22로 연결한다.
p.20 그림 0-2-7의 벽·자유수면, 법선·접선, b·s·in 첨자는 이 표의 정의에 해당한다.
그림 오른쪽의 `壁面`도 원문 그대로이다. 뜻은 벽면이다.

| 행 ID | 문서 위치와 원문 | 코드 위치와 원문 | 판정 | 이유 |
|---|---|---|---|---|
| KF1-057 | p.21 표 0-2-1 Slip, Non slip의 속도와 \(\partial\phi_b/\partial n=0\). 3D manual p.20과 같다. | 2F vf_bwuwn.f:104 `IF     (IB.EQ.1) THEN`; :114–117 `ELSEIF (IB.EQ.2) THEN` / `BCU(L,LGF)=0.0D0` / `BCV(L,LGF)=0.0D0` / `BCW(L,LGF)=0.0D0`; vf_bwuwt.f:78 `IF     (IB.EQ.1 .OR. IB.EQ.4) THEN`. | 일치 | slip은 법선 0·접선 영 기울기이다. non-slip은 세 속도 0이다. |
| KF1-058 | p.21 값 지정 및 조파 경계 \(u_n=u_{nin},u_t=u_{tin}\), \(\partial\phi_b/\partial n=0\). 3D manual p.20과 같다. | 2F vf_bwuwn.f:120–123 `ELSEIF (IB.EQ.3) THEN` / `BCU(L,LGF)=BCU(L,LGF)` / `BCV(L,LGF)=BCV(L,LGF)` / `BCW(L,LGF)=BCW(L,LGF)`. | 일치 | 입력 경계값을 보존한다. in은 입력값이라는 p.22 주석을 유지한다. |
| KF1-059 | p.21 Free, 속도 영 기울기·포텐셜 계산 뒤 법선 보정·\(\phi_b=0\). 3D manual p.20과 같다. | 2F vf_bwuwn.f:126–130 `ELSEIF (IB.EQ.4) THEN` / `IF     (NS.EQ.1) THEN` / `BCU(L,LGF)=UU(I+1,J,K)` / `ELSEIF (NS.EQ.2) THEN` / `BCU(L,LGF)=UU(I-1,J,K)`; vf_vmodif.f:113 `ELSEIF (INDB(LGBF,IS).EQ.4) THEN`. | 일치 | 자유수면과 외곽 Free를 구별한다. 경계의 φ=0으로 보정한다. |
| KF1-060 | p.21 Radiation, 법선·접선 Sommerfeld 식과 미소진폭 파속. 3D manual p.20과 같다. | 2F vf_bwuwn.f:180 `ELSEIF (IB.EQ.7) THEN`; vf_bwuwt.f:199 `ELSEIF (IB.EQ.7) THEN`. | 일치 | KF1-038의 방사 경계와 같은 처리이다. |
| KF1-061 | p.21 Logarithmic law의 무번호식·\(u^*=\sqrt{\tau/\rho}\), \(\kappa=0.4,A=5.5,y,u\) 정의. 3D manual p.20과 같다. | 2F vf_cloglw.f:36–44 `AKR=1.0D0/AKK0` / `ANR=1.0D0/ANU1` / `W=LOG(DL*XX*ANR)` / `F=XX*AKR*W+XX*AKA0-VA`; vf_a2dflt.f:188–189 `AKK0  =0.4D0` / `AKA0  =5.5D0`. | 일치 | 자연로그 법칙을 마찰속도에 대해 푼다. y는 벽에서 셀 중심까지 거리이다. |
| KF1-062 | p.21 Perfect rough surface의 무번호식·\(k_s\)·\(A+3.0\). `摩擦速度` 뜻: 마찰속도. 3D manual p.20과 같다. | 2F vf_clogks.f:30–31 `XX=LOG(DL/BKS)/AKK0+AKA0+3.0D0` / `VT=VA/XX`. | 일치 | 3.0을 유지한다. 벽 거칠기를 BKS로 사용한다. |
| KF1-063 | p.21–22 Free surface, \(p_s=p_{GAS}\), 법선 연속식·영 기울기·외삽, 접선 영 기울기·외삽. 3D manual p.21과 같다. | 2F vf_v1cal.f:390–392의 C2F 주석은 KF1-019이다. vf_vmodif.f:328 `PP(I,J,K)=PP(I,J,K)-PT(I,J,K)/DTNOW`. | 불일치(A) | 3D의 자유수면 압력·속도 경계 설명이다. 2F는 기체와 액체를 같은 압력·속도 해석에 포함한다. 표면 셀을 기체 압력으로 직접 덮는 경계와 같지 않다. |
| KF1-064 | p.22, 벽 압력 경계를 φ로 표현한다는 주석·in 첨자 정의. | 2F vf_vmodif.f:123–124 `UU(I,J,K)=UU(I,J,K)+2.0D0*XX(4,I  )`<br>`     &                        *GGV(I  ,J,K)/GLV(I  ,J,K)*PT(I  ,J,K)*RI`. | 일치 | 문서의 압력 열은 절대압의 직접 조건이 아니다. |
| KF1-065 | p.23 표 0-2-2 값 지정·영 기울기의 k·ε·T·\(c_i\) 무번호식. 3D manual p.22와 같다. | 2F vf_bwss.f:85–90 `IF     (IB.EQ.1) THEN` / `BCS(L)=BCS(L)` / `ELSEIF (IB.EQ.2) THEN` / `BCS(L)=SC`; vf_bwke.f:72–77 `IF     (IBK.EQ.1) THEN` / `BCK(L,LGF)=BCK(L,LGF)` / `ELSEIF (IBK.EQ.2) THEN` / `BCK(L,LGF)=AKC`; :93–98는 ε 대응. | 일치 | 각 스칼라의 지정값 또는 내부값을 경계에 둔다. |
| KF1-066 | p.23 열·확산 유속과 열·물질전달 무번호식, \(q_{in},h,T_\infty,k_i,c_{i\infty}\). 3D manual p.22와 같다. | 2F vf_bwss.f:97–98 `H=GL/DL` / `BCS(L)=SC+BCSI(1,L)/H`; :106–107 `H=GL/DL` / `BCS(L)=(H*SC+BCSI(1,L)*BCSI(2,L))/(H+BCSI(1,L))`. | 불일치(C) | 유체 셀에서는 대응한다. :94–95 및 :103–104의 NF=8 분기는 BCS=0으로 덮는다. 표는 기체 쪽 예외를 적지 않는다. |
| KF1-067 | p.23 대수법칙·완전조면의 \(k_c=(u^*)^2/\sqrt{C_\mu},\varepsilon_c=(u^*)^3/(\kappa y)\). 3D manual p.22와 같다. | 2F vf_bwkelg.f:49–50 `CMR=1.0D0/SQRT(AKCMU)` / `CKR=1.0D0/AKK0`. 실제 AK·AE 대입은 보충 인용이다. | 일치 | 경계면 값 자체가 아니라 경계에 접한 셀 중심값을 설정한다. |
| KF1-068 | p.23 Emission boundary의 k·ε·T·\(c_i\) Sommerfeld 무번호식. 3D manual p.22와 같다. | 2F vf_bwss.f:110–112 `CD      -- プログラムエラー --` / `ELSE` / `CALL VF_A2ERR('VF_BWSS','P.G ERROR.')`. 뜻: 프로그램 오류. vf_bwke.f:87–89도 해당 오류이다. | 문서에만(D) | 스칼라 경계는 이 방사 분기를 구현하지 않는다. 전체 Simulators의 rg -i 검색과 결과는 §5의 검색 기록이다. 유속 방사 경계와 혼동하지 않는다. |
| KF1-069 | p.23 Free surface의 k·ε·T·\(c_i\) 법선 영 기울기. 3D manual p.22와 같다. | 2F vf_k1cal.f:181–182 `C2F   CALL VF_BSSS(AK,DBUF,NF)` / `C2F   CALL VF_BSSS(AE,DBUF,NF)`; vf_t1cal.f:105 `CALL VF_BSSS(TT,DBUF,NF)`; vf_s1cal.f:113 `CALL VF_BSSS(CC(1,1,1,LC),DBUF,NF)`. | 불일치(A) | 2F는 k·ε의 자유수면 복사를 끈다. T·농도의 복사는 남겼다. 네 스칼라를 같은 현재 경로라고 적으면 안 된다. |

### 2.3 시간 이산화와 운동량 이산화

| 행 ID | 문서 위치와 원문 | 코드 위치와 원문 | 판정 | 이유 |
|---|---|---|---|---|
| KF1-070 | p.25, 모델명 `CADMAS-SURF/3D-2FC`. | 2F vf_a1main.f:5 `CDT   VF_A1MAIN:CADMAS-SURF/3D-2Fのメインルーチン`. 뜻: 3D-2F 메인 루틴. | 불일치(B) | 같은 문서 표지·다른 본문과 달리 C가 붙었다. 이 한 글자로 별도 판을 선언하지 않는다. |
| KF1-071 | p.25 `3.1` (1)–(3)(5)(6), 엇갈림·가변 격자·보존형 제어체적·선형 및 면적 보간·Euler·압력 음해 SMAC. 3D manual p.23과 같다. p.26 그림 0-3-1은 \(f^n\)의 공간 이웃에서 \(f^{n+1}\)로의 시간 갱신이다. | 2F vf_a1main.f:40–44 `CD                              ( 2,I):dx=x(I+1)-x(I)` / `CD                              ( 3,I):cx=(dx(I)+dx(I-1))/2.0` / `CD                              ( 4,I):1.0/dx` / `CD                              ( 5,I):1.0/cx` / `CD                              ( 6,I):1.0/(dx(I)+dx(I-1))`. 뜻: 셀 폭·중심 간격·각 역수. vf_v1cal.f:369–372의 Poisson 호출은 보충 인용이다. | 일치 | 폭·보간·플럭스·압력 보정을 분리한다. 그림은 3D manual p.24와 같다. |
| KF1-072 | p.25 (4), `other than the advection term`을 중앙차분과 상류차분 설명에서 두 번 사용. | 2F vf_vflxdu.f:81–87의 상류·중앙 이류 및 중앙 점성식은 KF1-017·KF1-080이다. | 불일치(B) | 두 번째 other than은 같은 항의 두 처리를 모순되게 만든다. 비이류는 중앙, 이류는 선택식이라는 표 p.6과 대조한다. 3D manual p.23도 같은 문장이다. |
| KF1-073 | p.27 식 (3.1)–(3.2), Euler 양해법. 3D manual p.25와 같다. | 2F vf_seuler.f:53 `CC(I,J,K)=(G0*CC(I,J,K)+DTNOW*DS)/GGV(I,J,K)`. | 일치 | 고정 공극률에서는 \(G0=GGV\)이다. 새 값은 옛 값과 Δt·우변의 합이다. 움직이는 공극률의 차이는 KF1-210이다. |
| KF1-074 | p.27 식 (3.3), 비압축 연속식. 3D manual p.25와 같다. | 2F vf_vpdrdt.f:77 `IF(ISTATE.EQ.0) RETURN`; :156 `BB(I,J,K) = BB(I,J,K) + AVL*DRHODT(I,J,K)`. | 불일치(B) | p.9 식 (2.1)을 시간 이산화했다고 적지만 압축항을 누락했다. ISTATE=0 조건에서는 맞는다. 이 보고서는 p.61의 추가 유도를 이 범위 식으로 간주하지 않는다. |
| KF1-075 | p.27–28 식 (3.4)–(3.9), (3.15)–(3.17), Gx·Gy·Gz 및 임시 속도. 3D manual p.25–26과 같다. | 2F vf_veuler.f:147–152 `DU=( XX(5,I)*(FLUU(I,J,K)-FLUU(I-1,J,K))`<br>`     &            +YY(4,J)*(FLUV(I,J+1,K)-FLUV(I,J,K))`<br>`     &            +ZZ(4,K)*(FLUW(I,J,K+1)-FLUW(I,J,K))+QU(I,J,K))`<br>`UU(I,J,K)=(GV*UUO(I,J,K)+DTNOW*(DU+DRDTU))/GV0`. | 일치 | G에 시간항과 압력항 이외의 항을 모은 구조는 같다. 그 안의 압축항 부호는 KF1-025–027의 별도 불일치이다. |
| KF1-076 | p.27의 G 설명이 `\(G_x(u^n,v^n,w^n)\) and \(G_z(u^n,v^n,w^n)\)`만 나열. | 2F vf_veuler.f:213–215 `DV=( XX(4,I)*(FLVU(I+1,J,K)-FLVU(I,J,K))`<br>`     &            +YY(5,J)*(FLVV(I,J,K)-FLVV(I,J-1,K))`<br>`     &            +ZZ(4,K)*(FLVW(I,J,K+1)-FLVW(I,J,K))+QV(I,J,K))`. | 불일치(B) | 같은 쪽 식 (3.5)·(3.8)에는 Gy가 있다. 본문 열거에서 Gy가 빠졌다. 3D manual p.25도 같다. |
| KF1-077 | p.28–29 식 (3.10)–(3.13), (3.19)–(3.22), p.40 식 (3.91)–(3.94). 3D manual p.26–27·38과 같다. | 2F vf_vmodif.f:110–111 `UU(I,J,K)=UU(I,J,K)`<br>`     &                      +XX(5,I)*GV*(PT(I,J,K)-PT(I-1,J,K))*RI`; :328 `PP(I,J,K)=PP(I,J,K)-PT(I,J,K)/DTNOW`. | 불일치(F) | 일정 밀도 ρ에서는 코드의 \(\psi=PT=\rho\phi\)로 두면 문서 보정식과 같다. 변수밀도 일반화는 KF1-205이다. 문서 φ와 코드 PT를 같은 단위라고 적지 않는다. |
| KF1-078 | p.28 식 (3.14)의 첫 y 발산항 \(\partial(\gamma_vv^{n+1})/\partial y\). 3D manual p.26과 같은 오기이다. | 2F vf_vpcoef.f:422 `     &           +AXZ*(GGY(I,JP,K)*VV(I,JP,K)-GGY(I,J,K)*VV(I,J,K))`. 전체 식은 KF1-023이다. | 불일치(B) | 면적투과율 γy가 들어갈 자리에 체적 공극률 γv를 적었다. 같은 문서 식 (3.3)·(3.18)은 γy이다. |
| KF1-079 | p.28 식 (3.18), p.37–39 식 (3.72)–(3.90)의 비압축 압력 Poisson 골격. 3D manual p.26·35–37과 같다. | 2F vf_v1cal.f:357–360 `CALL VF_VPDRDT(WK01,WK02,WK03,WK04,WK05,WK06,WK07,WK08,`<br>`     &               RHOG,RHOGO,DRHODP,DRHODT,`<br>`     &               UU,VV,WW,FF,`<br>`     &               GGV,GGX,GGY,GGZ,GLV,XX,YY,ZZ,NF,INDC)`. | 불일치(B) | 압축성 기본식의 완전한 이산식으로 읽으면 밀도 변화 행렬이 빠진다. 비압축 단계의 골격으로만 사용할 수 있다. p.1–60 안에서는 이 추가 행렬을 유도하지 않는다. |
| KF1-080 | p.29 식 (3.23)–(3.28)의 6개 격자 간격, p.30 식 (3.29)–(3.32)의 선형·면적·면에서 중심·이중 보간. 3D manual p.27–28과 같다. | 2F vf_vgene.f:101–103 `RHO02 = XX(6,I)*( XX(2,I )*RHOG(I ,J,K)`<br>`     &                         +XX(2,I1)*RHOG(I1,J,K))`<br>`RI=1.0D0/(FX(I,J,K)*RHO0(1)+(1.0D0-FX(I,J,K))*RHO02)`; vf_vflxdu.f:122–126의 이중 선형 보간은 보충 인용이다. | 일치 | XX·YY·ZZ의 2·3·4·5·6 성분이 Δ·δ 및 역수에 대응한다. 같은 쪽의 중복 예문은 계산식을 바꾸지 않는다. |
| KF1-081 | p.30 식 (3.33), \(\langle c\mid a,b\rangle=\{ca:(c\ge0),cb:(c<0)\}\). 3D manual p.28과 같다. | 2F vf_sconvd.f:82–85 `FLCU(I,J,K)=FLCU(I,J,K)`<br>`     &                      -SU*( MAX( WIN,0.0D0)*CC(I-1,J,K)`<br>`     &                           -MAX(-WIN,0.0D0)*CC(I  ,J,K))`<br>`     &                      -SC*FLC`. | 일치 | SU=1일 때 부호별 상류 선택이다. 셀 중심값은 왼쪽이 i-1이고 오른쪽이 i이다. |
| KF1-082 | p.31 그림 0-3-2, 스칼라 및 x 속도의 제어체적·각 3방향 플럭스. 오른쪽 폭 \(\Delta y_i\). 3D manual p.29도 같다. | 2F vf_veuler.f:148 `     &            +YY(4,J)*(FLUV(I,J+1,K)-FLUV(I,J,K))`. 전체 식은 KF1-075이다. | 불일치(B) | y 방향 폭 첨자는 j이다. 그림의 i는 식 (3.24)와 모순이다. 그림의 플럭스 위치는 코드와 대응한다. |
| KF1-083 | p.31–32 제어체적의 유입·유출·생성·소멸 절차, 식 (3.34)–(3.36)의 세 운동량 재배열. 3D manual p.29–30과 같다. | 2F vf_veuler.f:147–152·213–218·279–284의 플럭스 발산과 QU·QV·QW. 원문은 KF1-075·076 및 보충 인용이다. | 일치 | 플럭스와 셀 소스로 분리한다. 각 원문 오기와 압축항 부호는 별도 행으로 분리한다. |
| KF1-084 | p.32 식 (3.36)의 y 방향 이류 플럭스 \(-\lambda_yuw\). 3D manual p.30에도 같다. | 2F vf_vflxdw.f의 y 플럭스는 \(v w\)이다. :269–271의 원문은 보충 인용이다. | 불일치(B) | z 운동량의 y 수송 속도는 v이다. 같은 문서 식 (2.4)와 p.36 FLWV 정의는 \(\lambda_yvw\)이다. |
| KF1-085 | p.32 식 (3.37), VOF의 Euler 재배열. 3D manual p.30과 같다. | 2F vf_feuler.f:48–52는 KF1-033의 전체 식이다. | 일치 | 고정 공극률·비활성 조파원에서 같다. dt는 VOF 플럭스 내부에 들어간다. |
| KF1-086 | p.32–34 식 (3.38)–(3.48), FLUU·FLUV·FLUW·QU 정의, x 상류 이류·점성·압력·감쇠·저항·조파원. 3D manual p.30–32와 같다. | 2F vf_vflxdu.f:86–87 `FLUU(I,J,K)=FLUU(I,J,K)+(GGX(I,J,K)+GGX(I+1,J,K))`<br>`     &                      *ANU(I,J,K)*XX(4,I)*(UU(I+1,J,K)-UU(I,J,K))`; :127–129 `D1=YY(5,J)*(UU(I,J,K)-UU(I  ,J-1,K))` / `D2=XX(5,I)*(VV(I,J,K)-VV(I-1,J  ,K))` / `FLUV(I,J,K)=FLUV(I,J,K)+GG*AN*(D1+D2)`. | 일치 | 기본 SCMVP=1에서 (3.39)·(3.41)·(3.43)의 상류 부분과 일치한다. 대각 점성 (3.40)과 교차 미분의 간격은 대응한다. 보간 기호와 비활성 조파원은 KF1-087·089이다. |
| KF1-087 | p.33–36 식 (3.41)–(3.44), (3.50)–(3.51), (3.54)–(3.55), (3.61)–(3.64)의 면적 보간 바닥괄호. 3D manual p.31–34에도 같은 표기. | 2F vf_vflxdu.f:112–113 `WIN=XX(6,I)*( XX(2,I-1)*GLY(I  ,J,K)*VV(I  ,J,K)`<br>`     &                     +XX(2,I  )*GLY(I-1,J,K)*VV(I-1,J,K))`; :121 `GG=XX(6,I)*(XX(2,I-1)*GGY(I,J,K)+XX(2,I)*GGY(I-1,J,K))`. | 불일치(B) | p.30 식 (3.30)의 바닥괄호는 같은 쪽 폭을 가중한다. 코드는 반대쪽 폭으로 선형 보간한다. 비균등 격자에서 차이가 난다. 동일 폭에서는 소거된다. ν의 이중 선형 보간은 별개로 대응한다. |
| KF1-088 | p.33·35·36–37 식 (3.45)·(3.56)·(3.67)의 압력 구배, (3.46)·(3.57)·(3.68)의 새 속도 감쇠. 3D manual p.31·33–35와 같다. | 2F vf_vgene.f:112–113 `QU(I,J,K)=QU(I,J,K)`<br>`     &                    +GV*RI*XX(5,I)*(PP(I1,J,K)-PP(I,J,K))`; vf_veuler.f:192–193 `D=GV0/(GV0+DTNOW*G*DMAX)` / `UU(I,J,K)=UU(I,J,K)*D`. | 일치 | 압력 구배의 음 부호와 감쇠 음해 처리가 대응한다. 2F의 면 혼합 역밀도는 KF1-205이다. |
| KF1-089 | p.34·35·37 식 (3.48)·(3.59)·(3.70), 조파원 양면 분배·q의 z 차분·ν/3. 3D manual p.32·33·35와 같다. | 2F vf_vgene.f:132 `CAKIY         * 造波ソース`; :182 `CD            * 造波ソース`; :232 `CD            * 造波ソース`. 뜻: 조파원. 각 위치 뒤에 조파 소스 대입이 없다. | 불일치(A) | 3D의 조파원 설명이 남았으나 2F는 계산을 제거했다. p.14 Unused를 적용한다. |
| KF1-090 | p.34–35 식 (3.49)–(3.58), FLVU·FLVV·FLVW·QV의 정의. 3D manual p.32–33과 같다. | 2F vf_veuler.f:213–218은 KF1-076이다. vf_vflxdv.f:288–290 `D1=ZZ(5,K)*(VV(I,J,K)-VV(I,J  ,K-1))` / `D2=YY(5,J)*(WW(I,J,K)-WW(I,J-1,K  ))` / `FLVW(I,J,K)=FLVW(I,J,K)+GG*AN*(D1+D2)`. | 일치 | y 속도의 갱신 위치·정상응력 계수 2·상류 방향은 대응한다. (3.55)·(3.58)의 오류는 다음 두 행이다. |
| KF1-091 | p.35 식 (3.54)–(3.55)의 λzw·γz 보간 위첨자 \(\Delta z\), ν 안쪽 보간 위첨자 \(\Delta x\), (3.55)의 마지막 분모 \(\delta y_i\). 3D manual p.33의 해당 식과 비교한다. | 2F vf_vflxdv.f:273–274 `WIN=YY(6,J)*( YY(2,J-1)*GLZ(I,J  ,K)*WW(I,J  ,K)`<br>`     &                     +YY(2,J  )*GLZ(I,J-1,K)*WW(I,J-1,K))`; :282 `GG=YY(6,J)*(YY(2,J-1)*GGZ(I,J,K)+YY(2,J)*GGZ(I,J-1,K))`; :288–290은 KF1-090이다. | 불일치(B) | λzw·γz는 y 방향으로 보간해야 한다. ν는 z·y의 이중 보간이어야 한다. 마지막 분모는 δyj이다. 두 매뉴얼의 원해상도 이미지에는 같은 전단 미분과 두 분수 사이 더하기가 있다. 그 두 항목을 불일치로 세지 않는다. |
| KF1-092 | p.35 식 (3.58)의 저항계수 분모 \(\delta y_j\). 3D manual p.33과 같다. 루트 안에는 \(v_{i,j,k}^{2}\)가 인쇄되어 있다. | 2F vf_vgene.f:172·175–177 `V=VV(I,J,K)` / `UVW=SQRT(U*U+V*V+W*W)` / `QV(I,J,K)=QV(I,J,K)`<br>`     &                  -0.5D0*CD*YY(5,J)*(1.0D0-GGY(I,J,K))*V*UVW`. | 일치 | 원해상도 이미지의 분모는 δyj이다. 속도 크기 안의 세 제곱도 코드와 같다. |
| KF1-093 | p.36–37 식 (3.60)–(3.71), FLWU·FLWV·FLWW·QW의 정의. 3D manual p.34–35와 같다. 두 매뉴얼의 원해상도 이미지에서 (3.62)의 두 분수 사이 더하기를 확인했다. | 2F vf_vflxdw.f:121–123 `D1=XX(5,I)*(WW(I,J,K)-WW(I-1,J,K  ))` / `D2=ZZ(5,K)*(UU(I,J,K)-UU(I  ,J,K-1))` / `FLWU(I,J,K)=FLWU(I,J,K)+GG*AN*(D1+D2)`; vf_veuler.f:279–284는 보충 인용이다. | 일치 | 전단의 합은 코드와 같다. z 속도 제어체적과 zz 정상응력도 대응한다. 상세 오기·소스·부력 차이는 따로 판정한다. |
| KF1-094 | p.36 식 (3.65)의 평균 위첨자 \(\delta w\). p.37 식 (3.69)의 루트 앞 \(v_{i,j,k}\). 3D manual p.34–35도 같다. | 2F vf_vflxdw.f:73–74 `WIN=( GLZ(I,J,K  )*WW(I,J,K  )`<br>`     &             +GLZ(I,J,K+1)*WW(I,J,K+1))*0.5D0`; vf_vgene.f:224–227 `W=WW(I,J,K)` / `UVW=SQRT(U*U+V*V+W*W)` / `QW(I,J,K)=QW(I,J,K)`<br>`     &                  -0.5D0*CD*ZZ(5,K)*(1.0D0-GGZ(I,J,K))*W*UVW`. | 불일치(B) | 각각 δz·w가 되어야 한다. 같은 문서 (2.6), 격자 정의, z 운동량과 모순이다. (3.64)의 분모는 원해상도 이미지에서 δyj로 확인했다. |
| KF1-095 | p.9 식 (2.4) 및 p.37 식 (3.71), \(-\gamma_v\rho^*g/\rho\)의 부력. 3D manual p.10·35와 같다. | 2F vf_vgene.f:235 `QW(I,J,K)=QW(I,J,K)-GV*GRZ0`; :241 `DR=DR-TDR0*(T-TDT0)`; :245 `DR=DR-CDR0(LC)*(C-CDC0(LC))`; :248 `QW(I,J,K)=QW(I,J,K)-GV*GRZ0*DR/RHO0(1)`. | 불일치(C) | 코드는 온도·농도 기준값에 대한 선형 밀도차와 액상 기준밀도 RHO0(1)를 사용한다. 문서는 \(\rho^*\)만 정의한다. 농도를 유동에 영향이 없다고 한 p.18 조건은 CDR0=0일 때만 유지된다. |

### 2.4 압력 행렬

| 행 ID | 문서 위치와 원문 | 코드 위치와 원문 | 판정 | 이유 |
|---|---|---|---|---|
| KF1-096 | p.37 식 (3.72)–(3.76), p.38 식 (3.77)–(3.78), 6면 체적적분·중심 간 차분. 3D manual p.35–36과 같다. | 2F vf_vpcoef.f:156–159 `AXY=XX(2,I)*YY(2,J)` / `AXZ=XX(2,I)*ZZ(2,K)` / `AYZ=YY(2,J)*ZZ(2,K)` / `AVL=XX(2,I)*YY(2,J)*ZZ(2,K)`; :173 `AIM=AYZ*XX(5,I)*GGX(I,J,K)*GV*RI`. | 일치 | 면적·중심 간 역간격을 사용한다. 문서의 대칭성 유지는 비압축 확산 골격에 한정한다. 압축 이류 행렬 전체의 대칭성을 보장하지 않는다. |
| KF1-097 | p.38 식 (3.79)–(3.86), 7점 행렬·6개 이웃계수·대각 음의 합. 3D manual p.36과 같다. | 2F vf_vpcoef.f:174 `ALI(I,J,K)=-AIM`; :418 `AD(I,J,K)=AKM+AJM+AIM+AIP+AJP+AKP`; :430 `BB(I,J,K)=VD-VQ`. | 불일치(F) | 일정 밀도에서 \(A_c=-A_d/\rho\), \(B_c=-B_d\), \(PT=\rho\phi\)이다. 따라서 \(A_cPT=B_c\)는 문서 선형계와 동치이다. 변수밀도와 압축 증강은 KF1-205·204이다. |
| KF1-098 | p.38 식 (3.79)의 \(A^D_{i,j,.k}\), (3.81)–(3.84)의 \(\Delta z_z\). 3D manual p.36도 같은 z 첨자 오류를 갖는다. | 2F vf_vpcoef.f:157–158 `AXZ=XX(2,I)*ZZ(2,K)` / `AYZ=YY(2,J)*ZZ(2,K)`. | 불일치(B) | 미정의 z 첨자와 불필요한 점이다. 같은 문서 p.37의 면적은 \(\Delta z_k\)이다. |
| KF1-099 | p.38 식 (3.87)–(3.89), \(\alpha_x,\alpha_y,\alpha_z\). 3D manual p.36과 같다. | 2F vf_vpcoef.f:165–166 `GV=XX(6,I)*( XX(2,I )*GGV(I ,J,K)/GLV(I ,J,K)`<br>`     &                      +XX(2,IM)*GGV(IM,J,K)/GLV(IM,J,K))`; :173 `AIM=AYZ*XX(5,I)*GGX(I,J,K)*GV*RI`. | 불일치(F) | 일정 밀도에서는 PT=ρφ로 정규화한 α/ρ이다. 2F의 변수밀도 혼합은 KF1-205에서 별도로 다룬다. |
| KF1-100 | p.39 식 (3.90)의 y 발산 분모 \(\Delta y_k\). p.39는 이 식만 있음. 3D manual p.37도 같다. | 2F vf_vpcoef.f:421–423의 VD는 KF1-023이다. :157 `AXZ=XX(2,I)*ZZ(2,K)`. | 불일치(B) | 셀 체적을 \(\Delta y_j\)로 나눈 면적 AXZ가 사용된다. y 폭의 첨자는 j이다. |
| KF1-101 | p.40 식 (3.91)–(3.94)의 x·y·z 속도와 압력 보정. 3D manual p.38과 같다. | 2F vf_vmodif.f:198–199 `VV(I,J,K)=VV(I,J,K)`<br>`     &                      +YY(5,J)*GV*(PT(I,J,K)-PT(I,J-1,K))*RI`; :328 `PP(I,J,K)=PP(I,J,K)-PT(I,J,K)/DTNOW`. x 식은 KF1-077이다. z 식은 보충 인용이다. | 불일치(F) | KF1-077의 같은 PT=ρφ 변환이다. RI를 문서 φ식에 없다는 이유만으로 코드 오류로 분류하지 않는다. |

### 2.5 VOF 분류·donor–acceptor·기울기 재구성

| 행 ID | 문서 위치와 원문 | 코드 위치와 원문 | 판정 | 이유 |
|---|---|---|---|---|
| KF1-102 | p.40–41, NF=0 유체, 1·2 x 음·양, 3·4 y 음·양, 5·6 z 음·양, 8 기체. 3D manual p.38–40과 같다. | 2F vf_fnfini.f:39 `IF (NF(I,J,K).GT.-1) NF(I,J,K)=0`; :92 `NF(I,J,K)=8`; vf_fnfprv.f:104 `IF (NF(I,JB,K).EQ.0 .AND. NF(I,J+1,K).EQ.8) THEN`; :127 `NF(I,J,K)=3`. 모든 방향 대입은 보충 인용이다. | 일치 | NF 방향은 액체가 있는 쪽이다. 원문은 NF의 Fortran 형·배열 크기를 이 쪽에서 선언하지 않는다. |
| KF1-103 | p.42 절차 ①–⑦, F=0을 기체로 분류, 유체·기체 사이의 표면만 남김. 3D manual p.39–40과 같다. | 2F vf_fnfini.f:49 `IF (FF(I,J,K).LT.FLOWER) THEN`; :86–92의 FUPPER 이웃 검사; :118–123의 기체 인접 검사; :141–144의 유체 인접 검사; :189 `IF (NF(I,J,K).EQ.-7) NF(I,J,K)=8`; :194 `GOTO 1000`. | 불일치(C) | 실제 F=0 판정은 FLOWER 미만이다. FUPPER를 넘는 유체 이웃 검사도 있다. 중간 NF=7·-7과 전역 통신을 문서는 생략한다. |
| KF1-104 | p.41–44 그림 0-3-3의 반복 격자 그림, 유체에 둘러싸인 \(0<F<1\) 셀은 표면이 아님. p.43 유일 배열·주변 F가 큰 방향 선택. 3D manual p.39–41과 같다. | 2F vf_fnfprv.f:105 `FS=2.0D0*FF(I,JB,K)`; :126–129 `IF (FS.GT.FM) THEN` / `NF(I,J,K)=3` / `FM=FS` / `ENDIF`. | 일치 | 중심 이웃에 가중치 2와 주변 값을 더해 방향을 고른다. p.43의 ①·② 반복은 새 알고리즘이 아니다. |
| KF1-105 | p.43, 격자보다 작은 물방울·기포 무시·안정성을 위한 불가피한 처리. p.6 TimerDoor. | 2F vf_f1cal.f:190 `CALL VF_FNFINI(FF,BCF,NF,INDX,INDY,INDZ,INDS,IBUF)`; :192 `CALL VF_FBUBUP(ZZ,FF,GGV,TBUB,DBUF,NF)`; :196–198의 VF_FDROPF 전체 호출은 보충 인용이다. | 불일치(C) | NF의 표면 제외와 물방울·기포 제거는 같은 동작이 아니다. 실제로 TimerDoor 보조 처리와 재분류가 존재한다. 문서의 안정성 성능 주장은 코드로 검증하지 않는다. |
| KF1-106 | p.44 식 (3.95), FLFU·FLFV·FLFW·ΔtQF, 플럭스에 Δt 포함. 3D manual p.41과 같다. | 2F vf_feuler.f:48–52의 전체 식은 KF1-033이다. | 일치 | 정지 공극률일 때 같은 식이다. p.44의 고립된 `v`를 플럭스 변수로 해석하지 않는다. |
| KF1-107 | p.45 식 (3.96), 무번호식 FLFU·CFX·C·FAD·FDM·양/음 C의 DMW·D·A. 3D manual p.42와 같다. | 2F vf_fconv.f:58–69 `C=DTNOW*GGX(I,J,K)*UU(I,J,K)` / `AC=ABS(C)` / `IF (C.GE.0.0D0) THEN` / `LSN=1` / `LA =I` / `LD =I-1` / `LDM=I-2` / `ELSE` / `LSN=-1` / `LA =I-1` / `LD =I` / `LDM=I+1`; :94–97 `CFX=MAX((FDM-FAD)*AC-(FDM-FD)*V,0.0D0)` / `FVX=FAD*AC+CFX` / `FVM=FD*V` / `FLFU(I,J,K)=FLFU(I,J,K)-DBLE(LSN)*MIN(FVX,FVM)`. | 일치 | Cの符号에 따른 상류 셀과 도너 보유량 제한이 같다. 한국어로는 C 부호에 따른 선택이다. 경계·작은 F 예외는 KF1-212이다. |
| KF1-108 | p.45 식 (3.97), 무번호식 \(QF=S_F\), \(S_F=Fq\). 3D manual p.42와 같다. | 2F vf_f1cal.f:123 `QF  (I,J,K)=0.0D0`; :143 `CAKIY CALL FGENE(XX,ZZ,FF,WVU,QF,NF)`. | 불일치(A) | 조파원 비활성이다. |
| KF1-109 | p.46 그림 0-3-4(a)의 흐름별 DMW·D·A, (b)의 세 `Let suffix AD be D`. 그림·부분 캡션만 있음. 3D manual p.42–43도 같다. | 2F vf_fconv.f:87–90 `FAD=FA`<br>`IF (N.EQ.-1 .OR. N.EQ.3 .OR. N.EQ.4`<br>`     &                    .OR. N.EQ.5 .OR. N.EQ.6) THEN`<br>`IF (FDMW.NE.0.0D0 .AND. FA.NE.0.0D0) FAD=FD`. | 불일치(B) | 풍하 그림 두 칸은 A를 써야 p.45의 FAD 정의와 맞는다. 세 칸 전부 D라는 그림 문구는 틀리다. 흐름별 첨자 배치는 맞는다. |
| KF1-110 | p.47 그림 0-3-4(c), 무번호식 \(C=\Delta t\gamma_xu\), \(\mathrm{Transfer\ flow\ rate}=\min(F_{AD}CS,F_D\Delta x_D\gamma_{vD}S)\). S는 면적. 그림·캡션만 있음. 3D manual p.43과 같다. | 2F vf_fconv.f:76 `V=XX(2,LD)*GGV(LD,J,K)`; :95–97의 MIN 식은 KF1-107이다. | 일치 | 그림은 양의 C인 설명도이다. 일반식의 절댓값·CFX는 p.45에 있다. 코드 플럭스는 면적당 체적이며 면적 S는 발산 적분에서 처리한다. |
| KF1-111 | p.48–49 절차 ①법선 ②패턴 ③계면 ④이류량, 기울기는 F 이류에 적용, 속도·압력은 기존 방법, 설명은 2차원. 그림 0-3-5. 3D manual p.44와 같다. | 2F vf_fconvs.f:366–368 `CALL VF_FSLP2A(SX(I,J,K),SY(I,J,K),`<br>`     &                         XX(2,I)  ,YY(2,J)  ,`<br>`     &                         FF(I,J,K),SA(I,J,K) )`; :378–380 `CALL VF_FSLP3A(SX(I,J,K),SY(I,J,K),SZ(I,J,K),`<br>`     &                         XX(2,I)  ,YY(2,J)  ,ZZ(2,K)  ,`<br>`     &                         FF(I,J,K),SA(I,J,K)           )`. | 일치 | 2차원 선분과 3차원 평면 재구성 분기가 실제 존재한다. |
| KF1-112 | p.49 식 (3.98)–(3.99), 셀 중심에서 \(-\partial F/\partial x,-\partial F/\partial z\). p.50 그림 0-3-6의 셀 중심·격자점 비교. 3D manual p.45와 같다. | 2F vf_fconvs.f:335–338 `IF (DM+DP.LE.ZERO) THEN` / `S3=0.0D0` / `ELSE` / `S3=(FM-FP)/(DM+DP)`. | 불일치(C) | 일반 이웃에서는 같은 중심 차분이다. 벽·기체·유체 상태별 FM·FP·DM·DP 보정과 단위 법선 정규화를 문서가 생략한다. 단위와 임계값은 KF1-213이다. |
| KF1-113 | p.50 그림 0-3-7·0-3-8, 무번호 \(ISW=1,-1\), \(n_x=-n_x,n_z=-n_z,ISW=-ISW\) 및 양의 법선으로 반사. 3D manual p.46과 같다. | 2F vf_fconvs.f:446–449 `LSW=LSN` / `IF (SX(LD,J,K).LT.0.0D0) LSW=-LSW` / `DD0=AC` / `IF (LSW.EQ.1) DD0=XX(2,LD)-AC`; vf_fslp2a.f:30–31 `SS(1)=ABS(SX)` / `SS(2)=ABS(SY)`. | 일치 | 코드 LSW가 문서의 이류 방향 ISW에 대응한다. 코드 ISW는 별도로 ISTYP의 패턴 번호를 담는다. 두 변수를 동일시하지 않는다. |
| KF1-114 | p.51 그림 0-3-9의 무번호식 3개와 p.53 식 (3.100), \(n_1c_1+n_2c_2=\alpha\), 두 절편식·\(\alpha\ge0\). 3D manual p.47·49와 같다. | 2F vf_fslp2a.f:45–50 `CNS=2.0D0*SS(1)*SS(2)` / `XMX=SD(1)+SD(2)` / `VMX=DD(1)*DD(2)*CNS` / `VIN=VMX*FVAL` / `XL=0.0D0` / `XR=SD(L1)`. | 일치 | 셀 유체량으로 평면 상수를 정한다. \(\alpha\)는 코드 AA이다. 그림 속 A–H는 기하 점이며 행렬 계수가 아니다. |
| KF1-115 | p.51 그림 0-3-10의 \(n_1<\varepsilon,n_2<\varepsilon\), \(n_2<\varepsilon\), \(n_1<\varepsilon\)일 때 donor–acceptor. 3D manual p.47과 같다. | 2F vf_fconvs.f:351–355 `IF (ABS(S1).GE.1.0D-4) I1=1` / `IF (ABS(S2).GE.1.0D-4) I2=1` / `IF (ABS(S3).GE.1.0D-4) I3=1` / `IF (I1+I2+I3.GE.2) THEN` / `ISTYP(I,J,K)=I1+2*I2+4*I3`. | 불일치(C) | 문서는 ε 수치를 제시하지 않는다. 코드는 정규화된 성분에 10⁻⁴를 적용한다. |
| KF1-116 | p.52–53 여섯 패턴 P1-1·P1-2·P1-3·P2-1·P2-2·P2-3, \(n_1\Delta C_1\le n_2\Delta C_2\) 및 반대 조건, 무번호 Vlim·Vgive 비교와 H1·H2. 3D manual p.48–49와 같다. | 2F vf_fslp2a.f:34–41 `SD(1)=SS(1)*DX` / `SD(2)=SS(2)*DY` / `IF (SD(1).LE.SD(2)) THEN` / `L1=1` / `L2=2` / `ELSE` / `L1=2` / `L2=1`; :55 `IF (VIN.LE.VV) THEN`; :66 `IF (VIN.LE.VV) THEN`. | 일치 | 축을 정렬하고 낮은·중간·높은 체적 구간을 나눈다. H1=H2=0, (1,0)/(0,1), (1,1)에 해당한다. |
| KF1-117 | p.52 두 번째 `P1-1` 제목은 D를 지나고 Vgive>Vlim일 때 P1-3이라고 설명한다. `P1-2：P1-1 および P1-3 のパターンでなければ P1-2 である．後に必要となる値は`. 뜻: P1-1·P1-3이 아니면 P1-2이고 필요한 값은 다음과 같음. | 2F vf_fslp2a.f:70–75 `XL=XR` / `XR=XMX` / `Q =SD(L2)` / `A =A-1.0D0` / `B =B+2.0D0*Q` / `C =C-Q*Q`. | 불일치(B) | 두 번째 제목은 P1-3이어야 한다. 일본어 문장은 (H1,H2)=(1,0)을 뜻한다. 같은 쪽 깨진 그림 참조도 편집 오류이다. |
| KF1-118 | p.53 식 (3.101) V(α)의 전개 중 한 줄 분모 \(2n_1\eta_2\). 나머지 전개와 p.54 무번호 A·B·C는 \(2n_1n_2\). 3D manual p.49에도 같은 η2가 있다. | 2F vf_fslp2a.f:45 `CNS=2.0D0*SS(1)*SS(2)`; :62–65 `A =A-1.0D0` / `B =B+2.0D0*Q` / `C =C-Q*Q` / `VV=A*XR*XR+B*XR+C`. | 불일치(B) | 미정의 η2는 n2의 오기이다. 문서 내부의 앞·뒤 동치식만으로 판별한다. |
| KF1-119 | p.53 식 (3.101)–(3.102), p.54 무번호 A·B·C 계수와 `の 2 次方程式を解くことで，α を決定することができる．`. 뜻: 이차방정식을 풀어 α를 정할 수 있음. p.54는 계수와 이 문장만 있음. 3D manual p.49와 같다. | 2F vf_fslp2a.f:45–48 `CNS=2.0D0*SS(1)*SS(2)` / `XMX=SD(1)+SD(2)` / `VMX=DD(1)*DD(2)*CNS` / `VIN=VMX*FVAL`; :56–57 `CX=C-VIN` / `CALL VF_CROOT2(A,B,CX,XX1,XX2,NRT)`. | 불일치(F) | 코드는 양변에 \(2n_1n_2\)를 곱한 계수이다. A·B·C의 모양은 달라도 같은 다항식이다. 구간별 해 선택과 실패 보정은 KF1-214이다. |
| KF1-120 | p.55 식 (3.103)의 ISW별 c1, 식 (3.104)–(3.109)의 삼각형·보영역·사다리꼴 면적과 유출량 선택. p.56은 (3.109)만 있음. 3D manual p.50과 같다. | 2F vf_fconvs.f:448–449 `DD0=AC` / `IF (LSW.EQ.1) DD0=XX(2,LD)-AC`; :466–470 `VG=XX(2,LD)*FF(LD,J,K)` / `FVX=DFF*DD0` / `IF (LSW.EQ.1) FVX=VG-FVX` / `VG=VG*GGV(LD,J,K)` / `FLFU(I,J,K)=FLFU(I,J,K)-DBLE(LSN)*MIN(FVX,VG)`. | 일치 | 면적 함수를 축 정렬로 평가한다. 방향별 보영역 선택이 대응한다. 공극률 상한은 KF1-215이다. |
| KF1-121 | p.55·57 식 (3.104)·(3.106)·(3.110)은 조건의 P와 면적식의 p를 혼용한다. 3D manual p.50–51도 같다. | 2F vf_fslp2f.f:51–52 `ELSEIF (AA.LE.SD(L1)) THEN` / `VV=A*AA*AA`. | 불일치(B) | 압력 p가 아닌 같은 기하 절편이다. p와 P를 구별하는 정의가 없다. 기하·같은 식의 조건으로 오기를 판별한다. |
| KF1-122 | p.57 식 (3.110)의 \(p_0\ge c_1:V_*=V_{give}-p_0\Delta c_2\), 식 (3.111)의 방향별 Vflx. 그림 0-3-12(d). 3D manual p.51도 같다. | 2F vf_fconvs.f:467–468 `FVX=DFF*DD0` / `IF (LSW.EQ.1) FVX=VG-FVX`; vf_fslp2f.f:58–59 `IF (AA.LE.SD(L2)) THEN` / `VV=A*AA*AA+B*AA+C`. | 불일치(B) | p0 아래에서는 왼쪽 띠 면적이 c1·Δc2이다. 인쇄식은 p0·Δc2로 고정하여 c1=0에서도 전체 유체량을 반환하지 않는다. 문서 자체 그림과 면적 계산으로 판별한다. |

### 2.6 난류·온도·농도 이산화

| 행 ID | 문서 위치와 원문 | 코드 위치와 원문 | 판정 | 이유 |
|---|---|---|---|---|
| KF1-123 | p.57–58 식 (3.112)–(3.113), k·ε의 발산·소스 갱신. 3D manual p.51–52와 같다. | 2F vf_k1cal.f:152–153의 VF_SEULER 호출은 KF1-042이다. vf_seuler.f:50–53의 전체식은 KF1-129이다. | 일치 | 비압축 스칼라 골격은 같다. p.17의 추가 압축항 미구현은 KF1-042이다. |
| KF1-124 | p.58 식 (3.113), FLEV 차분의 분모 \(\Delta y_i\). 3D manual p.52도 같다. | 2F vf_seuler.f:51 `     &            +YY(4,J)*(FLCV(I,J+1,K)-FLCV(I,J,K))`. 전체 식은 KF1-129이다. | 불일치(B) | y 간격은 j 첨자이다. 바로 앞 (3.112)도 j를 쓴다. |
| KF1-125 | p.58 무번호 FLKU 정의, 식 (3.114)–(3.115)의 상류 k 플럭스·선형 점성 보간. k·ε는 중심이며 방향 변경은 첨자 교체. 3D manual p.52와 같다. | 2F vf_k1cal.f:109–112 `CALL VF_SCONVD(-1,XX,YY,ZZ,UU,VV,WW,AK,GGX,GGY,GGZ,BCK,`<br>`     &                 FLKU,FLKV,FLKW,NF,INDX,INDY,INDZ,INDC,INDBK)`<br>`CALL VF_SCONVD(-1,XX,YY,ZZ,UU,VV,WW,AE,GGX,GGY,GGZ,BCE,`<br>`     &                 FLEU,FLEV,FLEW,NF,INDX,INDY,INDZ,INDC,INDBE)`. | 일치 | SCMK=1의 기본 상류식이다. 확산은 FF 인수를 포함한 VF_SDIFF를 호출한다. |
| KF1-126 | p.58 식 (3.116)–(3.117), QK=γv(Gs−ε), QE=γv(C1 εGs/k−C2 ε²/k). 3D manual p.52와 같다. | 2F vf_kgene.f:174–182 `AK0=MAX(AK(I,J,K),AKMINK)` / `AE0=AE(I,J,K)` / `AEK=AE0/AK0` / `GG=GGV(I,J,K)` / `QK(I,J,K)=QK(I,J,K)+GG*(GST-AE0)`<br>`QE(I,J,K)=QE(I,J,K)+GG*( AKC1*AEK*GST*(1.0D0+AKC3*RF)`<br>`     &                                -AKC2*AEK*AE0                )`. | 불일치(C) | GT=0·AKC3=0·k≥AKMINK에서 같다. k 분모 하한과 갱신 후 컷오프는 문서 식에 없다. |
| KF1-127 | p.58 `A in the equations (3.116) and (3.117)`, 뒤의 \(G_{s_{i,k}}\). | 2F vf_kgene.f:161 `GS=ANUT(I,J,K)*(2.0D0*( DUDX*DUDX`. 전체 식은 KF1-043이다. | 불일치(B) | 두 문서 식에는 A가 없다. Gs 첨자는 i,j,k이다. 3D manual p.52도 같은 편집 오류이다. |
| KF1-128 | p.58–59 식 (3.118), Gs의 연속형과 3방향 이산형. 첫 \(v_y\)가 \((v_{i+1,j,k}-v_{i,j,k})/\Delta y_j\). 3D manual p.52–53도 같다. | 2F vf_kgene.f:151–154 `DLR=YY(4,J)` / `DUDY=DLR*(UYP-UYM)` / `DVDY=DLR*(VYP-VYM)` / `DWDY=DLR*(WYP-WYM)`; :161–166은 KF1-043이다. | 불일치(B) | y 법선 차분은 v의 j+1을 참조해야 한다. 나머지 세 전단 제곱과 2의 계수는 대응한다. |
| KF1-129 | p.59 식 (3.119), p.60 식 (3.123), T·c 중심의 Euler 보존형. 농도 성분 첨자 생략. 3D manual p.53–54와 같다. | 2F vf_seuler.f:49–53 `G0=GGV(I,J,K)-(GGV(I,J,K)-GGV0(I,J,K))*DBLE(LOOPS)`<br>`DS=( XX(4,I)*(FLCU(I+1,J,K)-FLCU(I,J,K))`<br>`     &            +YY(4,J)*(FLCV(I,J+1,K)-FLCV(I,J,K))`<br>`     &            +ZZ(4,K)*(FLCW(I,J,K+1)-FLCW(I,J,K))+QC(I,J,K))`<br>`CC(I,J,K)=(G0*CC(I,J,K)+DTNOW*DS)/GGV(I,J,K)`. | 일치 | 고정 공극률의 스칼라 갱신 골격이다. 개별 소스·압축항·호출 인수 오류는 별도 행이다. |
| KF1-130 | p.59 무번호 FLTU, 식 (3.120)–(3.121), p.60 무번호 FLCU, 식 (3.124)–(3.125)의 이류·확산. 3D manual p.53–54와 같다. | 2F vf_sconvd.f:82–85의 전체 이류식은 KF1-081이다. vf_sdiff.f:81–84 `D=XX(6,I)*(XX(2,I-1)*DD(I,J,K)+XX(2,I)*DD(I-1,J,K))` / `D=D*AL2`<br>`FLCU(I,J,K)=FLCU(I,J,K)`<br>`     &                +GGX(I,J,K)*D*XX(5,I)*(CC(I,J,K)-CC(I-1,J,K))`. | 일치 | 정상적인 VF_SDIFF 인수 대응을 전제로 한 플럭스 식이다. 온도 AL2는 두 상의 \(1/(\rho c_p)\)를 F로 혼합한다. 실제 T·c 호출의 인수 불일치는 KF1-206이다. |
| KF1-131 | p.60 식 (3.122), \(QT=(\rho c_pTq)_{i,j,k}\). 3D manual p.54와 같다. | 2F vf_t1cal.f:76 `QT  (I,J,K)=0.0D0`; :94 `CAKIY CALL VF_TGENE`; vf_seuler.f:53의 갱신은 KF1-129이다. | 불일치(B) | QT는 이미 온도 시간변화율의 단위여야 한다. p.18 식 (2.32)의 \(S_T/(\rho c_p)\)를 이산화하면서 그 분모와 γv를 반영하지 않았다. 조파원 비활성 자체는 KF1-052이다. |
| KF1-132 | p.18 식 (2.37) \(S_{c_i}=c_iq(z,t)\), p.60 식 (3.126) \(QC=(cq)_{i,j,k}\). 3D manual p.19·54와 같다. | 2F vf_s1cal.f:79 `QC  (I,J,K)=0.0D0`; :100 `CAKIY   CALL VF_SGENE`. 3D vf_s1cal.f:96도 `CAKIY   CALL VF_SGENE`이다. | 문서에만(D) | 두 코드 사본 모두 농도 소스를 계산하지 않는다. p.5의 Unused 표시를 함께 적용한다. 전체 Simulators의 검색 결과에는 주석 호출만 있다. |
| KF1-133 | p.59의 FLTU·FLTU 반복, p.60의 FLCU·FLCU 반복, `C`와 c 혼용, 그림 참조 `エラー! 参照元が見つかりません。`. 뜻: 오류! 참조 원본을 찾을 수 없습니다. | 2F vf_t1cal.f:73–76 `FLTU(I,J,K)=0.0D0` / `FLTV(I,J,K)=0.0D0` / `FLTW(I,J,K)=0.0D0` / `QT  (I,J,K)=0.0D0`; vf_s1cal.f:76–79의 FLCU·FLCV·FLCW·QC. | 불일치(B) | 실제 플럭스는 각 3방향이다. 단순 편집 오류이다. C와 c는 이 문맥에서 같은 농도이다. |

### 2.7 보충 항목

| 행 ID | 문서 위치와 원문 | 코드 위치와 원문 | 판정 | 이유 |
|---|---|---|---|---|
| KF1-134 | p.13, `interpolating in the time direction and spatial direction`. 사용자 matrix 자료의 수위·속도 보간이다. 3D manual p.13과 같다. | 2F vf_cwmtb1.f:43–45 `W2=1.0D0/(DMTBTT(I+1)-DMTBTT(I))` / `W1=(DMTBTT(I+1)-WVT)*W2` / `W2=(WVT-DMTBTT(I  ))*W2`; :68 `WVZ=W1*DMTBHH(MTBNOW)+W2*DMTBHH(MTBNOW+1)`; vf_cwmtb2.f:59–61 `P1=W1*DMTBUN(KM,IM )+W2*DMTBUN(KM1,IM )` / `P2=W1*DMTBUN(KM,IM1)+W2*DMTBUN(KM1,IM1)` / `UN=WT1*P1+WT2*P2`. | 일치 | 수위는 시간 보간한다. 속도는 z 보간과 시간 보간을 결합한다. 수직 속도 UT도 같은 두 보간을 수행한다(:62–64). |
| KF1-135 | p.12–13, `second definition of the wave velocity`, Stokes·Knoid·Dean의 정의와 정칙 진행파 설명. 3D manual p.13과 같다. | 2F vf_cwmak0.f:33–34 `N=5` / `CALL VF_STK0(N,R4D,R4T,R4H,R4W1,R4E1,R4K,R4L,R4C,R4CC)`; :40–41 `N=3` / `CALL VF_CND0(N,R4D,R4T,R4H,R4W1,R4E1,R4K,R4L,R4C,R4CC)`. | 코드 대조 대상 아님(H) | 파속 정의와 인용 이론의 소개이다. 호출 종류와 차수는 KF1-014에서 확인한다. p.1–60은 인용 논문의 개별 파형 계수식을 제시하지 않는다. |
| KF1-136 | p.20 그림 0-2-7 오른쪽 자유수면에 `壁面`을 인쇄했다. 뜻: 벽면. 캡션은 `Suffix on wall and free surface`이다. | 2F vf_v1cal.f:390의 표면 처리와 :393의 벽면 처리는 서로 다르다. :393 `CALL VF_BWUWT (XX,YY,ZZ,UU,VV,WW,ANU,BCU,BCV,BCW,BCF,BCVI,INDB)`. | 불일치(B) | 같은 그림의 수면 기호·s 첨자·캡션은 자유수면을 가리킨다. 오른쪽 벽면 표시는 그림의 오기이다. |
| KF1-137 | p.34 식 (3.50)–(3.51)의 λxu·γx 보간 위첨자 \(\Delta x\), (3.51)의 \(\delta y_i\). 3D manual p.32와 같다. | 2F vf_vflxdv.f:113–114 `WIN=YY(6,J)*( YY(2,J-1)*GLX(I,J  ,K)*UU(I,J  ,K)`<br>`     &                     +YY(2,J  )*GLX(I,J-1,K)*UU(I,J-1,K))`; :122 `GG=YY(6,J)*(YY(2,J-1)*GGX(I,J,K)+YY(2,J)*GGX(I,J-1,K))`; :129 `D2=YY(5,J)*(UU(I,J,K)-UU(I  ,J-1,K))`. | 불일치(B) | λxu·γx는 y 방향으로 보간해야 한다. y 방향 중심 간격 첨자는 j이다. ν의 x·y 이중 보간 자체는 대응한다. |
| KF1-138 | p.28 식 (3.11)–(3.13)의 \(\partial P^{n+1}-P^n\), p.30의 보간 설명 중복, p.31 `Figure III - 3 - 2`, p.34–35 `エラー! 参照元が見つかりません。`. 뜻: 오류! 참조 원본을 찾을 수 없습니다. | 2F vf_vmodif.f:110–111의 압력 증분 차분은 KF1-077이다. 2F vf_veuler.f:147–149의 플럭스는 KF1-075이다. | 불일치(B) | 미분은 압력 차 전체에 적용해야 한다. 중복 문장은 추가 계산 단계를 뜻하지 않는다. 그림의 실제 번호는 0-3-2이다. 깨진 참조 문자열은 수치식이 아니다. |

### 2.8 쪽·식 누락 점검

아래 목록의 각 쪽은 300 dpi 원본 쪽 이미지로 열었다.
본문이 없는 쪽도 식·그림을 따로 판정했다.
완전히 빈 쪽은 p.1–60에 없다.

| PDF 쪽(인쇄 쪽) | 포섭 행 및 항목 |
|---|---|
| p.1–6(463–468) | KF1-001–022. 표지·개요·시스템 그림·기능표의 모든 행. |
| p.7–8(469–470) | KF1-012·023. 격자 및 변수 배치의 두 그림. p.8은 그림 쪽. |
| p.9–10(471–472) | KF1-024–032·095. (2.1)–(2.6), 모든 기호 정의·깨진 참조. |
| p.11–12(473–474) | KF1-018·033·014. (2.7), VOF·void fraction 그림, 규칙파 3종. |
| p.13–14(475–476) | KF1-034–037·015. (2.8)–(2.15), 수위·속도 스케일링·조파원·그림 0-2-5. |
| p.15–16(477–478) | KF1-038–041. (2.16)–(2.21), 무번호 Dx·Dy·Dz, 그림 0-2-6. |
| p.17–19(479–481) | KF1-042–054. (2.22)–(2.37), 6개 난류상수·입력 Prt·SCT·온도·농도 정의. |
| p.20–23(482–485) | KF1-055·057–069. 그림 0-2-7, 두 경계표의 모든 무번호식·계수·기호·주석. p.23 끝은 `2.10` 제목. |
| p.24(486) | KF1-055–056. (2.38)–(2.39), 시공간 기상밀도·사용자 함수. |
| p.25–26(487–488) | KF1-070–072. 6개 이산화 방침·시간 갱신 설명·그림 0-3-1. |
| p.27–28(489–490) | KF1-073–079. (3.1)–(3.18), 임시 속도·포텐셜 정의·SMAC 단계 1·2. |
| p.29–30(491–492) | KF1-077·080–081. (3.19)–(3.33), 단계 3·6개 간격·4개 보간식·상류 정의. |
| p.31–33(493–495) | KF1-082–088. 그림 0-3-2, (3.34)–(3.47), 모든 무번호 FLUU·FLUV·FLUW·QU. |
| p.34–36(496–498) | KF1-087–094. (3.48)–(3.67), 모든 y·z 플럭스·소스 정의와 깨진 참조. |
| p.37–39(499–501) | KF1-088–100. (3.68)–(3.90). p.39는 식 (3.90)만 있는 쪽. |
| p.40(502) | KF1-101–102. (3.91)–(3.94), NF·F의 순차 계산 설명. |
| p.41–44(503–506) | KF1-102–106. NF 8개 정의·분류 7단계·방향 2단계·반복 그림·(3.95). |
| p.45–47(507–509) | KF1-107–110. (3.96)–(3.97), CFX·C·FAD·FDM·부호별 첨자·QF 무번호식·제한 이류 그림. p.46–47은 그림 쪽. |
| p.48–51(510–513) | KF1-111–115. (3.98)–(3.99), 4단계·그림 0-3-5–10·3개 직선식·영 법선 조건·ISW 반사. |
| p.52–54(514–516) | KF1-116–119. 6패턴·모든 무번호 Vlim·H1·H2·Heaviside H(x)·(3.100)–(3.102)·무번호 A·B·C. |
| p.55–56(517–518) | KF1-120–121. (3.103)–(3.109). p.56은 식 (3.109)만 있는 쪽. |
| p.57–58(519–520) | KF1-121–128. (3.110)–(3.117), 그림 0-3-12, FLKU 무번호식·방향 대칭·Gs 연속형. |
| p.59–60(521–522) | KF1-128–133. (3.118)–(3.126), FLTU·FLCU 무번호식·QT·QC·농도 성분 첨자 생략. |

KF1-134–138은 위 쪽 목록의 matrix 보간·파속 정의·그림 표기·보간 방향·편집 참조를 보충한다.
KF1-054의 식 (2.37)은 KF1-132에서 판정했다.

식 번호는 (2.1)–(2.39) 및 (3.1)–(3.126)이다.
p.1–60은 입력 카드 문법, COMMON 블록, Fortran 변수형·配列 크기, 파일 장치 번호 표를 포함하지 않는다.
配列의 한국어 뜻은 배열이다.
§3은 위 개요·식의 실제 옵션과 기본값을 추적한 보충 대조이다.

## 3 코드에만 있는 처리

이 절의 “문서에 없음”은 대상 p.1–60 안에 세부 사항이 없다는 뜻이다.
160쪽 전체에 없다는 단언이 아니다.
물리식에 직접 필요한 옵션·검사·배열·보정 경로만 추적했다.
구조 FEM·MPI 라이브러리·외부 도구 내부로 범위를 확대하지 않았다.

| 행 ID | 항목 | 코드 위치와 원문 | 판정 | 이유 |
|---|---|---|---|---|
| KF1-201 | 밀도 반복 상한·오차·완화와 표준출력 | 2F vf_a2dflt.f:48 `MAXITR=1`; :73–74 `SERROR =1.0D-4` / `SRELAX =1.0D0`; vf_a1main.f:1359–1364 `IF(NF(I,J,K).EQ.8) THEN`<br>`SERR = MAX(SERR`<br>`     &                    ,ABS(WK01(I,J,K) - RHOG(I,J,K))/RHOG(I,J,K))`<br>`END IF`<br>`RHOG(I,J,K) =        SRELAX *RHOG(I,J,K)`<br>`     &                      + (1.0D0-SRELAX)*WK01(I,J,K)`; :1369 `CALL VF_P1MAXD(W,SERR)`; :1385–1388은 KF1-005·010. | 코드에만(C) | 오차는 순수 기체 NF=8에서 완화 전에 계산한다. 최대값을 MPI로 모은다. 기본 반복은 1회이다. 상한 도달 때 별도 종료 오류 없이 ITER·SERR를 출력한다. |
| KF1-202 | OPTION STATE·DENS-ERROR 문법·기본값·검사 | 2F vf_iiopt.f:81 `ELSEIF (TEXT(IS(2):IE(2)).EQ.'STATE') THEN`; :83–87 `CALL VF_ZSTOI(ISTATE,TEXT(IS(3):IE(3)))` / `IF (ISTATE.GT.1) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')` / `DO I=4,NWD` / `CALL VF_ZSTOR(SPARAM(I-3),TEXT(IS(I):IE(I)))` / `END DO`; :90 `ELSEIF (TEXT(IS(2):IE(2)).EQ.'DENS-ERROR') THEN`; :92·95·99은 SERROR·MAXITR·SRELAX 읽기. vf_a2dflt.f:47 `ISTATE=0`; :70–74 `SPARAM(1) =1.0D5` / `SPARAM(2) =8.31451D0/0.029D0` / `SPARAM(3) =300.` / `SERROR =1.0D-4` / `SRELAX =1.0D0`. | 코드에만(C) | 형식은 OPTION STATE integer [real …], OPTION DENS-ERROR real [integer [real]]이다. STATE는 1 초과만 거부한다. SERROR>ZERO·MAXITR>0·SRELAX≥ZERO를 검사한다. SRELAX≤1 검사는 없다. EOS가 그 밖의 ISTATE를 오류로 처리한다. |
| KF1-203 | 기상밀도·미분 배열·COMMON·단위 | 2F vf_a1main.f:364–367 `ALLOCATE(RHOG(NUMI,NUMJ,NUMK),STAT=IERR)` / `ALLOCATE(DRHODP(NUMI,NUMJ,NUMK),STAT=IERR)` / `ALLOCATE(DRHODT(NUMI,NUMJ,NUMK),STAT=IERR)` / `ALLOCATE(RHOGO(NUMI,NUMJ,NUMK),STAT=IERR)`; VF_ACOMPI.h:1–4와 VF_ACOMPR.h:1–5는 보충 인용이다. | 코드에만(C) | RHOG·RHOGO는 R*8 기상밀도와 전 시각 밀도이다. DRHODP는 \((d\rho/dp)/\rho\), 단위 1/Pa이다. DRHODT는 코드 계산상 \(\dot\rho/\rho\), 단위 1/s이다. 1-F는 저장값이 아니라 후속 소비 위치에서 곱한다. ISTATE·MAXITR는 I*4 COMMON이다. SPARAM(MAXWDS-3)·SERROR·SRELAX는 R*8 COMMON이다. |
| KF1-204 | 압축 이류 행렬 x 방향 첨자 | 2F vf_vpdrdt.f:114–118 `IF(NF(I+1,J,K).GT.0) THEN`<br>`C                 DRHODX = (RHOG(I+1,J,K) - RHOG(I,J,K))*XX(5,I+1)`<br>`DCOEF = AVLT*WUC*XX(5,I+1)`<br>`AD (I,J,K) = AD (I,J,K) - DCOEF*DRHODP(I  ,J,K)`<br>`AUI(I,J,K) = AUI(I,J,K) + DCOEF*DRHODP(I-1,J,K)`. | 코드에만(E) | 음의 x 흐름에서 우측 이웃 압력계수에 왼쪽 미분을 곱한다. :134의 AUJ는 J+1이고 :150의 AUK는 K+1이다. 자체 주석과 다른 방향 코드가 함께 I+1을 지지한다. 현재 VF_V1CAL:357–360에서 호출한다. |
| KF1-205 | 면 혼합 밀도·압력 포텐셜의 차원 | 2F vf_vpcoef.f:169–173 `RHO02 = XX(6,I)*( XX(2,I )*RHOG(I ,J,K)`<br>`     &                           +XX(2,IM)*RHOG(IM,J,K))`<br>`RI=1.0D0/(FX(I,J,K)*RHO0(1)+(1.0D0-FX(I,J,K))*RHO02)`<br>`AIM=AYZ*XX(5,I)*GGX(I,J,K)*GV*RI`; vf_vmodif.f:328 `PP(I,J,K)=PP(I,J,K)-PT(I,J,K)/DTNOW`. | 코드에만(C) | RHO02는 면적 보간 기상밀도이다. 면 F와 액상 상수밀도로 혼합한다. 예측·행렬·보정에서 같은 역밀도를 사용한다. 코드 PT의 차원은 Pa·s이다. 일정 밀도에서만 문서의 ρφ로 단순 변환한다. |
| KF1-206 | 온도·농도 확산 호출의 인수 불일치 | 2F vf_sdiff.f:1–2 `SUBROUTINE VF_SDIFF(ISW,XX,YY,ZZ,FF,CC,GGX,GGY,GGZ,BCC,DD,`<br>`     &                    FLCU,FLCV,FLCW,INDX,INDY,INDZ,INDC)`; vf_t1cal.f:90–91 `CALL VF_SDIFF(0,XX,YY,ZZ,TT,GGX,GGY,GGZ,BCT,ALM,`<br>`     &              FLTU,FLTV,FLTW,NF,INDX,INDY,INDZ)`; vf_s1cal.f:95–97 `CALL VF_SDIFF(LC,XX,YY,ZZ,CC(1,1,1,LC),`<br>`     &                GGX,GGY,GGZ,BCC(1,LC),DD(1,1,1,LC),`<br>`     &                FLCU,FLCV,FLCW,INDX,INDY,INDZ,INDC)`. | 코드에만(E) | 2F SDIFF는 18개 인수를 받는다. T·농도 호출은 각각 17개이다. FF 인수가 빠져 뒤 실수 배열의 대응이 밀린다. 온도는 예전 NF도 남아 있다. 같은 2F K1CAL:129–130·142–143은 FF를 올바르게 전달한다. 3D의 옛 signature와 T 호출은 서로 맞는다. T·농도를 켜면 호출 가능한 경로이다. |
| KF1-207 | 기체·표면 밀도 보간·이웃 차분 제한 | 2F vf_v1eos.f:88–90 `IF     (NF(I,J,K).EQ.1) THEN` / `RHOG(I,J,K)   = RHOG  (I-1,J,K)` / `DRHODP(I,J,K) = DRHODP(I-1,J,K)`; :126–136의 조건 전체는 보충 인용이다. | 코드에만(C) | 표면 NF=1–6에 이웃 밀도를 복사한다. 액체 이웃을 향한 기상밀도 차분은 0으로 둔다. 복사 방향과 자체 주석의 모순은 KF1-219이다. p.24의 시공간 밀도 정의는 이 세부 사항을 적지 않는다. |
| KF1-208 | DONOR·기울기 옵션·기본값·범위 | 2F vf_iicomp.f:35–39 `IF     (TEXT(IS(3):IE(3)).EQ.'VP-DONOR') THEN` / `CALL VF_ZSTOR(SCMVP,TEXT(IS(4):IE(4)))`<br>`IF (SCMVP.LT.0.0D0 .OR. SCMVP.GT.1.0D0)`<br>`     &                 CALL VF_A2ERR('VF_IICOMP','INVALID VALUE.')`; :42 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'FF-DN-AC') THEN`; :45 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'FF-SLOPE') THEN`; vf_a2dflt.f:40–43 `ISCMVP=0` / `ISCMFF=0` / `ISCMK =0` / `ISCMT =0`; :64–67 `SCMVP =1.0D0` / `SCMK  =1.0D0` / `SCMT  =1.0D0` / `CALL VF_ZSETR1(SCMC,1.0D0,MAXNC)`. | 코드에만(C) | COMP SCHM VP-DONOR real, FF-DN-AC, FF-SLOPE, KE-DONOR real, T-DONOR real, C-DONOR integer real을 읽는다. donor 가중치는 0–1이다. p.6은 선택 종류만 적는다. |
| KF1-209 | 난류상수·벽상수·Prt·SCT 입력 | 2F vf_iimdl.f:209 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'PARAMETER') THEN`; :223 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'LOG-LAW'  ) THEN`; :229 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'PRANDTL'  ) THEN`; :233 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'SCHMIDT'  ) THEN`; :231 `CALL VF_ZSTOR(AKPR,TEXT(IS(4):IE(4)))`; :240 `AKSM(LC)=SC`; vf_a2dflt.f:190–191 `AKPR  =1.0D0` / `CALL VF_ZSETR1(AKSM,1.0D0,MAXNC)`. | 코드에만(C) | MODEL K-EPS PARAMETER의 6실수와 LOG-LAW의 2실수, PRANDTL의 1실수, SCHMIDT의 성분 번호·실수를 읽는다. p.17·21의 수치가 기본값과 같아도 불변 상수로 고정된 것은 아니다. |
| KF1-210 | 움직이는 공극률·서브루프·속도 제한 | 2F vf_seuler.f:49–53은 KF1-129이다. vf_vgene.f:130 `QU(I,J,K)=QU(I,J,K)+(GV1-GV)*DTI*U`; vf_veuler.f:155–156 `IF (UU(I,J,K).GT. VVMAX) UU(I,J,K)= VVMAX` / `IF (UU(I,J,K).LT.-VVMAX) UU(I,J,K)=-VVMAX`; vf_a2dflt.f:226 `VVMAX=30.0D0`; vf_iiopt.f:41–44 `IF     (TEXT(IS(2):IE(2)).EQ.'SUB-LOOP') THEN` / `CALL VF_ZSTOI(LOOPS,TEXT(IS(3):IE(3)))` / `IF (LOOPS.LT.1) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')`. | 코드에만(C) | p.1–60의 정지 다공체 식은 공극률 시간변화와 속도 상한을 적지 않는다. 구조 결합 내부를 여기서 추가 판독하지 않는다. |
| KF1-211 | 면별 감쇠·방사 경계의 격자 보정 | 2F vf_veuler.f:163–188에서 네 면의 후보 D 중 최대값을 선택한다. :167 `IF (D.GT.DMAX) DMAX=D`; vf_bwuwn.f:467–483 `ALN=MIN(C*DTNOW/XX(2,IC-IP),1.0D0)` / `ALT=MIN(ALN*2.0D0          ,1.0D0)`<br>`BCU(L,1)=`<br>`     &                    (1.0D0-ALN)*BCU(L,1)+ALN*UB(I2-IP,J-JP,K)` / `BCV(L,1)=(1.0D0-ALT)*BCV(L,1)+ALT*VC` / `BCW(L,1)=(1.0D0-ALT)*BCW(L,1)+ALT*WC`. | 코드에만(C) | 4면별 감쇠 매개변수를 독립 보유한다. 방사 접선 속도는 반 셀 위치 때문에 ALN의 2배를 쓴다. 두 Courant 가중치를 1로 제한한다. 최초 시각은 두 가중치 1이다. |
| KF1-212 | donor–acceptor 작은 F·벽 경계 예외 | 2F vf_fconv.f:74–80 `FDMW=1.0D0` / `IF (NF(LDM,J,K).GT.-1) FDMW=FF(LDM,J,K)` / `V=XX(2,LD)*GGV(LD,J,K)` / `ELSE` / `FD=BCF(INDX(I,J,K))` / `FDMW=1.0D0` / `V=XX(2,LD)`; :93 `IF (FDMW.LT.FLOWER .AND. FA.LT.FLOWER) FDM=MAX(FDM,0.1D0)`. | 코드에만(C) | 문서 (3.96)의 FDM=max(FDMW,FD)에 0.1 하한을 추가할 수 있다. 벽의 도너는 BCF와 공극률 없는 V를 사용한다. |
| KF1-213 | 법선·패턴의 수치 임계값 | 2F vf_fconvs.f:342–347 `RN=S1*S1+S2*S2+S3*S3` / `IF (RN.GE.ZERO) THEN` / `RN=1.0D0/SQRT(RN)` / `S1=S1*RN` / `S2=S2*RN` / `S3=S3*RN`; :351–355는 KF1-115이다. | 코드에만(C) | 문서의 \(-\nabla F\)를 단위 벡터로 바꾼다. ZERO와 성분 10⁻⁴로 퇴화를 구분한다. |
| KF1-214 | 재구성 다항식의 근·실패 보정 | 2F vf_fslp2a.f:87 `EP=XMX*1.0D-6`; :88–95 `IF     (NRT.EQ.0                       ) THEN` / `CALL VF_A2ERR('VF_FSLP2A','P.G ERROR(2).')` / `ELSEIF (NRT.EQ.1                       ) THEN` / `IF     (XX1.GE.XL-EP .AND. XX1.LE.XR+EP) THEN` / `AA=XX1` / `ELSE` / `WRITE(ILPFIL,9510) 'VF_FSLP2A WARNING(1).'` / `AA=(XL+XR)/2.0D0`. | 코드에만(C) | 근이 없으면 오류이다. 허용 구간 안의 근을 고른다. 구간을 벗어나면 경고 후 구간 중점을 사용한다. 두 근 경로도 :98–104에서 같은 검사를 수행한다. |
| KF1-215 | 재구성 이류의 공극률 상한·F 컷오프 | 2F vf_fconvs.f:466–470은 KF1-120이다. vf_fcut01.f:41–48 `IF     (FF(I,J,K).GT.FUPPER) THEN` / `FCUT=FCUT+(FF(I,J,K)-1.0D0)*V` / `FF(I,J,K)=1.0D0` / `ELSEIF (FF(I,J,K).LT.FLOWER) THEN` / `FCUT=FCUT+(FF(I,J,K)-0.0D0)*V` / `FF(I,J,K)=0.0D0` / `ENDIF` / `FSUM=FSUM+FF(I,J,K)*V`; vf_a2dflt.f:58–60 `FEPS  =1.0D-6` / `FLOWER=FEPS` / `FUPPER=1.0D0-FEPS`. | 코드에만(C) | PLIC도 도너 공극량 MIN을 적용한다. F 컷오프가 보존량을 바꾼 값은 FCUT으로 별도 집계한다. p.1–60은 이 보존 오차 출력을 설명하지 않는다. |
| KF1-216 | solver·시간 간격 옵션과 실패 검사 | 2F vf_iicomp.f:81–89의 ILUBCGSTAB·M-ILUBCGSTAB, :91–105의 MAX-ITR·A-ERROR·R-ERROR; vf_a2dflt.f:37–38 `ICGTYP=1` / `ICGMAX=500`; :52–54 `CGPARA=0.95D0` / `CGEPSA=1.0D-15` / `CGEPSR=1.0D-12`; vf_iitime.f:31 `IF (TEXT(IS(2):IE(2)).EQ.'CONST') THEN`; :38 `ELSEIF (TEXT(IS(2):IE(2)).EQ.'AUTO') THEN`; :47 `ELSEIF (TEXT(IS(2):IE(2)).EQ.'LIMIT') THEN`. | 코드에만(C) | p.6은 MILU와 고정·자동 시간만 적는다. 코드의 ILU 대안·오차·상한·시간 제한 문법은 적지 않는다. 전체 실패 조건과 TIME 기본값은 보충 인용이다. |
| KF1-217 | 대수법칙의 Newton 실패 검사 | 2F vf_cloglw.f:32–34 `NI=20` / `EPS=1.0D-10`; :48 `IF (ABS(DX).LT.XX*EPS) GOTO 110`; :51 `IF (ABS(DX).GE.XX*EPS) CALL VF_A2ERR('VF_CLOGLW','NOT CONVERGED.')`. | 코드에만(C) | p.21은 마찰속도 이론식만 적는다. Newton 최대 20회·상대 증분 기준·미수렴 오류를 생략한다. |
| KF1-218 | 난류·열 확산 하한·EOS 상수밀도 경로 | 2F vf_k1cal.f:169–174 `IF     (AE(I,J,K).LT.AKMINE) THEN` / `AK(I,J,K)=AKMINK` / `AE(I,J,K)=AKMINE` / `ELSEIF (AK(I,J,K).LT.AKMINK) THEN` / `AK(I,J,K)=AKMINK`; vf_cdtcal.f:81–85 `RHO2=FF(I,J,K)*RHO0(1)+(1.0D0-FF(I,J,K))*RHO0(2)` / `!!            RHO2=FF(I,J,K)*RHO0(1)+(1.0D0-FF(I,J,K))*RHOG(I,J,K)` / `W=1.0D0/(RHO2*TCP0)` / `WK01(I,J,K)=MAX(WK01(I,J,K),ALM(I,J,K)*W)`. | 코드에만(C) | k·ε를 하한으로 조정한다. 열 확산의 시간 제한은 EOS 기상밀도 대신 상수 RHO0(2)를 사용한다. 이 행은 p.64 CFL 식의 대조가 아니다. |
| KF1-219 | 表面 기상밀도의 복사 방향 | 2F vf_v1eos.f:83 `C 表面セルの気相密度は、気体セルから埋め込む`. 뜻: 표면 셀의 기상밀도는 기체 셀에서 채운다. :88–90 `IF     (NF(I,J,K).EQ.1) THEN` / `RHOG(I,J,K)   = RHOG  (I-1,J,K)` / `DRHODP(I,J,K) = DRHODP(I-1,J,K)`; vf_fnfprv.f:187 `NF(I,J,K)=1`. | 코드에만(E) | p.41 NF=1은 액체가 x 음측에 있다. 코드는 그 액체 쪽 I-1을 복사한다. NF=2–6도 같은 역방향 관계이다. 자체 주석과 NF 결정 코드가 동시에 기체 쪽 복사라는 설명을 반박한다. |
| KF1-220 | 그림 파일 이름의 병렬 접미사·MG 입력 이름 | 2F vf_ir1inp.f:115 `WRITE(TEXTP,'(I5.5)') MYRANK`; vf_ii1inp.f:127–130 `OPEN(MFILIN,ERR=9010,`<br>`     &       FILE=TRIM(MGNAME(MGRANK+1))//'.in',`<br>`C----------------------------------------------------for MG/2FC coupling`<br>`     &       STATUS='OLD',FORM='FORMATTED'  )`. | 코드에만(A) | p.4의 0000-XXXX식 분할 이름과 달리 입력 .in·.mtb·.poro는 대표 프로세스가 MG 이름으로 연다. .list·.grp·.rsl은 프로세스 수가 2 이상일 때 5자리 MYRANK를 붙인다. MG/2FC coupling 변경 주석과 두 판 날짜 표지가 판 차이 근거이다. .tran은 아래 보충 인용에서 구분한다. |
| KF1-221 | 조파 수직 속도의 수심비 보정 | 2F vf_bwuwn.f:346–348 `BCU(L,2)=UN*VWS*AW*SA` / `BCV(L,2)=UN*VWS*AW*SB` / `BCW(L,2)=UT*VWS*AW`. | 코드에만(C) | p.13 식 (2.8)은 x 또는 y 조파 속도를 설명한다. 코드는 수직 속도 UT에도 VWS를 곱한다. 문서에 없는 추가 보정으로 기록한다. |

| 행 ID | 항목 | 코드 위치와 원문 | 판정 | 이유 |
|---|---|---|---|---|
| KF1-222 | TimerDoor 옵션·기본값·실행 조건 | 2F vf_iiopt.f:58 `ELSEIF (TEXT(IS(2):IE(2)).EQ.'T-DOOR') THEN`; :60–62 `IF     (TEXT(IS(3):IE(3)).EQ.'BUB' ) THEN` / `IF (TEXT(IS(4):IE(4)).EQ.'OFF' ) THEN` / `WBUB=0.0D0`; :67–71 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'DROP') THEN` / `IF     (TEXT(IS(4):IE(4)).EQ.'OFF'         ) THEN` / `IDROP=0` / `ELSEIF (TEXT(IS(4):IE(4)).EQ.'FREE-RUNDOWN') THEN` / `IDROP=1`; vf_a2dflt.f:156 `IDROP=1`; :218 `WBUB =0.2D0`; vf_f1cal.f:191 `IF (WBUB.GE.ZERO) THEN`; :195 `IF (IDROP.GE.1) THEN`. | 코드에만(C) | 형식은 `OPTION T-DOOR BUB OFF` 또는 `OPTION T-DOOR BUB real`이다. 물방울 형식은 `OPTION T-DOOR DROP OFF` 또는 `OPTION T-DOOR DROP FREE-RUNDOWN`이다. BUB 실수는 ZERO 미만을 거부한다(:64–65). 기본값은 두 보조 처리를 켠다. p.6은 방법 이름만 적는다. |
| KF1-223 | 수송식 선택·기본값 | 2F vf_iiequa.f:30 `IF     (TEXT(IS(2):IE(2)).EQ.'K-EPS') THEN`; :34–35 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'CALC'  ) THEN` / `LEQK=1`; :41 `ELSEIF (TEXT(IS(2):IE(2)).EQ.'TEMPERATURE') THEN`; :45–46 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'CALC'  ) THEN` / `LEQT=1`; :52–56 `ELSEIF (TEXT(IS(2):IE(2)).EQ.'CONCENTRATION') THEN` / `IF (NWD.LT.3) CALL VF_A2ERR('VF_IIEQUA','SYNTAX ERROR.')` / `CALL VF_ZSTOI(LEQC,TEXT(IS(3):IE(3)))` / `IF (LEQC.LT.0    ) CALL VF_A2ERR('VF_IIEQUA','INVALID VALUE.')` / `IF (LEQC.GT.MAXNC) CALL VF_A2ERR('VF_IIEQUA','INVALID VALUE.')`; vf_a2dflt.f:146–148 `LEQK =0` / `LEQT =0` / `LEQC =0`. | 코드에만(C) | `EQUATION K-EPS CALC`와 `EQUATION TEMPERATURE CALC`가 수송식을 켠다. 두 키워드는 `NOCALC`도 읽는다. `EQUATION CONCENTRATION integer`는 0–MAXNC의 성분 수를 읽는다. 세 기본값은 수송식을 끈다. 기능표의 Unused와 입력 경로의 차이는 KF1-016에서 판정했다. |

### 3.1 보충 원문 인용

아래 인용은 표에서 연결한 고정형식 연속 문장 전체이다.
줄 번호는 nl -ba로 부여했다.
주석이 연속 줄 사이에 있어도 삭제하지 않았다.
일본어 주석의 뜻은 각 인용의 한국어 설명에 적었다.


2F vf_ii1inp.f:124–131.


```fortran
   124	      IF (MYRANK.EQ.0) THEN
   125	C----------------------------------------------------for MG/2FC coupling
   126	C       OPEN(MFILIN,ERR=9010,FILE='data.in',
   127	        OPEN(MFILIN,ERR=9010,
   128	     &       FILE=TRIM(MGNAME(MGRANK+1))//'.in',
   129	C----------------------------------------------------for MG/2FC coupling
   130	     &       STATUS='OLD',FORM='FORMATTED'  )
   131	        IINFIL=MFILIN
```

2F vf_im1inp.f:45–49.


```fortran
    45	C----------------------------------------------------for MG/2FC coupling
    46	C     OPEN(MFILMT,ERR=9010,FILE='data.mtb',
    47	      OPEN(MFILMT,ERR=9010,FILE=TRIM(MGNAME(MGRANK+1))//'.mtb',
    48	C----------------------------------------------------for MG/2FC coupling
    49	     &     STATUS='OLD',FORM='FORMATTED'  )
```

2F vf_ip1inp.f:47–62.


```fortran
    47	C----------------------------------------------------for MG/2FC coupling
    48	C           OPEN(MFILPR,ERR=9010,FILE='data.poro',
    49	            OPEN(MFILPR,ERR=9010,FILE=TRIM(MGNAME(MGRANK+1))//'.poro',
    50	C----------------------------------------------------for MG/2FC coupling
    51	     &                  STATUS='OLD',FORM='UNFORMATTED' )
    52	            IPRFIL=MFILPR
    53	            WRITE(ILPFIL,9510)
    54	            READ(IPRFIL,END=9020,ERR=9030) IPRNB,ISW1,ISW2,ISW3,ISW4
    55	CC            WRITE(2001,'(A,5I)') '(H1):',IPRNB,ISW1,ISW2,ISW3,ISW4
    56	          ELSE
    57	C----------------------------------------------------for MG/2FC coupling
    58	C           OPEN(MFILPR,ERR=9010,FILE='data.poro.ascii',
    59	            OPEN(MFILPR,ERR=9010,
    60	     &                  FILE=TRIM(MGNAME(MGRANK+1))//'.poro.ascii',
    61	C----------------------------------------------------for MG/2FC coupling
    62	     &                  STATUS='OLD',FORM='FORMATTED' )
```

2F vf_ir1inp.f:108–120.


```fortran
   108	      IF (NPROCS.EQ.1) THEN
   109	C----------------------------------------------------for MG/2FC coupling
   110	C       OPEN(MFILRE,ERR=9010,FILE='data.res',
   111	        OPEN(MFILRE,ERR=9010,FILE=TRIM(MGNAME(MGRANK+1))//'.res',
   112	C----------------------------------------------------for MG/2FC coupling
   113	     &       STATUS='OLD',FORM='UNFORMATTED' )
   114	      ELSE
   115	        WRITE(TEXTP,'(I5.5)') MYRANK
   116	C----------------------------------------------------for MG/2FC coupling
   117	C       OPEN(MFILRE,ERR=9010,FILE='data.res'//TEXTP,
   118	        OPEN(MFILRE,ERR=9010,FILE=TRIM(MGNAME(MGRANK+1))//'.res'//TEXTP,
   119	C----------------------------------------------------for MG/2FC coupling
   120	     &       STATUS='OLD',FORM='UNFORMATTED' )
```

2F vf_a1main.f:306–320.


```fortran
   306	      IF (NPROCS.EQ.1) THEN
   307	C----------------------------------------------------for MG/2FC coupling
   308	C       OPEN(MFILLP,ERR=9010,FILE='data.list',
   309	        OPEN(MFILLP,ERR=9010,
   310	     &       FILE=TRIM(MGNAME(MGRANK+1))//'.list',
   311	C----------------------------------------------------for MG/2FC coupling
   312	     &       STATUS='NEW',FORM='FORMATTED'    )
   313	      ELSE
   314	        WRITE(TEXTP,'(I5.5)') MYRANK
   315	C----------------------------------------------------for MG/2FC coupling
   316	C       OPEN(MFILLP,ERR=9010,FILE='data.list'//TEXTP,
   317	        OPEN(MFILLP,ERR=9010,
   318	     &       FILE=TRIM(MGNAME(MGRANK+1))//'.list'//TEXTP,
   319	C----------------------------------------------------for MG/2FC coupling
   320	     &       STATUS='NEW',FORM='FORMATTED'    )
```


2F vf_og1ini.f:45–57.


```fortran
    45	      IF (NPROCS.EQ.1) THEN
    46	C----------------------------------------------------for MG/2FC coupling
    47	C       OPEN(MFILGR,ERR=9010,FILE='data.grp',
    48	        OPEN(MFILGR,ERR=9010,FILE=TRIM(MGNAME(MGRANK+1))//'.grp',
    49	C----------------------------------------------------for MG/2FC coupling
    50	     &       STATUS='NEW',FORM='UNFORMATTED' )
    51	      ELSE
    52	        WRITE(TEXTP,'(I5.5)') MYRANK
    53	C----------------------------------------------------for MG/2FC coupling
    54	C       OPEN(MFILGR,ERR=9010,FILE='data.grp'//TEXTP,
    55	        OPEN(MFILGR,ERR=9010,FILE=TRIM(MGNAME(MGRANK+1))//'.grp'//TEXTP,
    56	C----------------------------------------------------for MG/2FC coupling
    57	     &       STATUS='NEW',FORM='UNFORMATTED' )
```

2F vf_or1ini.f:37–49.


```fortran
    37	      IF (NPROCS.EQ.1) THEN
    38	C----------------------------------------------------for MG/2FC coupling
    39	C       OPEN(MFILRS,ERR=9010,FILE='data.rsl',
    40	        OPEN(MFILRS,ERR=9010,FILE=TRIM(MGNAME(MGRANK+1))//'.rsl',
    41	C----------------------------------------------------for MG/2FC coupling
    42	     &       STATUS='NEW',FORM='UNFORMATTED' )
    43	      ELSE
    44	        WRITE(TEXTP,'(I5.5)') MYRANK
    45	C----------------------------------------------------for MG/2FC coupling
    46	C       OPEN(MFILRS,ERR=9010,FILE='data.rsl'//TEXTP,
    47	        OPEN(MFILRS,ERR=9010,FILE=TRIM(MGNAME(MGRANK+1))//'.rsl'//TEXTP,
    48	C----------------------------------------------------for MG/2FC coupling
    49	     &       STATUS='NEW',FORM='UNFORMATTED' )
```

2F vf_ot1ini.f:25–34.
주석 `時系列ファイルのオープンとメッセージの出力`의 뜻은 시계열 파일 열기와 메시지 출력이다. `.tran`은 MYRANK=0만 열며 병렬 접미사를 붙이지 않는다.

```fortran
    25	      IF (MYRANK.NE.0) GOTO 9000
    26	
    27	CD    -- 時系列ファイルのオープンとメッセージの出力 --
    28	      ITRFIL=0
    29	C----------------------------------------------------for MG/2FC coupling
    30	C     OPEN(MFILTR,ERR=9010,FILE='data.tran',
    31	      OPEN(MFILTR,ERR=9010,FILE=TRIM(MGNAME(MGRANK+1))//'.tran',
    32	C----------------------------------------------------for MG/2FC coupling
    33	     &     STATUS='NEW',FORM='FORMATTED' )
    34	      ITRFIL=MFILTR
```

2F vf_ot1trn.f:332–332.


```fortran
   332	      IF (MYRANK.EQ.0) WRITE(ITRFIL,9510) TNOW,(RTRVAL(L),L=1,ITRNUM)
```

2F vf_bwuwn.f:328–348.
주석 `境界値を計算する`의 뜻은 경계값 계산이다. p.13의 두 식을 수심비 VWS와 ZC에서 확인한다.

```fortran
   328	                      VAL=VAL-(WVLVL-ZZ(1,2))
   329	                      VWS=(WVZ+D)/(VAL+D)
   330	                    ELSE
   331	                      VWS=1.0D0
   332	                    ENDIF
   333	C                   * 境界値を計算する
   334	                    KMT=1
   335	                    DO 220 K=2,NUMK-1
   336	                      L=INDX(I-IP,J-JP,K)
   337	                      IF (L.GE.1) THEN
   338	                        ZC=(ZZ(1,K)+ZZ(1,K+1))*0.5D0-WVLVL
   339	                        ZC=VWS*(ZC+D)-D
   340	                        IF (N.NE.-3) THEN
   341	                          CALL VF_CWMAK2(WVT,ZC,UN,UT,N)
   342	                        ELSE
   343	                          CALL VF_CWMTB2(KMT,WMT1,WMT2,ZC,UN,UT,
   344	     &                                   DMTBZZ,DMTBUN,DMTBUT)
   345	                        ENDIF
   346	                        BCU(L,2)=UN*VWS*AW*SA
   347	                        BCV(L,2)=UN*VWS*AW*SB
   348	                        BCW(L,2)=UT*VWS*AW
```


2F vf_cglv.f:32–37.


```fortran
    32	CSTR        IF (NF(I,J,K).LE.-1) THEN
    33	            IF (NF(I,J,K).LE.-1 .AND. ICPL.EQ.0 .AND. ISTM.EQ.0) THEN
    34	              GLV(I,J,K)=1.0D0
    35	            ELSE
    36	              GLV(I,J,K)=GGV(I,J,K)+(1.0D0-GGV(I,J,K))*CM0(I,J,K)
    37	            ENDIF
```

2F vf_vflxdu.f:121–129.


```fortran
   121	              GG=XX(6,I)*(XX(2,I-1)*GGY(I,J,K)+XX(2,I)*GGY(I-1,J,K))
   122	              ANR=YY(6,J)*( YY(2,J-1)*ANU(I  ,J  ,K)
   123	     &                     +YY(2,J  )*ANU(I  ,J-1,K))
   124	              ANL=YY(6,J)*( YY(2,J-1)*ANU(I-1,J  ,K)
   125	     &                     +YY(2,J  )*ANU(I-1,J-1,K))
   126	              AN=XX(6,I)*(XX(2,I-1)*ANR+XX(2,I)*ANL)
   127	              D1=YY(5,J)*(UU(I,J,K)-UU(I  ,J-1,K))
   128	              D2=XX(5,I)*(VV(I,J,K)-VV(I-1,J  ,K))
   129	              FLUV(I,J,K)=FLUV(I,J,K)+GG*AN*(D1+D2)
```

2F vf_vflxdw.f:266–283.
주석 `線形補間`의 뜻은 선형 보간이다. y 이류 속도는 VV이다.

```fortran
   266	              WIN=ZZ(6,K)*( ZZ(2,K-1)*GLY(I,J,K  )*VV(I,J,K  )
   267	     &                     +ZZ(2,K  )*GLY(I,J,K-1)*VV(I,J,K-1))
   268	              FG =WIN*YY(6,J)*(YY(2,J-1)*WW(I,J,K)+YY(2,J)*WW(I,J-1,K))
   269	              FLWV(I,J,K)=FLWV(I,J,K)-SU*( MAX( WIN,0.0D0)*WW(I,J-1,K)
   270	     &                                    -MAX(-WIN,0.0D0)*WW(I,J  ,K))
   271	     &                               -SC*FG
   272	
   273	C             * Gy*Nu*(dw/dy+dv/dz)
   274	C             ? 線形補間
   275	              GG=ZZ(6,K)*(ZZ(2,K-1)*GGY(I,J,K)+ZZ(2,K)*GGY(I,J,K-1))
   276	              ANR=YY(6,J)*( YY(2,J-1)*ANU(I,J  ,K  )
   277	     &                     +YY(2,J  )*ANU(I,J-1,K  ))
   278	              ANL=YY(6,J)*( YY(2,J-1)*ANU(I,J  ,K-1)
   279	     &                     +YY(2,J  )*ANU(I,J-1,K-1))
   280	              AN=ZZ(6,K)*(ZZ(2,K-1)*ANR+ZZ(2,K)*ANL)
   281	              D1=YY(5,J)*(WW(I,J,K)-WW(I,J-1,K  ))
   282	              D2=ZZ(5,K)*(VV(I,J,K)-VV(I,J  ,K-1))
   283	              FLWV(I,J,K)=FLWV(I,J,K)+GG*AN*(D1+D2)
```

2F vf_vmodif.f:282–287.


```fortran
   282	                RHO02 = ZZ(6,K)*( ZZ(2,K  )*RHOG(I,J,K  )
   283	     &                           +ZZ(2,K-1)*RHOG(I,J,K-1))
   284	                RI=1.0D0/(FZ(I,J,K)*RHO0(1)+(1.0D0-FZ(I,J,K))*RHO02)
   285	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   286	                WW(I,J,K)=WW(I,J,K)
   287	     &                      +ZZ(5,K)*GV*(PT(I,J,K)-PT(I,J,K-1))*RI
```

2F vf_vpsol.f:70–81.


```fortran
    70	      CALL VF_M1BCGS(DBUF,
    71	     &               AD ,ALI,ALJ,ALK,AUI,AUJ,AUK,BB ,PT ,
    72	     &               DD ,XW ,YY ,R0 ,RR ,PP ,AP ,AE ,
    73	     &               CGPARA,CGEPSA,CGEPSR,CGDIV,CGBNRM,CGXNRM,
    74	     &               INDC,MI,MJ,MK,NUMI,NUMJ,NUMK,
    75	     &               ICGTYP,ICGMAX,ICGITR)
    76	      IF (ICGITR.GT.ICGMAX)
    77	     &           CALL VF_A2ERR('VF_VPSOL','NOT CONVERGED.')
    78	      IF (ICGITR.EQ.-2    )
    79	     &           CALL VF_A2ERR('VF_VPSOL','INSTABILITY.')
    80	      IF (ICGITR.EQ.-1    )
    81	     &           CALL VF_A2ERR('VF_VPSOL','CAN NOT DECOMPOSITION.')
```


2F vf_a2dflt.f:228–242.
주석 `初期化`의 뜻은 초기화이다. 기본 시간 모드는 자동이다.

```fortran
   228	CD    -- VF_ATIMEI.hの初期化 --
   229	      NEND  =0
   230	      NNOW  =0
   231	      IDTTYP=1
   232	      LOOPS =1
   233	
   234	CD    -- VF_ATIMER.hの初期化 --
   235	      TEND  =0.0D0
   236	      TNOW  =0.0D0
   237	      DTNOW =0.0D0
   238	      DTCNST=1.0D-3
   239	      DTINIT=1.0D-6
   240	      DTMIN =ZERO
   241	      DTMAX =1.0D0/ZERO
   242	      DTSAFE=1.0D-1
```

2F VF_ACOMPI.h:1–5.


```fortran
     1	      COMMON /VF_ACOMPI/ ICGTYP,ICGMAX,ICGITR,ISCMVP,ISCMFF,
     2	     &                   ISCMK,ISCMT,ISCMC(MAXNC),IBSUW0
     3	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
     4	     &                  ,ISTATE,MAXITR
     5	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
```

2F VF_ACOMPR.h:1–6.


```fortran
     1	      COMMON /VF_ACOMPR/ CGPARA,CGEPSA,CGEPSR,CGDIV ,CGBNRM,CGXNRM,
     2	     &                   FEPS  ,FLOWER,FUPPER,FSUM  ,FCUT  ,PLOWER,
     3	     &                   SCMVP ,SCMK  ,SCMT  ,SCMC(MAXNC)
     4	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
     5	     &                  ,SPARAM(MAXWDS-3),SERROR,SRELAX
     6	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
```

2F vf_v1eos.f:126–138.


```fortran
   126	              IF(WUC.GT.0.0D0) THEN
   127	                IF(NF(I-1,J,K).GT.0) THEN
   128	                  DRHODX = (RHOG(I,J,K) - RHOG(I-1,J,K))*XX(5,I)
   129	                ELSE
   130	                  DRHODX = 0.0D0
   131	                END IF
   132	              ELSE
   133	                IF(NF(I+1,J,K).GT.0) THEN
   134	                  DRHODX = (RHOG(I+1,J,K) - RHOG(I,J,K))*XX(5,I+1)
   135	                ELSE
   136	                  DRHODX = 0.0D0
   137	                END IF
   138	              END IF
```

3D vf_a1main.f:33–35.


```fortran
    33	C----------------------------------------------------------2012.03 start
    34	      INCLUDE 'VF_ASEABT.h'
    35	C----------------------------------------------------------2012.03 end
```


3D vf_f1cal.f:153–155.
주석 `生成消滅項の計算`의 뜻은 생성·소멸항 계산이다. 3D에서 조파원 호출은 활성이다.

```fortran
   153	
   154	CD    -- 生成消滅項の計算 --
   155	      CALL VF_FGENE(XX,YY,FF,SRCUV,QF,NF)
```

3D vf_v1cal.f:293–295.


```fortran
   293	      CALL VF_BSUWT (XX,YY,ZZ,UU,VV,WW,DBUF,NF,INDX,INDY,INDZ)
   294	      CALL VF_BSUWT2(UU,VV,WW,DBUF,NF,INDX,INDY,INDZ,INDS)
   295	      CALL VF_BSUWN (XX,YY,ZZ,UU,VV,WW,GGX,GGY,GGZ,DBUF,SRCUV,NF,INDS)
```

### 3.2 표에서 연결한 추가 원문

2F vf_v1cal.f:369–372. 압력 행렬을 푸는 호출 전체이다.

```fortran
   369	      CALL VF_VPSOL(0,DBUF,
   370	     &              WK01,WK02,WK03,WK04,WK05,
   371	     &              WK06,WK07,WK08,WK09,WK10,
   372	     &              WK11,WK12,WK13,WK14,WK15,WK16,WK17,INDC)
```

2F vf_veuler.f:279–284. z 속도 예측의 플럭스 발산과 압축항이다. 느낌표 줄은 원문의 구분 주석이다.

```fortran
   279	              DW=( XX(4,I)*(FLWU(I+1,J,K)-FLWU(I,J,K))
   280	     &            +YY(4,J)*(FLWV(I,J+1,K)-FLWV(I,J,K))
   281	     &            +ZZ(5,K)*(FLWW(I,J,K)-FLWW(I,J,K-1))+QW(I,J,K))
   282	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   283	!!            WW(I,J,K)=(GV*WW(I,J,K)+DTNOW*DW)/GV0
   284	              WW(I,J,K)=(GV*WWO(I,J,K)+DTNOW*(DW+DRDTW))/GV0
```

2F vf_f1cal.f:191–201. TimerDoor 호출과 재분류의 조건이다.

```fortran
   191	      IF (WBUB.GE.ZERO) THEN
   192	        CALL VF_FBUBUP(ZZ,FF,GGV,TBUB,DBUF,NF)
   193	        CALL VF_FNFINI(FF,BCF,NF,INDX,INDY,INDZ,INDS,IBUF)
   194	      ENDIF
   195	      IF (IDROP.GE.1) THEN
   196	        CALL VF_FDROPF(XX,YY,ZZ,UU,VV,WW,FF,GGV,
   197	     &                 DROPTX,DROPTY,DROPTZ,DROPUU,DROPVV,DROPWW,
   198	     &                 DBUF,WK05,WK06,WK07,WK08,WK09,WK10,WK11,NF)
   199	        CALL VF_FNFINI(FF,BCF,NF,INDX,INDY,INDZ,INDS,IBUF)
   200	      ENDIF
   201	      CALL VF_FNFPRV(FF,BCF,NF,INDX,INDY,INDZ,INDS,IBUF)
```

2F vf_bwkelg.f:166–184. 벽면 마찰속도로 계산한 k·ε를 접한 경계의 가중평균으로 설정한다.

```fortran
   166	                SR=1.0D0/(SX+SY+SZ+SXM+SXP+SYM+SYP+SZM+SZP)
   167	                AK(I,J,K)=CMR*( UT *UT        *SX
   168	     &                         +VT *VT        *SY
   169	     &                         +WT *WT        *SZ
   170	     &                         +UTM*UTM       *SXM
   171	     &                         +UTP*UTP       *SXP
   172	     &                         +VTM*VTM       *SYM
   173	     &                         +VTP*VTP       *SYP
   174	     &                         +WTM*WTM       *SZM
   175	     &                         +WTP*WTP       *SZP)*SR
   176	                AE(I,J,K)=CKR*( UT *UT *UT /DX*SX
   177	     &                         +VT *VT *VT /DY*SY
   178	     &                         +WT *WT *WT /DZ*SZ
   179	     &                         +UTM*UTM*UTM/DX*SXM
   180	     &                         +UTP*UTP*UTP/DX*SXP
   181	     &                         +VTM*VTM*VTM/DY*SYM
   182	     &                         +VTP*VTP*VTP/DY*SYP
   183	     &                         +WTM*WTM*WTM/DZ*SZM
   184	     &                         +WTP*WTP*WTP/DZ*SZP)*SR
```

2F vf_clm00.f:60–62. 열전도율 계산의 RI는 상수 기상밀도를 사용한 혼합 밀도이다.

```fortran
    60	                RI=FF(I,J,K)*RHO0(1)+(1.0D0-FF(I,J,K))*RHO0(2)
    61	                W=RI*TCP0/AKPR
    62	                ALM(I,J,K)=TCN0+ANUT(I,J,K)*W
```

2F vf_vflxdv.f:113–130. xy 플럭스의 y 보간과 x·y 전단 차분이다. 주석 線形補間의 뜻은 선형 보간이다.

```fortran
   113	              WIN=YY(6,J)*( YY(2,J-1)*GLX(I,J  ,K)*UU(I,J  ,K)
   114	     &                     +YY(2,J  )*GLX(I,J-1,K)*UU(I,J-1,K))
   115	              FG =WIN*XX(6,I)*(XX(2,I-1)*VV(I,J,K)+XX(2,I)*VV(I-1,J,K))
   116	              FLVU(I,J,K)=FLVU(I,J,K)-SU*( MAX( WIN,0.0D0)*VV(I-1,J,K)
   117	     &                                    -MAX(-WIN,0.0D0)*VV(I  ,J,K))
   118	     &                               -SC*FG
   119	
   120	C             * Gx*Nu*(dv/dx+du/dy)
   121	C             ? 線形補間
   122	              GG=YY(6,J)*(YY(2,J-1)*GGX(I,J,K)+YY(2,J)*GGX(I,J-1,K))
   123	              ANR=XX(6,I)*( XX(2,I-1)*ANU(I  ,J  ,K)
   124	     &                     +XX(2,I  )*ANU(I-1,J  ,K))
   125	              ANL=XX(6,I)*( XX(2,I-1)*ANU(I  ,J-1,K)
   126	     &                     +XX(2,I  )*ANU(I-1,J-1,K))
   127	              AN=YY(6,J)*(YY(2,J-1)*ANR+YY(2,J)*ANL)
   128	              D1=XX(5,I)*(VV(I,J,K)-VV(I-1,J  ,K))
   129	              D2=YY(5,J)*(UU(I,J,K)-UU(I  ,J-1,K))
   130	              FLVU(I,J,K)=FLVU(I,J,K)+GG*AN*(D1+D2)
```

2F vf_a2dflt.f:153–156. 주석 初期化의 뜻은 초기화이다. IDROP 기본값을 확인한다.

```fortran
   153	CD    -- VF_APHYSI.hの初期化 --
   154	      CALL VF_ZSETI2(IBCTYP, 0,4,4)
   155	      CALL VF_ZSETI1(IDAMP ,-1,4)
   156	      IDROP=1
```

NF 방향의 대입은 다음과 같다. 조건의 NF=0 이웃이 액체 방향이다.

| NF | 액체 방향 | 조건과 대입 원문 |
|---|---|---|
| 1 | x 음측 | 2F vf_fnfprv.f:164 `IF (NF(IB,J,K).EQ.0 .AND. NF(I+1,J,K).EQ.8) THEN`; :187 `NF(I,J,K)=1`. |
| 2 | x 양측 | 2F vf_fnfprv.f:194 `IF (NF(IB,J,K).EQ.0 .AND. NF(I-1,J,K).EQ.8) THEN`; :217 `NF(I,J,K)=2`. |
| 3 | y 음측 | 2F vf_fnfprv.f:104 `IF (NF(I,JB,K).EQ.0 .AND. NF(I,J+1,K).EQ.8) THEN`; :127 `NF(I,J,K)=3`. |
| 4 | y 양측 | 2F vf_fnfprv.f:134 `IF (NF(I,JB,K).EQ.0 .AND. NF(I,J-1,K).EQ.8) THEN`; :157 `NF(I,J,K)=4`. |
| 5 | z 음측 | 2F vf_fnfprv.f:44 `IF (NF(I,J,KB).EQ.0 .AND. NF(I,J,K+1).EQ.8) THEN`; :67 `NF(I,J,K)=5`. |
| 6 | z 양측 | 2F vf_fnfprv.f:74 `IF (NF(I,J,KB).EQ.0 .AND. NF(I,J,K-1).EQ.8) THEN`; :97 `NF(I,J,K)=6`. |

### 3.3 입력 선택의 문자열 비교 보충

아래 행 참조는 기존 KF1 행의 보충 인용이다. 별도 발견으로 세지 않는다.
기본값 대입 원문은 KF1-208·209·216과 §3.1에 있다.

| 행 참조 | 형식 | 문자열 비교와 읽기 원문 |
|---|---|---|
| 208 | `COMP SCHM KE-DONOR real` | 2F vf_iicomp.f:48 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'KE-DONOR') THEN`; :50 `CALL VF_ZSTOR(SCMK,TEXT(IS(4):IE(4)))`. |
| 208 | `COMP SCHM T-DONOR real` | 2F vf_iicomp.f:55 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'T-DONOR') THEN`; :57 `CALL VF_ZSTOR(SCMT,TEXT(IS(4):IE(4)))`. |
| 208 | `COMP SCHM C-DONOR integer real` | 2F vf_iicomp.f:62 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'C-DONOR') THEN`; :64–65 `CALL VF_ZSTOI(LC,TEXT(IS(4):IE(4)))` / `CALL VF_ZSTOR(SC,TEXT(IS(5):IE(5)))`. |
| 209 | `MODEL K-EPS PARAMETER real real real real real real` | 2F vf_iimdl.f:209 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'PARAMETER') THEN`; :211–216 `CALL VF_ZSTOR(AKCMU,TEXT(IS(4):IE(4)))` / `CALL VF_ZSTOR(AKSGK,TEXT(IS(5):IE(5)))` / `CALL VF_ZSTOR(AKSGE,TEXT(IS(6):IE(6)))` / `CALL VF_ZSTOR(AKC1 ,TEXT(IS(7):IE(7)))` / `CALL VF_ZSTOR(AKC2 ,TEXT(IS(8):IE(8)))` / `CALL VF_ZSTOR(AKC3 ,TEXT(IS(9):IE(9)))`. |
| 209 | `MODEL K-EPS LOG-LAW real real` | 2F vf_iimdl.f:223 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'LOG-LAW'  ) THEN`; :225–226 `CALL VF_ZSTOR(AKK0,TEXT(IS(4):IE(4)))` / `CALL VF_ZSTOR(AKA0,TEXT(IS(5):IE(5)))`. |
| 209 | `MODEL K-EPS SCHMIDT integer real` | 2F vf_iimdl.f:233 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'SCHMIDT'  ) THEN`; :235–236 `CALL VF_ZSTOI(LC,TEXT(IS(4):IE(4)))` / `CALL VF_ZSTOR(SC,TEXT(IS(5):IE(5)))`; :240 `AKSM(LC)=SC`. |
| 216 | `COMP MTRX ILUBCGSTAB`, `COMP MTRX M-ILUBCGSTAB real` | 2F vf_iicomp.f:81–82 `IF     (TEXT(IS(3):IE(3)).EQ.'ILUBCGSTAB') THEN` / `ICGTYP=0`; :84 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'M-ILUBCGSTAB') THEN`; :86 `CALL VF_ZSTOR(CGPARA,TEXT(IS(4):IE(4)))`; :89 `ICGTYP=1`. |
| 216 | `COMP MTRX MAX-ITR integer`, `A-ERROR real`, `R-ERROR real` | 2F vf_iicomp.f:91 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'MAX-ITR') THEN`; :93 `CALL VF_ZSTOI(ICGMAX,TEXT(IS(4):IE(4)))`; :96 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'A-ERROR') THEN`; :98 `CALL VF_ZSTOR(CGEPSA,TEXT(IS(4):IE(4)))`; :102 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'R-ERROR') THEN`; :104 `CALL VF_ZSTOR(CGEPSR,TEXT(IS(4):IE(4)))`. |
| 216 | `TIME CONST real`, `TIME AUTO real real`, `TIME LIMIT real real` | 2F vf_iitime.f:31 `IF (TEXT(IS(2):IE(2)).EQ.'CONST') THEN`; :33 `CALL VF_ZSTOR(DTCNST,TEXT(IS(3):IE(3)))`; :38 `ELSEIF (TEXT(IS(2):IE(2)).EQ.'AUTO') THEN`; :40–41 `CALL VF_ZSTOR(DTINIT,TEXT(IS(3):IE(3)))` / `CALL VF_ZSTOR(DTSAFE,TEXT(IS(4):IE(4)))`; :47 `ELSEIF (TEXT(IS(2):IE(2)).EQ.'LIMIT') THEN`; :49–50 `CALL VF_ZSTOR(DTMIN,TEXT(IS(3):IE(3)))` / `CALL VF_ZSTOR(DTMAX,TEXT(IS(4):IE(4)))`. |

## 4 노트 대조와 수정안

아래 파일은 읽기만 했다.
수정안은 이 보고서 안에만 적는다.
노트에 포함된 범위 밖 주장까지 재검증했다고 해석하지 않는다.

| 현재 노트 위치와 원문 | 대조 결과 | 노트 수정안 |
|---|---|---|
| N/manual-notes/cadmas-2f-manual-compressibility.md:18 `**/3D 매뉴얼의 ~95% 중복** + **기상 압축성 부록**` | 95%의 집계 기준이 없다. 이번 보고서는 p.1–60의 식별 대응만 확인했다. | “p.1–60에는 3D manual과 공통인 식이 있다. 압축항·미사용 표시·일부 편집 오류가 다르다. 식별 대응은 이 보고서 §2를 따른다.” |
| 같은 파일:26 `**기상 압축성 소스항` 다음 `1개를 연속식·Poisson에 주입` | KF1-024–027·042·050·053. 문서는 운동량·난류·온도·농도에도 항을 더한다. | “문서는 연속식과 운동량·스칼라 수송식에 기상밀도 변화항을 기술한다. 현재 코드의 운동량 항은 문서와 부호가 다르다. 스칼라 갱신에는 그 항이 없다.” |
| 같은 파일:28 `γ_vS_φ` | p.9 식 (2.1)은 \(S_\rho\)이다. | “연속식의 조파 소스 기호는 \(S_\rho\)이다. 2F 코드의 조파 소스는 비활성이다.” |
| 같은 파일:30 `**EOS eq(2.38)(p.485)**` | KF1-055. 인쇄 485는 경계조건 표와 `2.10` 제목이다. | “EOS 식 (2.38)은 2F manual p.24(인쇄 486)에 있다.” |
| 같은 파일:31 `ρ̇_G = γ_v∂ρ_G/∂t + ∂ₓ(γₓuρ_G)+...` | KF1-056. 원문은 보존형 밀도 플럭스의 발산이 아니다. | “식 (2.39)은 \(\dot\rho_G=\gamma_v\partial_t\rho_G+\gamma_xu\partial_x\rho_G+\gamma_yv\partial_y\rho_G+\gamma_zw\partial_z\rho_G\)이다. 코드의 이류 계수에는 추가 γv/λv가 있다.” |
| 같은 파일:33 `**EOS 등온이상기체**(operation default)` | KF1-202. 기본 ISTATE=0이다. | “기본값은 비압축 기상이다. OPTION STATE 1을 선택하면 등온 EOS를 사용한다. 기본 매개변수는 \(p_0=10^5\,Pa\), \(R=8.31451/0.029\,J/(kg\,K)\), \(T=300\,K\)이다.” |
| 같은 파일:40 `DRHODT=(1−F)(dρ/dt)/ρ` 및 `✅ 일치` | KF1-024·029·056·203. DRHODT 대입 자체는 1-F를 곱하지 않는다. | “DRHODT는 코드의 가중 밀도미분/기상밀도이다. Poisson과 운동량의 소비 위치가 1-F를 곱한다. 식 (2.39)와의 계수 차이는 결함 후보로 남긴다.” |
| 같은 파일:41·44 `✅ 정확일치(행렬계수+RHS)` 및 `**정확일치**` | KF1-204·219. x 이류 첨자와 표면밀도 복사 방향이 모순이다. | “압축성 증강 행렬이 존재한다. VF_VPDRDT의 음의 x 이류 계수와 VF_V1EOS의 표면밀도 복사 방향은 각각 결함 후보이다. 전체 계수의 정확일치 판정은 철회한다.” |
| 같은 파일:32·40–41의 (3.127)–(3.128) 인용 | p.60 끝은 (3.126)이다. 이 두 식은 이번 쪽 범위 밖이다. | “p.1–60 대조 결과로 (3.127)–(3.128)을 검증했다고 쓰지 않는다. 별도 범위 대조 결과와 연결한다.” |
| 같은 파일:44 `액=1열·기=2열, 기본 1.0` | 2F vf_a2dflt.f:170–171 `RHO0(1)=1.0D+3` / `RHO0(2)=1.0D0`. | “액상 기본 밀도는 1000이다. 비압축 기상 기본 밀도는 1이다. EOS 기상밀도는 압력에 따라 달라진다.” |
| 같은 파일:48 `전문검색 = **0 hit**` 및 `매뉴얼 부재` | 이번 범위는 p.1–60이다. KF1-210에서 시간변화 공극률만 확인했다. | “p.1–60의 다공성 이론식은 정지 공극률을 전제로 설명한다. 이 보고서는 매뉴얼 160쪽 전체의 구조 결합 부재를 재검증하지 않았다.” |
| 같은 파일:52 `DENS_ERROR` 및 `그 외 Ch2 분석모델·Ch3 이산화·VOF·k-ε·SMAC·조파·무반사는 … 동일` | KF1-202의 문자열은 DENS-ERROR이다. KF1-025–027·042·050·053의 압축항과 KF1-019의 호출도 다르다. | “키워드는 OPTION DENS-ERROR이다. 공통식의 번호별 대응과 차이는 보고서 §2를 따른다. 장 전체를 동일하다고 요약하지 않는다.” |
| N/source-analysis/cadmas-2f-twophase-compressible-gas.md:22 `PLIC **없음**` | KF1-018·111. FF-SLOPE·FSLP3A 호출이 있다. N/source-analysis/cadmas-surf3d-vof-free-surface.md:75는 이미 `경사면 PLIC`을 설명한다. | “기본 VOF 이류는 donor–acceptor이다. COMP SCHM FF-SLOPE를 선택하면 기울어진 계면을 선분·평면으로 재구성한다.” |
| 같은 2F 소스 노트:30 `**자유표면 포함 기액 2상 3D 비압축성 유체**` | KF1-012·202. 코드 헤더를 그대로 현재 기능 전체로 일반화했다. | “코드 헤더는 비압축성이라고 적는다. 현재 구현은 ISTATE=0의 비압축 기상과 ISTATE=1의 등온 압축성 기상을 선택한다.” |
| 같은 파일:39 `NF>0` 및 `(1-F)(Dρ/Dt)/ρ` | KF1-203·207·219. EOS 호출 조건은 INDC≠-1이다. 미분 계산 조건이 NF>0이다. | “EOS는 INDC≠-1에서 호출한다. 밀도 시간·이류 미분은 NF>0에서 계산한다. DRHODT 자체에는 1-F가 없다. 표면밀도 복사 방향을 별도 후보로 기록한다.” |
| 같은 파일:43·45 `단상 코드 옆에 주석` 및 `← 단상(상수 기상)` | 3D vf_vgene.f:80 `RI=1.0D0/RHO0`. 2F 안의 상수 기상 혼합 주석은 실제 3D 사본과 다르다. | “2F 안에 주석으로 남은 상수 기상 혼합식과 가변 기상 혼합식을 구별한다. 그 주석을 동봉 3D 코드의 원문이라고 부르지 않는다.” |
| 같은 파일:58–64의 대각·RHS 요약 | KF1-204의 비대각 이류 계수가 빠졌다. | “대각·RHS뿐 아니라 6개 방향 이류 계수도 조립한다. AUI의 DRHODP(I-1,J,K)는 I+1 이웃 계수와 모순이다.” |
| 같은 파일:68 `under-relaxation … + … 상대오차` | KF1-201. SERR는 완화 전에 계산한다. MAXITR 기본 1이다. | “순수 기체 NF=8에서 완화 전 밀도 상대오차의 전역 최대값을 계산한다. 그 뒤 RHOG를 완화한다. 기본 최대 반복은 1이다.” |
| N/README.md:22 `슬래밍/충격파압·공기연행에 2상 필요.` | KF1-002의 개발 동기는 성능·필수성 검증이 아니다. | “매뉴얼 p.2–3은 고립 기상 압축이 케이슨 충격압에 미치는 영향을 고려하려는 개발 목적을 설명한다. 이 정적 대조는 적용 정확도를 검증하지 않는다.” |
| N/source-analysis/cadmas-2f-twophase-compressible-gas.md:74 `VF_ACOMPI.h:33-39` | 해당 범위의 앞부분은 IBSUW0이다. ISTATE 주석은 37–39이다. | “ISTATE의 기상 압축 모드는 VF_ACOMPI.h:37–39를 인용한다. COMMON 선언은 1–4를 인용한다.” |
| N/source-analysis/cadmas-surf3d-vof-free-surface.md:75 `ISCMFF≠0`와 `piecewise-linear 평면` | KF1-111·208의 2F 구현도 이 선택과 대응한다. | 이 두 서술은 유지한다. 2F 노트의 PLIC 부재 주장을 이 서술과 맞게 고친다. |
| N/source-analysis/cadmas-surf3d-turbulence-and-porous-resistance.md:36 `GT=0` | KF1-044의 2F 구현도 GT=0이다. | GT 비활성이라는 서술은 유지한다. 일반 부력생성식을 현재 활성 구현으로 바꾸지 않는다. |
| N/source-analysis/cadmas-surf3d-smac-velocity-pressure-solver.md:68 `PP = PP - (RHO0/DTNOW)*PT` | 3D 식이다. 2F vf_vmodif.f:328은 밀도 인자가 없는 압력 갱신이다. | “3D PT와 2F PT의 정규화를 구분한다. 일정 밀도에서 PT2F=ρPT3D이다.” |

## 5 차이 결론

분류별 개수: A 8행, B 32행, C 29행, D 3행, E 10행, F 5행, H 7행, X 0행. 이 절의 결론 표는 일치 이외의 94행이다.

분류별 개수는 이 절 표의 행 ID를 기준으로 센다.
같은 결함의 x·y·z 성분은 §2의 행 ID를 보존하므로 각각 센다.
§4는 같은 발견의 수정안이므로 다시 세지 않는다.
일치 행은 이 절 표에서 제외한다.
H는 사실 오류라는 뜻이 아니라 정적 코드 대조의 대상이 아니라는 뜻이다.
F는 명시한 조건에서 동치인 표기 차이이다.
D와 X는 외부 논문을 읽었다는 뜻이 아니다.

판 차이 A의 공통 근거는 3D vf_a1main.f:33의 `C----------------------------------------------------------2012.03 start`와 2F vf_a1main.f:33의 `C----------------------------------------------------------2016.09 start`이다.
이 날짜는 전체 프로그램의 공식 판 번호가 아니라 코드 안의 날짜 표지이다.
3D의 VF_FGENE 활성 호출 및 VF_BSUWT·VF_BSUWN 호출과 2F의 CAKIY·C2F 주석을 직접 비교했다.
파일 이름의 변경은 `for MG/2FC coupling` 주석을 함께 근거로 쓴다.
매뉴얼 표지에 날짜가 없으므로 정확한 발행 연도를 만들어 붙이지 않는다.

E 후보의 반대 근거와 강도는 다음과 같다.

- KF1-025–027: 해석: 근거 강도 중간. 세 성분이 모두 양의 압축항을 사용한다. 일관된 의도 변경일 가능성을 먼저 검토했다. 코드의 추가 블록에는 그 변경을 설명하는 날짜·부호 변경 사유가 없다. 자체 연속식 주석 vf_vpdrdt.f:79 `C  div v + (1-F)*(dρ/dt)/ρ = 0 の (1-F)*(dρ/dt)/ρ をpoisson方程式に加える`의 뜻은 연속식의 밀도 변화항을 Poisson 식에 더한다는 것이다. 이 연속식과 보존형 이류 플럭스에서 일정 속도를 유지하려면 문서와 같은 음의 항이 필요하다. ISTATE=0 또는 F=1에서는 차이가 소거된다. VF_VEULER는 VF_V1CAL의 현재 호출 경로이다. 실행 결과는 확인하지 않았다.
- KF1-042·050·053: 해석: 근거 강도 중간. p.57–60의 이산식 자체도 압축항을 빠뜨린다. p.5의 온도·농도 Unused와 기본 ISTATE=0는 반대 근거이다. 그러나 입력 해석기는 T·농도를 CALC로 켤 수 있고, 보존형 VF_SEULER는 NF>-1인 기체까지 갱신한다. 같은 코드의 VF_VEULER에는 별도 밀도 변화항이 있다. 일반 압축 모드에서는 스칼라에 같은 보정이 필요한데 호출·소스 모두 이를 전달하지 않는다. 에너지 EOS를 별도로 푼다는 뜻으로 해석하지 않았다.
- KF1-056: 해석: 근거 강도 중간. VF_VPDRDT:98–104도 같은 γv/λv를 사용하므로 반복된 의도일 가능성을 먼저 검토했다. 하지만 VF_V1EOS는 이미 해석 유속 UU·VV·WW를 받고, VF_VPCOEF:421–423의 연속식 유량은 이 추가 비를 곱하지 않는다. 문서 (2.39)와 이 별도 연속식 경로가 동시에 차이를 보인다. 이를 상쇄하는 밀도미분 보정이나 설명 주석은 확인하지 못했다. 일반 셀에서 γv=λv=1이면 소거된다.
- KF1-204: 해석: 근거 강도 강함. 반대 근거를 찾기 위해 VF_V1EOS의 양·음 차분, VF_VPDRDT의 y·z 분기, 행렬을 푸는 경로를 확인했다. 자체 주석 :115는 RHOG(I+1) 차분이다. y·z 분기는 각각 J+1·K+1의 DRHODP를 사용한다. I-1을 상쇄하는 보정은 이 조립·해법·보정 경로에 없다. 양의 x 흐름과 일정 DRHODP에서는 차이가 드러나지 않을 수 있다. 현재 VF_V1CAL:357–360에서 호출한다.
- KF1-206: 해석: 근거 강도 강함. 반대 근거로 3D의 옛 signature·호출과 2F의 정상 K1CAL 호출을 확인했다. 2F SDIFF의 dummy 인수와 실제 T·농도 인수 수·배열 위치가 다르다. k·ε 경로는 FF를 추가한 새 signature와 맞는다. p.5의 Unused 표시는 T·농도 기능의 의도된 비활성이라는 반대 근거이다. 그러나 현재 main은 LEQT·LEQC를 조건으로 해당 루틴을 호출한다. 기본값에서 꺼지는 선택 경로이며, 호출되지 않는 사장 루틴이라고 분류하지 않는다.
- KF1-219: 해석: 근거 강도 강함. 자체 주석은 기체 셀에서 채운다고 적는다. NF 결정 코드와 p.41의 방향 정의는 실제 복사 원점이 액체 쪽임을 보인다. 6개 분기가 모두 같은 방향 관계인 점은 의도 변경의 반대 근거이다. 액체 쪽 EOS 압력을 사용하려고 바꿨다는 설명이나 별도 역전 정의는 확인하지 못했다. 현재 main의 VF_V1EOS에서 실행 가능한 분기이다.

D 행 KF1-052·068·132의 검색은 S 전체에 대해 수행했다.
명령 형식은 `rg -i -n '검색어' "models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators"`이다.
검색은 기본 rg의 텍스트 검색이다. 바이너리 매뉴얼의 문장 부재를 증명하는 검색이 아니다.

| 검색어 | 전체 텍스트 결과 | D 판정에 사용한 원문 |
|---|---|---|
| `sommerfeld\|radiation\|emission\|放射` | 21행. 3D 11행·2F 10행. STR3D·AGENT에는 일치 행 없음. 이 숫자는 실제 rg 출력행 수이다. | 유속의 방사 경계 주석은 있다. scalar 방사 경계 호출은 나오지 않는다. |
| `VF_(B[SW](SS\|KE)\|TGENE\|SGENE\|VPDRDT)` | 90행. 3D 43행·2F 47행. | 2F vf_bwss.f는 IB=1–4 뒤 :112 `CALL VF_A2ERR('VF_BWSS','P.G ERROR.')`이다. vf_bwke.f는 IBK·IBE=1·2·6·8 뒤 :89·110에서 같은 오류를 호출한다. |
| `DRDTU\|DRDTV\|DRDTW\|DRHODP\(I-1,J,K\)` | 9행. 전부 2F. | 운동량 세 성분과 VPDRDT:111·118만 해당한다. 반대 부호의 대체 구현은 이 검색 결과에 없다. |
| `TGENE\|SGENE` | 4행. 3D 2행·2F 2행. STR3D·AGENT에는 일치 행 없음. | 3D vf_t1cal.f:91·2F vf_t1cal.f:94 `CAKIY CALL VF_TGENE`; 3D vf_s1cal.f:96·2F vf_s1cal.f:100 `CAKIY   CALL VF_SGENE`. 모두 주석 호출이다. 활성 호출과 해당 SUBROUTINE 선언은 검색되지 않았다. |

위 첫 두 검색은 “0 hit”가 아니다.
유속의 방사 경계 존재와 스칼라 경계 부재를 구분했다.
스칼라 분기 본문을 nl -ba로 열어 검색 결과를 보강했다.

| 행 ID | 항목 | 결론 | 근거(원문 인용) | 노트에 쓸 결론 문장 |
|---|---|---|---|---|
| KF1-002 | 개발 목적·충격압 적용 | H | 2F manual p.2 `the volume of the isolated gas phase region can not change`. | 매뉴얼은 고립 기상 압축을 고려하려는 개발 목적을 설명한다. 이 대조는 충격압 정확도를 검증하지 않는다. |
| KF1-009 | 그림의 ASCII 공극률 입력 누락 | C | 2F vf_ip1inp.f:59–62의 `FILE=TRIM(MGNAME(MGRANK+1))//'.poro.ascii',`와 전체 OPEN은 §3.1에 인용했다. p.4 그림에는 이 입력이 없다. | 코드는 ASCII 공극률 파일도 읽는다. 파일 이름의 판 차이는 KF1-220을 따른다. |
| KF1-011 | 후처리 흐름 | H | 2F manual p.4 `Word`, `Spread Sheet`, `Viewer`. | 그림은 외부 편집·그리기 도구의 연결을 설명한다. 해당 도구 내부는 이번 코드 대조 대상이 아니다. |
| KF1-012 | 무조건적인 비압축성 서술 | B | p.5·7·9 `incompressible`과 p.24 식 (2.38) \(\rho_G=\rho_G(p)\)가 같은 문서에 있다. | 액상은 비압축성이다. 기상은 ISTATE에 따라 비압축 또는 압축 모드를 선택한다. |
| KF1-016 | 온도·농도의 Unused 표시 | B | p.5 `(Unused)Energy equation`; 2F vf_iiequa.f:45–46 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'CALC'  ) THEN` / `LEQT=1`. | 온도·농도는 기본적으로 꺼져 있다. 입력 해석기와 메인은 선택 계산 경로를 남겼다. 정상 동작을 보장하는 판정은 아니다. |
| KF1-018 | 계면 경사의 unused 표시 | B | p.6 `(unused)Method considering inclination of interface`; p.11 `can also be selected`; 2F vf_iicomp.f:45–46 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'FF-SLOPE') THEN` / `ISCMFF=1`. | FF-SLOPE 선택과 실제 재구성 호출이 존재한다. 기능표의 unused 표시는 잘못되었다. |
| KF1-019 | 3D 자유수면 속도 처리 잔존 | A | 날짜 표지는 3D vf_a1main.f:33 `C----------------------------------------------------------2012.03 start`, 2F :33 `C----------------------------------------------------------2016.09 start`이다. 3D vf_v1cal.f:293의 활성 CALL과 2F :390의 `C2F   CALL VF_BSUWT (XX,YY,ZZ,UU,VV,WW,DBUF,NF,INDX,INDY,INDZ)`가 다르다. | 3D의 자유수면 속도 외삽 설명을 현재 2F 실행 경로로 적용하지 않는다. |
| KF1-021 | 그래픽 기능 | H | p.6 `2D only in drawing section`. | 그리기 기능 설명은 수치 연산의 구현·성능 판정과 구분한다. |
| KF1-022 | 기능표 범례 | H | p.6 `◎：今回実現した機能，×：今回は実現しなかった機能`. 뜻: ◎는 이번 구현, ×는 이번 미구현. | 이 행은 기능표 기호의 뜻을 정한다. 별도 수치 연산식이 아니다. |
| KF1-025 | x 운동량 압축항 부호 | E | p.9 식 (2.2)는 \(-u(1-F)\dot\rho_G/\rho_G\)이다. 2F vf_veuler.f:152 `UU(I,J,K)=(GV*UUO(I,J,K)+DTNOW*(DU+DRDTU))/GV0`. 연속식과 반대 근거는 위 E 검토에 인용했다. | 해석: x 운동량의 압축항 부호는 결함 후보이다. 근거 강도는 중간이다. |
| KF1-026 | y 운동량 압축항 부호 | E | p.9 식 (2.3)는 \(-v(1-F)\dot\rho_G/\rho_G\)이다. 2F vf_veuler.f:218 `VV(I,J,K)=(GV*VVO(I,J,K)+DTNOW*(DV+DRDTV))/GV0`. | 해석: y 운동량의 압축항 부호는 결함 후보이다. 근거 강도는 중간이다. |
| KF1-027 | z 운동량 압축항 부호 | E | p.9 식 (2.4)는 \(-w(1-F)\dot\rho_G/\rho_G\)이다. 2F vf_veuler.f:284 `WW(I,J,K)=(GV*WWO(I,J,K)+DTNOW*(DW+DRDTW))/GV0`. | 해석: z 운동량의 압축항 부호는 결함 후보이다. 근거 강도는 중간이다. |
| KF1-029 | 실질미분의 점 누락 | B | p.10의 두 번째 \(\rho_G\) 정의와 p.24 식 (2.39)의 \(\dot\rho_G\)를 비교했다. | p.10에서 실질미분을 뜻하는 기호는 점 있는 기호로 고친다. |
| KF1-032 | 깨진 참조·계단함수 문구 | B | p.10 `エラー! 参照元が見つかりません。`의 뜻은 오류! 참조 원본을 찾을 수 없습니다. p.11은 `not fluid / not`이다. | 참조 문자열과 계단함수 설명은 편집 오류이다. 코드의 F 갱신식과 구분한다. |
| KF1-034 | 조파원 채택 문장의 잔존 | A | 3D vf_f1cal.f:155 `CALL VF_FGENE(XX,YY,FF,SRCUV,QF,NF)`와 2F :143 `CAKIY CALL FGENE(XX,ZZ,FF,WVU,QF,NF)`가 다르다. 날짜 표지는 KF1-019와 같다. p.14는 `Wave source(Unused)`이다. | 2F의 조파원은 비활성이다. p.13의 채택 문장은 3D 설명이 남은 것으로 처리한다. |
| KF1-037 | 조파원 기본식 | A | p.14 식 (2.10)–(2.15)는 3D manual p.14와 같다. 활성·주석 호출의 원문은 KF1-034이다. | 이 식들은 미사용 조파원 이론이다. 현재 2F 소스항으로 계산된다고 쓰지 않는다. |
| KF1-039 | 감쇠대 폭·성능 설명 | H | p.15 `1 to 3 wavelengths`. | 파장 1–3배는 문서의 적용 설명이다. 코드가 강제하는 폭의 범위가 아니다. |
| KF1-041 | 난류 변동량의 수학적 정의 | H | p.16 식 (2.20) \(k=\frac12(u'^2+v'^2+w'^2)\)와 식 (2.21). | 변동 속도에서 정의한 k·ε를 RANS 코드가 직접 평가한다고 쓰지 않는다. |
| KF1-042 | k·ε 압축항 부재 | E | p.17 식 (2.22)–(2.23)의 추가 압축항과 2F vf_k1cal.f:152–153의 VF_SEULER 호출을 비교했다. 전체 호출은 KF1-042에 인용했다. vf_kgene.f:169 `GT =0.0D0`와 :180–182의 QK·QE에도 해당 항이 없다. | 해석: 압축 모드의 k·ε 소멸항 부재는 결함 후보이다. 근거 강도는 중간이다. |
| KF1-044 | GT 식과 실제 소스 | B | p.17 식 (2.25)는 부력생성식을 제시한다. p.58 식 (3.116)–(3.117)은 GT를 빼고 적는다. 2F vf_kgene.f:169 `GT =0.0D0`. | 문서의 GT 일반식은 현재 코드에서 계산하지 않는다. 같은 문서의 이산식도 일반식과 다르다. |
| KF1-045 | Rf 분모 하한 | C | 2F vf_kgene.f:171 `RF =-GT/MAX(GST,ZERO)`; p.17 식 (2.26)은 하한 없는 분모이다. | 코드는 Rf 분모에 ZERO 하한을 적용한다. 현재 GT=0이므로 Rf도 0이다. |
| KF1-046 | 와동점성의 ε 하한 | C | 2F vf_cnut0.f:46 `W=MAX(AE(I,J,K),AKMINE)`; p.17 식 (2.27)은 ε를 그대로 나눈다. | 코드는 와동점성 분모에 AKMINE 하한을 적용한다. |
| KF1-050 | 온도 압축항 부재 | E | p.18 식 (2.32)의 추가 항과 2F vf_t1cal.f:99 `CALL VF_SEULER(XX,YY,ZZ,TT,GGV,GGV ,DBUF,FLTU,FLTV,FLTW,QT,NF)`를 비교했다. :76 `QT  (I,J,K)=0.0D0`. | 해석: 압축 모드의 온도 소멸항 부재는 결함 후보이다. 근거 강도는 중간이다. 확산 호출 문제는 별도로 적용한다. |
| KF1-052 | 온도 조파 소스 | D | 전체 S의 `rg -i -n 'TGENE\|SGENE'`는 위 검색표의 4행을 반환했다. 2F vf_t1cal.f:94와 3D :91은 모두 `CAKIY CALL VF_TGENE`이다. | 온도 조파 소스식은 문서에 있다. 활성 구현은 확인되지 않는다. 두 코드 사본의 판 차이로 분류하지 않는다. |
| KF1-053 | 농도 압축항 부재 | E | p.18 식 (2.35)의 추가 항과 2F vf_s1cal.f:79 `QC  (I,J,K)=0.0D0`를 비교했다. :105–106의 VF_SEULER 호출 전체는 KF1-053에 인용했다. | 해석: 압축 모드의 농도 소멸항 부재는 결함 후보이다. 근거 강도는 중간이다. |
| KF1-056 | 밀도 이류의 추가 공극률 비 | E | p.24 식 (2.39)에는 γv/λv가 없다. 2F vf_v1eos.f:118 `GV = GGV(I,J,K)/GLV(I,J,K)`. :119–124의 전체 WUC·WVC·WWC 식은 KF1-056에 인용했다. | 해석: 밀도 이류 계수의 추가 γv/λv는 결함 후보이다. 근거 강도는 중간이다. 일반 셀에서는 차이가 소거된다. |
| KF1-063 | 자유수면 압력·속도 경계 | A | 3D vf_v1cal.f:293–295의 활성 표면 호출과 2F :390–392의 C2F 주석 호출이 다르다. p.21은 \(p_s=p_{GAS}\)이다. 두 날짜 표지는 KF1-019에 인용했다. | 3D의 자유수면 경계표를 2F의 공통 압력·속도 해석과 동일하게 취급하지 않는다. |
| KF1-066 | 스칼라 열·확산 유속의 기체 예외 | C | 2F vf_bwss.f:94–95 `IF (NC.EQ.8) THEN` / `BCS(L)=0.0D0`; :103–104도 같다. | 열·확산 유속과 전달 경계는 기체에 접하면 0 경계값을 사용한다. 표는 이 예외를 적지 않는다. |
| KF1-068 | 스칼라 Sommerfeld 경계 | D | 위 전체 S의 방사 관련 검색은 21행이다. 스칼라 경계 관련 검색은 90행이다. 2F vf_bwss.f:112 `CALL VF_A2ERR('VF_BWSS','P.G ERROR.')`; vf_bwke.f:89·110도 오류 분기이다. | 스칼라 방사 경계는 표에만 있다. 유속 방사 경계의 존재를 스칼라 구현의 근거로 쓰지 않는다. |
| KF1-069 | 스칼라 자유수면 처리의 분리 | A | 2F vf_k1cal.f:181 `C2F   CALL VF_BSSS(AK,DBUF,NF)`; 3D :168 `CALL VF_BSSS(AK,DBUF,NF)`. 2F vf_t1cal.f:105의 T 호출은 활성이다. 날짜 표지는 KF1-019이다. | 2F는 k·ε의 표면 복사를 끈다. T·농도의 표면 복사는 계산 경로에 남아 있다. |
| KF1-070 | 모델명의 C | B | p.25 `CADMAS-SURF/3D-2FC`; 표지 p.1 `CADMAS-SURF 3D-2F`; 2F vf_a1main.f:5 `CDT   VF_A1MAIN:CADMAS-SURF/3D-2Fのメインルーチン`. 뜻: 3D-2F 메인 루틴. | p.25의 C를 별도 판 번호로 해석하지 않는다. 문서 안 모델명 표기의 오류이다. |
| KF1-072 | 이류 차분 설명 | B | p.25 (4)는 `other than the advection term`을 두 번 적는다. p.6은 이류항의 상류·중앙·DONOR 선택을 명시한다. | 비이류항은 중앙차분이다. 이류항은 선택한 DONOR 가중치를 사용한다. |
| KF1-074 | 시간 이산 연속식의 압축항 누락 | B | p.9 식 (2.1)의 추가 항이 p.27 식 (3.3)에 없다. 2F vf_vpdrdt.f:156 `BB(I,J,K) = BB(I,J,K) + AVL*DRHODT(I,J,K)`. | 식 (3.3)은 ISTATE=0 조건의 골격이다. 압축 모드 전체의 이산식으로 사용하지 않는다. |
| KF1-076 | Gy 열거 누락 | B | p.27 본문은 Gx·Gz만 나열한다. 같은 쪽 식 (3.5)·(3.8)은 \(G_y(u^n,v^n,w^n)\)를 사용한다. | 설명문에 Gy를 추가한다. 코드의 y 성분 계산은 존재한다. |
| KF1-077 | φ와 PT의 정규화 | F | p.28 식 (3.10)과 2F vf_vmodif.f:328 `PP(I,J,K)=PP(I,J,K)-PT(I,J,K)/DTNOW`. | 일정 밀도에서 PT=ρφ로 두면 압력·속도 보정식은 같다. PT와 φ의 단위를 구분한다. |
| KF1-078 | y 발산의 γ 첨자 | B | p.28 식 (3.14)은 \(\partial(\gamma_vv^{n+1})/\partial y\)이다. p.27 식 (3.3)은 γy이다. 코드의 전체 발산은 KF1-023에 인용했다. | 식 (3.14)의 해당 γv는 γy의 오기이다. |
| KF1-079 | 비압축 Poisson과 압축 모드 | B | p.28 식 (3.18)과 p.37–39의 식은 밀도미분 행렬을 포함하지 않는다. 2F vf_v1cal.f:357–360의 VF_VPDRDT 호출 전체는 KF1-079에 인용했다. | p.1–60의 Poisson 유도만으로 압축 모드의 전체 행렬을 설명하지 않는다. |
| KF1-082 | 제어체적 그림의 y 폭 | B | p.31 그림은 \(\Delta y_i\)이다. p.29 식 (3.24)는 \(\Delta y_j=y_{j+1}-y_j\)이다. | 그림 오른쪽의 y 폭 첨자는 j이다. |
| KF1-084 | z 운동량의 y 수송 속도 | B | p.32 식 (3.36)의 \(-\lambda_yuw\)와 p.36 FLWV 정의의 \(-\lambda_yvw\)가 모순이다. 2F vf_vflxdw.f:266–271의 전체 이류식은 §3.1에 인용했다. | 식 (3.36)의 y 이류항은 v로 w를 수송해야 한다. |
| KF1-087 | 교차 플럭스 보간 표기 | B | p.30 식 (3.30)은 바닥괄호에 같은 쪽 폭을 가중한다. 2F vf_vflxdu.f:121 `GG=XX(6,I)*(XX(2,I-1)*GGY(I,J,K)+XX(2,I)*GGY(I-1,J,K))`. | 교차 플럭스의 코드는 반대쪽 폭으로 선형 보간한다. 문서의 바닥괄호 정의와 비균등 격자에서 다르다. 방향 위첨자의 별도 오류도 적용한다. |
| KF1-089 | 운동량의 조파 소스 | A | 2F vf_vgene.f:132 `CAKIY         * 造波ソース` 뒤에는 소스 대입이 없다. 뜻: 조파원. 3D 활성 조파 경로와 날짜 표지는 KF1-034·019이다. | 식 (3.48)·(3.59)·(3.70)은 현재 2F에서 비활성인 조파원의 이론식이다. |
| KF1-091 | yz 전단의 보간 축·분모 | B | p.35 식 (3.54)–(3.55)은 Δz·Δx·δyi를 인쇄한다. 2F vf_vflxdv.f:282 `GG=YY(6,J)*(YY(2,J-1)*GGZ(I,J,K)+YY(2,J)*GGZ(I,J-1,K))`; :289 `D2=YY(5,J)*(WW(I,J,K)-WW(I,J-1,K  ))`. | yz 전단은 y·z 방향 보간과 δyj를 사용한다. 두 매뉴얼의 전단 미분과 더하기 기호는 코드와 같다. |
| KF1-094 | z 이류 평균·저항의 문자 | B | p.36 식 (3.65)의 \(\delta w\)는 정의되지 않는다. p.37 식 (3.69)은 루트 앞에 v를 쓴다. 2F vf_vgene.f:224 `W=WW(I,J,K)`; 전체 저항식은 KF1-094이다. | 평균 위첨자는 δz이다. z 저항의 루트 앞 속도는 w이다. |
| KF1-095 | 부력의 실제 밀도차 모델 | C | 2F vf_vgene.f:241 `DR=DR-TDR0*(T-TDT0)`; :245 `DR=DR-CDR0(LC)*(C-CDC0(LC))`; :248 `QW(I,J,K)=QW(I,J,K)-GV*GRZ0*DR/RHO0(1)`. | 코드는 온도·농도 기준값에 대한 선형 밀도차를 부력에 더한다. 유동 영향 무시는 해당 계수가 0일 때 유지된다. |
| KF1-097 | 압력 행렬 부호·밀도 정규화 | F | 2F vf_vpcoef.f:174 `ALI(I,J,K)=-AIM`; :418 `AD(I,J,K)=AKM+AJM+AIM+AIP+AJP+AKP`; :430 `BB(I,J,K)=VD-VQ`. | 일정 밀도에서 Ac=−Ad/ρ, Bc=−Bd, PT=ρφ를 함께 적용하면 같은 선형계이다. |
| KF1-098 | 압력 행렬의 인쇄 첨자 | B | p.38 식 (3.79)의 \(A^D_{i,j,.k}\), 식 (3.81)–(3.84)의 \(\Delta z_z\). 2F vf_vpcoef.f:157 `AXZ=XX(2,I)*ZZ(2,K)`. | 대각 첨자의 점을 삭제한다. z 폭 첨자는 k이다. |
| KF1-099 | α와 코드 계수 | F | p.38 식 (3.87)–(3.89)의 α와 2F vf_vpcoef.f:173 `AIM=AYZ*XX(5,I)*GGX(I,J,K)*GV*RI`. | 일정 밀도에서는 코드 계수에 α/ρ가 들어간다. PT=ρφ 변환과 함께 비교한다. |
| KF1-100 | Poisson 우변의 y 폭 | B | p.39 식 (3.90)은 \(\Delta y_k\)이다. 2F vf_vpcoef.f:157 `AXZ=XX(2,I)*ZZ(2,K)`. | y 발산의 분모는 Δyj이다. 체적 적분의 y 면적은 AXZ이다. |
| KF1-101 | 공간 보정식과 PT | F | p.40 식 (3.91)–(3.94)와 2F vf_vmodif.f:328 `PP(I,J,K)=PP(I,J,K)-PT(I,J,K)/DTNOW`. 속도 보정의 전체 식은 KF1-077·101과 §3.1에 인용했다. | 일정 밀도의 공간 보정식도 PT=ρφ에서 동치이다. |
| KF1-103 | NF 분류의 허용오차·임시 상태 | C | 2F vf_fnfini.f:49 `IF (FF(I,J,K).LT.FLOWER) THEN`; :123 `NF(I,J,K)=7`; :189 `IF (NF(I,J,K).EQ.-7) NF(I,J,K)=8`. | 실제 분류는 FLOWER·FUPPER 임계값과 임시 NF를 사용한다. 정확한 F=0 검사만 수행한다고 쓰지 않는다. |
| KF1-105 | 기포·물방울 보조 처리 | C | 2F vf_f1cal.f:191 `IF (WBUB.GE.ZERO) THEN`; :192 `CALL VF_FBUBUP(ZZ,FF,GGV,TBUB,DBUF,NF)`; :195–199의 물방울 호출 전체는 §3.2이다. | 표면 분류 외에 TimerDoor와 재분류가 존재한다. 격자 이하 물방울·기포를 단순히 모두 삭제한다고 요약하지 않는다. |
| KF1-108 | VOF 조파 소스 | A | 2F vf_f1cal.f:123 `QF  (I,J,K)=0.0D0`; :143 `CAKIY CALL FGENE(XX,ZZ,FF,WVU,QF,NF)`; 3D 활성 호출은 KF1-034이다. | 식 (3.97)의 VOF 조파 소스는 현재 2F에서 비활성이다. |
| KF1-109 | donor–acceptor 그림의 AD | B | p.46은 세 칸 모두 `Let suffix AD be D`이다. p.45의 FAD 정의는 수직 계면 외에 FA를 사용한다. 2F vf_fconv.f:87 `FAD=FA`. | 그림의 풍하 선택 두 칸은 AD=A로 고친다. 부호별 D·A 위치는 유지한다. |
| KF1-112 | 법선 차분의 이웃 예외 | C | 2F vf_fconvs.f:335–339 `IF (DM+DP.LE.ZERO) THEN` / `S3=0.0D0` / `ELSE` / `S3=(FM-FP)/(DM+DP)` / `ENDIF`. | 법선 차분은 벽·상태별 이웃 보정과 0 간격 검사를 포함한다. 일반 중심차분식만으로 전체 처리를 설명하지 않는다. |
| KF1-115 | 퇴화 법선의 ε 값 | C | 2F vf_fconvs.f:351–353 `IF (ABS(S1).GE.1.0D-4) I1=1` / `IF (ABS(S2).GE.1.0D-4) I2=1` / `IF (ABS(S3).GE.1.0D-4) I3=1`. | 정규화한 법선 성분의 패턴 임계값은 10⁻⁴이다. 문서는 ε의 수치를 적지 않는다. |
| KF1-117 | 패턴 제목·참조 | B | p.52의 두 번째 `P1-1` 제목과 뒤 문장의 `this is a pattern of P1-3`가 모순이다. | 두 번째 패턴 제목은 P1-3이다. P1-2 조건과 H1·H2 값은 유지한다. |
| KF1-118 | 면적 전개의 η2 | B | p.53 식 (3.101)의 한 줄은 \(2n_1\eta_2\)이다. 같은 식의 다른 줄과 p.54 계수식은 \(2n_1n_2\)이다. | 미정의 η2를 n2로 고친다. |
| KF1-119 | 재구성 다항식의 배율 | F | 2F vf_fslp2a.f:45 `CNS=2.0D0*SS(1)*SS(2)`; :48 `VIN=VMX*FVAL`; :56–57 `CX=C-VIN` / `CALL VF_CROOT2(A,B,CX,XX1,XX2,NRT)`. | 코드는 면적식 양변에 2n1n2를 곱한 다항식을 푼다. 명시한 비퇴화 조건에서 같은 식이다. |
| KF1-121 | 면적식의 P·p 혼용 | B | p.55 식 (3.104)·(3.106), p.57 식 (3.110)은 조건에서 P를 정의하고 우변에 p를 쓴다. | P와 p는 같은 기하 절편이다. 압력 변수를 새로 도입한 식으로 읽지 않는다. |
| KF1-122 | P2-2의 왼쪽 띠 면적 | B | p.57 식 (3.110)의 \(p_0\ge c_1:V_*=V_{give}-p_0\Delta c_2\)와 같은 쪽 그림 0-3-12(d)를 비교했다. | 이 분기의 왼쪽 띠 면적은 c1Δc2이다. 문서식은 c1=0에서도 전체 유체 면적을 반환하지 못한다. |
| KF1-124 | ε 이산식의 y 폭 | B | p.58 식 (3.113)의 \(\Delta y_i\)와 p.57 식 (3.112)의 \(\Delta y_j\)가 다르다. 2F vf_seuler.f:50–53의 전체 갱신식은 KF1-129이다. | ε 플럭스의 y 폭 첨자를 j로 고친다. |
| KF1-126 | 난류 소스의 분모 하한 | C | 2F vf_kgene.f:174 `AK0=MAX(AK(I,J,K),AKMINK)`; :176 `AEK=AE0/AK0`. QK·QE 전체 식은 KF1-126이다. | 난류 소스는 k 분모에 AKMINK 하한을 적용한다. 갱신 뒤 k·ε 컷오프도 존재한다. |
| KF1-127 | Gs 본문의 A·첨자 | B | p.58 `A in the equations (3.116) and (3.117)`과 \(G_{s_{i,k}}\). 두 식에 A는 없다. | 본문의 대상은 Gs이다. 셀 첨자는 i,j,k이다. |
| KF1-128 | Gs의 y 법선 미분 | B | p.59 식 (3.118)은 \((v_{i+1,j,k}-v_{i,j,k})/\Delta y_j\)이다. 2F vf_kgene.f:151 `DLR=YY(4,J)`; :153 `DVDY=DLR*(VYP-VYM)`. | y 법선 미분의 양측 속도는 j+1과 j에서 취한다. |
| KF1-131 | 온도 소스 단위 | B | p.60 식 (3.122)은 \(QT=(\rho c_pTq)_{i,j,k}\)이다. p.18 식 (2.32)은 소스에 \(\gamma_v/(\rho c_p)\)를 곱한다. p.59 식 (3.119)은 QT를 직접 더한다. | 식 (3.122)은 온도 시간변화율로 정규화한 소스와 다르다. 현재 QT=0인 실행과 구분한다. |
| KF1-132 | 농도 조파 소스 | D | 전체 S의 `TGENE`·`SGENE` 검색은 4개 주석 호출만 반환했다. 2F vf_s1cal.f:100과 3D :96은 `CAKIY   CALL VF_SGENE`이다. | 농도 조파 소스식은 문서에 있다. 활성 구현은 확인되지 않는다. |
| KF1-133 | 온도·농도 플럭스 열거 | B | p.59는 `FLTU`를 두 번 나열한다. p.60은 `FLCU`를 두 번 나열한다. 같은 쪽 이산식은 U·V·W 세 방향을 사용한다. | 본문의 플럭스 이름 열거는 편집 오류이다. 식의 실제 세 방향을 기준으로 설명한다. |
| KF1-135 | 파속 정의·인용 파형 이론 | H | p.13 `second definition of the wave velocity`. p.12는 정칙 진행파의 세 방법을 열거한다. | 이론 정의와 인용 소개는 구현 차수 대조와 구분한다. 문서가 제시하지 않은 외부 논문 계수를 검증했다고 쓰지 않는다. |
| KF1-136 | 자유수면 그림의 벽면 표시 | B | p.20 오른쪽의 `壁面`과 캡션 `Suffix on wall and free surface`가 모순이다. 일본어 표시는 벽면이라는 뜻이다. | 오른쪽 그림은 자유수면이다. 벽면 표시는 오기이다. |
| KF1-137 | xy 전단의 보간 축·분모 | B | p.34 식 (3.50)–(3.51)의 Δx·δyi와 2F vf_vflxdv.f:122 `GG=YY(6,J)*(YY(2,J-1)*GGX(I,J,K)+YY(2,J)*GGX(I,J-1,K))`를 비교했다. | λxu·γx의 보간 방향은 y이다. y 간격 첨자는 j이다. |
| KF1-138 | 압력 차 미분·편집 참조 | B | p.28 식 (3.11)–(3.13)의 \(\partial P^{n+1}-P^n\), p.31 `Figure III - 3 - 2`, p.34–35의 깨진 참조 문자열은 KF1-138에 인용했다. | 미분 기호는 압력 차 전체에 적용한다. 그림 번호와 깨진 참조를 고친다. 중복 설명을 추가 계산 절차로 읽지 않는다. |
| KF1-201 | 밀도 반복의 기본값·오차 | C | 2F vf_a2dflt.f:48 `MAXITR=1`; vf_a1main.f:1359 `IF(NF(I,J,K).EQ.8) THEN`; :1385 `IF(SERR.LE.SERROR) EXIT`. 오차·완화의 전체 식은 KF1-201이다. | 기본 최대 반복은 1회이다. 순수 기체의 완화 전 밀도 상대오차로 종료를 판단한다. |
| KF1-202 | STATE·DENS-ERROR | C | 2F vf_iiopt.f:81 `ELSEIF (TEXT(IS(2):IE(2)).EQ.'STATE') THEN`; :90 `ELSEIF (TEXT(IS(2):IE(2)).EQ.'DENS-ERROR') THEN`; vf_a2dflt.f:47 `ISTATE=0`. | 기본 기상은 비압축성이다. STATE 1은 등온 EOS를 선택한다. 완화계수의 상한 1 검사는 없다. |
| KF1-203 | 밀도 배열·COMMON·단위 | C | 2F vf_a1main.f:366 `ALLOCATE(DRHODT(NUMI,NUMJ,NUMK),STAT=IERR)`; VF_ACOMPI.h:1–4와 VF_ACOMPR.h:1–5의 연속 COMMON 선언은 §3.1이다. | DRHODP는 정규화 압력미분이다. DRHODT는 정규화 밀도미분이다. 1-F는 소비 위치에서 곱한다. |
| KF1-204 | AUI의 x 이웃 첨자 | E | 2F vf_vpdrdt.f:118 `AUI(I,J,K) = AUI(I,J,K) + DCOEF*DRHODP(I-1,J,K)`; :134 `AUJ(I,J,K) = AUJ(I,J,K) + DCOEF*DRHODP(I,J+1,K)`; 자체 :115의 RHOG(I+1) 차분 주석은 KF1-204이다. | 해석: 음의 x 흐름에서 AUI가 왼쪽 밀도미분을 사용하는 처리는 결함 후보이다. 근거 강도는 강함이다. 현재 호출 경로에서 실행 가능하다. |
| KF1-205 | 면 혼합 밀도·PT 차원 | C | 2F vf_vpcoef.f:171 `RI=1.0D0/(FX(I,J,K)*RHO0(1)+(1.0D0-FX(I,J,K))*RHO02)`; vf_vmodif.f:328 `PP(I,J,K)=PP(I,J,K)-PT(I,J,K)/DTNOW`. | 압력 연산은 면 혼합 역밀도를 사용한다. PT 차원은 Pa·s이다. |
| KF1-206 | T·농도 SDIFF 인수 | E | 2F vf_sdiff.f:1–2의 18개 dummy와 vf_t1cal.f:90–91·vf_s1cal.f:95–97의 17개 실제 인수 전체는 KF1-206이다. 정상 k·ε 호출과 3D의 옛 signature를 반대 근거로 확인했다. | 해석: T·농도의 FF 인수 누락은 결함 후보이다. 근거 강도는 강함이다. 기본값에서는 꺼지지만 CALC 또는 양의 성분 수를 주면 호출 가능한 경로이다. |
| KF1-207 | 표면 밀도 복사·차분 제한 | C | 2F vf_v1eos.f:89 `RHOG(I,J,K)   = RHOG  (I-1,J,K)`; :126–138의 전체 이웃 조건은 §3.1이다. | 표면밀도 복사와 액체 쪽 밀도 차분 제한을 EOS 처리에 함께 기록한다. 복사 방향 문제는 별도 E 후보이다. |
| KF1-208 | DONOR·FF-SLOPE 입력 | C | 2F vf_iicomp.f:35 `IF     (TEXT(IS(3):IE(3)).EQ.'VP-DONOR') THEN`; :45 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'FF-SLOPE') THEN`; vf_a2dflt.f:41 `ISCMFF=0`; :64 `SCMVP =1.0D0`. | 기본 VOF는 donor–acceptor이다. 기본 운동량 이류는 1차 상류이다. DONOR 가중치 범위는 0–1이다. |
| KF1-209 | 난류상수·벽상수 입력 | C | 2F vf_iimdl.f:209 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'PARAMETER') THEN`; :229 `ELSEIF (TEXT(IS(3):IE(3)).EQ.'PRANDTL'  ) THEN`; vf_a2dflt.f:190 `AKPR  =1.0D0`. | 난류·벽 상수는 입력으로 바꿀 수 있다. Prt와 성분별 난류 Schmidt 수의 기본값은 1이다. |
| KF1-210 | 움직이는 공극률·속도 제한 | C | 2F vf_vgene.f:130 `QU(I,J,K)=QU(I,J,K)+(GV1-GV)*DTI*U`; vf_a2dflt.f:226 `VVMAX=30.0D0`; vf_veuler.f:155 `IF (UU(I,J,K).GT. VVMAX) UU(I,J,K)= VVMAX`. | 공극률 시간변화와 속도 상한은 코드의 추가 처리이다. 정지 다공체 이론식과 구분한다. |
| KF1-211 | 감쇠대 중첩·방사 가중치 | C | 2F vf_veuler.f:167 `IF (D.GT.DMAX) DMAX=D`; vf_bwuwn.f:467–468 `ALN=MIN(C*DTNOW/XX(2,IC-IP),1.0D0)` / `ALT=MIN(ALN*2.0D0          ,1.0D0)`. | 중첩 감쇠대는 최대 감쇠계수를 사용한다. 방사 경계는 법선·접선에 서로 다른 제한 가중치를 사용한다. |
| KF1-212 | 작은 F·벽 도너 예외 | C | 2F vf_fconv.f:93 `IF (FDMW.LT.FLOWER .AND. FA.LT.FLOWER) FDM=MAX(FDM,0.1D0)`; :78 `FD=BCF(INDX(I,J,K))`. | donor–acceptor는 작은 F에서 FDM 하한 0.1을 추가한다. 벽 도너는 BCF를 사용한다. |
| KF1-213 | 법선의 정규화 | C | 2F vf_fconvs.f:342 `RN=S1*S1+S2*S2+S3*S3`; :344 `RN=1.0D0/SQRT(RN)`; 전체 조건은 KF1-213이다. | 코드는 −∇F를 단위 법선으로 바꾼 뒤 패턴을 분류한다. |
| KF1-214 | 재구성 근의 선택·보정 | C | 2F vf_fslp2a.f:87 `EP=XMX*1.0D-6`; :95 `AA=(XL+XR)/2.0D0`; NRT와 구간 조건은 KF1-214이다. | 근이 없으면 오류이다. 근이 허용 구간을 벗어나면 경고 뒤 구간 중점을 사용한다. |
| KF1-215 | F 컷오프·유체량 집계 | C | 2F vf_fcut01.f:42 `FCUT=FCUT+(FF(I,J,K)-1.0D0)*V`; :48 `FSUM=FSUM+FF(I,J,K)*V`; vf_a2dflt.f:58 `FEPS  =1.0D-6`. | 코드는 F를 0 또는 1로 자른 변화량을 FCUT으로 집계한다. 문서는 이 보존량 변화를 설명하지 않는다. |
| KF1-216 | solver·시간 설정과 실패 검사 | C | 2F vf_a2dflt.f:37–38 `ICGTYP=1` / `ICGMAX=500`; vf_vpsol.f:76–81의 전체 오류 조건은 §3.1이다. 시간 모드 기본값은 :231 `IDTTYP=1`이다. | 기본 해법은 MILU-BiCGSTAB이다. ILU 대안과 수렴·시간 설정은 입력으로 바꿀 수 있다. 해법 실패 조건도 기록한다. |
| KF1-217 | 벽 법칙 Newton 실패 | C | 2F vf_cloglw.f:32 `NI=20`; :34 `EPS=1.0D-10`; :51 `IF (ABS(DX).GE.XX*EPS) CALL VF_A2ERR('VF_CLOGLW','NOT CONVERGED.')`. | 마찰속도 계산은 최대 20회의 Newton 반복을 사용한다. 상대 증분이 기준을 만족하지 못하면 오류를 낸다. |
| KF1-218 | 난류 하한·열 시간제한의 밀도 | C | 2F vf_k1cal.f:169–174의 컷오프는 KF1-218이다. vf_cdtcal.f:81 `RHO2=FF(I,J,K)*RHO0(1)+(1.0D0-FF(I,J,K))*RHO0(2)`. | 난류량은 갱신 뒤 하한을 적용한다. 열 확산 시간제한은 EOS 밀도를 사용하지 않는다. |
| KF1-219 | 표면 기상밀도 복사 방향 | E | 2F vf_v1eos.f:83 `C 表面セルの気相密度は、気体セルから埋め込む`. 뜻: 표면 셀 기상밀도는 기체 셀에서 채운다. :89 `RHOG(I,J,K)   = RHOG  (I-1,J,K)`; vf_fnfprv.f:164·187의 NF=1 조건은 §3.2이다. | 해석: 액체 쪽을 복사하는 구현은 자체 주석과 NF 정의에 모순이다. 결함 후보의 근거 강도는 강함이다. 현재 EOS 호출 경로에서 실행 가능하다. |
| KF1-220 | 파일 이름의 판 차이 | A | 2F vf_ii1inp.f:125 `C----------------------------------------------------for MG/2FC coupling`; :126 `C       OPEN(MFILIN,ERR=9010,FILE='data.in',`. 현행 전체 OPEN은 §3.1이다. 두 날짜 표지는 KF1-019이다. | 현행 파일 이름은 MGNAME을 사용한다. 병렬 출력의 5자리 접미사와 대표 프로세스의 단일 tran을 구분한다. |
| KF1-221 | 수직 조파 속도 보정 | C | p.13은 x 또는 y 방향 U의 수심비 보정만 설명한다. 2F vf_bwuwn.f:348 `BCW(L,2)=UT*VWS*AW`. | 코드는 수직 조파 속도에도 VWS를 곱한다. |
| KF1-222 | TimerDoor 입력과 기본값 | C | 2F vf_iiopt.f:58 `ELSEIF (TEXT(IS(2):IE(2)).EQ.'T-DOOR') THEN`; vf_a2dflt.f:156 `IDROP=1`; :218 `WBUB =0.2D0`. | TimerDoor는 기포 상승값과 물방울 처리의 입력을 갖는다. 두 기본값은 보조 처리를 켠다. |
| KF1-223 | 수송식 선택 입력 | C | 2F vf_a2dflt.f:146–148 `LEQK =0` / `LEQT =0` / `LEQC =0`; vf_iiequa.f:54 `CALL VF_ZSTOI(LEQC,TEXT(IS(3):IE(3)))`. CALC 문자열 비교는 KF1-223에 인용했다. | 난류·온도·농도 수송은 기본적으로 꺼져 있다. 사용자 입력은 선택 경로를 켤 수 있다. |

분류별 개수: 일치 67행, A 8행, B 32행, C 29행, D 3행, E 10행, F 5행, H 7행, X 0행. 열지 못한 파일: 없음.
