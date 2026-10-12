---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_wave_fields_from_mat.m
lines: 48
sha256: 9a779694c6a289a9400abc6f9b5dca1e9b3dc1b4de1493a4ff62f831d4d0e984
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_wave_fields_from_mat.m — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | 함수 시그니처는 `function [ xg,yg,Hg_all,phiwg_all,dirtab,Tptab,Hstab ] = get_wave_fields_from_mat( fname )` (1). 파고(wave height)·파향(wave direction)·파주기(wave period) 조건별 파랑장(wave field) 변환 행렬(transformation matrix)을 설명한다(2–12). 주석은 jonswaptable.txt·XBeach·xboutput.nc를 언급한다(7–9). 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(13–40). |
| 41–48 | 시작 시 1행 get_wave_fields_from_mat 함수 안. 파랑 모델 결과가 생성되었다고 가정한다는 주석을 적는다(41–42). 파일 적재 호출은 `load(fname)` (43). `if isempty(Hstab)` (44)이면 파고 표 기본값은 `Hstab=[1]` (45). 분기·함수 종료와 마지막 빈 줄을 포함한다(46–48). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–9·43: 주석은 XBeach의 xboutput.nc 판독을 설명한다. 실행문은 fname의 load 호출이다.
- 43–45: Hstab 처리 조건은 isempty(Hstab)이다. 적재 파일에 Hstab 변수가 존재하는지 검사하는 문장은 없다.
