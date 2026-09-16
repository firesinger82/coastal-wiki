## (A) 원문 해석해 사실 — Lynch & Gray (1978)

**다운로드/판본**
- URL: `https://ccht.ccee.ncsu.edu/wp-content/uploads/sites/10/2019/05/Lynch-1978-JHY.pdf`, HTTP 200, 15,865,599 bytes.
- `pdfinfo`: Pages 21, PDF 1.5, Producer iTextSharp 4.1.6, page size 798.72 × 760.32 pt, 비암호화.
- **텍스트 레이어 없음**(스캔 영상). `pdftotext -layout` 결과 파일은 사실상 빈 파일 → 전 페이지를 `pdftoppm -r 150 -png`로 이미지화해 직접 판독.
- 페이지 대응: PDF 1 = 저널 표지, **PDF 2 = 인쇄면 1409**, 이후 PDF N = 인쇄면 1407+N. 본문은 인쇄면 1409–1428.
- SHA256은 산출하지 못함(사유는 (C)).
- 보존 파일: `/tmp/lynch1978-test.pdf`, `/tmp/lynch1978-p-01..21.png`(150 dpi 전 페이지), `/tmp/lynch1978-lo-02..21.png`(55 dpi), 크롭 `/tmp/lynch1978-c5top-05.png`, `/tmp/lynch1978-c7mid-07.png`, `/tmp/lynch1978-c7bot-07.png`, `/tmp/lynch1978-c2abs-02.png`. (요청된 `/tmp/adcirc-quarterannular-20260916/` 디렉터리는 생성이 차단되어 파일명 접두어로 대체 — (C) 참조.)

### A-1. 지배방정식과 선형화 조건 — 인쇄면 1410 (PDF 3), “BASIC EQUATIONS”

원문: “The linearized shallow water equations will be solved in the subsequent examples. These equations are obtained from the full shallow water equations **by neglecting the convective terms, assuming the oscillations of the free surface are small in comparison to the total depth, and using a linearized friction term.**”

| 식 | 내용 | 위치 |
|---|---|---|
| (1) | ∂ζ/∂t + ∇·[h **v**] = 0 | 1410 / PDF 3 |
| (2) | ∂**v**/∂t + g∇ζ + τ**v** − **W**/h = 0 | 1410 / PDF 3 |
| (3) | ∂²ζ/∂t² + ∇·[h ∂**v**/∂t] = 0 | 1410 / PDF 3 |
| (4) | ∂²ζ/∂t² − ∇·(gh∇ζ) − τ∇·(h**v**) = 0 | 1410 / PDF 3 |
| (5) | ∂²ζ/∂t² + τ ∂ζ/∂t − g∇·(h∇ζ) = 0 | 1410 / PDF 3 |

- 기호 정의(같은 페이지): ζ = 평균해면 위 수위, **v** = 연직평균 유속, h(x,y) = 평균해면부터 바닥까지 거리(**정수심, 총수심 아님**), τ = **상수로 가정된 선형화 저면마찰 계수**, **W** = 공간적으로 불변인 바람응력.
- **Coriolis 항은 식 (2)에 존재하지 않는다.** 판독한 1409–1415 범위에서 Coriolis를 명시적으로 언급한 문장은 찾지 못했다(원문 전체를 훑지는 않음 — (C)).
- 서론(1410 상단): “By necessity the shallow water equations **have been linearized.** However bottom friction, wind stress, Cartesian and polar geometry, and variable bathymetry have been incorporated into the equations.”
- 유속은 별도 해가 아니라 식 (2)로부터 얻는다고 명시(1410 하단: “The solution for **v** is then obtained from …”).

### A-2. Case I: Polar Geometry — 인쇄면 1411 (PDF 4)

- 문제 설정 원문: “Flow is required to be **tangent to the solid boundaries at r = r₁, θ = 0 and θ = φ**. A tidal forcing function is specified at **r = r₂**, and constant wind stress is imposed throughout, in an arbitrary direction. Bathymetry is described by **h = H₀ rⁿ** in which H₀ is a constant, and n is not necessarily an integer and may assume any real value.”
- 경계조건 (6a) at r=r₁: ∂ζ/∂r − W_r/(gh) = 0; (6b) at r=r₂: ζ(r₂,θ,t) = Re{ζ₀(θ) e^{iωt}}; (6c) at θ=0,φ: (1/r)∂ζ/∂θ − W_θ/(gh) = 0.
- “ζ₀(θ) = a complex function representing the tidal amplitude and phase at r = r₂; and **i = √−1**.” → **조화시간 규약은 Re{ · e^{+iωt}}**.
- Fig. 1 “Annular Section in r-θ Coordinates with Opening at r = r₂” — 개구부(조석 경계)가 **바깥 반경**, 나머지 3변이 무유량.
- 분해 (7): ζ = ζ_f + ζ_w, ζ_f = 바람응력 없을 때의 해, ζ_w = 조석 강제 없을 때의 해. (8a–8d)는 바람(정상상태) 문제.

