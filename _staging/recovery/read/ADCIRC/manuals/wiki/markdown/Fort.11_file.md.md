---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.11_file.md
lines: 119
sha256: 4ee5c03f39cb246c522f20a6e4684080b736e1b2b47df143d48a8238a6065060
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.11_file.md — 판독 구간 기록

구간은 1행부터 119행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | 제목·판본 표기·빈 줄·목차를 포함한다(1–30). Fort.11 file — 경압(baroclinic) 실행에만 사용하며 경압 2DDI는 아직 지원하지 않는다고 적는다(5). 경압 3차원 실행의 `IDEN` 조건을 옮긴다(5). 원문: `The fort.11 file is only used for a baroclinic run. Baroclinic 2DDI runs are not yet supported. Baroclinic 3D runs occur if [IDEN](/index.php?title=IDEN&action=edit&redlink=1) is not equal to 0.` (5). |
| 31–36 | File Format / 2DDI — 입력의 각 줄을 변수 이름으로 표현하며 빈 줄은 가독성용이고 반복문은 여러 입력 줄을 뜻한다고 설명한다(33). 경압 2DDI 형식 절 제목을 포함한다(35). |
| 37–45 | 2DDI / IDEN = 1 or -1 — 두 헤더·`NVP`·`jki`에 따른 `DASIGT` 입력 반복 구조를 원문 그대로 옮긴다(37–44). 원문: `#### IDEN = 1 or -1[[edit](/index.php?title=Fort.11_file&action=edit&section=3)]` (37); `Header Line 1` (39); `Header Line 2` (40); `[NVP](/index.php?title=NVP&action=edit&redlink=1)` (41); `for k=1 to NVP` (42); `[jki](/index.php?title=Jki&action=edit&redlink=1),[DASIGT(jki)](/index.php?title=DASIGT(jki)&action=edit&redlink=1)` (43); `end k loop` (44). |
| 46–54 | 2DDI / IDEN = 2 or -2 — 두 헤더·`NVP`·`jki`에 따른 `DASALT` 입력 반복 구조를 원문 그대로 옮긴다(46–53). 52행의 맨 앞 작은따옴표도 유지한다. 원문: `#### IDEN = 2 or -2[[edit](/index.php?title=Fort.11_file&action=edit&section=4)]` (46); `Header Line 1` (48); `Header Line 2` (49); `NVP` (50); `for k=1 to NVP` (51); `'jki,[DASALT(jki)](/index.php?title=DASALT(jki)&action=edit&redlink=1)` (52); `end k loop` (53). |
| 55–63 | 2DDI / IDEN = 3 or -3 — 두 헤더·`NVP`·`jki`에 따른 `DATEMP` 입력 반복 구조를 원문 그대로 옮긴다(55–62). 원문: `#### IDEN = 3 or -3[[edit](/index.php?title=Fort.11_file&action=edit&section=5)]` (55); `Header Line 1` (57); `Header Line 2` (58); `NVP` (59); `for k=1 to NVP` (60); `jki,[DATEMP(jki)](/index.php?title=DATEMP(jki)&action=edit&redlink=1)` (61); `end k loop` (62). |
| 64–72 | 2DDI / IDEN = 4 or -4 — 두 헤더·`NVP`·`jki`에 따른 `DATEMP`와 `DASALT`의 입력 반복 구조를 원문 그대로 옮긴다(64–71). 원문: `#### IDEN = 4 or -4[[edit](/index.php?title=Fort.11_file&action=edit&section=6)]` (64); `Header Line 1` (66); `Header Line 2` (67); `NVP` (68); `for k=1 to NVP` (69); `jki, DATEMP(jki), DASALT(jki)` (70); `end k loop` (71). |
| 73–85 | 3D / IDEN = 1 or -1 — 두 헤더·`NVN`·`NVP`·중첩 반복문과 `SIGT(NHNN,NVNN)` 입력 구조를 원문 그대로 옮긴다(75–84). 원문: `#### IDEN = 1 or -1[[edit](/index.php?title=Fort.11_file&action=edit&section=8)]` (75); `Header Line 1` (77); `Header Line 2` (78); `[NVN](/index.php?title=NVN&action=edit&redlink=1), NVP` (79); `for k=1 to NVP` (80); `for j=1 to NVN` (81); `k, j, [SIGT(NHNN,NVNN)](/index.php?title=SIGT(NHNN,NVNN)&action=edit&redlink=1)` (82); `end j loop` (83); `end k loop` (84). |
| 86–96 | 3D / IDEN = 2 or -2 — 두 헤더·`NVN`·`NVP`·중첩 반복문과 `SAL(k,j)` 입력 구조를 원문 그대로 옮긴다(86–95). 원문: `#### IDEN = 2 or -2[[edit](/index.php?title=Fort.11_file&action=edit&section=9)]` (86); `Header Line 1` (88); `Header Line 2` (89); `NVN, NVP` (90); `for k=1 to NVP` (91); `for j=1 to NVN` (92); `k, j, [SAL(k,j)](/index.php?title=SAL(k,j)&action=edit&redlink=1)` (93); `end j loop` (94); `end k loop` (95). |
| 97–107 | 3D / IDEN = 3 or -3 — 두 헤더·`NVN`·`NVP`·중첩 반복문과 `TEMP(k,j)` 입력 구조를 원문 그대로 옮긴다(97–106). 원문: `#### IDEN = 3 or -3[[edit](/index.php?title=Fort.11_file&action=edit&section=10)]` (97); `Header Line 1` (99); `Header Line 2` (100); `NVN, NVP` (101); `for k=1 to NVP` (102); `for j=1 to NVN` (103); `k, j, [TEMP(k,j)](/index.php?title=TEMP(k,j)&action=edit&redlink=1)` (104); `end j loop` (105); `end k loop` (106). |
| 108–119 | 3D / IDEN = 4 or -4 — 두 헤더·`NVN`·`NVP`·중첩 반복문과 `TEMP(k,j)`·`SAL(k,j)` 입력 구조를 원문 그대로 옮긴다(108–117). 수직 첨자 1은 저면(bottom), `NVN`은 표면(surface)이라고 적는다(119). 원문: `#### IDEN = 4 or -4[[edit](/index.php?title=Fort.11_file&action=edit&section=11)]` (108); `Header Line 1` (110); `Header Line 2` (111); `NVN, NVP` (112); `for k=1 to NVP` (113); `for j=1 to NVN` (114); `k, j, TEMP(k,j),SAL(k,j)` (115); `end j loop` (116); `end k loop` (117); `Note: j=1 at bottom, j=NVN at surface` (119). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5·35–71: 도입부는 경압 2DDI 실행을 아직 지원하지 않는다고 적지만 뒤에는 경압 2DDI의 입력 형식을 제시한다.
- 52: 입력 예제의 `jki` 앞에 작은따옴표 하나가 있으며 대응하는 닫는 작은따옴표는 이 줄에 없다.
- 80–82: 반복 첨자는 `k`·`j`이지만 첫 3D 예제의 변수 첨자는 `NHNN`·`NVNN`이다. 이 파일은 두 첨자 쌍의 관계를 정의하지 않는다.
- 5·41·43·52·61·79·82·93·104: IDEN·NVP·jki·DASIGT(jki)·DASALT(jki)·DATEMP(jki)·NVN·SIGT(NHNN,NVNN)·SAL(k,j)·TEMP(k,j) 링크에는 `action=edit&redlink=1`이 붙어 있다.
