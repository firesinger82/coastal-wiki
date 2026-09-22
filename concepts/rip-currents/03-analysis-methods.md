---
title: "이안류를 재는 법과 잰 것을 채점하는 법 — 관측 수단·주석 프로토콜·지표 3세대"
topic: rip-currents
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "[[01-concept]] §4 가 CV 벤치마크 4편을 **목록·계보 수준**으로 정리했다면, 본 노트는 그 **방법론 층**(무엇을 정답으로 삼고, 무엇으로 채점하는가)을 다룬다. 출처 4편 전부 arXiv full PDF 를 본 세션에 재확보해 `pdftotext` 전문 판독 후 인용: RipVIS(2504.01128v2, 18.3 MB)·YOLOv8 baseline(2504.02558v1, 21.8 MB)·RipSeg AIM2025(2508.13401v3, 1.5 MB)·RipDetSeg NTIRE2026(2604.17070v2, 17.6 MB). 인용한 문장·수식·표 값은 전부 해당 절에서 verbatim 확인했다. **한계**: (1) 네 편 모두 같은 연구 계보(RipVIS 벤치마크 기반)라 외부 반증 문헌이 없다 — 지표 설계의 타당성 자체는 본 노트가 검증하지 않았다. (2) §1 현장 관측 수단은 RipVIS §2 Related Work 의 **서술을 인용한 것**이고 원 계측 문헌(drifter·dye·laser)은 판독하지 않았다. (3) 대회 간 점수는 지표 정의가 달라 비교하지 않았다(§5 주). (4) [[02-theory]] §5 가 남긴 flash rip·shear instability **정량** 공백은 본 노트로 해소되지 않는다 — 오히려 §6 이 그 공백을 평가 쪽에서 재확인한다."
note_author: "Claude Opus 5 (1M context)"
note_date: 2026-09-22
related:
  - concepts/rip-currents/01-concept.md
  - concepts/rip-currents/02-theory.md
  - concepts/rip-currents/06-model-application.md
---

# 이안류를 재는 법과 잰 것을 채점하는 법

> [[01-concept]] §4 는 "어떤 벤치마크가 있는가" 를 정리했다.
> 이 노트는 그 앞뒤를 맡는다 — **무엇을 정답으로 삼는가**(§2–3)와
> **무엇으로 채점하는가**(§4–5). 둘 다 이안류의 물리에 묶여 있다.

## 1. 관측 수단 — 정확한 것은 드물고, 흔한 것은 부정확하다

RipVIS 는 관련 연구 개관에서 이안류 관측 수단을 네 갈래로 정리한다.[^rv-obs]

| 수단 | 성격 | 인용된 한계 |
|---|---|---|
| 육안 감시·카메라 시스템 | 전통적 | (별도 한계 서술 없음) |
| **GPS drifter·부유체** | 정밀 추적, "effective" | **비용이 크고, 위치 종속적이며, flash rip 탐지에 부적합** |
| 레이저 거리계·염료(tracer dye) 드론 | 유연·광시야 | — |
| **기계학습(영상)** | 저비용·확장 가능·실시간 | (본 노트 §2 이하가 그 대가를 다룬다) |

핵심은 **정밀 수단일수록 이안류의 본질과 어긋난다**는 것이다.
drifter 는 궤적을 정확히 주지만 **어디서 언제 생길지 알아야 놓을 수 있다.**
[[02-theory]] §3 이 정리한 유형 중 위치가 고정된 것(bathymetric·boundary-controlled)에는 맞고,
돌발적인 flash rip 에는 맞지 않는다 — 출처가 명시적으로 그렇게 적는다.[^rv-obs]

영상+ML 이 부상한 이유가 여기 있다. 싸고 넓고 상시라서지, 정확해서가 아니다.

## 2. 왜 영상 탐지가 어려운가 — 대상의 성질

RipVIS 는 고품질 자료 확보가 어려운 이유를 다섯으로 나열한다.[^rv-hard]
요지는 **이안류가 일반적인 탐지 대상의 조건을 거의 다 어긴다**는 것이다.

