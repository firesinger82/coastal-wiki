---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/SedTrans_Pass3_old_wgsl.md
lines: 19
sha256: 95dbbc5116c4382c1988ae979f27fcfa395c763fbabfbabfe266a40ae618e018
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# SedTrans_Pass3_old_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/SedTrans_Pass3_old.wgsl`

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 원문 링크와 구형 퇴적물 갱신이다(1–7). `SedTrans_Pass3.wgsl`과 비슷하나 새 소류사 경사 처리가 없고 침식/퇴적 스케일이 약간 다르다(7). 현재 주 경로는 이 파일이 아닌 `SedTrans_Pass3.wgsl`을 가져와 실행한다(11). [11-04 전수 검증 정정] |
| 13–19 | 후기 소류사 추가 전 부유사 발생항·마찰/전단의 변화를 이해하는 문맥 자료다(15). 실행 동작을 바꾸려면 `main.js` 선택도 바꿔야 한다고 적는다(19). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11: 문서는 이 파일을 현재 비활성 구형 변형으로 구분한다.
