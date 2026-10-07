---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Operating_System_and_Hardware_Compatibility.md
lines: 69
sha256: 0325662321bed8b406d327bb5d8548185fee833f50a7d0234800aa890134cf92
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Operating_System_and_Hardware_Compatibility.md — 판독 구간 기록

구간은 1행부터 69행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 문서 메타데이터와 적용 범위 — OS 및 하드웨어 호환성 페이지의 ID, URL, 버전, 갱신 시각, 계층을 포함한다(1–9). 개발사가 테스트하고 정기적으로 사용하는 시스템이며 정보는 최신 EEMS 버전에 관한 것이라고 적는다(10–12). 이 판독은 저장된 원문을 대상으로 한다. |
| 14–30 | EFDC+ Explorer / Minimum Required Specification — OS·소수점 지역 설정·프레임워크·CPU·메모리의 요구조건 원문: `**Operating Systems:** 64-bit Windows operating systems. Windows 7, Windows 10, and Windows Server (2012-2019). Note that Windows 8 and 8.1 are no longer supported. ` (18) `**Regional Settings:** The decimal symbol must be a period or full stop (.), not a comma (,) ` (20) `**Target framework:** .NetFramework v4.7.2` (22) `**CPU**: Any modern x86-64 or AMD64 CPU` (24) `**Memory:** 4GiB DDR4` (26) Apple Mac과 가상 머신(Virtual Machines)에서 Windows OS를 이용하는 실행 조건 원문: `- EE10 can run on Apple Mac computers running the Windows OS` (28) `- EE10 can be run on Virtual Machines running the Windows OS` (29) |
| 31–40 | EFDC+ Explorer / DSI Specification — 내부에서 정기적으로 사용하는 시스템을 소개한다(31–33). OS·CPU·메모리 사양 원문: `**Operating Systems:** 64-bit Windows operating systems. Windows 10 Pro, and Windows Server (2012-2019).` (35) `**CPU**: Intel i7, i9, & Xeon CPUs. AMD Zen2 CPUs (Epyc & Ryzen).` (37) `**Memory:** 16GiB DDR4` (39) |
| 41–54 | EFDC+ / Minimum Required Specification — EFDC+의 Windows·Linux, 프레임워크, CPU, 메모리 요구조건을 적는다(41–51). 사양·Linux용 별도 실행파일 조건 원문: `**Operating Systems:** Windows or Linux\* operating systems. Windows 7, Windows 10, and Windows Server (2012-2019). Note that Windows 8 and 8.1 are no longer supported. ` (45) `**Target framework:** .NetFramework v4.7.2` (47) `**CPU**: Any modern x86-64 or AMD64 CPU` (49) `**Memory:** 4GiB DDR4` (51) `*\* Running EFDC+ on Linux requires a separate executable compiled for Linux systems.*` (53) |
| 55–64 | EFDC+ / DSI Specification — 내부에서 정기적으로 쓰는 Windows·CentOS·Redhat·Ubuntu와 CPU·메모리 사양을 적는다(55–63). 원문: `**Operating Systems:** Windows 10 Pro, Windows Server (2012-2019), CentOS, Redhat, Ubuntu. ` (59) `**CPU**: Intel i7, i9, & Xeon CPUs. AMD Zen2 CPUs (Epyc & Ryzen).` (61) `**Memory:** 8-16GiB DDR4` (63) |
| 65–69 | Cloud Computing — 제목, 공백이 있는 행, 빈 줄을 포함한다(65–68). EFDC+가 Amazon AWS 등 클라우드 컴퓨팅 서비스에서 실행될 수 있다고 적는다(69). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행: 색상 CSS가 본문 시작에 남아 있다.
- 12·28–29행: 적용 범위는 최신 EEMS 버전이라고 적지만 Mac·가상 머신 설명의 제품 표기는 `EE10`이다. 최신 버전 번호는 이 파일에 명시되지 않았다.

