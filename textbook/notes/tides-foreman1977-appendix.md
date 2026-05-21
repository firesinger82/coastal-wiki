---
title: "Foreman 1977 Manual — Appendix 분조 주파수 테이블"
source_id: tidal-heights-manual
chapter: "Appendix (구체 chapter 미식별, p.48-66)"
pages: "48-66"
page_offset_applied: false
topic: tides
canonical_source: self
citation_status: verified
verification_method: "AI programmatic cross-reference. Foreman 1977 본문(p.1-47)은 스캔 PDF로 텍스트 추출 안 됨 (보강 OCR 필요). 본 노트는 appendix(p.48-66) 추출 가능 부분만 포함."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# Foreman 1977 Appendix — 조석 분조 주파수 테이블

> Foreman, M.G.G. (1977). *Manual for Tidal Heights Analysis and Prediction.* Pacific Marine Science Report 77-10. Institute of Ocean Sciences, Patricia Bay, Sidney, B.C.

이 매뉴얼은 조석 조화분해의 **고전적 알고리즘 참조서**. t_tide (Pawlowicz et al. 2002), UTide (Codiga 2011)의 직접 조상.

## ⚠️ 추출 한계

PDF 본문(p.1-47, 알고리즘 설명·이론)은 스캔 이미지 형식으로 opendataloader-pdf fast mode가 텍스트 추출 실패. **본 노트는 appendix(p.48-66)의 분조 주파수·satellite constituent 데이터만 포함**.

본문 인용 필요 시 OCR (hybrid mode) 재실행 또는 원본 PDF 직접 확인.

## Appendix 구조

| 페이지 | 내용 |
|---|---|
| p.48-51 | **주분조 (main constituent) 주파수 테이블** — 각 분조의 cycles/hour 주파수, satellite 모기성분 |
| p.52-54 | satellite constituent 상세 (각 주분조의 부분 성분) |
| p.55-58 | 예제 입력 데이터 (Tuktoyaktuk NWT, 1976) — 위도·경도·관측값 |
| p.59-62 | satellite 보정 데이터 — Doodson 수 + 진폭 비 |
| p.63-66 | 예제 출력 (조위 시계열, 고저조 시각·높이) |

## 핵심 — 분조 주파수 (p.48-51 발췌)

Foreman 매뉴얼이 다루는 **146개 분조** 일부:

### Long Period (장기)

| 분조 | 주파수 (cph) | 주기 (h) | 분류 |
|---|---|---|---|
| Z0 | 0.0000000000 | ∞ | 평균 (DC) |
| SA | 0.0001140741 | 8765.8 | 1년 |
| SSA | 0.0002281591 | 4383.1 | 6개월 |
| MSM | 0.0013097808 | 763.5 | |
| MM | 0.0015121518 | 661.3 | 1 anomalistic month |
| MSF | 0.0028219327 | 354.4 | |
| MF | 0.0030500918 | 327.9 | fortnight |

### Diurnal (일주)

| 분조 | 주파수 (cph) | 주기 (h) |
|---|---|---|
| ALP1 | 0.0343965699 | 29.07 |
| 2Q1 | 0.0357063507 | 28.01 |
| SIG1 | 0.0359087218 | 27.85 |
| Q1 | 0.0372185026 | 26.87 |
| RHO1 | 0.0374208736 | 26.72 |
| **O1** | 0.0387306544 | **25.82** |
| TAU1 | 0.0389588136 | 25.67 |
| NO1 | 0.0402685944 | 24.83 |
| CHI1 | 0.0404709654 | 24.71 |
| PI1 | 0.0414385130 | 24.13 |
| **P1** | 0.0415525871 | **24.07** |
| S1 | 0.0416666721 | 24.00 |
| **K1** | 0.0417807462 | **23.93** |
| PSI1 | 0.0418948203 | 23.87 |
| PHI1 | 0.0420089053 | 23.80 |
| THE1 | 0.0430905270 | 23.21 |
| J1 | 0.0432928981 | 23.10 |
| 2PO1 | 0.0443745198 | 22.54 |
| SO1 | 0.0446026789 | 22.42 |
| OO1 | 0.0448308380 | 22.31 |
| UPS1 | 0.0463429898 | 21.58 |

### Semidiurnal (반일주)

