# XBeach Wong2016 수치 입력 7개 전량 판독 sidecar

날짜: 2026-09-09  
범위: 기존 `manuals-preflight`에서 `partial`로 남았던 `bed.dep`/`x.grd`/`y.grd` 6개와 `chezy.txt` 1개. 원본과 기존 preflight 원장은 수정하지 않았고 모델은 실행하지 않았다.

## 완료 범위

7개 파일의 **10,258,554개 수치 토큰 전부**를 float64로 파싱했다. 비수치 토큰, ragged row, 비유한값이 하나라도 있으면 실패하도록 했으며, 각 원본의 SHA-256을 모든 byte에서 다시 계산했다. 모든 파일은 일정한 행 폭이고 NaN/Inf는 0개다.

두 사례별로 모든 셀을 색상화하고 전 셀 histogram, x/y 격자선, bed-x 분포를 생성해 직접 시각 검토했다. `chezy.txt`도 9,210,012개 셀 전체를 native index 공간에서 렌더링했다. 화면 rasterization은 픽셀을 집약할 수 있으므로 이것은 **전 토큰 기계 파싱 + 전체 공간장 시각 검토** 완료다. 사람이나 LLM이 1,025만 개 숫자 문자열을 하나씩 육안으로 읽었다는 주장은 아니다.

이 기준에서 7개는 `complete-machine-parse-and-whole-field-visual-review`로 보충할 수 있다. 기존 `manuals-read-coverage.csv`와 `remaining-incomplete-or-unread.txt`는 당시 판정을 보존하며, 이 디렉터리의 `numeric-read-receipts.jsonl`이 후속 sidecar다.

## `Bijleveld_nonh_s5`

`params.txt` SHA-256은 `0419bb692a2076b78a72ac2f0c5bcce352a8cae7cc7aee2b5e4a9db03eeab0d3`이다. 원문은 `nx=438`, `ny=628`, `depfile=bed.dep`, `xfile=x.grd`, `yfile=y.grd`, `posdwn=0`, `bedfriction=manning`, `bedfriccoef=0.02`다(각각 lines 14-15, 26-29, 32-33).

- bed/x/y는 각각 629×439 = 276,131 tokens로 `(ny+1)×(nx+1)`과 정확히 맞는다.
- x 범위 1.0–1753.5029, y 범위 1.0–3000.0. i-edge 중앙값 4, j-edge 중앙값 4이며 0 길이 edge가 없다. 셀 Jacobian은 16–48, 모두 양수다.
- bed 범위는 -20–999다. -20이 259,864개, 999가 5,188개이며 비유한값은 없다. 시각적으로 -20 배경, 중앙의 연속 경사부, 두 가늘고 긴 999 띠와 연결부가 확인된다. 999의 물리적 뜻은 이 판독만으로 이름 붙이지 않았다.
- Manning 0.02는 raw manual이 제시하는 전형값과 같고 그 문서 단위는 s/m^(1/3)이다. 이는 값·단위 대응 확인이며 사례 적합성 평가는 아니다.

## `Bijleveld_surfbeat_s200`

`params.txt` SHA-256은 `fb8e2ef37722c2623098d8977f599096ed5812b2efb07096c4cd5bc04b45e57a`이다. 원문은 `nx=400`, `ny=182`, `depfile=bed.dep`, `xfile=x.grd`, `yfile=y.grd`, `posdwn=0`, `bedfriction=chezy`, `bedfricfile=chezy.txt`다(lines 15-16, 26-29, 32-33).

- bed/x/y는 각각 183×401 = 73,383 tokens로 `(ny+1)×(nx+1)`과 정확히 맞는다.
- x 범위 -51.153729–3484.2917, y 범위 -120.8–2763.4. i-edge 중앙값 5, j-edge 중앙값 8이며 0 길이 edge가 없다. 셀 Jacobian은 39.99968–869.23, 모두 양수다. 그림에서 양 방향의 가변 격자 간격이 확인된다.
- bed 범위는 -20–999다. -20이 52,493개, 999가 1,694개다. 공간장에는 연속 경사와 U자 모양의 999 띠가 보인다.
- `chezy.txt`는 2,642×3,486 = 9,210,012 tokens이며 모델 격자 183×401과 형상이 다르다. 값은 정확히 세 종류다: 50이 7,696,267개, 12.5가 1,348,713개, 15가 165,032개. native field에는 오른쪽 12.5 띠와 내부 사선 저마찰 띠가 뚜렷하다.
- raw manual은 `bedfricfile`이 bathymetry와 같은 형식의 셀별 마찰장이라고 설명한다. 고정 source snapshot의 `initialize.F90:991-1001`은 매 레코드에서 `nx+1`개만 읽어 `ny+1`번 반복한다. 따라서 이 사례에서는 파일의 첫 183행 각각의 첫 401열만 모델 배열에 들어가며, 그 73,383개 값은 **전부 50**이다. 나머지 열과 행은 이 reader 경로에서 할당되지 않는다. 이는 파일 전량 판독으로 드러난 입력/reader 관계이며 실행 결과를 주장하지 않는다.
- raw manual에서 Chézy C의 전형 단위는 m^(1/2)/s다. 12.5/15/50의 공간 분포와 단위 체계만 확인했고 값의 물리적 적합성은 평가하지 않았다.

## `posdwn=0` 관계

두 `params.txt` 모두 `posdwn=0`이고 bed는 주로 음수다. raw parameter 문서는 positive down을 1, positive up을 -1로 정의한다. 고정 snapshot의 `initialize.F90:240-249`는 `s%zb=-s%zb*s%posdwn`을 수행하므로 이 snapshot에 그대로 적용하면 초기 bed 값이 0으로 소거된다. `params.F90`은 -1에서 1 범위를 허용해 0 자체를 입력 단계에서 거부하지 않는다. 이 불일치는 기존 XBeach 문서 discrepancy와 일치하며, 여기서는 사례 실행이나 버전 일반화 없이 정확한 입력·snapshot 관계로만 기록한다.

## 증거 파일

- `numeric-audit.json`: 모든 SHA, 크기, shape, token 수, quantile, 빈도, 비유한값, 기하, params 원문 line 및 source 근거
- `numeric-read-receipts.jsonl`: 7개 파일별 sidecar 완료 영수증과 claim boundary
- `Bijleveld_nonh_s5-spatial-review.png`
- `Bijleveld_surfbeat_s200-spatial-review.png`
- `audit_numeric_grids.py`: 전량 파싱·통계·그림 재현
- `validate_numeric_read.py` / `validation.json`: 원본 SHA, token 수, 영수증 및 그림 검증

시각 검토 관측은 위 두 사례 절에 기록했다. 그림은 모든 field cell을 입력으로 사용하지만 x/y 격자선과 bed-x scatter는 가독성을 위해 균일 index sampling을 사용한다.
