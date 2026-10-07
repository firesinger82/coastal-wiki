---
file: models/EFDC/raw/manuals/confluence/spaces/CVLKB/pages/CVLGrid_Knowledge_Base/CVLGrid_Users_Manual/Installation_and_License_Management/Installation.md
lines: 40
sha256: c5f390d16d79917c991bc7996b8d03ca49ed174a4560ee63322e09c7341e0f9d
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Installation.md — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Installation / 문서 메타데이터 — 페이지 ID `2818263`, 제목, space, 원문 URL, 버전 `3`, 갱신 시각, 문서 계층을 포함한다(1–9). |
| 10–17 | Installation / 압축 해제와 설치 시작 — `CVLGrid.ZIP`를 받은 경우 임시 디렉터리(temporary directory)에 압축을 해제한다(10). 이후 정리를 쉽게 하기 위해 비어 있는 디렉터리를 권장한다(10). 입력 파일 이름·조건 원문: `1. If you received CVLGrid in a zip file (CVLGrid.ZIP), unzip the zip file into a *temporary directory* on your hard drive. To simplify the cleanup of files later it is recommended that the *temporary directory* be empty before unzipping.` (10). 설치 프로그램 이름과 실행 원문: `2. You should use the CVLGrid Installation program to install CVLGrid (CVLGrid1.1\_Setup\_Ver160622.exe). After opening the setup program the CVLGrid Install Wizard will run as shown in [Figure 1](#Installation-Figure1) below.` (11). 직접 연 그림 1은 `CVLGrid1.1`의 `InstallShield Wizard` 시작 화면과 `Ver160622`를 보여 준다(13–14). 임시 디렉터리를 썼다면 해제한 파일을 지우고 재설치용 ZIP 사본은 보관하라고 적는다(16). 조건 원문: `3. If you used a *temporary directory* you should delete the files that were unzipped. Keep a copy of the zip file in case you need to install the program again.` (16). |
| 18–24 | Installation / 관리자 실행 가능성과 계약 동의 — Vista 또는 Windows 7 사용자는 모형 실행을 위해 `CVLGrid1.1.exe`를 관리자 권한으로 실행하도록 바꿔야 할 수도 있다(18). 조건·불확실성 원문: `4. For Vista™ and Windows 7™ users, you may need to change the CVLGrid1.1.exe to "Run as Administrator" before you can use CVLGrid to run models.` (18). 설치 전에 라이선스 계약(License Agreement)에 동의해야 한다(20). 의무 원문: `5. As part of the conditions of use of CVLGrid, the user must accept the License Agreement before installation.` (20). 직접 연 그림 2는 계약 동의 화면이며 `I do not accept the terms in the license agreement`가 선택되어 있고 `Next` 버튼이 비활성 상태다(22–23). |
| 25–31 | Installation / 사용자 정보와 설치 유형 — 사용자는 `User Name`, `Organization`을 입력한다(25). 설정 옵션(Setup Option)은 `Complete` 또는 `Custom`이다(27). `Complete`는 모든 기능을 설치하고 더 많은 디스크 공간을 요구한다(27). `Custom`은 CVLGrid 프로그램, Datafiles, Documents, Extra files 중 하나 또는 조합을 선택하도록 한다(27). 적용 옵션 원문: `7. The user is then prompted for the Setup Option desired. A choice of "Complete" or "Custom" setup options are available. "Complete" means that all setup features will be installed, requiring more disc space. The "Custom" setup option allows the user to install just one or a combination of files, including CVLGrid program file, Datafiles, Documents and Extra files.` (27). 직접 연 그림 3의 실제 화면 제목은 `Setup Type`이며 `Complete`가 선택되어 있다(29–30). |
| 32–36 | Installation / Custom과 설치 폴더 — `Custom`일 때 설치 기능을 선택하고 `Change`로 목적지 폴더(destination folder)를 바꿀 수 있다(32). 기본 폴더·예제 저장 경로 원문: `8. If the "Custom" option is used a number of features may be selected to be installed at shown in are available . Here the user may also decide on the destination folder for the setup by selecting the "Change" button. The default folder is: C:\Program Files(x86)\DSI\CVLGrid1.1\. A CVLGrid example will be saved to C:\Program Files\DSI\CVLGRID1.1\Example.` (32). 이 본문은 기본 폴더를 `C:\Program Files(x86)\DSI\CVLGrid1.1\`, 예제 경로를 `C:\Program Files\DSI\CVLGRID1.1\Example`로 적는다(32). 직접 연 그림 4는 `Custom Setup` 화면이며 `Install to:` 아래 경로가 `C:\Program Files\DSI\CVLGRID1.1\`이다(34–35행 참조 그림). 화면의 기능 설명은 `42MB`, `2 of 2 subfeatures selected`, `2496KB`를 표시한다(34행 참조 그림). |
| 37–40 | Installation / 완료 — 본문은 설치 마법사 완료 메시지 뒤 `Finish`를 누르면 바탕 화면으로 돌아간다고 적는다(37). 직접 연 그림 5는 `InstallShield Wizard Completed` 메시지와 `Finish` 버튼을 보여 준다(39–40). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 11행: `#Installation-Figure1` 내부 참조가 있다. 이 파일에는 해당 ID를 정의하는 명시 앵커가 없다.
- 29–30행: 캡션은 `Custom Setup`이라고 적지만 참조 그림 3의 화면 제목은 `Setup Type`이고 `Complete`가 선택되어 있다.
- 32·34행: 본문의 기본 폴더는 `C:\Program Files(x86)\DSI\CVLGrid1.1\`이다. 참조 그림 4의 `Install to:` 경로는 `C:\Program Files\DSI\CVLGRID1.1\`이다.
- 32행: `at shown in are available .`라는 문구에 참조 대상이 제시되지 않는다.
