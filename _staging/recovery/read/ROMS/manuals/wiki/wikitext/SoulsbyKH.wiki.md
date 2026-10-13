---
file: models/ROMS/raw/manuals/wiki/wikitext/SoulsbyKH.wiki
lines: 8
sha256: 289f077ac6003a319dcfb2fd2ced0e092878ac61453cf9460ed14ae9ec338749
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# SoulsbyKH.wiki — 판독 구간 기록

구간은 1행부터 8행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | Methods for Calculating kh — 표면 중력파(surface gravity waves)의 분산(dispersion) 관계와 각주파수(angular frequency)·주기·중력·수심·파수(wavenumber)·파장 정의와 단위를 제시한다(1–3). k가 암시적이라 kh 근사를 사용한다고 적는다(3). SSW_HUNT_KH이면 Hunt의 5차 다항식, SSW_SOULSBY_KH이면 Soulsby의 Newton-Raphson 방법을 사용한다고 적는다(5). 두 CPP 정의는 Sherwood 개발 분기의 SSW_BBL.h에만 구현되었다고 한정하고 하나를 선택하는 예제를 제시한다(7–8). 원문: `The dispersion equation for surface gravity waves is <math>\omega^2 = gk~ \text{tanh}(kh)</math>, where <math>\omega</math> is the angular frequency of the wave (<math>2\pi/T</math>) where <math>T</math> is period (s), <math>g</math> is gravitational acceleration (m2 s-1), <math>h</math> is water depth (m), and <math>k</math> is wavenumber (<math>2\pi/\lambda</math>) where <math>\lambda</math> is wavelength (m). <math>k</math> is difficult to calculate because it is implicit.[[Bibliography#WibergP_2008a \| Wiberg and Sherwood (2008)]] reported on the speed and accuracy of several explicit and iterative methods for approximating <math>kh</math>. Two good methods are implemented in ROMS/CSTMS.` (3); `A fifth-order polynomial approximation attributed to Hunt (1979) by [[Bibliography#DeanR_1991a \| Dean and Dalrymple (1991), p72]] is used when SSW_HUNT_KH is defined, and the Newton-Raphson method suggested by [[Bibliography#SoulsbyR_2005a \| Soulsby (2005)]] is used when SSW_SOULSBY_KH is defined.` (5); `{{warning}} '''Note:''' The Soulsby option and these two CPP defs are only  implemented in the version of SSW_BBL.h located in [https://www.myroms.org/projects/cstm/browser/branches/crs/cstm_trunk Sherwood's branch]. Define one of these two options:` (7); `<div class="box">#define SSW_SOULSBY_KH<br />#undef SSW_HUNT_KH</div>` (8); `\omega^2 = gk~ \text{tanh}(kh)` (3); `\omega` (3); `2\pi/T` (3); `T` (3); `g` (3); `h` (3); `k` (3); `2\pi/\lambda` (3); `\lambda` (3); `k` (3); `kh` (3). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 3행: 중력 가속도 g의 단위는 원문에 `m2 s-1`로 적혀 있다.
