# SFINCS 외부 원문 대조 결과

작성일은 2026-10-12이다.
대상은 [external-needed-sf.md](external-needed-sf.md)의 12행과 [SFINCS-docs-vs-code.md](SFINCS-docs-vs-code.md) §5의 B042 1행이다.
GitHub 소스는 `git clone --bare --filter=blob:none https://github.com/Deltares/SFINCS.git`로 받은 저장소와 `raw.githubusercontent.com/Deltares/SFINCS/<태그>/source/src/<파일>` 주소에서 읽었다.
로컬 코드 `models/SFINCS/raw/source_code/sfincs/source/src/`의 아래 파일은 `v2.4.0_Galibier_release` 태그의 같은 파일과 `cmp`로 바이트 단위로 같다. 확인한 파일은 sfincs_wavemaker.f90, sfincs_domain.f90, sfincs_boundaries.f90, sfincs_meteo.f90, sfincs_input.f90, sfincs_structures.f90, sfincs_subgrid.F90, sfincs_momentum.f90, sfincs_ncoutput.F90, snapwave/snapwave_solver.f90, snapwave/snapwave_domain.f90이다.
따라서 로컬 코드의 줄번호는 v2.4.0 태그의 줄번호와 같다.
SFINCS 코드는 한 번도 실행하지 않았다. QGIS도 실행하지 않았다.

태그 날짜는 `git log -1`로 센 값이다.

- v2.0.0 = 336abcd, 2022-11-11
- v2.0.2_Blockhaus_release = 640289f, 2023-06-09
- v2.2.0_col_dEze_release = b7a03d1, 2025-04-18
- v2.3.0_mt_Faber_release = e829fd2, 2025-11-18
- v2.4.0_Galibier_release = 1f1d828, 2026-06-15

문서 `docs/developments.rst:283` 근처의 링크 `releases/tag/v2.0.2`는 GitHub 태그 목록(`api.github.com/repos/Deltares/SFINCS/tags`)에 없다. 실제 태그 이름은 `v2.0.2_Blockhaus_release`이다. `raw.githubusercontent.com/.../v2.0.2/...`은 HTTP 404를 돌려주었다.

## 요약

| 행 ID | 결론 | 한 줄 |
| --- | --- | --- |
| B024 | A | 학위논문 식 (3.5)·(3.12)와 현재 코드의 기본 골격은 같다. 평활 θ 기본값, 2차원 마찰, 이류 식은 다르다. |
| B042 | H | 코드가 쓰는 UGRID 속성은 MDAL이 읽는 속성과 겹친다. QGIS 표시는 코드 비교 항목이 아니다. 실행은 하지 않았다. |
| B048 | A | v2.3.0은 `sin(pi - phi)`, v2.4.0은 `-sin(phi)`를 쓴다. |
| B049 | A | v2.3.0은 `do nm = 1, np`, v2.4.0은 `do ip = 1, npuv`를 쓴다. |
| B050 | A | v2.4.0에서 msk=6 셀에 msk=1 이웃이 없으면 셀을 비활성으로 되돌리는 분기가 새로 생겼다. |
| B051 | A | v2.3.0은 방향 bin별 `eeprev_ig`를 쓰고, v2.4.0은 총 에너지 `Eprev_ig`와 `/E*ee` 재분배를 쓴다. 이 수정이 Elmessary 제안과 연결됨은 PR 설명과 릴리스 커밋 메시지로 확인했다. |
| B067 | A | v2.2.0은 `dyrinvc = 1.0*(3*dyrm/2)`와 `dxuvinv = dyrinv`를 쓴다. v2.3.0은 투영 좌표 분기만 `1.0/(...)`로 고치고 V 점에서 `dyrinvc`를 쓴다. 지리 좌표 분기는 v2.4.0에서 고쳤다. |
| B068 | A | v2.2.0은 `2*(spw_radius - dstspw)/spw_radius`, v2.3.0은 `1/(1 - min(spw_merge_frac, 0.999))` 계수를 쓴다. |
| B069 | A | v2.2.0은 깊이 조건으로 `inner`를 .false.로 바꾸고, v2.3.0은 그 조건을 주석 처리했다. |
| B070 | A·F | 에너지 수지 구조는 같다. Baldock 계수는 preprint 0.25, 코드 0.28이다. preprint 식 B의 `c_θ/Δθ` 항은 코드에 없다. |
| B080 | 일치 (F) | 코드가 논문 식 (12), (17)–(19), (22)–(25)와 같은 구조를 쓴다. 차이는 부등호 `>` 대 `≥`뿐이다. |
| B103 | A | v2.0.0은 속도 대신 유량 `qx0` 차분을 쓰고, v2.0.2는 `(uu_nm - uu_ndm)` 속도 차분과 유량 합 `qvt`의 부호를 쓴다. |
| B110 | A | v2.0.0은 `h1>0 .and. h2>0`일 때 `Cd*cweir*h1*sqrt(...)`, v2.0.2는 `h2 > 2/3*h1`일 때 `Cd*h2*sqrt(2*9.81*...)`를 쓴다. |

---

## B024 Leijnse (2018)에 기초

- **행 ID**: B024
- **외부 원문**: Leijnse, T. (2018). *Computationally Efficient Modelling of Compound Flooding due to Tropical Cyclones with the Explicit Inclusion of Wave-Driven Processes*. TU Delft 석사학위논문, 2018-06-29. 서지 페이지 `https://repository.tudelft.nl/record/uuid:53037d4d-d7a9-4f71-9b22-8c329f2b384c`는 HTTP 200이었다. 연결 PDF `https://repository.tudelft.nl/file/File_da13d247-495e-4556-9211-abb18ee7232d`는 HTTP 200, `application/pdf`, 54,621,765바이트였다. PDF는 145쪽이다. 식 (3.5)와 (3.6)은 PDF 34쪽(인쇄 쪽번호 18)에 있고, 식 (3.12)는 PDF 35쪽(인쇄 쪽번호 19)에 있다. 3.2.3절은 PDF 33쪽(인쇄 쪽번호 17)에서 시작한다.
- **원문 인용(exact)**:
  - §3.1: `The model is developed by Maarten van Ormondt and based on the LFP model as described in Bates et al. (2010).`
  - §3.2.3: `The descritisation of the momentum equations has some additional smoothing with respect to Bates et al. (2010), using a Lax-scheme to improve stability of the numerical solution. The state is smoothed by using a weighted average of the flux at the previous time level and the average of the fluxes in the adjacent cells also at that time level, controlled by a factor θ (default: θ = 0.9).`
  - 식 (3.5)의 분자: `θ · q_x^{t-Δt} + (1 − θ) · [(q_x,m+3/2 + q_x,m-1/2)/2] − Δt · g · h_x · (ζ_{m+1,n} − ζ_{m,n})/Δx + τ_x · Δt − adv_x · Δt` (식은 pdftotext 출력에서 재구성했으며 기호 배치는 PDF 34쪽 레이아웃을 따른다).
  - 식 (3.5)의 분모: `1 + Δt · g · n² · |q_x^{t-Δt}| / (h_x^{t-Δt})^{7/3}`.
  - 식 (3.12): `ζ^t_{m,n} = ζ^{t-Δt}_{m,n} − Δt [ (q_x,m+1/2 − q_x,m-1/2)/Δx + (q_y,n+1/2 − q_y,n-1/2)/Δy ]`.
  - §3.2.4: `The 1D advection term is included using the Upwind scheme` (식 3.8, 3.9). `the 2D advection term can be added using the Central Difference scheme` (식 3.10).
