---
file: models/ShorelineS/raw/source_code/shorelines/functions/wave_refraction.m
lines: 110
sha256: 037172515cb83af6a794eef4511432331e083201410252bb1997d216c0f114d6
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# wave_refraction.m — 판독 구간 기록

구간은 1행부터 110행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–61 | 함수 시그니처(1), 외해에서 근해까지 굴절(refraction) 목적과 직접 외해 사용·Snell 변환·2차원 파랑 모델의 세 옵션(4–8), WAVE·COAST·TRANSP 입력과 파고·파향 출력 설명(10–32), 저작권·LGPL·무보증·빈 줄(34–61). 옵션 2를 default로 설명하지만 입력 기본값 설정문은 없다. 원문: `function [WAVE]=wave_refraction(WAVE,COAST,TRANSP)` (1). |
| 62–81 | 시작 시 1행 함수 안. eps=0이다(62). waveinteraction이 참이면 get_wave_fields_from_mat로 파랑 표를 읽고 각도를 mod 360으로 바꾼다(63–66). Hstab 길이가 1보다 크면 Hs·방향·Tp 보간 루틴, else면 방향·Tp 보간 루틴을 호출한다(67–71). PHIwg를 WAVE.PHIo에 저장하고 해안 좌표·점 수·surfwidth로 get_interpolated_waves_from_grid를 호출하여 PHItdp·HStdp를 저장한다(72–80). 원문: `eps=0;` (62), `if WAVE.waveinteraction` (63), `[ xg,yg,Hg_all,phiwg_all,dirtab,Tptab,Hstab ] = get_wave_fields_from_mat( WAVE.wavefile );` (65), `phiwg_all=mod(phiwg_all,360.);` (66), `if length(Hstab)>1` (67), `[Hg,PHIwg,iwtw,PHIwg_wr,Hg_wr]=get_interpolated_wavefield_Hs_dir_Tp(xg,yg,Hg_all,phiwg_all,WAVE.HSo,WAVE.PHIo,WAVE.TP,Hstab,dirtab,Tptab);` (68), `else` (69), `[Hg,PHIwg,iwtw,PHIwg_wr,Hg_wr]=get_interpolated_wavefield_dir_Tp(xg,yg,Hg_all,phiwg_all,WAVE.HSo,WAVE.PHIo,WAVE.TP,dirtab,Tptab);` (70), `WAVE.PHIo=PHIwg;` (72), `x=COAST.x;` (73), `y=COAST.y;` (74), `n=COAST.n;` (75), `nq=COAST.nq;` (76), `surfwidth=WAVE.surfwidth;` (77), `[H,PHIcd]=get_interpolated_waves_from_grid(x,y,n,nq,surfwidth,xg,yg,Hg,PHIwg);` (78), `WAVE.PHItdp=PHIcd;` (79), `WAVE.HStdp=H;` (80). |
| 82–103 | 시작 시 1행 함수·63행 파랑 옵션 선택문 안. COAST.PHIf가 있고 CERC가 아니면 상대 입사각을 −180–180으로 만들고 절대값 89.999 이상을 그 값으로 제한한다(82–89). 두 get_disper 호출 뒤 Snell 법칙(Snell's law)으로 근해 파향, 에너지 유속 비로 천수(shoaling)·굴절 파고를 계산한다(92–96). else에서는 외해 파향·파고를 그대로 복사한다(98–102). 원문: `elseif ~isempty(COAST.PHIf) && ~strcmpi(TRANSP.trform,'CERC')` (82), `relANGLE=mod(WAVE.PHIo-COAST.PHIf+180,360)-180;` (85), `IDoff=find(abs(relANGLE)>=89.999);` (88), `relANGLE(IDoff)=sign(relANGLE(IDoff)) .* 89.999;` (89), `[~,c_deep,~,n_deep]=get_disper(WAVE.ddeep,WAVE.TP);` (92), `[~,c_tdp,~,n_tdp]=get_disper(WAVE.dnearshore,WAVE.TP);` (93), `WAVE.PHItdp=mod(COAST.PHIf+real(asind(c_tdp./c_deep.*sind(relANGLE))),360);` (94), `relANGLEtdp=mod(WAVE.PHItdp-COAST.PHIf+180,360)-180;` (95), `WAVE.HStdp=WAVE.HSo.*max(real(sqrt(n_deep.*c_deep.*cosd(relANGLE)./(n_tdp .*c_tdp .*cosd(relANGLEtdp)))),eps);` (96), `else` (98), `WAVE.PHItdp=WAVE.PHIo;` (100), `WAVE.HStdp=WAVE.HSo;` (101). |
| 104–110 | 시작 시 1행 함수 안이며 옵션 선택문 밖. 파향과 파고 길이가 각각 1 이하이면 COAST.nq만큼 복제한다(104–109). 함수가 끝난다(110). 원문: `if length(WAVE.PHItdp)<=1` (104), `WAVE.PHItdp=repmat(WAVE.PHItdp,[1,COAST.nq]);` (105), `if length(WAVE.HStdp)<=1` (107), `WAVE.HStdp=repmat(WAVE.HStdp,[1,COAST.nq]);` (108). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 68·70: iwtw·PHIwg_wr·Hg_wr는 호출 출력으로 받은 뒤 이 파일에서 참조되지 않는다.
- 72: 2차원 파랑 모델 분기는 WAVE.PHIo를 격자 보간 전 PHIwg 값으로 덮어쓴다.
- 82: Snell 변환을 제외하는 수송식 조건은 CERC 하나만 명시한다.
- 62·96: 파고 계수 하한 eps는 0이다. 굴절 파향과 파고 계수에 real을 적용한다(94·96).
