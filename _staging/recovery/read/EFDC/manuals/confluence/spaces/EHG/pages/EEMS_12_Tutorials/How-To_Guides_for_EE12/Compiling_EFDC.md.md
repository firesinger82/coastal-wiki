---
file: models/EFDC/raw/manuals/confluence/spaces/EHG/pages/EEMS_12_Tutorials/How-To_Guides_for_EE12/Compiling_EFDC.md
lines: 134
sha256: 9849b87e8c51ce90c06868aa2ae577bf14e6c455052e45b38933e2ecf1dec271
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Compiling_EFDC.md — 판독 구간 기록

구간은 1행부터 134행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | 문서 메타데이터와 개요 — EFDC+ 실행 파일을 Visual Studio Community와 Intel OneAPI Fortran 컴파일러로 구축하는 안내다(1–10). 본문은 필요한 도구가 모두 무료로 제공된다고 서술한다(10). 이 기록은 도구의 현재 제공 상태를 조사한 결과가 아니다. |
| 12–39 | 1. Download and Install Microsoft Visual Studio Community — 다운로드·저장·설치 파일 실행 후 Desktop Development with C++ 선택이 필요하다고 적는다(12–16). 필수 옵션 원문: `Click the *Download Visual Studio* button as shown in [Figure 1](#Figure1). The form to save the setup file will appear as shown in [Figure 2](#Figure2); click the *Save File* button. Once it is downloaded, check your local drive, then double-click on the VisualStudioSetup.exe file. The process will continue from [Figure 3](#Figure3) to [Figure 4](#Figure4). The Desktop Development with C++ option must be checked as shown in [Figure 5](#Figure5), then click the *Install* button.` (16). 로컬 그림 1–5를 열었다(18·22·26·30·34). 그림 1은 다운로드 버튼, 그림 2는 `VisualStudioSetup.exe` 저장 창, 그림 3은 Continue 창, 그림 4는 설치 준비 진행 표시, 그림 5는 `Desktop development with C++` 선택과 Install 버튼을 보여 준다. Intel oneAPI Toolkit 설치 문장이 이 절 끝에 있다(38). |
| 40–67 | 2. Install Intel OneAPI — Base Toolkit의 설명과 공식 다운로드 링크를 제시한다(40–46). 이 예제의 OS·설치 방식 원문: `When the page opens, select the applicable Operating System and installer type. In this case, select the OS for Windows and Offline for the installer, as shown in [Figure 6](#Figure6).` (48). 로컬 그림 6–9를 열었다(50·56·60·64). 그림 6은 `Operating System: Windows`, `Distribution: Online & Offline (recommended)`, `Installer Type: Offline`이다(50). 그림 7은 Base Toolkit `Version 2022.1.2`, `Size 3545.92 MB`, `Date January 25, 2022`와 Download 버튼을 보여 준다(56). 그림 8은 Continue as a Guest, 그림 9는 `w_BaseKit_p_2022.1.2.154_offline.exe` 저장 창이다. |
| 68–95 | 3. Download Intel OneAPI HPC Toolkit — Base Toolkit 추가 도구에 Intel Fortran Compiler·Compiler Classic·MPI Library가 포함되며 EFDC+ MPI에 필요한 MPI 라이브러리라고 적는다(68–74). 도구 및 적용 대상 원문: `This toolkit is an add-on to the Intel® oneAPI Base Toolkit. It contains the Intel® Fortran Compiler, Intel® Fortran Compiler Classic, and Intel® MPI Library. These are necessary for MPI library of EFDC+ MPI.` (70). 예제 선택값 원문: `When the site opens, again select OS (e.g., Windows) and Installer Type (e.g., Offline), as shown in [Figure 10](#Figure10).` (76). 로컬 그림 10–13을 열었다(78·82·86·90). 그림 10은 Windows·Offline 선택 화면, 그림 11은 HPC Toolkit `Version 2022.1.2`, `Size 1246.50 MB`, `Date February 04, 2022`와 Download 버튼, 그림 12는 게스트 다운로드, 그림 13은 `w_HPCKit_p_2022.1.2.116_offline.exe` 저장 창이다. 다운로드 후 설치하라고 적는다(94). |
| 96–115 | 4. Download EFDC+ code from the DSI Github — DSI GitHub 주소와 Code·Download ZIP·압축 해제 절차를 제시한다(96–102). 로컬 그림 14–16을 열었다(104·108·112). 그림 14는 GitHub Code의 Download ZIP, 그림 15는 `EFDCPlus-main.zip` 저장, 그림 16은 압축 해제 폴더의 `EFDCPlus_MPI_10.4.sln` 파일을 보여 준다. 본문 솔루션 이름 원문: `Click the *Code* button then the *Download ZIP* button as shown in [Figure 14](#Figure14) and [Figure 15](#Figure15). Once the Zip file is downloaded to your local drive, unzip the file to see the file “EFDC+\_MPI\_10.4.sln” in the folder.` (102). |
| 116–134 | 5. Compile and Run the EFDC+ Code — 솔루션을 열어 Rebuild를 선택하고 사전 지정 디렉터리에 생성되는 실행 파일을 사용한다(116–124). 실행 파일 예시 원문: `This process may take some time, with the screen as shown in [Figure 18](#Figure18). Once it finishes, the EFDC+ executable file is generated and be located in the pre-defined directory. For example E:\EFDC\EFDC\64DP\_R\_MPI\EFDC+\_MPI\_10.4.0\_210721DP.exe` (124). 설치 폴더로 복사한 뒤 EE에서 모델을 불러와 실행 파일을 선택하는 절차 원문: `To use the EFDC+ executable file to run the EFDC model, copy the EFDC+ executable file (e.g EFDC+\_MPI\_10.4.0\_210721DP.exe) into the installation folder (e.g C:\Program Files\DSI\EEMS10.4). Open the EFDC+ Explorer, load an EFDC model, click the *Run EFDC* button from the toolbar, then browse to the new EFDC+ executable file (e.g EFDC+\_MPI\_10.4.0\_210721DP.exe ) as shown in [Figure 19](#Figure19).` (130). 로컬 그림 17–19를 열었다(120·126·132). 그림 17은 Visual Studio 솔루션의 Rebuild 메뉴, 그림 18은 빌드 출력 창, 그림 19는 EFDC+ Explorer 위 실행 콘솔이다. 이 기록에서는 컴파일·실행을 수행하지 않았다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 16·48·54·76·102·118·124·130행: `#Figure1`–`#Figure19` 링크를 사용하나 해당 ID를 선언한 앵커가 본문에 없다. 그림 캡션은 존재한다.
- 102·118·112행 그림 16: 본문 솔루션 이름은 `EFDC+\_MPI\_10.4.sln`이다. 그림의 파일명은 `EFDCPlus_MPI_10.4.sln`이다.