- **문서·코드와 비교**:
  - 문서 `docs/numerical_implementation.rst:7`은 `Based on Leijnse (2018)` 한 구절만 적는다.
  - 마찰 분모는 같다. 코드 `sfincs_momentum.f90:677`은 `q(ip) = (qsm + frc * dt) / (1.0 + gnavg2 * dt * qfr / hu73)`이고, 식 (3.5)의 분모와 같은 구조이다. `gnavg2`는 g·n²이다.
  - 연속식은 같다. 코드 `sfincs_continuity.f90:151`은 `(q(nmd) - q(nmu)) * dxrinv + (q(ndm) - q(num)) * dyrinv`를 `zs`에 더하고, 식 (3.12)와 부호·구조가 같다.
  - θ 평활은 다르다. 논문 기본값은 θ = 0.9이고 평활을 항상 쓴다. 코드 `sfincs_input.f90:71`은 `theta` 기본값을 1.0으로 두고, `sfincs_input.f90:616–618`은 `theta<0.9999`일 때만 `thetasmoothing`을 켠다. 코드 `sfincs_momentum.f90:644–648`은 이웃 두 점이 모두 `kcuv==1`이고 `abs(q) > 1.0e-6`일 때만 평활한다. 논문은 이 조건을 적지 않았다.
  - 마찰 유량은 다르다. 논문은 `|q_x|`만 쓴다. 코드 `sfincs_input.f90:186`은 `friction2d` 기본값을 `.true.`로 두고, `sfincs_momentum.f90:624`는 `qfr = sqrt(qx_nm**2 + (hu * vu)**2)`를 쓴다. `sfincs_momentum.f90:628–630`의 주석은 `|q_x|`만 쓰는 방식을 `original Bates et al. (2010)`이라 부른다.
  - 이류 식은 다르다. 논문 식 (3.8)–(3.10)과 v2.0.2 이후 코드(B103 참조)의 차분 형태가 다르다.
- **결론**: A
- **노트에 쓸 결론 문장**: Leijnse (2018) 식 (3.5)·(3.12)의 마찰 분모와 연속식은 현재 코드와 같은 구조이지만, 논문의 θ 기본값 0.9와 항상 켜지는 평활, 1차원 마찰 유량은 현재 코드의 θ 기본값 1.0, 조건부 평활, 기본 2차원 마찰과 다르다.

## B042 quadtree NetCDF를 QGIS에서 표시

- **행 ID**: B042
- **외부 원문**:
  - MDAL 문서 `https://raw.githubusercontent.com/lutraconsulting/MDAL/master/docs/source/drivers/ugrid.rst`.
  - MDAL 소스 `https://raw.githubusercontent.com/lutraconsulting/MDAL/master/mdal/frmts/mdal_ugrid.cpp`와 `.../mdal_cf.cpp`. 2026-10-12에 받은 master 판이다. 줄번호는 그 판을 센 값이다.
  - SFINCS 릴리스 노트 `https://api.github.com/repos/Deltares/SFINCS/releases/tags/v2.4.0_Galibier_release`와 PR #335 `https://github.com/Deltares/SFINCS/pull/335`. PR #335 설명은 `https://api.github.com/repos/Deltares/SFINCS/issues/335`로 받았다.
- **원문 인용(exact)**:
  - `ugrid.rst`: `MDAL supports reading of unstructured grid (mesh) data from NetCDF files based on UGRID_ format.`
  - `mdal_ugrid.cpp:41`: `bool isMeshTopology = mNcFile->getAttrStr( var, "cf_role" ) == "mesh_topology";`
  - `mdal_ugrid.cpp:137`: `mMeshDimension = mNcFile->getAttrInt( mMeshName, "topology_dimension" );`
  - `mdal_ugrid.cpp:148`: `parse2VariablesFromAttribute( mMeshName, "node_coordinates", nodeXVariable, nodeYVariable, false );`
  - `mdal_ugrid.cpp:203`: `std::string faceDimensionLocation = mNcFile->getAttrStr( mMeshName, "face_dimension" );`
  - `mdal_ugrid.cpp:350`: `const std::string mesh2dFaceNodeConnectivity = mNcFile->getAttrStr( mMeshName, "face_node_connectivity" );`
  - `mdal_ugrid.cpp:354–356`: `if ( mNcFile->hasAttrInt( mesh2dFaceNodeConnectivity, "_FillValue" ) )` / `fillVal = ...` / `int startIndex = mNcFile->getAttrInt( mesh2dFaceNodeConnectivity, "start_index" );`
  - `mdal_ugrid.cpp:400`: `coordinateSystemVariable = mNcFile->getAttrStr( nodeVariablesName[0], "grid_mapping" );`
  - `mdal_ugrid.cpp:496`: `parse2VariablesFromAttribute( mesh, "face_coordinates", xName, yName, true );`
  - `mdal_ugrid.cpp:644`: `else if ( MDAL::contains( longName, "direction" ) )`
  - `mdal_cf.cpp:512–515`: `std::string epsg_code = mNcFile->getAttrStr( coordinate_system_variable, "EPSG_code" );` … `int epsg = mNcFile->getAttrInt( coordinate_system_variable, "epsg" );`
  - 릴리스 노트(v2.4.0): `with some extra info on the epsg_code, renaming of variables and long_names, qgis can immediatly read the mesh2d output! (#345)`는 릴리스 커밋 1f1d828의 메시지 줄이다. 릴리스 본문의 문장은 `Quadtree netcdf output sfincs_map.nc files can now directly be loaded and visuallised in QGIS.`이다.
  - PR #335 설명: `MDAL (the QGIS mesh provider) silently rejects an entire mesh when any variable has the word "direction" or "directional" in its long_name` 그리고 `Tested on QGIS 3.40.10 / MDAL (provider_mdal.dll) — quadtree output loads immediately as a UGRID mesh layer with all datasets visible.`
- **문서·코드와 비교**:
  - 코드 `sfincs_ncoutput.F90:979–987`은 `mesh2d` 변수에 `cf_role=mesh_topology`, `topology_dimension=2`, `node_coordinates`, `face_coordinates`, `node_dimension`, `max_face_nodes_dimension`, `face_node_connectivity`, `face_dimension`을 쓴다.
  - 코드 `sfincs_ncoutput.F90:1033–1038`은 `mesh2d_face_nodes`에 `cf_role=face_node_connectivity`, `start_index=1`, `_FillValue=-999`를 쓴다.
  - 코드 `sfincs_ncoutput.F90:998`과 `:1007`은 노드 좌표에 `grid_mapping='crs'`를 쓴다. `:1085`는 `crs` 변수에 정수 `epsg`를 쓴다. `:181`·`:1086` 근처는 소문자 `epsg_code`를 쓴다. MDAL은 대문자 `EPSG_code`를 읽고, 비어 있으면 정수 `epsg`로 대체한다(`mdal_cf.cpp:512–515`).
  - 코드 `sfincs_ncoutput.F90:1044` 이후는 `mesh2d_face_x`, `mesh2d_face_y`를 쓴다.
  - 코드의 map 파일 구간(1–1500행 부근)에는 `long_name`에 `direction`이 들어간 줄이 없다. `grep -n -i direction`에 걸린 map 구간 줄은 `standard_name`뿐이다(633, 1432, 1448행). `long_name`에 `direction`이 들어간 줄은 his 파일 구간(1968, 1975, 1989, 2062, 2069, 2091, 2098행)에 있다.
  - 이 비교는 정적 판독이다. QGIS를 실행하지 않았다. MDAL이 `direction` 때문에 메시를 거부한다는 말은 PR #335 설명에서 인용했고 직접 재현하지 않았다.
  - 문서 문장은 도구 호환성 주장이다. 코드가 문서의 수치·식·절차와 일치하는지 묻는 항목이 아니다.
