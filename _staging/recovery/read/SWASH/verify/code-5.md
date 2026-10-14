# SWASH code-5 전수 대조 기록

대조 대상은 사용자가 지정한 판독 기록 5개이다.
원문은 각 기록 frontmatter의 `file:` 경로이다.
각 구간은 `nl -ba <원문> | sed -n 'A,Bp'`로 열어 대조했다.
각 원문 출력은 200행 이하로 제한했다.
대조 범위에는 구간 표의 모든 행과 파일 끝의 코드 사실 항목을 포함했다.
구간 경계와 frontmatter는 바꾸지 않았다.
원문·노트·git은 수정하지 않았다.
모델은 실행하지 않았다.

아래의 구간 행 수는 각 기록의 구간 표에서 셌다.
코드 사실 수는 각 기록 끝의 목록에서 셌다.
원문 행 수는 각 원문 파일에서 셌다.

| 기록 | 대조 구간 행 | 대조 코드 사실 | 대조 원문 행 | 정정 | 보완 | 두 표시 모두 | 이상 없음 |
|---|---:|---:|---:|---:|---:|---:|---:|
| [SwashBCspecfile.ftn90.md](../swash/src/SwashBCspecfile.ftn90.md) | 25 | 8 | 1–932 (932행) | 4 | 20 | 3 | 12 |
| [SwashBCspectrum.ftn90.md](../swash/src/SwashBCspectrum.ftn90.md) | 10 | 6 | 1–363 (363행) | 4 | 4 | 0 | 8 |
| [SwashBackup.ftn90.md](../swash/src/SwashBackup.ftn90.md) | 10 | 3 | 1–389 (389행) | 1 | 5 | 1 | 8 |
| [SwashBndTopology.ftn90.md](../swash/src/SwashBndTopology.ftn90.md) | 4 | 2 | 1–144 (144행) | 0 | 0 | 0 | 6 |
| [SwashBotFrict.ftn90.md](../swash/src/SwashBotFrict.ftn90.md) | 23 | 6 | 1–929 (929행) | 2 | 20 | 2 | 9 |
| 합계 | 72 | 25 | 2757행 | 11 | 49 | 6 | 43 |

정정과 보완은 각 표시가 붙은 기록 행 수이다.
두 표시가 함께 붙은 6행은 정정과 보완에 각각 포함했다.
이상 없음은 두 표시가 모두 없는 기록 행 수이다.
따라서 서로 다른 대조 항목은 97개이다.

전처리 활성 규칙은 `models/SWASH/raw/source_code/swash/switch.pl`의 57–66행에서 확인했다.
`!TIMG`·`!MPI`·`!F95`·`!DOS`·`!UNIX`는 각각 `$tim`·`$mpi`·`$f95`·`$dos`·`$unx`가 `/TRUE/`에 일치할 때 행 첫머리 표시가 제거된다.
`!/Cray`·`!/SGI`·`!/impi`·`!CVIS`·`!MatL4`는 각각 `$cry`·`$sgi`·`$imp`·`$cvi`·`$mv4`가 `/TRUE/`에 일치할 때 행 첫머리 표시가 제거된다.
대상 원문 5개의 전체 행에는 이 전처리 표시가 없다.

`SwashBCspecfile`의 층 관련 주석은 blayk 인자의 층별 경계 지정 설명이다(56).
`SwashBCspectrum`과 `SwashBndTopology`에는 수직 층 방향을 설명하는 주석이 없다.
`SwashBackup`의 주석은 층 구성과 층별 속도 출력을 설명한다(133, 248, 277, 324, 353).
`SwashBackup`은 `k=1,kmax` 순서로 층별 값을 쓴다(135–136, 258, 287, 334, 363).
`SwashBackup`의 해당 주석은 최상층·최하층의 인덱스를 명시하지 않는다.
`SwashBotFrict`의 입력 주석은 u·v를 수심 평균 유속으로 정의한다(66–67).
따라서 이 대상 기록들에서는 수직 층 방향의 오기를 발견하지 않았다.