### A-3. 조석 문제의 방정식 — 인쇄면 1412 (PDF 5)

| 식 | 내용 |
|---|---|
| (9a) | ∂²ζ_f/∂t² + τ ∂ζ_f/∂t − g H₀ r^{n−2} [ r² ∂²ζ_f/∂r² + r(n+1) ∂ζ_f/∂r + ∂²ζ_f/∂θ² ] = 0 |
| (9b) | at r = r₁: ∂ζ_f/∂r = 0 (무유량) |
| (9c) | at r = r₂: ζ_f(r₂,θ,t) = Re{ζ₀(θ) e^{iωt}} |
| (9d) | at θ = 0, φ: ∂ζ_f/∂θ = 0 (무유량) |

### A-4. Periodic Tidal Response — 인쇄면 1414 (PDF 7)

- 가정 해: “assume a solution of the form **ζ_f(r,θ,t) = Re{R(r) T(θ) e^{iωt}}**. Substituting this in Eq. 9a produces”
- (20a): (1/R)[ r²R″ + rR′(1+n) + β²R / r^{n−2} ] = κ²
- (20b): T″/T = −κ²
- “in which κ² = a separation constant and **β² = (ω² − iωτ)/(g H₀)**.” — 마찰이 β²의 허수부로만 들어가는 복소 파라미터.
- (21): ζ_f(r,θ,t) = Re{ Σ_j (a_j R_{1j} + b_j R_{2j})[cos(κ_j θ) + c_j sin(κ_j θ)] e^{iωt} }
- 경계조건 9d로 **c_j = 0**, 그리고 **κ_j = jπ/φ, j = 0,1,2,…** 만 남김.
- (22): ζ₀(θ) = Σ_{j=0}^{∞} F_j cos(jπθ/φ)

### A-5. 정확해와 n = 2(2차 수심) 한계형 — 인쇄면 1415 (PDF 8)

- F_j 정의: F_j = ∫₀^φ ζ₀(θ) cos(jπθ/φ) dθ / ∫₀^φ cos²(jπθ/φ) dθ
- (23a) a_j R′_{1j}(r₁) + b_j R′_{2j}(r₁) = 0 ; (23b) a_j R_{1j}(r₂) + b_j R_{2j}(r₂) = F_j ; (23c)(23d) 그 해 a_j, b_j (분모 = R′_{2j}(r₁)R_{1j}(r₂) − R_{2j}(r₂)R′_{1j}(r₁))
- **(24) 완전해**: ζ_f(r,θ,t) = Re{ e^{iωt} Σ_{j=0}^{∞} (a_j R_{1j} + b_j R_{2j}) [ cos(jπθ/φ) ] }
- **n ≠ 2**: (25a) R_{1j}(r) = r^{−n/2} J_p[ β r^{1−(n/2)} / (1 − n/2) ], (25b) 동일형에 Y_p. (25c) p = (1/(2−n))·√( n² + (2jπ/φ)² ). “in which J_p and Y_p are the solutions of Bessel’s equation of order p” (Hildebrand 인용 (6)).
- **“When n = 2 or β = 0, the limiting forms of Eqs. 25a and 25b are”**
  - (25d) R_{1j}(r) = r^{s_j}; **s_j = −n/2 + √( (n/2)² − β² + (jπ/φ)² )**
  - (25e) R_{2j}(r) = r^{t_j}; **t_j = −n/2 − √( (n/2)² − β² + (jπ/φ)² )**
  - 즉 **2차 수심(n=2)에서는 Bessel이 아니라 멱함수 r^{s_j}, r^{t_j}** 이며, n=2 대입 시 지수는 −1 ± √(1 − β² + (jπ/φ)²).
- 선형성에 따른 다주파 중첩 가능: ζ_f(r₂,θ,t) = Re{ Σ_{j=1}^{N} ζ_j(θ) e^{iω_j t} } 형태 강제도 N개의 개별해로 처리.

