---
file: models/ShorelineS/raw/source_code/shorelines/functions/transport_groynesubmerged.m
lines: 79
sha256: 9b97850099d91e29339e916b20c23fedae629b7ee9aacf93577087f39100e2ad
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# transport_groynesubmerged.m — 판독 구간 기록

구간은 1행부터 79행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–49 | 함수 시그니처(1), 잠긴 돌제(submerged groyne)의 조석·파랑 수송 계산과 TIDEPROF 조합에 관한 주석(4–5), Slong·vw·h·zb·x·Aw·gammabr·HStdp 입력과 QSt·Dltr·zs 출력 설명(7–20), 저작권·LGPL·무보증 및 빈 줄(22–49). 구조체 입력은 없고 인수 기본값 설정도 없다. 원문: `function [QSt,Dltr,zs]=transport_groynesubmerged(Slong,vw,h,zb,x,Aw,gammabr,HStdp)` (1). |
| 50–62 | 시작 시 1행 함수 안. 조석 시간 인덱스는 1:24로 고정한다(50). 매 시간 noDLT=0으로 시작한다(53). max(vw(:,tt))>0이면 Slong(:,tt)의 최대값을 고른다(54–55). 그 밖에는 Slong(:,tt)의 최소값에 절대값을 취한다(56–57). Slong의 부호를 제한하는 조건은 없다(54–57). 동일 절대 수송 인덱스 중 첫 위치와 그 위치의 부호 있는 수송을 취한다(59–61). 원문: `for tt=1:24` (50), `noDLT=0;` (53), `if max(vw(:,tt))>0` (54), `slongmax=max((Slong(:,tt)));` (55), `else` (56), `slongmax=abs(min((Slong(:,tt))));` (57), `[ind]=find(abs(Slong(:,tt))==slongmax);` (59), `jj=ind(1);` (60), `slongmaxe=Slong(jj,tt);` (61). [10-12 전수 검증 정정] |
| 63–79 | 시작 시 1행 함수·50행 tt 루프 안. 수송 절대값이 slongmax의 10%를 넘고 noDLT=0이며 slongmaxe와 해당 수송의 곱이 양수인 동안 jj를 줄인다(63–64). jj<3이면 noDLT=1, jj=1로 설정한다(65–68). noDLT에 따라 단면 수심 또는 Aw·HStdp/gammabr로 Dltr를 정한다(70–74). 첫 두 x 간격으로 Slong 합을 적분하고 h와 zb로 수위 zs를 구한다(75–76). 루프·함수 끝과 빈 줄(77–79). 원문: `while abs(Slong(jj,tt))>0.1*slongmax & (noDLT==0 & slongmaxe*Slong(jj,tt)>0)` (63), `jj=jj-1;` (64), `if jj<3` (65), `noDLT=1;` (66), `jj=1;` (67), `if noDLT==0` (70), `Dltr(tt)=-zb(jj);` (71), `else` (72), `Dltr(tt)=Aw*HStdp/gammabr;` (73), `QSt(tt)=sum(Slong(:,tt))*(x(2)-x(1));` (75), `zs(tt)=h(1,tt)+zb(1);` (76). [10-12 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 50·75: 시간 인덱스는 24개로 고정되어 있다. 횡단 적분 간격은 x(2)−x(1) 하나를 사용한다.
- 59–60: 최대 수송과 같은 절대값을 찾은 결과에서 ind(1)을 바로 참조한다. 해당 인덱스가 비었는지 검사하는 문장은 이 파일에 없다.
- 20·76: 출력 설명은 zs를 water depth로 적는다. 실행식은 h(1,tt)+zb(1)이다.