1. 외형이 수역·해빈 구조·기상·해저지형에 따라 크게 변한다 → 다양성 확보에 전지구적 수집이 필요
2. 일부는 육안으로 뚜렷하지만 **일부는 전문가라야 식별된다**
3. 고지대 시점이 필요하다 — 드론·타워·절벽. 그런 지점이 없는 해빈이 많다
4. 인스턴스 분할 주석에 **이안류 동역학 지식 + CV 기술**이 동시에 필요하다
5. **무정형(amorphous) 객체**다

다섯 번째가 결정적이고, 출처의 논증이 정확하다 —
불·연기도 형상이 계속 변하지만 **배경과 뚜렷이 구분된다.** 이안류는 그렇지 않다:

> *"rip currents blend seamlessly into the large water environment, often appearing as subtle
> patterns within a dynamic, constantly shifting background."*[^rv-hard]

즉 이안류 탐지는 "변하는 물체" 문제가 아니라 **"변하는 배경 속의 변하는 무늬"** 문제다.
[[01-concept]] §3 의 시각 signature(쇄파 패턴의 틈·외해 방향 퇴적물 수송)가 바로 그 무늬이고,
RipVIS 도 같은 단서로 대상을 식별했다고 밝힌다.[^rv-type]

## 3. 정답을 만드는 일 — ground truth 도 판단이다

RipVIS 의 주석 프로토콜은 이 분야에서 "정답"이 어떻게 생산되는지 보여준다.[^rv-anno]

| 항목 | 내용 |
|---|---|
| 인력 | 자원자 **30명**, 현장 교육 이수. 현장 계측 경험이 있는 **학술 전문가 2인**이 감독 |
| 기준 제시 | 전문가가 **각 영상의 첫 프레임**을 직접 주석해 일관성 기준으로 제공 |
| 검수 | 전 주석을 전문가 2인이 재검토·검증 |
| 일치도 | **Cohen's κ = 0.82** (almost perfect) |
| 재작업 | 주석된 150개 영상 중 **28개가 major revision** 필요 |
| 규모 | 수동 폴리곤 **15,784 프레임 / 25,298 인스턴스**(프레임당 평균 1.6) |
| 확장 | 중간 프레임은 **보간**으로 생성 후 전수 검증 → 163,528 프레임 |
| 표본율 | 영상 동역학에 따라 1–30 FPS, 최빈 **5 FPS**(정지 영상일수록 낮게) |

읽을 점 둘.

- **κ = 0.82 는 높지만 1 이 아니다.** 150개 중 28개(19%)가 전문가 재작업을 요했다.
  즉 **정답 자체에 판단이 들어 있다.** 모델 성능의 상한은 이 합의 수준에 묶인다.
- **정답의 대부분은 보간이다.** 수동 주석 15,784 프레임이 163,528 프레임으로 확장됐다.
  보간 구간의 "정답"은 관측이 아니라 **모델 가정**이며, 출처는 전수 검증했다고만 밝힌다.

데이터셋은 **이안류가 없는 영상 34편(48,800 프레임)**도 포함한다.[^rv-data]
오탐을 측정하려면 음성 표본이 있어야 하기 때문이고, 이것이 §4 의 지표 설계로 이어진다.

## 4. ★ 지표가 목적을 따른다 — 왜 $F_2$ 인가

표준 분할 벤치마크는 보통 mAP·F1 로 순위를 매긴다. 이안류 연구는 **$F_\beta$ 의 $\beta=2$**,
즉 재현율(recall)에 가중한 $F_2$ 를 전면에 놓는다.[^rv-f2]

$$F_\beta = \frac{(1+\beta^2)\cdot(\text{precision}\cdot\text{recall})}{\beta^2\cdot\text{precision} + \text{recall}}$$

근거는 통계가 아니라 **결과의 비대칭**이다:

> *"In a beach monitoring system, a false positive may simply disturb beachgoers, while a false
> negative could result in a potentially life-threatening situation."*[^rv-f2]

