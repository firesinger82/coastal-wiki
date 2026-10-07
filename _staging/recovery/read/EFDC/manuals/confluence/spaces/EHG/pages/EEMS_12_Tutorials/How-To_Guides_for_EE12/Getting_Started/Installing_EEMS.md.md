---
file: models/EFDC/raw/manuals/confluence/spaces/EHG/pages/EEMS_12_Tutorials/How-To_Guides_for_EE12/Getting_Started/Installing_EEMS.md
lines: 53
sha256: 515d593e2eee227143f9e6967c8d7234473ae5cea2001c9c4e5acb45199b7788
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Installing_EEMS.md — 판독 구간 기록

구간은 1행부터 53행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 메타데이터와 설치 파일 — ZIP을 받았으면 빈 임시 디렉터리에 압축을 푸는 것을 권고하고 지정 설치 프로그램을 사용한다(1–11). 설치 파일 이름·조건 원문: `1. If you received EEMS10.3 in a zip file (EEMS10.3\_SetupRel210611.zip), unzip the zip file into a *temporary directory* on your hard drive. To simplify the cleanup of files later it is recommended that the *temporary directory* be empty before unzipping.` (10); `2. You should use the EEMS10.3 Installation program to install EEMS10.3 (EEMS10.3\_SetupRel210611.exe). After opening the setup program the EEMS Install Wizard will run as shown in [Figure 1](#Figure1) below.` (11). 임시 디렉터리를 사용했으면 압축 해제 파일을 삭제하고 재설치용 ZIP 사본을 보관하라고 적는다(17). 13행 로컬 그림 1을 열었다. 그림은 EEMS InstallShield Wizard의 환영·Next 화면이다. 이 기록에서는 설치나 삭제를 실행하지 않았다. |
| 18–30 | 사용권 동의와 고객 정보 — 설치 전에 End-User Agreement에 동의해야 한다(19). `User Name`과 `Organization`을 입력하고 Next를 누른다(25). 의무와 입력 이름 원문: `4. As part of the conditions of use of EEMS, the user must accept the End-User Agreement before installation.` (19); ` 5. The user is then prompted for customer information. Please enter your User Name and Organization in the fields provided, then click *Next* button.` (25). 21·27행 로컬 그림 2·3을 열었다. 그림 2는 라이선스 동의 선택, 그림 3은 `User Name: Daniel`, `Organization: DSI`의 예시 입력 화면이다. |
| 31–42 | 설치 디렉터리와 Setup Type — 기본 경로를 사용하거나 Change로 바꾼다(31). EEMS10.3 패키지는 Windows 64 bit에만 설치할 수 있다고 적는다(31). Complete는 모든 기능을 설치하며 Custom은 프로그램·자료·문서·추가 파일 일부를 선택한다(37). 조건·선택 의미 원문: `6. After clicking *Next* button, a form for setting the destination folder for installation of EEMS, and the example models appear. The user either chooses the default destination or change the destination as needed by clicking the *Change* button. Note that EEMS10.3 of the EEMS10.3 setup package can be installed on Windows 64 bit only.` (31); `7. After the destination folder has been selected, the user should click the *Next* button where they will be prompted to select a setup option. A choice of “Complete” or “Custom” setup options are available. “Complete” means that all setup features will be installed, requiring more disc space. The “Custom” setup option allows the user to install just one or a combination of files, including EEMS program files, data files, documents, and extra files.` (37). 33·39행 로컬 그림 4·5를 열었다. 그림 4의 경로는 `Install EEMS10 to: C:\Program Files\DSI\EEMS10.3\`, `Install EEMS8.5 to: C:\Program Files (x86)\DSI\EEMS8.5\`, `The EEMS Examples will be installed to: C:\EEMS\`이다(33행 그림). 그림 5는 Complete를 선택한 Setup Type 화면이다. |
| 43–53 | Custom Setup와 완료 — Custom에서 기능·경로를 선택하며 기본 폴더와 예제 경로를 명시한다(43). 기본값·조건 원문: `8. If the “Custom” option is used a number of features may be selected to be installed. Here the user may also decide on the destination folder for the setup by selecting the *Change* button. The default folder is: C:\Program Files\DSI\EEMS10.3\. An example test case will also be saved to C:\EEMS.` (43). 45·51행 로컬 그림 6·7을 열었다. 그림 6은 EEMS10.3·DSIActivationService·CVLGrid1.1·Grid_Example·Documents·EFDC_Explorer10.3 등의 기능 트리와 설치 경로를 보여 준다. 그림 7은 설치 완료·Finish 화면이다. Finish로 마치고 바탕화면으로 돌아간다고 적는다(49). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 11행: `#Figure1` 링크를 사용하지만 해당 ID를 선언한 로컬 앵커가 없다. Figure 1 캡션과 그림은 존재한다.
