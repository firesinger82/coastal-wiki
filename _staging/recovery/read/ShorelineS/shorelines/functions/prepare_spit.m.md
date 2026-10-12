---
file: models/ShorelineS/raw/source_code/shorelines/functions/prepare_spit.m
lines: 90
sha256: 901d2b6f24f3de90aca30aa92b49eba0a2169820aa4aaf6149b03fb5a94f47d4
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# prepare_spit.m — 판독 구간 기록

구간은 1행부터 90행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–65 | 함수 시그니처는 `function [SPIT]=prepare_spit(S)` (1). 주석은 사취(spit) 발달, 월파 퇴적(overwash), 상류측 보정(upwind correction), 전빈(shoreface)·배후 사주(back-barrier)의 수중 활성 높이(active height), 버름(berm) 높이, 조석·파랑 상호작용, 쇄파대(surf zone) 폭과 수심 갱신 시각을 설명한다(2–37). method의 'default'는 주석 설명이다(24). 이 파일에는 S 필드 기본값 대입이 없다. 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(38–65). |
| 66–78 | 로그 뒤 SPIT를 만들고 `SPIT.used=1;` (69)로 설정한다. method는 S.spitmethod에서, spitwidth·spitheadwidth·owscale·owtimescale은 같은 이름의 S 필드에서 복사한다(70–74). 주석은 owtimescale의 단위를 년으로 적는다(74). `if SPIT.owtimescale>0` (76)이면 `SPIT.owscale=0;` (77)으로 기존 월파 퇴적 비율을 끈다. |
| 79–90 | Dsf·Dbb를 S.spitdsf·S.spitdbb에서 복사한다(79–80). bheight·tideinteraction·waveinteraction·wavefile·surfwidth·bathyupdate를 같은 이름의 S 필드에서 복사한다(81–86). struct2log 호출은 주석이다(88). 빈 줄과 함수 종료를 포함한다(89–90). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12–13·79–80: 입력 주석은 Dsf·Dbb를 적는다. 실제 S 필드 이름은 spitdsf·spitdbb이다.
- 18·66–90: 입력 주석에는 surfwidthw가 있다. 본문에는 해당 필드 참조나 SPIT 필드 대입이 없다.
- 69: used는 조건 없이 1로 대입한다.
