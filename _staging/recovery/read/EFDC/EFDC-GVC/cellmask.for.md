---
file: models/EFDC/raw/source_code/EFDC-GVC/cellmask.for
lines: 169
sha256: 86f74d0c6a39b96f871700e7be3fdd793d89d90922752480fe013a05ef6992c4
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# cellmask.for — 판독 구간 기록

구간은 1행부터 169행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | 구분 주석과 `SUBROUTINE CELLMASK` 입구(6). EFDC-FULL 1.0a·수정일·변경 기록 주석(8–17). 마스킹(masking) 변수로 육지 셀을 물 셀로 바꾸며 마스킹 셀 수심을 DXDY.INP 끝에 입력하라는 설명(21–23). `EFDC.PAR`·`EFDC.CMN` 포함(27–28). |
| 32–51 | 시작 시 6행 CELLMASK 루틴 안. MASK.INP를 STATUS='UNKNOWN'으로 연다(32). NS=1..6에서 80X FORMAT으로 여섯 행을 건너뛴다(34–37). MMASK 판독과 M=1..MMASK 반복의 I·J·MTYPE 판독은 ERR=1000을 지정한다(38·42–43). LIJ로 L을 얻는다(44). IJCT가 0 또는 9이거나 L이 2..LA 밖이면 위치 오류를 6번 장치에 출력한다(45–50). 원문: `DO NS=1,6` (34); `DO M=1,MMASK` (42); `L=LIJ(I,J)` (44); `IF(IJCT(I,J).EQ.0.OR.IJCT(I,J).EQ.9)THEN` (45); `WRITE(6,*)'INVALID MASK LOCATION AT ',M,I,J` (46); `ENDIF` (47); `IF(L.LT.2.OR.L.GT.LA)THEN` (48); `WRITE(6,*)'INVALID MASK LOCATION AT ',M,I,J` (49); `ENDIF` (50). |
| 52–83 | 시작 시 6행 CELLMASK 루틴·42행 M 루프 안. MTYPE=1이면 SUB·SUBO 및 UHDYE·UHDY1E·UHDY2E를 0으로 설정한다(52–57). K=1..KC에서 U·U1·U2·UHDY·UHDY1·UHDY2도 0으로 설정한다(58–65). 독립 MTYPE=2 조건은 SVB·SVBO·VHDXE·VHDX1E·VHDX2E와 모든 층의 V·V1·V2·VHDX·VHDX1·VHDX2를 0으로 설정한다(68–82). 원문: `IF(MTYPE.EQ.1)THEN` (52); `DO K=1,KC` (58); `IF(MTYPE.EQ.2)THEN` (68); `DO K=1,KC` (74). |
| 84–107 | 시작 시 6행 CELLMASK 루틴·42행 M 루프 안. MTYPE=3이면 LN=LNC(L)을 얻는다(84–85). L과 L+1의 SUB 계열·UHDYE 계열, L과 LN의 SVB 계열·VHDXE 계열을 0으로 설정한다(86–105). L의 P·P1=0(106–107). 원문: `IF(MTYPE.EQ.3)THEN` (84). |
| 108–150 | 시작 시 6행 CELLMASK 루틴·42행 M 루프·84행 MTYPE=3 참 분기 안. K=1..KC에서 B·B1·SAL·SAL1·DYE·DYE1·SED(...,1)·SED1(...,1)·QQ·QQ1·QQL·QQL1을 0으로 설정한다(108–122). TEM·TEM1은 TEMO로 설정한다(113–114). L과 L+1의 U·UHDY 계열, L과 LN의 V·VHDX 계열을 0으로 설정한다(123–146). 층 루프·MTYPE 조건·M 루프 종료(147–150). 원문: `DO K=1,KC` (108); `TEM(L,K)=TEMO` (113); `TEM1(L,K)=TEMO` (114). |
| 151–169 | 시작 시 6행 CELLMASK 루틴 안. 정상 경로는 MASK.INP를 닫고 GOTO 1002로 오류 블록을 건너뛴다(154·160). 1000번 표지는 MASK.INP 판독 오류 FORMAT을 출력하고 STOP한다(161–163). 1002번 표지·구분 주석·RETURN·END(164–169). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 45–50·52–148: 위치 오류 조건은 WRITE만 실행한다. 그 뒤 마스킹 조건 앞에 STOP·RETURN·다음 M 반복으로 이동하는 문장이 없다.
- 52·68·84·148: MTYPE 조건은 1·2·3에 대한 독립 IF 세 개이다. 이 값들 밖의 MTYPE에 대한 오류 처리나 ELSE는 없다.
- 117–118: MTYPE=3의 퇴적물(SED·SED1) 초기화는 세 번째 인덱스 1만 사용한다.
- 21–23·32–154: 머리말은 마스킹 셀 수심을 DXDY.INP에 넣도록 적는다. 이 루틴의 입력 파일은 MASK.INP이며 수심 변수에 대한 대입은 없다.
