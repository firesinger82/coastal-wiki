---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/oyster_floats_mod.h
lines: 260
sha256: 4e80e7d4e2f8ab11bf3523610f1a91f23dfdbf34461bbd55c83c73b1f8fe8b52
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# oyster_floats_mod.h — 판독 구간 기록

구간은 1행부터 260행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–43 | 시작 시 열린 전처리 조건 없음. `mod_behavior`를 선언한다(1). 저작권·MIT/X 라이선스·참고문헌·구분 주석과 빈 줄을 포함한다(2–43). 굴 유생(oyster larva)의 성장률(growth rate)·초기 길이·먹이(food)·정착(settlement) 크기와 탁도(turbidity)·유영(swimming)·침강(sinking) 매개변수를 설명한다(13–42). 먹이 단위는 mg Carbon/l이다(15). |
| 44–78 | 시작 시 열린 전처리 조건 없음. 시작 시 1행 mod_behavior 안. 주석은 유영 표의 온도 I축과 크기 J축을 설명한다(44–53). 성장 계수 표는 염분 I축·온도 J축, 성장률 표는 먹이 I축·크기 J축으로 설명한다(55–75). 주석·구분선·빈 줄을 포함한다(76–78). |
| 79–138 | 시작 시 열린 전처리 조건 없음. 시작 시 1행 mod_behavior 안. mod_param·implicit none을 사용한다(79–81). 세 조회표(lookup table)의 크기·시작값·간격을 스칼라로 선언한다(85–107). 성장·초기 길이·먹이·정착·침강·유영·탁도 배열은 격자별 allocatable이며 세 표는 2차원 allocatable이다(109–136). CONTAINS를 포함한다(138). |
| 139–185 | 시작 시 열린 전처리 조건 없음. `allocate_behavior`를 시작한다(140). 미할당 Larvae_GR0·Larvae_size0·food_supply·settle_size·sink_base·sink_rate·sink_size를 Ngrids 크기로 할당한다(152–185). 각 할당 직후 Dmem(1)에 REAL(Ngrids,r8)을 더한다. 이 블록에는 매개변수 값 초기화가 없다. 원문 조건·계산식·호출: `      IF (.not.allocated(Larvae_GR0)) THEN` (152); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (154); `      END IF` (155); `      IF (.not.allocated(Larvae_size0)) THEN` (157); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (159); `      END IF` (160); `      IF (.not.allocated(food_supply)) THEN` (162); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (164); `      END IF` (165); `      IF (.not.allocated(settle_size)) THEN` (167); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (169); `      END IF` (170); `      IF (.not.allocated(sink_base)) THEN` (172); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (174); `      END IF` (175); `      IF (.not.allocated(sink_rate)) THEN` (177); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (179); `      END IF` (180); `      IF (.not.allocated(sink_size)) THEN` (182); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (184); `      END IF` (185). |
| 186–215 | 시작 시 열린 전처리 조건 없음. 시작 시 140행 allocate_behavior 안. slope_Sdec·slope_Sinc·swim_Sdec·swim_Sinc·swim_Tmax·swim_Tmin을 미할당일 때 할당한다(187–215). 각 배열은 Ngrids 크기이며 Dmem을 증가시킨다. 원문 조건·계산식·호출: `      IF (.not.allocated(slope_Sdec)) THEN` (187); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (189); `      END IF` (190); `      IF (.not.allocated(slope_Sinc)) THEN` (192); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (194); `      END IF` (195); `      IF (.not.allocated(swim_Sdec)) THEN` (197); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (199); `      END IF` (200); `      IF (.not.allocated(swim_Sinc)) THEN` (202); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (204); `      END IF` (205); `      IF (.not.allocated(swim_Tmax)) THEN` (207); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (209); `      END IF` (210); `      IF (.not.allocated(swim_Tmin)) THEN` (212); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (214); `      END IF` (215). |
| 216–260 | 시작 시 열린 전처리 조건 없음. 시작 시 140행 allocate_behavior 안. turb_ambi·turb_axis·turb_base·turb_crit·turb_mean·turb_rate·turb_size·turb_slop를 미할당일 때 Ngrids 크기로 할당하고 Dmem을 증가시킨다(217–255). RETURN·루틴·모듈 종료 및 빈 줄을 포함한다(256–260). 원문 조건·계산식·호출: `      IF (.not.allocated(turb_ambi)) THEN` (217); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (219); `      END IF` (220); `      IF (.not.allocated(turb_axis)) THEN` (222); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (224); `      END IF` (225); `      IF (.not.allocated(turb_base)) THEN` (227); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (229); `      END IF` (230); `      IF (.not.allocated(turb_crit)) THEN` (232); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (234); `      END IF` (235); `      IF (.not.allocated(turb_mean)) THEN` (237); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (239); `      END IF` (240); `      IF (.not.allocated(turb_rate)) THEN` (242); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (244); `      END IF` (245); `      IF (.not.allocated(turb_size)) THEN` (247); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (249); `      END IF` (250); `      IF (.not.allocated(turb_slop)) THEN` (252); `        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (254); `      END IF` (255). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 47–52: 모듈 주석은 유영 표의 온도를 I축, 크기를 J축으로 설명한다. 판독한 oyster_floats.h의 375–378행은 크기로 i1/i2, 온도로 j1/j2를 계산한다.
- 85–107·152–255: 조회표 크기·시작값·간격 스칼라의 선언에는 초기값이 없다. allocate_behavior에서도 이 스칼라 값을 설정하지 않는다.
- 134–136·140–258: 세 조회표를 allocatable로 선언한다. allocate_behavior에는 이 표의 할당문이 없다.
- 152–255: 격자별 매개변수 배열은 할당과 Dmem 갱신만 수행한다. 이 루틴에는 할당 직후 기본값으로 채우는 대입문이 없다.
