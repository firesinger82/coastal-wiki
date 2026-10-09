---
file: models/ADCIRC/raw/source_code/adcirc/docs/introduction/what_is_adcirc.rst
lines: 85
sha256: e770ea26b4b80c5885186b1b25470530a80ea22c7f470da3ed7933e9fa518fcc
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# what_is_adcirc.rst — 판독 구간 기록

구간은 1행부터 85행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | What is ADCIRC? — 비정상 자유수면 순환과 수송(free surface circulation and transport)을 2차원과 3차원에서 푸는 프로그램 체계로 설명한다(4). 공간 유한요소법(finite element method), 비구조 격자(unstructured grid)와 병렬 최적화를 소개한다(4). |
| 6–18 | Model Features — 조석·바람 순환, 허리케인 폭풍해일(storm surge)·홍수, 파랑과 흐름의 상호작용(wave-current interaction), 준설·투기, 물질 수송, 경압 순환(baroclinic circulation)과 연안 침수·보호를 모의할 수 있다고 적는다(9–17). |
| 19–34 | ADCIRC Programs — ADCIRC, PADCIRC, ADCPREP, SWAN, ADCSWAN, PADCSWAN, PUNSWAN, ASWIP, LIBADC와 전후처리 도구의 역할을 열거한다(22–33). |
| 35–51 | System Requirements — 데스크톱부터 고성능 계산(high-performance computing) 클러스터까지 실행할 수 있으며 격자 크기·복잡도와 모의 기간에 따라 하드웨어 요구가 달라진다고 적는다(38). 운영체제, Fortran 컴파일러, 병렬 실행 시 MPI와 특정 출력 형식의 선택적 NetCDF를 안내한다(40–50). 원문: `* Fortran compiler (gfortran, Intel Fortran, etc.)` (48); `* MPI library for parallel execution` (49); `* Optional: NetCDF libraries for certain output formats` (50). |
| 52–66 | Getting Started — 설치·빌드·입력 준비·실행·출력 분석 순서를 제시한다(55–61). 시작 안내와 질문·지원 문서를 참조한다(63–65). |
| 67–80 | ADCIRC Files — 영역·경계조건(boundary conditions)·실행 매개변수를 정의하는 입력과 수위·흐름 등의 출력을 설명한다(70–79). fort.14·fort.15·fort.13과 기상·파랑 강제력(forcing) 파일을 열거한다(72–75). 원문: `* Fort.14: Grid and boundary information` (72); `* Fort.15: Model parameters and periodic boundary conditions` (73); `* Fort.13: Nodal attributes` (74); `* Additional files for meteorological forcing, wave forcing, etc.` (75). |
| 81–85 | Contributors — 저자와 개발진 정보로 ADCIRC 저장소의 README 링크를 제시한다(84). 마지막 빈 줄을 포함한다(85). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
