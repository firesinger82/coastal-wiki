---
file: models/ROMS/raw/manuals/wiki/wikitext/GLS_MIXING.wiki
lines: 19
sha256: 7b7a82ba0f41ac6b50f7dfd95dbbbaded545cac17c938a07ff794764295879fd
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# GLS_MIXING.wiki — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Generic Length Scale vertical mixing parameterization — Options에서 GLS_MIXING 절을 포함하는 지시문을 제시한다(1–2). 더 자세한 설명을 앞으로 쓸 것이라는 Wilkin의 작성 메모를 포함한다(4). 다음 CPP 옵션이 일반 길이 척도(Generic Length Scale, GLS)의 수직 난류 폐합(vertical turbulence closure) 구성을 바꾼다고 적는다(6). 원문: `{{#lst:Options\|GLS_MIXING}}` (2); `Wilkin: Here we would write a more verbose description of the GLS scheme (but not a full algorithm/science description). Basically just enough to help a user with a meaningful choice among the following suboptions:` (4); `The following CPP options modify the configuration of the Generic Length-Scale vertical turbulence closure:` (6). |
| 8–19 | 하위 옵션과 폐합 선택 — CPP 옵션 이름을 옮긴다(8–15). roms.in 매개변수가 k-kl·k-ε·k-ω 폐합 선택을 결정한다고 적는다(17). 상위 문서는 Vertical Turbulence Closure이다(19). 원문: `[[CANUTO_A]]` (8); `[[CANUTO_B]]` (9); `[[CHARNOK]]` (10); `[[CRAIG_BANNER]]` (11); `[[KANTHA_CLAYSON]]` (12); `[[K_C2ADVECTION]]` (13); `[[K_C4ADVECTION]]` (14); `[[N2S2_HORAVG]]` (15); `There are parameters in [[roms.in]] that determine whether [[GLS_MIXING]] implements the turbulence closure options of ''k-kl'', k-&epsilon; or k-&omega;.` (17); `Parents: [[Vertical Turbulence Closure]]` (19). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 2행: `{{#lst:Options|GLS_MIXING}}`의 포함 대상 본문은 이 파일에 없다.
- 4행: GLS 설명을 앞으로 작성하겠다는 메모가 남아 있다.
- 17행: 폐합을 선택하는 roms.in 매개변수의 이름·값은 이 파일에 제시되지 않는다.