RipDetSeg 도 같은 문장을 반복한다 — *"a false positive can be a nuisance while a false negative
can potentially be deadly."*[^rd-f2]

이것은 **평가 설계가 응용 목적에서 연역된 사례**다. 같은 모델, 같은 예측이라도
F1 로 줄 세우면 1등이 바뀐다. **지표 선택은 기술적 선택이 아니라 안전 정책의 선택이다.**

RipVIS 는 여기에 후처리 하나를 더한다 — **TCA(Temporal Confidence Aggregation)**.
프레임별 신뢰도를 시간축으로 집계해 "temporal heatmap" 을 만들고, 다운샘플링·인스턴스 추적·
시간 평활·히스테리시스 임계를 거친다. 효과는 셋 — 오탐 감소(지속 증거 요구), **미탐 회복**
(일시적 잡음·가림으로 놓친 픽셀 복구), 마스크 경계 평활.[^rv-tca]
즉 **무정형 대상의 프레임별 불안정성을 시간으로 보상**하는 것이고, 단일 이미지 평가로는
드러나지 않는 이득이다.

## 5. ★ 그리고 지표는 역이용된다 — 합성 점수 3세대

$F_2$ 를 전면에 놓자마자 새 문제가 생겼다. RipSeg(AIM 2025) 주최측이 직접 적는다 —
대회 형식에서는 **오탐을 늘리는 쪽으로 $F_2$ 를 올릴 수 있다.**[^rs-score]
그래서 단일 지표를 버리고 가중 합성으로 갔다.

| 세대 | 대회/논문 | 점수 정의 | 설계 의도 |
|---|---|---|---|
| **1세대** | RipVIS (2504.01128) | IoU·AP(mAP)·F1 + **$F_2$ 강조** | 안전 비대칭 반영 |
| **2세대** | RipSeg AIM 2025 | $0.3F_1 + 0.3F_2 + 0.3\,\text{AP}_{50} + 0.1\,\text{AP}_{[50:95]}$ | **$F_2$ 단독의 게임성 차단**[^rs-score] |
| **3세대** | RipDetSeg NTIRE 2026 | $\dfrac{F_1[50] + F_1[40{:}95] + F_2[50] + F_2[40{:}95]}{4}$ | F1 의 균형 + $F_2$ 의 재현율 강조를 **IoU 축으로 확장**[^rd-score] |

3세대의 눈에 띄는 선택은 **IoU 하한을 0.40 으로 내린 것**이다
(`[40:95]` = IoU 0.40–0.95 를 0.05 간격 평균).[^rd-score]
일반적인 `[50:95]` 대신 0.40 부터 시작하는 것은 **경계가 원래 모호한 대상**에 맞춘 완화로 읽힌다 —
다만 출처는 이 하한 선택의 이유를 명시하지 않았다(`source-needed`).

평가 설계에는 부정행위 방지도 들어간다 — RipSeg 는 테스트 기간을 **2일로 제한**(수동 주석 방지),
최종 테스트 파일을 **랜덤 해시로 재명명**, 평가 코드는 처음부터 공개, 재현 코드 제출 통과 팀만 순위 인정.[^rs-fraud]

## 6. 무엇이 병목인가 — 존재보다 경계

RipDetSeg 2026 결과를 지표축으로 읽으면 병목이 한눈에 보인다(분할 트랙 1위 기준).[^rd-tab]

| 지표 | 값 |
|---|---|
| $F_2$ (IoU 0.50) | **70.61** |
| $F_1$ (IoU 0.40–0.95 평균) | 41.25 |
| $F_2$ (IoU 0.40–0.95 평균) | 42.06 |
| **최종 점수** | **55.79** |

탐지 트랙 1위도 같은 모양이다 — $F_1$ 67.86 / $F_1[40{:}95]$ 46.65 / 최종 56.33.[^rd-tab2]

