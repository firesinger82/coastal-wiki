# SWASH code-49 — 10-15 전수 검증

검증일은 2026-10-15이다.
각 기록의 frontmatter `file:`이 가리키는 원문을 대조했다.
원문의 각 구간은 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
한 번에 연 원문 구간은 모두 200행 이하였다.

대조한 구간 행 수는 각 기록의 구간 표에서 센 값이다.
대조한 원문 행 수는 공백과 주석을 포함한 전체 행 수이다.
부가 사실 행 수는 각 기록의 ‘판독 중 확인된 코드 사실’ 목록에서 센 값이다.

| 기록 | 대조한 구간 행 | 대조한 원문 행 | 부가 사실 행 | 정정 | 보완 | 이상 없음 |
|---|---:|---:|---:|---:|---:|---:|
| [SwashUpdFlowFlds.ftn90.md](../swash/src/SwashUpdFlowFlds.ftn90.md) | 10 | 307 | 3 | 1 | 9 | 1 |
| [SwashUpdKBCrigb.ftn90.md](../swash/src/SwashUpdKBCrigb.ftn90.md) | 19 | 734 | 4 | 0 | 19 | 0 |
| [SwashUpdPress.ftn90.md](../swash/src/SwashUpdPress.ftn90.md) | 7 | 262 | 3 | 0 | 7 | 0 |
| [SwashUpdUDepu.ftn90.md](../swash/src/SwashUpdUDepu.ftn90.md) | 6 | 315 | 3 | 0 | 6 | 0 |
| [SwashUpdUFlowFlds.ftn90.md](../swash/src/SwashUpdUFlowFlds.ftn90.md) | 3 | 125 | 2 | 0 | 3 | 0 |
| [SwashUpdUPress.ftn90.md](../swash/src/SwashUpdUPress.ftn90.md) | 3 | 116 | 0 | 1 | 3 | 0 |
| 합계 | 48 | 1,859 | 15 | 2 | 47 | 1 |

정정과 보완은 표시가 붙은 구간 행을 유형별로 한 번씩 센 값이다.
정정 2행은 보완 47행에도 포함된다.
이상 없음 1행은 `SwashUpdFlowFlds.ftn90.md:1–41`이다.
구간 표 밖의 부가 사실 15행도 해당 원문과 대조했다.
부가 사실 15행에는 수정할 오류를 찾지 못했다.

