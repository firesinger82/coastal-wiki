# ShorelineS upstream 이슈 초안 3건 (2026-09-22)

대상: https://github.com/danoroelvink/shorelines
검증 기준 스냅샷: `f3ec8638ddb53eb93fc2a77fa472bcb11b2cf940` (2026-08-13) — 코드는 `7bf4481ab`(2025-10-07)과 동일.
매뉴얼: `doc/ShorelineS_manual_v1.0.pdf` (v1.0 'TKI' release, 15 October 2024, 66 pp).

**상태: 미제출.** 제출 전 사용자 승인 필요. 아래는 그대로 붙여넣을 수 있는 본문이다.

---

## 이슈 1 — `rotfac` input keyword has no effect (dead parameter)

**유형**: bug · **영향**: 사용자가 설정해도 무시됨

> ### Summary
> The `rotfac` keyword is documented as a user-settable parameter and is assigned a default, but its value never reaches the diffraction computation. `wave_diffraction.m` recomputes `rotfac` locally and ignores the value passed in the structure.
>
> ### Evidence (commit `f3ec863`)
> The value is set and propagated:
> ```
> functions/initialize_defaultvalues.m:158    S.rotfac=1.5;   % factor determining the rotation of waves due to diffraction
> functions/prepare_structures.m:114          STRUC.rotfac=S.rotfac;
> ```
> `STRUC.rotfac` is assigned there and **never read anywhere in the codebase** (`grep -rn '\.rotfac' functions/` returns only the two lines above).
>
> Inside the diffraction routine a *local* `rotfac` is computed from scratch and that is what the rotation uses:
> ```
> functions/wave_diffraction.m:106   rotfac_longcrested  = 0.8;   % at dirspr = 12 (default)
> functions/wave_diffraction.m:108   rotfac_shortcrested = 0.8;   % at dirspr = 32
> functions/wave_diffraction.m:113   rotfac = (1-alfa)*rotfac_longcrested + alfa*rotfac_shortcrested;
> functions/wave_diffraction.m:118   rotfac = 1;                  % when wdform is dabees/hurst/kamphuis
> functions/wave_diffraction.m:373-374, 544-545                   % <- the local rotfac is used here
> ```
>
> ### Consequences
> 1. Setting `rotfac` in the input file has no effect in the Roelvink diffraction path.
> 2. The default in Appendix B of the technical manual (`rotfac = 1.5`, p.62) is never the effective value. The effective value is **0.8**, which matches the manual body (p.35) — so the manual contradicts itself and the table is the one that is unreachable.
> 3. Because `rotfac_longcrested` and `rotfac_shortcrested` are **both 0.8**, the directional-spreading blend at `:113` is an identity for `rotfac`; only `omegat` actually varies with spreading (-20° → -35°). The manual states "The degree of rotation also depends on a spreading factor of the waves (`rotfac`)" (p.35), which does not hold as implemented.
>
> ### Suggested resolution
> Either honour `STRUC.rotfac` (e.g. use it as the long-crested anchor, falling back to 0.8 when unset), or remove the keyword and its default and document `rotfac` as an internal constant. Whichever is chosen, Appendix B and §6.1.2 should agree with the code.

---

## 이슈 2 — `RAY` transport formulation is undocumented

**유형**: documentation · **영향**: 구현된 기능이 매뉴얼·주석 어디에도 없음

> ### Summary
> `transport.m` implements a transport branch selected by `trform` containing `'ray'`, but it appears in neither the technical manual nor the in-file documentation comment.
>
> ### Evidence (commit `f3ec863`)
> The branch exists:
> ```
> functions/transport.m:194   elseif ~isempty(findstr(lower(TRANSP.trform),'ray'))
> functions/transport.m:195       QS = -WAVE.c1.*WAVE.dPHItdp .* exp(-(WAVE.c2.*WAVE.dPHItdp).^2) + WAVE.QSoffset;
> functions/transport.m:196       QS(abs(WAVE.dPHItdp)>90)=0;
> functions/transport.m:197       dQSdPHI = ...
> ```
> It is not documented:
> - `doc/ShorelineS_manual_v1.0.pdf` §5.1 "Transport formulations" describes CERC1, CERC2, CERC3, KAMP, MILH, VR14 and TIDEPROF — searching the whole PDF for `RAY`/`'ray'`/`trform.*ray` returns nothing.
> - The in-file header comment lists only five: `functions/transport.m:10` — `.trform : transport formulation (either 'CERC', 'KAMP', 'MILH', 'CERC3', 'VR14')`.
>
> ### Related: the Appendix B enumeration is also incomplete
> ```
> Appendix B (p.61):  trform  'CERC'  switch for transport formulation (e.g. S.trform='CERC', 'KAMP', 'MILH' or 'VR14')
> ```
> This omits `CERC2`, `CERC3`, `TIDEPROF` and `RAY`, although §5.1 documents the first three. (`transport.m:140` accepts both `'CERC'` and `'CERC1'`, so those two are aliases — that is also worth stating.)
>
> ### Suggested resolution
> Document the `RAY` branch (inputs `c1`, `c2`, `QSoffset`, and the intended use case — it reads like an interface for externally computed ray/s-φ transport curves), or mark it explicitly as experimental/internal. Align `transport.m:10` and Appendix B with the seven formulations in §5.1.

---

## 이슈 3 — Manual states `Kw = 1.2` in the text but `4.2` in the table (code is 4.2)

**유형**: documentation · **영향**: 사구 풍성수송 계수 오인

> ### Summary
> The aeolian transport coefficient `Kw` is given two different values in the same document, and only one matches the code.
>
> ### Evidence
> ```
> doc/ShorelineS_manual_v1.0.pdf p.49 (§7.2, under Eq. 70):
>     "Where Kw is an empirical coefficient of 1.2 [-] based on Sherman et al. 2013."
>
> doc/ShorelineS_manual_v1.0.pdf p.50 (parameter list, §7.2):
>     Kw=4.2    Empirical coefficient (Sherman et al. 2013)
>
> doc/ShorelineS_manual_v1.0.pdf p.63 (Appendix B):
>     kw        4.2    empirical coefficient (Sherman et al. 2013)
> ```
> The code agrees with 4.2:
> ```
> functions/initialize_defaultvalues.m:193   S.kw=4.2;   % empirical coefficient (Sherman et al. 2013)
> functions/prepare_dunes.m:96               DUNE.kw=S.kw;
> ```
>
> ### Suggested resolution
> Correct the p.49 sentence to 4.2 (or state explicitly why the equation description uses a different value than the default).

---

## 제출 시 유의

- 세 건 모두 **읽기 전용 검증**으로만 도출했다 — 모델을 실행하지 않았다.
- 이슈 1은 동작 변경을 수반하므로 업스트림이 의도한 설계일 가능성을 열어 두고 물음 형태로 적었다.
- 본 위키의 대응 기록: `models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md` §9.3·§9.4.
  위키는 **코드 실측을 기준**으로 삼고 매뉴얼 표기를 부차로 둔다.
