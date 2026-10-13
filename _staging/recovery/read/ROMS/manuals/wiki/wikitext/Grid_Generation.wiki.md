---
file: models/ROMS/raw/manuals/wiki/wikitext/Grid_Generation.wiki
lines: 30
sha256: 762b766ece82221d6f457528a3b12af88cec2f7f900682462718bbe3f730c410
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# Grid_Generation.wiki — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | Grid Generation — 변수 위치와 경계 위치를 이해해야 한다고 적는다(1–3). 그림 파일 `Whole_grid.png`를 참조하며 캡션은 없다(5). 그림 파일 없음. 본문은 두꺼운 선이 외곽 경계·벽·주기성 위치라고 설명한다(7). 계산점 수와 2의 거듭제곱 분할 조건을 옮긴다(9). 원문: `[[Image:Whole_grid.png]]` (5); `The thick lines denote the outer boundary of the grid, though some tools may draw the boundary through the rho points lying outside the box. If your domain has walls, the walls will be where the thick line is. If your domain is periodic, the periodicity is from one thick line to the next.` (7); `{{note}} Note that there are Lm by Mm computational points. If you want to create a grid that's neatly divisible by powers of 2, make sure Lm and Mm have those factors.` (9). |
| 11–25 | Grid Generation Software — ROMS에 필요한 직교 곡선 격자(orthogonal curvilinear grid) 생성 도구를 설명한다(11–12). 네 모서리를 갖는 Matlab GUI SEAGRID와 임의 개수 모서리를 갖는 C GRIDGEN을 소개한다(15–23). 원문: `A GUI-based Matlab program for creating curvilinear orthogonal grids with 4 corners <span class="red">SEAGRID</span> includes tools to create ROMS NetCDF grid files. See [[seagrid]] for more information.` (16); `A C program for creating curvilinear orthogonal grids with an arbitrary number of corners.` (20). |
| 26–30 | Bathymetry / Land/Sea Masking — 수심(bathymetry)은 기준면에서 아래쪽을 양으로 측정한다고 설명한다(26–27). 일반 적용의 양수 수심·최소 clipping 깊이와 음수 육지 수심을 쓰는 WET_DRY 조건을 옮긴다(27). 마지막은 육지/해양 마스킹(land/sea masking) 제목이다(30). 원문: `The bathymetry for ROMS is measured positive downwards, from a datum such as mean sea level (MSL). For a 'typical' ROMS application, the bathymetry would consist of all positive values. Also, for a 'typical' application, the bathymetry can not have values of 0 or any negative values. Most users would set some minimum 'clipping' depth and not allow the values of [[Variables#h\|h]] to be less than that depth. However, if an application requires land, ''i.e.'' values of [[Variables#h\|h]] that are negative, then the user is required to activate the [[Options#WET_DRY\|WET_DRY]] CPP option.` (27). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5행: `Whole_grid.png` 그림 파일 없음.
- 30행: Land/Sea Masking 제목 뒤 본문 없이 파일이 끝난다.
