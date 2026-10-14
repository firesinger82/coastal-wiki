---
file: models/SWASH/raw/source_code/swash/src/SwashLayerIntfaces.ftn90
lines: 194
sha256: 049c477d3aac5067edd650a04fc8f8fabeed8c609a5502570237f667c9ce735a
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashLayerIntfaces.ftn90 — 판독 구간 기록

구간은 1행부터 194행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–51 | `SwashLayerIntfaces` 입구와 기관·GPL 3 이상·무보증·저자·2010년 신규 및 2016년 세부 격자(subgrid) 이력(1–38). 목적은 수위점(waterlevel point)·속도점(velocity point)의 층 접면(layer interface)과 층 두께(layer thickness) 계산이다(42). 주석은 수면에서 아래로 k=0..kmax의 고정 층 수를 적는다(46–48). 접면 인덱스는 0..kmax이다(76–84). 층 두께 인덱스는 1..kmax이다(82–86). 1번 층은 접면 0과 1 사이의 최상층이다(84). [10-15 전수 검증 보완] |
| 52–73 | 시작 시 1행 루틴 안. 공통·흐름 모듈과 m_genarr의 npu를 가져온다(52–57). save ient=0·j·k·kp 선언과 구조·소스 주석을 포함한다(61–71). ltrace 조건에서 strace를 호출한다(72). 원문 조건·식·루프·호출: `integer, save :: ient = 0 ! number of entries in this subroutine` (61); `if (ltrace) call strace (ient,'SwashLayerIntfaces')` (72). |
| 74–87 | 시작 시 1행 루틴 안. zks(:,0)=-dps+hs로 수위점 수면 접면을 만들고 sigmacoor(zks,hs,mcgrd)를 호출한다(76–78). k=1..kmax에서 접면 높이 차를 hks에 넣는다(82–86). 원문 조건·식·루프·호출: `zks(:,0) = -dps(:) + hs(:)` (76); `call sigmacoor( zks, hs, mcgrd )` (78); `do k = 1, kmax` (82); `hks(:,k) = zks(:,k-1) - zks(:,k)` (84). |
| 88–104 | 시작 시 1행 루틴 안. 시간 외삽(extrapolation) humn으로 먼저 두께를 계산하며 zkum 임시 사용이라는 주석(88–89). 기존 바닥 zkum에 humn을 더한 뒤 sigmacoor를 호출한다(93–95). k 루프에서 hkumn을 접면 차로 계산한다(99–103). 원문 조건·식·루프·호출: `zkum(:,0) = zkum(:,kmax) + humn(:)` (93); `call sigmacoor( zkum, humn, mcgrd )` (95); `do k = 1, kmax` (99); `hkumn(:,k) = zkum(:,k-1) - zkum(:,k)` (101). |
| 105–123 | 시작 시 1행 루틴 안. hu·hum으로 zku·zkum 수면 접면을 만들고 sigmacoor를 두 번 호출한다(109–113). k 루프는 hu로 만든 zku의 접면 차를 hku에 넣는다(109·112·119). 같은 루프는 hum으로 만든 zkum의 접면 차를 hkum에 넣는다(110·113·120). 원문 조건·식·루프·호출: `zku (:,0) = zku (:,kmax) + hu (:)` (109); `zkum(:,0) = zkum(:,kmax) + hum(:)` (110); `call sigmacoor( zku , hu , mcgrd )` (112); `call sigmacoor( zkum, hum, mcgrd )` (113); `do k = 1, kmax` (117); `hku (:,k) = zku (:,k-1) - zku (:,k)` (119); `hkum(:,k) = zkum(:,k-1) - zkum(:,k)` (120). 이 파일은 hu와 hum의 시간 수준을 명시하지 않는다(105–120). [10-15 전수 검증 정정] |
| 124–152 | 시작 시 1행 루틴 안. .not.oned 조건에서 v점 계산을 수행한다(126). hvmn으로 임시 zkvm을 만들고 sigmacoor 후 hkvmn을 계산한다(128–136). hv·hvm으로 zkv·zkvm을 다시 만들고 sigmacoor 두 번과 hkv·hkvm 접면 차 계산을 수행한다(138–149). oned 조건을 닫는다(151). 원문 조건·식·루프·호출: `if ( .not.oned ) then` (126); `zkvm(:,0) = zkvm(:,kmax) + hvmn(:)` (128); `call sigmacoor( zkvm, hvmn, mcgrd )` (130); `do k = 1, kmax` (132); `hkvmn(:,k) = zkvm(:,k-1) - zkvm(:,k)` (134); `zkv (:,0) = zkv (:,kmax) + hv (:)` (138); `zkvm(:,0) = zkvm(:,kmax) + hvm(:)` (139); `call sigmacoor( zkv , hv , mcgrd )` (141); `call sigmacoor( zkvm, hvm, mcgrd )` (142); `do k = 1, kmax` (144); `hkv (:,k) = zkv (:,k-1) - zkv (:,k)` (146); `hkvm(:,k) = zkvm(:,k-1) - zkvm(:,k)` (147). |
| 153–194 | 시작 시 1행 루틴 안. lsubg 분기에서 압력층(pressure layer) 두께 hksc·hkuc·hkumc를 0으로 만들고 2차원이면 hkvc·hkvmc도 0으로 만든다(155–166). k=0에서 시작해 kp=1..kpmax·j=1..npu(kp)마다 k를 증가시키고 각 속도층 두께를 압력층에 누적한다(168–179). v점 누적은 .not.oned 조건이다(181–186). 루프·분기·루틴 끝을 포함한다(188–194). 원문 조건·식·루프·호출: `if ( lsubg ) then` (155); `hksc  = 0.` (157); `hkuc  = 0.` (158); `hkumc = 0.` (159); `if ( .not.oned ) then` (161); `hkvc  = 0.` (163); `hkvmc = 0.` (164); `k = 0` (168); `do kp = 1, kpmax` (170); `do j = 1, npu(kp)` (172); `k = k + 1` (174); `hksc (:,kp) = hksc (:,kp) + hks (:,k)` (176); `hkuc (:,kp) = hkuc (:,kp) + hku (:,k)` (178); `hkumc(:,kp) = hkumc(:,kp) + hkum(:,k)` (179); `if ( .not.oned ) then` (181); `hkvc (:,kp) = hkvc (:,kp) + hkv (:,k)` (183); `hkvmc(:,kp) = hkvmc(:,kp) + hkvm(:,k)` (184). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 168–190: 압력층 누적의 k는 각 npu(kp) 반복마다 증가한다. 이 블록에는 npu 합과 kmax를 비교하는 검사나 k 범위를 제한하는 조건이 없다. npu의 외부 설정은 이 파일에서 확인하지 않았다.
