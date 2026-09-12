---
title: "XBeach 매뉴얼 수식과 구현: 파수 보정·지형 갱신·침투"
canonical_source: self
citation_status: draft-unsourced
note_author: "Codex"
note_date: 2026-09-12
verification_method: "Kingsday/Master 원본 수식 객체·주변 문단·복원 페이지와 동결 소스의 대조; 새 주장 검토본"
---

AI 대조 노트다. 원본은 `models/XBeach/raw/source_code/trunk/doc/manual/XBeach_manual_kingsday.docx`와 `XBeach_manual_master.docx`이며, 구현은 같은 `trunk/src/xbeachlibrary/` 기준이다. 원문은 변경하지 않았다. [원본 SHA·수식 객체·페이지·코드 근거](../../../_staging/total-read/model-audit/XBeach/connectivity/build-mode-20260912/contracts.json)를 함께 기록했다.

## (2.5)~(2.10): 파수 보정과 파랑–흐름 상호작용

두 판본의 식 (2.5)는 이전 스텝 파수에 보정량을 더하는 관계다. 위첨자의 네모 위치에는 원본 MathType 데이터의 `∼` 문자가 있고, 식 바로 뒤 문단이 이 항을 **파수 보정량**으로 정의한다. 따라서 이 기호의 모델 의미는 보정량으로 읽을 수 있다. 글꼴 렌더의 네모 현상 자체를 수정했다는 뜻은 아니다. (두 DOCX 복원본 물리 p.19, 식 (2.5)와 직후 문단; 기존 [문자 판독 근거](../../../_staging/total-read/model-audit/XBeach/connectivity/manuals-docx-read/glyph-record-read/receipt.json))

이어지는 식 (2.6)은 Eikonal 관계, (2.7)은 파수 벡터의 크기, (2.8)은 고유 주파수에 흐름의 Doppler 항을 더한 절대 주파수다. (2.9)~(2.10)은 전파·굴절 속도를 설명한다. 현재 코드에서는 `wave_dispersion`의 `kmx/kmy`, `km`, `s%wm`이 이 역할에 대응하지만 다음 구현 조건까지 보아야 한다. (동일 p.19; `wave_functions.F90:978-1108`)

- `wci==1`에서만 파수 보정 경로를 실행한다. 먼저 평균 파향과 격자 방향의 차이로 `kmx/kmy`를 구성한다. 분산 계산의 호출 인수 0/1/2에 따라 순간장·방향 계산용 평균장·비정상 WCI 평균장을 선택한다. (`wave_functions.F90:978-1021`; `wave_timestep.F90:75-114`)
- 절대 주파수의 흐름 항에는 `hwci/hwcimax`를 이용한 수심 가중이 있다. 파수 갱신에는 `dkmydx-dkmxdy` 교차 미분 항도 있고, 이후 `km<=25`, 유한 파고 보정과 고유 주파수 하한이 적용된다. 매뉴얼의 간결한 식을 이 전체 이산 구현과 직접 동일시하지 않는다. (`wave_functions.F90:1022-1091`)
- 방향별 전파 속도에는 WCI 유속을 더하고, 굴절 속도에는 수심 경사와 유속 경사 항을 적용한다. 최종 방향 속도는 `0.5*pi/Trep` 크기로 제한한다. (`wave_functions.F90:1176-1211`)

## B.37 / C.37: 지형 갱신과 `sourcesink`

Kingsday B.37과 Master C.37의 첫 줄은 원본 객체와 페이지 모두 `0a`로 끝나고, 둘째 줄은 `0`으로 끝난다. 주변 문단은 첫째 식을 부유사·소류사 수송량의 발산으로, 둘째 식을 부유사의 침식–퇴적항과 소류사 발산으로 설명한다. `a`의 저자 의도는 이 문맥에 정의되어 있지 않으므로 원문을 임의로 고치지 않는다. (Kingsday 복원본 물리 p.135 / 인쇄 p.134; Master 복원본 물리 p.138 / 인쇄 p.135; 각 B.5/C.5와 식 B.37/C.37)

