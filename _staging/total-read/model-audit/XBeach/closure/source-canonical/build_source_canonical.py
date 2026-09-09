#!/usr/bin/env python3
"""Build the approved XBeach source-supplement canonical draft and ledgers.

This builder reads the immutable supplement/crosswalk records and the live vendor
source. It never rewrites those inputs. Line numbers are counted by physical LF
bytes; CRLF files retain CR in the raw-span hash and use LF-normalized text only
for the human-readable quote/hash that is compared with the immutable manifest.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path


REPO = Path(__file__).resolve().parents[6]
AUDIT = REPO / "_staging/total-read/model-audit/XBeach"
HERE = Path(__file__).resolve().parent
SOURCE_ROOT = REPO / "models/XBeach/raw/source_code"
CANONICAL_REL = "models/XBeach/source-analysis/xbeach-source-audit-supplements.md"
CANONICAL_OUT = HERE / "canonical" / CANONICAL_REL
SHARD_RE = re.compile(r"XBeach-(00[0-5]|T00)\Z")


# key = normalized_path#audit_id. Each sentence preserves the final crosswalk
# applicability verdict; it is not a translation of the earlier finding alone.
SUMMARY_KO = {
    "trunk/src/xbeachlibrary/filefunctions.F90#B3": "헤더만 있는 LOCLIST를 이 helper가 허용하지만 spectral_wave_init가 뒤에서 위치 1개 이상을 요구해 중단한다. 경계 파일 없이 계산이 진행되는 결함이 아니라 조기 검증 누락이다.",
    "trunk/src/xbeachlibrary/initialize.F90#B4": "nx가 너무 작거나 dsu/dnv가 0인 격자를 강제 차단하지 않은 채 경계 열을 복사하고 경사를 metric으로 나눈다. XBeach의 nx 하한은 권고 검사이고 Delft3D 격자 치수는 이를 우회한다.",
    "trunk/src/xbeachlibrary/initialize.F90#B8": "WBCTYPE_PARAMS와 TS_1/TS_2에서는 비엄격 입력 검사를 통과한 Trep=0이 2π/Trep 계산에 도달할 수 있다.",
    "trunk/src/xbeachlibrary/initialize.F90#B11": "hotstart_init_1이 읽은 uu/vv를 뒤의 flow_init가 무조건 0으로 덮고 hotstart_init_2도 다시 읽지 않으므로, 저장된 hotstart 유속은 복원되지 않는다.",
    "trunk/src/xbeachlibrary/params.F90#B0": "all_input은 hotstart 입력값을 읽기 전에 기본 sentinel 값으로 depfile 필요 여부를 판정한다. 따라서 정상적인 새 hotstart 요청도 불필요하게 depfile을 요구한다.",
    "trunk/src/xbeachlibrary/params.F90#B1": "중력·주기·활성 격자간격의 0 또는 음수 값은 권고 검사만 거쳐 위험한 나눗셈과 격자 계산에 도달할 수 있다. 다만 일부 음수 dx/dy는 가변격자 metric fallback 지시이므로 일괄 오류가 아니며, 비종료 각도 정규화 주장은 성립하지 않는다.",
    "trunk/src/xbeachlibrary/params.F90#B2": "외부 Delft3D 헤더의 mmax/nmax는 읽기 성공과 Cartesian 표지만 검사한 뒤 nx/ny로 변환된다. 최소 치수 검사가 없어 작은 격자가 후속 할당·경계 인덱싱에 도달한다.",
    "trunk/src/xbeachlibrary/params.F90#B7": "tint 계열의 엄격 하한이 0이라 출력 간격 0이 허용된다. 해당 출력 종류의 자동 schedule을 실제로 켰을 때만 timestep_init의 나눗셈에 도달하며, 사용하지 않는 출력은 분모가 되지 않는다.",
    "trunk/src/xbeachlibrary/params.F90#B8": "posdwn은 허용된 작은 양수도 0.1 미만이면 -1로 바꾸고 그 이상 양수는 그대로 둔다. 이후 이산 부호 정규화가 없어 깊이 부호·크기 처리가 불연속이다.",
    "trunk/src/xbeachlibrary/readkey.F90#B3": "vector reader는 vlength를 결과 길이와 대조하지 않고 prefix만 정의한다. ngd 호출은 엄격 제한되지만 비엄격 nrugdepth는 고정 결과 용량을 넘을 수 있어 실제 overflow 경로가 남는다.",
    "trunk/src/xbeachlibrary/readkey.F90#B6": "parameter cache는 파일명 문자열이 바뀔 때만 갱신된다. 같은 경로의 파일 내용을 실행 중 바꾸고 다시 읽으면 이전 값과 used-key 상태를 계속 반환한다.",
    "trunk/src/xbeachlibrary/readkey.F90#B8": "비-master rank의 parmapply 단독 반환에서는 optional parm_str가 정의되지 않는다. 정상 all_input 경로는 이후 parameter 구조 전체를 broadcast하므로 지속적인 MPI 파라미터 손상으로 확대되지는 않는 낮은 수준의 API 계약 결함이다.",
    "trunk/src/xbeachlibrary/readkey.F90#B13": "strippedline은 입력 record의 7-bit printable ASCII 밖 바이트를 진단 없이 공백으로 바꾼다. 비ASCII 파일명과 문자열 파라미터가 cache에 들어가기 전에 변형된다.",
    "trunk/src/xbeachlibrary/spaceparams.F90#B7": "nx=1이면 alfaz 내부 계산이 비어 있고 두 경계 대입이 미정의 값을 서로 복사한다. nx 하한이 비엄격이고 외부 격자에도 강제 하한이 없어 입력 경로에서 배제되지 않는다.",
    "trunk/src/xbeachlibrary/timestep.F90#B4": "schedule에 같은 시각이 연속되면 counter는 한 번만 증가하고 다음 시각 탐색은 같은 값을 제외한다. 그 출력 종류는 뒤 시각을 놓치지만 모델 시간 루프 전체가 교착된다고 볼 근거는 없다.",
    "trunk/src/xbeachlibrary/timestep.F90#B12": "groundwater가 켜진 분기에서 kx와 조건부 ky를 직접 분모로 쓴다. 입력 하한이 권고 검사라 0·음수 permeability가 이 계산에 도달할 수 있다.",
    "trunk/src/xbeachlibrary/boundaryconditions.F90#B1": "TS_1/TS_2 reader는 nt의 I/O 성공만 확인하고 배열 할당 뒤 sum(dataE)/nt를 계산한다. 문법적으로 유효한 nt=0은 차단되지 않는다.",
    "trunk/src/xbeachlibrary/boundaryconditions.F90#B3": "Surfbeat 경계에서는 마른 경계의 평균수심 ht가 보호 없이 분모가 되는 위험이 남는다. 비정수압 경로의 수심 나눗셈은 양의 수심 불변조건으로 일부 보호되고, 유한 양수심에서 cg²=g·h의 정확 공진은 성립하지 않는다.",
    "trunk/src/xbeachlibrary/boundaryconditions.F90#B4": "지원되는 reuse/list 경계 파일의 dtbcfile은 양수 검사 없이 record 번호와 보간 분모에 쓰인다. 내부 생성기의 양수 step은 외부 reuse 파일을 보호하지 않는다.",
    "trunk/src/xbeachlibrary/boundaryconditions.F90#B10": "비정수압 경계 파일에 Z가 없으면 zi에 절대 수면 zs(2,:)를 복사한 뒤 FRONT_NONH 적용에서 zs0를 다시 더한다. taper는 이 기준수위 중복을 제거하지 않는다.",
    "trunk/src/xbeachlibrary/boundaryconditions.F90#B12": "cats·Trep 권고 하한은 비엄격이고 table의 Trep도 별도 검사하지 않아 0이면 relaxation 분모가 된다. 기본 hybrid 설정이 아니라 잘못된 사용자·외부 forcing 값에서만 발생한다.",
    "trunk/src/xbeachlibrary/boundaryconditions.F90#B15": "ny=2이면 transverse velocity의 전역 선택 구간이 비어 dnvsum=0이 될 수 있고, vdnvsum/dnvsum에 0/0이 남는다. MPI reduction은 소유권만 합치며 빈 선택을 보정하지 않는다.",
    "trunk/src/xbeachlibrary/boundaryconditions.F90#B18": "back-boundary 두 corner의 수위를 계산하면서 front row의 dzs0dn·dnv·zb를 참조한다. 뒤의 lateral 보정 범위는 이 corner를 일반적으로 덮지 않는다.",
    "trunk/src/xbeachlibrary/boundaryconditions.F90#B22": "MPI 수평 discharge segment의 두 끝점이 rank 밖에 있으면 그 rank를 가로질러도 indomain=false가 된다. 이후 endpoint clipping과 전역 면적 합산은 누락된 local momentum 적용을 복원하지 않는다.",
    "trunk/src/xbeachlibrary/wave_boundary_datastore.f90#B0": "randomseed는 scalar인데 consumer가 ALLOCATED/DEALLOCATE 대상으로 사용해 타입 계약이 맞지 않는다. 이 prototype 모듈은 확인한 build source list와 활성 call graph에 없으므로 배포 실행파일의 도달 가능한 결함이 아니라 잠재 통합 결함이다.",
    "trunk/src/xbeachlibrary/wave_boundary_main.f90#B6": "생성 배열 순서는 point,time,direction인데 consumer는 time 자리에 itheta를 고정하고 direction slice를 시간열로 넘긴다. 확인한 build와 활성 call graph에서 제외된 prototype의 잠재 통합 결함이다.",
    "trunk/src/xbeachlibrary/wave_boundary_main.f90#B7": "nonhydrostatic 생성 분기는 hydrostatic 배열을 할당하지 않지만 BUILDXBEACH 보간부는 이를 무조건 참조한다. 확인한 build와 활성 call graph에서 제외된 prototype의 잠재 통합 결함이다.",
    "trunk/src/xbeachlibrary/wave_boundary_update.f90#B10": "BUILDXBEACH가 없으면 보간부가 pdflocal과 thetagen을 정의하지 않은 채 뒤에서 정규화·사용한다. 확인한 build와 활성 call graph에서 제외된 prototype의 잠재 통합 결함이다.",
    "trunk/src/xbeachlibrary/wave_boundary_update.f90#B16": "generate_ebcf의 BUILDXBEACH logging은 scope에 없는 s%ntheta·s%ny를 참조한다. 확인한 build와 활성 call graph에서 제외된 prototype의 잠재 build 결함이다.",
    "trunk/src/xbeachlibrary/wave_boundary_update.f90#B20": "generate_qbcf가 전달받거나 선언하지 않은 s%ny로 q를 할당한다. 확인한 build와 활성 call graph에서 제외된 prototype의 잠재 build 결함이다.",
    "trunk/src/xbeachlibrary/wave_directions.F90#B5": "구형 solver는 부분 j 범위에도 full-row mask를 써 배열 extent가 달라진다. 활성 replacement는 일관된 slice를 쓰고 구형 routine은 호출되지 않으므로 현재 실행 경로의 결함은 아니다.",
    "trunk/src/xbeachlibrary/waveparams.F90#B11": "legacy makebcf의 일부 출력 모드에서는 Ampzeta 중간값이 loop 순서에 의존한다. WBCTYPE_PARAMS/JONS_TABLE은 최종 Amp를 써 우회하고, 이 legacy routine 자체도 저장소 내 호출자가 없어 도달 범위가 제한된다.",
    "trunk/src/xbeachlibrary/bedroughness.F90#B5": "infiltration ventilation이 활성일 때 cfu=0이면 regularization 전에 cfu로 나누고 뒤에서도 1/cfu를 평가한다. wetu는 수심 mask라 zero friction을 배제하지 않는다.",
    "trunk/src/xbeachlibrary/bedroughness.F90#B6": "infiltration=0이어도 비음수 분기가 blphi를 -1e-4로 바꿔 facbl을 정확히 1보다 크게 만든다. 흐름과 보통의 cfu가 있으면 작은 추가 전단이 남는다.",
    "trunk/src/xbeachlibrary/bedroughness.F90#B9": "velocity=0에서 SIGN이 양의 부호를 선택하므로 kbl이 양수인 젖은 face에는 고정 방향의 turbulent bed shear가 남을 수 있다. zero-velocity guard가 없다.",
    "trunk/src/xbeachlibrary/morphevolution.F90#B6": "pbbedu의 마지막 x face와 pbbedv의 마지막 y face를 채우지 않고 전체 배열 곱에 사용한다. 경계 transport가 0이어도 미정의 multiplier를 읽는 동작은 정의되지 않는다.",
    "trunk/src/xbeachlibrary/morphevolution.F90#B15": "suspended와 bed load의 dilatancy 보정식은 서로 다른 비선형 factor를 쓴다. 차이는 srfRhee가 0이 아니고 BDSLPEFFINI_TOTAL 밖인 경우에만 남으며, TOTAL 분기는 Ucrb를 Ucrs로 복사한다.",
    "trunk/src/xbeachlibrary/nonh.F90#B8": "y방향 vertical-viscosity flux가 V face에서 hv 대신 hu를 곱한다. wetv는 젖음만 보장하고 방향별 upwind 수심의 동일성을 보장하지 않는다.",
    "trunk/src/pybeach/xbeach/libxbeach.py#B10": "set_array의 실제 ndarray shape 검사는 assert뿐이라 Python -O에서 사라진다. 뒤의 pointer cast는 원래 배열 extent를 다시 검사하지 않는다.",
    "trunk/src/pybeach/xbeach/libxbeach.py#B12": "set_array는 알 수 없는 native type code를 거부하는 else가 없어 dtype·typename 미정의 상태로 함수명을 만든다. native type query 실패와 Python 3 byte code 불일치도 이 경로를 배제하지 않는다.",
    "trunk/src/xbeachlibrary/introspection.F90#B3": "C entry point의 length개 name buffer를 MAXSTRINGLEN까지 NUL 탐색하는 helper에 넘긴다. Python buffer는 보통 여분 NUL을 갖지만, 정확히 length byte이고 NUL이 없는 직접 C 호출은 할당 범위를 넘겨 읽을 수 있다.",
    "trunk/src/xbeachlibrary/introspection.F90#B4": "numeric getter는 이름 존재만 확인하고 parameter 실제 type을 검사하지 않는다. integer 이름을 double getter로 요청하거나 그 반대이면 연결되지 않은 component를 참조한다.",
    "trunk/src/xbeachlibrary/iso_c_utils.f90#B2": "strcmp helper는 trim과 Fortran blank-padding 때문에 NUL 앞 trailing space의 C strcmp 의미를 보존하지 않는다. 저장소 내 호출이 없어 현재 BMI 실행 실패가 아니라 잠재 호환성 결함이다.",
    "trunk/src/xbeachlibrary/libxbeach.F90#B5": "MPI library run이 0~1 step에서 끝나면 t01이 아직 정의되지 않았는데 final이 timing 출력에 넘긴다. writelog_finalize에도 초기화 여부 guard가 없다.",
    "trunk/src/xbeachlibrary/ncoutput.F90#B1": "NetCDF-only 초기화는 saved drifter counter itd를 설정하지 않지만 출력 시 이를 증가시켜 record index로 쓴다. fortoutput_init만 이 counter를 초기화한다.",
    "trunk/src/xbeachlibrary/ncoutput.F90#B5": "point variable의 앞 두 dimension이 x/y가 아니어도 알려진 dimension이면 log만 남기고 point-by-time 변수로 정의·공간 index로 sampling한다. 비공간 rank-2 변수에서 shape 계약이 깨질 수 있다.",
    "trunk/src/xbeachlibrary/ncoutput.F90#B12": "global·point·mean NetCDF 시간은 morfacopt를 보지 않고 morfac을 곱한다. 불일치는 morfacopt=0이면서 morfac>1인 허용 조합에서만 생기며 morfacopt=1에서는 의도된 변환이다.",
    "trunk/src/xbeachlibrary/ncoutput.F90#B18": "varianceupdate는 thetamean을 직접 ATAN2 각도로 저장하지만 NetCDF와 Fortran 출력은 이를 과거 packed 값처럼 다시 decode한다. 중간 collect 단계에서 repack하지 않아 각도가 손상된다.",
    "trunk/src/xbeachlibrary/ncoutput.F90#B19": "다음 mean interval 갱신이 Fortran-compatible 분기 안에만 있어 NetCDF-only의 비균일 사용자 schedule은 이전 tintm으로 평균 가중한다. 자동 생성된 고정간격 schedule에는 영향이 없다.",
    "trunk/src/xbeachlibrary/ncoutput.F90#B20": "morfacopt=1에서 drifter release/end time은 내부 hydrodynamic time으로 환산되지만 drifter NetCDF time은 raw par%t를 쓴다. morfac>1이면 같은 파일의 다른 시간축과 단위가 달라진다.",
    "trunk/src/xbeachlibrary/ncoutput.F90#B22": "integer rank-2 mean 변수도 허용되지만 Fortran mean-file record length는 항상 real pointer t%r2에서 구한다. wetz 같은 integer mean 출력에서 잘못된 component를 참조한다.",
    "trunk/src/xbeachlibrary/ncoutput.F90#B23": "global Fortran direct-access 파일을 STATUS='UNKNOWN'으로 열어 이전 run보다 적게 쓰면 높은 record가 물리적으로 남는다. dims.dat를 따르는 reader는 새 record 수를 알 수 있지만 파일 자체는 truncate되지 않는다.",
    "trunk/src/xbeachlibrary/postprocess.F90#B8": "이 helper는 전역 wetz 최소 위치 하나에서 만든 값을 모든 runup gauge에 복사해 논리가 틀리다. 활성 runup 출력은 gauge별 row를 따로 탐색하므로 현재 출력 경로가 아니라 미사용 helper의 잠재 결함이다.",
    "trunk/src/xbeachlibrary/varianceupdate.F90#B4": "원형평균의 near-zero guard는 SIGN의 magnitude 인자를 잘못 써 epsilon floor가 아니라 epsilon·abs(cos_sum)을 만든다. 보통 t=0 출력은 gate되지만 반복 zero-dt API 출력 등에서 ATAN2(0,0)를 확실히 막지 못한다.",
    "trunk/src/xbeachlibrary/xmpi.F90#B2": "processor-grid score와 1,000,000,000 sentinel이 default integer라 큰 domain에서 overflow하거나 모든 후보가 sentinel 이상이면 factorization을 선택하지 못할 수 있다. 뒤의 domain-size 검사는 이를 복구하지 못한다.",
    "trunk/src/xbeachlibrary/xmpi.F90#B3": "manual mmpi/nmpi 하한은 비엄격이라 음수 두 개가 warning만 남기고 양의 process 수 곱 검사를 통과할 수 있다. 뒤 검사도 이를 배제하지 않아 잘못된 분할 geometry와 divisor로 이어진다.",
    "trunk/scripts/generate.py#B3": "variable declaration parser는 JSON 필수 key·이름 중복·declaration rank와 shape rank 일치를 검사하지 않는다. 현재 327개 변수는 조건을 만족하지만, 향후 불일치 입력은 선언과 할당 rank가 다른 Fortran을 생성할 수 있다.",
    "trunk/scripts/generate.py#B4": "variable JSON은 파싱한 name·rank 같은 구조 필드를 검증 없이 덮을 수 있다. parameter 정규식에서는 앞의 greedy comment가 JSON을 소비해 같은 override 경로가 현재 도달되지 않으므로 변수 schema 결함으로 한정된다.",
    "trunk/src/xbeachlibrary/templates/indextos.mako#B2": "metadata를 single-quoted Fortran literal에 escape 없이 넣는다. 현재 description에는 apostrophe가 없지만 새 설명에 water's 같은 정상 문자열이 들어오면 생성 소스가 깨진다.",
    "trunk/test/testgenmodule.F90#B8": "master가 초기화 전 a·ia를 aa·iaa로 복사해 미정의 read가 발생한다. 뒤 scattertest가 영역을 덮지만, harness는 현재 xmpi 호출 signature와 맞지 않고 build manifest에도 없어 그대로 실행되는 테스트 결함은 아니다.",
}


CATEGORY = {
    "filefunctions.F90": "input-state",
    "initialize.F90": "input-state",
    "params.F90": "input-state",
    "readkey.F90": "input-state",
    "spaceparams.F90": "input-state",
    "timestep.F90": "input-state",
    "boundaryconditions.F90": "wave-boundary",
    "wave_boundary_datastore.f90": "wave-boundary",
    "wave_boundary_main.f90": "wave-boundary",
    "wave_boundary_update.f90": "wave-boundary",
    "wave_directions.F90": "wave-boundary",
    "waveparams.F90": "wave-boundary",
    "bedroughness.F90": "morphology-numerics",
    "morphevolution.F90": "morphology-numerics",
    "nonh.F90": "morphology-numerics",
    "libxbeach.py": "interfaces",
    "introspection.F90": "interfaces",
    "iso_c_utils.f90": "interfaces",
    "libxbeach.F90": "interfaces",
    "xmpi.F90": "interfaces",
    "ncoutput.F90": "output",
    "postprocess.F90": "output",
    "varianceupdate.F90": "output",
    "generate.py": "generated-schema",
    "indextos.mako": "generated-schema",
    "testgenmodule.F90": "test",
}

CATEGORY_TITLE = {
    "input-state": "입력·초기 상태·시간 제어",
    "wave-boundary": "파·흐름 경계",
    "morphology-numerics": "마찰·형태·비정수압 수치",
    "interfaces": "Python/C/BMI·MPI interface",
    "output": "출력·통계",
    "generated-schema": "생성 schema·template",
    "test": "테스트 harness",
}

RELATED = {
    "input-state": ["xbeach_params.md", "xbeach_initialize.md", "xbeach_timestep_control.md"],
    "wave-boundary": ["wave/xbeach_wave_boundary.md", "xbeach_flow_boundary_conditions.md", "xbeach_wave_boundary_generation.md"],
    "morphology-numerics": ["xbeach_bed_friction.md", "xbeach_morphology.md", "xbeach_nonh.md"],
    "interfaces": ["xbeach_infrastructure.md"],
    "output": ["xbeach_output.md"],
    "generated-schema": ["xbeach_params.md", "xbeach_infrastructure.md"],
    "test": ["xbeach_infrastructure.md"],
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def resolve_crosswalk(path: str) -> Path:
    prefix = "total-read/model-audit/XBeach/"
    if not path.startswith(prefix):
        raise ValueError(f"unexpected crosswalk path: {path}")
    return AUDIT / path[len(prefix) :]


def source_citation(path: str, lines: str) -> str:
    return f"models/XBeach/raw/source_code/{path}:{lines}"


def normalize_where(where: str | None) -> str | None:
    if not where:
        return None
    if where.startswith("models/XBeach/raw/source_code/"):
        return where.replace(":L", ":", 1)
    if where.startswith("trunk/"):
        return f"models/XBeach/raw/source_code/{where}".replace(":L", ":", 1)
    return where.replace(":L", ":", 1)


def verify_scope_evidence(neutralizer: dict | None) -> dict | None:
    """Re-extract a crosswalk neutralizer using the same physical-LF rule."""
    if neutralizer is None:
        return None
    where = neutralizer.get("where")
    match = re.fullmatch(r"(.+):L(\d+)-L?(\d+)", where or "")
    if match is None:
        raise AssertionError(f"unparseable neutralizer location: {where}")
    source_name, lo_text, hi_text = match.groups()
    lo, hi = int(lo_text), int(hi_text)
    if source_name.startswith("models/XBeach/raw/source_code/"):
        source_path = REPO / source_name
    elif source_name.startswith("trunk/"):
        source_path = SOURCE_ROOT / source_name
    else:
        raise AssertionError(f"unexpected neutralizer source: {source_name}")
    source_bytes = source_path.read_bytes()
    physical_lines = source_bytes.split(b"\n")
    if not (1 <= lo <= hi <= len(physical_lines)):
        raise AssertionError(f"neutralizer LF bounds invalid: {where}")
    raw_span = b"\n".join(physical_lines[lo - 1 : hi])
    normalized_quote = b"\n".join(
        line[:-1] if line.endswith(b"\r") else line
        for line in physical_lines[lo - 1 : hi]
    ).decode("utf-8", "strict")
    if normalized_quote != neutralizer.get("quote"):
        raise AssertionError(f"crosswalk neutralizer quote drift: {where}")
    return {
        "where": normalize_where(where),
        "source_byte_sha256": sha256(source_bytes),
        "line_start": lo,
        "line_end": hi,
        "raw_span_sha256": sha256(raw_span),
        "lf_normalized_quote": normalized_quote,
        "lf_normalized_quote_sha256": sha256(normalized_quote.encode("utf-8")),
        "matches_crosswalk_quote": True,
    }


def anchor_for(path: str, audit_id: str, source_sha: str) -> str:
    stem = Path(path).name.lower().replace(".", "-").replace("_", "-")
    return f"xb-sup-{stem}-{audit_id.lower()}-{source_sha[:8]}"


def main() -> None:
    manifest_path = AUDIT / "XBeach-supplement-manifest.json"
    decisions_path = AUDIT / "XBeach-supplement-decisions.json"
    manifest_bytes = manifest_path.read_bytes()
    decisions_bytes = decisions_path.read_bytes()
    manifest = json.loads(manifest_bytes)
    decisions = json.loads(decisions_bytes)
    approved = {}
    for decision in decisions["decisions"]:
        key = f'{decision["canonical_source_sha256"]}:{decision["audit_id"]}'
        if key in approved:
            raise AssertionError(f"duplicate human-decision stable key: {key}")
        approved[key] = decision
    rows = []

    for entry in manifest["entries"]:
        if not SHARD_RE.fullmatch(entry["shard"]):
            continue
        crosswalk_path = resolve_crosswalk(entry["crosswalk"]["path"])
        crosswalk_bytes = crosswalk_path.read_bytes()
        if sha256(crosswalk_bytes) != entry["crosswalk"]["sha256_bytes"]:
            raise AssertionError(f"crosswalk hash changed: {crosswalk_path}")
        crosswalk = json.loads(crosswalk_bytes)
        normalized_path = entry["canonical_key"]["normalized_path"]
        source_path = SOURCE_ROOT / normalized_path
        source_bytes = source_path.read_bytes()
        source_sha = sha256(source_bytes)
        if source_sha != entry["canonical_key"]["source_sha256"]:
            raise AssertionError(f"source hash changed: {source_path}")
        physical_lines = source_bytes.split(b"\n")
        newline_style = "CRLF" if source_bytes.count(b"\r\n") == source_bytes.count(b"\n") else "LF"

        for supplement in entry["supplements"]:
            if len(supplement["member_input_ids"]) != 1:
                raise AssertionError("stable key requires one audit_id per selected supplement")
            audit_id = supplement["member_input_ids"][0]
            stable_key = f"{source_sha}:{audit_id}"
            human_decision = approved.get(stable_key)
            if human_decision is None or human_decision.get("status") != "approved":
                raise AssertionError(f"selected supplement lacks human approval: {stable_key}")
            if human_decision.get("canonical_path") != normalized_path:
                raise AssertionError(f"human-decision path mismatch: {stable_key}")
            summary_key = f"{normalized_path}#{audit_id}"
            if summary_key not in SUMMARY_KO:
                raise AssertionError(f"missing Korean summary: {summary_key}")
            dispositions = [
                d
                for d in crosswalk["dispositions"]
                if audit_id in d.get("audit_ids", [])
            ]
            if len(dispositions) != 1:
                raise AssertionError(f"ambiguous crosswalk disposition: {summary_key}")
            disposition = dispositions[0]
            adversarial = disposition.get("adversarial")
            if not adversarial or adversarial.get("verdict") not in {"STANDS", "NARROWED"}:
                raise AssertionError(f"missing final adversarial verdict: {summary_key}")

            lo, hi = (int(v) for v in supplement["source_span"]["lines"].split("-"))
            if not (1 <= lo <= hi <= len(physical_lines)):
                raise AssertionError(f"LF bounds invalid: {summary_key}")
            raw_span = b"\n".join(physical_lines[lo - 1 : hi])
            normalized_quote = b"\n".join(
                line[:-1] if line.endswith(b"\r") else line
                for line in physical_lines[lo - 1 : hi]
            ).decode("utf-8", "strict")
            if normalized_quote != supplement["authoritative_quote"]:
                raise AssertionError(f"manifest quote drift: {summary_key}")
            if sha256(normalized_quote.encode("utf-8")) != supplement["source_span_hash"]:
                raise AssertionError(f"manifest quote hash drift: {summary_key}")

            category = CATEGORY[Path(normalized_path).name]
            anchor = anchor_for(normalized_path, audit_id, source_sha)
            neutralizer = adversarial.get("neutralizer")
            rows.append(
                {
                    "stable_key": stable_key,
                    "source_sha256": source_sha,
                    "audit_id": audit_id,
                    "shard": entry["shard"],
                    "source": {
                        "normalized_path": normalized_path,
                        "repo_relative_path": f"models/XBeach/raw/source_code/{normalized_path}",
                        "byte_sha256": source_sha,
                        "newline_style": newline_style,
                    },
                    "physical_lf_evidence": {
                        "line_start": lo,
                        "line_end": hi,
                        "citation": source_citation(normalized_path, f"{lo}-{hi}"),
                        "raw_span_sha256": sha256(raw_span),
                        "lf_normalized_quote": normalized_quote,
                        "lf_normalized_quote_sha256": sha256(normalized_quote.encode("utf-8")),
                        "matches_immutable_manifest_quote": True,
                    },
                    "manifest": {
                        "path": str(manifest_path.relative_to(REPO)),
                        "decision": supplement["decision"],
                        "finding_text": supplement["finding_texts"][audit_id],
                        "rationale": supplement["rationale"],
                        "source_span_hash": supplement["source_span_hash"],
                    },
                    "human_decision": {
                        "path": str(decisions_path.relative_to(REPO)),
                        "status": human_decision["status"],
                        "approver": human_decision["approver"],
                        "approved_at": human_decision["approved_at"],
                        "scope": human_decision["scope"],
                    },
                    "crosswalk": {
                        "path": str(crosswalk_path.relative_to(REPO)),
                        "byte_sha256": sha256(crosswalk_bytes),
                        "disposition": disposition["disposition"],
                        "final_adversarial_verdict": adversarial["verdict"],
                        "final_adversarial_rationale": adversarial["rationale"],
                        "neutralizer_or_scope_evidence": verify_scope_evidence(neutralizer),
                    },
                    "canonical": {
                        "category": category,
                        "summary_ko": SUMMARY_KO[summary_key],
                        "citation_status": "source-needed",
                        "anchor": f"{CANONICAL_REL}#{anchor}",
                        "related_existing_notes": [
                            f"models/XBeach/source-analysis/{name}" for name in RELATED[category]
                        ],
                    },
                }
            )

    if len(rows) != 60 or len({r["stable_key"] for r in rows}) != 60:
        raise AssertionError("selected supplement denominator/key uniqueness is not exactly 60")
    if set(SUMMARY_KO) != {
        f"{r['source']['normalized_path']}#{r['audit_id']}" for r in rows
    }:
        raise AssertionError("Korean summary key set differs from selected 60")
    counts = Counter(r["crosswalk"]["final_adversarial_verdict"] for r in rows)
    if counts != Counter({"STANDS": 40, "NARROWED": 20}):
        raise AssertionError(f"unexpected verdict denominator: {counts}")

    HERE.mkdir(parents=True, exist_ok=True)
    CANONICAL_OUT.parent.mkdir(parents=True, exist_ok=True)
    evidence = {
        "schema": "xbeach-source-supplement-evidence/v1",
        "generated_at": "2026-09-09",
        "scope": "Human-approved source supplements from XBeach-000..005 and XBeach-T00 only",
        "stable_key": "(source_sha256, audit_id)",
        "line_method": "1-based lines counted by splitting exact source bytes on LF; CR retained in raw_span_sha256 and removed only for the manifest-compatible LF-normalized quote",
        "immutable_inputs_modified": False,
        "immutable_input_sha256": {
            str(manifest_path.relative_to(REPO)): sha256(manifest_bytes),
            str(decisions_path.relative_to(REPO)): sha256(decisions_bytes),
        },
        "entry_count": len(rows),
        "verdict_counts": dict(sorted(counts.items())),
        "entries": rows,
    }
    (HERE / "evidence-ledger.json").write_text(
        json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    mapping = {
        "schema": "xbeach-source-supplement-canonical-map/v1",
        "generated_at": "2026-09-09",
        "stable_key": "(source_sha256, audit_id)",
        "entry_count": len(rows),
        "all_entries_have_concrete_anchor": all(r["canonical"]["anchor"] for r in rows),
        "citation_status": "source-needed pending final Claude review",
        "mappings": [
            {
                "stable_key": r["stable_key"],
                "source_sha256": r["source_sha256"],
                "audit_id": r["audit_id"],
                "shard": r["shard"],
                "category": r["canonical"]["category"],
                "verdict": r["crosswalk"]["final_adversarial_verdict"],
                "canonical_anchor": r["canonical"]["anchor"],
                "related_existing_notes": r["canonical"]["related_existing_notes"],
                "evidence_key": r["stable_key"],
            }
            for r in rows
        ],
    }
    (HERE / "mapping-ledger.json").write_text(
        json.dumps(mapping, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    md = [
        "---",
        'title: "XBeach 승인 소스 보충 60건 — 입력·경계·형태·interface·출력 적용 한계"',
        "topic: xbeach",
        "canonical_source: self",
        "citation_status: source-needed",
        'note_author: "Codex"',
        "note_date: 2026-09-09",
        "related:",
        "  - models/XBeach/source-analysis/xbeach_params.md",
        "  - models/XBeach/source-analysis/wave/xbeach_wave_boundary.md",
        "  - models/XBeach/source-analysis/xbeach_morphology.md",
        "  - models/XBeach/source-analysis/xbeach_infrastructure.md",
        "  - models/XBeach/source-analysis/xbeach_output.md",
        "---",
        "",
        "# XBeach 승인 소스 보충 60건",
        "",
        "> [!source-needed]",
        "> 60건 모두 원본 코드와 최종 crosswalk를 대조했지만 최종 Claude 검토 전 단계이므로 문서 상태를 `source-needed`로 둔다. `STANDS`는 인용된 조건에서 결함이 유지됨을, `NARROWED`는 최종 문장에 적은 범위에서만 유지됨을 뜻한다. 이 목록은 해당 checkout의 정적 소스 판정이며 실행 재현 결과를 뜻하지 않는다.",
        "",
        "기존 메커니즘 노트의 설명을 반복하지 않고, 승인된 보충이 추가하는 실패 조건과 적용 한계를 기록한다. 정확한 인용문·바이트 해시·crosswalk 판정은 closure의 `source-canonical/evidence-ledger.json`, 60건 전량의 앵커 대응은 `mapping-ledger.json`에 있다.",
        "",
    ]
    for category in CATEGORY_TITLE:
        md.extend(
            [
                f"## {CATEGORY_TITLE[category]}",
                "",
                "| ID | 판정 | 소스 판정과 적용 범위 | 근거 |",
                "|---|---|---|---|",
            ]
        )
        for row in (r for r in rows if r["canonical"]["category"] == category):
            anchor = row["canonical"]["anchor"].split("#", 1)[1]
            cite = row["physical_lf_evidence"]["citation"]
            md.append(
                f'| <a id="{anchor}"></a>`{row["audit_id"]}` `{row["source"]["normalized_path"]}` | '
                f'`{row["crosswalk"]["final_adversarial_verdict"]}` | '
                f'{row["canonical"]["summary_ko"]} | `{cite}` |'
            )
        related = ", ".join(
            f"[{Path(name).name}]({name})" for name in RELATED[category]
        )
        md.extend(["", f"기존 구조 설명: {related}.", ""])
    md.extend(
        [
            "## 판정 경계",
            "",
            "- 활성 build·call graph에서 제외된 prototype, 미사용 helper, 현재 build manifest 밖 test는 배포 실행파일의 기본 경로 문제로 표현하지 않았다.",
            "- 잘못된 입력·외부 forcing·특정 output mode에서만 생기는 항목은 그 조건을 각 문장에 남겼다.",
            "- `STANDS` 40건과 `NARROWED` 20건의 수는 승인 보충 처분 수이며 고유 runtime 결함 수나 실행 실패 수가 아니다.",
            "- 실행·compiler 재현을 수행하지 않았으며, 정적 소스와 최종 crosswalk 밖의 동작은 확인된 사실로 추가하지 않았다.",
            "",
        ]
    )
    CANONICAL_OUT.write_text("\n".join(md), encoding="utf-8")

    readme = f"""# XBeach source-canonical closure

