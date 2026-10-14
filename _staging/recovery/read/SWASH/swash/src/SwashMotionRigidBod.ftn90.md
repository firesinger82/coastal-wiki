---
file: models/SWASH/raw/source_code/swash/src/SwashMotionRigidBod.ftn90
lines: 160
sha256: ff42594c0eb529475b82f79c0ad3a93d99a67d27f2f9244e8f96c41c6e987c08
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashMotionRigidBod.ftn90 — 판독 구간 기록

구간은 1행부터 160행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–51 | `SwashMotionRigidBod` 시작(1).기관·SWASH 비정수압(non-hydrostatic) 파랑·흐름 모델·2010–2026 저작권·GPL 3 이상·무보증 주석(3–27). 저자·2022년 신설 이력(30–36). 부유 강체(floating rigid body)의 운동 방정식을 푸는 목적(38–40). 선형·각운동량 보존의 힘·토크 균형, 상미분방정식(ordinary differential equation)을 일반화 알파(generalized-alpha) 방법으로 적분한다는 주석(44–47). 특수 경우로 비소산 Newmark(1959), SWASH 기본값으로 2차 소산 Chung–Hulbert(1993) 방법을 설명한다(49–50). |
| 52–79 | 시작 시 1행 SwashMotionRigidBod 루틴 안. ocpcomm4·SwashCommdata3·SwashTimecomm의 dt·SwashRigBoddata 사용(54–57), implicit none(59). 저장 진입 횟수 ient=0, 반복 인덱스 m/n, 보조 가속도 accu·완화 계수(under-relaxation factor) alfa·일반화 알파 계수 beta/gamma·이전/현재 힘 f0/f1 선언(63–72). 구조·의사코드·Source text 머리말 및 빈 줄(74–79). 선언 초기값은 `integer, save :: ient = 0 ! number of entries in this subroutine`이다(63). [10-15 전수 검증 보완] |
| 80–91 | 시작 시 1행 루틴 안. `if (ltrace) call strace (ient,'SwashMotionRigidBod')` (80). 이동 강체가 아니면 `if ( ifloat /= 2 ) return` (84). 완화 계수 대입은 `alfa  = pship(10)`이다(86). 일반화 알파 계수 대입은 `beta  = pship( 3)` (87), `gamma = pship( 4)` (88)이다. 병진 운동(translational motion) 머리말(90–91). [10-15 전수 검증 보완] |
| 92–124 | 시작 시 1행 루틴 안. `do n = 1, ndim` (92)·`do m = 1, mbod` (94)에서 `if ( .not.bdof(m,n,1) ) cycle` (96)로 비활성 병진 자유도(degree of freedom)를 건너뛴다. 질량당 전체 힘은 `f0 = ( fhyd0(m,n) + fbod0(m,n) ) / bmass(m)` (100), `f1 = ( fhyd1(m,n) + fbod1(m,n) ) / bmass(m)` (101). `accu = afot1(m,n)`으로 직전 반복의 병진 가속도를 저장한다(105). `afot1(m,n) = ( -alfam * afot0(m,n) + alfaf * f0 + (1.-alfaf) * f1 ) / (1.-alfam)` (109), `afot1(m,n) = alfa * afot1(m,n) + (1.-alfa) * accu` (113). 완화된 가속도로 `vfot1(m,n) = vfot0(m,n) + dt * ( gamma * afot1(m,n) + (1.-gamma) * afot0(m,n) )` (117), `xfot1(m,n) = xfot0(m,n) + dt * ( vfot0(m,n) + dt * ( beta * afot1(m,n) + (0.5-beta) * afot0(m,n) ) )` (119). 두 루프 종료·구분 주석(121–124). [10-15 전수 검증 보완] |
| 125–160 | 시작 시 1행 루틴 안. 회전 운동(rotational motion) 머리말(125–126). `do n = 1, ndim` (127)·`do m = 1, mbod` (129)에서 `if ( .not.bdof(m,n,2) ) cycle` (131). 관성모멘트(moment of inertia)당 토크는 `f0 = ( thyd0(m,n) + tbod0(m,n) ) / bmoi(m,n)` (135), `f1 = ( thyd1(m,n) + tbod1(m,n) ) / bmoi(m,n)` (136). `accu = afor1(m,n)`으로 직전 반복의 회전 가속도를 저장한다(138–140). `afor1(m,n) = ( -alfam * afor0(m,n) + alfaf * f0 + (1.-alfaf) * f1 ) / (1.-alfam)` (144), `afor1(m,n) = alfa * afor1(m,n) + (1.-alfa) * accu` (148). `vfor1(m,n) = vfor0(m,n) + dt * ( gamma * afor1(m,n) + (1.-gamma) * afor0(m,n) )` (152), `xfor1(m,n) = xfor0(m,n) + dt * ( vfor0(m,n) + dt * ( beta * afor1(m,n) + (0.5-beta) * afor0(m,n) ) )` (154). 두 루프·루틴 종료(156–160). [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 100–109·135–144: bmass·bmoi·1−alfam을 분모에 사용한다. 이 루틴에는 해당 분모의 영 여부를 검사하는 조건이 없다.
- 96·131: 비활성 병진·회전 자유도는 cycle로 건너뛴다. 해당 자유도의 가속도·속도·변위를 초기화하는 대입은 이 루틴에 없다.