- **결론**: H
- **노트에 쓸 결론 문장**: 이 주장은 코드 대조 항목이 아니라 도구 호환성 주장이며, 코드가 쓰는 UGRID 속성(`cf_role`, `topology_dimension`, `node_coordinates`, `face_coordinates`, `face_node_connectivity`, `start_index`, `grid_mapping`, `epsg`)은 MDAL 소스가 읽는 속성과 겹치지만 QGIS 표시는 실행해 확인하지 않았다.

## B048 북쪽에서 파를 가하는 wavemaker 버그

- **행 ID**: B048 (`docs/developments.rst:64`, v2.4.0 절 안)
- **외부 원문**: `https://raw.githubusercontent.com/Deltares/SFINCS/v2.3.0_mt_Faber_release/source/src/sfincs_wavemaker.f90`와 `.../v2.4.0_Galibier_release/source/src/sfincs_wavemaker.f90`. 변경 커밋은 `dce1e52`(2026-04-15, Tim Leijnse)와 릴리스 커밋 `1f1d828`이다. 문서는 이 항목을 v2.4.0 절에 두었다(`docs/developments.rst` 30–37행 근처).
- **원문 인용(exact)**:
  - v2.3.0 `sfincs_wavemaker.f90:1007` 외 3곳(1029, 1096, 1118): `wavemaker_angfac(iwm)    = max(sin(pi - phi(ip)), 0.0)`
  - v2.4.0 `sfincs_wavemaker.f90:1032, 1056, 1129, 1153`: `wavemaker_angfac(iwm)    = max(-sin(phi(ip)), 0.0)`
  - v2.3.0 `sfincs_wavemaker.f90:304`: `iz = uv_index_z_nm(ip)`
  - v2.4.0 `sfincs_wavemaker.f90:307`: `iz = uv_index_z_nm(nmu)`
  - 커밋 `dce1e52` 메시지: `In the lower-left directional quadrant, iz was being looked up with the source cell index ip instead of the neighbor index nmu, causing the indwm(iz)==0 guard to inspect the wrong cell.`
  - 릴리스 커밋 `1f1d828` 메시지: `"Below" direction angfac (Q3 nd1/nd2, Q4 nd1/nd2): sin(π − φ) ≡ sin(φ) and sin(φ) ≤ 0 for φ ∈ [π, 2π), so max(sin(π − φ), 0) always returned zero, silencing all south-pointing wavemaker UV faces. Fixed to max(−sin(φ), 0).`
- **문서·코드와 비교**:
  - 문서의 `waves forced from the north`는 v2.4.0 릴리스 커밋 메시지에서 `south-facing wavemakers`, `phi in the south half-plane (Q3/Q4)`로 나타난다. 두 표현이 같은 사건을 가리키는지는 커밋 메시지가 직접 연결하지 않는다. 둘 다 phi가 π~2π인 범위(Q3·Q4)의 wavemaker이다.
  - 로컬 코드 `sfincs_wavemaker.f90:1032, 1056, 1129, 1153`은 `-sin(phi(ip))`이고 v2.4.0과 같다.
  - 인용된 코드 줄 `sfincs_wavemaker.f90:108–109`, `1734–1737`은 v2.3.0 대 v2.4.0 차이에 들어 있지 않다. `phip` 계산(`atan2 + 0.5*pi`, `- rotation`)은 두 태그에서 같다(두 태그의 diff는 공백 차이뿐이다).
- **결론**: A
- **노트에 쓸 결론 문장**: v2.4.0은 wavemaker 아래쪽 면의 각도 계수 `angfac`를 `max(sin(pi - phi), 0)`에서 `max(-sin(phi), 0)`로 바꾸어 phi가 π~2π인 wavemaker 면이 항상 0이 되던 문제를 고쳤고, 현재 로컬 코드는 이 수정판이다.

## B049 정규격자 binary sbgfile 버그

- **행 ID**: B049 (`docs/developments.rst:65`)
- **외부 원문**: `https://raw.githubusercontent.com/Deltares/SFINCS/v2.3.0_mt_Faber_release/source/src/sfincs_subgrid.F90`와 `.../v2.4.0_Galibier_release/source/src/sfincs_subgrid.F90`. 변경 커밋은 `96b5014`(2026-04-15, 메시지 `- Bugfix in old binary sbgfile for regular grid (legacy code)`)이다.
- **원문 인용(exact)**:
  - v2.3.0 `sfincs_subgrid.F90:789–790`: `do nm = 1, np` / `subgrid_uv_nrep(1, nm) = subgrid_uv_nrep(2, nm)`
  - v2.3.0 `sfincs_subgrid.F90:862–863`, `866–867`도 같은 두 줄이다.
  - v2.4.0 `sfincs_subgrid.F90:789–790`: `do ip = 1, npuv` / `subgrid_uv_nrep(1, ip) = subgrid_uv_nrep(2, ip)`
  - v2.4.0 `sfincs_subgrid.F90:862–863`, `866–867`도 같은 두 줄이다.
- **문서·코드와 비교**:
  - `subgrid_uv_nrep`는 uv 점 배열이다. v2.3.0의 반복은 셀 수 `np`까지 돈다. v2.4.0의 반복은 uv 점 수 `npuv`까지 돈다. 이 차이가 이 파일의 두 판 사이 diff 전부이다(`diff -w`로 센 변경 구간 3곳).
  - 코드가 인용한 `sfincs_subgrid.F90:499–500`, `672–698`(level 수 +1, `pwet = 1.0`)은 두 태그에서 같다.
  - 문서 `docs/developments.rst:65`의 `Fixed bug in old binary sbgfile for regular grid`는 위 반복 범위 수정과 맞는다. 다만 소스 diff만으로 이 수정이 `np`와 `npuv`의 대소 차이 때문에 생긴 어떤 증상을 고쳤는지는 확인하지 않았다.
- **결론**: A
- **노트에 쓸 결론 문장**: v2.4.0은 정규격자 구형 binary subgrid 파일 리더에서 `subgrid_uv_nrep(1, :)` 채움 반복을 셀 수 `np`에서 uv 점 수 `npuv`로 바꾸었고, 현재 로컬 코드는 이 수정판이다.

## B050 Neumann 경계(msk=6) 버그

