---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/obs_k2z.F
lines: 219
sha256: 2eadca990a419d0067a9708da1ccb1942199c23a41669571c59a0bd4214c16e9
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# obs_k2z.F — 판독 구간 기록

구간은 1행부터 219행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–105 | cppdefs.h 포함·obs_k2z_mod 시작·SOLVE3D 조건(1–3). 저작권·입출력·격자 그림·빈 주석(4–99). 주석은 소수 수직 좌표(fractional vertical coordinate)를 아래쪽 음의 미터 깊이로 바꾸어 앙상블 칼만 필터(Ensemble Kalman Filter, EnKF)의 국소화(localization)에 사용한다고 설명한다(12–15). Hmat의 8개 셀 꼭짓점(cell vertex)과 경계 인덱스 재설정, 모든 관측이 rho점 기준이라는 설명(46–98). mod_kinds 사용·implicit none·CONTAINS(100–105). 전처리 행: `#include "cppdefs.h"` (1); `#ifdef SOLVE3D` (3). |
| 106–156 | 시작 시 `#ifdef SOLVE3D` (3) 안. 또한 2행 obs_k2z_mod 안. obs_k2z 인수 목록·mod_param 사용(106–114). 격자 경계·관측 개수·수평 좌표 한계 입력(118–122). ASSUMED_SHAPE이면 관측 벡터·출력은 assumed-shape 배열이고 z는 지정된 하한을 사용한다(124–131). else는 길이 Mobs의 벡터·전체 상하한의 z 배열(132–140). obs_depths는 intent(out). Linterpolate·정수·깊이 및 보간(interpolation) 가중치·길이 8 Hmat 선언, 계산 제목·빈 줄(142–156). 전처리 행: `#  ifdef ASSUMED_SHAPE` (124); `#  else` (132); `#  endif` (140). |
| 157–177 | 시작 시 `#ifdef SOLVE3D` (3) 안. 또한 2행 obs_k2z_mod·107–111행 obs_k2z 안. iobs=1..Mobs 루프(157). Xmin·Ymin을 포함하고 Xmax·Ymax를 제외하는 수평 범위 조건(158–159). INT로 i1·j1을 얻고 i2·j2를 1 증가시킨다(160–163). i2>Imax 또는 j2>Jmax이면 해당 두 인덱스를 같게 만든다(164–169). 수평 거리 비율 p2·q2와 보완 비율 p1·q1, 네 쌍선형(bilinear) 가중치를 계산한다(170–177). 조건 원문: `IF (((Xmin.le.Xobs(iobs)).and.(Xobs(iobs).lt.Xmax)).and.        &` (158); `&      ((Ymin.le.Yobs(iobs)).and.(Yobs(iobs).lt.Ymax))) THEN` (159); `IF (i2.gt.Imax) THEN` (164); `IF (j2.gt.Jmax) THEN` (167). 계산·설정 원문: `i1=INT(Xobs(iobs))` (160); `j1=INT(Yobs(iobs))` (161); `i2=i1+1` (162); `j2=j1+1` (163); `p2=REAL(i2-i1,r8)*(Xobs(iobs)-REAL(i1,r8))` (170); `q2=REAL(j2-j1,r8)*(Yobs(iobs)-REAL(j1,r8))` (171); `p1=1.0_r8-p2` (172); `q1=1.0_r8-q2` (173); `w11=p1*q1` (174); `w21=p2*q1` (175); `w22=p2*q2` (176); `w12=p1*q2` (177). |
| 178–192 | 시작 시 `#ifdef SOLVE3D` (3) 안. 또한 2행 obs_k2z_mod·107–111행 obs_k2z·157행 iobs 루프·158–159행 수평 범위 분기 안. Zobs>0이면 소수 층 번호로 처리한다(178). UBk와의 차이가 1.0E-8_r8 미만이면 Linterpolate=FALSE이고 깊이는 0(179–181). 나머지 양의 Zobs는 Linterpolate=TRUE로 두고 W점 k1·k2와 수직 비율 r1·r2를 계산한다(182–188). Zobs<=0인 else는 이미 미터 깊이로 보고 그대로 복사하며 보간을 끈다(189–192). 조건 원문: `IF (Zobs(iobs).gt.0.0_r8) THEN` (178); `IF (ABS(REAL(UBk,r8)-Zobs(iobs)).lt.1.0E-8_r8) THEN` (179). 계산·설정 원문: `obs_depths(iobs)=0.0_r8` (181); `k1=MAX(LBk,INT(Zobs(iobs)-0.5_r8))               ! W-point` (184); `k2=MIN(k1+1,UBk)` (185); `r2=REAL(k2-k1,r8)*(Zobs(iobs)-REAL(k1,r8))` (186); `r1=1.0_r8-r2` (187). |
| 193–219 | 시작 시 `#ifdef SOLVE3D` (3) 안. 또한 2행 obs_k2z_mod·107–111행 obs_k2z·157행 iobs 루프·158–159행 수평 범위 분기 안. Linterpolate가 참이고 r1+r2>0이면 수평·수직 비율의 곱으로 8개 Hmat 가중치를 만든다(193–202). 이 가중치로 z의 8개 꼭짓점 깊이를 더해 obs_depths를 계산한다(203–210). 조건·루프 종료·빈 줄·반환·루틴 종료(211–217), SOLVE3D 조건·모듈 종료(218–219). 조건 원문: `IF (Linterpolate) THEN` (193); `IF ((r1+r2).gt.0.0_r8) THEN` (194). 계산·설정 원문: `Hmat(1)=w11*r1` (195); `Hmat(2)=w21*r1` (196); `Hmat(3)=w22*r1` (197); `Hmat(4)=w12*r1` (198); `Hmat(5)=w11*r2` (199); `Hmat(6)=w21*r2` (200); `Hmat(7)=w22*r2` (201); `Hmat(8)=w12*r2` (202); `obs_depths(iobs)=Hmat(1)*z(i1,j1,k1)+                     &` (203); `&                         Hmat(2)*z(i2,j1,k1)+                     &` (204); `&                         Hmat(3)*z(i2,j2,k1)+                     &` (205); `&                         Hmat(4)*z(i1,j2,k1)+                     &` (206); `&                         Hmat(5)*z(i1,j1,k2)+                     &` (207); `&                         Hmat(6)*z(i2,j1,k2)+                     &` (208); `&                         Hmat(7)*z(i2,j2,k2)+                     &` (209); `&                         Hmat(8)*z(i1,j2,k2)` (210). 전처리 행: `#endif` (218). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 39·125·133·157–214: obs_scale는 관측 선별 플래그로 설명되고 입력 배열로 선언된다. 실행문은 obs_scale를 참조하지 않는다.
- 118·146·148·157–214: 입력 ng·Imin·Jmin과 지역변수 i·ic·k·Zbot·Ztop·dz는 실행문에서 참조되지 않는다.
- 131·139·158–213: obs_depths는 intent(out)이다. 수평 범위 밖 관측에 값을 대입하는 else나 전체 배열 초기화는 이 파일에 없다.
- 179–181: 표면 관측 판정 허용오차는 1.0E-8_r8로 고정되어 있다. 해당 분기의 출력 깊이는 z의 표면값을 읽지 않고 0.0_r8로 설정한다.
- 184–187·194: k1은 LBk 하한만 제한하고 k2는 UBk 상한을 제한한다. r1은 1−r2로 만든다. 보간 실행 조건은 r1+r2>0이다.