조건식·반복문·대입식의 백틱 인용을 원문과 대조했다.
인용 뒤의 단일 행 번호도 원문과 대조했다.
대상 원문의 SHA-256은 각 기록 frontmatter의 SHA-256과 일치했다.
각 기록의 구간은 원문 첫 행부터 마지막 행까지 빈틈없이 이어졌다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| SwashBCspecfile.ftn90.md:178–225 | 경고문의 1/df와 음수 밀도의 exit를 설명만 했다. | [보완] 경고문의 1./df 계산식과 exit를 원문으로 인용했다. | SwashBCspecfile.ftn90:206, 223 |
| SwashBCspecfile.ftn90.md:226–280 | 바깥 SPEC1D 분기를 이름으로만 적었다. | [보완] 바깥 조건식과 분기 전환·종료 위치를 보완했다. | SwashBCspecfile.ftn90:190, 281, 911 |
| SwashBCspecfile.ftn90.md:281–308 | 파일 종류 조건의 시작식을 생략했다. | [보완] SPEC1D 조건식과 전체 조건의 종료 위치를 보완했다. | SwashBCspecfile.ftn90:190, 281, 911 |
| SwashBCspecfile.ftn90.md:309–338 | 바깥 SWAN 분기를 이름으로만 적었다. | [보완] SWAN 조건식과 분기 전환·종료 위치를 보완했다. | SwashBCspecfile.ftn90:190, 281, 909, 911 |
| SwashBCspecfile.ftn90.md:339–357 | msc<3일 때 오류 메시지와 시험 출력을 함께 수행한다고 썼다. 바깥 조건식이 없었다. | [정정·보완] 오류는 msc<3 조건이다. 시험 출력은 별도의 ITEST>=60 조건이다. 바깥 조건식과 종료 위치를 보완했다. | SwashBCspecfile.ftn90:190, 281, 355–356, 909–911 |
| SwashBCspecfile.ftn90.md:358–400 | 바깥 SWAN 조건식과 종료 위치가 없었다. | [보완] SWAN 조건식과 분기 전환·종료 위치를 보완했다. | SwashBCspecfile.ftn90:190, 281, 909–911 |
| SwashBCspecfile.ftn90.md:401–464 | 바깥 조건식과 ELSE 없는 분기 사슬을 명시하지 않았다. 오류 수치 출력과 주석 식을 생략했다. | [보완] SWAN 조건의 범위를 보완했다. j=1/2/3 사슬과 QUANT 조건에 ELSE가 없음을 적었다. 오류 수치 출력과 rho*grav 주석을 인용했다. | SwashBCspecfile.ftn90:190, 281, 403–447, 462, 909–911 |
| SwashBCspecfile.ftn90.md:465–510 | 바깥 SWAN 분기를 이름으로만 적었다. | [보완] 바깥 조건식과 분기 전환·종료 위치를 보완했다. | SwashBCspecfile.ftn90:190, 281, 909–911 |
| SwashBCspecfile.ftn90.md:511–537 | 바깥 조건식이 없었다. NODATA/ZERO의 cycle을 인용하지 않았다. | [보완] 바깥 조건식과 반복 종료를 보완했다. cycle은 nbloc==1 조건 밖에서 실행함을 명시했다. | SwashBCspecfile.ftn90:281, 511, 520–525, 889, 909–911 |
| SwashBCspecfile.ftn90.md:538–575 | 바깥 SWAN 조건과 bsploop를 이름으로만 적었다. | [보완] 바깥 조건식과 반복문 및 종료 위치를 보완했다. | SwashBCspecfile.ftn90:190, 281, 511, 889, 909–911 |
| SwashBCspecfile.ftn90.md:576–617 | 바깥 SWAN·bsploop·mdc 블록을 이름이나 요약값으로만 적었다. | [보완] 각 바깥 조건·반복을 원문으로 인용했다. 각 블록의 종료 위치를 보완했다. | SwashBCspecfile.ftn90:281, 511, 538, 645, 677, 889, 909–911 |
| SwashBCspecfile.ftn90.md:618–644 | ITEST 조건이 스펙트럼 곱셈에도 걸리는 것처럼 썼다. 바깥 조건식과 종료 위치가 없었다. | [정정·보완] 시험 적분·출력과 조건 밖의 스펙트럼 곱셈을 구별했다. 바깥 블록의 조건식과 종료 위치를 보완했다. | SwashBCspecfile.ftn90:281, 511, 538, 636–643, 645, 677, 889, 909–911 |
| SwashBCspecfile.ftn90.md:645–678 | 바깥 mdc 조건을 이름으로만 적었다. | [보완] SWAN·bsploop·mdc 조건의 원문과 종료 위치를 보완했다. | SwashBCspecfile.ftn90:281, 511, 538, 645, 677, 889, 909–911 |
| SwashBCspecfile.ftn90.md:679–710 | 바깥 SWAN 조건과 bsploop의 원문이 없었다. | [보완] 바깥 조건식과 반복문 및 종료 위치를 보완했다. | SwashBCspecfile.ftn90:281, 511, 889, 909–911 |
| SwashBCspecfile.ftn90.md:711–752 | 바깥 SWAN·bsploop 원문과 종료 위치가 없었다. | [보완] 바깥 조건식과 반복문 및 종료 위치를 보완했다. | SwashBCspecfile.ftn90:281, 511, 889, 909–911 |
| SwashBCspecfile.ftn90.md:753–791 | 바깥 SWAN·bsploop·nfreq 조건을 이름이나 요약값으로만 적었다. | [보완] 각 바깥 조건·반복을 원문으로 인용했다. 각 블록의 종료 위치를 보완했다. | SwashBCspecfile.ftn90:281, 511, 725, 790, 889, 909–911 |
| SwashBCspecfile.ftn90.md:792–800 | 다음 노드를 nullify한다고 썼다. 바깥 조건식이 없었다. | [정정·보완] nullify 대상이 다음 노드 포인터임을 정정했다. 바깥 조건식과 종료 위치를 보완했다. | SwashBCspecfile.ftn90:281, 511, 792, 889, 909–911 |
| SwashBCspecfile.ftn90.md:801–840 | 바깥 SWAN·bsploop 원문과 종료 위치가 없었다. | [보완] 바깥 조건식과 반복문 및 종료 위치를 보완했다. | SwashBCspecfile.ftn90:281, 511, 889, 909–911 |
| SwashBCspecfile.ftn90.md:841–888 | 여러 바깥 조건식을 생략했다. 종료 행을 블록별로 구별하지 않았다. 경고 좌표 계산식을 생략했다. | [보완] 각 바깥 조건·반복의 원문과 종료 행을 보완했다. 좌표 오프셋을 더하는 경고문을 인용했다. | SwashBCspecfile.ftn90:281, 511, 804–836, 872–889, 909–911 |
| SwashBCspecfile.ftn90.md:889–913 | 바깥 SWAN·bsploop·파일 종류 조건을 이름으로만 적었다. | [보완] 바깥 조건식과 반복문 및 종료 위치를 보완했다. | SwashBCspecfile.ftn90:190, 281, 511, 889, 909–911 |
| SwashBCspecfile.ftn90.md:코드 사실 7 (394·580–607·632–634) | 방향 밀도의 하한을 1.e-10이라고 단정했다. | [정정] 양의 cosdir에서는 cosdir**ms에 하한을 적용한 뒤 cnorm을 곱한다. ELSE에서는 edir에 1.e-10을 대입한다. | SwashBCspecfile.ftn90:631–634 |
| SwashBCspectrum.ftn90.md:1–51 | wave field를 파장으로 옮겼다. | [정정] wave field를 파동장으로 정정했다. | SwashBCspectrum.ftn90:44–46 |
| SwashBCspectrum.ftn90.md:52–79 | spparm(5)에 배열 전체의 다섯 의미를 붙였다. | [정정] 다섯 의미를 spparm의 1–5번 성분에 대응시켰다. | SwashBCspectrum.ftn90:64–69 |
| SwashBCspectrum.ftn90.md:130–180 | hs 분기 사슬에 마지막 ELSE가 없다는 설명이 구간 행에 없었다. | [보완] ELSE가 없음을 구간 행에 보완했다. | SwashBCspectrum.ftn90:144–148 |
| SwashBCspectrum.ftn90.md:181–223 | 라벨 10으로 돌아가는 명령을 설명만 했다. | [보완] goto 10을 원문으로 인용했다. | SwashBCspectrum.ftn90:217–220 |
| SwashBCspectrum.ftn90.md:224–240 | 마지막 ELSE가 없음을 적지 않았다. 주기 출력문의 원문과 초 단위를 생략했다. | [보완] ELSE 부재와 종료 행을 보완했다. 두 출력문을 인용했다. | SwashBCspectrum.ftn90:224–230 |
| SwashBCspectrum.ftn90.md:241–279 | tarr·spec 해제와 조건 종료의 순서를 구별하지 않았다. | [정정] tarr 해제는 조건 안이고 spec 해제는 조건 종료 뒤임을 명시했다. | SwashBCspectrum.ftn90:243, 274–278 |
| SwashBCspectrum.ftn90.md:320–357 | 바깥 방향 분포 조건을 이름으로만 적었다. | [보완] spparm(4) 조건식과 종료 행을 보완했다. | SwashBCspectrum.ftn90:282, 357 |
| SwashBCspectrum.ftn90.md:코드 사실 6 (75–78·288–310·325) | 분포 하한을 1.e-10이라고 단정했다. | [정정] cosdir>0 조건의 하한과 ELSE의 0 대입을 구별했다. | SwashBCspectrum.ftn90:324–327 |
| SwashBackup.ftn90.md:83–130 | 노드 번호를 첫 공백 앞에 붙인다고 썼다. 파일 버전과 위치 수 계산의 원문이 없었다. | [정정·보완] 기록 위치를 ilpos+1:ilpos+4로 정정했다. 버전 헤더와 위치 수 식을 인용했다. | SwashBackup.ftn90:94–95, 101, 114 |
| SwashBackup.ftn90.md:131–174 | QUANT 수와 층 구성 출력값을 설명만 했다. | [보완] 각 분기의 고정 수와 층 구성 출력문을 인용했다. | SwashBackup.ftn90:135–151 |
| SwashBackup.ftn90.md:263–298 | 바깥 격자·활성점 조건과 루프의 원문을 생략했다. | [보완] 바깥 조건식·반복문과 각각의 종료 행을 보완했다. | SwashBackup.ftn90:211, 214–215, 220–224, 294–298, 372 |
| SwashBackup.ftn90.md:299–338 | optg 조건을 이름으로만 적었다. | [보완] optg 원문 조건식과 ELSE·종료 행을 보완했다. | SwashBackup.ftn90:211, 298, 372 |
| SwashBackup.ftn90.md:339–374 | 바깥 ELSE와 정점 루프의 원문 조건이 없었다. | [보완] optg 원문 조건과 정점 반복의 시작·종료 행을 보완했다. | SwashBackup.ftn90:211, 298, 300, 370–372 |
| SwashBotFrict.ftn90.md:136–169 | 바깥 oned·거칠기 조건을 이름으로만 적었다. | [보완] 바깥 조건식과 분기 전환·종료 위치를 보완했다. | SwashBotFrict.ftn90:100, 102, 365, 367, 927 |
| SwashBotFrict.ftn90.md:170–203 | 바깥 oned·거칠기 조건을 이름으로만 적었다. | [보완] 바깥 조건식과 분기 전환·종료 위치를 보완했다. | SwashBotFrict.ftn90:100, 102, 365, 367, 927 |
| SwashBotFrict.ftn90.md:204–264 | abs(sold-s)를 상대 차이라고 썼다. 바깥 조건식과 비수렴 exit의 인용이 없었다. | [정정·보완] 절대 차이를 eps*s와 비교함을 정정했다. 바깥 조건식과 exit를 보완했다. | SwashBotFrict.ftn90:100, 102, 237, 243–247, 365, 367, 927 |
| SwashBotFrict.ftn90.md:265–323 | 바깥 oned·irough·varfr 조건을 요약값으로만 적었다. 비수렴 exit를 생략했다. | [보완] 조건 원문과 분기 전환·종료 위치를 보완했다. 비수렴 반복 탈출을 보완했다. | SwashBotFrict.ftn90:100, 204, 208, 265, 300–324, 367, 927 |
| SwashBotFrict.ftn90.md:324–366 | 바깥 oned·거칠기 조건을 이름으로만 적었다. | [보완] 바깥 조건식과 분기 전환·종료 위치를 보완했다. | SwashBotFrict.ftn90:100, 102, 365, 367, 927 |
| SwashBotFrict.ftn90.md:367–390 | 바깥 oned 조건식과 종료 위치가 없었다. | [보완] oned 조건식과 ELSE·종료 행을 보완했다. | SwashBotFrict.ftn90:100, 367, 927 |
| SwashBotFrict.ftn90.md:391–400 | 바깥 조건을 요약값으로만 적었다. 다음 구간으로 이어지는 블록의 종료 행이 없었다. | [보완] 바깥 조건 원문과 wetv·n·m 블록의 종료 행을 보완했다. | SwashBotFrict.ftn90:100, 367, 369, 373, 393–407, 441, 920, 927 |
| SwashBotFrict.ftn90.md:401–442 | 바깥 조건과 반복을 요약값으로만 적었다. | [보완] 각 바깥 조건·반복의 원문과 종료 행을 보완했다. | SwashBotFrict.ftn90:100, 367, 369, 373, 393–407, 441, 920, 927 |
| SwashBotFrict.ftn90.md:443–480 | 바깥 oned·거칠기 조건식이 없었다. | [보완] 바깥 조건 원문과 종료 행을 보완했다. | SwashBotFrict.ftn90:100, 367, 369, 920, 927 |
| SwashBotFrict.ftn90.md:481–516 | 바깥 oned·irough·varfr 조건을 요약값으로만 적었다. | [보완] 바깥 조건 원문과 ELSE·종료 행을 보완했다. | SwashBotFrict.ftn90:100, 367, 369, 443, 447, 481, 515, 920, 927 |
| SwashBotFrict.ftn90.md:517–554 | 바깥 oned·거칠기 조건식이 없었다. | [보완] 바깥 조건 원문과 종료 행을 보완했다. | SwashBotFrict.ftn90:100, 367, 369, 920, 927 |
| SwashBotFrict.ftn90.md:555–590 | 바깥 oned·irough·varfr 조건을 요약값으로만 적었다. | [보완] 바깥 조건 원문과 ELSE·종료 행을 보완했다. | SwashBotFrict.ftn90:100, 367, 369, 517, 521, 555, 589, 920, 927 |
| SwashBotFrict.ftn90.md:591–655 | 바깥 조건식이 없었다. 비수렴 경고 후의 반복 탈출을 생략했다. | [보완] 바깥 조건 원문과 종료 행을 보완했다. 비수렴 exit를 보완했다. | SwashBotFrict.ftn90:100, 367, 369, 633–637, 920, 927 |
| SwashBotFrict.ftn90.md:656–714 | 바깥 oned·irough·varfr 조건식이 없었다. 비수렴 exit를 생략했다. | [보완] 바깥 조건 원문과 종료 행을 보완했다. 비수렴 반복 탈출을 보완했다. | SwashBotFrict.ftn90:100, 367, 369, 591, 595, 692–696, 715, 835–837, 920, 927 |
| SwashBotFrict.ftn90.md:715–775 | 바깥 조건식이 없었다. 비수렴 경고 후의 exit를 생략했다. | [보완] 바깥 조건 원문과 ELSE·종료 행을 보완했다. 비수렴 반복 탈출을 보완했다. | SwashBotFrict.ftn90:100, 367, 369, 591, 595, 715, 753–757, 835–837, 920, 927 |
| SwashBotFrict.ftn90.md:776–800 | 바깥 oned·irough·varfr 조건을 이름이나 요약값으로만 적었다. | [보완] 바깥 조건 원문과 ELSE·종료 행을 보완했다. | SwashBotFrict.ftn90:100, 367, 369, 591, 595, 715, 835–837, 920, 927 |
| SwashBotFrict.ftn90.md:801–836 | 한 줄 IF 뒤의 실행을 ELSE라고 썼다. 여러 바깥 조건식과 블록별 종료 행이 없었다. | [정정·보완] ELSE 없이 exit 여부에 따라 다음 문장을 실행함을 정정했다. 각 바깥 조건·반복의 원문과 종료 행을 보완했다. | SwashBotFrict.ftn90:100, 367, 369, 591, 595, 715, 778–835, 837, 920, 927 |
| SwashBotFrict.ftn90.md:837–876 | 바깥 oned·거칠기 조건식이 없었다. | [보완] 바깥 조건 원문과 종료 행을 보완했다. | SwashBotFrict.ftn90:100, 367, 369, 920, 927 |
| SwashBotFrict.ftn90.md:877–914 | 바깥 oned·irough·varfr 조건을 요약값으로만 적었다. | [보완] 바깥 조건 원문과 ELSE·종료 행을 보완했다. | SwashBotFrict.ftn90:100, 367, 369, 837, 841, 877, 913, 920, 927 |
| SwashBotFrict.ftn90.md:915–929 | 바깥 oned·거칠기 조건식이 없었다. | [보완] 바깥 조건 원문과 종료 행을 보완했다. | SwashBotFrict.ftn90:100, 367, 369, 920, 927 |

이상 없음으로 집계한 구간과 코드 사실은 다음과 같다.

- SwashBCspecfile.ftn90.md: 구간 1–41, 42–75, 76–137, 138–177, 914–932. 코드 사실 1, 2, 3, 4, 5, 6, 8.
- SwashBCspectrum.ftn90.md: 구간 80–129, 280–319, 358–363. 코드 사실 1, 2, 3, 4, 5.
- SwashBackup.ftn90.md: 구간 1–41, 42–82, 175–210, 211–262, 375–389. 코드 사실 1, 2, 3.
- SwashBndTopology.ftn90.md: 구간 1–41, 42–80, 81–115, 116–144. 코드 사실 1, 2.
- SwashBotFrict.ftn90.md: 구간 1–53, 54–97, 98–135. 코드 사실 1, 2, 3, 4, 5, 6.

정정 11, 보완 49, 이상 없음 43