- **행 ID**: B050 (`docs/developments.rst:66`)
- **외부 원문**: `https://raw.githubusercontent.com/Deltares/SFINCS/v2.3.0_mt_Faber_release/source/src/sfincs_boundaries.f90`와 `.../v2.4.0_Galibier_release/source/src/sfincs_boundaries.f90`. 변경 커밋은 `6dea570`(2026-04-03, 메시지 `311 bugfix neumann6 for sfincs for specific cases (#312)`)이다.
- **원문 인용(exact)**:
  - v2.3.0 `sfincs_boundaries.f90:633, 638, 643, 648`: `if (kcs(nmi) == 1) nmi_gbp(ib) = nmi`
  - v2.4.0 `sfincs_boundaries.f90:661–668`: `if (nmi_gbp(ib) == 0) then` / `! No active msk=1 point found in any of the neighbours, reset cell to inactive` / `kcs(nm) = 0` / `write(logstr,*)'Warning : Found a Neumann cell (msk=6) that does not have any valid neighbouring regular cell (msk=1)!'`
- **문서·코드와 비교**:
  - v2.3.0은 msk=6 셀에서 msk=1 이웃을 찾지 못해도 `nmi_gbp(ib)`를 그대로 두고 지나간다. v2.4.0은 이 경우 `kcs(nm) = 0`으로 셀을 비활성으로 되돌리고 로그를 쓴다.
  - 문서가 말한 `specific cases`는 이 `msk=1` 이웃이 없는 경우로 확인했다. 커밋 메시지는 이 이상을 설명하지 않는다.
  - 인용한 `sfincs_domain.f90:1871–1875`(`kcuv(ip) = 6`), `sfincs_boundaries.f90:903–913, 958`, `sfincs_momentum.f90:159`는 두 태그의 diff에 들어 있지 않다. 이 줄들은 v2.3.0과 v2.4.0에서 같다.
- **결론**: A
- **노트에 쓸 결론 문장**: v2.4.0은 Neumann 경계 셀(msk=6)에 활성 이웃(msk=1)이 하나도 없으면 그 셀을 비활성(`kcs = 0`)으로 되돌리고 경고를 쓰도록 `sfincs_boundaries.f90`을 고쳤고, v2.3.0에는 이 분기가 없다.

## B051 SnapWave IG 생성항 버그

- **행 ID**: B051 (`docs/developments.rst:67`)
- **외부 원문**: `https://raw.githubusercontent.com/Deltares/SFINCS/v2.3.0_mt_Faber_release/source/src/snapwave/snapwave_solver.f90`와 `.../v2.4.0_Galibier_release/source/src/snapwave/snapwave_solver.f90`. PR #283 `https://github.com/Deltares/SFINCS/pull/283`(`https://api.github.com/repos/Deltares/SFINCS/issues/283`로 받음). 릴리스 커밋 `1f1d828`의 메시지.
- **원문 인용(exact)**:
  - v2.3.0 `snapwave_solver.f90:1142`: `srcig_local(itheta, k) = alphaigfac * alphaig_local(itheta,k) * sqrt(eeprev_ig(itheta)) * cgprev(itheta) / depthprev(itheta,k) * dSxx / ds(itheta, k)`
  - v2.4.0 `snapwave_solver.f90:1399`: `srcig_local(itheta, k) = alphaigfac * alphaig_local(itheta,k) * sqrt(Eprev_ig(itheta)) * cgprev(itheta) / depthprev(itheta,k) * dSxx / ds(itheta, k) /max(E_local(k), 1.0e-6) * ee(itheta,k)`
  - v2.4.0 `snapwave_solver.f90:1396–1398` 주석: `Base on E_prev_ig instead of eeprev_ig(itheta) > no bins but total energy` / `NOTE - already here multiplied with ee(itheta,k), for direct inclusion in 'R'-term`
  - PR #283 제목과 설명: `Add option where IG source term uses mean wave energy Eprev_ig in s…` / `…ource term calculation instead of bin dependent eeprev_ig, thanks to suggestion of Yasmine - results look promising`. PR 상태는 `open`이다.
  - 릴리스 커밋 `1f1d828` 메시지: `Already do the bugfix of PR #283 by switching to srcig based on E and redistribute by /E * ee`
- **문서·코드와 비교**:
  - 외부 문서에 `Elmessary`라는 이름은 커밋 메시지·PR 제목·이슈 검색(`api.github.com/search/issues?q=repo:Deltares/SFINCS+Elmessary`, 결과 0건)에서 나오지 않는다. PR #283 설명의 `Yasmine`이 같은 사람인지는 확인하지 못했다.
  - 두 판의 생성항은 방향 bin별 에너지 `eeprev_ig(itheta)`에서 총 에너지 `Eprev_ig(itheta)`로 바뀌었고, 결과에 `/max(E_local(k), 1.0e-6) * ee(itheta,k)`가 붙었다. 이 곱은 방향 분배를 맡는다.
  - 외부 작업의 가정(`k1·k2` 검사 조건의 주석을 곱 조건 교체와 연결)은 틀렸다. `if (k1>0 .and. k2>0) then ! IMPORTANT - for some reason (k1*k2)>0 is not reliable always` 줄은 v2.2.0(`snapwave_solver.f90:1062`)과 v2.3.0(`:1077`)에 이미 있다. v2.4.0에서 같은 줄은 `:1330`이다. 이 조건은 이번 수정과 무관하다.
  - 소스 diff는 위 식 변경을 보여 준다. 이 변경이 문서가 말한 버그를 고쳤는지의 수치 검증은 하지 않았다.
- **결론**: A
- **노트에 쓸 결론 문장**: v2.4.0의 SnapWave IG 생성항은 방향 bin별 에너지 `eeprev_ig` 대신 총 에너지 `Eprev_ig`에 기초하고 `/E * ee`로 방향에 재분배하며, 릴리스 커밋 메시지가 이 변경을 PR #283의 수정으로 적는다.

## B067 quadtree `dyrinvc` 정의·사용 버그

- **행 ID**: B067 (`docs/developments.rst:122`, v2.3.0 절 안)
- **외부 원문**: `https://raw.githubusercontent.com/Deltares/SFINCS/<태그>/source/src/sfincs_domain.f90`와 `.../sfincs_momentum.f90`. 태그는 `v2.2.0_col_dEze_release`, `v2.3.0_mt_Faber_release`, `v2.4.0_Galibier_release`이다. 변경 커밋은 `e5f94e0`(2025-11-10, `243 last fixes for release (#244)`)이고, 지리 좌표 분기 정리는 `44a38cc`(2026-03-19)이다.
- **원문 인용(exact)**:
  - v2.2.0 `sfincs_domain.f90:1417`(`crsgeo` 분기)와 `:1480`(투영 분기): `dyrinvc(iref) = 1.0*(3*dyrm(iref)/2)`
  - v2.3.0 `sfincs_domain.f90:1431`(`crsgeo` 분기): `dyrinvc(iref) = 1.0*(3*dyrm(iref)/2)`
  - v2.3.0 `sfincs_domain.f90:1494`(투영 분기): `dyrinvc(iref) = 1.0/(3*dyrm(iref)/2)`
  - v2.4.0 `sfincs_domain.f90:1446`(`crsgeo` 분기)와 `:1509`(투영 분기): `dyrinvc(iref) = 1.0 / (3 * dyrm(iref) / 2)`
  - v2.2.0 `sfincs_momentum.f90:280`(V 점, 정밀화 경계): `dxuvinv  = dyrinv(iref)`
  - v2.3.0 `sfincs_momentum.f90:280`: `dxuvinv  = dyrinvc(iref)`