**느슨한 IoU 에서 70 대, 엄격한 IoU 평균에서 40 대.** 즉 *이안류가 거기 있다*를 맞히는 일보다
*어디까지가 이안류인가*를 맞히는 일이 훨씬 어렵다. §2 의 무정형성이 숫자로 나타난 것이고,
**분할 과제가 탐지 과제보다 유의미하게 낫지 않다**(55.79 vs 56.33)는 점도 같은 방향을 가리킨다.

2세대 RipSeg 주최측의 총평도 같다 — 최상위 팀의 합성 점수가 **0.68** 에 그쳤고,
*"existing state-of-the-art models ... are not yet sufficient for robust rip current detection"*
라고 적었다.[^rs-concl]

> **주의**: 세 대회의 점수는 **지표 정의가 서로 달라 직접 비교할 수 없다.**
> 0.68(2세대)과 55.79(3세대)는 다른 양이다. 본 노트는 세대 간 성능 추이를 주장하지 않는다.

분할로의 전환 자체는 근거가 있다. YOLOv8 baseline 논문은 경계상자의 한계를 직접 든다 —
*"bounding boxes may exclude relevant parts of the rip currents while also incorporating
surrounding noise."*[^yv-bbox] 같은 연구가 정지 이미지로 학습해 **영상**으로 시험했을 때
검증 mAP50 88.94% → 시험 macro 평균 81.21% 로 떨어진 것도 함께 기록해 둘 만하다.[^yv-res]

## 7. ★ 이 벤치마크가 재지 않는 것

성능 수치를 읽을 때 반드시 함께 읽어야 할 두 가지가 있다.

**(1) 유형이 일부다.** RipVIS 는 Castelle et al. 분류를 따라
**bathymetrically-controlled**(해저 사주·수로가 만드는)와 **boundary-controlled**(잔교·방파제 가장자리)
이안류를 담고, **flash rip 과 traveling rip 은 예측 불가·일시적이라는 이유로 제외**했다.
데이터셋은 "위치가 일관되게 유지되는 안정적 이안류" 에 초점을 둔다고 명시한다.[^rv-type]

[[02-theory]] §3 의 유형 taxonomy 와 대조하면 **평가된 것은 위치가 고정된 쪽뿐**이다.
그리고 §1 에서 본 대로 drifter 역시 flash rip 에 부적합하다 —
**돌발형 이안류는 정밀 계측에서도, 영상 벤치마크에서도 빠져 있다.**
[[02-theory]] §5 가 flash rip 정량을 `source-needed` 로 남긴 공백이 이론 쪽만의 문제가 아니다.

**(2) 지역이 편중돼 있다.** RipVIS 수집지는 미국·멕시코·코스타리카·포르투갈·이탈리아·그리스·
루마니아·스리랑카·호주·뉴질랜드다.[^rv-data] **동아시아 연안은 없다.**

[[01-concept]] §5 가 한국 적용을 "탐색" 으로 남겼는데, 그 전제 조건이 여기서 분명해진다 —
한국 해빈에 기성 모델을 그대로 적용하면 **훈련 분포 밖**이다.
RipSeg 참가팀들이 domain adaptation·domain generalization·합성 데이터를 쓴 것도
이 분야의 도메인 격차가 실제 문제임을 보여준다.[^rs-concl]

## 8. 남은 것

- **원 계측 문헌 미판독** — §1 의 drifter·dye·laser 한계는 RipVIS 의 **개관 서술**을 인용한 것이다.
  정량 성능(유속 정확도·공간 해상도)은 원 문헌 확보 후. `source-needed`
- **IoU 0.40 하한의 근거** — §5. 출처가 이유를 적지 않았다. `source-needed`
- **지표 설계의 외부 검증 없음** — 인용 4편이 모두 같은 벤치마크 계보다.
  $F_2$·합성 점수가 실제 인명 안전 성과와 상관하는지를 보인 연구는 확보하지 않았다. `source-needed`
- **한국 자료 부재** — §7(2). 한국 해빈 영상·주석 자산이 있는지, KHOA·지자체 CCTV 로
  구축 가능한지는 미조사. [[01-concept]] §5 와 같은 자리.
