# MPICH MSI identity correction (review evidence)

이 디렉터리는 원본 MSI의 `File` 테이블을 해석해 cabinet 멤버 식별자를 실제 파일명에 연결한다. 설치하거나 PE를 실행하지 않는다. 기존 `hard-resolutions/` 파일과 원본 MSI는 수정하지 않는다.

기존 `runtime-provenance.json`이 추출한 `_1BE96E15F472462586C19E8C77FF7927`은 MSI `File` 테이블에서 `mpich2nemesisp.dll`이다. 실제 `mpich2mpi.dll`은 `_7D9F6BC68D3B438D9D6834EF34F3754F`이다. 따라서 전자를 `mpich2mpi.dll`로 간주한 XB-HARD-04의 바이너리 반증은 성립하지 않는다. 실제 `mpich2mpi.dll`의 `MPI_Comm_dup`(RVA `0x97a0`)와 `PMPI_Comm_dup`(RVA `0x10f30`)에는 초기 전달 함수 설정 실패 시 출력 포인터를 쓰지 않고 `0x10`을 반환하는 정적 분기가 있다. 이는 제공 아티팩트 안에서 “모든 복귀 경로가 출력을 정의한다”는 반증을 깨지만, XBeach 실행 파일이 이 DLL을 실제 로드했다거나 해당 분기를 실행했다는 뜻은 아니다.

XB-HARD-05가 검사한 저장소 `cxx.lib`는 MSI `File` 행 `_00D89EB1B52A45B79628A8A91613E9C1`에서 `cxx.lib`로 매핑되고, 추출 멤버와 바이트 단위 SHA-256이 같다. 그러므로 hard05의 기존 포인터 동일성 치환 근거는 제공 아티팩트에 연결된다. 이 확인도 특정 XBeach 실행 파일의 링크·로더 사용을 입증하지 않는다.

시스템 패키지를 추가하지 않고 다음 명령으로 재현할 수 있다. 현재 환경에서 Python 3.12.3, `olefile` 0.47, `libarchive.so.13`, GNU objdump 2.42를 확인했다.

```bash
cd /home/firesinger/coastal-wiki
python3 -c 'import ctypes.util, olefile; assert ctypes.util.find_library("archive"); print(olefile.__version__, ctypes.util.find_library("archive"))'
command -v objdump
python3 _staging/total-read/model-audit/XBeach/closure/local-refutations/mpich-identity/extract_mpich_identity.py
sha256sum /tmp/xbeach-mpich-identity/cxx.lib models/XBeach/raw/source_code/trunk/lib/x64/mpich/lib/cxx.lib
objdump -p /tmp/xbeach-mpich-identity/mpich2mpi.dll | grep -E 'ImageBase|MPI_Comm_dup|PMPI_Comm_dup|Export RVA'
objdump -d --start-address=0x1800097a0 --stop-address=0x1800097f0 /tmp/xbeach-mpich-identity/mpich2mpi.dll
objdump -d --start-address=0x180010f30 --stop-address=0x180010f80 /tmp/xbeach-mpich-identity/mpich2mpi.dll
```

검토 결론은 `identity-ledger.json`에 구조화했다. 이 자료는 승인 발급물이 아니다.