- **문서·코드와 비교**:
  - v2.2.0의 `dyrinvc`는 두 분기 모두 역수가 아니라 `1.0*(3*dyrm/2)`로 정의되어 있었고, V 점은 `dyrinvc` 대신 `dyrinv`를 썼다.
  - v2.3.0은 투영 분기 정의와 V 점의 사용을 고쳤다. 지리 좌표(`crsgeo`) 분기 정의 `:1431`은 v2.3.0에서 고치지 않았다. 이 분기는 v2.4.0에서 고쳤다. 따라서 문서의 `quadtree variable dyrinvc use and definition` 수정은 v2.3.0에서 일부(투영 분기와 사용)만 닫혔다.
  - 현재 로컬 코드는 `sfincs_domain.f90:1446, 1509`와 `sfincs_momentum.f90:302`에서 v2.4.0과 같다. 외부 문서 목록이 인용한 `sfincs_domain.f90:1508–1509`의 `dxrinvc`·`dyrinvc` 식(`1.0 / (3 * dxrm(iref) / 2)`)은 이 수정 뒤의 투영 분기 식이다.
- **결론**: A
- **노트에 쓸 결론 문장**: v2.2.0의 `dyrinvc`는 역수가 아닌 `1.0*(3*dyrm/2)`였고 V 점에서 쓰이지도 않았으며, v2.3.0은 투영 좌표 분기와 사용을 고쳤고 지리 좌표 분기는 v2.4.0에서 고쳤다.

## B068 `spwmergefrac` 병합 버그

- **행 ID**: B068 (`docs/developments.rst:123`)
- **외부 원문**: `https://raw.githubusercontent.com/Deltares/SFINCS/v2.2.0_col_dEze_release/source/src/sfincs_meteo.f90`와 `.../v2.3.0_mt_Faber_release/source/src/sfincs_meteo.f90`. 변경 커밋은 `0c7d4f7`(2025-06-23, `fixed bug when spw_merge_frac is different from default 0.5 (#186)`)이다.
- **원문 인용(exact)**:
  - v2.2.0 `sfincs_meteo.f90:510–511`: `if (dstspw>spw_merge_frac*spw_radius) then` / `merge_frac = 2*(spw_radius - dstspw)/spw_radius`
  - v2.3.0 `sfincs_meteo.f90:668–669`: `if (dstspw > spw_merge_frac * spw_radius) then` / `merge_frac = (1.0 / (1.0 - min(spw_merge_frac, 0.999))) * (spw_radius - dstspw) / spw_radius`
  - 두 판 모두 `sfincs_input`에서 `call read_real_input(500,'spwmergefrac',spw_merge_frac,0.5)`(v2.2.0 `:104`, v2.3.0 `:108`).
- **문서·코드와 비교**:
  - v2.2.0의 기울기 계수는 상수 2이다. v2.3.0의 계수는 `1/(1 - min(spw_merge_frac, 0.999))`이다. `spwmergefrac = 0.5`(기본값)에서 v2.3.0 계수는 `1/(1 - 0.5) = 2`로 v2.2.0과 같다. 두 판은 기본값이 아닌 값에서만 다르다. 병합 시작 거리는 두 판 모두 `spw_merge_frac * spw_radius`이다.
  - 현재 로컬 코드 `sfincs_meteo.f90:701–702`는 v2.3.0과 같고(`0.999` 상한 포함), 로컬과 v2.4.0이 같다.
- **결론**: A
- **노트에 쓸 결론 문장**: v2.3.0은 spiderweb 병합 비율의 기울기 계수를 상수 2에서 `1/(1 - min(spw_merge_frac, 0.999))`로 바꾸었고 기본값 0.5에서는 계수가 2로 같고 다른 값에서만 두 판이 다르다.

## B069 SnapWave IG와 inner 셀 정의 버그

- **행 ID**: B069 (`docs/developments.rst:124`)
- **외부 원문**: `https://raw.githubusercontent.com/Deltares/SFINCS/v2.2.0_col_dEze_release/source/src/snapwave/snapwave_solver.f90`와 `.../v2.3.0_mt_Faber_release/source/src/snapwave/snapwave_solver.f90`. 변경 커밋은 `2c55d22`(2025-05-16, `That extra check on 'inner' is an issue in our case with changing w…`)와 `ed41f5d`(2025-11-18, `FIXED! the IG part still needed the (k1==1 .and. k2==1) > false for inner`)이다.
- **원문 인용(exact)**:
  - v2.2.0 `snapwave_solver.f90:412–416`: `if (k1*k2==0) then` / `inner(k)=.false.` / `elseif (depth(k1)<1.1*hmin .or. depth(k2)<1.1*hmin .or. (k1==1 .and. k2==1)) then` / `inner(k)=.false.` / `exit`
  - v2.3.0 `snapwave_solver.f90:415–428`: `if (k1 * k2 == 0) then` … `elseif ((k1==1 .and. k2==1)) then ! TL: for now still needed for a working IG solver` / `inner(k)=.false.` / `exit` 그리고 주석 처리된 `!elseif (depth(k1) < hmin .or. depth(k2) < hmin .or. (k1 == 1 .and. k2 == 1)) then` 앞에 `! Do not change inner here! It should be static! In a next update of the wave fields, these points may be wet.`
  - v2.4.0 `snapwave_solver.f90:508–516`: `if (k1 * k2 == 0) then` / `elseif (k1==1 .and. k2==1) then ! TL: for now still needed for a working IG solver`
- **문서·코드와 비교**:
  - v2.2.0은 `inner`를 해수면 아래의 깊이 조건(`depth < 1.1*hmin`)으로 .false.로 바꾸었다. v2.3.0은 그 깊이 조건을 주석 처리하고 `(k1==1 .and. k2==1)` 조건만 남겼다. 주석 이유는 `inner`를 정적으로 유지하기 위해서이다.
  - 인용한 `snapwave_domain.f90:342–345`(`msk(k)==1`이면 `inner = .true.`)는 두 판에서 같은 형태이다(v2.2.0 `:353–355`, v2.3.0 `:352–354`, v2.4.0 `:343–345`).
  - 문서의 `Fixed bug in use of SnapWave with IG balance in relation to definition of inner cells`는 이 수정과 맞는다. 커밋 `ed41f5d`의 메시지가 IG 쪽 필요를 직접 적는다.
- **결론**: A
- **노트에 쓸 결론 문장**: v2.3.0은 SnapWave에서 `inner`를 깊이 조건으로 바꾸던 분기를 주석 처리해 `inner`를 정적으로 유지하고, `(k1==1 .and. k2==1)`일 때만 .false.로 바꾸어 IG 수지가 쓰도록 했다.

## B070 SnapWave 통합 solver와 Roelvink et al. (2025) 일관성

