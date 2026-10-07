---
file: models/EFDC/raw/source_code/EFDC-GVC/valkh.for
lines: 74
sha256: 272ba6709b87e37fd0100e55812d12c2e5d6b5b69789d8ea15511d5f044197f9
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# valkh.for — 판독 구간 기록

구간은 1행부터 74행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | 머리말과 `REAL FUNCTION VALKH(HFFDG)` 입구(1–6). EFDC-FULL 1.0a·수정 이력 주석(8–17). `INCLUDE 'EFDC.PAR'` (19), `INCLUDE 'EFDC.CMN'` (20). 포함 파일 내부는 이 기록의 판독 대상이 아니다. |
| 22–31 | 시작 시 6행 VALKH 안. `IF(HFFDG.LE.0.02)THEN` (22)이면 `VALKH=HFFDG*HFFDG` (23), RETURN(24). 별도 `IF(HFFDG.GE.10.)THEN` (27)이면 VALKH=HFFDG 복사(28), RETURN(29). 각 조건 종료와 주석(25–26·30–31). |
| 32–47 | 시작 시 6행 VALKH 안. `DO NTAB=2,1001` (32)에서 `FTMPM1=FUNKH(NTAB-1)` (33), `FTMP  =FUNKH(NTAB  )` (34)으로 표 값을 복사한다. `IF(FTMPM1.LE.HFFDG.AND.HFFDG.LT.FTMP)THEN` (35)이면 선형 보간(linear interpolation) 식 `VALKH=RKHTAB(NTAB)` (36); `&   -(RKHTAB(NTAB)-RKHTAB(NTAB-1))*(FTMP-HFFDG)/(FTMP-FTMPM1)` (37)으로 반환값을 설정하고 RETURN(38). 루프 종료(40) 뒤 `IF(NTAB.EQ.1001)THEN` (42)은 단위 6/8에 RKHTAB(1001) 오류 메시지를 쓰고 STOP(43–45). |
| 48–74 | 시작 시 6행 VALKH 안. 파랑 분산(wave dispersion) 관계 표 초기화 주석(48). 501개 RKH/FRKH 표 생성식·0.02와 10 경계 조건·500개 구간 보간 예제는 모두 주석(50–67). 주석·빈 주석(68–70). `600 FORMAT(' WAVE DISPERSION TABLE OUT OF BOUNDS KH = ',E12.4)` (71), RETURN·END(73–74). 이 함수에는 CALL 문과 실행되는 표 초기화문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22–24: HFFDG<=0.02 경로는 HFFDG 제곱을 반환한다. 이 조건에는 HFFDG의 별도 하한 검사가 없다.
- 32·42–45: 표 검색 루프의 상한은 1001이다. 루프 뒤 STOP 조건은 NTAB.EQ.1001이다. 실제 루프 종료 시 변수값은 실행으로 확인하지 않았다.
- 22–40·42–46·73: 반환값 대입은 두 경계 조건과 표 구간 일치 조건 안에만 있다. 그 조건에서 RETURN하지 않고 STOP 조건도 참이 아닌 경로의 73행 앞에는 별도 VALKH 대입이 없다.
