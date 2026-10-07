---
file: models/EFDC/raw/source_code/EFDC-GVC/restran.for
lines: 90
sha256: b25daf764b9de0ccb0ff7ab0eef8070aa4627488c738da9629916e680fc954ef
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# restran.for — 판독 구간 기록

구간은 1행부터 90행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | 구분 주석·RESTRAN 선언·EFDC-FULL 1.0a·수정일·변경 기록 머리말(1–17). 잔여 수송(residual transport) 파일 판독 목적을 적는다(21). EFDC.PAR·EFDC.CMN을 포함한다(25–26). |
| 30–56 | 시작 시 6행 RESTRAN 루틴 안. NTSMMT<NTSPTC이면 장치 99에서 L=2..LA의 HMP·HLPF·QSUMELPF, UHLPF·VHLPF·AHULPF·AHVLPF·SALLPF의 1..KC 층 및 ABLPF의 1..KS 층을 읽는다(30–40). ELSE는 같은 입력에 VPZ의 1..KC 층과 VPX·VPY의 1..KS 층을 추가한다(41–55). 두 분기의 ABEFF READ는 주석이다(39·53). 원문: `IF(NTSMMT.LT.NTSPTC)THEN` (30) / `DO L=2,LA` (31) / `ELSE` (41) / `DO L=2,LA` (42). |
| 57–70 | 시작 시 6행 RESTRAN 루틴 안. K=1..KC·L=2..LA에서 AHULPF·AHVLPF에 AHO를 더한다(57–62). 셀의 U 두 면과 V 두 면 값을 0.25로 평균하여 AH를 계산한다(64–69). 북쪽 면 인덱스는 LNC(L)이다(67). 원문: `DO K=1,KC` (57) / `DO L=2,LA` (58) / `AHULPF(L,K)=AHULPF(L,K)+AHO` (59) / `AHVLPF(L,K)=AHVLPF(L,K)+AHO` (60) / `DO K=1,KC` (64) / `DO L=2,LA` (65) / `AH(L,K)=0.25*(AHULPF(L,K)+AHULPF(L+1   ,K)` (66); `&             +AHVLPF(L,K)+AHVLPF(LNC(L),K))` (67). |
| 71–90 | 시작 시 6행 RESTRAN 루틴 안. NTSMMT<NTSPTC 또는 ISLTMT=2이면 VPZ의 1..KC 층과 VPX·VPY의 1..KS 층을 0으로 둔다(71–83). 907 FORMAT은 12E12.4이다(85). 구분 주석·RETURN·END를 포함한다(86–90). 원문: `IF(NTSMMT.LT.NTSPTC.OR.ISLTMT.EQ.2)THEN` (71) / `DO K=1,KC` (72) / `DO L=2,LA` (73) / `VPZ(L,K)=0.` (74) / `DO K=1,KS` (77) / `DO L=2,LA` (78) / `VPX(L,K)=0.` (79) / `VPY(L,K)=0.` (80). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32–52·85: 입력 장치는 99로 고정되어 있다. 이 파일에는 장치 99의 OPEN·CLOSE 문장이 없고 해당 READ에는 ERR·IOSTAT 지정이 없다.
- 41–54·71–83: NTSMMT≥NTSPTC이면 VPZ·VPX·VPY를 파일에서 읽는다. ISLTMT=2이면 뒤 조건에서 이 세 배열을 0으로 다시 설정한다.