이 디렉토리는 사람 승인된 source supplement 중 `XBeach-000..005`와 `XBeach-T00`의 정확한 60건만 다룬다. 기존 103건 manifest·decision·crosswalk·receipt는 수정하지 않는다.

- `evidence-ledger.json`: `(source_sha256, audit_id)`별 원본 바이트 SHA, 물리 LF 행, raw span SHA, LF 정규화 인용문·SHA, manifest와 최종 crosswalk 판정
- `mapping-ledger.json`: 60건 전량의 canonical 앵커와 기존 관련 노트
- `canonical/{CANONICAL_REL}`: 보호 경로 설치 전 canonical 초안(`citation_status: source-needed`)
- `build_source_canonical.py`: 위 세 산출물을 불변 입력에서 다시 만드는 검증 builder

검사 결과: 60/60 source byte SHA 일치, 60/60 LF 행 인용문·manifest quote SHA 일치, 60/60 crosswalk 최종 판정 존재, `STANDS=40`, `NARROWED=20`, concrete canonical anchor=60.

소스는 Fortran 모듈 22개와 test 1개가 CRLF, Python/Mako 3개가 LF이다. 행 번호는 양쪽 모두 LF byte를 기준으로 센다. CRLF source의 `raw_span_sha256`은 CR을 보존하고, `lf_normalized_quote_sha256`만 manifest의 정규화 인용문과 비교한다.

남은 검토 경계: 이 작업은 정적 source/crosswalk 통합이며 compiler·runtime 재현을 새로 수행하지 않았다. 최종 Claude 검토 전에는 `verified`로 승격하지 않는다.
"""
    (HERE / "README.md").write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    main()
