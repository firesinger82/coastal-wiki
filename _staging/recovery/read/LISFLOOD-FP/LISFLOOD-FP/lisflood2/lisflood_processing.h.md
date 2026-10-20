---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/lisflood2/lisflood_processing.h
lines: 5
sha256: dea82e0b970700a180e454707556122f83380f30917c2180754769b0277d54e4
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# lisflood_processing.h — 판독 구간 기록

구간은 1행부터 5행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | 단일 포함 지시와 공통 lisflood.h 포함, 빈 줄을 포함한다(1–4). Fast_MainStart의 함수 원형(function prototype)은 파일·상태·매개변수·해법·경계·관측점·채널·배열·하위 격자 수로(subgrid channel)·댐 자료와 verbose를 받는다(5). 함수 본문·계산식·기본 인수·전처리 조건 분기는 없다. 원문 조건·식·지시: `#pragma once` (1), `void Fast_MainStart(Fnames *Fnameptr, Files *Fptr, States *Statesptr, Pars *Parptr, Solver *Solverptr, BoundCs *BCptr, Stage *Locptr, ChannelSegmentType *ChannelSegments, Arrays *Arrptr, SGCprams *SGCptr, vector<ChannelSegmentType> *ChannelSegmentsVecPtr, DamData *Damptr, int verbose);` (5). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
