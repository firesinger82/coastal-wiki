---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Mapping/Mod_Sort_Global_Soln.f90
lines: 535
sha256: e4d6e7fb33c4383beec8eca3a81025819270f208428962129987f7e0279c0c64
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Mod_Sort_Global_Soln.f90 — 판독 구간 기록

구간은 1행부터 535행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | EFDC+ 출처·저작권·GPLv2 머리말과 모듈 설명·저자·날짜 주석(1–19). `Mod_Sort_Global_Soln` 시작(21), GLOBAL·MPI 변수·매핑 모듈 사용(23–25), implicit none·save(27–29). 공개 일반 인터페이스(generic interface) Sort_Global_Soln은 real(4)·real(rkd)·integer 각각의 1·2·3차원 절차를 연결한다(31–45). contains·빈 줄(47–48). 각 절차는 매핑(mapping)에 따라 전역(global) 위치로 값을 복사하며 외부 루틴 호출은 없다. |
| 49–94 | 시작 시 21행 Mod_Sort_Global_Soln 모듈 안. 전역 1차원 L 순서로 복원한다는 주석과 `Sort_1D_Real` 시작(49–63). GLOBAL·MPI 변수·출력·매핑 사용(65–68). 반복 상한 loop_bound_1d, size_global_1d 크기의 real(4) 입력 해·integer Mapping·real(4) intent(inout) 출력 해 및 지역 변수 선언(73–80). ii=0(82). `do l = 1, loop_bound_1d` (83)에서 `ii = ii + 1` (84), l_gl=Mapping(l)(86). `if( l_gl > 0 )then` (88)이면 Soln_Global_Remapped(l_gl)에 Soln_Global_1D(ii)를 복사한다(90). 루프·루틴 종료(91–94). |
| 95–140 | 시작 시 21행 모듈 안. 주석과 `Sort_1D_Real_RK8` 시작(95–109). 작업 모듈 사용(111–114). loop_bound_1d·size_global_1d와 real(rkd) 입력/출력 해·integer Mapping 및 지역 변수 선언(119–126). ii=0(128). `do l = 1, loop_bound_1d` (129), `ii = ii + 1` (130), l_gl=Mapping(l)(132). `if( l_gl > 0 )then` (134)이면 지정된 전역 l_gl에 값을 복사한다(136). 루프·루틴 종료(137–140). |
| 141–186 | 시작 시 21행 모듈 안. 주석과 `Sort_1D_Int` 시작(141–155). 작업 모듈 사용(157–160). loop_bound_1d·size_global_1d와 integer 입력/출력 해·Mapping 및 지역 변수 선언(165–172). ii=0(174). `do l = 1, loop_bound_1d` (175), `ii = ii + 1` (176), l_gl=Mapping(l)(178). `if( l_gl > 0  )then` (180)이면 지정된 전역 l_gl에 정수 값을 복사한다(182). 루프·루틴 종료(183–186). |
| 187–240 | 시작 시 21행 모듈 안. 주석과 `Sort_2D_Real` 시작(187–204). 작업 모듈 사용(206–209). 입력 real(4) 해와 Mapping은 first_dim_size*second_dim_size 크기이고, 출력 Soln_Global_3D는 first_dim_size_gl·second_dim_size_gl의 2차원 real(4) 배열이다(214–220). 지역 변수 선언·ii=0(223–225). `do l = 2, first_dim_size_gl` (226), `do k = 1, second_dim_size_gl` (227), `ii = ii + 1` (228), l_gl=Mapping(ii)(230). `if(l_gl > 0 )then` (232)이면 Soln_Global_3D(l_gl, k)에 Soln_Global_1D(ii)를 복사한다(234). 조건·루프·루틴 종료와 빈 줄(235–240). |
| 241–294 | 시작 시 21행 모듈 안. 주석과 `Sort_2D_Real_RK8` 시작(241–258). 작업 모듈 사용(260–263). 입력 real(rkd) 해와 integer Mapping은 first_dim_size*second_dim_size 크기이고, 출력은 전역 두 차원의 real(rkd) 배열이다(268–274). 지역 변수 선언·ii=0(277–279). `do l = 2, first_dim_size_gl` (280), `do k = 1, second_dim_size_gl` (281), `ii = ii + 1` (282), l_gl=Mapping(ii)(284). `if(l_gl > 0 )then` (286)이면 전역 (l_gl,k)에 값을 복사한다(288). 조건·루프·루틴 종료와 빈 줄(289–294). |
| 295–348 | 시작 시 21행 모듈 안. 주석과 `Sort_2D_Int` 시작(295–312). 작업 모듈 사용(314–317). 입력 integer 해와 Mapping은 first_dim_size*second_dim_size 크기이고, 출력은 전역 두 차원의 integer 배열이다(322–328). 지역 변수 선언·ii=0(331–333). `do l = 2, first_dim_size_gl` (334), `do k = 1, second_dim_size_gl` (335), `ii = ii + 1` (336), l_gl=Mapping(ii)(338). `if(l_gl > 0 )then` (340)이면 전역 (l_gl,k)에 값을 복사한다(342). 조건·루프·루틴 종료와 빈 줄(343–348). |
| 349–410 | 시작 시 21행 모듈 안. 주석과 `Sort_3D_Real` 시작(349–368). 작업 모듈 사용(370–373). 입력 real(4) 해와 Mapping은 first_dim_size*second_dim_size*third_dim_size 크기이고, 출력은 전역 세 차원의 real(4) 배열이다(379–387). 지역 변수 선언·ii=0(391–393). `do l = 2, first_dim_size_gl` (394), `do k = 1, second_dim_size_gl` (395), `do nn = 1, third_dim_size_gl` (396), `ii = ii + 1` (397), l_gl=Mapping(ii)(399). `if(l_gl > 0 )then` (401)이면 Soln_Global_3D(l_gl, k, nn)에 Soln_Global_1D(ii)를 복사한다(403). 조건·루프·루틴 종료와 빈 줄(404–410). |
| 411–471 | 시작 시 21행 모듈 안. 주석과 `Sort_3D_Real_RK8` 시작(411–430). 작업 모듈 사용(432–435). 입력 real(rkd) 해와 integer Mapping은 first_dim_size*second_dim_size*third_dim_size 크기이고, 출력은 전역 세 차원의 real(rkd) 배열이다(441–449). 지역 변수 선언·ii=0(452–454). `do l = 2, first_dim_size_gl` (455), `do k = 1, second_dim_size_gl` (456), `do nn = 1, third_dim_size_gl` (457), `ii = ii + 1` (458), l_gl=Mapping(ii)(460). `if(l_gl > 0 )then` (462)이면 전역 (l_gl,k,nn)에 값을 복사한다(464). 조건·루프·루틴 종료와 빈 줄(465–471). |
| 472–535 | 시작 시 21행 모듈 안. 주석과 `Sort_3D_Int` 시작(472–491). 작업 모듈 사용(493–496). 입력 integer 해와 Mapping은 first_dim_size*second_dim_size*third_dim_size 크기이고, 출력은 전역 세 차원의 integer 배열이다(502–510). 지역 변수 선언·ii=0(514–516). `do l = 2, first_dim_size_gl` (517), `do k = 1, second_dim_size_gl` (518), `do nn = 1, third_dim_size_gl` (519), `ii = ii + 1` (520), l_gl=Mapping(ii)(522). `if(l_gl > 0 )then` (524)이면 전역 (l_gl,k,nn)에 정수 값을 복사한다(526). 조건·루프·루틴·모듈 종료와 빈 줄(527–535). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12·21: 머리말의 모듈 이름은 Mod_Gather_Soln이다. 실제 선언은 Mod_Sort_Global_Soln이다.
- 80·126·172·223·277·331·391·452·514: i·j는 아홉 절차에서 선언 후 사용되지 않는다. 세 1차원 절차의 k도 선언 후 사용되지 않는다(80·126·172).
- 88·134·180·232·286·340·401·462·524: 매핑 값의 유효성 조건은 l_gl>0이다. 출력 배열 첫 차원의 상한을 검사하는 조건은 이 파일에 없다.
- 83·129·175·226–227·280–281·334–335·394–396·455–457·517–519: 1차원 절차의 입력 순회는 1에서 시작한다. 2·3차원 절차의 바깥 순회는 2에서 시작한다. 실제 출력의 첫 인덱스는 이 반복 변수 l이 아니라 Mapping에서 얻은 l_gl이다.
- 77·90·123·136·169·182·220·234·274·288·328·342·387·403·449·464·510·526: 출력 배열은 intent(inout)이다. 각 절차에는 출력 전체 초기화가 없으며 양수 매핑에 해당하는 위치만 대입한다.
- 73–76·83·214–220·226–227·268–274·280–281·322–328·334–335·379–387·394–396·441–449·455–457·502–510·517–519: 입력 해·Mapping의 선언 크기와 반복 상한은 별도 인수로 정한다. 이 파일에는 반복 요소 수를 입력 배열 크기와 비교하는 검사가 없다.
