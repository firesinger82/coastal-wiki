---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/spaceparamsdef.F90
lines: 61
sha256: 55e083d7b10e36da434e9c5e752b0603cf20c7aa6a639fab267a6af9031803b0
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# spaceparamsdef.F90 — 판독 구간 기록

구간은 1행부터 61행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | `spaceparamsdef` 모듈 선언, `mnemmodule` 사용, `implicit none`·`save`. `spacepars` 형을 열고 `spacedecl.inc`(6)를 포함한다. include 내부 선언은 이 파일 본문에 없다. |
| 7–31 | `spacepars` 형 안에서 `#ifdef USEMPI`(7)를 연다. 주석은 process p=0..numprocs-1과 배열 p+1의 대응, local b(1,1)와 global a(is(p+1),js(p+1))의 대응(16), 크기 lm/ln(19) 및 전역 slice(21), left/right/top/bot의 외곽 뜻(23–28)을 설명한다. 값은 `space_distribute_space`에서 결정된다고 명시(30). |
| 32–40 | 구간 시작 시 `spacepars` 형과 USEMPI 전처리 영역 내부. 분할 시작 is/js, 크기 lm/ln의 integer 포인터 및 네 외곽 여부 logical 포인터를 모두 `=> NULL()`로 선언(32–39). |
| 41–56 | 같은 형과 USEMPI 영역 내부. 전역 계산범위 icgs/icge/jcgs/jcge와 지역 계산범위 icls/icle/jcls/jcle를 allocatable로 선언(42–49). `logical, dimension(numvars) :: collected`(51), `logical, dimension(numvars) :: precollected`(52)는 이 선언에서 초기값 없음. 54에서 USEMPI, 55에서 형 종료. |
| 57–61 | 형과 USEMPI 영역 밖. ee/uu/vv/zs 계산범위의 i/j min/max 정수 16개를 public으로 선언(57–60)하며 초기값 없음. 모듈 종료(61). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 51–52: collected/precollected 선언에는 초기값이 없다. 이 파일에는 초기화 실행문이 없다.
- 57–60: public 계산범위 정수 선언에도 초기값이 없다.