기록 경로의 공통 접두사는 `_staging/recovery/read/SWASH/swash/src/`이다.
원문 경로의 공통 접두사는 `models/SWASH/raw/source_code/swash/src/`이다.
다음 표의 원문 행은 같은 이름의 `.ftn90` 파일을 가리킨다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [SwashUpdFlowFlds.ftn90.md:42–74](../swash/src/SwashUpdFlowFlds.ftn90.md) | ient의 초기값을 서술만 함. | 보완. ient 선언의 초기값을 원문으로 인용함. | 54 |
| [SwashUpdFlowFlds.ftn90.md:75–95](../swash/src/SwashUpdFlowFlds.ftn90.md) | nm/nmd 매핑식을 생략함. 94행 else를 백틱으로 인용하지 않음. | 보완. 두 포인터 대입식을 원문으로 인용함. 94행 `else`를 원문으로 인용함. | 87–88·94 |
| [SwashUpdFlowFlds.ftn90.md:96–140](../swash/src/SwashUpdFlowFlds.ftn90.md) | 바깥 조건식과 루프 범위를 생략함. 포인터·영구 건조점·초기화 플래그 대입식을 서술만 함. | 보완. 바깥 조건식과 반복 범위를 인용함. 포인터·영구 건조점·플래그 대입식을 인용함. | 75·79·94·98–108·118–139 |
| [SwashUpdFlowFlds.ftn90.md:141–160](../swash/src/SwashUpdFlowFlds.ftn90.md) | nm와 u1 대입식을 서술만 함. | 보완. 두 대입식을 원문으로 인용함. 루프 종료 행을 명시함. | 151–157 |
| [SwashUpdFlowFlds.ftn90.md:161–205](../swash/src/SwashUpdFlowFlds.ftn90.md) | 바깥 조건식과 반복 범위를 생략함. nm/ndm·u1 대입식의 인용이 없음. lstag(2) 참 분기를 원문에 설명이 없는 엇갈림 격자 입력으로 단정함. | 보완·정정. 바깥 조건식·반복 범위·포인터 대입식·u1 복사 및 0 대입을 인용함. 169행 대입으로 확인되는 uxf의 직접 복사 경로로 설명함. | 141·145·157·163–184·202–204·161–169 |
| [SwashUpdFlowFlds.ftn90.md:206–232](../swash/src/SwashUpdFlowFlds.ftn90.md) | 바깥 조건식을 생략함. udep·층별 u1·inituf 대입식을 서술만 함. | 보완. 바깥 조건식과 세 대입식을 인용함. k 루프 종료 행을 명시함. | 141·215–231 |
| [SwashUpdFlowFlds.ftn90.md:233–250](../swash/src/SwashUpdFlowFlds.ftn90.md) | nm와 v1 대입식을 서술만 함. | 보완. 두 대입식을 원문으로 인용함. | 243–245 |
| [SwashUpdFlowFlds.ftn90.md:251–275](../swash/src/SwashUpdFlowFlds.ftn90.md) | 바깥 조건식과 반복 범위 및 포인터 대입식을 생략함. | 보완. 바깥 조건식·반복 범위·포인터 대입식을 인용함. | 233·237·251–260·270–274 |
| [SwashUpdFlowFlds.ftn90.md:276–307](../swash/src/SwashUpdFlowFlds.ftn90.md) | 바깥 조건식을 생략함. v1·vdep·initvf 대입식을 서술만 함. | 보완. 바깥 조건식과 대입식을 인용함. lstag 및 k 루프의 종료 행을 명시함. | 233·237·274·278–305 |
| [SwashUpdKBCrigb.ftn90.md:1–83](../swash/src/SwashUpdKBCrigb.ftn90.md) | ient의 초기값을 서술만 함. | 보완. ient 선언의 초기값을 원문으로 인용함. | 54 |
| [SwashUpdKBCrigb.ftn90.md:84–108](../swash/src/SwashUpdKBCrigb.ftn90.md) | theta·skc·격자 포인터 대입식을 서술만 함. | 보완. 각 대입식을 원문으로 인용함. | 90–105 |
| [SwashUpdKBCrigb.ftn90.md:109–126](../swash/src/SwashUpdKBCrigb.ftn90.md) | 바깥 조건식과 반복 범위를 생략함. 강체 번호 대입식을 서술만 함. | 보완. 바깥 조건식과 반복 범위 및 강체 번호 대입식을 인용함. | 94·98·111·125·732 |
| [SwashUpdKBCrigb.ftn90.md:127–166](../swash/src/SwashUpdKBCrigb.ftn90.md) | 바깥 조건식과 l 대입식을 생략함. 두 IF의 종료 위치를 생략함. | 보완. 바깥 조건식·반복 범위·l 대입식과 독립된 IF의 종료 행을 명시함. | 94·98·129–165·258·732 |
| [SwashUpdKBCrigb.ftn90.md:167–207](../swash/src/SwashUpdKBCrigb.ftn90.md) | 바깥 조건식과 l 대입식 인용을 생략함. IF 종료 행과 flou 방향 주석을 생략함. | 보완. 바깥 조건식·반복 범위·l 대입식·IF 종료 행과 flou 부호를 보완함. | 94·98·169–206·258·732 |
| [SwashUpdKBCrigb.ftn90.md:208–258](../swash/src/SwashUpdKBCrigb.ftn90.md) | 바깥 조건식과 l 대입식 인용을 생략함. IF 종료 행과 flos 방향 주석을 생략함. | 보완. 바깥 조건식·반복 범위·l 대입식·IF 종료 행과 flos 부호를 보완함. | 94·98·210–258·732 |
| [SwashUpdKBCrigb.ftn90.md:259–286](../swash/src/SwashUpdKBCrigb.ftn90.md) | 바깥 조건식을 생략함. 다섯 포인터 대입식을 서술만 함. | 보완. 바깥 조건식·포인터 대입식·루프와 조건의 종료 행을 명시함. | 94·98·258–276·729–732 |
| [SwashUpdKBCrigb.ftn90.md:287–306](../swash/src/SwashUpdKBCrigb.ftn90.md) | 바깥 조건식과 반복 범위 및 l 대입식 인용이 없음. flou 부호 주석을 생략함. | 보완. 조건식·반복 범위·종료 행·l 대입식과 flou 부호를 명시함. | 94·260·264–265·289·299·729–732 |
| [SwashUpdKBCrigb.ftn90.md:307–350](../swash/src/SwashUpdKBCrigb.ftn90.md) | 바깥 조건식과 l 대입식 인용이 없음. 내부 IF 종료 행과 flos 부호 주석을 생략함. | 보완. 바깥 조건식·반복 범위·l 대입식·IF 종료 행과 flos 부호를 명시함. | 94·260·264–265·309–349·729–732 |
| [SwashUpdKBCrigb.ftn90.md:351–374](../swash/src/SwashUpdKBCrigb.ftn90.md) | 바깥 조건식과 l 대입식 인용이 없음. 내부 IF 종료 행을 생략함. | 보완. 바깥 조건식·반복 범위·l 대입식과 IF 종료 행을 명시함. | 94·260·264–265·355·371·729–732 |
| [SwashUpdKBCrigb.ftn90.md:375–394](../swash/src/SwashUpdKBCrigb.ftn90.md) | 바깥 조건식과 l 대입식 인용이 없음. flos 부호 주석을 생략함. | 보완. 바깥 조건식·반복 범위·종료 행·l 대입식과 flos 부호를 명시함. | 94·260·264–265·377·387·729–732 |
| [SwashUpdKBCrigb.ftn90.md:395–416](../swash/src/SwashUpdKBCrigb.ftn90.md) | 바깥 조건식과 l 대입식 인용이 없음. flos 부호 주석을 생략함. | 보완. 바깥 조건식·반복 범위·종료 행·l 대입식과 flos 부호를 명시함. | 94·260·264–265·399·409·729–732 |
| [SwashUpdKBCrigb.ftn90.md:417–459](../swash/src/SwashUpdKBCrigb.ftn90.md) | 바깥 조건식과 l 대입식 인용이 없음. IF 종료 행과 flov 부호 주석을 생략함. | 보완. 바깥 조건식·반복 범위·l 대입식·IF 종료 행과 flov 부호를 명시함. | 94·260·264–265·419–458·729–732 |
| [SwashUpdKBCrigb.ftn90.md:460–511](../swash/src/SwashUpdKBCrigb.ftn90.md) | 바깥 조건식과 l 대입식 인용이 없음. IF 종료 행과 flos 부호 주석을 생략함. | 보완. 바깥 조건식·반복 범위·l 대입식·IF 종료 행과 flos 부호를 명시함. | 94·260·264–265·462–510·729–732 |
| [SwashUpdKBCrigb.ftn90.md:512–539](../swash/src/SwashUpdKBCrigb.ftn90.md) | 바깥 조건식과 l 대입식 인용이 없음. IF 종료 행과 flou 부호 주석을 생략함. | 보완. 바깥 조건식·반복 범위·l 대입식·IF 종료 행과 flou 부호를 명시함. | 94·260·264–265·516·524·538·729–732 |
| [SwashUpdKBCrigb.ftn90.md:540–591](../swash/src/SwashUpdKBCrigb.ftn90.md) | 바깥 조건식과 l 대입식 인용이 없음. IF 종료 행과 flos 부호 주석을 생략함. | 보완. 바깥 조건식·반복 범위·l 대입식·IF 종료 행과 flos 부호를 명시함. | 94·260·264–265·542–590·729–732 |
| [SwashUpdKBCrigb.ftn90.md:592–622](../swash/src/SwashUpdKBCrigb.ftn90.md) | 바깥 조건식과 l 대입식 인용이 없음. IF 종료 행과 flou/flov 부호 주석을 생략함. | 보완. 바깥 조건식·반복 범위·l 대입식·IF 종료 행과 flou/flov 부호를 명시함. | 94·260·264–265·596·613·621·729–732 |
| [SwashUpdKBCrigb.ftn90.md:623–674](../swash/src/SwashUpdKBCrigb.ftn90.md) | 바깥 조건식과 l 대입식 인용이 없음. IF 종료 행과 flos 부호 주석을 생략함. | 보완. 바깥 조건식·반복 범위·l 대입식·IF 종료 행과 flos 부호를 명시함. | 94·260·264–265·625–673·729–732 |
| [SwashUpdKBCrigb.ftn90.md:675–734](../swash/src/SwashUpdKBCrigb.ftn90.md) | 바깥 조건식과 l 대입식 인용이 없음. IF 종료 행과 flos 부호 주석을 생략함. | 보완. 바깥 조건식·반복 범위·l 대입식·IF 종료 행과 flos 부호를 명시함. | 94·260·264–265·677–725·729–732 |
| [SwashUpdPress.ftn90.md:1–81](../swash/src/SwashUpdPress.ftn90.md) | ient의 초기값을 서술만 함. | 보완. ient 선언의 초기값을 원문으로 인용함. | 56 |
| [SwashUpdPress.ftn90.md:82–118](../swash/src/SwashUpdPress.ftn90.md) | 수위점과 경계의 kgrpnt 포인터 대입식을 생략함. | 보완. 포인터 대입식과 m 루프 종료 행을 명시함. | 96–113 |
| [SwashUpdPress.ftn90.md:119–156](../swash/src/SwashUpdPress.ftn90.md) | 바깥 조건식과 네 포인터 및 patm(1) 대입식의 인용이 없음. | 보완. 바깥 조건식·포인터·patm(1) 대입식과 루프 종료 행을 명시함. | 84·88·118·129–148 |
| [SwashUpdPress.ftn90.md:157–185](../swash/src/SwashUpdPress.ftn90.md) | 바깥 조건식을 생략함. 경계 포인터와 압력 복사식을 서술만 함. | 보완. 바깥 조건식·경계 포인터·압력 복사식과 블록 종료 행을 명시함. | 84·88·118·161–178·215–217 |
| [SwashUpdPress.ftn90.md:186–218](../swash/src/SwashUpdPress.ftn90.md) | 바깥 조건식을 생략함. 경계 포인터와 압력 복사식을 서술만 함. | 보완. 바깥 조건식·경계 포인터·압력 복사식과 블록 종료 행을 명시함. | 84·88·118·184·190–217 |
| [SwashUpdPress.ftn90.md:219–243](../swash/src/SwashUpdPress.ftn90.md) | 조건 밖이라는 설명에 조건식과 종료 행이 없음. 경계 포인터 대입식을 생략함. | 보완. 종료된 입력장 조건식과 경계 포인터 대입식 및 x 경계 블록 종료 행을 명시함. | 84·217·230–242 |
| [SwashUpdPress.ftn90.md:244–262](../swash/src/SwashUpdPress.ftn90.md) | 바깥 조건식을 축약함. 경계 포인터 대입식과 블록별 종료 행의 연결이 없음. | 보완. 바깥 조건식·포인터 대입식과 각 블록의 종료 행을 명시함. | 221·223·228·248–262 |
| [SwashUpdUDepu.ftn90.md:1–95](../swash/src/SwashUpdUDepu.ftn90.md) | ient의 초기값을 서술만 함. | 보완. ient 선언의 초기값을 원문으로 인용함. | 63 |
| [SwashUpdUDepu.ftn90.md:96–140](../swash/src/SwashUpdUDepu.ftn90.md) | 구조체 포인터 연결식과 좌우 셀 및 hu 대입식을 서술만 함. | 보완. 포인터 연결식·좌우 셀·hu 대입식과 IF 및 루프 종료 행을 명시함. | 100–113·121·135–139 |
| [SwashUpdUDepu.ftn90.md:141–176](../swash/src/SwashUpdUDepu.ftn90.md) | 바깥 조건식의 부정을 인용하지 않음. 보간 계수와 셀 및 hu 대입식을 서술만 함. | 보완. `if ( .not.depcds ) then`과 대입식을 원문으로 인용함. 분기 종료 행을 명시함. | 104·141·147–175 |
| [SwashUpdUDepu.ftn90.md:177–202](../swash/src/SwashUpdUDepu.ftn90.md) | 고차 보정 주석의 위치 표현을 생략함. 계수·정점·셀 대입식을 서술만 함. | 보완. 셀 외심이라는 주석과 실제 hu(iface) 대입 대상을 구분함. 계수·정점·셀 대입식을 인용함. | 104·175·177–197·254·307 |
| [SwashUpdUDepu.ftn90.md:203–255](../swash/src/SwashUpdUDepu.ftn90.md) | 바깥 조건식·반복 범위와 정점·초기값·셀·면적 대입식의 인용이 없음. | 보완. 조건식·반복 범위·각 대입식·exit 대상과 블록 종료 행을 명시함. | 180·187·199·207–240·309–313 |
| [SwashUpdUDepu.ftn90.md:256–315](../swash/src/SwashUpdUDepu.ftn90.md) | 바깥 조건식·반복 범위와 정점·초기값·셀·면적 대입식의 인용이 없음. | 보완. 조건식·반복 범위·각 대입식·exit 대상과 블록 종료 행을 명시함. | 180·187·199·260–293·309–315 |
| [SwashUpdUFlowFlds.ftn90.md:1–73](../swash/src/SwashUpdUFlowFlds.ftn90.md) | ient의 초기값을 서술만 함. | 보완. ient 선언의 초기값을 원문으로 인용함. | 56 |
| [SwashUpdUFlowFlds.ftn90.md:74–100](../swash/src/SwashUpdUFlowFlds.ftn90.md) | 포인터 연결식·셀 정점 대입식·initsf 대입식을 서술만 함. | 보완. 포인터 연결식과 각 대입식을 원문으로 인용함. | 78–79·89–97 |
| [SwashUpdUFlowFlds.ftn90.md:101–125](../swash/src/SwashUpdUFlowFlds.ftn90.md) | 정점·법선·초기화 플래그 대입식을 서술만 함. | 보완. 대입식을 원문으로 인용함. 앞선 조건의 식과 종료 행을 명시함. | 81·99·107–121 |
| [SwashUpdUPress.ftn90.md:1–73](../swash/src/SwashUpdUPress.ftn90.md) | 수위 보정 목적에서 `if appropriate`를 누락함. ient 초기값을 서술만 함. | 정정·보완. 수위 보정의 적용 조건을 복원함. ient 초기값을 원문으로 인용함. | 40–41·60 |
| [SwashUpdUPress.ftn90.md:74–98](../swash/src/SwashUpdUPress.ftn90.md) | 구조체 포인터 연결식과 셀 정점 대입식을 서술만 함. | 보완. 포인터 연결식과 셀 정점 대입식을 원문으로 인용함. | 78–79·89–91 |
| [SwashUpdUPress.ftn90.md:99–116](../swash/src/SwashUpdUPress.ftn90.md) | 경계 면·셀·경계 유형 대입식을 서술만 함. | 보완. 각 대입식을 원문으로 인용함. 입력장 갱신 조건식과 종료 행을 명시함. | 81·97·105–108 |