**로컬 입력과의 대응 관찰(계산·판단은 상위 Codex 몫)**: 로컬 fort.14의 수심은 h = 3.048·(r/60960)² 형태이므로 n = 2, H₀ = h₁/r₁²; 개방경계는 바깥 반경(r₂=152400)에 위치해 식 (9c) 위치와 같고, 나머지 3변이 무유량으로 (9b)(9d)와 같다; 개구각 φ = π/2; fort.15의 M2 진폭·위상이 9개 경계노드에서 모두 동일(0.3048 m, 0°)하므로 식 (22)의 Fourier 전개에서 j = 0 항만 남는 형태에 해당한다. 반면 로컬 입력은 NOLIFA=NOLICA=NOLICAT=1, NOLIBF=1(2차 마찰)로 위 선형화 조건 3가지(대류항 무시, 미소진폭, 선형마찰 τ)와 모두 어긋난다.

**판독 신뢰도**: 위 식들은 모두 150 dpi 렌더 이미지에서 직접 읽었고 해당 페이지 이미지를 보존했다. 애매해 부호를 추정한 곳은 없다. 재확인이 필요하면 `/tmp/lynch1978-p-03.png`(1410), `p-04.png`(1411), `c5top-05.png`(1412), `c7mid-07.png`·`c7bot-07.png`(1414), `p-08.png`(1415)를 보면 된다.

## (B) NetCDF 및 입력 코드 사실

### B-1. control NetCDF 메타데이터 (`_staging/adcirc-quarterannular-20260916/control-metadata.json`)

- 6개 파일(fort.61.nc, fort.62.nc, fort.63.nc, fort.64.nc, maxele.63.nc, maxvel.63.nc) 모두 `version_attributes` = **`version: v56.0.1-21-gbcb79a8`, `source: CircleCI`** (JSON 각 항목의 `version_attributes` 필드).
- 각 파일 sha256이 JSON에 기록됨(예: fort.61.nc `2305d583bd…`, fort.63.nc `be65a3d3…`).
- 전역 속성 이름 목록에 `model, version, git_hash, rundes, runid, institution, source, history, host, creation_date, modification_date, fort.15, dt, ihot, ics, nolibf, nolifa, nolica, nolicat, nwp, ncor, ntip, nws, nramp, tau0, statim, reftim, rnday, dramp, h0, cf, eslm, cori, ntif, nbfr` 포함. **이름만 있고 값은 JSON에 없다** (`git_hash`, `creation_date`, `dt`, `nolifa` 등 실제 값 미수록).
- 차원: fort.61/62 = time 824, station 3; fort.63/64 = time 824, node 63, nele/nfaces 96, nvertex 3, nope 1, neta 9, max_nvdll 9, nbou 1, nvel 21, max_nvell 21; maxele/maxvel = time 1. 시간 변수 단위는 `seconds since 2020-04-28 00:00:00` — fort.15:74의 날짜 문자열과 일치.
- 앞선 보고와의 구분: **ASCII control(fort.51, fort.53)에는 여전히 판본 증거가 없다**(헤더에 성분/주파수/노드수만). 이번에 추가된 것은 **NetCDF control 6개의 self-reported 전역 속성**이며, 이는 파일이 스스로 기록한 값이다. 컴파일러·최적화 플래그·NetCDF 라이브러리 버전·실행 호스트 설정을 입증하지 않는다(`host` 속성은 목록에만 있고 값 미확보).
- 비교 계약과의 접점(관찰): `drop_variables` 중 `neta, nvel, max_nvdll, max_nvell`은 이 파일들에서 **차원 이름**이고 변수 목록에는 없다 → 실제로 드롭되는 것은 `nvdll, ibtype, nbdv, nvell, nbvv, ibtypee`. `time_of_zeta_max`, `time_of_vel_max`는 `"time_of" in var` 규칙으로 제외되고, `element`·`adcirc_mesh`(int32)는 dtype kind 'i'라 비교 대상이 된다.

### B-2. 입력 계약 코드 (`S/src/read_input.F`) — 값 처리 위치만

