검토 완료. 실제 사용 모델은 Claude Fable 5.1(`claude-fable-5-1`)이며, 파일은 쓰지 않았고 subagent도 만들지 않았다.

**결론: 새로 도입된 차단/중요 오류는 없다.** candidate의 변경 주장 전부를 source-index가 지정한 원문 구간과 로컬 ADCIRC HEAD에 대조했고, 검토 초점 항목 모두 원문과 일치하거나 도출 주장으로 올바르게 표시돼 있다.

**원문 일치 확인 항목**

- **FES cm/lag/mask/결측/radial**: handbook p.17 Table 2 `amplitude` cm·`phase` "phaselag" degrees, Table 4 mask 0/1/2/3, p.24 `_FillValue = 1.844674e+19f`, p.6 "loading tide atlas (radial component)", p.7 1/30° Cartesian. candidate 표와 일치. fort.24의 SAL 항은 `fort24.rst:6–8`("Self attraction/earth load", "units compatible with the units of gravity")과 `timestep.F:1547–1555`의 `SALTAMP*COS(ARGT−SALTPHA)`로 확인되어, radial 변위→fort.24 직접 이전을 `source-needed`로 둔 판단이 타당하다.
- **NAO integer scale/Greenwich/lag/UTC/성분**: `nao2xyap.f:92–93` `iamp*aunit`(cm)·`iphs*punit`(deg), `:118,122,167` aunit/punit/ideff와 `undef`, `naotidej.f:1113–1115` cos/sin 분해, `:761–769` atan2 복원, `:811,815` `cos(arg − phase)` lag 합성. README §4 UTC·cm·16 major+33 inferred+장주기, §5 `_gc`/pure/rload 구분, §7 "Greenwich phase". 모두 일치.
- **TPXO 범위 제한**: 제품 페이지의 2024-08-14, MSL-relative, 1/30°, base+patch, "netcdf format is different from TMD3", 동화/비동화 검증 구분만 인용하고 변수·부호·결측을 `source-needed`로 둔 것이 원문 범위와 맞는다.
- **handbook vs PyFES 기본값**: p.20 "Schureman (order 3) by default"·"v2025.2.0 at least" 대 PyFES 2026.5.3 문서(HTML title 확인) `FESSettings` `SCHUREMAN_ORDER_1`. 불일치를 명시 설정 요구로 처리한 것이 적절하다.
- **mask vs flags**: PyFES "Positive = number of interpolation points used; negative = extrapolated; zero = undefined" 일치. 두 정보를 결합하는 확인 방법은 도출로 표시됨.
- **동화 독립성**: p.6 "all tidal constituents are not constrained at each assimilated location", Appendix B "depending on the wave considered not all of these TG have been assimilated" 일치.
- **sqrt(2)**: Wang 2022 식(3)의 한 주기·전 정점 평균을 전개하면 정점당 ½E², 따라서 D=√(ΣE²/2N)이고 복소거리 RMS의 1/√2. candidate 식과 해석이 맞다. RSS 정의도 "root square sum of the rms" 일치.
- **순환 위상·표본 RMSE·Rayleigh**: PyFES `Z=a+ib=He^{iG}`, `T > C_R/|f1−f2|`, `C_R ≥ 1`, 잔차 ε의 기상 성분 모두 일치. atan2·A=0 제외·원형 보간은 도출로 표시됨.
- **무근거 권고 철회**: 5–10% SAL, 지역 정확도 순위, 분기별 갱신, "conventions match", FES/NAO 위상 규약 상이 단정 모두 제거 또는 `source-needed` 유지. README §2 분조 목록으로 N2/K2/P1 포함 확인.
- **ADCIRC 인용**: `timestep.F:257–258`, `gwce.F:1642–1649`, `read_input.F:3431–3456,3485–3497`, `fort24.rst:1–8` 모두 HEAD와 일치. ELEVALPHA가 echo만 되고 BOUNTAG와 대조되지 않는다는 서술도 `:3489–3490`과 맞다.
- **미발급 표시**: 세 파일 frontmatter `external_evidence_human_approval: not-issued`, 본문의 실행/자료품질/물리검증 미수행 문구 유지.

**비차단 소견 2건** (수정 여부는 선택)

- candidate NAO 행의 "radial은 별도"는 README §2·§5상 radial loading이 전지구 0.5° 모델만 있고 지역(NAO99Jb) 모델은 없다는 점을 드러내지 않는다. 최소 수정안: "radial loading은 전지구 0.5° 제품만 있고 지역 모델은 없다(README §2/§5)".
- source-index.md가 `sources/fes2022-handbook.provenance.json`으로 적었으나 실제 파일명은 `fes2022-handbook-provenance.json`이다. 내용 오류는 아니며 다음 Codex 설치기 검토에서 고치면 된다.