- **행 ID**: B070 (`docs/developments.rst:130, 167`)
- **외부 원문**: Roelvink, D., van Ormondt, M., Reyns, J., and van der Lugt, M. (2025). *SnapWave: fast, implicit wave transformation from offshore to nearshore*. EGUsphere preprint, DOI 10.5194/egusphere-2025-492. PDF `https://egusphere.copernicus.org/preprints/2025/egusphere-2025-492/egusphere-2025-492.pdf`는 HTTP 200으로 받았다. `pdfinfo`는 40쪽이라 적었다. 식 (2.1)–(2.5)는 PDF 3쪽에 있고, 식 (2.6)–(2.7)과 계수 A, B, C, R은 PDF 3–4쪽에 있다. 쪽 이미지를 `pdftoppm -r 130`으로 렌더해 눈으로 확인했다. 독립 코드는 `https://github.com/danoroelvink/snapwave`이고 `src/snapwave_solver.f90`을 받았다.
- **원문 인용(exact)**:
  - 식 (2.2): `D_w = 0.25 α ρ g f_p exp(−H_max²/H_rms²)(H_max² + H_rms²) = 2α f_p exp(−E_max/E)(E_max + E)`
  - 식 (2.4): `dd = (D/E) ee`
  - 식 (2.6): `(ee^{n+1}_{k,iϑ} − ee^n_{k,iϑ})/Δt + (c_{g,k} ee^{n+1}_{k,iϑ} − c_{gu,iϑ} ee^{n+1}_{u,iϑ})/Δs_{k,iϑ} + (c_{ϑ,k,iϑ+1} ee^{n+1}_{k,iϑ+1} − c_{ϑ,k,iϑ−1} ee^{n+1}_{k,iϑ−1})/(2Δϑ) + (D_k/E_k) ee^{n+1}_{k,iϑ} = 0`
  - 계수(PDF 4쪽): `A = −c_{ϑ k,iϑ−1}/(2Δϑ)`, `B = 1/Δt + c_{gx,}/Δs_{k,iϑ} + c_{ϑ,k,iϑ}/Δϑ + D_k/E_k`, `C = c_{ϑ,k,iϑ+1}/(2Δϑ)`, `R = ee^n_{k,iϑ}/Δt + c_{gx,prev} ee^{n+1}_{prev}/Δs_{k,iϑ}`
  - 독립 코드 `snapwave_solver.f90:1070`: `Dw = 0.28 * alfa * rho * g / T * exp(-(Hmax / Hloc)**2) * (Hmax**2 + Hloc**2)`
  - v2.2.0 `snapwave_solver.f90:997–998`: `Dw=0.28*alfa*rho*g/T*exp(-(Hmax/Hloc)**2)*(Hmax**2+Hloc**2)` / `!Dw=0.25*alfa*rho*g/T*exp(-(Hmax/Hloc)**2)*(Hmax**2+Hloc**2) !Old`
- **문서·코드와 비교**:
  - 에너지 수지의 구조는 같다. 코드 `snapwave_solver.f90:778`은 `R(itheta) = oneoverdt * ee(itheta, k) + cgprev(itheta) * eeprev(itheta) / ds(itheta, k) - srcig_local * shinc2ig`이고, 식의 R에 IG 생성항이 붙은 형태이다. 코드 `:785`는 `A = -ctheta(itheta - 1, k) * oneover2dtheta`, `:787`은 `C = ctheta(itheta + 1, k) * oneover2dtheta`로 식의 A, C와 같다. 코드 `:799`는 `if (wind) R(:) = R(:) + WsorE(:, k)`로 preprint에 없는 바람 항을 더한다.
  - 계수 B는 다르다. 코드 `:786`은 `B = oneoverdt + cg(k) / ds(itheta, k) + DoverE(k)`이고 `c_ϑ/Δϑ` 항이 없다. preprint의 계수 B에는 `c_{ϑ,k,iϑ}/Δϑ`가 있다. 그러나 preprint의 식 (2.6)은 `iϑ`를 중심으로 하는 항 없이 `iϑ+1`과 `iϑ−1`의 중앙 차분만 쓴다. 따라서 preprint 식 (2.6)과 계수 B가 서로 맞지 않고, 코드는 식 (2.6)과 맞는다. 독립 코드는 경계 상류 분기(`snapwave_solver.f90:680, 684`)에서만 `ctheta(itheta,k) * oneoverdtheta` 항을 쓴다.
  - Baldock 계수는 다르다. preprint 식 (2.2)는 0.25이고, 독립 코드(`:1070`)와 SFINCS 코드(`snapwave_solver.f90:1200`, `0.28`)는 0.28이다. v2.2.0도 이미 0.28을 쓰고 0.25는 `!Old` 주석이다. 0.28이 preprint의 0.25를 대체한 값이다.
  - SFINCS 코드의 `* f` 인자(`snapwave_solver.f90:1192–1200`, `f = (Hloc/Hmax)**iexp`)는 preprint와 독립 코드(`:1070`)에 없다.
  - 문서가 가리키는 독립 코드의 당시 commit은 지정되지 않았다. 2026-10-12에 받은 최신 HEAD는 `3f090e4`이다. 이 HEAD 판을 비교에 썼다.
- **결론**: A (Baldock 계수 0.25 → 0.28), F (preprint 식 B의 `c_ϑ/Δϑ` 항은 식 (2.6)과 맞지 않는 표기)
- **노트에 쓸 결론 문장**: SnapWave 에너지 수지의 A·C·R 계수와 구조는 Roelvink et al. (2025) preprint 식 (2.6)–(2.7)과 같지만, Baldock 소산 계수는 preprint 식 (2.2)의 0.25가 아니라 독립 코드와 SFINCS가 쓰는 0.28이고 preprint의 계수 B가 적은 `c_ϑ/Δϑ` 항은 식 (2.6)과 맞지 않아 코드에 없다.

## B080 subgrid 모드와 van Ormondt et al. (2025) 일관성

- **행 ID**: B080 (`docs/developments.rst:162`, `docs/index.rst:46`, `docs/input.rst:267`)
- **외부 원문**: van Ormondt, M., Leijnse, T., de Goede, R., Nederhoff, K., and van Dongeren, A. (2025). Geosci. Model Dev., 18, 843–861, DOI 10.5194/gmd-18-843-2025. HTML `https://gmd.copernicus.org/articles/18/843/2025/gmd-18-843-2025.html`(HTTP 200)과 PDF `.../gmd-18-843-2025.pdf`(HTTP 200)를 받았다. 식은 HTML의 MathML을 텍스트로 풀어 읽었고 기호 사이 공백과 괄호는 이 변환에서 일부 사라졌다. 식 번호는 HTML 본문에서 읽은 값이다.
- **원문 인용(exact)**:
  - §2.2 식 (12): `⟨q_u⟩_G^{t+Δt} = ⟨q_u⟩_G^t − gΔt⟨H_u⟩_G Δz/Δx + φ_u FΔt / (1 + gΔt n_u² ⟨q_u⟩_G^t / ⟨H_u⟩_G^{7/3})`, 바로 아래: `where n_u is φ_u^{2/3} n_{u,W}.`
  - 식 (13): `n_u = ⟨H_u⟩_G^{5/3} / ⟨H_u^{5/3}/n⟩_G`
  - 식 (16): `φ_{u,m} = (1/N) Σ_{k=1}^{N} p(z_m − z_{b,k})`
  - 식 (17): `⟨H_u⟩_{G,m} = (1/N) Σ_{k=1}^{N} max(z_m − z_{b,k}, 0)`
  - 식 (18): `n_{u,m} = ⟨H_u⟩_{G,m}^{5/3} / [(1/N) Σ_{k=1}^{N} max(z_m − z_{b,k}, z_min, 0)/n_k^{5/3}]` (HTML 변환에서 `max(…)`의 괄호가 지워졌다. 본문 문장은 `to determine the representative roughness, the maximum of the pixel elevation and z min is used`이다.)
  - 식 (19): `n_u = ⟨n_u⟩_G − (⟨n_u⟩_G − n_{u,M}) / (β(z_u − z_max) + 1)`
  - 식 (22): `⟨H_u⟩_G = ⟨H_u⟩_{G,M} + z_u − z_max`
  - §2.3 식 (23): `V^{t+Δt}_{m,n} = V^t_{m,n} + Δt[(⟨q_u⟩^t_{G,m−1,n} − ⟨q_u⟩^t_{G,m,n})/Δy + (⟨q_u⟩^t_{G,m,n−1} − ⟨q_u⟩^t_{G,m,n})/Δx + S_{m,n}]`(HTML 변환 결과의 괄호 배치는 불확실하다).
  - 식 (24): `V(z) = (ΔxΔy/N) Σ_{k=1}^{N} max(z − z_k, 0)`
  - 식 (25): `z_s = z_max + (V − V_max)/(ΔxΔy)`
  - 본문: `When the entire velocity point is wet (z_u ≥ z_max)`
