---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Appendices/Appendix_A_-_EFDC_Internal_Array_Visualization_Instructions.md
lines: 73
sha256: 89c680150f991e609403a2809f8c2e1f059335e13cd2f2578699b82bfadd4d98
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Appendix_A_-_EFDC_Internal_Array_Visualization_Instructions.md — 판독 구간 기록

구간은 1행부터 73행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 문서 메타데이터 — 페이지 ID·제목·space·URL·판본·갱신 시각·문서 경로와 frontmatter 구분자를 포함한다(1–9). Appendix A / 내부 배열 시각화 켜기·끄기 — EEXPORT 서브루틴(subroutine)의 예제 코드를 수정해 EFDC 내부 배열을 시각화한다고 설명한다(10). 기능을 켜는 조건문 원문: `     IF(.TRUE..AND.JSEXPLORER.EQ.0)THEN` (12). 기능을 끄는 조건문 원문: `     IF(.FALSE..AND.JSEXPLORER.EQ.0)THEN` (16). 빈 줄을 포함한다(11·13·15·17). |
| 18–27 | 출력 종류·파일 구조 — 시간에 따라 변하지 않는 배열(time static array)과 시간에 따라 변하는 배열(time variable array)의 반복문 위치를 구분한다(18). 필수 조건 원문: `There are basic two types of output, one for time static arrays and one for those that vary as the model progresses (the standard case). Depending on the temporal nature of the array, the user must code the loops inside the IF/THEN block for time static arrays and outside/below the IF/THEN block for time variable arrays. The basic code for outputting the arrays is very simple and examples for both are shown in the text box. The user must make sure the flags are set right in order for EFDC+ Explorer to correctly handle the arrays. The EFDC\_INT.OUT file is a binary file for efficient reads and disk storage. The following is the basic structure:   ` (18). EFDC_INT.OUT은 바이너리(binary) 파일이라고 설명한다(18). 기본 구조 원문: `DimFlag, TimeFlagTwo                    Integer\*4 flags  ` (20); `ArrayName                                      One Character\*8 name to identify the array  ` (21); `The array                                        Loop over the appropriate dimensions and output the array.` (22). 코드 수정 후 재컴파일(recompile) 의무 원문: `**Remember to recompile after any changes to the source code.**` (24). 다음 예제의 캡션은 EEXPOUT 서브루틴이라고 적는다(26). 빈 줄과 캡션을 포함한다(19·23–27). |
| 28–42 | 코드 예제 / 선언·파일 열기 — INTEGER*4와 CHARACTER*8 선언, 시각화 분기, 시간 고정 배열 분기, 기존 파일 삭제와 바이너리 순차 파일 열기, 판본과 시간 변화 배열 수 쓰기를 보여 준다(29–42). 조건·유형·파일 옵션·예시값을 원문 그대로 옮긴다: `INTEGER*4 VER` (29); `CHARACTER*8 ARRAYNAME` (30); `C**********************************************************C` (31); `C` (32); `! *** INTERNAL ARRAYS` (33); `IF(.TRUE..AND.JSEXPLORER.EQ.0)THEN` (34); `! *** TIME STATIC ARRAYS` (35); `IF(N.LT.(2*NTSPTC/NPSPH(8)))THEN` (36); `OPEN(97,FILE='EFDC_INT.OUT',STATUS='UNKNOWN')` (37); `CLOSE(97,STATUS='DELETE')` (38); `OPEN(97,FILE='EFDC_INT.OUT',STATUS='UNKNOWN',` (39); `& ACCESS='SEQUENTIAL',FORM='BINARY')` (40); `WRITE(97)VER ! FILE FORMAT VERSION #` (41); `WRITE(97)1 ! # OF TIME VARYING ARRAYS` (42). 36행의 분기 조건을 계산하거나 바꾸지 않았다. 코드 블록 시작 마크업을 포함한다(28). |
| 43–57 | 코드 예제 / 플래그·시간 고정 배열 — 배열 차원 플래그(flag)와 시간 변화 플래그의 값별 뜻을 열거한다(43–50). WVKHV 예제는 플래그 0,0을 쓰고 L=2,LA 범위로 출력한다(51–56). 행별 원문: `! FLAGS: ARRAY TYPE, TIME VARIABLE` (43); `! ARRAY TYPE: 0 = L DIM'D` (44); `! 1 = L,KC DIM'D` (45); `! 2 = L,0:KC DIM'D` (46); `! 3 = L,KB DIM'D` (47); `! 4 = L,KC,NCLASS DIM'D` (48); `! TIME VARIABLE: 0 = NOT CHANGING` (49); `! 1 = TIME VARYING` (50); `WRITE(97)0,0` (51); `ARRAYNAME='WVKHV'` (52); `WRITE(97)ARRAYNAME` (53); `DO L=2,LA` (54); `WRITE(97)WVKHV(L)` (55); `ENDDO` (56); `ENDIF` (57). 이 값들은 예제의 설정이며 기본값으로 정의되어 있지 않다. |
| 58–73 | 코드 예제 / 시간 변화 배열·종료 — QQ 예제는 플래그 2,1을 쓰고 L=2,LA 및 K=0,KC 범위로 출력한다(59–66). 바깥 분기와 서브루틴을 종료한다(67–72). 행별 원문: `! *** TIME VARYING ARRAYS` (58); `WRITE(97)2,1` (59); `ARRAYNAME='QQ'` (60); `WRITE(97)ARRAYNAME` (61); `DO L=2,LA` (62); `DO K=0,KC` (63); `WRITE(97)QQ(L,K) ! Turbulent Intensity (` (64); `ENDDO` (65); `ENDDO` (66); `ENDIF` (67); `C` (68); `C*********************************************************C` (69); `C` (70); `RETURN` (71); `END` (72). 코드 블록 종료 마크업을 포함한다(73). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행의 수정 대상은 `EEXPORT`이다. 26행의 코드 캡션은 `EEXPOUT`이라고 적는다.
- 20–22행의 기본 구조는 두 플래그·배열 이름·배열이다. 예제는 그 앞에 `VER`와 시간 변화 배열 수를 쓴다(41–42).
- 29행은 `VER`를 선언한다. 41행은 `VER`를 출력하지만 이 코드 예제에는 값을 지정하는 문장이 없다.
- 36행의 `N`, `NTSPTC`, `NPSPH(8)`과 반복 범위의 `LA`, `KC`는 이 파일에서 물리적 뜻이나 설정값을 정의하지 않는다(36·54·62–63).
- 64행의 주석은 `! Turbulent Intensity (`로 끝난다. 닫는 괄호나 그 뒤 설명은 없다.
