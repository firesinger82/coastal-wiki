---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/lisflood2/sgm_fast.h
lines: 82
sha256: 0bd5f7e6f8a86ad50aa3f0dab5c413965fdb82775af3824115d743ca0ef4a79a
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# sgm_fast.h — 판독 구간 기록

구간은 1행부터 82행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | 파일명·작성일·작성자 주석(1–6), 단일 포함 지시와 lisflood2·DataTypes·강우 헤더를 포함한다(8–12). VolumeHeightUpdateInfo 구조체는 증발 손실·강우 합계·양/음 점 수원(point source) 시간단계 유량의 NUMERIC_TYPE 필드 네 개를 선언한다(14–20). 기본값 대입은 없다. 이 구간은 전처리 조건 밖이다. 원문 조건·식·지시: `#pragma once` (8). |
| 22–33 | 하위 격자 수로(subgrid channel)의 단면적/폭 SGC2_CalcA_public, 상위 격자 연결(super-grid link) 유량 SGC2_CalcLinksQ, 속도 SGC2_CalculateVelocity_public, 부하 분배 SGC2_UpdateLoadBalance를 선언한다(22–32). 포인터 입출력과 const 인수만 있으며 본문·계산식은 없다. |
| 34–74 | Fast_IterateLoop 원형 선언의 인수 목록이다(34–74). 수심·체적·유량·최대값·속도·DEM·마찰·셀 기하·범람원(floodplain) 폭·수로 배치/상태·만제수심(bankfull depth)·기상 자료·습윤/건조(wet/dry) 경계·수원·위어(weir)/교량·경로전달(routing)·연결·공통 상태·스레드 작업 배열을 받는다. 이 구간은 RESULT_CHECK 조건 밖이며 함수 실행 블록이 아니다. |
| 75–82 | 시작 시 34행 Fast_IterateLoop의 미종결 인수 목록 안. RESULT_CHECK 정의 때만 Arrptr·BCptr·채널 세그먼트·벡터 포인터 인수를 추가한다(75–80). 82행 const int verbose 인수와 세미콜론은 해당 조건 밖이다. 계산식·조건문·기본 인수는 없다. 원문 조건·식·지시: `#ifdef RESULT_CHECK` (75), `Arrays * Arrptr, // only for compare results` (76), `BoundCs * BCptr, // only for compare results` (77), `ChannelSegmentType *ChannelSegments,` (78), `vector<ChannelSegmentType> *ChannelSegmentsVecPtr,` (79), `#endif` (80). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 75–80: RESULT_CHECK 정의 유무에 따라 Fast_IterateLoop 함수 인수 목록이 달라진다. 같은 원본 디렉터리 result_check.mk:7의 컴파일 명령은 `$(CC) $(CFLAGS_RELEASE) -D _NUMERIC_MODE=1 -D RESULT_CHECK=1 -c $< -o $@`이다.