- **문서·코드와 비교**:
  - 식 (12)의 압력항은 코드 `sfincs_momentum.f90:409`의 `frc = - g * hu * dzdx`와 같다(`hu`는 ⟨H_u⟩_G).
  - 식 (12)의 마찰 분모는 코드 `sfincs_momentum.f90:677`의 `1.0 + gnavg2 * dt * qfr / hu73`와 같다. `gnavg2`는 `g*n²`이고 입력에서 `subgrid_uv_nrep = g*max(rtmpuv2, 0.0001)**2`로 변환한다(`sfincs_subgrid.F90:347`).
  - 식 (12)의 `φ_u F`는 코드에서 `phi`를 `F`에 곱하지 않고 `hwet = hu / phi`(`sfincs_momentum.f90:391`)로 쓴다. 바람 힘은 `tauwu(nm) * hu * 4`(`:570`)로 계산하고, 주석 처리된 이전 형태 `phi * tauwv * hwet * 4`(`:574`)와 곱이 같다.
  - 식 (17)·(18)의 표는 코드 `subgrid_uv_havg`, `subgrid_uv_nrep`에, 식 (16)은 `subgrid_uv_pwet`에 대응한다. 입력은 `sfincs_subgrid.F90:352–356`이다.
  - 식 (22)는 코드 `sfincs_momentum.f90:351`의 `hu = subgrid_uv_havg_zmax(ip) + zsu`와 같다. `subgrid_uv_havg_zmax`는 `subgrid_uv_havg(subgrid_nlevels, ip) - subgrid_uv_zmax(ip)`(`sfincs_subgrid.F90:444`)이다.
  - 식 (19)는 코드 `sfincs_momentum.f90:364`의 `gnavg2 = subgrid_uv_navg_w(ip) - (subgrid_uv_navg_w(ip) - subgrid_uv_nrep_zmax(ip)) / (subgrid_uv_fnfit(ip) * (zsu - zmax) + 1.0)`와 같은 구조이다.
  - 식 (24)·(25)는 코드 `sfincs_continuity.f90:565–568`(`dzvol = subgrid_z_volmax(nm) / (subgrid_nlevels - 1)`, 부피 구간 선형 보간)과 `:553`(`zs(nm) = max(subgrid_z_zmax(nm), -20.0) + (z_volume(nm) - subgrid_z_volmax(nm)) / a`)에 대응한다.
  - 차이는 두 곳이다. 논문은 `z_u ≥ z_max`일 때 완전 젖음으로 쓰고, 코드 `sfincs_momentum.f90:347`은 `zsu > zmax`를 쓴다. 코드 `sfincs_continuity.f90:549`는 `z_volume(nm) >= subgrid_z_volmax(nm) * 0.999`로 0.999 배율을 쓰는데 논문은 이 배율을 적지 않는다.
  - 논문의 전처리 표 정의(식 14–18, 21)와 실행 중 표 사용을 구분했다. 전처리 식은 SFINCS 코드가 아니라 HydroMT-SFINCS·Delft Dashboard에 있다. 이 대조는 실행 중 사용 식만 확인했다.
- **결론**: 일치 (분류 기호 해당 없음). 차이는 부등호와 0.999 배율의 F급 표기·구현 세부이다.
- **노트에 쓸 결론 문장**: 실행 중 subgrid 식의 압력항, 마찰 분모, 완전 젖음 깊이 식 (22), 거칠기 식 (19), 부피–수위 표 식 (24)·(25)는 van Ormondt et al. (2025)의 식과 같은 구조이며, 코드는 완전 젖음 판정에 `zsu > zmax`와 부피 비율 0.999를 쓰는 점만 논문 본문과 다르다.

## B103 개선된 2차원 이류 항

- **행 ID**: B103 (`docs/developments.rst:283`)
- **외부 원문**: `https://raw.githubusercontent.com/Deltares/SFINCS/v2.0.0/source/src/sfincs_momentum.f90`(`v2.0.0`, 2022-11-11, `336abcd`)와 `.../v2.0.2_Blockhaus_release/source/src/sfincs_momentum.f90`(2023-06-09, `640289f`). 변경 커밋은 `105da46`(2023-01-12, `improved advection terms in sfincs_momentum.f90`)과 `5a33695`(2023-03-30, `returned to alpe d'huez 1d advection`)이다. 이 두 커밋 이름은 `git log v2.0.0..v2.0.2_Blockhaus_release`에서 읽었다. 문서의 링크 `releases/tag/v2.0.2`는 존재하지 않는 태그이다.
- **원문 인용(exact)**:
  - v2.0.0 `sfincs_momentum.f90:401, 403`: `if ( (v0_nmu + v0_nm > 0.0) .and. (v0_ndm + v0_ndmu > 0.0) ) then` / `adv = adv + ( (v0_ndm + v0_ndmu) * (qx0_nm - qx0_ndm) ) * dyuvinv / 2`
  - v2.0.0 `sfincs_momentum.f90:405, 407`: `elseif ( (v0_nmu + v0_nm < 0.0) .and. (v0_ndm + v0_ndmu < 0.0) ) then` / `adv = adv + ( (v0_nm + v0_nmu) * (qx0_num - qx0_nm) ) * dyuvinv / 2`
  - v2.0.2 `sfincs_momentum.f90:376, 378`: `qvt = q0(uv_index_v_ndm(ip)) + q0(uv_index_v_ndmu(ip)) + q0(uv_index_v_nm(ip)) + q0(uv_index_v_nmu(ip))` / `if ( qvt > 1.0e-6 ) then`
  - v2.0.2 `sfincs_momentum.f90:380, 384`: `adv = adv - (q0(uv_index_v_ndm(ip)) + q0(uv_index_v_ndmu(ip))) * (uu_nm - uu_ndm) * dyuvinv / 2` / `adv = adv - (q0(uv_index_v_nm(ip)) + q0(uv_index_v_nmu(ip))) * (uu_num - uu_nm) * dyuvinv / 2`
