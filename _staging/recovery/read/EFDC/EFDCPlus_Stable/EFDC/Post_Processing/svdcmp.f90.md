---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Post_Processing/svdcmp.f90
lines: 261
sha256: 708bd7d563f8b2a6b0c6d4d6ef1b9b996aaa80175794c955e6105ae72e8fc9c0
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# svdcmp.f90 — 판독 구간 기록

구간은 1행부터 261행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | EFDC+·GPLv2·저작권 머리말(1–8), `SUBROUTINE SVDCMP(A,M,N,MP,NP,W,V)` (9). Numerical Recipes 출처 주석(11). `use GLOBAL,only: LWC` (14), implicit none(15). 크기·인덱스·A(MP,NP)·W(NP)·V(NP,NP)·allocatable RV1와 실수 작업변수 선언(17–22). `if( .not. allocated(RV1) )then` (24)이면 RV1(N) 할당·0 초기화(25–26). G·SCALE·ANORM=0 초기화(28–30). |
| 31–71 | 시작 시 9행 SVDCMP 안. 특이값 분해(singular value decomposition)의 I=1..N 루프(31)에서 `L = I+1` (32), `RV1(I) = SCALE*G` (33), G·S·SCALE=0(34–36). `if( I <= M )then` (37)의 K=I..M에서 `SCALE = SCALE+ABS(A(K,I))` (39). `if( SCALE /= 0.0 )then` (41)이면 `A(K,I) = A(K,I)/SCALE` (43), `S = S+A(K,I)*A(K,I)` (44), F=A(I,I)(46), `SQRTSSS = SQRT(S)` (47), `G = -SIGN(SQRTSSS,F)` (48), `H = F*G-S` (49), `A(I,I) = F-G` (50). 내부 `if( I /= N )then` (51)의 J=L..N·K=I..M에서 `S = S+A(K,I)*A(K,J)` (55), `F = S/H` (57), `A(K,J) = A(K,J)+F*A(K,I)` (59). 두 내부 조건의 적절한 종료 뒤 `A(K,I) = SCALE*A(K,I)` (64). I<=M 조건 밖에서 `W(I) = SCALE *G` (68), G·S·SCALE=0(69–71). |
| 72–105 | 시작 시 9행 SVDCMP·31행 I 루프 안. `if( (I <= M) .and. (I /= N) )then` (72)의 K=L..N에서 `SCALE = SCALE+ABS(A(I,K))` (74). `if( SCALE /= 0.0 )then` (76)이면 `A(I,K) = A(I,K)/SCALE` (78), `S = S+A(I,K)*A(I,K)` (79), F=A(I,L)(81), `G = -SIGN(SQRT(S),F)` (82), `H = F*G-S` (83), `A(I,L) = F-G` (84), `RV1(K) = A(I,K)/H` (86). 내부 `if( I /= M )then` (88)의 J=L..M·K=L..N에서 `S = S+A(J,K)*A(I,K)` (92), `A(J,K) = A(J,K)+S*RV1(K)` (95). 이 조건 밖에서 `A(I,K) = SCALE*A(I,K)` (100). 72·76행 조건 종료 후 `ANORM = max(ANORM,(ABS(W(I))+ABS(RV1(I))))` (104). I 루프 종료(105). |
| 106–130 | 시작 시 9행 SVDCMP 안. I=N..1 역순으로 오른쪽 변환을 V에 누적(106). `if( I < N )then` (107), 내부 `if( G /= 0.0 )then` (108)에서 J=L..N의 `V(J,I) = (A(I,J)/A(I,L))/G` (110). 이어 J·K=L..N에서 `S = S+A(I,K)*V(K,J)` (115), `V(K,J) = V(K,J)+S*V(K,I)` (118). G 조건 밖의 J 루프는 V(I,J)·V(J,I)=0(122–125). I<N 조건 밖에서 `V(I,I) = 1.0` (127), G=RV1(I)·L=I 복사(128–129), 루프 종료(130). |
| 131–162 | 시작 시 9행 SVDCMP 안. I=N..1에서 `L = I+1` (132), G=W(I)(133). `if( I < N )then` (134)의 J=L..N에서 A(I,J)=0(136). `if( G /= 0.0 )then` (139)이면 `G = 1.0/G` (140). 내부 `if( I /= N )then` (141)의 J=L..N·K=L..M에서 `S = S+A(K,I)*A(K,J)` (145), `F = (S/A(I,I))*G` (147), K=I..M에서 `A(K,J) = A(K,J)+F*A(K,I)` (149). 내부 조건 밖의 J=I..M에서 `A(J,I) = A(J,I)*G` (154). G 조건의 else는 A(J,I)=0(156–159). 조건 밖에서 `A(I,I) = A(I,I)+1.0` (161), 역순 루프 종료(162). |
| 163–204 | 시작 시 9행 SVDCMP 안. K=N..1(163), ITS=1..30(164), L=K..1(165)의 반복에서 NM=LWC(L)(166). `if( (ABS(RV1(L))+ANORM) == ANORM)  GOTO 2` (167), `if( (ABS(W(NM))+ANORM) == ANORM)  GOTO 1` (168). 라벨 1은 C=0·S=1(170–171). I=L..K에서 `F = S*RV1(I)` (173), `if( (ABS(F)+ANORM) /= ANORM )then` (174)이면 G=W(I)(175), `H = SQRT(F*F+G*G)` (176), W(I)=H(177), `H = 1.0/H` (178), `C = (G*H)` (179), `S = -(F*H)` (180). J=1..M의 Y/Z 복사 뒤 `A(J,NM) = (Y*C)+(Z*S)` (184), `A(J,I) = -(Y*S)+(Z*C)` (185). 라벨 2에서 Z=W(K)(189). `if( L == K )then` (190), 내부 `if( Z < 0.0 )then` (191)이면 `W(K) = -Z` (192), `V(J,K) = -V(J,K)` (194); L==K이면 GOTO 3(197). `if( ITS == 60 )then` (199)은 비수렴 메시지(200·204), RV1 해제·return(201–202). |
| 205–234 | 시작 시 9행 SVDCMP·163행 K 루프·164행 ITS 루프 안. X=W(L), `NM = K-1` (206), Y=W(NM)·G=RV1(NM)·H=RV1(K) 복사(205–209). 이동값 계산은 `F = ((Y-Z)*(Y+Z)+(G-H)*(G+H))/(2.0*H*Y)` (210), `G = SQRT(F*F+1.0)` (211), `F = ((X-Z)*(X+Z)+H*((Y/(F+SIGN(G,F)))-H))/X` (212). C·S=1(213–214). J=L..NM(215)에서 `I = J+1` (216), G=RV1(I)·Y=W(I)(217–218), `H = S*G` (219), `G = C*G` (220), `Z = SQRT(F*F+H*H)` (221), RV1(J)=Z(222), `C = F/Z` (223), `S = H/Z` (224), `F= (X*C)+(G*S)` (225), `G = -(X*S)+(G*C)` (226), `H = Y*S` (227), `Y = Y*C` (228). NM=1..N 루프에서 V 두 성분을 X/Z로 복사하고 `V(NM,J)= (X*C)+(Z*S)` (232), `V(NM,I) = -(X*S)+(Z*C)` (233). |
| 235–261 | 시작 시 9행 SVDCMP·163행 K 루프·164행 ITS 루프·215행 J 루프 안. `Z = SQRT(F*F+H*H)` (235), W(J)=Z(236). `if( Z /= 0.0 )then` (237)이면 `Z = 1.0/Z` (238), `C = F*Z` (239), `S = H*Z` (240). 조건 밖에서 `F= (C*G)+(S*Y)` (242), `X = -(S*G)+(C*Y)` (243). NM=1..M에서 Y/Z에 A 두 성분을 복사하고 `A(NM,J)= (Y*C)+(Z*S)` (247), `A(NM,I) = -(Y*S)+(Z*C)` (248). J 루프 종료(250), RV1(L)=0·RV1(K)=F·W(K)=X(251–253). ITS 루프 종료·라벨 3·K 루프 종료(254–256). RV1 해제, return·END·마지막 빈 줄(257–261). 별도 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 164·199–204: ITS 루프의 범위는 1..30이다. 비수렴 분기의 조건과 메시지는 60회이다.
- 14·166·168·182–185: NM은 GLOBAL에서 가져온 LWC(L)로 설정한다. 그 NM을 W와 A의 배열 인덱스로 사용한다.
