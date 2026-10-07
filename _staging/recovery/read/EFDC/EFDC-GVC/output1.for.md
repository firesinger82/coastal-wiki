---
file: models/EFDC/raw/source_code/EFDC-GVC/output1.for
lines: 260
sha256: 167711b187b7897ee58fc56b84bdfa8c911b4389497cc7eb3a55b0d9b82cd8e5
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# output1.for — 판독 구간 기록

구간은 1행부터 260행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | 구분 주석과 `SUBROUTINE OUTPUT1` 입구(1–6). EFDC-FULL 1.0a·수정일·변경 이력 주석(8–17). `INCLUDE 'EFDC.PAR'`·`INCLUDE 'EFDC.CMN'` (21–22). 수면 고도(surface elevation) 출력 머리말도 포함한다(24–29). 포함 파일 내부는 판독하지 않았다. |
| 30–43 | 시작 시 6행 OUTPUT1 안. L=2..LA 루프(30)의 `PAM(L)=P(L)*GI` (31)로 수면 출력값을 만든다. 단위 7에 N을 쓰고 `CALL PPLOT (1)` (34)을 실행한다. FORMAT의 단위 표기는 meters이고 시간은 timestep이다(36). 다음 염분(salinity) 머리말도 포함한다(38–43). |
| 44–61 | 시작 시 6행 OUTPUT1 안. `DO KK=1,KC,KS` (44)의 각 층에서 L=2..LA의 SAL(L,KK)를 PAM으로 복사한다(46–48). 단위 7에 KK/N을 쓰고 `CALL PPLOT (1)` (50)을 실행한다. 루프를 닫고 염분의 단위 PPT와 층/단계 FORMAT을 정의한다(52–54). 염분 성층(stratification) 머리말도 포함한다(56–61). |
| 62–79 | 시작 시 6행 OUTPUT1 안. `IF(KC.GT.1)THEN` (62)에서 L 루프의 `PAM(L)=SAL(L,1)-SAL(L,KC)` (65)로 최하층·최상층 염분 차를 계산한다. N을 출력하고 `CALL PPLOT (1)` (68)을 실행한다. 조건 종료와 PPT 표기 FORMAT을 포함한다(70–72). 잔차(residual) 총수심 머리말도 포함한다(74–79). |
| 80–95 | 시작 시 6행 OUTPUT1 안. L 루프의 HLPF를 PAM으로 복사한다(80–82). 단위 7에 잔차 총수심 제목과 N을 쓴 뒤 `CALL PPLOT (2)` (85)을 실행한다. FORMAT은 수심 단위를 meters로 적고 평균 기간을 TWO TIDAL CYCLES로 적는다(87–88). 오일러 잔차 수송 속도(Eulerian residual transport velocity) 머리말도 포함한다(90–95). |
| 96–127 | 시작 시 6행 OUTPUT1 안. `DO KK=1,KC,KS` (96)와 L 루프의 X 방향 식은 `PAM(L)=0.5*(UHLPF(L,KK)+UHLPF(L+1,KK))/HMP(L)` (99). KK/N 제목 뒤 `CALL PPLOT (2)` (103)을 실행한다. 별도 `DO KK=1,KC,KS` (109)의 L 루프에서 LN=LNC(L)을 찾는다(112). Y 방향 식은 `PAM(L)=0.5*(VHLPF(L,KK)+VHLPF(LN,KK))/HMP(L)` (113). KK/N 제목 뒤 `CALL PPLOT (2)` (117)을 실행한다. 층 루프 종료와 X/Y 속도 단위 M/S의 FORMAT을 포함한다(119–124). 구분 주석도 포함한다(125–127). |
| 128–163 | 시작 시 6행 OUTPUT1 안. 벡터 퍼텐셜(vector potential) 수송 속도 머리말(128–131). `DO KK=1,KC,KS` (132)의 L 루프 식은 `PAM(L)=0.5*(UVPT(L,KK)+UVPT(L+1,KK))/HMP(L)` (135). KK/N 제목 뒤 `CALL PPLOT (2)` (139). 별도 `DO KK=1,KC,KS` (145)의 L 루프 식은 `PAM(L)=0.5*(VVPT(L,KK)+VVPT(LN,KK))/HMP(L)` (149)이며 LN=LNC(L)을 먼저 찾는다(148). KK/N 제목 뒤 `CALL PPLOT (2)` (153). 루프 종료·X/Y의 M/S FORMAT·구분 주석을 포함한다(155–163). |
| 164–201 | 시작 시 6행 OUTPUT1 안. 라그랑주 잔차 수송 속도(Lagrangian residual transport velocity) 머리말(164–167). `DO KK=1,KC,KS` (168)의 L 루프 식은 `PAM(L)=0.5*(UHLPF(L,KK)+UHLPF(L+1,KK)+UVPT(L,KK)` (171), `&       +UVPT(L+1,KK))/HMP(L)` (172). KK/N 제목 뒤 `CALL PPLOT (2)` (176). 별도 `DO KK=1,KC,KS` (182)의 Y 식은 `PAM(L)=0.5*(VHLPF(L,KK)+VHLPF(LN,KK)+VVPT(L,KK)` (186), `&       +VVPT(LN,KK))/HMP(L)` (187). LN을 먼저 찾고 KK/N 제목 뒤 `CALL PPLOT (2)` (191)을 실행한다. 루프 종료·X/Y의 M/S FORMAT·구분 주석을 포함한다(193–201). |
| 202–222 | 시작 시 6행 OUTPUT1 안. 개방 경계(open boundary)의 잔차 체적 유량(volumetric flow) 머리말(202–205). 단위 7에 제목·평균 종료 N·QXW/QXE·QYS/QYN·QXWVP/QXEVP·QYSVP/QYNVP를 쓴다(206–211). FORMAT은 유량 단위를 M3/S로 적으며 각 쌍을 E12.4로 출력한다(215–219). 구분 주석도 포함한다(220–222). |
| 223–239 | 시작 시 6행 OUTPUT1 안. 잔차 부력(buoyancy)·성층 머리말(223–226). `DO KK=1,KC,KS` (227)의 L 루프에서 SALLPF(L,KK)를 PAM으로 복사한다(229–231). KK/N 제목을 쓴 뒤 `CALL PPLOT (1)` (234)을 실행한다. 층 루프 종료·구분 주석도 포함한다(236–239). |
| 240–260 | 시작 시 6행 OUTPUT1 안. `IF(KC.GT.1)THEN` (240)의 L 루프에서 LN=LNC(L)을 대입한다(243). 성층 식은 `PAM(L)=SALLPF(L,1)-SALLPF(L,KC)` (244). 제목·N을 쓴 뒤 `CALL PPLOT (1)` (248)을 실행한다. 조건을 닫고 잔차 염분·성층의 PPT FORMAT을 정의한다(250–255). 구분 주석·RETURN·END로 끝난다(256–260). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 44·96·109·132·145·168·182·227: 층 출력 루프는 모두 DO KK=1,KC,KS를 사용한다. 각 층 루프 앞에 KS=0을 검사하는 조건은 이 파일에 없다.
- 99·113·135·149·171–172·186–187: 잔차 수송 속도 식의 분모는 HMP(L)이다. 이 파일에는 해당 나눗셈 전에 HMP(L)=0을 검사하는 조건이 없다.
- 243–244: 마지막 성층 블록은 LN=LNC(L)을 대입한다. 바로 뒤 PAM 식과 해당 블록의 출력은 LN을 참조하지 않는다.