| 파라미터 | 코드 처리 | file:line |
|---|---|---|
| NOUTE 읽기 | `READ(15,*) NOUTE,TOUTSE,TOUTFE,NSPOOLE` | read_input.F:3607 |
| NOUTE 분기 | `SELECT CASE(ABS(NOUTE))`; `CASE(5)` → `useNetCDF=.true.`, `useNetCDFOutput=.true.`, 로그 `'UNIT 61 WILL BE NETCDF CLASSIC MODEL / NETCDF4 (HDF5) FORMAT.'`; `CASE(4,6:)` → terminate | read_input.F:3613, **3628-3632**, 3633-3636 |
| NOUTV(fort.62) = 5 | 동일 패턴, `'UNIT 62 … NETCDF4 (HDF5) FORMAT.'` | read_input.F:**3757-3761** |
| NOUTGE(fort.63) = 5 | 동일 패턴, `'UNIT 63 FORMAT … NETCDF4 (HDF5) FORMAT'` | read_input.F:**4143-4148** |
| NOUTGV(fort.64) = 5 | 동일 패턴, `'UNIT 64 FORMAT … NETCDF4 (HDF5) FORMAT'` | read_input.F:**4217-4222** |
| NHSTAR/NHSINC 읽기 | `READ(15,*) NHSTAR,NHSINC` | read_input.F:4508 |
| NHSTAR = 5 | `SELECT CASE(NHSTAR)`; `CASE(5,567,568)` → `useNetCDF=.true.`, 로그 `'HOT START OUTPUT WILL BE GENERATED IN PORTABLE NETCDF CLASSIC / NETCDF4 (HDF5) FORMAT.'` | read_input.F:4521, **4534-4537** |
| NHSINC 유효성 | `NHSINC=0` & `NHSTAR≠0` → terminate | read_input.F:4542-4545 |
| NHSINC 의미 에코 | `'HOT START OUTPUT WILL BE WRITTEN TO UNIT 67 OR 68 EVERY <I10> TIME STEPS'` | read_input.F:4547-4549 |

이는 입력 파일 계약 해석일 뿐 실행 확인이 아니다. 출력 라이브러리 내부는 열지 않았다. 앞선 보고에서 “문서 미기재”로 남겼던 `NOUT*=5`, `NHSTAR=5`는 **코드상 netCDF4(HDF5) 포맷 선택지로 확정**되며, `S/docs/.../parameter_definitions/index.rst`의 NOUTE 열거(0..3 및 음수)가 코드보다 좁은 상태라는 문서-코드 불일치는 그대로 남는다.

## (C) 남은 접근/판독 갭

1. **PDF SHA256 미산출.** `sha256sum`과 `python3 -c hashlib` 모두 하네스가 차단·승인 요구(“may only compute SHA-256 checksums for files in the allowed working directories: /home/firesinger/coastal-wiki”). 확보한 무결성 근거는 HTTP 200과 바이트 크기 15,865,599뿐.
2. **지정 작업 폴더 생성 불가.** `mkdir -p /tmp/adcirc-quarterannular-20260916`, `mv`, `ls /tmp`, `wc`가 모두 cwd 제한으로 차단됐다. 파일 쓰기 자체(curl/pdftotext/pdftoppm 출력)는 `/tmp`에 가능했으므로 접두어 `/tmp/lynch1978-*`로 저장했다. 요청된 경로 규약과 다르므로 상위 Codex가 경로를 재지정하면 그대로 재생성 가능하다.
3. **OCR 미사용.** `tesseract`는 설치되어 있으나 실행이 매 호출 승인 요구로 막혀, 전 페이지 텍스트화 대신 이미지 직접 판독으로 대체했다. 따라서 “Coriolis”, “annular” 등 전문 검색은 수행하지 못했고, Coriolis 부재는 **판독한 1409–1415 범위 내 관찰**이다.
4. **유속 해석해 식 미판독.** 원문은 v를 식 (2)에서 얻는다고만 밝히며, polar 조석 문제의 유속 명시식(있다면 1416 이후)은 요청 범위 밖이라 열지 않았다.
5. **1416–1428(Cartesian 사례, startup-from-rest, 논의·요약) 미판독** — 요청된 polar/2차수심/주기조석 절에 한정했다.
6. **netCDF 전역 속성 값 미확보**: `git_hash`, `creation_date`, `host`, `fort.15` 속성의 실제 문자열은 제공된 JSON에 없어 확인하지 못했다. self-reported `version`은 컴파일러·빌드 옵션·라이브러리 판본을 입증하지 않는다.
7. **ASCII control(fort.51-54) 판본 증거**는 여전히 없음(추가 확인 사항 없음).
