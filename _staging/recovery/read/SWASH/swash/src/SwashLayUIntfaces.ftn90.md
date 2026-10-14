---
file: models/SWASH/raw/source_code/swash/src/SwashLayUIntfaces.ftn90
lines: 120
sha256: ba49b1f9149182ec912ed35c1ac4ba05ed2d57dc3e3dd997627a4f4a83606ea2
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashLayUIntfaces.ftn90 — 판독 구간 기록

구간은 1행부터 120행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–49 | `SwashLayUIntfaces` 입구와 기관·GPL 3 이상·무보증·저자·2020년 신규 이력(1–36). 목적은 비정형 격자(unstructured mesh)의 수위점(waterlevel point)·속도점(velocity point) 층 접면(layer interface) 위치와 층 두께(layer thickness) 계산이다(40). 주석은 수면에서 아래로 k=0..kmax의 고정 층 수를 쓴다고 적는다(44–46). 접면 인덱스는 0..kmax이다(72–80). 층 두께 인덱스는 1..kmax이다(78–82). 1번 층은 접면 0과 1 사이의 최상층이다(80). [10-15 전수 검증 보완] |
| 50–69 | 시작 시 1행 루틴 안. 공통·흐름·격자 모듈에서 ncells·nfaces를 가져오고 implicit none을 선언한다(50–55). 지역변수는 save ient=0·k이다(59–60). 구조·소스 주석과 ltrace 조건의 strace 호출을 포함한다(62–68). 원문 조건·식·루프·호출: `integer, save :: ient = 0 ! number of entries in this subroutine` (59); `if (ltrace) call strace (ient,'SwashLayUIntfaces')` (68). |
| 70–83 | 시작 시 1행 루틴 안. 수위점 수면 접면은 -dps+hs이다(72). sigmacoor에 zks·hs·ncells를 넘긴다(74). k=1..kmax에서 접면 높이 차로 hks를 계산한다(78–82). 원문 조건·식·루프·호출: `zks(:,0) = -dps(:) + hs(:)` (72); `call sigmacoor( zks, hs, ncells )` (74); `do k = 1, kmax` (78); `hks(:,k) = zks(:,k-1) - zks(:,k)` (80). |
| 84–100 | 시작 시 1행 루틴 안. 주석은 시간 외삽(extrapolation) 수심 humn으로 먼저 두께를 계산하고 zkum을 임시 사용한다고 적는다(84–85). 기존 바닥 zkum에 humn을 더해 0번 접면을 만들고 sigmacoor를 nfaces 크기로 호출한다(89–91). k 루프에서 hkumn을 접면 차로 계산한다(95–99). 원문 조건·식·루프·호출: `zkum(:,0) = zkum(:,kmax) + humn(:)` (89); `call sigmacoor( zkum, humn, nfaces )` (91); `do k = 1, kmax` (95); `hkumn(:,k) = zkum(:,k-1) - zkum(:,k)` (97). |
| 101–120 | 시작 시 1행 루틴 안. hu·hum으로 zku·zkum의 0번 접면을 설정한다(105–106). 두 sigmacoor 호출은 nfaces를 쓴다(108–109). k=1..kmax에서 hku·hkum을 계산한다(113–118). 끝 주석과 루틴 종료를 포함한다(119–120). 원문 조건·식·루프·호출: `zku (:,0) = zku (:,kmax) + hu (:)` (105); `zkum(:,0) = zkum(:,kmax) + hum(:)` (106); `call sigmacoor( zku , hu , nfaces )` (108); `call sigmacoor( zkum, hum, nfaces )` (109); `do k = 1, kmax` (113); `hku (:,k) = zku (:,k-1) - zku (:,k)` (115); `hkum(:,k) = zkum(:,k-1) - zkum(:,k)` (116). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
