---
file: models/ROMS/raw/manuals/wiki/wikitext/Jwtype.wiki
lines: 34
sha256: 9f93c18dc61b0fe054c97ed123b9f25aecfa7adf0abe3cf8899fe3c3bfa2b6f7
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# Jwtype.wiki — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Jwtype — Variables의 Jwtype 포함 지시문이 있다(1–2). 단파 흡수(shortwave absorption)의 이중 지수(double exponential) 계수를 고르는 매개변수라고 설명한다(6). WTYPE의 1–5와 Jerlov 수형(water type) I·IA·IB·II·III 대응을 옮긴다(8). 원문: `{{#lst:Variables\|Jwtype}}` (2); `<span class="blue">WTYPE</span> ([[roms.in]]) values 1 through 5 correspond to Jerlov's classification of water types  I, IA, IB, II and III, respectively.` (8). |
| 10–26 | 태양 복사 하향 플럭스 — Qdown(z) 식을 제시한다(10–12). 표면 하향 단파 입력 또는 해석적 값이 필요하고 lmd_swfrac.F에서 사용한다고 설명한다(14). mod_scalars.F의 lmd_mu1/lmd_mu2 흡수 계수 역수와 m 단위·lmd_r1 복사 비율 정의를 옮긴다(16–25). 원문: `where <math>Q_sw</math> is the downward shortwave radiation at the sea surface. This parameterization is implemented in [[lmd_swfrac.F]] if called for. Downward shortwave data (or an analytical value) is required as input. ` (14); `    [[Variables#lmd_mu1\|lmd_mu1]]     Reciprocal of the absorption coefficient for solar` (18); `                wavelength band 1 as a function of the Jerlov` (19); `                water type. Units are meters.` (20); `    [[Variables#lmd_mu2\|lmd_mu2]]     Reciprocal of the absorption coefficient for solar` (21); `                wavelength band 2 as a function of the Jerlov` (22); `                water type. Units are meters.` (23); `    [[Variables#lmd_r1\|lmd_r1]]      Fraction of total radiance for wavelength band 1 as` (24); `                a function of the Jerlov water type.` (25). LaTeX 원문: `Q_{down}(z) = Q_{sw}( r \, \exp(z/\mu_1) + (1-r) \, \exp(z/\mu_2) )` (12); `Q_sw` (14). |
| 27–34 | 계수 값 — WTYPE 1–5의 Jerlov 분류와 lmd_mu1·lmd_mu2·lmd_r1의 각 열 수치를 원문 순서대로 옮긴다(27–34). 원문: `     [[Variables#Jwtype\|WTYPE]]                1       2       3       4       5` (29); `     Jerlov water type :  I       IA      IB      II     III` (30); `    &nbsp;` (31); `      [[Variables#lmd_mu1\|lmd_mu1]]            0.35 ,  0.60 ,  1.00 ,  1.50 ,  1.40  ` (32); `      [[Variables#lmd_mu2\|lmd_mu2]]           23.00 , 20.00 , 17.00 , 14.00 ,  7.90  ` (33); `      [[Variables#lmd_r1\|lmd_r1]]             0.58 ,  0.62 ,  0.67 ,  0.77 ,  0.78` (34). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 2행: Variables의 Jwtype 포함 대상 본문은 이 파일에 없다.
- 12·14행: 표면 단파 기호는 식에서 `Q_{sw}`, 설명 LaTeX에서 `Q_sw`로 적혀 있다.
