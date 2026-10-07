---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-Original/csndzeq.f90
lines: 79
sha256: d859e6bdef8a8f5f798ebc1a1880b0c6cb32ff7fc104dcaa7b5dfee467534df1
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# csndzeq.f90 — 판독 구간 기록

구간은 1행부터 79행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | EFDC+·저작권·GPLv2 머리말(1–8). CSNDZEQ 함수 입구(9). 바닥 부근 참조농도(reference concentration)의 무차원 참조높이(reference height)를 계산한다는 주석(11). 2011년 F90 재작성·WS<=0 처리 이력을 적는다(13–17). IOPT·입경·전단응력·깊이·비중(specific gravity)·침강속도(settling velocity)와 작업변수를 선언한다(19–23). 빈 줄을 포함한다(24–25). |
| 26–45 | 시작 시 9행 CSNDZEQ 안. IOPT=1은 Garcia–Parker 1991을 적고 0.05를 반환한다(26–32). IOPT=2는 Smith–McLean 1977을 적는다(34–39). SNDDMX와 응력 초과량으로 TMPVAL을 계산하고 SNDDIA/SNDDMX·1/DEP를 곱한 뒤 0.01 하한을 적용한다(41–44). 조건·계산·호출 원문: `if( IOPT == 1 )then` (26); `CSNDZEQ = 0.05` (32); `elseif( IOPT == 2 )then` (34); `TMPVAL = 26.3*SNDDMX*(TAUB-TAUR)/GPDIASED` (41); `TMPVAL = TMPVAL*SNDDIA/SNDDMX` (42); `TMPVAL = TMPVAL/DEP` (43); `CSNDZEQ = max(TMPVAL,0.01)` (44). |
| 46–65 | 시작 시 9행 CSNDZEQ·26행 옵션 선택 블록 안. IOPT=3은 van Rijn 1984를 적는다(46–50). WS>0인 경우 입자 Reynolds 수(Reynolds number)를 구하고 REY<=10 또는 >10에 따라 TAURS를 계산한다(51–54). 54행 주석은 0.016을 0.16으로 수정했다고 적는다. 응력 초과량 VAL을 0..100으로 제한한다(55–56). 지수식과 25.-VAL, DEP의 0.7승·SNDDMX의 0.3승으로 높이를 계산하고 0.01 하한을 적용한다(57–61). WS 분기의 else는 0.01이다(62–64). 조건·계산·호출 원문: `elseif( IOPT == 3 )then` (46); `if( WS > 0. )then` (51); `REY = 1.E4*SNDDIA*( (9.8*(SSG-1.))**0.333 )` (52); `if( REY <= 10. ) TAURS = (4.*WS/REY)**2` (53); `if( REY  > 10. ) TAURS = 0.16*WS*WS                      ! *** Corrected 2021-06 from 0.016.  0.16 = 0.4^2 from VanRijn 1984` (54); `VAL = (TAUB/TAURS)-1.` (55); `VAL = min(MAX(VAL,0.),100.)` (56); `VAL1 = 1.-EXP(-0.5*VAL)` (57); `VAL1 = 0.11*VAL1*(25.-VAL)` (58); `ZEQ1 = 0.5*VAL1*(DEP**0.7)*(SNDDMX**0.3)` (59); `ZEQ1 = ZEQ1/DEP` (60); `CSNDZEQ = max(ZEQ1,0.01)` (61); `else` (62); `CSNDZEQ = 0.01` (63). |
| 66–79 | 시작 시 9행 CSNDZEQ·26행 옵션 선택 블록 안. IOPT=4 또는 5이면 Hamrick SEDFLUME 옵션으로 0.01을 반환한다(66–68). 바깥 else는 STOPP('BAD CSNDZEQ OPTION')를 호출한다(70–72). 분기 종료·return·END·마지막 빈 줄을 포함한다(74–79). 조건·계산·호출 원문: `elseif( IOPT  ==  4 .or. IOPT == 5 )then` (66); `CSNDZEQ = 0.01` (68); `else` (70); `call STOPP('BAD CSNDZEQ OPTION')` (72). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41–43: 옵션 2는 첫 식에서 SNDDMX를 곱하고 다음 식에서 SNDDMX로 나눈다. 이 분기에 SNDDMX=0 또는 DEP=0 검사는 없다.
- 55–61: 옵션 3은 VAL의 상한을 100으로 제한한다. 그 뒤 식에는 25.-VAL 인수가 있다. 최종 CSNDZEQ에는 0.01 하한이 적용된다.