`models/SWASH/raw/source_code/swash/switch.pl:57–66`의 대상 표지는 `!TIMG`, `!MPI`, `!F95`, `!DOS`, `!UNIX`, `!/Cray`, `!/SGI`, `!/impi`, `!CVIS`, `!MatL4`이다.
대상 원문 여섯 파일에는 이 표지로 시작하는 행이 없다.
대상 원문 여섯 파일에는 `!DIFF`, `!MUD`, `!TEST`, `!VEGE`로 시작하는 행도 없다.

대상 원문 여섯 파일에는 `k=1`을 최상층으로 명시하는 주석이 없다.
`SwashUpdFlowFlds.ftn90:219·293`의 주석은 수직으로 균일한 속도를 가정한다.
`SwashUpdFlowFlds.ftn90:217–225·291–299`는 두 번째 인덱스가 1인 속도를 `k=2`부터 `kmax`까지 복사한다.
`SwashUpdUDepu.ftn90:213–218·266–271`의 k 루프는 면의 두 정점과 다른 셀 정점을 찾는다.

보조 기계 검사는 조건문·분기문·반복문·대입문 491개를 각 구간의 백틱 인용과 대조했다.
491개는 여섯 원문에서 각각 76·213·70·94·22·16개를 센 값이다.
보조 기계 검사는 인용 문자열과 바로 붙은 원문 행 번호에서 불일치를 찾지 못했다.
구간 경계와 frontmatter는 작업 전 내용과 일치한다.
구간 표 밖의 기록 내용은 작업 전 내용과 일치한다.
여섯 원문의 SHA-256은 작업 전 값과 일치한다.
모델은 실행하지 않았다.

정정 2, 보완 47, 이상 없음 1