현재 구현의 대응은 다음과 같다. 여기서 `dzg`는 입경별 **침식 방향을 양수로 둔 바닥 변화량**이다.

| 입력 | 계산하는 항 | 이후 지형 갱신 |
|---|---|---|
| `sourcesink==0` | 부유사와 소류사의 면 수송량 차이에 격자 면적 역수를 곱함 | `morfac*dt/(1-por)`를 곱해 `dzg` 계산 |
| `sourcesink==1` | `ero-depo_ex`와 소류사 면 수송량 차이 | 같은 계수를 곱해 `dzg` 계산 |

한 입경에서는 `zb=zb-sum(dzg)`로 갱신한다. 그러므로 양의 수송 발산/침식은 바닥을 낮추며, 이 대응 경로에는 별도의 `a` 의존 항이 없다. 다입경은 `update_fractions`로 이어지고, `ny==0` 분기에는 `lsgrad`에 의한 연안방향 기여가 남는다. `0a`를 삭제하거나 저자 의도를 단정하지 않아도 구현의 부호·공극률·형태 가속계수 계약은 확인할 수 있다. (`morphevolution.F90:731-804`; 실행 시간과 `morfac` guard는 `:640-644`)

## 불포화 침투식: 판본 표기와 시간 이산화

원본 WMF와 MathType Native 판독에서 Kingsday `oleObject133`, Master `oleObject143/81`의 분수 뒤 `1` 앞에는 연산자가 없다. Kingsday `oleObject70` 대응식에는 `+1`이 있다. 이 차이는 원본의 표기 차이로 남긴다. 구현이 더하기를 쓴다는 사실로 원본 저자의 미기재 의도를 확정하거나 원본 식을 수정하지 않는다. ([원본 객체·주변 문단·코드와 대수 검산](../../../_staging/total-read/model-audit/XBeach/connectivity/infiltration-document-code-comparison.json), [객체별 복원 PDF p.1 시각 판독](../../../_staging/total-read/model-audit/XBeach/connectivity/manuals-docx-read/conditional-visual-read/receipt.json))

`groundwater.F90:1554-1573`의 기본 관계는 다음과 같다. `d=dinfil`, `h=hh`, `D=dt/por`로 놓으며, 여기서 `D`는 시간 이산화 계수다.

```text
w = K (1 + h/(d + D w))
D w² + (d − D K) w − K(d+h) = 0
w = (−d + D K + sqrt(d² + 2D dK + 4D hK + D² K²))/(2D)
```

이 양의 근은 `K>0, d>0, h>=0, D>0`에서 코드의 계산과 대수적으로 대응한다. 층류 분기와 난류 첫 추정에는 `par%kz`, 난류 반복에는 갱신한 `kze`가 들어간다. 기존 세 수치 예의 대수 잔차는 0 또는 약 `3.4e-17`이었으며, 이는 전체 Fortran 실행 시험이 아니다. (`groundwater.F90:1574-1630`; 위 대수 검산 기록)

실제 반환 `infil`은 이 순간 식의 `w` 그대로가 아니다. 코드가 불포화 상태로 남는 시간 비율 `fracdt`를 `[0,1]`로 제한하고 `infil=vest*fracdt`를 계산하므로, 반환량은 전체 스텝에 대한 평균 침투속도다. 이어 표층 가용수 `max((hh-eps)/dt,0)`로 제한한다. 호출은 비연결·젖은 셀에서 지하수위가 바닥 아래일 때이며, 양의 `infil`은 해수→지하수 방향이다. 침투층 깊이는 양의 침투 때 `dt*infil/por`만큼 증가하고 그 외에는 리셋된다. (`groundwater.F90:1631-1643, 610-638, 283-285`; [[xbeach_groundwater]])

이 노트는 위 세 수식 묶음의 대응을 기록한다. 전체 매뉴얼 수식의 검증이나 새로운 사람 승인을 뜻하지 않는다.