| 분조 | 주파수 (cph) | 주기 (h) |
|---|---|---|
| EPS2 | 0.0761773161 | 13.13 |
| O2 | 0.0774613089 | 12.91 |
| 2N2 | 0.0774870970 | 12.91 |
| MU2 | 0.0776894680 | 12.87 |
| N2 | 0.0789992488 | 12.66 |
| NU2 | 0.0792016198 | 12.63 |
| H1 | 0.0803973266 | 12.44 |
| **M2** | 0.0805114007 | **12.4206** |
| H2 | 0.0806254748 | 12.40 |
| MKS2 | 0.0807395598 | 12.39 |
| LDA2 | 0.0818211815 | 12.22 |
| L2 | 0.0820235525 | 12.19 |
| T2 | 0.0832192592 | 12.02 |
| **S2** | 0.0833333333 | **12.0000** |
| R2 | 0.0834474074 | 11.98 |
| **K2** | 0.0835614924 | **11.97** |
| MSN2 | 0.0848454852 | 11.78 |
| ETA2 | 0.0850736443 | 11.75 |

### Higher Order (3·4·6·8차 등)

p.49-51에 M3·MK3·M4·MS4·MK4·M6·2MS6·M8·M10·M12 등 비선형(천해) 분조 다수. 천해 비선형 조석 분석에 사용.

### 검증: Stewart Table 17.2 정합

| 분조 | Stewart (h) | Foreman (cph → h) | 차이 |
|---|---|---|---|
| M₂ | 12.4206 | 1/0.0805114 = 12.4206 | 일치 |
| S₂ | 12.0000 | 1/0.0833333 = 12.0000 | 일치 |
| K₂ | 11.9673 | 1/0.0835614924 = 11.9673 | 일치 |
| K₁ | 23.9344 | 1/0.0417807462 = 23.9344 | 일치 |
| O₁ | 25.8194 | 1/0.0387306544 = 25.8194 | 일치 |
| P₁ | 24.0659 | 1/0.0415525871 = 24.0659 | 일치 |
| Mf | 327.85 | 1/0.0030500918 = 327.86 | 일치 |
| Mm | 661.31 | 1/0.0015121518 = 661.31 | 일치 |

**완전 일치** — Stewart Table 17.2와 Foreman appendix 분조 주파수 데이터는 동일 출처 (Doodson 1922 + Cartwright-Edden 1973) 추적.

## Satellite Constituent (p.60 발췌)

각 주분조는 인접 주파수의 satellite 분조 보정으로 정확도 향상. 예시 (K₁):

```
K1 1 1 0 0 0 0-0.75 10
  K1 -2 -1 0 .0 0.0002
       -1 -1 0 .75 0.0001 R1
       -1  0 0 .25 0.0007 R1
       -1  1 0 .75 0.0001 R1
        0 -2 0 .0 0.0001
        0 -1 0 .50 0.0198
   K1   0  1 0 .0 0.1356
        0  2 0 .50 0.0029
        1  0 0 .25 0.0002 R1
   K1   1  1 0 .25 0.0001 R1
```

해석:
- 첫 줄: 주분조 K1, Doodson 수 (1, 1, 0, 0, 0, 0), 위상 -0.75 (×π?), satellite 수 = 10
- 후속: 각 satellite의 Doodson 수 오프셋 + 위상 + 진폭 비
- R1 표시: rare 또는 special 분류

이 데이터는 nodal correction과 satellite admittance 계산에 사용 (UTide·t_tide의 핵심 입력).

## 예제 데이터 (p.55, p.64-66)

매뉴얼은 **Tuktoyaktuk NWT (캐나다 북서)** 1976년 조위 관측을 예제로 사용:

```
M10 M8 8 16060775 14090975 6485 TUKTOYUKTUK NWT MST 6927 3302
```

- 위도 6927 = 69°27'N
- 경도 3302 = 어떤 표기 (m'lat lon)
- 관측 시간대: MST (Mountain Standard Time)
- M10·M8: 분조 차수 옵션

조위 데이터 (p.64): 시간별 8개 컬럼 × N일 형식.

## 인용 가능 항목

- ✓ 분조 주파수·주기 (각 cph 값)
- ✓ satellite Doodson 수 + 진폭 비
- ✓ 예제 데이터 형식
- ✗ 본문 알고리즘 설명 (OCR 필요)
- ✗ 시계열 길이 권고, Rayleigh criterion
- ✗ nodal correction 수식

## 보강 작업 (priority)

1. **OCR 재변환** — `opendataloader-pdf --hybrid --ocr en`으로 본문 p.1-47 추출 (시간 10-30분, 별도 백그라운드)
2. 또는 원본 PDF 직접 읽고 페이지별 수동 노트
3. Pawlowicz et al. (2002) t_tide 논문 — Foreman 알고리즘의 Modern Python/MATLAB 구현 설명

## 연결

- `concepts/tides/02-theory.md` §4 분조 — Stewart Table 17.2와 본 데이터 정합
- `concepts/tides/03-analysis-methods.md` — 본 매뉴얼이 알고리즘의 canonical 출처
- `concepts/tides/04-code-and-tools.md` (미작성) — UTide / t_tide / pytides 실제 구현
