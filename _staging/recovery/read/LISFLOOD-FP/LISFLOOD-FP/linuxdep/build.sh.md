---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/linuxdep/build.sh
lines: 42
sha256: b5222fb9640d5a4dc13f63fcf98110c49547301ac72d2f2c61e64d1b43aada99
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# build.sh — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–19 | 빌드 디렉터리(build directory) 설정은 `BUILD_DIR=~/netcdf_build_intel` (1)이다. `# http://www.unidata.ucar.edu/software/netcdf/docs/getting_and_building_netcdf.html` (3), `# http://www.hdfgroup.org/HDF5/release/obtainsrc.html` (4), `# cd ~/${BUILD_DIR}` (5), `# wget http://zlib.net/zlib-1.2.8.tar.gz` (6), `# wget http://www.hdfgroup.org/ftp/HDF5/current/src/hdf5-1.8.14.tar.gz` (7), `# wget ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4.3.2.tar.gz` (8)는 문서 주소·이동·다운로드 예시 주석이다. `#tar zxvf zlib-1.2.8.tar.gz` (10), `#tar zxvf hdf5-1.8.14.tar.gz` (11), `#tar zxvf netcdf-4.3.2.tar.gz` (12)도 압축 해제 명령을 주석 처리한 줄이다. 실제 경로 설정은 `RELEASE_DIR=${BUILD_DIR}/release` (14), `ZLIB_SOURCE=${BUILD_DIR}/zlib-1.2.8` (16), `HDF5_SOURCE=${BUILD_DIR}/hdf5-1.8.14` (17), `NETCDF_SOURCE=${BUILD_DIR}/netcdf-4.3.2` (18)이다. `zlib-1.2.8`, `hdf5-1.8.14`, `netcdf-4.3.2` 버전을 그대로 사용한다. 빈 줄도 포함한다. |
| 20–31 | 디렉터리 생성 명령은 `mkdir ${RELEASE_DIR}` (20)이다. 컴파일러 환경 설정은 `export CC=icc` (22), `export CFLAGS='-O3 -xHost -ip'` (23), `export CXX=icpc` (24), `export CXXFLAGS='-O3 -xHost -ip'` (25)이다. `#cd ${ZLIB_SOURCE}` (27), `#./configure --prefix=${RELEASE_DIR}` (28), `#make check install` (29)는 zlib 디렉터리 이동·설정·검사 설치 명령을 주석 처리한 줄이다. 나머지는 빈 줄이다. |
| 32–42 | HDF5 설정 명령은 `cd ${HDF5_SOURCE}` (32), `./configure --with-zlib=${RELEASE_DIR} --prefix=${RELEASE_DIR}` (33)이다. `#make check install` (34), `#make install` (35)는 검사·설치 명령을 주석 처리한 줄이다. NetCDF 설정은 `cd ${NETCDF_SOURCE}` (38) 다음 연속 명령 `CPPFLAGS="-I${RELEASE_DIR}/include" \` (39), `LDFLAGS="-L${RELEASE_DIR}/lib" \` (40), `./configure --prefix=${RELEASE_DIR}` (41)로 수행한다. 이어서 `make check install` (42)를 실행하는 스크립트이다. 36·37행은 빈 줄이다. 이 판독에서는 스크립트를 실행하지 않았다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–35·38–42: zlib의 디렉터리 이동·설정·검사 설치 명령과 HDF5의 검사 설치 명령은 주석이다. NetCDF의 `make check install`은 주석이 아니다.
- 20: 디렉터리 생성 명령은 `mkdir ${RELEASE_DIR}`이며 `-p` 옵션이 없다.
