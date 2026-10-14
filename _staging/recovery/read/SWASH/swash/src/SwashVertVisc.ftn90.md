---
file: models/SWASH/raw/source_code/swash/src/SwashVertVisc.ftn90
lines: 90
sha256: ef3143e489381cdeab9a8e558e7fbc202faf018d2bfe740634111101dd854500
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashVertVisc.ftn90 — 판독 구간 기록

구간은 1행부터 90행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–47 | `SwashVertVisc` 선언(1). 소속·저작권·GPL 3 이상·무보증 주석(3–27). 작성자·2011년 신규 이력(30–36). 수직 와점성(eddy viscosity) 계수 계산 목적(38–40). 수직 혼합(vertical mixing)에 표준 k–ε 모델을 쓴다는 방법 주석(42–44). 모듈 안내·빈 주석(46–47). |
| 48–69 | 시작 시 1행 SwashVertVisc 루틴 안. 통신·흐름 모듈 사용(48–50), implicit none(52). 고정 폐쇄 상수(closure constant)·분모 보정·최대 점성은 `real, parameter :: cmu = 0.09    ! closure constant for standard k-eps model` (56); `real, parameter :: eps = 1.e-8   ! small number used to prevent division by zero` (57); `real, parameter :: maxvisc = 10. ! maximal vertical viscosity` (58): cmu=0.09, eps=1.e−8, maxvisc=10. 추적 기본값 `integer, save :: ient = 0 ! number of entries in this subroutine` (62). 구조·소스 안내 주석(64–69). |
| 70–73 | 시작 시 1행 SwashVertVisc 루틴 안. `if (ltrace) call strace (ient,'SwashVertVisc')` (70)에서 strace 호출. 전체 vnu3d에 `vnu3d(:,:) = cmu * rtur(:,:,1) * rtur(:,:,1) / ( rtur(:,:,2) + eps )` (72)로 rtur의 첫 성분 제곱에 cmu를 곱한 뒤 두 번째 성분과 eps의 합으로 나눈 값을 설정한다. 빈 주석(71·73). [10-15 전수 검증 정정] |
| 74–90 | 시작 시 1행 SwashVertVisc 루틴 안. `if ( iturb == 1 ) then` (74)일 때 미해상 혼합(unresolved mixing) 배경 점성(background viscosity) 주석(76), `vnu3d = max( vnu3d, bvisc )` (78). 운동 점성(kinematic viscosity) 추가 `vnu3d = vnu3d + kinvis` (82). 최대 점성 제한(clipping) `vnu3d = min( vnu3d, maxvisc )` (86). 조건·빈 주석·루틴 종료(88–90). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 72·74–88: k–ε 점성 계산은 iturb 조건 밖에 있다. 배경 점성 하한·운동 점성 추가·maxvisc 상한은 모두 iturb=1일 때만 적용한다.
