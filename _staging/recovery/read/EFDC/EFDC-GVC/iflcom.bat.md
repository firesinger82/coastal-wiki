---
file: models/EFDC/raw/source_code/EFDC-GVC/iflcom.bat
lines: 3
sha256: 4db7006525506ef87bf467df75b8d366f38abf97d4618a07c8922058f7a3d9ad
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# iflcom.bat — 판독 구간 기록

구간은 1행부터 3행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–3 | 1행은 *.for를 대상으로 /c·/O3·/Qvms·/QxW·/Qvec_report2 옵션을 지정하여 ifort를 실행한다. 2행은 input.f를 대상으로 /c·/O1·/Qvms 옵션으로 ifort를 실행한다. 3행은 *.obj를 대상으로 ifort를 실행하여 링크(link)한다. 파일에는 조건 분기가 없다. 실행 명령 원문: `ifort /c /O3 /Qvms /QxW /Qvec_report2 *.for` (1); `ifort /c /O1 /Qvms  input.f` (2); `ifort *.obj` (3). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1–3: 소스·오브젝트(object) 대상은 경로 없는 *.for·input.f·*.obj로 지정되어 있다. 링크 대상 오브젝트를 개별 파일로 나열하는 명령은 없다.
- 1–3: 세 실행 명령 사이에 IF ERRORLEVEL 검사나 오류 시 종료 명령이 없다.
