---
title: 부유체·구조물에 의한 파 투과/반사 (floating breakwater·VLFS·floe array)
topic: waves
canonical_source: self
citation_status: verified
verification_method: "arxiv full-PDF 직접 read (1402.1555v3, 1403.3766v1) — abstract·방법·결과 본문 인용. SWAN obstacle 식은 기존 manual-note 교차참조."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - concepts/waves/01-concept.md
  - concepts/waves/04-code-and-tools.md
  - models/SWAN/manual-notes/swan-tech-ch2-obstacles-diffraction-setup.md
---

# 부유체·구조물에 의한 파 투과/반사

부유 박판(floating thin plate)·부유체 배열(disk array)에 의한 파의 **반사(reflection)**·**투과(transmission)** 문제. 해빙 marginal ice zone(MIZ)의 파 감쇠가 1차 동기이나, 동일 물리(부유 탄성판의 hydroelastic scattering)는 **부유식 방파제(floating breakwater)·초대형 부유체(VLFS)·부유 disk array** 모델링과 직접 연결된다. 위상해상 모델([[04-code-and-tools]])이나 SWAN obstacle 투과식과 대비되는, 잠재류(potential-flow)+박판 이론 기반 접근이다.

기본 개념·정의는 [[01-concept]] 참조.

---

## 1. 두 실험적 관점

본 노트는 같은 그룹(Bennetts·Meylan·Toffoli 등)의 두 wave-basin 실험 논문에 근거한다.

| | **1402.1555** (Toffoli et al. 2014) | **1403.3766** (Bennetts & Williams 2014) |
|---|---|---|
| 대상 | 단일 정방형 floe (square plate) | 부유 disk **배열**(array) |
| 시설 | Plymouth University coastal basin (10×15.5 m, h=0.5 m) | Oceanide BGO basin, La Seyne (32×16 m, h=3.1 m) |
| 재료 | polypropylene·PVC 박판 | 목재 disk (rigid, E=4 GPa) |
| 입사파 | regular, T=0.6/0.8/1.0 s, ka=0.04~0.15 | regular, τ=0.65~2 s, steepness<0.05 |
| 척도 | 1:100 full-scale 해빙 | — (disk a=0.495 m) |
| 핵심 발견 | overwash·slamming이 비선형 감쇠 지배 | 선형 모델 검증 + overwash·collision이 불일치 원인 |

> 출처: 1402.1555v3 Abstract·§II Laboratory experiments(p.4-5 본문); 1403.3766v1 Abstract·§2 Experimental design(본문).

---

## 2. 단일 floe — 반사·투과 계수 (1402.1555)

### 2.1 측정·정의

파고를 zero down-crossing으로 추출하고 전 시계열 평균. 입사파고 $H_i$(control test), floe 전면 $H_{front}$, 후면 $H_{rear}$로:

$$R = \frac{H_{front}}{H_i} - 1, \qquad T = \frac{H_{rear}}{H_i}$$

이 정의는 **선형+비선형 기여를 모두 포함**하며, beach·piston wave maker로부터의 반사는 제거되어 $R$은 floe 유발 반사만 나타낸다. (basin 자체 반사 <1%, active piston + 1:10 beach.)

> 출처: 1402.1555v3 §III.B Reflection and transmission(본문 p.9-10). 식 $R,T$는 논문 본문 그대로.

### 2.2 결과 — 파장·두께·경사 의존성

- **반사**: 저경사파에서 floe 두께 증가 시 반사 증가, 파장 증가 시 반사 감소 — 선형 수치모델과 정성 일치. 큰 경사에서는 관계가 무너짐.
- **투과**: 저경사에서도 파장에 대해 단조증가하지 **않음**. 투과는 **파장 = floe 길이**일 때 최소. 이는 field data의 attenuation "roll-over"를 닮음(단, 동일 원인이라 주장하지 않음).
- 경사 증가 시 반사·투과 모두 감소(짧은 파에서 현저). $ka\ge 0.08$에서 $L_{wave}/L_{plate}\le 1$ 구간 투과 거의 일정 후 가장 긴 파에서 증가.
- 더 유연한(compliant) PVC floe가 더 많이 투과.

> 출처: 1402.1555v3 §III.B 및 결론 1-3(p.10-11, 17). Figs.8-9는 무차원 파장 $L_{wave}/L_{plate}$ 대 $T$.

### 2.3 overwash·slamming (비선형 손실)

artificial edge barrier를 쓰지 않아 **overwash**(파가 floe 위로 넘어 흐름)를 허용한 것이 선행 실험과의 차이. floe 상면 중앙 mini-gauge로 overwash 수심 측정.

- 저경사파: 투과파가 규칙적 유지. 감쇠는 반사 + floe 휨 손실.
- storm-like파(큰 경사): overwash + slamming → 천수파가 floe 위 양단에서 생성·상호작용 → 처오름·쇄파·고주파 free wave 성분 생성. 투과파가 불규칙해짐.
- overwash는 경사 증가 시 증가. 투과는 (i) 무차원 overwash **수심** 증가 시 약하게 감소, (ii) overwash 유체의 **유의파고** 증가 시 더 뚜렷·단조 감소(파장 비민감).

> 출처: 1402.1555v3 §III.C Effect of overwash(p.12-16), 결론 4(p.17).

---

## 3. disk array — 모델 vs 실험 (1403.3766)

