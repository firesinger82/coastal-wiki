---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/build/distribute.bat
lines: 29
sha256: 8095e2951bae4a5e6f3d5e810a4f0a39bd8034cce8acd01ce8c881f87ec79648
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# distribute.bat — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | echo off, 인수 `%1..%4`를 SolutionDir·ConfigurationName·TargetDir·Platform으로 설정(4–7)한 뒤 따옴표 제거(10–13). |
| 15–21 | DstDir=`SolutionDir\dist\Platform\ConfigurationName`(16), SrcDir1=`src\xbeachlibrary\bin\dynamic\...`, SrcDir2=`...\bmi\...`(17–18). echo on(20). |
| 22–26 | 기존 배포 `XBeach.Library.dll`·`XBeach.BMI.dll`이 있으면 `del /q /f`(23–24), DstDir 없으면 mkdir(25). |
| 27–29 | dynamic 원본이 있으면 `xbeachlibrary_dynamic.dll`을 `XBeach.Library.dll`로, bmi 원본이 있으면 `xbeachlibrary_bmi.dll`을 `XBeach.BMI.dll`로 이름 바꾸어 copy(28–29). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·12·16–29: TargetDir를 인수에서 설정하고 따옴표를 제거하지만 배포 경로 계산·copy에는 사용하지 않는다.
- 23–24·28–29: 기존 DLL 삭제는 원본 존재 검사보다 먼저 실행된다. 원본이 없는 경우 해당 copy는 건너뛴다.
