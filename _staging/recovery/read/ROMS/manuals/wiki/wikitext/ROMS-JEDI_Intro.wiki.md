---
file: models/ROMS/raw/manuals/wiki/wikitext/ROMS-JEDI_Intro.wiki
lines: 21
sha256: e14c6b624356fc11f8a0bf9b391e050612a577b10fd39cb6ef9cb8b453c75692
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ROMS-JEDI_Intro.wiki — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 제목·목차·그림 — 제목·정리 태그·목차와 ROMS-JEDI 로고 및 구성 도식(schematic) 참조를 포함한다(1–15). 두 그림은 로컬 파일이 없어 열지 못했다(11–12). 그림 참조: `[[Image:romsjedi_logo.png\|left]]` (11). 그림 파일 없음. 그림 참조: `[[Image:romsjedi_schematic.png\|1000px\|left]]` (12). 그림 파일 없음. |
| 16–18 | Introduction / 구조 — JEDI(Joint Effort for Data Assimilation Integration)의 자료동화(data assimilation) 목적과 모델에 독립적인 추상 구성요소(abstract building block)를 설명한다(16–17). OOPS(Object-Oriented Prediction System)의 C++ 템플릿(template), ROMS-JEDI의 Fortran 2003 객체·다형성(polymorphism)·상속(inheritance)과 양방향 언어 호출을 설명한다(17). 원문: `The Joint Effort for Data Assimilation Integration ('''JEDI''') framework is a unified, high-level, state-of-the-art data assimilation ('''DA''') system for scientific exploration and operational forecasting. The diagram above shows that the '''JEDI''' building blocks are model agnostic, and any modern geophysical numerical kernels can be interfaced. Its separable generic design and abstraction allow the implementation of various '''DA''' methodologies, including variational, ensemble, hybrid, and coupled approaches that are common to any geophysical system, without the need to develop such algorithms separately for each model. The '''JEDI''' framework is centered around the Object-Oriented Prediction System ('''OOPS''') layer classes and operators implemented in '''C++''' using templates. The specific implementations like '''ROMS-JEDI''' are written in Fortran 2003 because of the need for class objects, polymorphism, inheritance, and interoperability between '''C++''' and '''Fortran'''. The interoperability binding allows '''Fortran''' to invoke '''C++''' functions and vice versa '''C++''' to invoke '''Fortran''' procedures.` (17). |
| 19–20 | Introduction / 관측 — UFO(Unified Forward Operator)의 관측 연산자(observation operator), 상태 벡터(state vector)와의 관계 `H(x)`, 품질관리(quality control)·솎아내기(data thinning)·편향 보정(bias correction)을 설명한다(19). IODA(Interface for Observation Data Access)가 공급자 관측을 UFO·OOPS에 전달하며 동화 전과 진단 처리 중의 필터링을 설명한다(19). 원문: `The '''JEDI''' separation of concerns design allows the incorporation of diverse (current and future) observational data streams essential for any DA system. Observation operators can be efficiently coded and added to the Unified Forward Operator ('''UFO''') interface, which simulates, interpolates, and relates observable data to the model component state vector, '''H(x)'''. The '''UFO''' interface also implements quality control, data thinning, and bias correction. The Interface for Observation Data Access ('''IODA''') storage layer ingests observational data from providers into the '''UFO''' and '''OOPS''' building blocks. The immense amount of incoming data can be trimmed down, quality-controlled, and filtered by '''UFO''' operators before it is assimilated and during postprocessing when computing diagnostics, impacts, and sensitivities.` (19). |
| 21–21 | Introduction / 자료동화 방법 — 문서가 사용한다고 적은 변분(variational)·앙상블(ensemble)·혼합(hybrid) 방법을 열거한다(21). 4DVar 계열에서 ROMS의 접선 선형 모델(Tangent Linear Model, TLM)과 수반 모델(Adjoint Model, ADM)을 사용한다고 설명한다(21). 원문: `The '''ROMS-JEDI''' framework is intended for users interested in ocean prediction and data assimilation. Currently, we use the '''JEDI''' framework to incorporate physical observational data into regional '''ROMS''' applications using variational ('''3DVar'''/'''4DVar''', '''3D-FGAT'''/'''4D-FGAT'''), ensemble ('''EDA''', '''EnKF''', '''LETKF'''), and hybrid ('''3DEnVar'''/'''4DEnVar''') data assimilation methodologies. The '''ROMS''' Tangent Linear Model ('''TLM''') and Adjoint Model ('''ADM''') kernels are used in the '''4DVar''' family of algorithms.` (21). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 11행: `[[Image:romsjedi_logo.png\|left]]`의 로컬 그림 파일 없음.
- 12행: `[[Image:romsjedi_schematic.png\|1000px\|left]]`의 로컬 그림 파일 없음.
