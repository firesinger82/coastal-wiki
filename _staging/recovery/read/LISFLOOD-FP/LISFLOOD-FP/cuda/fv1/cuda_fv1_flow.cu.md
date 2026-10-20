---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/fv1/cuda_fv1_flow.cu
lines: 58
sha256: 99aba119d5439835b2a03b42c698de9ec69f81f41b0e904afd7909afee349754
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_fv1_flow.cu — 판독 구간 기록

구간은 1행부터 58행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | FV1 flow·기하·solver·util 헤더를 포함한다(1–4). 파일 내부 전처리 조건 분기는 없다. Flow::allocate_pinned는 수심 H·x/y 유량 HU/HV 각각에 cuda::GhostRaster::allocate_pinned를 호출한다(6–15). 고정 호스트 메모리(pinned host memory) 할당이다. |
| 17–27 | Flow::allocate_device는 H·HU·HV 각각에 cuda::GhostRaster::allocate_device를 호출한다(23–25). 장치 메모리(device memory) 할당이다. |
| 28–39 | Flow::copy는 dst·src의 H·HU·HV 세 쌍을 cuda::GhostRaster::copy로 복사한다(35–37). |
| 40–58 | Flow::free_pinned는 H·HU·HV를 cuda::free_pinned로 해제한다(45–47). Flow::free_device는 같은 세 필드를 cuda::free_device로 해제한다(55–57). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–58: 이 파일의 Flow 할당·복사·해제는 H·HU·HV만 처리한다. maxH·totalHtm·maxHtm·initHtm은 본문에 등장하지 않는다.