- **flash rip 평가 공백** — §7(1). 탐지·계측 양쪽에서 빠져 있다는 **구조적 관찰**까지가
  본 노트의 범위이고, 대안 방법론은 제시하지 않았다.
- **모델 표현과의 연결 미작성** — [[06-model-application]] 이 다루는 수치모델의 이안류 재현과,
  본 노트의 영상 탐지는 아직 만나지 않았다. 모델이 낸 이안류를 영상 탐지로 검증하는 경로는 미조사.

## 출처

[^rv-obs]: RipVIS, arXiv:2504.01128v2 §2 Related Work — *"Traditional observation techniques include visual monitoring and camera-based systems. Precision tracking with GPS-equipped drifters or floating devices is effective, but costly, location-dependent, and unsuitable for flash rip detection. Newer tools, such as laser rangefinders and drones with tracer dye, offer flexibility and broader perspectives. In contrast, machine learning (ML) approaches are cost-effective, scalable, and capable of real-time detection, making rip current detection more accessible for public safety applications."*
[^rv-hard]: 同 §1 Introduction, 자료 확보 난점 1–5 — 5번 verbatim: *"Unlike objects with consistent shapes and clear boundaries, rip currents are continuously changing in shape and form, making them particularly challenging to detect. While some amorphous objects, like fire or smoke, also undergo continuous shape changes, they usually stand out distinctly from their background, making them easier to identify. In contrast, rip currents blend seamlessly into the large water environment, often appearing as subtle patterns within a dynamic, constantly shifting background."*
[^rv-data]: 同 §3.1 General Description — 184 videos / 212,328 frames(이안류 있음 150 videos·163,528 frames, 없음 **34 videos·48,800 frames**, *"allowing for both positive and negative sample training"*). 수집지: *"the USA, Mexico, Costa Rica, Portugal, Italy, Greece, Romania, Sri Lanka, Australia and New Zealand"*. 전문가가 수동 큐레이션한 train-val-test 분할을 처음 도입.
[^rv-type]: 同 §3.3 Video and Rip Current Variety — *"Following the classification of Castelle et al., RipVIS features primarily bathymetrically-controlled rip currents, which are shaped by underwater sandbars or channels, and boundary-controlled rip currents, which flow along the edges of anthropogenic structures like piers or jetties. These rip currents were identified primarily by gaps in wave-breaking patterns or offshore sediment transport. While the dataset does not include flash or traveling rip currents—due to their unpredictability and transient nature—it focuses on stable rip currents that vary in strength but remain consistent in location."* 시점 4종(water-level beachfront / elevated beachfront / aerial tilted / aerial bird's-eye)도 같은 절.
[^rv-anno]: 同 §3.4 Annotations — 자원자 30명·전문가 2인 감독·첫 프레임 전문가 주석 가이드·전수 재검토, *"achieving an inter-annotator Cohen's κ agreement of 0.82 (almost perfect agreement) on the entire dataset"*. 수동 폴리곤 15,784 프레임 / 25,298 인스턴스(프레임당 1.6), 중간 프레임 보간 후 검증 → 163,528 프레임. *"Out of the 150 annotated videos, 28 required major revisions from the experts"*. 표본율 1–30 FPS, 최빈 5 FPS.
[^rv-f2]: 同 §5.2 Evaluation Metrics — IoU·mAP·$F_\beta$ 사용, $\beta=2$ 강조. 식 (2) 가 $F_\beta$ 정의. 근거 verbatim: *"Emphasizing recall with F2 aligns with the safety-critical nature of rip current detection, as false negatives—missed detections—pose significant risks. In a beach monitoring system, a false positive may simply disturb beachgoers, while a false negative could result in a potentially life-threatening situation."* 단일 클래스 과제이므로 mAP = AP.
[^rv-tca]: 同 §4.3 Temporal Confidence Aggregation — *"a pixel-level post-processing technique aimed at improving segmentation consistency over video frames"*, 구성은 downsampling·instance tracking·temporal smoothing·hysteresis thresholding(Figure 3). 이득 3종 verbatim 요지: noise reduction(지속 증거 요구로 오탐 감소)·*"False negative mitigation: TCA also reduces false negatives by leveraging the temporal heatmap to recover pixels missed in individual frames"*·refined segmentation masks.
[^rs-score]: RipSeg(AIM 2025 Challenge Report), arXiv:2508.13401v3 §2 Challenge: Format and Ranking — *"Correct rip current identification is a safety critical task, where the F2 score is one of the relevant metrics. While F2 is useful in real-world scenarios, in a challenge format, the score can be increased by preferring an increased number of false positives. In order to mitigate this, we employed a weighted average of four relevant metrics"*, 식 (1): `score = 0.3·F1 + 0.3·F2 + 0.3·AP50 + 0.1·AP[50:95]`.
[^rs-fraud]: 同 §2 — 테스트 기간을 짧게 둔 이유 *"in order to minimize risk of fraud by manually annotating the images"*, 최종 테스트 파일은 *"renamed with a randomized hash as an extra step in preventing fraud"*, 음성 표본 파일명 규약 `RipSeg-NR-<number>`, 재현 코드·팀 설명 제출 검증 통과 팀만 최종 순위 인정, *"The evaluation code was made publicly available since the beginning, for transparency."*
[^rs-concl]: 同 §4 Conclusion and Future Work — 5개 프레임워크 참가, 전략은 *"lightweight CNNs, transformer-based architectures, domain adaptation techniques, synthetic data generation, and morphological post-processing"*. 총평 verbatim: *"even the top-performing method achieved a computed score of only 0.68. These results indicate that existing state-of-the-art models, whether directly applied or adapted through domain transfer, are not yet sufficient for robust rip current detection."*
[^rd-f2]: RipDetSeg(NTIRE 2026 Challenge Report), arXiv:2604.17070v2 §2 — *"Correctly identifying rip currents is a safety-critical task, where a false positive can be a nuisance while a false negative can potentially be deadly. Therefore, we encourage the use of the F2 score when evaluating rip current detection for real-world scenarios, to minimize false negatives."*
[^rd-score]: 同 §2, 식 (1) — `score = (F1[50] + F1[40:95] + F2[50] + F2[40:95]) / 4`. 표기 설명 verbatim: *"[50] refers to evaluation at an IoU threshold of 0.50, whereas [40:95] represents the average score over thresholds ranging from 0.40 to 0.95 with a step size of 0.05."* 의도: *"combining the assessment of F1 with the recall-oriented emphasis of F2 ... the metric reasonably reflects real-world usefulness while also promoting proper model design for the challenge."* IoU 하한을 0.50 이 아닌 0.40 으로 둔 이유는 본문에 서술되지 않았다.
[^rd-tab]: 同 Table 1 (Segmentation task, NTIRE 2026 RipDetSeg test split) — 1위 행: $F_2$ 70.61 / $F_1[40{:}95]$ 41.25 / $F_2[40{:}95]$ 42.06 / Final Score 55.79.
[^rd-tab2]: 同 Table 2 (Detection task) — 1위 행: $F_1$ 67.86 / $F_1[40{:}95]$ 46.65 / $F_2$ 65.67 / $F_2[40{:}95]$ 45.15 / Final Score 56.33.
[^yv-bbox]: YOLOv8 instance segmentation baseline, arXiv:2504.02558v1 — Figure 1 캡션 verbatim: *"This example highlights how bounding boxes may exclude relevant parts of the rip currents while also incorporating surrounding noise."* §Related Work 도 같은 취지: 기존 데이터셋·방법은 *"only produce bounding box detections at best"* 이고 그 형식상 *"either information is left out or background information is added to the detection."*
[^yv-res]: 同 Abstract — 신규 데이터셋 2,466 images(폴리곤 인스턴스 분할 주석), 드론 영상 17편 기반. 정지 이미지로 YOLOv8 학습 후 영상 시험: *"an mAP50 of 88.94% on the validation dataset and 81.21% macro average on the test dataset."*
