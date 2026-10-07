---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_11B.md
lines: 28
sha256: b838fa6bb102a802e859a3fc9a8d2b77baa43717bf9a1a726f2b7f3b961a88de
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_11B.md — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(metadata) — 페이지 ID(2), 제목(3), space(4), 원문 URL(5), 버전(6), 갱신 시각(7), 문서 계층 경로(8)를 기록한다. `---` 구분자를 포함한다(1·9). |
| 10–24 | C11B CORNER CELL BOTTOM STRESS CORRECTION OPTIONS (2TL ONLY) — 모서리 셀(corner cell)의 저면 응력(bottom stress) 보정을 두 시간 레벨 방식에서만 사용하는 것으로 제목에 적는다(10). `ISCORTBC`의 1·2 옵션, 사용하지 않는다고 적힌 진단 출력 옵션, 보정 계수의 원문 범위·0과 1의 의미·권장 0.5를 설명한다(14–22). 원문 범위의 `GE`를 `LE`로 바꾸지 않았다. 제목·매개변수·조건·권장값 원문: `C11B CORNER CELL BOTTOM STRESS CORRECTION OPTIONS (2TL ONLY)` (10); `\* ISCORTBC: 1 TO CORRECT BED STRESS AVERAGING TO CELL CENTERS IN CORNERS` (14); `\*                     2 TO USE SPATIALLY VARYING CORRECTION FOR CELLS IN CORNERC.INP` (16); `\* ISCORTBCD: 1 WRITE DIAGNOSTICS EVERY NSPTC TIME STEPS (NOT USED)` (18); `\* FSCORTBC: CORRECTION FACTOR, 0.0 GE FSCORTBC LE 1.0` (20); `\*                      1.0 = NO CORRECTION, 0.0 = MAXIMUM CORRECTION, 0.5 SUGGESTED` (22). 주석용 `\*` 줄과 빈 줄을 포함한다. |
| 25–28 | C11B / 입력 예시 — 세 매개변수의 헤더와 모두 0인 입력 예시를 적는다(26·28). 예시를 기본값으로 표시하지 않았다. 입력 줄 원문: `C11B ISCORTBC ISCORTBCD FSCORTBC` (26); `              0                  0                    0` (28). 앞뒤 빈 줄을 포함한다(25·27). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 18행: 진단 주기를 `NSPTC TIME STEPS`로 적는다. 이 파일에는 `NSPTC`의 정의나 값이 없다.
- 20·22행: 범위 표기는 `0.0 GE FSCORTBC LE 1.0`이다. 다음 설명은 `1.0 = NO CORRECTION, 0.0 = MAXIMUM CORRECTION, 0.5 SUGGESTED`를 적는다.

