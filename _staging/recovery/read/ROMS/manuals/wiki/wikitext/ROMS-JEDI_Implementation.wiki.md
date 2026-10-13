---
file: models/ROMS/raw/manuals/wiki/wikitext/ROMS-JEDI_Implementation.wiki
lines: 43
sha256: bf952361fcb54f164f263b520ed751c37f2ebc651952a82cf6856de0f2ac8f17
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ROMS-JEDI_Implementation.wiki — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | 구현 소개 — 제목·목차·정리 태그와 사전 정의된 추상 C++/Fortran 클래스(abstract class)를 구현할 때 지구물리 모델을 JEDI에 연결할 수 있다는 조건을 제시한다(1–9). 원문: `Most modern geophysical models can be connected to the '''JEDI''' framework, provided that the following predefined abstract C++/Fortran '''classes''' or '''building blocks''' are coded:` (9). |
| 11–22 | 클래스 표 / 전반 — CLASS·Description 열과 배경 오차 공분산(background error covariance)·필드(field)·격자 geometry·LETKF 순회자(iterator)·증분(increment) 클래스 행을 원문 그대로 옮긴다(11–22). 원문: `{\| border="1" cellspacing="0" cellpadding="5" align="center"` (11); `!CLASS!!Description` (12); `\|-` (13); `\|'''ErrorCovarinace''' \|\| Background error covariance, training, and modeling ('''SABER''': BUMP/NICAS) ` (14); `\|-` (15); `\| '''Field/Fields''' \|\| Elemental operators to manipulate a field or a set of fields to the model state/increment vector and metadata ` (16); `\|-` (17); `\| '''Geometry''' \|\| Application grid definition, including coordinates, metrics, parallel decomposition, and operators ` (18); `\|-` (19); `\| '''GeometryIterator''' \|\| Methods to set/get state fields over specified grid points in '''LETKF''' applications ` (20); `\|-` (21); `\| '''Increment''' \|\| Procedures to operate on the increment vector that extends/inherits from the '''Fields''' class ` (22). |
| 23–38 | 클래스 표 / 후반 — 접선 선형(tangent linear)·수반(adjoint) 모델, 변수 변환(variable change), 국소화(localization), 비선형(nonlinear) 모델, 상태(state), 궤적(trajectory) 클래스 행과 닫기 태그를 원문대로 옮긴다(23–37). 원문: `\|-` (23); `\| '''LinearModel''' \|\| Initializes, run, and finalizes Tangent Linear and Adjoint model dynamical/numerical kernels ` (24); `\|-` (25); `\| '''LinearVariableChange''' \|\| Tangent/adjoint increment vector variables transformation from one field to another ` (26); `\|-` (27); `\| '''Localization''' \|\| Model Ensemble Localization ('''SABER''': BUMP/NICAS) ` (28); `\|-` (29); `\| '''Model''' \|\| Initializes, run, and finalizes the Nonlinear model dynamical/numerical kernel ` (30); `\|-` (31); `\| '''State''' \|\| Procedures to operate on the state vector that extends/inherits from the '''Fields''' class ` (32); `\|-` (33); `\| '''Trajectory''' \|\| Methods to process the Nonlinear trajectory that linearizes the tangent linear and adjoint models ` (34); `\|-` (35); `\| '''VariableChange''' \|\| Nonlinear state vector variables transformation from one field to another ` (36); `\|}` (37). |
| 39–43 | Code Design — Geometry 클래스에서 Fortran이 C++를 호출하고 C++가 Fortran을 호출하는 양방향 상호운용(interoperability)을 설명한다(39–41). 도식 참조를 포함한다(43). 원문: `Below is a diagram showing the interoperability mechanism for the '''Geometry Class''' that allows '''Fortran''' to invoke '''C++''' function and vice versa for '''C++''' to invoke '''Fortran''' procedures.` (41). 그림 참조: `[[Image:romsjedi_implementation_schematic.png\|1000px\|left]]` (43). 그림 파일 없음. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14행: 배경 오차 공분산 클래스 이름을 `ErrorCovarinace`로 적는다.
- 43행: `[[Image:romsjedi_implementation_schematic.png\|1000px\|left]]`의 로컬 그림 파일 없음.