- **문서·코드와 비교**:
  - v2.0.0의 횡방향 이류는 `v` 속도에 `qx` 유량의 차분을 곱한다. v2.0.2는 `qy` 유량 합에 `uu` 속도의 차분을 곱한다. 부호 판정도 `v` 속도의 합에서 유량 합 `qvt`로 바뀌었다. 부호 규약도 바뀌었다(v2.0.0은 `adv`를 더하고 `frc = frc - adv`, v2.0.2는 `adv`를 빼고 `frc = frc + adv`).
  - 현재 로컬 코드 `sfincs_momentum.f90:440`은 `dqyudy = ( qy_ndm + qy_ndmu ) * (uu_nm - uu_ndm) * dyuvinv / 2`로 v2.0.2의 형태(유량 합 × 속도 차분)를 이어 쓴다. 외부 문서 목록의 주의대로 현재 `upw1` 분기(`:448`)는 v2.0.2 수정 전후를 대신하지 않는다.
  - 문서 `docs/developments.rst:283`의 `Improved 2D component of advection scheme`는 위 수정과 맞는다. 그러나 v2.0.0 대 v2.0.2의 차이가 `improved`인지 여부(정확도 개선)는 소스 diff만으로 판정하지 않았다.
- **결론**: A
- **노트에 쓸 결론 문장**: v2.0.2는 2차원 횡방향 이류 항을 v2.0.0의 `v`속도 × `qx`유량 차분에서 `qy`유량 합 × `uu`속도 차분과 유량 합 부호 판정으로 바꾸었다.

## B110 weir 공식 수정

- **행 ID**: B110 (`docs/developments.rst:290`)
- **외부 원문**: `https://raw.githubusercontent.com/Deltares/SFINCS/v2.0.0/source/src/sfincs_structures.f90`와 `.../v2.0.2_Blockhaus_release/source/src/sfincs_structures.f90`. 변경 커밋은 `def301e`(2023-04-06, PR #19 `18-potential-bug-in-weir-formula-fully-submerged`의 병합, 파일 1개, 2줄 변경)이다.
- **원문 인용(exact)**:
  - v2.0.0 `sfincs_structures.f90:523, 524`: `cweir = 1.7049` / `m = 0.0 ! Modular limit ...`
  - v2.0.0 `sfincs_structures.f90:541, 545`: `if (h1>0.0 .and. h2>0.0) then` / `qstruc = Cd*cweir*h1*sqrt((h1 - h2)/(1.0 - m))`
  - v2.0.2 `sfincs_structures.f90:589, 593`: `if (h2 > 2.0 / 3.0 * h1) then` / `qstruc = Cd*h2*sqrt(2.0 * 9.81 * (h1 - h2)/(1.0 - m))`
  - 두 판 모두 자유 유출식: `qstruc = Cd*cweir*h1**1.5`
- **문서·코드와 비교**:
  - 두 판의 `diff -w`는 `sfincs_structures.f90`에서 위 두 줄의 변경과 `give_structure_information` 서브루틴의 추가(463–511행 부근)뿐이다.
  - v2.0.2의 잠김 조건은 `h2 > 2/3*h1`이고 잠긴 흐름은 `Cd*h2*sqrt(2*g*(h1 - h2)/(1 - m))`이다. v2.0.0은 잠김을 `h1>0 .and. h2>0`으로 판정했고 `Cd*cweir*h1*sqrt((h1 - h2)/(1 - m))`을 썼다.
  - 현재 로컬 코드 `sfincs_structures.f90:651–652, 669, 673, 679`는 v2.0.2와 같다. `v2.0.2_Blockhaus_release`의 `sfincs_structures.f90`은 v2.2.0 태그의 같은 파일과 다르다(`diff -q`). 그 차이 내용은 확인하지 않았다.
- **결론**: A
- **노트에 쓸 결론 문장**: v2.0.2는 broad-crested weir의 잠김 판정을 `h1>0 .and. h2>0`에서 `h2 > 2/3*h1`로 바꾸고 잠긴 흐름식을 `Cd*h2*sqrt(2*9.81*(h1 - h2)/(1 - m))`로 바꾸었다.

---

## 접근 기록

접근하지 못한 URL은 없다. 시도한 URL과 결과는 아래와 같다.

- `https://raw.githubusercontent.com/Deltares/SFINCS/v2.2.0_col_dEze_release/...`, `v2.3.0_mt_Faber_release`, `v2.4.0_Galibier_release`, `v2.0.0`, `v2.0.2_Blockhaus_release`: 모두 HTTP 200.
- `https://raw.githubusercontent.com/Deltares/SFINCS/v2.0.2/source/src/sfincs_momentum.f90`: HTTP 404(해당 이름의 태그가 없다).
- `https://raw.githubusercontent.com/Deltares/SFINCS/v2.0.0_Alpe_d_Huez_release/source/src/sfincs_momentum.f90`: HTTP 404(해당 이름의 태그가 없다. 실제 태그는 `v2.0.0`).
- `https://raw.githubusercontent.com/Deltares/SFINCS/<태그>/source/src/sfincs_subgrid.f90`(소문자 확장자): HTTP 404. 실제 파일은 `sfincs_subgrid.F90`(v2.2.0 이후). v2.0.0과 v2.0.2 트리에는 subgrid 파일이 없다.
- `https://repository.tudelft.nl/record/uuid:53037d4d-d7a9-4f71-9b22-8c329f2b384c`: HTTP 200. `https://repository.tudelft.nl/file/File_f7c6a5a4-7c8e-4a2e-a4a5-0f9a0d3a1b2c`(추측한 주소): HTTP 404. 올바른 PDF 주소 `https://repository.tudelft.nl/file/File_da13d247-495e-4556-9211-abb18ee7232d`는 서지 페이지의 링크에서 읽었고 HTTP 200. 저장소의 이용 조건은 `Other than for strictly personal use, it is not permitted to download, forward or distribute the text or part of it`이라 적는다. 이 파일에는 짧은 인용만 적었다.
- `https://gmd.copernicus.org/articles/18/843/2025/gmd-18-843-2025.html`, `.pdf`: HTTP 200.
- `https://egusphere.copernicus.org/preprints/2025/egusphere-2025-492/egusphere-2025-492.pdf`: HTTP 200.
- `https://api.github.com/repos/lutraconsulting/MDAL/git/trees/master?recursive=1`, `raw.githubusercontent.com/lutraconsulting/MDAL/master/...`: HTTP 200.
- `https://api.github.com/repos/Deltares/SFINCS/issues/283`, `/issues/335`, `/releases/tags/v2.4.0_Galibier_release`, `/tags`: 응답 있음.
- `https://api.github.com/search/commits?q=repo:Deltares/SFINCS+Elmessary`, `.../search/issues?q=repo:Deltares/SFINCS+Elmessary`: 결과 0건. 이 이름은 외부 기록에서 찾지 못했다.

## 확인하지 않은 것

- SFINCS를 실행하지 않았다. 위 수정이 수치 결과를 어떻게 바꾸는지는 확인하지 않았다.
- QGIS를 실행하지 않았다. B042의 QGIS 표시는 MDAL 소스와 PR #335 설명으로만 판단했다.
- SnapWave 독립 코드의 문서가 가리키는 당시 commit은 식별하지 못했다. B070은 2026-10-12의 HEAD `3f090e4`로 비교했다.
- B051의 `Elmessary`와 PR #283의 `Yasmine`이 같은 사람인지 확인하지 못했다.
- B080의 논문 식 (14)–(18), (20), (21)에 해당하는 전처리 코드는 이 저장소 밖(HydroMT-SFINCS 등)에 있어 확인하지 않았다.
