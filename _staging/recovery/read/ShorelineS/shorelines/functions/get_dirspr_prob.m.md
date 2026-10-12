---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_dirspr_prob.m
lines: 58
sha256: c1d772aeb30ca62217348613d52cd33fb42abe53f90b5b7046a9d6a5d33b6dc2
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_dirspr_prob.m — 판독 구간 기록

구간은 1행부터 58행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–39 | 함수 시그니처 `function [prob]=get_dirspr_prob(dspr,dirout,mu)` (1). 방향 퍼짐(directional spreading) dspr, 선택 방향 배열 dirout와 주 방향 mu, 방향별 확률 출력 설명(4–11). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(12–39). |
| 40–50 | mu 생략 조건 `if nargin<3` (40)의 기본값 `mu=0;` (41). sigma=dspr 복사(43). dirout 생략 조건 `if nargin<2` (44), 기본 간격·방향 범위 `ddir=10;` (45); `dirout=[-40:10:40];` (46): -40..40에서 10 간격. 실제 방향 간격 `ddir=diff(dirout);` (48). prob 빈 배열 초기화(50). |
| 51–58 | 방향 루프 `for pp=1:length(dirout)` (51). 양옆 간격 선택 `ddir1=ddir(max(pp-1,1));` (52); `ddir2=ddir(min(pp,length(ddir)));` (53). 정규 분포(normal distribution)의 양 경계 밀도·사다리꼴 확률 `p1=1/(sigma*sqrt(2*pi)).*exp((-(dirout(pp)-ddir1/2-mu).^2)/(2*sigma.^2));` (54); `p2=1/(sigma*sqrt(2*pi)).*exp((-(dirout(pp)+ddir2/2-mu).^2)/(2*sigma.^2));` (55); `prob(pp)=(ddir1+ddir2)/2*(p2+p1)/2; % compute probability of area underneath normal distribution for 'meandir-ddir/2' to 'meandir+ddir/2'` (56). 루프·함수 종료(57–58). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 45·48: 기본 ddir=10 대입 뒤 ddir=diff(dirout)로 덮어쓴다.
- 48·52–53: dirout의 인접 간격을 참조하며 단일 방향 입력을 별도로 처리하는 분기는 없다.
- 43·54–56: dspr를 sigma로 사용하고 밀도 분모에 넣는다. sigma=0 검사와 최종 확률합 정규화는 없다.
