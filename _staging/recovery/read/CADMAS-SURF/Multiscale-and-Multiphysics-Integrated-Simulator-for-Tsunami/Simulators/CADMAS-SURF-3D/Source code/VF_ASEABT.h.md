---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/VF_ASEABT.h
lines: 3
sha256: ad9f9f225391bc2d8865fa76748979546129b4b66ffdc1ef2dcb9d6e2c12b616
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_ASEABT.h — 판독 구간 기록

구간은 1행부터 3행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–3 | 정수 ISEABT와 COMMON/VF_ASEABI/ISEABT를 선언한다. 1행 인라인 주석의 “地形変化考慮せず”는 지형 변화 미고려, “地形変化考慮”는 지형 변화 고려를 뜻한다. 주석은 0·1의 의미이며 실제 초기값 대입은 없다. 원문: `      INTEGER :: ISEABT        ! =0 地形変化考慮せず =1 地形変化考慮` (1) (0은 지형 변화 미고려, 1은 지형 변화 고려); `      COMMON/VF_ASEABI/ISEABT` (3). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 3: COMMON 이름은 파일명 VF_ASEABT와 다른 VF_ASEABI이다.
