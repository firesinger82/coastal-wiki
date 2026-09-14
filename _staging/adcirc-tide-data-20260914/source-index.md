# 외부 조석 근거 — 선정 원문 위치

원문 조회: 2026-09-14. AI 요약은 candidate/와 분리한다. 공개 문서 전체를 canonical에 복제하지 않고 URL·판본·절과 아래 해시 영수증을 남긴다. 모델 실행·atlas 수치자료 다운로드·관측 선택은 하지 않았다.

- FES2022 handbook Issue 2.0, 2026-02-03: sources/fes2022-handbook.pdf(기존 PDF ignore 정책), sources/fes2022-handbook-provenance.json. SHA-256 44bac373e314d35d2d171b1f0dd0793893fd76fcb8e3f815ae531afae0a3e7bb. `/tmp/adcirc-tide-data-sources/fes-sections.txt`는 인쇄 pp. 1, 6–7, 15, 17, 20, 24–25, 34의 추출 원문. p.17 Table2–4는 로컬 PDF 렌더를 직접 확인했다. PDF 0-based index = 인쇄 page + 6. Appendix B는 동화 정점 목록 제공 사실 확인이며 특정 후보 정점의 독립성 심사가 아니다.
- 웹/NAO 파일: sources/web-provenance.json의 URL·응답 해시·시각. 원문 HTML과 읽기용 text는 `/tmp/adcirc-tide-data-sources/`에 있다. text 추출은 BeautifulSoup의 script/style/nav 제거 및 get_text이며 원문 재작성/AI 요약이 아니다.
- `nao-readme.txt` §2 제품 범위·분조, §4 성분/UTC/cm/추론·장주기, §5 ocean/geocentric 배포, §7 Greenwich phase 변환. 2000-09-09 공식 README.
- 공식 `naotidej000909.tar.gz`: SHA-256 f61c3e473c5c40812b76e27063016cec0602c756c86607aee3c8b2108c862328. tar에서 파일 내용을 읽었으며 archive 경로에 extractall 하지 않았다. 검토 대상은 `naotidej/nao2xyap.f:17–28,90–93,116–122,149–171`와 `naotidej/naotidej.f:757–771,807–817,1112–1117`만. 전자는 integer scale·단위·결측과 출력, 후자는 lag 복원·합성. `/tmp/adcirc-tide-data-sources/nao2xyap.f` SHA-256 3f435e89e04e7adcec9f7088527cb58e70b3b09b02b0b035b6cb1874880b4f75; `naotidej.f` eb42f13713a7bcd43d88f8b4af03b236081d31792b09f13edb692c8af1a0ff45. 변환·예측 실행과 패키지 전체 내부 검증은 범위 밖.
- `pyfes-user.txt`: FES 2026.5.3 문서의 Configuration(tide/radial), Runtime Settings(order1), Inference Modes, Prediction Functions(cm/flags). handbook order3 설명과의 불일치는 기본값을 추측하지 않고 명시 설정으로 확인하도록 기술했다.
- `pyfes-nodal.txt`: Prediction Equation with Nodal Corrections — lag/Greenwich 천문 인수/f/u 의미 및 시변 보정. 공급자 식의 시각 항 표기를 새 ADCIRC 변환 공식으로 복사하지 않았다.
- `pyfes-analysis.txt`: Complex Amplitude Representation·Rayleigh Criterion·Observation Equation. atan2, 0진폭의 위상 부정, 원형 위상 보간은 복소 표현에서 도출한 확인 방법으로 구분했다.
- `tpxo10.txt`, `otps.txt`: TPXO10-atlas-v2 제품/포맷 구분 및 동화/비동화 검증, OTPS/OTPSnc 역할. actual NetCDF variable/scale/sign/fill 또는 모든 TPXO 제품 공통 규약을 확정하지 않는다.
- `uhslc.txt`: What datasets are available? FD/RQD, Frequently Asked Questions의 datum/epoch, A/B 시계열, timing 품질 평가. 특정 정점/기간/관측오차 수치는 미확정.
- `wang2022.txt`: Wang et al. 2022, DOI 10.5194/os-18-881-2022, §3.1 Eq.(3)의 한 주기·정점 평균 및 RSS. 복소거리 E와 한 주기 RMS D의 sqrt(2) 관계는 이 식에서 전개한 것으로 명시. 논문 수치를 project tolerance로 사용하지 않는다. 시계열 bias/RMSE는 노트에서 사용하는 표본 정의를 별도 명시했다.
- ADCIRC 코드/동봉 docs HEAD 6037225ce4573efd3c1f8877a5dc908d01c199a8: `models/ADCIRC/raw/source_code/adcirc/` 아래 docs/technical_reference/input_files/fort24.rst:1–8, src/timestep.F:257–258,1543–1555, src/gwce.F:1642–1649, src/read_input.F:3431–3456,3485–3497. 기존 NBFR·공식 예제 대조 영수증은 ../adcirc-feature-map-20260914/와 ../adcirc-tide-20260914/에 유지한다.
