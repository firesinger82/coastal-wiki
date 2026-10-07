---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/Create_a_Decomp.md
lines: 34
sha256: 5c2004cd561bff276318f90cd45c5ae8d08dde9dc4928657b43bbb047775fbea
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Create_a_Decomp.md — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(metadata) — 페이지 ID(2), 제목(3), space(4), 원문 URL(5), 버전(6), 갱신 시각(7), 문서 계층 경로(8)를 기록한다. `---` 구분자를 포함한다(1·9). |
| 10–13 | Create a Decomp.inp File — `decomp.inp`는 각 하위 영역(subdomain)의 I 방향과 J 방향 폭을 지정한다(10). 다음 구간을 입력 예시로 소개한다(12). |
| 14–24 | 입력 형식 예시 — 코드 블록(code block) 구분자와 JSON 객체를 포함한다(14–23). 아래 값은 예시이다. 입력 줄 원문: `{` (15); `    "number_i_subdomains": 2,` (16); `    "number_j_subdomains": 2,` (17); `    "number_active_subdomains": 4,` (18); `    "i_subdomain_widths": [31,42],` (19); `    "j_subdomain_widths": [19,28],` (20); `    "active_flag":[1,1,1,1]` (21); `}` (22). |
| 25–34 | 입력 항목 설명 / 전체 격자 폭 — I·J 방향 하위 영역 수, 전체 하위 영역 수, 방향별 폭 배열과 활성 플래그(active flag)를 설명한다(25–32). 원문은 대부분의 경우 활성 플래그를 모두 1로 두라고 적는다(32). 각 방향 폭의 합은 해당 방향 전체 격자 폭 또는 높이와 같아야 한다(34). 예시의 전체 `IC=73` 및 `JC=47`은 `efdc.inp`의 Card 9에 해당한다고 적는다(34). 매개변수·조건 원문: ``- "`number_i_subdomains`" - this specifies the number of subdomains in the I direction`` (27); ``- "`number_j_subdomains`" - this specifies the number of subdomains in the J direction`` (28); ``- "`number_active_subdomains`" - The total subdomains is equal to the number of I subdomains times the number of J subdomains.`` (29); ``- "`i_subdomain_widths`" - Specifies the respective width in the I direction of each subdomain.`` (30); ``- "`j_subdomain_widths`" - Specifies the respective width in the J direction of each subdomain.`` (31); ``- “`active_flag` - Specifies if that sub-domain is active. For most cases just set all equal to 1.`` (32); `So the sum of the widths in each respective dimension must add up to the total grid width (or height) in each respective direction. In the example decomp.inp file shown above, this would amount to a 'global' IC=73 and JC=47 in the *efdc.inp* file (Card 9).` (34). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 18·29·32행: `number_active_subdomains`라는 항목의 설명은 I 방향 하위 영역 수와 J 방향 하위 영역 수를 곱한 전체 하위 영역 수이다. 32행은 개별 하위 영역의 활성 여부를 `active_flag`로 따로 설명한다.
- 32행: `active_flag` 앞에 여는 인용부호 `“`가 있으나 해당 줄에 대응하는 닫는 인용부호가 없다.

