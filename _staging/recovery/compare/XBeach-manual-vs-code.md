# XBeach 매뉴얼·보고서와 소스코드 대조

이 보고서는 식생 항력의 v 방향 속력, `FvgCau` 초기화, 비정수압 바닥 경사 항의 부호를 대조한다.
이 보고서는 원문 인용과 AI의 해석을 구분한다.
작성자는 모델을 실행하지 않았다.
작성자는 기존 노트를 수정하지 않았다.

코드의 짧은 `파일:줄` 표기는 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/`를 기준으로 한다.
작성자는 판정에 사용한 코드 원문을 모두 `nl -ba`로 열었다.
원문 인용 표는 들여쓰기와 연속행을 보존한다.
기존 노트 인용은 기존 문체를 보존한다.
PDF 쪽 번호는 파일의 첫 쪽부터 센 번호다.
인쇄 쪽 번호는 쪽 이미지 또는 지정한 판독 기록에서 확인한 번호다.
Kingsday 식과 readthedocs 식은 지정한 판독 기록에서 인용한다.

## A. 식생 항력의 v 방향 속력

### 1. 매뉴얼 서술

**확인:** `XBeach_manual_master.pdf`의 §2.4.3 “Damping by vegetation”은 인쇄 25쪽, PDF 29쪽에 있다.
**확인:** 작성자는 이 쪽을 300 dpi 이미지로 열어 식 (2.57)과 식 (2.58)을 직접 확인했다.

\[
F_v=F_D=\frac12\rho C_Db_vNu\vert u\vert 
\tag{2.57}
\]

\[
\begin{aligned}
F_v(t)&=\sum_{i=1}^{n_v}F_{v,i}(t)\\
F_{v,i}(t)&=\frac12\rho C_{D,i}b_{v,i}N_{v,i}h_{v,i}u^L(t)\left|u^L(t)\right|
\end{aligned}
\tag{2.58}
\]

**확인:** 식 (2.58)의 `C_{D,i}`에는 물결표가 없다.
**확인:** 두 식의 속력 표시는 한 겹의 절댓값 기호다.
**확인:** 같은 쪽 본문은 `u`를 파 또는 흐름과 관련된 속도로 정의한다.
**확인:** 같은 쪽 본문은 평균류와 infragravity 파의 속도를 고려할 때 Lagrangian 속도 `u^L`을 사용한다고 적는다.
**확인:** 이 식생 절은 v점의 속력 배열이나 격자 보간 방법을 지정하지 않는다.
출처는 `models/XBeach/raw/manuals/pdfs/XBeach_manual_master.pdf`, 인쇄 25쪽, PDF 29쪽이다.

**확인:** Kingsday 판독 기록은 §2.4.3을 인쇄 27쪽, PDF 29쪽으로 적는다.
**미확인:** 작성자는 Kingsday 쪽 이미지를 이번 작업에서 직접 확인하지 않았다.
다음 LaTeX는 판독 기록의 식 (2.52)와 식 (2.53)을 전사한다.

\[
F_v = F_D = \int_{-h}^{-h+h_{veg}}\frac{1}{2}\rho C_Db_vNu|u|dz
\tag{2.52}
\]

\[
\begin{aligned}
F_v(t)&=\sum_{i=1}^{n_v}F_{v,i}(t)\\
F_{v,i}(t)&=\frac12\rho C_{D,i}b_{v,i}N_{v,i}h_{v,i}u^L(t)\left|u^L(t)\right|
\end{aligned}
\tag{2.53}
\]

**확인:** Kingsday 판독 기록도 Lagrangian 속도 `u^L` 사용을 명시한다.
출처는 `_staging/recovery/read/XBeach/manuals/pdfs/XBeach_manual_kingsday.pdf/p019-036.md:26`의 PDF 29쪽 행이다.

**확인:** readthedocs 판독 기록은 “Damping by vegetation”의 원문 1223행과 1236행을 다음과 같이 인용한다.
**확인:** 이 판독 기록은 두 식의 숫자 식 번호를 제공하지 않는다.
**확인:** 두 식의 `:label:` 값은 판독 기록에서 비어 있다.
**미확인:** 작성자는 readthedocs 화면을 이번 작업에서 직접 확인하지 않았다.
readthedocs에는 인쇄 쪽 번호와 PDF 쪽 번호가 없다.

\[
F_{v}=F_{D}=\frac{1}{2}\rho C_{D}b_{v}Nu\left\|u\right\|
\]

\[
\begin{array}{l}
F_{v}(t)=\sum_{i=1}^{n_v}F_{v,i}(t)\\
F_{v,i}(t)=\frac{1}{2}\rho\widetilde{C}_{D,i}b_{v,i}N_{v,i}h_{v,i}u^L(t)\left\|u^L(t)\right\|
\end{array}
\]

**확인:** readthedocs 식은 두 겹의 노름 기호를 사용한다.
**확인:** readthedocs의 층별 식은 물결표가 있는 `\widetilde{C}_{D,i}`를 사용한다.
**확인:** readthedocs 원문 1228–1229행의 인용은 Lagrangian 속도 사용을 명시한다.
출처는 `_staging/recovery/read/XBeach/manuals/readthedocs/en/latest/_sources/xbeach_manual.rst.txt.md:48`이다.

### 2. 코드

**확인:** `vegetation.F90:516`은 v 방향 성분 `s%vev(i,j)`에 u점 속력 `s%vmageu(i,j)`를 곱한다.
**확인:** `vegetation.F90:520`은 다른 분기에서 `s%vv(i,j)`에 u점 속력 `s%vmagu(i,j)`를 곱한다.
**확인:** `vegetation.F90:563–564`는 층별 항력 합에 밀도 `par%rho`를 곱한다.

| 위치 | 줄 원문 |
|---|---|
| `vegetation.F90:512` | `                  else ! vegetation section is located (partly) in between wave trough and crest level` |
| `vegetation.F90:513` | `                     if (par%veguntow == 1) then` |
| `vegetation.F90:514` | `                        ! mean and long wave flow (ue, ve)` |
| `vegetation.F90:515` | `                        Fvgtu = max((min(aht,watr)-ahtold),0d0)*0.5d0*s%Cdveg(i,j,m)*s%bveg(i,j,m)*s%Nveg(i,j,m)*(s%ueu(i,j)*s%vmageu(i,j))` |
| `vegetation.F90:516` | `                        Fvgtv = max((min(aht,watr)-ahtold),0d0)*0.5d0*s%Cdveg(i,j,m)*s%bveg(i,j,m)*s%Nveg(i,j,m)*(s%vev(i,j)*s%vmageu(i,j))` |
| `vegetation.F90:517` | `                     else` |
| `vegetation.F90:518` | `                        ! Only long wave velocity (assume undertow is diverted over vegetation)` |
| `vegetation.F90:519` | `                        Fvgtu = max((min(aht,watr)-ahtold),0d0)*0.5d0*s%Cdveg(i,j,m)*s%bveg(i,j,m)*s%Nveg(i,j,m)*(s%uu(i,j)*s%vmagu(i,j))` |
| `vegetation.F90:520` | `                        Fvgtv = max((min(aht,watr)-ahtold),0d0)*0.5d0*s%Cdveg(i,j,m)*s%bveg(i,j,m)*s%Nveg(i,j,m)*(s%vv(i,j)*s%vmagu(i,j))` |
| `vegetation.F90:521` | `                     endif` |
| `vegetation.F90:543` | `                  ! save aht to ahtold to correct possibly in next vegetation section` |
| `vegetation.F90:544` | `                  ahtold = aht` |
| `vegetation.F90:546` | `                  ! add Forcing current layer` |
| `vegetation.F90:547` | `                  Fvgu(i,j) = Fvgu(i,j) + Fvgtu` |
| `vegetation.F90:548` | `                  Fvgv(i,j) = Fvgv(i,j) + Fvgtv` |
| `vegetation.F90:563` | `      s%Fvegu = Fvgu*par%rho ! make sure units of drag force are consistent (N/m2)` |
| `vegetation.F90:564` | `      s%Fvegv = Fvgv*par%rho ! make sure units of drag force are consistent (N/m2)` |

**확인:** `flow_timestep.F90:805–821`은 v 방향 속도를 u점으로 보간한다.
**확인:** `flow_timestep.F90:824–853`은 u점의 Stokes 속도 성분을 계산한다.
**확인:** `flow_timestep.F90:856, 858`은 Stokes 속도를 뺀 u점의 Eulerian 성분 `veu`와 `s%ueu`를 계산한다.
**확인:** `flow_timestep.F90:864`는 `vmageu=sqrt(s%ueu**2+veu**2)`를 계산한다.
**확인:** `flow_timestep.F90:877–892`는 u 방향 속도를 v점으로 보간한다.
**확인:** `flow_timestep.F90:895–923`은 v점의 Stokes 속도 성분을 계산한다.
**확인:** `flow_timestep.F90:926, 928`은 Stokes 속도를 뺀 v점의 Eulerian 성분 `s%vev`와 `uev`를 계산한다.
**확인:** `flow_timestep.F90:934`는 `vmagev=sqrt(uev**2+s%vev**2)`를 계산한다.
**확인:** `flow_timestep.F90:860–862, 930–932`는 `sedtrans==0`일 때 `vmagu`와 `vmagv`도 각각 계산한다.

| 위치 | 줄 원문 |
|---|---|
| `flow_timestep.F90:805` | `      ! V-velocities at u-points` |
| `flow_timestep.F90:806` | `      if (s%ny>0) then` |
| `flow_timestep.F90:807` | `         s%vu(1:s%nx,2:s%ny)= 0.25d0*(s%vv(1:s%nx,1:s%ny-1)+s%vv(1:s%nx,2:s%ny)+ &` |
| `flow_timestep.F90:808` | `         s%vv(2:s%nx+1,1:s%ny-1)+s%vv(2:s%nx+1,2:s%ny))` |
| `flow_timestep.F90:809` | `         ! how about boundaries?` |
| `flow_timestep.F90:810` | `         if(xmpi_isleft) then` |
| `flow_timestep.F90:811` | `            s%vu(:,1) = s%vu(:,2)` |
| `flow_timestep.F90:812` | `         endif` |
| `flow_timestep.F90:813` | `         if(xmpi_isright) then` |
| `flow_timestep.F90:814` | `            s%vu(:,s%ny+1) = s%vu(:,s%ny)` |
| `flow_timestep.F90:815` | `         endif` |
| `flow_timestep.F90:816` | `      else` |
| `flow_timestep.F90:817` | `         s%vu(1:s%nx,1)= 0.5d0*(s%vv(1:s%nx,1)+s%vv(2:s%nx+1,1))` |
| `flow_timestep.F90:818` | `      endif !s%ny>0` |
| `flow_timestep.F90:819` | `      ! wwvv fill in vu(:1) and vu(:ny+1) for non-left and non-right processes` |
| `flow_timestep.F90:820` | `      !  and vu(nx+1,:)` |
| `flow_timestep.F90:821` | `      s%vu=s%vu*s%wetu` |
| `flow_timestep.F90:822` | `      ! V-stokes velocities at U point` |
| `flow_timestep.F90:823` | `      if (s%ny>0) then` |
| `flow_timestep.F90:824` | `         vsu(1:s%nx,2:s%ny)=0.5d0*(s%ust(1:s%nx,2:s%ny)*sinthm(1:s%nx,2:s%ny)+ &` |
| `flow_timestep.F90:825` | `         s%ust(2:s%nx+1,2:s%ny)*sinthm(2:s%nx+1,2:s%ny))` |
| `flow_timestep.F90:826` | `         if(xmpi_isleft) then` |
| `flow_timestep.F90:827` | `            vsu(:,1)=vsu(:,2)` |
| `flow_timestep.F90:828` | `         endif` |
| `flow_timestep.F90:829` | `         if(xmpi_isright) then` |
| `flow_timestep.F90:830` | `            vsu(:,s%ny+1) = vsu(:,s%ny)` |
| `flow_timestep.F90:831` | `         endif` |
| `flow_timestep.F90:832` | `      else` |
| `flow_timestep.F90:833` | `         vsu(1:s%nx,1)=0.5d0*(s%ust(1:s%nx,1)*sinthm(1:s%nx,1)+ &` |
| `flow_timestep.F90:834` | `         s%ust(2:s%nx+1,1)*sinthm(2:s%nx+1,1))` |
| `flow_timestep.F90:835` | `      endif !s%ny>0` |
| `flow_timestep.F90:836` | `      ! wwvv same for vsu` |
| `flow_timestep.F90:837` | `      vsu = vsu*s%wetu` |
| `flow_timestep.F90:838` | `      ! U-stokes velocities at U point` |
| `flow_timestep.F90:839` | `      if (s%ny>0) then` |
| `flow_timestep.F90:840` | `         usu(1:s%nx,2:s%ny)=0.5d0*(s%ust(1:s%nx  ,2:s%ny)*costhm(1:s%nx  ,2:s%ny)+ &` |
| `flow_timestep.F90:841` | `         s%ust(2:s%nx+1,2:s%ny)*costhm(2:s%nx+1,2:s%ny))` |
| `flow_timestep.F90:842` | `         if(xmpi_isleft) then` |
| `flow_timestep.F90:843` | `            usu(:,1)=usu(:,2)` |
| `flow_timestep.F90:844` | `         endif` |
| `flow_timestep.F90:845` | `         if(xmpi_isright) then` |
| `flow_timestep.F90:846` | `            usu(:,s%ny+1)=usu(:,s%ny)` |
| `flow_timestep.F90:847` | `         endif` |
| `flow_timestep.F90:848` | `      else` |
| `flow_timestep.F90:849` | `         usu(1:s%nx,1)=0.5d0*(s%ust(1:s%nx,1)*costhm(1:s%nx,1)+ &` |
| `flow_timestep.F90:850` | `         s%ust(2:s%nx+1,1)*costhm(2:s%nx+1,1))` |
| `flow_timestep.F90:851` | `      endif !s%ny>0` |
| `flow_timestep.F90:852` | `      ! wwvv same for usu` |
| `flow_timestep.F90:853` | `      usu=usu*s%wetu` |
| `flow_timestep.F90:855` | `      ! V-euler velocities at u-point` |
| `flow_timestep.F90:856` | `      veu = s%vu - vsu` |
| `flow_timestep.F90:857` | `      ! U-euler velocties at u-point` |
| `flow_timestep.F90:858` | `      s%ueu = s%uu - usu` |
| `flow_timestep.F90:859` | `      ! Velocity magnitude at u-points` |
| `flow_timestep.F90:860` | `      if (par%sedtrans == 0) then` |
| `flow_timestep.F90:861` | `         s%vmagu=sqrt(s%uu**2+s%vu**2)` |
| `flow_timestep.F90:862` | `      endif` |
| `flow_timestep.F90:863` | `      ! Eulerian velocity magnitude at u-points` |
| `flow_timestep.F90:864` | `      s%vmageu=sqrt(s%ueu**2+veu**2)` |
| `flow_timestep.F90:877` | `      ! U-velocities at v-points` |
| `flow_timestep.F90:878` | `      if (s%ny>0) then` |
| `flow_timestep.F90:879` | `         s%uv(2:s%nx,1:s%ny)= .25d0*(s%uu(1:s%nx-1,1:s%ny)+s%uu(2:s%nx,1:s%ny)+ &` |
| `flow_timestep.F90:880` | `         s%uu(1:s%nx-1,2:s%ny+1)+s%uu(2:s%nx,2:s%ny+1))` |
| `flow_timestep.F90:881` | `         ! boundaries?` |
| `flow_timestep.F90:882` | `         ! wwvv and what about uv(:,1) ?` |
| `flow_timestep.F90:883` | `         if(xmpi_isright) then` |
| `flow_timestep.F90:884` | `            s%uv(:,s%ny+1) = s%uv(:,s%ny)` |
| `flow_timestep.F90:885` | `         endif` |
| `flow_timestep.F90:886` | `      else` |
| `flow_timestep.F90:887` | `         s%uv(2:s%nx,1)= .5d0*(s%uu(1:s%nx-1,1)+s%uu(2:s%nx,1))` |
| `flow_timestep.F90:888` | `      endif !s%ny>0` |
| `flow_timestep.F90:889` | `      ! wwvv fix uv(:,ny+1) for non-right processes` |
| `flow_timestep.F90:890` | `      ! uv(1,:) and uv(nx+1,:) need to be filled in for` |
| `flow_timestep.F90:891` | `      ! non-bot or top processes` |
| `flow_timestep.F90:892` | `      s%uv=s%uv*s%wetv` |
| `flow_timestep.F90:893` | `      ! V-stokes velocities at V point` |
| `flow_timestep.F90:894` | `      if (s%ny>0) then` |
| `flow_timestep.F90:895` | `         vsv(2:s%nx,1:s%ny)=0.5d0*(s%ust(2:s%nx,1:s%ny)*sinthm(2:s%nx,1:s%ny)+&` |
| `flow_timestep.F90:896` | `         s%ust(2:s%nx,2:s%ny+1)*sinthm(2:s%nx,2:s%ny+1))` |
| `flow_timestep.F90:897` | `         if(xmpi_isleft) then` |
| `flow_timestep.F90:898` | `            vsv(:,1) = vsv(:,2)` |
| `flow_timestep.F90:899` | `         endif` |
| `flow_timestep.F90:900` | `         if(xmpi_isright) then` |
| `flow_timestep.F90:901` | `            vsv(:,s%ny+1) = vsv(:,s%ny)` |
| `flow_timestep.F90:902` | `         endif` |
| `flow_timestep.F90:903` | `      else` |
| `flow_timestep.F90:904` | `         vsv(2:s%nx,1)= s%ust(2:s%nx,1)*sinthm(2:s%nx,1)` |
| `flow_timestep.F90:905` | `      endif !s%ny>0` |
| `flow_timestep.F90:906` | `      ! wwvv fix vsv(:,1) and vsv(:,ny+1) and vsv(1,:) and vsv(nx+1,:)` |
| `flow_timestep.F90:908` | `      vsv=vsv*s%wetv` |
| `flow_timestep.F90:909` | `      ! U-stokes velocities at V point` |
| `flow_timestep.F90:910` | `      if (s%ny>0) then` |
| `flow_timestep.F90:911` | `         usv(2:s%nx,1:s%ny)=0.5d0*(s%ust(2:s%nx,1:s%ny)*costhm(2:s%nx,1:s%ny)+&` |
| `flow_timestep.F90:912` | `         s%ust(2:s%nx,2:s%ny+1)*costhm(2:s%nx,2:s%ny+1))` |
| `flow_timestep.F90:913` | `         if(xmpi_isleft) then` |
| `flow_timestep.F90:914` | `            usv(:,1) = usv(:,2)` |
| `flow_timestep.F90:915` | `         endif` |
| `flow_timestep.F90:916` | `         if(xmpi_isright) then` |
| `flow_timestep.F90:917` | `            usv(:,s%ny+1) = usv(:,s%ny)` |
| `flow_timestep.F90:918` | `         endif` |
| `flow_timestep.F90:919` | `      else` |
| `flow_timestep.F90:920` | `         usv(2:s%nx,1)=s%ust(2:s%nx,1)*costhm(2:s%nx,1)` |
| `flow_timestep.F90:921` | `      endif !s%ny>0` |
| `flow_timestep.F90:922` | `      ! wwvv fix usv(:,1) and usv(:,ny+1) and usv(1,:) and usv(nx+1,:)` |
| `flow_timestep.F90:923` | `      usv=usv*s%wetv` |
| `flow_timestep.F90:925` | `      ! V-euler velocities at V-point` |
| `flow_timestep.F90:926` | `      s%vev = s%vv - vsv` |
| `flow_timestep.F90:927` | `      ! U-euler velocties at V-point` |
| `flow_timestep.F90:928` | `      uev = s%uv - usv` |
| `flow_timestep.F90:929` | `      ! Velocity magnitude at v-points` |
| `flow_timestep.F90:930` | `      if (par%sedtrans==0) then` |
| `flow_timestep.F90:931` | `         s%vmagv=sqrt(s%uv**2+s%vv**2)` |
| `flow_timestep.F90:932` | `      endif` |
| `flow_timestep.F90:933` | `      ! Eulerian velocity magnitude at v-points` |
| `flow_timestep.F90:934` | `      s%vmagev=sqrt(uev**2+s%vev**2)` |

**확인:** `initialize.F90:789–790`은 `vmageu`와 `vmagev` 배열을 할당한다.
**확인:** `initialize.F90:897–898, 1055–1056`은 두 배열을 0으로 만든다.
**확인:** `initialize.F90:1076`의 `hotstartflow==1` 경로는 초기 정상류를 계산한다.
**확인:** 이 경로의 `initialize.F90:1128`은 `vmagev=sqrt(s%uv**2+s%vv**2)`를 계산한다.
**확인:** 이 경로의 `initialize.F90:1152`는 `vmageu=sqrt(s%uu**2+s%vu**2)`를 계산한다.
**확인:** `initialize.F90:1158–1159`는 `ueu=uu`와 `vev=vv`를 설정한다.
**확인:** `initialize.F90:1162–1163`은 `vmagu=vmageu`와 `vmagv=vmagev`를 설정한다.

| 위치 | 줄 원문 |
|---|---|
| `initialize.F90:789` | `      allocate(s%vmageu(1:s%nx+1,1:s%ny+1))` |
| `initialize.F90:790` | `      allocate(s%vmagev(1:s%nx+1,1:s%ny+1))` |
| `initialize.F90:897` | `      s%vmageu = 0.0d0` |
| `initialize.F90:898` | `      s%vmagev = 0.0d0` |
| `initialize.F90:1055` | `      s%vmageu=0.d0` |
| `initialize.F90:1056` | `      s%vmagev=0.d0` |
| `initialize.F90:1076` | `      if (par%hotstartflow==1) then` |
| `initialize.F90:1104` | `         do while (flowerr > 0.00001d0)` |
| `initialize.F90:1115` | `            ! update vmagev` |
| `initialize.F90:1116` | `            ! u velocity in v points` |
| `initialize.F90:1117` | `            if (s%ny>0) then` |
| `initialize.F90:1118` | `               s%uv(2:s%nx,1:s%ny)= .25d0*(s%uu(1:s%nx-1,1:s%ny)+s%uu(2:s%nx,1:s%ny)+ &` |
| `initialize.F90:1119` | `               s%uu(1:s%nx-1,2:s%ny+1)+s%uu(2:s%nx,2:s%ny+1))` |
| `initialize.F90:1120` | `               ! boundaries?` |
| `initialize.F90:1121` | `               ! wwvv and what about uv(:,1) ?` |
| `initialize.F90:1122` | `               if(xmpi_isright) then` |
| `initialize.F90:1123` | `                  s%uv(:,s%ny+1) = s%uv(:,s%ny)` |
| `initialize.F90:1124` | `               endif` |
| `initialize.F90:1125` | `            else` |
| `initialize.F90:1126` | `               s%uv(2:s%nx,1)= .5d0*(s%uu(1:s%nx-1,1)+s%uu(2:s%nx,1))` |
| `initialize.F90:1127` | `            endif !s%ny>0` |
| `initialize.F90:1128` | `            s%vmagev = sqrt(s%uv**2+s%vv**2)` |
| `initialize.F90:1139` | `            ! update vmageu` |
| `initialize.F90:1140` | `            if (s%ny>0) then` |
| `initialize.F90:1141` | `               s%vu(1:s%nx,2:s%ny)= 0.25d0*(s%vv(1:s%nx,1:s%ny-1)+s%vv(1:s%nx,2:s%ny)+ &` |
| `initialize.F90:1142` | `               s%vv(2:s%nx+1,1:s%ny-1)+s%vv(2:s%nx+1,2:s%ny))` |
| `initialize.F90:1143` | `               if(xmpi_isleft) then` |
| `initialize.F90:1144` | `                  s%vu(:,1) = s%vu(:,2)` |
| `initialize.F90:1145` | `               endif` |
| `initialize.F90:1146` | `               if(xmpi_isright) then` |
| `initialize.F90:1147` | `                  s%vu(:,s%ny+1) = s%vu(:,s%ny)` |
| `initialize.F90:1148` | `               endif` |
| `initialize.F90:1149` | `            else` |
| `initialize.F90:1150` | `               s%vu(1:s%nx,1)= 0.5d0*(s%vv(1:s%nx,1)+s%vv(2:s%nx+1,1))` |
| `initialize.F90:1151` | `            endif !s%ny>0` |
| `initialize.F90:1152` | `            s%vmageu = sqrt(s%uu**2+s%vu**2)` |
| `initialize.F90:1156` | `         enddo` |
| `initialize.F90:1158` | `         s%ueu=s%uu` |
| `initialize.F90:1159` | `         s%vev=s%vv` |
| `initialize.F90:1160` | `         s%qx=s%uu*s%hu` |
| `initialize.F90:1161` | `         s%qy=s%vv*s%hv` |
| `initialize.F90:1162` | `         s%vmagu=s%vmageu` |
| `initialize.F90:1163` | `         s%vmagv=s%vmagev` |

### 3. 판정

**판정: 불일치.**
이 판정은 매뉴얼의 Lagrangian 속도 지정과 `veguntow==1` 분기를 대조한 결과다.

**확인:** 매뉴얼과 readthedocs의 층별 식은 `u^L`을 사용한다.
**확인:** `veguntow==1` 분기는 Eulerian 성분과 속력을 사용한다.
근거는 master 인쇄 25쪽·PDF 29쪽 식 (2.58), Kingsday 판독 기록의 인쇄 27쪽·PDF 29쪽 식 (2.53), readthedocs 원문 1236행, `vegetation.F90:513–516`, `flow_timestep.F90:855–864, 925–934`이다.

**해석:** 매뉴얼 식을 이차원 국소 속도에 성분별로 적용하면 v 방향 항력에는 v점의 속력 또는 v점으로 보간한 속력이 필요하다.
**확인:** `vegetation.F90:516`은 `vmageu`를 v점으로 보간하지 않고 같은 배열 첨자로 사용한다.
**해석:** `vmageu(i,j)`와 `vmagev(i,j)`가 다르면 이 코드는 v점의 Eulerian 국소 속력으로 계산한 항력과 다르다.
**해석:** `vegetation.F90:520`도 `vmagu`와 `vmagv` 사이에서 같은 격자 위치 차이를 가진다.
근거는 `vegetation.F90:516, 520`과 `flow_timestep.F90:861, 864, 931, 934`이다.

**판정: 자료로 판정 불가.**
이 판정의 대조 대상은 v점에서 `vmageu`를 쓰는 선택이 매뉴얼의 격자 이산화 규칙을 위반하는지다.
**확인:** 지정한 식생 절은 그 격자 이산화 규칙을 명시하지 않는다.
**미확인:** 이 자료만으로 `vmageu` 사용이 작성자의 의도인지 코드의 오기인지 판정할 수 없다.
**해석:** Stokes 속도가 0이고 두 격자점의 속력이 같으면 이 차이는 항력 값에 나타나지 않는다.
**미확인:** 작성자는 이 조건의 실제 발생 여부를 모델 실행으로 확인하지 않았다.

### 4. 현재 노트 서술

| 위치 | 줄 원문 |
|---|---|
| `models/XBeach/source-analysis/xbeach_vegetation.md:51` | `  VV["v 방향: vev × vmageu<br/>⚠ v점 속도 × u점 속력 (516)<br/>veguntow=0이면 vv × vmagu (520)"]` |
| `models/XBeach/source-analysis/xbeach_vegetation.md:65` | ``- v 방향 항력은 v점 속도 `vev`·`vv`에 u점 속력 `vmageu`·`vmagu`를 곱한다(vegetation.F90:516·520). v점 속력 `vmagev`는 flow_timestep.F90:934에 따로 있다. `porcanflow` 경로는 u·v점 평균을 한다(871·877).`` |
| `models/XBeach/source-analysis/xbeach_vegetation.md:120` | ``**`veguntow=1`** (`vegetation.F90:513-516`):`` |
| `models/XBeach/source-analysis/xbeach_vegetation.md:122` | `Fvgtu = h_layer * 0.5 * Cdveg * bveg * Nveg * (ueu * vmageu)` |
| `models/XBeach/source-analysis/xbeach_vegetation.md:123` | `Fvgtv = h_layer * 0.5 * Cdveg * bveg * Nveg * (vev * vmageu)` |
| `models/XBeach/source-analysis/xbeach_vegetation.md:126` | ``**`veguntow=0`** (`:517-520`):`` |
| `models/XBeach/source-analysis/xbeach_vegetation.md:128` | `Fvgtu = h_layer * 0.5 * Cdveg * bveg * Nveg * (uu * vmagu)` |
| `models/XBeach/source-analysis/xbeach_vegetation.md:129` | `Fvgtv = h_layer * 0.5 * Cdveg * bveg * Nveg * (vv * vmagu)` |
| `models/XBeach/source-analysis/xbeach_vegetation.md:132` | ```h_layer = max((min(aht, watr) − ahtold), 0d0)` — the submerged vertical extent of this section.`` |
| `models/XBeach/source-analysis/xbeach_vegetation.md:140` | ``Final multiplication by `rho`: `s%Fvegu = Fvgu*par%rho` (`:563-564`). Internal arrays `[N/m²]` (`variables.def:279-280`).`` |

**확인:** 노트 51행과 65행은 v점 성분에 u점 속력을 곱하는 사실을 이미 적는다.
**확인:** 노트 123행과 129행은 코드의 두 v 방향 식을 같은 속력 배열로 적는다.
**판정:** 이 노트의 코드 서술은 이번 원문 확인과 일치한다.
**확인:** 해당 문장들은 매뉴얼 식과의 일치 여부를 판정하지 않는다.

### 5. 노트 수정안

없음.
현재 노트의 해당 코드 서술은 원문과 일치한다.

## B. `FvgCau` 초기화

### 1. 매뉴얼 서술

**확인:** master의 인쇄 25쪽·PDF 29쪽 식 (2.58)은 시각 `t`의 층별 항력을 합한다.
**확인:** Kingsday 판독 기록의 인쇄 27쪽·PDF 29쪽 식 (2.53)도 시각 `t`의 층별 항력을 합한다.
**확인:** readthedocs 원문 1236행의 인용도 시각 `t`의 층별 항력을 합한다.
세 식의 LaTeX는 A의 “1. 매뉴얼 서술”에 적었다.
작성자는 master 쪽 이미지를 직접 확인했다.
작성자는 Kingsday 쪽 이미지와 readthedocs 화면을 직접 확인하지 않았다.

**확인:** 지정한 매뉴얼·보고서·readthedocs 판독 기록에서 `FvgCau` 또는 `vegcanflo`를 검색한 결과는 없다. [10-12 결론 정정] `_staging/recovery/read/XBeach/manuals/readthedocs_markdown/en/latest/input_parameters.md.md:23`은 `vegcanflo`와 설명 `Include incanopy flow [1] or not [0]`를 기록한다. 이 입력 설명은 `FvgCau`의 초기화 규칙을 제공하지 않는다.
**미확인:** 지정한 판독 기록은 `FvgCau`의 호출별 초기화 규칙을 제공하지 않는다.
**미확인:** 지정한 판독 기록은 파봉 위 층에서 `FvgCau`를 어떻게 처리할지 제공하지 않는다.
**해석:** 층별 항력 합 식만으로 `FvgCau`의 초기화 위치를 정할 수 없다.

### 2. 코드

**확인:** `libxbeach.F90:303`은 식생을 켠 시간 단계에서 `vegatt`를 호출한다.
**확인:** `vegetation.F90:319–321`은 `porcanflow==1`일 때 다른 경로를 선택한다.
**확인:** 표준 식생 경로의 `vegetation.F90:342`는 `momeqveg`를 호출한다.
**확인:** 아래 판정은 `momeqveg`에 관한 판정이다.

| 위치 | 줄 원문 |
|---|---|
| `libxbeach.F90:303` | `            if (par%vegetation==1)                                  call vegatt         (s,par)` |

| 위치 | 줄 원문 |
|---|---|
| `vegetation.F90:318` | `      ! Skip in case of using porous in-canopy model` |
| `vegetation.F90:319` | `      if (par%porcanflow == 1) then` |
| `vegetation.F90:320` | `         call porcanflow(s,par)` |
| `vegetation.F90:321` | `      else ! use standard vegetation module` |
| `vegetation.F90:342` | `          call momeqveg(s,par)` |

**확인:** `vegetation.F90:418`은 `FvgCau`를 지역 스칼라 실수로 선언한다.
**확인:** 이 선언에는 `allocatable`, `pointer`, `save` 속성이 없다.
**확인:** `vegetation.F90:453`은 격자 반복 전에 `FvgCau`를 0으로 대입한다.
**확인:** `vegetation.F90:443–444`는 출력 항력의 작업 배열도 호출마다 0으로 만든다.
**확인:** `vegetation.F90:475–487`의 반복 순서는 j 격자, i 격자, 식생 층 m이다.
**확인:** `vegetation.F90:477`은 각 격자점에서 `ahtold`를 0으로 만든다.
**확인:** `vegetation.F90:544`는 각 층의 계산 뒤 `ahtold=aht`를 대입한다.
**확인:** `vegetation.F90:502–511`은 `ahtold>wacr`인 층에서 `Fvgtu`, `Fvgtv`, `Fvgnlu`, `Fvgnlv`를 0으로 만든다.
**확인:** 이 분기는 `FvgCau`와 `FvgCav`에 대입하지 않는다.
**확인:** 다른 분기의 `vegetation.F90:539–540`은 `FvgCau`와 `FvgCav`를 새로 계산한다.
**확인:** `vegetation.F90:554–557`은 `vegcanflo==1`이면 분기 뒤의 값을 항력 합에 더한다.

| 위치 | 줄 원문 |
|---|---|
| `vegetation.F90:404` | `   subroutine momeqveg(s,par)` |
| `vegetation.F90:405` | `      use params,         only: parameters` |
| `vegetation.F90:406` | `      use spaceparams` |
| `vegetation.F90:407` | `      use readkey_module` |
| `vegetation.F90:409` | `      use paramsconst` |
| `vegetation.F90:411` | `      type(parameters)                            :: par` |
| `vegetation.F90:412` | `      type(spacepars)                             :: s` |
| `vegetation.F90:413` | `      !type(veggie), dimension(:), pointer         :: veg` |
| `vegetation.F90:415` | `      ! local variables` |
| `vegetation.F90:416` | `      integer                                     :: i,j,m  ! indices of actual x,y point` |
| `vegetation.F90:417` | `      real*8                                      :: aht,ahtold,Fvgtu,Fvgtv,FvgStu,FvgStv,watr,wacr,uabsu,vabsv` |
| `vegetation.F90:418` | `      real*8                                      :: Fvgnlt,Fvgnlu,Fvgnlv,FvgCan,FvgCav,FvgCau,ucan,uabsunl !uabsunl,vabsvnl,hterm,htermold,` |
| `vegetation.F90:419` | `      real*8, dimension(s%nx+1,s%ny+1)            :: Fvgu,Fvgv,kmr` |
| `vegetation.F90:420` | `      real*8, save                                :: totT` |
| `vegetation.F90:421` | `      real*8, dimension(s%nx+1,s%ny+1,50)         :: unl0,etaw0` |
| `vegetation.F90:422` | `      real*8, save, allocatable, dimension(:,:,:) :: unl,etaw` |
| `vegetation.F90:423` | `      real*8, dimension(50)                       :: hvegeff,Fvgnlu0` |
| `vegetation.F90:424` | `      real*8, dimension(:,:), allocatable,save    :: sinthm, costhm` |
| `vegetation.F90:436` | `      ! only allocate in 1st timestep` |
| `vegetation.F90:437` | `      if (.not. allocated(sinthm)) then` |
| `vegetation.F90:438` | `         allocate (sinthm(s%nx+1,s%ny+1))` |
| `vegetation.F90:439` | `         allocate (costhm(s%nx+1,s%ny+1))` |
| `vegetation.F90:440` | `      endif` |
| `vegetation.F90:441` | `      kmr = min(max(s%k, 0.01d0), 100.d0)` |
| `vegetation.F90:443` | `      Fvgu = 0.d0` |
| `vegetation.F90:444` | `      Fvgv = 0.d0` |
| `vegetation.F90:445` | `      Fvgnlt = 0.d0` |
| `vegetation.F90:446` | `      Fvgnlu = 0.d0` |
| `vegetation.F90:447` | `      Fvgnlv = 0.d0` |
| `vegetation.F90:448` | `      FvgStu = 0.d0` |
| `vegetation.F90:449` | `      FvgStv = 0.d0` |
| `vegetation.F90:450` | `      ucan   = 0.d0` |
| `vegetation.F90:451` | `      FvgCan = 0.d0` |
| `vegetation.F90:452` | `      FvgCav = 0.d0` |
| `vegetation.F90:453` | `      FvgCau = 0.d0` |
| `vegetation.F90:454` | `      uabsunl = 0.d0` |
| `vegetation.F90:456` | `      costhm = cos(s%thetamean-s%alfaz)` |
| `vegetation.F90:457` | `      sinthm = sin(s%thetamean-s%alfaz)` |
| `vegetation.F90:475` | `      do j=1,s%ny+1` |
| `vegetation.F90:476` | `         do i=1,s%nx+1` |
| `vegetation.F90:477` | `            ahtold = 0.d0` |
| `vegetation.F90:478` | `            if (s%nsecveg(i,j)>0) then ! Only if vegetation is present` |
| `vegetation.F90:480` | `               ! Compute uabsu for calculation of Fveg` |
| `vegetation.F90:481` | `               uabsu = 0.d0` |
| `vegetation.F90:482` | `               vabsv = 0.d0` |
| `vegetation.F90:483` | `               Fvgnlu0 = 0.d0` |
| `vegetation.F90:485` | `               watr = 0d0` |
| `vegetation.F90:486` | `               wacr = 0d0` |
| `vegetation.F90:487` | `               do m=1,s%nsecveg(i,j)` |
| `vegetation.F90:488` | `                  ! Determine height of vegetation section (restricted to current bed level)` |
| `vegetation.F90:489` | `                  aht = s%ahveg(i,j,m)+s%zb0(i,j)-s%zb(i,j)` |
| `vegetation.F90:491` | `                  ! Determine which part of the vegetation is below the wave trough, and between trough and crest` |
| `vegetation.F90:492` | `                  if (par%vegnonlin == 1 .and. par%wavemodel/=WAVEMODEL_NONH) then` |
| `vegetation.F90:493` | `                     watr = minval(etaw(i,j,:))` |
| `vegetation.F90:494` | `                     watr = s%hh(i,j) + watr ! wave trough level` |
| `vegetation.F90:495` | `                     wacr = maxval(etaw(i,j,:))` |
| `vegetation.F90:496` | `                     wacr = s%hh(i,j) + wacr ! wave crest level` |
| `vegetation.F90:497` | `                  else` |
| `vegetation.F90:498` | `                     watr = s%hh(i,j)` |
| `vegetation.F90:499` | `                     wacr = s%hh(i,j)` |
| `vegetation.F90:500` | `                  endif` |
| `vegetation.F90:502` | `                  if (ahtold > wacr) then ! if plant section is entirely above wave crest, then do nothing` |
| `vegetation.F90:504` | `                     ! mean and long wave flow (ue)` |
| `vegetation.F90:505` | `                     Fvgtu = 0d0` |
| `vegetation.F90:506` | `                     Fvgtv = 0d0` |
| `vegetation.F90:508` | `                     ! nonlinear waves` |
| `vegetation.F90:509` | `                     Fvgnlu = 0.d0` |
| `vegetation.F90:510` | `                     Fvgnlv = 0.d0` |
| `vegetation.F90:512` | `                  else ! vegetation section is located (partly) in between wave trough and crest level` |
| `vegetation.F90:525` | `                     if (par%vegnonlin == 1 .and. par%wavemodel/=WAVEMODEL_NONH) then` |
| `vegetation.F90:526` | `                        hvegeff = max(etaw(i,j,:) + s%hh(i,j)-ahtold,0.d0) ! effective vegetation height over a wave cycle` |
| `vegetation.F90:527` | `                        Fvgnlt  = trapz(((0.5d0*s%Cdveg(i,j,m)*s%bveg(i,j,m)*s%Nveg(i,j,m))*min(hvegeff,aht)*unl(i,j,:)*abs(unl(i,j,:))),par%Trep/50)/s%hh(i,j)` |
| `vegetation.F90:529` | `                        ! decompose in u and v-direction` |
| `vegetation.F90:530` | `                        Fvgnlu  = Fvgnlt*costhm(i,j)` |
| `vegetation.F90:531` | `                        Fvgnlv  = Fvgnlt*sinthm(i,j)` |
| `vegetation.F90:532` | `                     endif` |
| `vegetation.F90:534` | `                     ! wave induced incanopy flow (Luhar et al., 2010)` |
| `vegetation.F90:535` | `                     ucan   = sqrt(4.d0*kmr(i,j)*par%Trep*s%urms(i,j)**3/(6.d0*par%px**2))` |
| `vegetation.F90:536` | `                     FvgCan = max((min(aht,watr)-ahtold),0d0)/s%hh(i,j)*0.5d0*s%Cdveg(i,j,m)*s%bveg(i,j,m)*s%Nveg(i,j,m)*ucan**2` |
| `vegetation.F90:538` | `                     ! decompose in u and v-direction` |
| `vegetation.F90:539` | `                     FvgCau = FvgCan*costhm(i,j)` |
| `vegetation.F90:540` | `                     FvgCav = FvgCan*sinthm(i,j)` |
| `vegetation.F90:541` | `                  endif` |
| `vegetation.F90:543` | `                  ! save aht to ahtold to correct possibly in next vegetation section` |
| `vegetation.F90:544` | `                  ahtold = aht` |
| `vegetation.F90:546` | `                  ! add Forcing current layer` |
| `vegetation.F90:547` | `                  Fvgu(i,j) = Fvgu(i,j) + Fvgtu` |
| `vegetation.F90:548` | `                  Fvgv(i,j) = Fvgv(i,j) + Fvgtv` |
| `vegetation.F90:550` | `                  if (par%vegnonlin == 1 .and. par%wavemodel/=WAVEMODEL_NONH) then ! add nonlin wave effect` |
| `vegetation.F90:551` | `                     Fvgu(i,j) = Fvgu(i,j) + Fvgnlu` |
| `vegetation.F90:552` | `                     Fvgv(i,j) = Fvgv(i,j) + Fvgnlv` |
| `vegetation.F90:553` | `                  endif` |
| `vegetation.F90:554` | `                  if (par%vegcanflo == 1) then ! add in canopy flow (Luhar et al., 2010)` |
| `vegetation.F90:555` | `                     Fvgu(i,j) = Fvgu(i,j) + FvgCau` |
| `vegetation.F90:556` | `                     Fvgv(i,j) = Fvgv(i,j) + FvgCav` |
| `vegetation.F90:557` | `                  endif` |
| `vegetation.F90:558` | `               enddo` |
| `vegetation.F90:559` | `            endif` |
| `vegetation.F90:560` | `         enddo` |
| `vegetation.F90:561` | `      enddo` |
| `vegetation.F90:563` | `      s%Fvegu = Fvgu*par%rho ! make sure units of drag force are consistent (N/m2)` |
| `vegetation.F90:564` | `      s%Fvegv = Fvgv*par%rho ! make sure units of drag force are consistent (N/m2)` |
| `vegetation.F90:566` | `   end subroutine momeqveg` |

**확인:** 작성자는 허용한 `xbeachlibrary/*.F90` 전체에서 대소문자를 구분하지 않고 식별자를 검색했다.
검색 명령은 다음과 같다.

```sh
grep -n -i -- 'FvgCau' models/XBeach/raw/source_code/trunk/src/xbeachlibrary/*.F90
```

**확인:** 검색 결과는 `vegetation.F90:418, 453, 539, 555`의 네 줄이다.
**확인:** 선언 위치는 418행이다.
**확인:** 대입 위치는 453행과 539행이다.
**확인:** 사용 위치는 555행이다.
**확인:** 검색 결과에는 `allocate(FvgCau...)`가 없다.
**확인:** 검색 결과에는 다른 파일의 0 대입이 없다.
**확인:** 작성자는 이 식별자 검색을 위해 MPI 구현 내부를 판독하지 않았다.

### 3. 판정

**판정: 불일치.**
이 판정의 대조 대상은 “반복 전에 초기화하지 않아 이전 시간 단계 값이 누적된다”는 가설이다.

**확인:** `momeqveg`는 각 호출에서 453행의 0 대입을 실행한다.
**확인:** 이 0 대입은 475행의 첫 격자 반복보다 앞에 있다.
**해석:** `FvgCau`의 이전 시간 단계 값은 이 호출의 항력 합에 누적되지 않는다.
근거는 `vegetation.F90:443–454, 475–487`이다.

**확인:** 파봉 위 층의 분기는 호출 중 남아 있는 `FvgCau`를 다시 대입하지 않는다.
**해석:** 앞선 층이 만든 `FvgCau`가 0이 아니고 다음 층이 `ahtold>wacr`이면 다음 층의 555행은 앞선 층의 값을 다시 더한다.
**해석:** 이 재사용은 같은 호출 안의 식생 층 반복에서 발생할 수 있다.
**확인:** 555행의 추가는 `vegcanflo==1`일 때만 실행한다.
근거는 `vegetation.F90:502–511, 535–555`이다.

**판정: 자료로 판정 불가.** [10-12 결론 정정] 매뉴얼의 초기화 규칙은 여전히 확인하지 못했다. 코드의 파봉 위 층 주석과 다른 층 처리식은 같은 호출의 힘 재사용을 결함 후보(E)로 분류할 근거를 제공한다. 5.3에 두 종류의 정적 근거를 적는다.
이 판정의 대조 대상은 매뉴얼이 요구하는 `FvgCau` 초기화 규칙이다.
지정한 판독 기록에 그 규칙이 없다.
**미확인:** 작성자는 값 재사용의 실제 항력 크기를 모델 실행으로 확인하지 않았다.

### 4. 현재 노트 서술

| 위치 | 줄 원문 |
|---|---|
| `models/XBeach/source-analysis/xbeach_vegetation.md:66` | ``- 파봉 위 단면에서 canopy 힘 `FvgCau/FvgCav`는 0으로 초기화되지 않는다(vegetation.F90:502–511).`` |

**확인:** 노트 66행은 파봉 위 층의 분기에서 두 변수를 0으로 만들지 않는 사실을 적는다.
**판정:** 이 문장을 해당 분기에 한정해서 읽으면 코드와 일치한다.
**확인:** 노트 66행은 호출 시작의 `FvgCau=0`을 적지 않는다.
**확인:** 노트 66행은 같은 호출의 앞선 층 값을 다시 더하는 조건을 적지 않는다.
**확인:** 노트 66행은 이전 시간 단계 값의 누적을 주장하지 않는다.

### 5. 노트 수정안

수정 대상은 `models/XBeach/source-analysis/xbeach_vegetation.md:66`이다.
고칠 문장의 원문은 다음과 같다.

``- 파봉 위 단면에서 canopy 힘 `FvgCau/FvgCav`는 0으로 초기화되지 않는다(vegetation.F90:502–511).``

새 문장은 다음과 같다.

> `momeqveg`는 호출마다 `FvgCau`와 `FvgCav`를 0으로 초기화한다. 출처는 `vegetation.F90:452–453`이다.
>
> `ahtold>wacr`인 식생 층의 분기는 `FvgCau`와 `FvgCav`를 다시 대입하지 않는다. 출처는 `vegetation.F90:502–511`이다.
>
> 앞선 층의 값이 0이 아니면 `vegcanflo==1`인 다음 파봉 위 층이 그 값을 항력 합에 다시 더할 수 있다. 출처는 `vegetation.F90:539–540, 554–556`이다.
>
> 이 값 재사용은 같은 호출 안의 층 반복에 관한 해석이다. 출처는 `vegetation.F90:475–487, 543–558`이다.
>
> 이전 시간 단계 값은 호출 시작의 0 대입 뒤에 남지 않는다. 출처는 `vegetation.F90:443–454`이다.
>
> 매뉴얼 판독 기록은 이 변수의 초기화 규칙을 제공하지 않는다. 대조 위치는 master 인쇄 25쪽·PDF 29쪽 식 (2.58), Kingsday 판독 기록의 인쇄 27쪽·PDF 29쪽 식 (2.53), readthedocs 판독 기록 48행의 원문 1236행이다.

## C. 비정수압 바닥 경사 항의 부호

### 1. 매뉴얼 서술

이 주제의 문서는 `models/XBeach/raw/manuals/reports/non-hydrostatic_report_draft.pdf`이다.
작성자는 아래 식의 부호와 첨자를 300 dpi 쪽 이미지에서 직접 확인했다.
작성자는 인쇄의 부호를 고치지 않고 LaTeX로 전사했다.

**확인:** 인쇄 3쪽·PDF 13쪽의 Figure 2-2는 `d`를 기준면에서 아래로 양인 바닥까지의 거리로 그린다.
**확인:** 같은 쪽 본문은 바닥을 `z=-d`로 정의한다.
**확인:** Figure 2-2는 자유수면에서 바닥까지의 전체 수심을 `H`로 표시한다.
**해석:** 이 정의에서 전체 수심은 `H=\eta+d`이다.
**해석:** 보고서의 `d`는 바닥고가 아니다.
**해석:** 보고서의 `d`는 전체 수심 `H`와도 다른 양이다.

**확인:** 인쇄 5쪽·PDF 15쪽의 식 (1.8)은 다음과 같이 인쇄한다.

\[
w(x,y,-d,t)=\frac{\partial d}{\partial t}-u\frac{\partial d}{\partial x}-v\frac{\partial d}{\partial y}
\tag{1.8}
\]

**확인:** 같은 쪽 본문은 바닥 변화의 시간 규모를 근거로 식 (1.8)의 시간 미분을 무시한다.
**확인:** 식 (1.8)의 두 수평 경사 항은 모두 음수다.

**확인:** 인쇄 6쪽·PDF 16쪽의 식 (1.13), 식 (1.14), 식 (1.17), 식 (1.18)은 다음과 같이 인쇄한다.

\[
\int_{-d}^{\eta}dz\left(\frac{\partial u^2}{\partial x}+\frac{\partial uv}{\partial y}+\frac{\partial uw}{\partial z}\right)=\frac{\partial}{\partial x}\left(HU^2-\int_{-d}^{\eta}(u-U)^2dz\right)-\frac{\partial}{\partial y}\left(HUV-\int_{-d}^{\eta}(v-V)(u-U)dz\right)-u\left[u\frac{\partial z}{\partial x}+v\frac{\partial z}{\partial y}+w\right]_{z=-d}^{z=\eta}
\tag{1.13}
\]

\[
\int_{-d}^{\eta}dz\left(\frac{\partial p}{\partial x}+g\frac{\partial\eta}{\partial x}\right)=\frac{\partial H\bar p}{\partial x}-\left[p\frac{\partial z}{\partial x}\right]_{z=-d}^{z=\eta}+gH\frac{\partial\eta}{\partial x}
\tag{1.14}
\]

\[
\frac{\partial}{\partial t}(HU)+\frac{\partial}{\partial x}\left(HU^2+\frac{1}{2}gH^2+H\bar p-\frac{1}{\rho}H\bar\tau_{xx}\right)+\frac{\partial}{\partial y}\left(HUV-\frac{1}{\rho}H\bar\tau_{yx}\right)=gH\frac{\partial d}{\partial x}-p\frac{\partial d}{\partial x}+S_x
\tag{1.17}
\]

\[
\frac{\partial}{\partial t}(HV)+\frac{\partial}{\partial x}\left(HUV-\frac{1}{\rho}H\bar\tau_{xy}\right)+\frac{\partial}{\partial y}\left(HV^2+\frac{1}{2}gH^2+H\bar p-\frac{1}{\rho}H\bar\tau_{yy}\right)=gH\frac{\partial d}{\partial y}-p\frac{\partial d}{\partial y}+S_y
\tag{1.18}
\]

**확인:** 식 (1.13)의 y 이류항 앞에는 음수가 있다.
**확인:** 식 (1.17)의 y 이류항 앞에는 양수가 있다.
**확인:** 이 차이는 y 이류항의 부호 차이다.
**확인:** 식 (1.17)과 식 (1.18)의 동압 바닥 경사 항은 우변에서 음수다.
**확인:** 이 두 식은 우변의 동압 `p`에 상선을 인쇄하지 않는다.

**확인:** 인쇄 15쪽·PDF 25쪽의 식 (2.15)은 다음과 같이 인쇄한다.

\[
{}^x\mathrm{Pr}^{n+\frac12}_{i+\frac12,j} = \frac{H^{n+1}_{i+1,j}\bar p^{n+\frac12}_{i+1,j} - H^{n+1}_{i,j}\bar p^{n+\frac12}_{i,j}}{\Delta x} - p^{n+\frac12}_{i+\frac12,j}\frac{d_{i+\frac12,j} - d_{i-\frac12,j}}{\Delta x} = \frac{\left(\eta^{n+1}_{i+1,j} + d^{n+1}_{i,j}\right)p^{n+\frac12}_{i+1,j} - \left(\eta^{n+1}_{i,j} - d^{n+1}_{i+1,j}\right)p^{n+\frac12}_{i,j}}{2\Delta x}
\tag{2.15}
\]

**확인:** 같은 쪽 본문은 `\bar p_{i+1,j}^{n+\frac12}=\frac12p_{i+1,j}^{n+\frac12}`를 적는다.
**확인:** 같은 쪽 본문은 `p`를 바닥 압력으로 설명한다.
**확인:** 같은 쪽 본문은 `p_{i+\frac12,j}^{n+\frac12}=\frac12(p_{i+1,j}^{n+\frac12}+p_{i,j}^{n+\frac12})`를 적는다.

**확인:** 인쇄 16쪽·PDF 26쪽의 식 (2.18)은 다음과 같이 인쇄한다.

\[
\frac{(HU)^{n+1\frac12}_{i+\frac12,j} - (HU)^{n*}_{i+\frac12,j}}{\Delta t} + \frac{{}^x\bar q^{n+\frac12}_{i+1,j}\Delta U_{i+1,j} - {}^x\bar q^{n+\frac12}_{i,j}\Delta U_{i,j}}{\Delta x} + \frac{{}^y\bar q^{n+\frac12}_{i,j+1}\Delta U_{i,j+1} - {}^y\bar q^{n+\frac12}_{i,j}\Delta U_{i,j}}{\Delta y} + \frac{\left(\eta^{n+1}_{i+1,j} + d^{n+1}_{i,j}\right)\Delta p^{n+1\frac12}_{i+1,j} - \left(\eta^{n+1}_{i,j} - d^{n+1}_{i+1,j}\right)\Delta p^{n+1\frac12}_{i,j}}{2\Delta x} = 0
\tag{2.18}
\]

**확인:** 같은 쪽의 식 (2.19)은 U 성분과 V 성분을 한 식 번호로 묶는다.
**확인:** 다음 전사는 원문에 인쇄된 생략 기호를 보존한다.
**확인:** 다음 전사는 V 성분에 인쇄된 `{}^y\bar q`와 분모 `\Delta y`를 보존한다.
**확인:** 다음 전사는 V 성분의 마지막 압력항에 인쇄된 분모 `\Delta x`를 보존한다.

\[
\begin{aligned}
&\frac{U^{n+1\frac12}_{i+\frac12,j}-U^{n*}_{i+\frac12,j}}{\Delta t}
+\frac{{}^x\bar q^{n+\frac12}_{i+1,j}\Delta U_{i+1,j}-{}^x\bar q^{n+\frac12}_{i,j}\Delta U^{n*}_{i,j}}{\bar H^{n+1}_{i+\frac12,j}\Delta x}
+\frac{{}^y\bar q^{n+\frac12}_{i+\frac12,j+\frac12}\Delta U_{i+\frac12,j+\frac12}-{}^y\bar q^{n+\frac12}_{i+\frac12,j-\frac12}\Delta U_{i+\frac12,j-\frac12}}{\bar H^{n+1}_{i+\frac12,j}\Delta y}
+\ldots\\
&\ldots+
\frac{(\eta^{n+1}_{i+1,j}+d^{n+1}_{i,j})\Delta p^{n+1\frac12}_{i+1,j}-(\eta^{n+1}_{i,j}-d^{n+1}_{i+1,j})\Delta p^{n+1\frac12}_{i,j}}{2\bar H^{n+1}_{i+\frac12,j}\Delta x}=0\\[1ex]
&\frac{V^{n+1\frac12}_{i,j+\frac12}-V^{n*}_{i,j+\frac12}}{\Delta t}
+\frac{{}^y\bar q^{n+\frac12}_{i,j+1}\Delta V_{i,j+1}-{}^y\bar q^{n+\frac12}_{i,j}\Delta V_{i,j}}{\bar H^{n+1}_{i,j+\frac12}\Delta y}
+\frac{{}^x\bar q^{n+\frac12}_{i+\frac12,j+\frac12}\Delta V_{i+\frac12,j+\frac12}-{}^y\bar q^{n+\frac12}_{i-\frac12,j+\frac12}\Delta V_{i-\frac12,j+\frac12}}{\bar H^{n+1}_{i,j+\frac12}\Delta y}
+\ldots\\
&\ldots+
\frac{(\eta^{n+1}_{i,j+1}+d^{n+1}_{i,j})\Delta p^{n+1\frac12}_{i,j+1}-(\eta^{n+1}_{i,j}-d^{n+1}_{i,j+1})\Delta p^{n+1\frac12}_{i,j}}{2\bar H^{n+1}_{i,j+\frac12}\Delta x}=0
\end{aligned}
\tag{2.19}
\]

**확인:** 식 (2.15), 식 (2.18), 식 (2.19)의 첫 압력 괄호에는 `+d`가 있다.
**확인:** 같은 식들의 둘째 압력 괄호에는 `-d`가 있다.
**확인:** 각 압력 괄호의 `d` 첨자는 그 괄호에 곱하는 압력의 첨자와 엇갈린다.
쪽 이미지 출처는 보고서의 인쇄 15–16쪽·PDF 25–26쪽이다.

### 2. 코드

**확인:** `initialize.F90:242`는 입력 지형의 부호를 `posdwn`에 따라 변환한다.
**확인:** `initialize.F90:1012`와 `flow_timestep.F90:940`은 전체 수심을 `zs-zb`로 계산한다.
**해석:** 코드의 `zb`는 위로 양인 바닥고다.
**해석:** 기준면을 같게 두면 `d=-zb`, `H=hh`, `\eta=zs`로 대응한다.
**확인:** 코드의 `hh` 계산은 `par%eps`를 하한으로 둔다.

| 위치 | 줄 원문 |
|---|---|
| `initialize.F90:45` | `      s%posdwn  = par%posdwn` |
| `initialize.F90:54` | `      s%posdwn = s%posdwn*sign(s%posdwn,1.d0)` |
| `initialize.F90:242` | `         s%zb=-s%zb*s%posdwn` |
| `initialize.F90:1012` | `      s%hh=max(s%zs-s%zb,par%eps)` |

| 위치 | 줄 원문 |
|---|---|
| `flow_timestep.F90:940` | `      s%hh  = max(s%zs-s%zb,par%eps)    ! water depth` |

**확인:** `nonh.F90:3372`는 u점의 바닥고 `zbu`를 두 `zb` 값의 최댓값으로 계산한다.
**확인:** `nonh.F90:3386`은 v점의 바닥고 `zbv`를 두 `zb` 값의 최댓값으로 계산한다.
**확인:** `nonh.F90:3398, 3407`은 수면고를 수심과 바닥고의 합으로 계산한다.

| 위치 | 줄 원문 |
|---|---|
| `nonh.F90:3353` | `      !   Interpolate bottom and free surface location to u/v points` |
| `nonh.F90:3369` | `      !Bottom location in U point` |
| `nonh.F90:3370` | `      do j=1,s%ny+1` |
| `nonh.F90:3371` | `         do i=1,s%nx` |
| `nonh.F90:3372` | `            zbu(i,j) = max(s%zb(i,j),s%zb(min(s%nx,i)+1,j))` |
| `nonh.F90:3373` | `         enddo` |
| `nonh.F90:3374` | `      enddo` |
| `nonh.F90:3382` | `      !Bottom location in V point` |
| `nonh.F90:3383` | `      if (s%ny>2) then` |
| `nonh.F90:3384` | `         do j=1,s%ny` |
| `nonh.F90:3385` | `            do i=1,s%nx+1` |
| `nonh.F90:3386` | `               zbv(i,j) = max(s%zb(i,j),s%zb(i,min(s%ny,j)+1))` |
| `nonh.F90:3387` | `            enddo` |
| `nonh.F90:3388` | `         enddo` |
| `nonh.F90:3389` | `         zbv(:,s%ny+1) = s%zb(:,s%ny+1)` |
| `nonh.F90:3390` | `      else` |
| `nonh.F90:3391` | `         zbv = s%zb` |
| `nonh.F90:3392` | `      endif` |
| `nonh.F90:3394` | `      !Free surface location in u-point` |
| `nonh.F90:3395` | `      do j=1,s%ny+1` |
| `nonh.F90:3396` | `         do i=1,s%nx` |
| `nonh.F90:3397` | `            !` |
| `nonh.F90:3398` | `            zsu(i,j) = s%hu(i,j) + zbu(i,j)` |
| `nonh.F90:3399` | `            !` |
| `nonh.F90:3400` | `         enddo` |
| `nonh.F90:3401` | `      enddo` |
| `nonh.F90:3403` | `      !Free surface location in v-point` |
| `nonh.F90:3404` | `      if (s%ny>2) then` |
| `nonh.F90:3405` | `         do j=1,s%ny` |
| `nonh.F90:3406` | `            do i=1,s%nx+1` |
| `nonh.F90:3407` | `               zsv(i,j) = s%hv(i,j) + zbv(i,j)` |
| `nonh.F90:3408` | `            enddo` |
| `nonh.F90:3409` | `         enddo` |
| `nonh.F90:3410` | `      else` |
| `nonh.F90:3411` | `         do j=1,s%ny+1` |
| `nonh.F90:3412` | `            zsv(:,j) = s%zs(:,min(2,s%ny+1))` |
| `nonh.F90:3413` | `         enddo` |
| `nonh.F90:3414` | `      endif` |

**확인:** `nonh.F90:233–245`의 기본 분기는 `nonh_1lay_pred`와 `nonh_1lay_cor`를 호출한다.
**해석:** 보고서의 단일 수심평균 압력식은 이 단일층 경로와 직접 대조할 수 있다.
**미확인:** 작성자는 아래 대조를 reduced 2층 모델 전체의 부호 판정으로 확대하지 않았다.

| 위치 | 줄 원문 |
|---|---|
| `nonh.F90:201` | `      select case ( par%nonhq3d )` |
| `nonh.F90:233` | `       case default` |
| `nonh.F90:234` | `         !` |
| `nonh.F90:235` | `         ! The "old" code is used` |
| `nonh.F90:236` | `         !` |
| `nonh.F90:237` | `         if ( ipredcor == 0 ) then` |
| `nonh.F90:238` | `            ! -- Predictor` |
| `nonh.F90:239` | `            call nonh_1lay_pred(s,par)` |
| `nonh.F90:240` | `            !` |
| `nonh.F90:241` | `         else` |
| `nonh.F90:242` | `            ! -- Corrector` |
| `nonh.F90:243` | `            call nonh_1lay_cor(s,par)` |
| `nonh.F90:244` | `            !` |
| `nonh.F90:245` | `         endif` |

**확인:** `nonh.F90:1193–1195`는 u 방향 압력 계수를 만든다.
**확인:** `nonh.F90:1216–1218`은 v 방향 압력 계수를 만든다.
**확인:** 두 방향의 두 깊이 괄호는 모두 `zs-zb` 형태다.
**확인:** `nonh.F90:1235–1252`는 `secorder==1`일 때 이 계수로 기존 압력의 기여를 더한다.
**확인:** `nonh.F90:697, 709`는 같은 계수로 압력 보정 `dp`의 기여를 더한다.

| 위치 | 줄 원문 |
|---|---|
| `nonh.F90:1190` | `      do j=jmin,jmax` |
| `nonh.F90:1191` | `         do i=2,s%nx` |
| `nonh.F90:1192` | `            if (nonhU(i,j)==1) then` |
| `nonh.F90:1193` | `               vol       = 0.5_rKind*par%dt/(s%hum(i,j)*dxu(i))` |
| `nonh.F90:1194` | `               au(1,i,j) = - (s%zs(i+1,j) - s%zb(i  ,j))*vol` |
| `nonh.F90:1195` | `               au(0,i,j) = + (s%zs(i  ,j) - s%zb(i+1,j))*vol` |
| `nonh.F90:1196` | `            else` |
| `nonh.F90:1197` | `               au(1,i,j) =  0.0_rKind` |
| `nonh.F90:1198` | `               au(0,i,j) =  0.0_rKind` |
| `nonh.F90:1199` | `            endif` |
| `nonh.F90:1200` | `         enddo` |
| `nonh.F90:1201` | `      enddo` |
| `nonh.F90:1202` | `      if (xmpi_istop) then               !wwvv: added test on istop` |
| `nonh.F90:1203` | `         au(:,1,:)      = 0.0_rKind` |
| `nonh.F90:1204` | `      endif` |
| `nonh.F90:1205` | `      if (xmpi_isbot) then               !wwvv: added test on isbot` |
| `nonh.F90:1206` | `         au(:,s%nx+1,:)   = 0.0_rKind` |
| `nonh.F90:1207` | `      endif` |
| `nonh.F90:1210` | `      !Built pressure coefficients V` |
| `nonh.F90:1211` | `      !call timer_start(timer_flow_nonh_av)` |
| `nonh.F90:1212` | `      if (s%ny>2) then` |
| `nonh.F90:1213` | `         do j=2,s%ny` |
| `nonh.F90:1214` | `            do i=2,s%nx` |
| `nonh.F90:1215` | `               if (nonhV(i,j)==1)then` |
| `nonh.F90:1216` | `                  vol       = 0.5_rKind*par%dt/(s%hvm(i,j)*dyv(j))` |
| `nonh.F90:1217` | `                  av(1,i,j)  = -(s%zs(i  ,j+1) - s%zb(i  ,j  ))*vol` |
| `nonh.F90:1218` | `                  av(0,i,j)  = +(s%zs(i  ,j  ) - s%zb(i  ,j+1))*vol` |
| `nonh.F90:1219` | `                  avr(i,j)   = s%vv(i,j)` |
| `nonh.F90:1220` | `               else` |
| `nonh.F90:1221` | `                  av(1,i,j) =  0.0_rKind` |
| `nonh.F90:1222` | `                  av(0,i,j) =  0.0_rKind` |
| `nonh.F90:1223` | `               endif` |
| `nonh.F90:1224` | `            enddo` |
| `nonh.F90:1225` | `         enddo` |
| `nonh.F90:1226` | `         if (xmpi_isleft) then               !wwvv: added test on isleft` |
| `nonh.F90:1227` | `            av(:,:,1)     = 0.0_rKind` |
| `nonh.F90:1228` | `         endif` |
| `nonh.F90:1229` | `         if (xmpi_isright) then              !wwvv: added test on isright` |
| `nonh.F90:1230` | `            av(:,:,s%ny+1)  = 0.0_rKind` |
| `nonh.F90:1231` | `         endif` |
| `nonh.F90:1232` | `      endif` |
| `nonh.F90:1234` | `      !Include explicit approximation for pressure in s%uu and s%vv   and Wm` |
| `nonh.F90:1235` | `      if (par%secorder == 1) then` |
| `nonh.F90:1236` | `         do j=jmin,jmax` |
| `nonh.F90:1237` | `            do i=imin_uu,imax_uu` |
| `nonh.F90:1238` | `               s%uu(i,j) = s%uu(i,j) + au(1,i,j) * s%pres(i+1,j) + au(0,i,j) * s%pres(i  ,j)` |
| `nonh.F90:1239` | `            enddo` |
| `nonh.F90:1240` | `         enddo` |
| `nonh.F90:1242` | `         if (s%ny>0) then` |
| `nonh.F90:1243` | `            do j=jmin_vv,jmax_vv` |
| `nonh.F90:1244` | `               do i=imin_vv,imax_vv` |
| `nonh.F90:1245` | `                  s%vv(i,j) = s%vv(i,j) + av(1,i,j) * s%pres(i,j+1) + av(0,i,j) * s%pres(i,j  )` |
| `nonh.F90:1246` | `               enddo` |
| `nonh.F90:1247` | `            enddo` |
| `nonh.F90:1248` | `         else` |
| `nonh.F90:1249` | `            do i=imin_vv,imax_vv` |
| `nonh.F90:1250` | `               s%vv(i,1) = s%vv(i,1) + av(1,i,1) * s%pres(i,1) + av(0,i,1) * s%pres(i,1  )` |
| `nonh.F90:1251` | `            enddo` |
| `nonh.F90:1252` | `         endif` |
| `nonh.F90:460` | `      aur  = s%uu` |
| `nonh.F90:461` | `      avr  = s%vv` |
| `nonh.F90:685` | `      dp = 0.0_rKind` |
| `nonh.F90:686` | `      call solver_solvemat( mat  , rhs   , dp , s%nx, s%ny,par)` |
| `nonh.F90:690` | `      s%pres = s%pres + dp` |
| `nonh.F90:695` | `      do j=jmin_uu,jmax_uu` |
| `nonh.F90:696` | `         do i=imin_uu,imax_uu` |
| `nonh.F90:697` | `            s%uu(i,j) = aur(i,j) + au(1,i,j)*dp(i+1,j)+au(0,i,j)*dp(i,j)` |
| `nonh.F90:698` | `         enddo` |
| `nonh.F90:699` | `      enddo` |
| `nonh.F90:701` | `      !v` |
| `nonh.F90:702` | `      if (sf1d) then` |
| `nonh.F90:703` | `         do i=imin_vv,imax_vv` |
| `nonh.F90:704` | `            s%vv(i,1) = avr(i,1) + av(1,i,1)*dp(i,1)+av(0,i,1)*dp(i,1)` |
| `nonh.F90:705` | `         enddo` |
| `nonh.F90:706` | `      else` |
| `nonh.F90:707` | `         do j=jmin_vv,jmax_vv` |
| `nonh.F90:708` | `            do i=imin_vv,imax_vv` |
| `nonh.F90:709` | `               s%vv(i,j) = avr(i,j) + av(1,i,j)*dp(i,j+1)+av(0,i,j)*dp(i,j)` |
| `nonh.F90:710` | `            enddo` |
| `nonh.F90:711` | `         enddo` |
| `nonh.F90:712` | `      endif` |

**확인:** 아래에서 활성점은 `nonhZ==1`인 점을 뜻한다.
**확인:** `nonh.F90:339–347`은 격자 거리의 역수를 계산한다.

| 위치 | 줄 원문 |
|---|---|
| `nonh.F90:339` | `         dyz  = s%dnz(1,:)` |
| `nonh.F90:340` | `         dyv  = s%dnv(1,:)` |
| `nonh.F90:341` | `         ddyz = 1.0_rKind/dyz` |
| `nonh.F90:342` | `         ddyv = 1.0_rKind/dyv` |
| `nonh.F90:344` | `         dxu  = s%dsu(:,1)` |
| `nonh.F90:345` | `         dxz  = s%dsz(:,1)` |
| `nonh.F90:346` | `         ddxu = 1.0_rKind/dxu` |
| `nonh.F90:347` | `         ddxz = 1.0_rKind/dxz` |

**확인:** `nonh.F90:477–503`은 일차원 활성점의 바닥 경사 계수와 바닥 속도 기여를 만든다.
**확인:** `nonh.F90:514–544`는 이차원 활성점의 바닥 경사 계수와 바닥 속도 기여를 만든다.
**확인:** 이 경로는 `zb`의 경사에 수평 속도를 양의 부호로 곱한다.
**확인:** `nonh.F90:754–756, 849–851`은 압력 보정 뒤의 바닥 속도를 계산한다.

| 위치 | 줄 원문 |
|---|---|
| `nonh.F90:472` | `      !AW Bottom` |
| `nonh.F90:473` | `      if (sf1d) then` |
| `nonh.F90:474` | `         do i=2,s%nx` |
| `nonh.F90:475` | `            if (nonhZ(i,1) == 1) then` |
| `nonh.F90:476` | `               if     (nonhU(i,1)*nonhU(i-1,1) == 1) then` |
| `nonh.F90:477` | `                  dzb_e = .5_rKind*(zbu(i,1)-zbu(i-1,1))*ddxz(i)` |
| `nonh.F90:478` | `                  dzb_w = dzb_e` |
| `nonh.F90:479` | `               elseif (nonhU(i  ,1) == 0) then` |
| `nonh.F90:480` | `                  dzb_e = .0_rKind` |
| `nonh.F90:481` | `                  dzb_w = .5_rKind*(s%zb(i,1)-zbu(i-1,1))*ddxz(i)` |
| `nonh.F90:482` | `               elseif (nonhU(i-1,1) == 0) then` |
| `nonh.F90:483` | `                  dzb_e = .5_rKind*(zbu(i,1)-s%zb(i,1))  *ddxz(i)` |
| `nonh.F90:484` | `                  dzb_w = .0_rKind` |
| `nonh.F90:485` | `               endif` |
| `nonh.F90:487` | `               if  (nonhV(i,1) == 1) then` |
| `nonh.F90:488` | `                  dzb_s = .0_rKind` |
| `nonh.F90:489` | `                  dzb_n = dzb_s` |
| `nonh.F90:490` | `               elseif (nonhV(i  ,1  ) == 0) then` |
| `nonh.F90:491` | `                  dzb_s = .0_rKind` |
| `nonh.F90:492` | `                  dzb_n = .5_rKind*(s%zb(i,1)-zbv(i,1))*ddyz(1)` |
| `nonh.F90:493` | `               endif` |
| `nonh.F90:495` | `               awb(1,i,1) =  dzb_e * au(0,i  ,1  )+dzb_w*au(1,i-1,1  )  &           !main diagonal` |
| `nonh.F90:496` | `               +  dzb_s * av(0,i  ,1  )+dzb_n*av(1,i  ,1)` |
| `nonh.F90:497` | `               awb(2,i,1) =  dzb_w *  au(0,i-1,1  )                             !west` |
| `nonh.F90:498` | `               awb(3,i,1) =  dzb_e *  au(1,i  ,1  )                             !east` |
| `nonh.F90:499` | `               awb(4,i,1) =  dzb_n *  av(0,i  ,1  )                             !south` |
| `nonh.F90:500` | `               awb(5,i,1) =  dzb_s *  av(1,i  ,1  )                             !north` |
| `nonh.F90:502` | `               awbr(i,1)  =  dzb_e*s%uu(i,1)+dzb_w*s%uu(i-1,1  ) &` |
| `nonh.F90:503` | `               +  dzb_s*s%vv(i,1)+dzb_n*s%vv(i  ,1  )` |
| `nonh.F90:504` | `            else` |
| `nonh.F90:505` | `               awb(:,i,1) = 0.0_rKind` |
| `nonh.F90:506` | `               awbr(i,1)  = 0.0_rKind` |
| `nonh.F90:507` | `            endif` |
| `nonh.F90:508` | `         enddo` |
| `nonh.F90:509` | `      else` |
| `nonh.F90:510` | `         do j=2,s%ny` |
| `nonh.F90:511` | `            do i=2,s%nx` |
| `nonh.F90:512` | `               if (nonhZ(i,j) == 1) then` |
| `nonh.F90:513` | `                  if     (nonhU(i,j)*nonhU(i-1,j) == 1) then` |
| `nonh.F90:514` | `                     dzb_e = .5_rKind*(zbu(i,j)-zbu(i-1,j))*ddxz(i)` |
| `nonh.F90:515` | `                     ! FB: this was dzs_e, which was not defined. Assumed it was a typo. TODO: check.` |
| `nonh.F90:516` | `                     dzb_w = dzb_e` |
| `nonh.F90:517` | `                  elseif (nonhU(i  ,j) == 0) then` |
| `nonh.F90:518` | `                     dzb_e = .0_rKind` |
| `nonh.F90:519` | `                     dzb_w = .5_rKind*(s%zb(i,j)-zbu(i-1,j))*ddxz(i)` |
| `nonh.F90:520` | `                  elseif (nonhU(i-1,j) == 0) then` |
| `nonh.F90:521` | `                     dzb_e = .5_rKind*(zbu(i,j)-s%zb(i,j))  *ddxz(i)` |
| `nonh.F90:522` | `                     dzb_w = .0_rKind` |
| `nonh.F90:523` | `                  endif` |
| `nonh.F90:525` | `                  if     (nonhV(i,j)*nonhV(i,j-1) == 1) then` |
| `nonh.F90:526` | `                     dzb_s = .5_rKind*(zbv(i,j)-zbv(i,j-1))*ddyz(j)` |
| `nonh.F90:527` | `                     dzb_n = dzb_s` |
| `nonh.F90:528` | `                  elseif (nonhV(i  ,j  ) == 0) then` |
| `nonh.F90:529` | `                     dzb_s = .0_rKind` |
| `nonh.F90:530` | `                     dzb_n = .5_rKind*(s%zb(i,j)-zbv(i,j-1))*ddyz(j)` |
| `nonh.F90:531` | `                  elseif (nonhV(i  ,j-1) == 0) then` |
| `nonh.F90:532` | `                     dzb_s = .5_rKind*(zbv(i,j)-s%zb(i,j))  *ddyz(j)` |
| `nonh.F90:533` | `                     dzb_n = .0_rKind` |
| `nonh.F90:534` | `                  endif` |
| `nonh.F90:536` | `                  awb(1,i,j) =  dzb_e * au(0,i  ,j  )+dzb_w*au(1,i-1,j  )  &           !main diagonal` |
| `nonh.F90:537` | `                  +  dzb_s * av(0,i  ,j  )+dzb_n*av(1,i  ,j-1)` |
| `nonh.F90:538` | `                  awb(2,i,j) =  dzb_w *  au(0,i-1,j  )                             !west` |
| `nonh.F90:539` | `                  awb(3,i,j) =  dzb_e *  au(1,i  ,j  )                             !east` |
| `nonh.F90:540` | `                  awb(4,i,j) =  dzb_n *  av(0,i  ,j-1)                             !south` |
| `nonh.F90:541` | `                  awb(5,i,j) =  dzb_s *  av(1,i  ,j  )                             !north` |
| `nonh.F90:543` | `                  awbr(i,j)  =  dzb_e*s%uu(i,j)+dzb_w*s%uu(i-1,j  ) &` |
| `nonh.F90:544` | `                  +  dzb_s*s%vv(i,j)+dzb_n*s%vv(i  ,j-1)` |
| `nonh.F90:545` | `               else` |
| `nonh.F90:546` | `                  awb(:,i,j) = 0.0_rKind` |
| `nonh.F90:547` | `                  awbr(i,j)  = 0.0_rKind` |
| `nonh.F90:548` | `               endif` |
| `nonh.F90:549` | `            enddo` |
| `nonh.F90:550` | `         enddo` |
| `nonh.F90:551` | `      endif` |
| `nonh.F90:752` | `         do i=imin_zs,imax_zs` |
| `nonh.F90:753` | `            if (nonhZ(i,1) == 1) then` |
| `nonh.F90:754` | `               s%wb(i,1) = awbr(i,1) + dp(i , 1)  * awb(1,i,1)                            &` |
| `nonh.F90:755` | `               + dp(i-1,1)  * awb(2,i,1) + dp(i+1,1  ) * awb(3,i,1) &` |
| `nonh.F90:756` | `               + dp(i  ,1)  * awb(4,i,1) + dp(i  ,1  ) * awb(5,i,1)` |
| `nonh.F90:846` | `         do j=jmin_zs,jmax_zs` |
| `nonh.F90:847` | `            do i=imin_zs,imax_zs` |
| `nonh.F90:848` | `               if (nonhZ(i,j) == 1) then` |
| `nonh.F90:849` | `                  s%wb(i,j) = awbr(i,j) + dp(i , j)  * awb(1,i,j)                            &` |
| `nonh.F90:850` | `                  + dp(i-1,j)  * awb(2,i,j) + dp(i+1,j  ) * awb(3,i,j) &` |
| `nonh.F90:851` | `                  + dp(i  ,j-1)* awb(4,i,j) + dp(i  ,j+1) * awb(5,i,j)` |

**확인:** 비정수압 제외점의 `nonh.F90:780–781, 881–882`도 `dzb` 계수에 수평 속도를 양의 부호로 곱한다.
**확인:** 이 분기의 `nonh.F90:760, 855`는 `dzb_w`에 `dzs_e`를 대입한다.
**확인:** 이 분기의 `nonh.F90:877–878`은 y 방향 마지막 조건에서 `dzb_e`와 `dzb_w`를 0으로 만든다.
**미확인:** 작성자는 이 제외점 분기의 전체 경계조건이 모든 조건에서 식 (1.8)과 같은지 확인하지 않았다.
다음 인용은 바닥 경사 부호 판정의 적용 범위를 보존한다.

| 위치 | 줄 원문 |
|---|---|
| `nonh.F90:757` | `            else` |
| `nonh.F90:758` | `               if     (s%wetU(i,1)*s%wetU(i-1,1) == 1) then` |
| `nonh.F90:759` | `                  dzb_e = .5_rKind*(zbu(i,1)-zbu(i-1,1))*ddxz(i)` |
| `nonh.F90:760` | `                  dzb_w = dzs_e` |
| `nonh.F90:761` | `               elseif (s%wetU(i  ,1) == 0) then` |
| `nonh.F90:762` | `                  dzb_e = .0_rKind` |
| `nonh.F90:763` | `                  dzb_w = .5_rKind*(s%zb(i,1)-zbu(i-1,1))*ddxz(i)` |
| `nonh.F90:764` | `               elseif (s%wetU(i-1,1) == 0) then` |
| `nonh.F90:765` | `                  dzb_e = .5_rKind*(zbu(i,1)-s%zb(i,1))  *ddxz(i)` |
| `nonh.F90:766` | `                  dzb_w = .0_rKind` |
| `nonh.F90:767` | `               else` |
| `nonh.F90:768` | `                  dzb_e = .0_rKind` |
| `nonh.F90:769` | `                  dzb_w = .0_rKind` |
| `nonh.F90:770` | `               endif` |
| `nonh.F90:772` | `               if     (s%wetV(i,1) == 1) then` |
| `nonh.F90:773` | `                  dzb_s = .0_rKind` |
| `nonh.F90:774` | `                  dzb_n = dzb_s` |
| `nonh.F90:775` | `               elseif (s%wetV(i  ,1  ) == 0) then` |
| `nonh.F90:776` | `                  dzb_s = .0_rKind` |
| `nonh.F90:777` | `                  dzb_n = .5_rKind*(s%zb(i,1)-zbv(i,1))*ddyz(1)` |
| `nonh.F90:778` | `               endif` |
| `nonh.F90:780` | `               s%wb(i,1) = + dzb_e*s%uu(i,1)+dzb_w*s%uu(i-1,1) &` |
| `nonh.F90:781` | `               + dzb_s*s%vv(i,1)+dzb_n*s%vv(i,1)` |
| `nonh.F90:782` | `            endif` |
| `nonh.F90:783` | `         enddo` |
| `nonh.F90:852` | `               else` |
| `nonh.F90:853` | `                  if     (s%wetU(i,j)*s%wetU(i-1,j) == 1) then` |
| `nonh.F90:854` | `                     dzb_e = .5_rKind*(zbu(i,j)-zbu(i-1,j))*ddxz(i)` |
| `nonh.F90:855` | `                     dzb_w = dzs_e` |
| `nonh.F90:856` | `                  elseif (s%wetU(i  ,j) == 0) then` |
| `nonh.F90:857` | `                     dzb_e = .0_rKind` |
| `nonh.F90:858` | `                     dzb_w = .5_rKind*(s%zb(i,j)-zbu(i-1,j))*ddxz(i)` |
| `nonh.F90:859` | `                  elseif (s%wetU(i-1,j) == 0) then` |
| `nonh.F90:860` | `                     dzb_e = .5_rKind*(zbu(i,j)-s%zb(i,j))  *ddxz(i)` |
| `nonh.F90:861` | `                     dzb_w = .0_rKind` |
| `nonh.F90:862` | `                  else` |
| `nonh.F90:863` | `                     dzb_e = .0_rKind` |
| `nonh.F90:864` | `                     dzb_w = .0_rKind` |
| `nonh.F90:865` | `                  endif` |
| `nonh.F90:867` | `                  if     (s%wetV(i,j)*s%wetV(i,j-1) == 1) then` |
| `nonh.F90:868` | `                     dzb_s = .5_rKind*(zbv(i,j)-zbv(i,j-1))*ddyz(j)` |
| `nonh.F90:869` | `                     dzb_n = dzb_s` |
| `nonh.F90:870` | `                  elseif (s%wetV(i  ,j  ) == 0) then` |
| `nonh.F90:871` | `                     dzb_s = .0_rKind` |
| `nonh.F90:872` | `                     dzb_n = .5_rKind*(s%zb(i,j)-zbv(i,j-1))*ddyz(j)` |
| `nonh.F90:873` | `                  elseif (s%wetV(i  ,j-1) == 0) then` |
| `nonh.F90:874` | `                     dzb_s = .5_rKind*(zbv(i,j)-s%zb(i,j))  *ddyz(j)` |
| `nonh.F90:875` | `                     dzb_n = .0_rKind` |
| `nonh.F90:876` | `                  else` |
| `nonh.F90:877` | `                     dzb_e = .0_rKind` |
| `nonh.F90:878` | `                     dzb_w = .0_rKind` |
| `nonh.F90:879` | `                  endif` |
| `nonh.F90:881` | `                  s%wb(i,j) = + dzb_e*s%uu(i,j)+dzb_w*s%uu(i-1,j) &` |
| `nonh.F90:882` | `                  + dzb_s*s%vv(i,j)+dzb_n*s%vv(i,j-1)` |
| `nonh.F90:883` | `               endif` |
| `nonh.F90:884` | `            enddo` |
| `nonh.F90:885` | `         enddo` |

**확인:** `flow_timestep.F90:215–237`은 y 이류 기여 `vdudy`를 계산한다.
**확인:** `flow_timestep.F90:564`는 `vdudy`를 양의 부호로 잔차에 넣는다.
**확인:** `flow_timestep.F90:576`은 이 잔차를 속도에서 뺀다.

| 위치 | 줄 원문 |
|---|---|
| `flow_timestep.F90:212` | `      if (par%ny>0) then` |
| `flow_timestep.F90:213` | `          do j=jmin_vv,jmax_vv` |
| `flow_timestep.F90:214` | `             do i=imin_vv,imax_vv` |
| `flow_timestep.F90:215` | `                s%vdudy(i,j)        = 0.d0` |
| `flow_timestep.F90:216` | `                qin               = .5d0*(s%qy(i,j-1)+s%qy(i+1,j-1))` |
| `flow_timestep.F90:217` | `                if (qin>0) then` |
| `flow_timestep.F90:218` | `                   dalfa          = s%alfau(i,j)-s%alfau(i,j-1)` |
| `flow_timestep.F90:219` | `                   uin            = s%uu(i,j-1)*cos(dalfa) + s%vu(i,j-1)*sin(dalfa)` |
| `flow_timestep.F90:220` | `                   if ((s%vv(i,j)-s%vv(i,j-1))>par%eps_sd) then` |
| `flow_timestep.F90:221` | `                      ! Conservation of energy head` |
| `flow_timestep.F90:222` | `                      s%vdudy(i,j)     = s%vdudy(i,j) + 0.5d0*(s%vv(i,j-1)+s%vv(i+1,j-1))*(s%uu(i,j)-uin)*s%dsc(i,j-1)*s%dsdnui(i,j)` |
| `flow_timestep.F90:223` | `                   else` |
| `flow_timestep.F90:224` | `                      ! Conservation of momentum` |
| `flow_timestep.F90:225` | `                      s%vdudy(i,j)     = s%vdudy(i,j) +        qin/s%hum(i,j)          *(s%uu(i,j)-uin)*s%dsc(i,j-1)*s%dsdnui(i,j)` |
| `flow_timestep.F90:226` | `                   endif` |
| `flow_timestep.F90:227` | `                endif` |
| `flow_timestep.F90:228` | `                qin               = -.5d0*(s%qy(i,j)+s%qy(i+1,j))` |
| `flow_timestep.F90:229` | `                if (qin>0) then` |
| `flow_timestep.F90:230` | `                   dalfa          = s%alfau(i,j)-s%alfau(i,j+1)` |
| `flow_timestep.F90:231` | `                   uin            = s%uu(i,j+1)*cos(dalfa) + s%vu(i,j+1)*sin(dalfa)` |
| `flow_timestep.F90:232` | `                   if ((s%vv(i,j+1)-s%vv(i,j))>par%eps_sd) then` |
| `flow_timestep.F90:233` | `                      ! Conservation of energy head` |
| `flow_timestep.F90:234` | `                      s%vdudy(i,j)     = s%vdudy(i,j) - 0.5d0*(s%vv(i,j)+s%vv(i+1,j))*(s%uu(i,j)-uin)*s%dsc(i,j)*s%dsdnui(i,j)` |
| `flow_timestep.F90:235` | `                   else` |
| `flow_timestep.F90:236` | `                      ! Conservation of momentum` |
| `flow_timestep.F90:237` | `                      s%vdudy(i,j)     = s%vdudy(i,j) +        qin/s%hum(i,j)       *(s%uu(i,j)-uin)*s%dsc(i,j)*s%dsdnui(i,j)` |
| `flow_timestep.F90:238` | `                   endif` |
| `flow_timestep.F90:239` | `                endif` |
| `flow_timestep.F90:240` | `             end do` |
| `flow_timestep.F90:241` | `          end do` |
| `flow_timestep.F90:242` | `      else` |
| `flow_timestep.F90:243` | `          ! do nothing vdudy already set to zero` |
| `flow_timestep.F90:244` | `      endif` |
| `flow_timestep.F90:561` | `      do j=jmin_uu,jmax_uu` |
| `flow_timestep.F90:562` | `         do i=imin_uu,imax_uu` |
| `flow_timestep.F90:563` | `            if(s%wetu(i,j)==1) then` |
| `flow_timestep.F90:564` | `                dudt = (s%ududx(i,j)+s%vdudy(i,j)-s%viscu(i,j) & !Ap,Robert,Jaap` |
| `flow_timestep.F90:565` | `                       + par%g*s%dzsdx(i,j) &` |
| `flow_timestep.F90:566` | `                       + s%taubx(i,j)/(par%rho*s%hu(i,j)) &  ! Dano: changed s%hum to s%hu NOT s%cf volume approach` |
| `flow_timestep.F90:567` | `                       + s%Fvegu(i,j)/(par%rho*s%hu(i,j)) &` |
| `flow_timestep.F90:568` | `                       - par%lwave*s%Fx(i,j)/(par%rho*s%hum(i,j)) &` |
| `flow_timestep.F90:569` | `                       - fc*s%vu(i,j) &` |
| `flow_timestep.F90:570` | `                       - par%rhoa*par%Cd*s%windsu(i,j)*sqrt(s%windsu(i,j)**2+s%windnv(i,j)**2)/(par%rho*s%hum(i,j)))    ! Kees: wind correction` |
| `flow_timestep.F90:571` | `                if (dudt>par%maxfacg*par%g) then` |
| `flow_timestep.F90:572` | `                    dudt=par%maxfacg*par%g` |
| `flow_timestep.F90:573` | `                elseif (dudt<-par%maxfacg*par%g) then` |
| `flow_timestep.F90:574` | `                    dudt=-par%maxfacg*par%g` |
| `flow_timestep.F90:575` | `                endif` |
| `flow_timestep.F90:576` | `                s%uu(i,j)=s%uu(i,j)-par%dt*dudt` |
| `flow_timestep.F90:577` | `            else` |

### 3. 판정

**판정: 불일치.**
이 판정은 보고서에 인쇄된 부호를 단일층 코드와 대조한 결과다.
다음 판정은 y 이류항과 동압 바닥 경사 항을 구분한다.
표의 “일치”는 해당 항의 부호에 관한 판정이다.

| 대조 대상 | 판정 | 이유 |
|---|---|---|
| 식 (1.13)의 y 이류항과 식 (1.17)의 y 이류항 | 불일치 | PDF 16쪽은 각각 음수와 양수를 인쇄한다. |
| 코드의 y 이류항과 식 (1.17)의 y 이류항 | 일치 | 운동량 잔차는 `+vdudy`를 사용한다. |
| 코드의 y 이류항과 식 (1.13)의 음수 y 이류항 | 불일치 | 잔차는 y 이류항을 음수로 뒤집지 않는다. |
| 코드의 동압 바닥 경사 항과 식 (1.14) 및 식 (2.15)의 첫 번째 표현 | 일치 | 압력 적분은 `\partial_x(H\bar p)-p_b\partial_x d` 형태다. |
| 코드의 동압 바닥 경사 항과 식 (1.17) 우변의 `-p\partial_x d` | 불일치 | 속도 갱신에서 바닥 경사 기여는 `+p_b\partial_x d/H` 형태다. |
| 코드의 압력 계수와 식 (2.15) 마지막 표현, 식 (2.18), 식 (2.19)의 압력항 | 불일치 | 코드의 두 깊이 괄호는 보고서 기호로 바꾸면 모두 `+d`다. |
| 활성점의 바닥 속도에서 수평 경사 항의 부호와 식 (1.8) | 일치 | `+u\partial_x zb+v\partial_y zb`는 `-u\partial_x d-v\partial_y d`다. |

다음 식은 코드의 대수적 해석이다.
다음 식은 보고서 인쇄 원문의 정정본이 아니다.

**해석:** `nonh.F90:1193–1195, 1238`에 `zs=\eta`, `zb=-d`를 대입하면 u 방향 압력 기여는 다음과 같다.

\[
\delta U_p=-\frac{\Delta t}{2\,\mathrm{hum}_{i,j}\,\mathrm{dxu}_i}
\left[(\eta_{i+1,j}+d_{i,j})p_{i+1,j}-(\eta_{i,j}+d_{i+1,j})p_{i,j}\right].
\]

**해석:** `nonh.F90:1216–1218, 1245`에 같은 대응을 대입하면 v 방향 압력 기여는 다음과 같다.

\[
\delta V_p=-\frac{\Delta t}{2\,\mathrm{hvm}_{i,j}\,\mathrm{dyv}_j}
\left[(\eta_{i,j+1}+d_{i,j})p_{i,j+1}-(\eta_{i,j}+d_{i,j+1})p_{i,j}\right].
\]

여기서 `p`는 코드의 기존 압력 `s%pres`를 나타낸다.
압력 보정 단계에서는 같은 자리에 `dp`가 들어간다.
근거는 `nonh.F90:697, 709`이다.

**해석:** 두 코드 식의 깊이 괄호는 모두 보고서의 `\eta+d`에 대응한다.
**해석:** 보고서에 인쇄된 둘째 괄호의 `\eta-d`는 같은 기준면 대응으로 코드와 같아지지 않는다.
다음 전개는 식 (2.15)의 두 표현을 대조하는 대수 반례다.
**해석:** 모든 격자점에서 `\eta=0`을 설정한다.
**해석:** 모든 격자점에서 `d=D`를 일정하게 설정한다.
**해석:** 모든 격자점에서 바닥 압력 `p=P`를 일정하게 설정한다.
**해석:** 이 조건에서 `H=D`와 `\bar p=P/2`가 성립한다.
**해석:** 식 (2.15)의 첫 번째 표현은 0이다.
**해석:** 식 (2.15)의 마지막 표현은 `DP/\Delta x`다.
**해석:** `D`와 `P`가 모두 0이 아니면 두 표현은 다르다.
**해석:** 따라서 식 (2.15)의 두 표현은 인쇄 그대로는 대수적으로 같지 않다.
근거는 보고서 인쇄 15쪽·PDF 25쪽 식 (2.15)다.

**해석:** 자유수면 동압을 0으로 두면 식 (1.14)의 바닥 경계 기여는 `-p_b\partial_x d`다.
**해석:** 이를 운동량식 우변의 압력 힘으로 바꾸면 부호가 양수가 된다.
**해석:** 코드의 동압 바닥 경사 부호는 이 압력 적분과 맞는다.
**해석:** 식 (1.17) 우변에 인쇄된 동압 바닥 경사 부호는 이 압력 적분과 맞지 않는다.
근거는 보고서 인쇄 6쪽·PDF 16쪽 식 (1.14), 식 (1.17), 인쇄 15쪽·PDF 25쪽 식 (2.15), `nonh.F90:1193–1195, 1238`이다.

**해석:** `zb=-d`이면 바닥고의 경사에 양의 부호를 곱하는 코드는 식 (1.8)의 음수 `d` 경사와 같은 부호다.
근거는 `nonh.F90:477–503, 514–544, 754–756, 849–851`이다.
**미확인:** 이 부호 판정은 제외점의 `dzb_w=dzs_e` 대입까지 전체 식의 일치를 확인한 판정이 아니다.
근거는 `nonh.F90:760, 855`이다.
**미확인:** 작성자는 인쇄 불일치의 편집 원인이나 작성자의 수정 의도를 확인하지 않았다.
**미확인:** 작성자는 이 부호 차이의 수치 영향을 모델 실행으로 확인하지 않았다.

### 4. 현재 노트 서술

| 위치 | 줄 원문 |
|---|---|
| `models/XBeach/source-analysis/xbeach_nonh.md:39` | ``이는 `nonh.F90:201-247`의 `SELECT CASE`와 내부 IF를 전사한 표다. `.true./.false.` 논리형 SELECT가 아니다. 각 루틴 내부의 공간 경계·wet 조건은 별도로 적용된다.`` |
| `models/XBeach/source-analysis/xbeach_nonh.md:43` | ``세 corrector는 `solver_solvemat(mat,rhs,dp,nx,ny,par)`로 압력 선형계를 풀고 속도를 보정한다. 1층 경로는 `s%pres += dp`를 수행한다. 두 reduced 2층 경로는 `secorder==1`이면 `s%pres += dp`, 그 외에는 `s%pres = dp`를 사용한다. (`nonh.F90:683-697, 1411-1422, 2162-2176`)`` |
| `models/XBeach/source-analysis/xbeach_nonh.md:45` | ``이 값은 nonh 루틴 내부의 수평·연직 속도 보정에 쓰인다. 기존 설명의 `dp → ph → g∂(zs+ph)` 연결은 잘못된 귀속이었다. `flow`의 `zs+ph` 경사는 선박 외력 경로이며 비정수압 보정과 별도로 읽어야 한다. (`nonh.F90:1234-1262`; `flow_timestep.F90:131-149`; [[xbeach_flow_solver]])`` |

**확인:** 노트 43행은 압력 저장과 보정값 누적 방식을 적는다.
**확인:** 노트 45행은 선박 압력과 비정수압 보정을 구분한다.
**확인:** 작성자는 `models/XBeach/source-analysis/xbeach_nonh.md:1–58`에서 이 주제의 바닥 경사 부호 서술을 찾지 못했다.
**확인:** 해당 노트에는 식 (1.13), 식 (1.17), 식 (2.15), 식 (2.18), 식 (2.19)의 부호 대조가 없다.
**판정:** 이 노트의 현재 문장들은 이번 부호 판정과 충돌하지 않는다.
**확인:** 이 노트는 이번 부호 판정을 서술하지 않는다.

### 5. 노트 수정안

없음.
현재 노트는 대조한 바닥 경사 항의 부호를 주장하지 않는다.

렌더한 이미지 목록: `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/pages/`의 `cmp-master-p29-029.png`, `cmp-nonh-p13-13.png`, `cmp-nonh-p15-15.png`, `cmp-nonh-p16-16.png`, `cmp-nonh-p25-25.png`, `cmp-nonh-p26-26.png`. 작성자는 이 이미지들을 모두 열었다. 열지 못한 파일: 없음.

## 5 차이 결론

분류별 개수는 기존 결론표의 9행을 센 값이다: A 판 차이 0행, B 문서 오기 5행, C 문서 누락 2행, D 문서만 있음 0행, E 코드 결함 후보 2행, F 표기 차이 0행, G 판단 근거 부족 0행. 이번 검증에서 추가한 CV-S-XB-01의 E 1행은 기존 9행 집계와 구분한다. [10-12 결론 검증 보완]

대상은 본문 판정문 5행과 세부 대조표 4행이다.
보고서 줄 번호는 이 절을 추가하기 전의 295·308·510·524·1068·1075·1077·1079·1080행이다.
1068행은 C절의 총괄 판정이다.
이 집계는 총괄행과 세부행을 함께 센 원문 판정행 수다.
기존 행에 붙인 정정은 같은 물리적 줄에 추가했다.
기존 행의 줄 번호는 바뀌지 않았다.
이 절의 원문 인용은 이번 작업에서 `nl -ba`로 확인했다.
PDF 근거는 아래에 적은 판독 기록의 쪽 번호를 사용한다.
식 변형과 정적 판독의 결론은 `해석:`으로 구분한다.

| 행 ID 또는 보고서 줄 | 항목 | 결론(A–G) | 근거 | 노트에 쓸 결론 문장(한 문장, 한국어) |
|---|---|---|---|---|
| 295 (A절) | Lagrangian 속도 식과 `veguntow`의 Eulerian 속도 선택 | C 문서 누락 | 확인: `_staging/recovery/read/XBeach/manuals/pdfs/XBeach_manual_master.pdf/p019-036.md:26`의 PDF 29쪽 식 (2.58)은 `u^L(t)\left\vert u^L(t)\right\vert`를 쓴다. `_staging/recovery/read/XBeach/manuals/pdfs/XBeach_manual_kingsday.pdf/p019-036.md:26`의 PDF 29쪽 식 (2.53)도 Lagrangian 속도를 쓴다. `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:513`의 `if (par%veguntow == 1) then` 아래의 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:515`의 `Fvgtu = max((min(aht,watr)-ahtold),0d0)*0.5d0*s%Cdveg(i,j,m)*s%bveg(i,j,m)*s%Nveg(i,j,m)*(s%ueu(i,j)*s%vmageu(i,j))`는 Eulerian 성분을 쓴다. `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/flow_timestep.F90:858`의 `s%ueu = s%uu - usu`가 그 성분을 정의한다. 확인: `models/XBeach/raw/manuals/readthedocs/en/latest/input_parameters.html:2713`의 `<td><p><p>Include undertow in phase-averaged vegetati</p>`와 같은 파일 2715행의 `<td><p><p>1</p>`는 `veguntow`의 설명과 기본값이다. 해석: 식생 이론절은 이 스위치의 Eulerian 분기를 생략한다. 문서의 Lagrangian 표기는 `veguntow=0`의 속도 종류에 대응한다. 판 이력과 분기 근거는 5.1에 적는다. | 표준 식생 경로는 기본값인 `veguntow=1`에서 Eulerian 속도로 평균류·장파 항력을 계산한다. |
| 308 (A절) | v점 성분에 u점 속력을 곱하는 선택의 정당성 | E 코드 결함 후보 | 확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:516,520`은 v점 성분에 같은 첨자의 u점 속력을 곱한다.<br>확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/flow_timestep.F90:807–808`은 주변 v 속도의 네 점 평균으로 u점의 횡속도 `s%vu`를 만든다.<br>확인: 같은 파일 861행의 원문은 `s%vmagu=sqrt(s%uu**2+s%vu**2)`이다.<br>확인: 같은 파일 931행의 원문은 `s%vmagv=sqrt(s%uv**2+s%vv**2)`이다.<br>해석: 5.2의 원문 대입에서는 v점 속력이 양수여도 u점 속력이 0이 되어 520행의 v 방향 항력이 사라진다.<br>해석: 같은 속도 배치를 x 방향으로 바꾸면 519행의 u 방향 항력은 남는다.<br>확인: `flow_timestep.F90:535,550`의 바닥마찰은 방향마다 해당 격자점의 속력을 쓴다.<br>확인: `vegetation.F90:871,877`의 porous 경로는 각 방향의 셀 경계로 힘을 보간한다.<br>해석: 축 교환의 비대칭과 다른 항력 경로의 격자 처리 차이는 E 후보의 근거이다.<br>해석: `models/XBeach/raw/manuals/readthedocs/en/latest/_sources/xbeach_manual.rst.txt:1236`의 양의 계수와 0이 아닌 속도에 대한 항력식도 5.2에서 대조했다.<br>확인: 추가 검색 파일·검색어·식 전개는 5.2에 적는다. | 표준 식생 경로가 v 방향 항력에 u점 속력을 사용하는 동작은 축 교환 시 항력이 비대칭이 되는 코드 결함 후보다. [10-12 G 재판정] |
| 510 (B절) | 호출 시작 초기화와 이전 시간 단계 값의 누적 가설 | C 문서 누락 | 확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:452`의 `FvgCav = 0.d0`와 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:453`의 `FvgCau = 0.d0`는 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:475`의 `do j=1,s%ny+1`보다 앞에 있다. `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/libxbeach.F90:303`의 `if (par%vegetation==1)                                  call vegatt         (s,par)`의 표준 경로는 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:342`의 `call momeqveg(s,par)`를 호출한다. 해석: 호출 시작의 대입은 이전 시간 단계의 값을 지운다. 이 행의 기존 불일치 판정은 누적 가설을 기각한다. C는 문서에 호출별 초기화 설명이 없는 점을 분류한다. 확인: `_staging/recovery/read/XBeach/manuals/pdfs/XBeach_manual_master.pdf/p019-036.md:26`의 PDF 29쪽 식 (2.58)은 시각 `t`의 층별 합을 적는다. 이 식과 readthedocs 입력 표는 지역 변수의 초기화 위치를 지정하지 않는다. 검색 범위와 351행의 검색 결과 정정은 5.3에 적는다. | `momeqveg`는 호출마다 `FvgCau`와 `FvgCav`를 0으로 초기화한다. |
| 524 (B절) | 초기화 규칙의 공백과 같은 호출의 canopy 힘 재사용 | E 코드 결함 후보 | 확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:502`의 `if (ahtold > wacr) then ! if plant section is entirely above wave crest, then do nothing`의 분기는 `FvgCau`와 `FvgCav`에 대입하지 않는다. `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:554`의 `if (par%vegcanflo == 1) then ! add in canopy flow (Luhar et al., 2010)` 아래에서 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:555`의 `Fvgu(i,j) = Fvgu(i,j) + FvgCau`와 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:556`의 `Fvgv(i,j) = Fvgv(i,j) + FvgCav`를 실행한다. 확인: 다른 층 처리 경로의 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:536`의 `FvgCan = max((min(aht,watr)-ahtold),0d0)/s%hh(i,j)*0.5d0*s%Cdveg(i,j,m)*s%bveg(i,j,m)*s%Nveg(i,j,m)*ucan**2`는 해당 층의 잠긴 높이를 힘에 곱한다. 해석: 파봉 위 층의 값 재사용은 502행의 `then do nothing` 주석과 모순된다. 해석: 같은 층의 힘을 잠긴 높이로 제한하는 536행의 다른 코드 경로와도 모순된다. 두 종류의 근거를 충족하므로 정적 판독의 결함 후보로 분류한다. 문서의 초기화 규칙은 여전히 확인하지 못했다. `[10-12 결론 정정]`의 상세 근거는 5.3에 적는다. | `vegcanflo==1`인 파봉 위 층이 같은 호출의 앞선 층에서 계산한 0이 아닌 canopy 힘을 다시 더하는 동작은 결함 후보다. |
| 1068 (C절 총괄) | 단일층 코드와 비정수압 보고서의 인쇄 부호 차이 | B 문서 오기 | 확인: `_staging/recovery/read/XBeach/manuals/reports/non-hydrostatic_report_draft.pdf/p001-018.md:29`의 PDF 16쪽 식 (1.13)과 식 (1.17)은 y 이류항의 부호가 다르다. `_staging/recovery/read/XBeach/manuals/reports/non-hydrostatic_report_draft.pdf/p019-036.md:22`의 PDF 25쪽 식 (2.15)은 첫 표현과 마지막 표현이 일정한 수심·압력에서도 같지 않다. 코드의 압력 계수는 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/nonh.F90:1195`의 `au(0,i,j) = + (s%zs(i  ,j) - s%zb(i+1,j))*vol`를 쓴다. 해석: 같은 문서 내부의 모순으로 B를 판정한다. 아래 1075·1077·1079·1080행과 5.4가 각 항의 근거다. 이 총괄행도 대상 행 수에 포함한다. | 단일층 코드와 대조한 비정수압 보고서의 y 이류항과 동압 압력항에는 문서 내부 모순으로 확인한 오기가 있다. |
| 1075 (C절 표) | 식 (1.13)과 식 (1.17)의 y 이류항 | B 문서 오기 | 확인: `_staging/recovery/read/XBeach/manuals/reports/non-hydrostatic_report_draft.pdf/p001-018.md:29`의 PDF 16쪽 식 (1.13)은 `-\frac{\partial}{\partial y}\left(HUV-\int_{-d}^{\eta}(v-V)(u-U)dz\right)`를 인쇄한다. 같은 쪽 식 (1.17)은 `+\frac{\partial}{\partial y}\left(HUV-\frac{1}{\rho}H\bar\tau_{yx}\right)`를 인쇄한다. 해석: 연직으로 균일한 속도와 평탄한 경계에서 식 (1.13)의 원래 적분은 `+\partial_y(HUV)`가 된다. 5.4의 반례가 음수 부호를 배제한다. | 비정수압 보고서 식 (1.13)의 y 이류항 앞 음수 부호는 문서 오기다. |
| 1077 (C절 표) | 코드의 y 이류항과 식 (1.13)의 음수 부호 | B 문서 오기 | 확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/flow_timestep.F90:564`의 `dudt = (s%ududx(i,j)+s%vdudy(i,j)-s%viscu(i,j) & !Ap,Robert,Jaap`는 잔차에 `+s%vdudy(i,j)`를 넣는다. `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/flow_timestep.F90:576`의 `s%uu(i,j)=s%uu(i,j)-par%dt*dudt`는 그 잔차를 뺀다. 확인: `_staging/recovery/read/XBeach/manuals/reports/non-hydrostatic_report_draft.pdf/p001-018.md:29`의 PDF 16쪽 식 (1.17)은 좌변에 `+\frac{\partial}{\partial y}\left(HUV-\frac{1}{\rho}H\bar\tau_{yx}\right)`를 둔다. 해석: 시간 갱신에서 잔차를 빼는 동작은 좌변 이류항의 부호를 바꾸지 않는다. 식 (1.13)의 문서 오기가 차이의 원인이다. | 코드는 운동량 잔차에 y 이류항을 양의 부호로 더한다. |
| 1079 (C절 표) | 식 (1.17) 우변의 동압 바닥 경사 부호 | B 문서 오기 | 확인: `_staging/recovery/read/XBeach/manuals/reports/non-hydrostatic_report_draft.pdf/p001-018.md:29`의 PDF 16쪽 식 (1.14)은 `\frac{\partial H\bar p}{\partial x}-\left[p\frac{\partial z}{\partial x}\right]_{z=-d}^{z=\eta}`를 인쇄한다. 같은 쪽 식 (1.17)은 우변에 `-p\frac{\partial d}{\partial x}`를 인쇄한다. `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/nonh.F90:1194`의 `au(1,i,j) = - (s%zs(i+1,j) - s%zb(i  ,j))*vol`와 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/nonh.F90:1195`의 `au(0,i,j) = + (s%zs(i  ,j) - s%zb(i+1,j))*vol`가 코드의 두 압력 계수다. 해석: `z=-d`와 수면 동압 0을 대입하면 식 (1.14)의 압력 적분은 `\partial_x(H\bar p)-p_b\partial_x d`다. 우변 힘으로 옮긴 바닥 경사 항은 `+p_b\partial_x d`다. 식 (1.17)의 우변 음수 부호가 같은 문서의 압력 적분과 모순된다. 5.4에서 코드 갱신과 대조한다. | 비정수압 보고서 식 (1.17) 우변의 동압 바닥 경사 항은 양의 부호로 써야 한다. |
| 1080 (C절 표) | 식 (2.15) 마지막 표현과 식 (2.18)·(2.19)의 압력 계수 | B 문서 오기 | 확인: `_staging/recovery/read/XBeach/manuals/reports/non-hydrostatic_report_draft.pdf/p019-036.md:22`의 PDF 25쪽 식 (2.15)은 둘째 괄호에 `\left(\eta^{n+1}_{i,j} - d^{n+1}_{i+1,j}\right)`를 인쇄한다. `_staging/recovery/read/XBeach/manuals/reports/non-hydrostatic_report_draft.pdf/p019-036.md:23`의 PDF 26쪽 식 (2.18)과 식 (2.19)도 그 음수 부호를 쓴다. 확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/nonh.F90:1195`의 `au(0,i,j) = + (s%zs(i  ,j) - s%zb(i+1,j))*vol`와 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/nonh.F90:1218`의 `av(0,i,j)  = +(s%zs(i  ,j  ) - s%zb(i  ,j+1))*vol`의 괄호는 `zb=-d`를 대입하면 모두 `+d`다. 해석: `\eta=0`, `d=D`, `p=P`가 일정하면 식 (2.15)의 첫 표현은 0이다. 마지막 표현은 `DP/\Delta x`다. 0이 아닌 `D`와 `P`에서 두 표현이 모순된다. 같은 오기가 압력 보정식에 반복된다. 식 (2.19)의 V 압력항에 남은 `\Delta x`도 5.4에서 대조한다. | 단일층 코드는 u·v 방향 압력 계수의 두 깊이 괄호에 모두 `zs-zb`를 사용한다. |
| <a id="cv-s-xb-01"></a>CV-S-XB-01 | canopy 힘 합산의 차원 | E 코드 결함 후보 | [식생 정본](../../../models/XBeach/source-analysis/xbeach_vegetation.md#cv-s-xb-01). `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:515–564`의 항력과 canopy 힘을 대조했다. `variables.def:82,121,274–280`과 `params.def:103,502`의 차원을 확인했다. 소비식은 `flow_timestep.F90:567,603`이다. | 표준 식생의 vegcanflo==1 경로는 m/s²인 canopy 항과 m²/s²인 장파·평균류 항을 합산한다. 수심을 곱하는 보정 경로는 찾지 못했다. [10-12 결론 검증 보완] |

### 5.1 속도 선택의 문서 누락과 판 이력

확인: `_staging/recovery/read/XBeach/manuals/pdfs/XBeach_manual_master.pdf/p001-018.md:24`의 PDF 9쪽은 적용 판을 `XBeach version 1.22 (revision 4567)`로 적는다.
확인: `_staging/recovery/read/XBeach/manuals/pdfs/XBeach_manual_kingsday.pdf/p001-018.md:23`의 PDF 8쪽도 같은 적용 판을 적는다.
확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:36`의 `! Version 2.0:`와 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:38`의 `! Arnold van Rooijen, okt 2015,`는 식생 모듈의 판과 날짜를 적는다.
확인: `models/XBeach/raw/source_code/trunk/ChangeLog:1`의 `Please see the subversion log for the latest changes, using the command:`와 같은 파일 2행의 `svn log`는 변경 내역을 외부 이력으로 안내한다.
확인: `models/XBeach/raw/source_code/trunk/NEWS:1`의 `Please visit the XBeach website for the latest news:`는 뉴스 웹사이트를 안내한다.
해석: 이 두 파일은 `veguntow` 분기를 도입한 변경 기록을 제공하지 않는다.
해석: 식생 모듈의 판 표기만으로 Lagrangian 식에서 Eulerian 분기로 바뀐 시점을 확정할 수 없다.

확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90:1338`의 `par%veguntow      = readkey_int   ('params.txt', 'veguntow', 1,0,1,silent=.true.)`는 입력 표의 기본값 1과 일치한다.
확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:519`의 `Fvgtu = max((min(aht,watr)-ahtold),0d0)*0.5d0*s%Cdveg(i,j,m)*s%bveg(i,j,m)*s%Nveg(i,j,m)*(s%uu(i,j)*s%vmagu(i,j))`는 `veguntow`를 끈 분기에서 GLM 속도를 사용한다.
확인: `models/XBeach/raw/manuals/readthedocs/en/latest/_sources/xbeach_manual.rst.txt:1028`의 `u^{L} =u^{E} +u^{S} \quad and\quad v^{L} =v^{E} +v^{S}`는 Lagrangian 속도와 Eulerian 속도의 관계다.
확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/flow_timestep.F90:926`의 `s%vev = s%vv - vsv`도 Stokes 성분을 뺀다.
확인: `models/XBeach/raw/manuals/readthedocs/en/latest/_sources/xbeach_manual.rst.txt:1228`의 `account the velocity due to mean flow and infragravity waves, we use`와 `models/XBeach/raw/manuals/readthedocs/en/latest/_sources/xbeach_manual.rst.txt:1229`의 ``the Lagrangian velocity (:math:`{u}^{L}`) here. The vegetation-induced``는 저장한 readthedocs 이론절의 서술이다.
해석: 이론절은 `veguntow`에 따른 속도 선택을 설명하지 않는다.
해석: 코드의 Eulerian 분기는 이름만 바꾼 계산이 아니다.
해석: Stokes 속도가 0이 아니면 두 속도 종류는 달라진다.
해석: 따라서 295행은 분기 설명의 문서 누락으로 분류한다.
해석: 이 결론은 v점에서 쓰는 속력 배열의 정당성까지 판정하지 않는다.

### 5.2 v 방향 식생 항력의 격자 위치와 축 교환 [10-12 G 재판정]

확인: 이번 검색 범위는 `models/XBeach/raw/` 전체와 `_staging/recovery/read/XBeach/` 전체이다.
확인: `rg --hidden --no-ignore`로 코드 주석·문서·판독 기록을 검색했다.
확인: PDF와 DOCX 문서의 텍스트도 같은 검색어로 검색했다.
확인: `rg --files --hidden --no-ignore`로 다른 코드 판과 시험·예제 파일의 존재를 확인했다.
추가 검색어: `Fvgtv`·`Fvgtu`·`vmageu`·`vmagev`·`vmagu`·`vmagv`·`vegetation`·`veguntow`·`vegcanflo`·`porcanflow`·`stagger`·`drag`.
추가 검색 파일: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90`·`flow_timestep.F90`·`variables.def`·`models/XBeach/raw/source_code/trunk/ChangeLog`·`NEWS`·`models/XBeach/raw/source_code/trunk/test/`·`models/XBeach/raw/manuals/examples/Wong2016/`·`models/XBeach/raw/manuals/`·`models/XBeach/raw/source_code/trunk/doc/manual/`.
확인: `models/XBeach/raw/source_code/trunk/ChangeLog:1–2`는 외부 SVN 이력 조회만 안내한다.
확인: `models/XBeach/raw/source_code/trunk/test/xbeachlibrary_test/run_xbeach_tests.f90:13`은 `call runtests( allInterpTests )`를 호출한다.
확인: 검색 범위에는 `Fvgtv`의 속력 선택을 설명하는 변경 기록이나 식생 항력의 격자 시험이 없다.

확인: `models/XBeach/raw/manuals/readthedocs/en/latest/_sources/xbeach_manual.rst.txt:1236`의 원문은 다음과 같다.

~~~text
   \begin{array}{l} {F_{v} (t)=\sum _{i=1}^{n_{v} }F_{v,i}  (t)} \\ {F_{v,i} (t)=\frac{1}{2} \rho \widetilde{C}_{D,i} b_{v,i} N_{v,i} h_{v,i} u^{L} (t)\left|u^{L} (t)\right|} \end{array}
~~~

확인: 이번에 연 RST 원문은 한 겹의 절댓값 기호를 쓴다.
해석: 이 식에서 항력계수·줄기 지름·밀도·잠긴 높이가 양수이면 0이 아닌 속도에 대응하는 항력도 0이 아니다.
확인: `models/XBeach/raw/manuals/readthedocs/en/latest/_sources/numerical_implementation.rst.txt:7–11`은 속도를 u·v 셀 경계에 정의한다.
해석: 한 방향만 흐르는 경우에는 위 식의 절댓값을 스칼라 속도의 절댓값으로 대조할 수 있다.

확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:319–342`는 porous 경로와 표준 `momeqveg` 경로를 구분한다.
해석: 다음 대입 검토는 표준 경로의 잠긴 식생 한 층에 적용한다.
해석: 파랑과 Stokes drift는 0으로 둔다.
해석: `par%vegnonlin`·`par%vegcanflo`·`par%sedtrans`는 0으로 둔다.
해석: 식생 계수와 잠긴 높이는 공간적으로 같은 양수로 둔다.
해석: 경계 밖의 젖은 내부 격자에서 `s%wetu`와 `s%wetv`는 1로 둔다.
해석: 이 설정은 추가 힘을 더하는 `vegetation.F90:550–557`의 분기를 제외한다.
확인: `flow_timestep.F90:855–864,925–934`에서 Stokes drift가 0이면 Eulerian 속도와 Lagrangian 속도가 같다.

확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/flow_timestep.F90:805–808`의 원문은 다음과 같다.

~~~fortran
      ! V-velocities at u-points
      if (s%ny>0) then
         s%vu(1:s%nx,2:s%ny)= 0.25d0*(s%vv(1:s%nx,1:s%ny-1)+s%vv(1:s%nx,2:s%ny)+ &
         s%vv(2:s%nx+1,1:s%ny-1)+s%vv(2:s%nx+1,2:s%ny))
~~~

해석: 같은 x 방향의 두 열에서 j번째 v 속도를 같은 양수로 둔다.
해석: 두 열의 j-1번째 v 속도는 그 값의 음수로 둔다.
해석: 위 네 점 평균에 이 값을 대입하면 해당 u점의 `s%vu`는 0이다.
확인: `flow_timestep.F90:861`의 원문은 `s%vmagu=sqrt(s%uu**2+s%vu**2)`이다.
해석: 모든 `s%uu`를 0으로 두면 해당 u점의 `s%vmagu`도 0이다.
확인: `flow_timestep.F90:879–880`은 `s%uu`의 네 점 평균으로 `s%uv`를 계산한다.
확인: `flow_timestep.F90:931`의 원문은 `s%vmagv=sqrt(s%uv**2+s%vv**2)`이다.
해석: 이 대입에서는 해당 v점의 `s%vmagv`가 양수이다.

확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:519–520`의 원문은 다음과 같다.

~~~fortran
                        Fvgtu = max((min(aht,watr)-ahtold),0d0)*0.5d0*s%Cdveg(i,j,m)*s%bveg(i,j,m)*s%Nveg(i,j,m)*(s%uu(i,j)*s%vmagu(i,j))
                        Fvgtv = max((min(aht,watr)-ahtold),0d0)*0.5d0*s%Cdveg(i,j,m)*s%bveg(i,j,m)*s%Nveg(i,j,m)*(s%vv(i,j)*s%vmagu(i,j))
~~~

해석: 위 대입에서 520행은 0이 아닌 v점 속도에 0인 u점 속력을 곱한다.
해석: 따라서 이 층의 v 방향 항력은 0이 된다.
확인: `vegetation.F90:548`은 `Fvgv(i,j) = Fvgv(i,j) + Fvgtv`로 이 값을 합산한다.
확인: 같은 파일 564행은 `s%Fvegv = Fvgv*par%rho ! make sure units of drag force are consistent (N/m2)`로 힘을 전달한다.
확인: `flow_timestep.F90:603`은 v 방향 운동량 잔차에 `+ s%Fvegv(i,j)/(par%rho*s%hv(i,j)) &`를 넣는다.
해석: 이 전달 경로에는 v점 속력을 복구하는 보간이 없다.

해석: 같은 격자와 식생을 유지하면서 위 속도 배치를 x 방향으로 바꾸어 본다.
해석: 모든 v 속도는 0으로 둔다.
해석: 해당 u 속도는 양수로 둔다.
해석: i-1번째 u 속도는 그 값의 음수로 둔다.
확인: `flow_timestep.F90:861`의 원문은 `s%vmagu=sqrt(s%uu**2+s%vu**2)`이다.
해석: 이 경우 `s%vmagu`는 해당 u 속도의 절댓값이다.
해석: `vegetation.F90:519`에 같은 양의 식생 계수를 대입하면 u 방향 항력은 양수이다.
해석: 이 두 대입은 축을 바꿀 때 항력의 소실 여부가 바뀌는 비대칭을 보인다.
해석: 이 비대칭은 현재 코드 식을 대입해 얻은 결과이다.
해석: 이 결과는 균일 유속에서 두 격자점 속력이 같은 경우에는 나타나지 않는다.

확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/flow_timestep.F90:535`의 원문은 `s%taubx=s%cfu*par%rho*s%ueu*sqrt((1.16d0*s%urms)**2+s%vmageu**2) !Ruessink et al, 2001`이다.
확인: 같은 파일 550행의 원문은 `s%tauby=s%cfv*par%rho*s%vev*sqrt((1.16d0*s%urms)**2+s%vmagev**2) !Ruessink et al, 2001`이다.
해석: 바닥마찰 경로는 각 방향의 성분과 같은 격자점의 속력을 사용한다.
확인: `vegetation.F90:812–814`는 porous 경로에서 중심의 힘을 셀 경계로 보간한다고 적는다.
확인: 같은 파일 871행의 원문은 `s%Fvegu(i,j) = (Fcanu(i,j)+Fcanu(i+1,j))/2`이다.
확인: 같은 파일 877행의 원문은 `s%Fvegv(i,j) = (Fcanv(i,j)+Fcanv(i,j+1))/2`이다.
해석: 이 두 경로는 힘이나 속력의 격자 위치를 각 방향에 맞추는 비교 근거이다.

해석: 308행은 축 교환의 비대칭과 다른 항력 경로의 격자 처리 차이에 근거하여 E 코드 결함 후보로 바꾼다.
해석: 한 방향 항력의 소실은 문서의 양의 계수와 0이 아닌 속도에 대한 항력식과도 맞지 않는다.
해석: `vegetation.F90:513–516`의 Eulerian 분기에도 같은 u점 속력 선택이 있으므로 Stokes drift가 0인 위 대입이 적용된다.
미확인: raw의 변경 기록에는 이 대입의 작성 의도가 없다.
해석: 작성 의도의 부재는 위 코드 식의 비대칭을 E 후보로 기록하는 것을 막지 않는다.
확인: 이 재판정은 모델 실행이나 컴파일을 사용하지 않았다.

### 5.3 호출 초기화와 파봉 위 층의 힘 재사용

확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:319`의 `if (par%porcanflow == 1) then`는 `porcanflow` 경로를 구분한다.
확인: 510행과 524행의 결론은 그 밖의 표준 경로가 호출하는 `momeqveg`에 적용한다.
확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90:1337`의 `par%vegcanflo     = readkey_int   ('params.txt', 'vegcanflo',0,0,1,silent=.true.)`는 `vegcanflo` 기본값을 0으로 읽는다.
해석: 524행의 결함 후보는 `vegcanflo==1` 조건에서 발생 가능한 값 재사용이다.

확인: `_staging/recovery/read/XBeach/manuals/` 전체에서 `FvgCau`, `FvgCav`, `vegcanflo`를 검색했다.
확인: `_staging/recovery/read/XBeach/manuals/readthedocs_markdown/en/latest/input_parameters.md.md:23`은 `vegcanflo`를 기록한다.
확인: 이 판독 기록의 설명 원문은 `Include incanopy flow [1] or not [0]`다.
확인: HTML 원문의 `models/XBeach/raw/manuals/readthedocs/en/latest/input_parameters.html:2665`의 `<tr class="row-odd"><td><p><p>vegcanflo</p>`와 `models/XBeach/raw/manuals/readthedocs/en/latest/input_parameters.html:2667`의 `<td><p><p>Include incanopy flow [1] or not [0]</p>`도 이 입력을 확인한다.
확인: `FvgCau`와 `FvgCav`의 초기화 규칙은 지정한 판독 기록에서 찾지 못했다.
[10-12 결론 정정] 보고서 351행의 `vegcanflo` 검색 결과 없음은 잘못된 서술이다.
해석: 입력 설명의 존재는 호출별 초기화 규칙의 존재를 뜻하지 않는다.
해석: 510행의 누적 가설은 호출 시작의 0 대입으로 기각한다.

확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:487`의 `do m=1,s%nsecveg(i,j)`는 식생 층을 순서대로 처리한다.
확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:544`의 `ahtold = aht`는 처리한 층의 높이를 다음 층의 `ahtold`로 넘긴다.
확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:498`의 `watr = s%hh(i,j)`와 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:499`의 `wacr = s%hh(i,j)`는 비선형 파형을 쓰지 않는 분기의 골·봉우리 높이다.
해석: 이 분기에서 `ahtold>wacr`이면 `min(aht,watr)-ahtold<0`이다.
해석: 따라서 536행의 잠긴 높이 인자 `max((min(aht,watr)-ahtold),0d0)`는 0이다.
확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:539`의 `FvgCau = FvgCan*costhm(i,j)`와 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:540`의 `FvgCav = FvgCan*sinthm(i,j)`는 잠긴 층 분기의 힘 성분을 새로 대입한다.
확인: 파봉 위 층의 분기는 이 두 대입을 건너뛴다.
해석: 앞선 층의 힘이 0이 아니면 다음 파봉 위 층의 합산은 그 값을 재사용한다.
해석: 이 값 재사용은 `then do nothing` 주석과 모순된다.
해석: 이 값 재사용은 다른 분기에서 잠긴 높이를 곱해 해당 층의 힘을 제한하는 처리와도 모순된다.
[10-12 결론 정정] 524행은 이 두 종류의 정적 근거로 E 코드 결함 후보까지 판정할 수 있다.
확인: 검색한 매뉴얼 판독 기록은 초기화를 어느 반복 위치에 두어야 하는지 지정하지 않는다.
미확인: 작성자는 이 값 재사용의 실제 수치 영향을 확인하지 않았다.

### 5.4 비정수압 보고서의 문서 내부 모순

확인: `_staging/recovery/read/XBeach/manuals/reports/non-hydrostatic_report_draft.pdf/p001-018.md:26`의 PDF 13쪽은 바닥을 `z=-d(\mathbf{x},t)`로 정의한다.
확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/initialize.F90:1012`의 `s%hh=max(s%zs-s%zb,par%eps)`는 코드의 전체 수심 정의다.
해석: 같은 기준면의 젖은 점에서 `zs=\eta`, `zb=-d`, `H=\eta+d`로 대응한다.
확인: 코드 대조는 `nonh.F90:233–243`의 단일층 분기에 한정한다.
확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/nonh.F90:1192`의 `if (nonhU(i,j)==1) then`는 u 압력 계수의 활성 조건이다.
확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/nonh.F90:1212`의 `if (s%ny>2) then`와 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/nonh.F90:1215`의 `if (nonhV(i,j)==1)then`는 아래 v 압력 계수의 조건이다.

**y 이류항: 1075·1077행.**

해석: 평탄한 수면과 바닥 사이에서 `u=U(y)`, `v=V_0`, `w=0`인 연직 균일 속도를 대입한다.
해석: 이 조건에서 보고서 PDF 16쪽 식 (1.13)의 적분 좌변은 `H V_0\partial_y U`다.
해석: 인쇄된 우변은 `-H V_0\partial_y U`다.
해석: `V_0\partial_y U`가 0이 아니면 두 변은 같지 않다.
해석: 이 반례는 식 (1.13)의 y 이류항 앞 음수 부호를 배제한다.
해석: 식 (1.17)의 양수 부호는 같은 조건의 적분과 일치한다.
확인: 코드의 y 이류 계산은 `flow_timestep.F90:212–241`에 있다.
확인: 코드의 잔차 조립과 갱신은 같은 파일 564–576행에 있다.
해석: 잔차의 `+vdudy`와 시간 갱신의 잔차 차감은 식 (1.17)의 좌변 양수 부호에 대응한다.

**동압 바닥 경사: 1079행.**

확인: `_staging/recovery/read/XBeach/manuals/reports/non-hydrostatic_report_draft.pdf/p001-018.md:29`의 PDF 16쪽 식 (1.14)은 수면 동압을 0으로 둔다.
해석: 아래 식은 식 (1.14)의 압력 부분에 바닥 정의를 대입한 결과다.

\[
I_p=\partial_x(H\bar p)-[p\,\partial_x z]_{-d}^{\eta}
=\partial_x(H\bar p)-p_b\partial_x d.
\]

해석: 운동량식 우변의 압력 힘은 `-I_p`다.
해석: 그 힘의 바닥 경사 항은 `+p_b\partial_x d`다.
해석: 따라서 식 (1.17) 우변의 음수 부호는 같은 문서의 식 (1.14)와 모순된다.
해석: 같은 쪽 식 (1.18)의 y 방향 음수 부호에도 같은 대입 결과가 적용된다.

확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/nonh.F90:1193`의 `vol       = 0.5_rKind*par%dt/(s%hum(i,j)*dxu(i))`는 u 방향 계수의 배율이다.
확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/nonh.F90:1235`의 `if (par%secorder == 1) then` 아래에서 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/nonh.F90:1238`의 `s%uu(i,j) = s%uu(i,j) + au(1,i,j) * s%pres(i+1,j) + au(0,i,j) * s%pres(i  ,j)`를 실행한다.
해석: 이 갱신의 압력 부분은 다음과 같다.

\[
\delta U_p=-\frac{\Delta t}{2\,\mathrm{hum}_{i,j}\,\mathrm{dxu}_i}
\left[(\eta_{i+1,j}+d_{i,j})p_{i+1,j}-(\eta_{i,j}+d_{i+1,j})p_{i,j}\right].
\]

해석: 이 식의 압력 부호는 `-I_p/H`의 바닥 경사 기여와 일치한다.
해석: 이 대조는 압력 부호에 한정한다.

**깊이 괄호와 V 압력항: 1080행.**

확인: `_staging/recovery/read/XBeach/manuals/reports/non-hydrostatic_report_draft.pdf/p019-036.md:22`의 PDF 25쪽 본문은 `\bar p^{n+\frac12}_{i+1,j} = \frac12 p^{n+\frac12}_{i+1,j}`를 적는다.
해석: `\eta=0`, `d=D>0`, `p=P\ne0`를 모든 점에 일정하게 대입한다.
해석: 이때 `H=D`이고 `\bar p=P/2`다.
해석: 식 (2.15)의 첫 표현은 수심평균 압력차와 바닥 경사가 모두 0이므로 0이다.
해석: 같은 식의 마지막 표현은 `(DP-(-D)P)/(2\Delta x)=DP/\Delta x`다.
해석: 코드의 두 `+d` 괄호는 `(DP-DP)/(2\Delta x)=0`을 준다.
해석: 따라서 둘째 괄호의 `-d`는 표기만 다른 동등한 계산이 아니다.
해석: 식 (2.18)과 식 (2.19)의 동일한 괄호도 일정한 `\Delta p`를 넣으면 같은 모순을 보인다.

확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/nonh.F90:1216`의 `vol       = 0.5_rKind*par%dt/(s%hvm(i,j)*dyv(j))`는 v 방향 거리로 `dyv(j)`를 쓴다.
확인: `_staging/recovery/read/XBeach/manuals/reports/non-hydrostatic_report_draft.pdf/p019-036.md:23`의 PDF 26쪽 식 (2.19)은 V 압력항의 분모를 `2\bar H^{n+1}_{i,j+\frac12}\Delta x`로 인쇄한다.
해석: 같은 식의 U 압력항에서 `x`와 `y`, `i`와 `j`를 교환하면 V 압력항의 분모는 `\Delta y`를 가져야 한다.
해석: V식에 남은 `\Delta x`도 코드와 다른 문서 오기다.
확인: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/nonh.F90:697`의 `s%uu(i,j) = aur(i,j) + au(1,i,j)*dp(i+1,j)+au(0,i,j)*dp(i,j)`와 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/nonh.F90:709`의 `s%vv(i,j) = avr(i,j) + av(1,i,j)*dp(i,j+1)+av(0,i,j)*dp(i,j)`는 압력 보정에도 같은 계수를 사용한다.
해석: 이 판정은 비정수압 보고서 자체의 모순에 근거한다.
미확인: 작성자는 인쇄 오류의 편집 원인이나 저자의 수정 의도를 확인하지 않았다.
확인: 작성자는 모델을 실행하거나 컴파일하지 않았다.

대상 9행, A 0, B 5, C 2, D 0, E 2, F 0, G 0

G 재판정: 대상 1행 중 A–F로 바꾼 1행, G 유지 0행