### 3.1 선형 이론 모델

잠재류 + Kirchhoff-Love 박판 이론 + 선형 운동 가정. 각 disk는 박판으로 모델. scaled flexural rigidity:

$$F = \frac{E D^3}{12\rho g(1-\nu^2)}$$

disk-덮인 영역의 표면조건(논문 식 2b): $(1-\sigma d)\eta + F\nabla^4\eta = \sigma\phi$ (z=−d), $\sigma=\omega^2/g$. free-edge 조건(굽힘모멘트·전단응력 소멸)과 surge 운동방정식 결합.

**2D 모델** (single-scattering = Wadhams 1973/1986; multiple-scattering = Bennetts & Squire 2012a): 두 모델이 놀랍게도 **동일**한 투과 에너지 비를 예측 —

$$\left(\frac{A_T}{A}\right)^2 = |T|^{cL/a}$$

여기서 $T$ = 단일 disk 투과계수, $c$ = disk 농도(concentration), $L$ = 파가 지난 거리, $a$ = disk 반경. → **투과 에너지의 로그가 농도 $c$에 비례**.

**3D 모델** (Boltzmann transport, Meylan et al. 1997 / Meylan & Masson 2006): single-scattering 근사로 directional spectrum $S(x,\theta)$의 advection-scattering 방정식(논문 식 9)을 각도 이산화 후 spectral method로 해.

> 출처: 1403.3766v1 §3 Theoretical model(식 3, 8, 9 본문), §5 Summary(p.16-17).

### 3.2 실험 검증 결과

농도: 저농도 array $c\approx0.38$(40 disk), 고농도 $c\approx0.77$(80 disk, 인접 disk 거의 접촉, 간격 ~10 mm).

- 투과는 파주기 증가 시 **단조증가**(거의 0 ~ 완전 투과). 고농도가 저농도보다 적게 투과.
- 2D·3D 모델이 거의 동일한 투과 예측. **다중산란(multiple scattering)이 투과에 영향 없음**을 시사(저농도·소진폭에서 산란이 지배적 감쇠원, 선형 잠재류/박판 이론 유효).
- **저농도 array**: 거의 모든 test에서 모델-데이터 우수 일치(예외: τ=0.95 s 대진폭 — overwash로 에너지 감쇠).
- **고농도 array**: τ=2 s(완전 투과)·τ≤0.95 s(강한 감쇠) 외에는 불일치. 중간주기(1.1~1.85 s)에서 모델이 투과를 최대 ~1.5배 **과대평가**.

### 3.3 모델 미포함 손실원

- **overwash**: 주기 <1 s에서 진폭 2배 시 투과 에너지 ×0.6(저농도)·×0.35(고농도)로 감소.
- **collision**(disk 간 충돌): 고농도에서만 발생(간격 ~10 mm). accelerometer로 정량화 — 중간주기에서 surge 진폭·위상차 동시 최대 → 충돌 최강. 중간주기 모델 과대평가의 주 원인. (rafting event도 관측되나 투과와 명확한 관계 없음.)

> 출처: 1403.3766v1 §4.3 Multiple disks(p.10-15), §5 결론(p.16-17).

---

## 4. SWAN obstacle 투과와의 대비

SWAN의 obstacle 투과는 sub-grid line(breakwater/dam)에 대한 **경험식 + 위상평균(phase-averaged)** 접근으로, 본 노트의 부유체 hydroelastic scattering과 근본적으로 다르다.

| | SWAN obstacle (Goda·d'Angremond) | 부유체 박판 (본 노트) |
|---|---|---|
| 구조물 | 고정 저천단 dam·breakwater(월파) | 부유 탄성판·disk(heave·surge·pitch 자유) |
| 투과 결정 | freeboard·crest width·breaker parameter $\xi_p$ 경험식 | $\|T\|^{cL/a}$, flexural rigidity $F$ 기반 선형 이론 |
| 물리 | 위상평균 에너지 감쇠 (식 2.131-2.137) | 잠재류+박판 산란(scattering) |
| 비선형 손실 | 월파·반사 경험적 흡수 | overwash·slamming·collision (모두 모델 미포함) |
| 방향성 | reflection을 여러 방향으로 diffuse 가능 | 3D Boltzmann이 directional spectrum 명시 |

SWAN 투과식 상세는 [[../../models/SWAN/manual-notes/swan-tech-ch2-obstacles-diffraction-setup]] (Goda 1967 식 2.131, d'Angremond 1996 식 2.132-2.135, freeboard reflection 식 2.136-2.137).

**핵심 대비**: 두 실험 논문 모두 **선형 모델은 저진폭·저농도에서만 유효**하고, 실제 감쇠는 overwash·slamming·collision 같은 **비선형·소산 과정**에 크게 좌우됨을 보였다. 이는 SWAN obstacle 식이 이런 과정을 경험계수로 흡수하는 이유이자, 부유식 방파제·VLFS 설계에서 위상해상([[04-code-and-tools]]) 또는 전용 hydroelastic 모델이 필요한 이유다.

---

## 미해결·source-needed

- 부유식 방파제(floating breakwater) **공학 설계식**(예: 폭/흘수 대 $K_t$ 관계, Macagno 등)은 본 두 논문 범위 밖 — 별도 출처 필요. `source-needed`.
- VLFS hydroelastic 설계 기준(예: Suzuki·Wang 리뷰)은 미인용. `source-needed`.
