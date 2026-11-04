---
file: models/Celeris/raw/source_code/Celeris-WebGPU/scripts/load_WebGPUCeleris_output.m
lines: 80
sha256: 64814d811ae3b712f0dc66d4a0b816fc6b259cc8b2bb85ba6f7050cbf0066880
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# load_WebGPUCeleris_output.m — 판독 구간 기록

구간은 1행부터 80행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 화면과 변수를 초기화한다. dx·dy·nx·ny 파일을 읽고 격자 좌표를 계산한다. 수심 지형을 float32의 nx×ny 배열로 읽는다. 시간 단계 수는 수동 설정 496이다. 바닥 지형의 주석 단위는 `[m]`이다(16). 원문: `clf;` (1); `clear all;` (2); `dx = load('dx.txt');` (5); `dy = load('dy.txt');` (6); `nx = load('nx.txt');` (7); `ny = load('ny.txt');` (8); `x = [0:1:nx-1] * dx;` (10); `y = [0:1:ny-1]' * dy;` (11); `nt = 496;  % need to change manually` (14); `fid = fopen('bathytopo.bin', 'r');` (17); `bathytopo = fread(fid, [nx, ny], 'float32');` (18); `fclose(fid);` (19); `time = zeros(nt,1);` (21) [11-04 전수 검증 보완] |
| 23–50 | 시작 시 23행에서 열리는 `for n = 1:nt`는 80행 `end`에서 닫힌다. 시간 단계 루프(loop)를 시작한다. 시간 텍스트와 수면고 이진 파일을 읽는다. x·y 유량과 난류 점성계수 파일 판독은 주석 처리되어 있다. 원문: `for n = 1:nt` (23); `time_fname = ['time_' num2str(n) '.txt'];` (24); `time(n) = load(time_fname);  % [sec]` (25); `eta_fname = ['elev_' num2str(n) '.bin']; % Note: Changed from .txt to .bin` (28); `fid = fopen(eta_fname, 'r');` (29); `eta = fread(fid, [nx, ny], 'float32');` (30); `fclose(fid);` (31) 주석 처리된 원문: `%     % x direction flux [m^2/s]` (33); `%     P_fname = ['xflux_' num2str(n) '.bin']; % Note: Changed from .txt to .bin` (34); `%     fid = fopen(P_fname, 'r');` (35); `%     P = fread(fid, [nx, ny], 'float32');` (36); `%     fclose(fid);` (37); `%     % y direction flux [m^2/s]` (39); `%     Q_fname = ['yflux_' num2str(n) '.bin']; % Note: Changed from .txt to .bin` (40); `%     fid = fopen(Q_fname, 'r');` (41); `%     Q = fread(fid, [nx, ny], 'float32');` (42); `%     fclose(fid);` (43); `%     % turbulent eddy viscosity from breaking [m/s^2]` (45); `%     nu_fname = ['turb_' num2str(n) '.bin']; % Note: Changed from .txt to .bin` (46); `%     fid = fopen(nu_fname, 'r');` (47); `%     nu = fread(fid, [nx, ny], 'float32');` (48); `%     fclose(fid);` (49). 수면고의 주석 단위는 `[m]`이다(27). [11-04 전수 검증 보완] |
| 51–69 | 시작 시 23행 `for n = 1:nt` 루프 안. 전체 수심을 계산하고 H<=0.0인 위치의 수심과 수면고를 NaN으로 바꾼다. 속도 계산과 특정 위치 interp2 보간 예시는 주석 처리되어 있다. 원문: `H = eta - bathytopo;  % total water depth` (51); `drynodes = find(H<=0.0);  % find dry nodes, may need to change 0.0 to some threshold (e.g. 0.1) to eliminate large velocitys in thin flows` (55); `H(drynodes) = NaN;` (56); `eta(drynodes) = NaN;` (57) 주석 처리된 원문: `%     u = P ./ H;  % [m/s]` (52); `%     v = Q ./ H;  % [m/s]` (53); `%     u(drynodes) = NaN;` (58); `%     v(drynodes) = NaN;` (59); `%     nu(drynodes) = NaN;` (60); `%     xp = 9000;` (63); `%     yp = 4000;` (64); `%     Hp = interp2(x,y,H',xp,yp);` (65); `%     up = interp2(x,y,u',xp,yp);` (66); `%     vp = interp2(x,y,v',xp,yp);` (67); `%     disp([Hp up vp])` (68). [11-04 전수 검증 보완] |
| 70–80 | 시작 시 23행 `for n = 1:nt` 루프 안. 전치한 수면고를 pcolor로 표시한다. 보간 음영과 같은 축 비율을 적용한다. 색 범위는 [-1 1]이다. 시간 제목과 0.01초 pause 후 루프를 마친다. 원문: `figure(1);` (71); `clf` (72); `pcolor(x, y, eta');  % note the transpose '  - the surface data is [nx,ny]` (73); `shading interp;` (74); `axis equal;` (75); `clim([-1 1])` (76); `colorbar;` (77); `title(sprintf('Time = %f seconds', time(n)));` (78); `pause(.01)` (79); `end` (80) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14: 시간 단계 수 `nt = 496;`은 수동 변경 주석과 함께 고정되어 있다.
- 17–19·29–31: fopen·fread 다음에 파일 열기 실패나 읽은 원소 수를 검사하는 조건은 없다.
- 33–49·52–53·62–68: 유량·점성계수 판독, 속도 계산, 특정 위치 보간은 주석 처리되어 있다.
