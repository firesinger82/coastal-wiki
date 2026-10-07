---
file: models/EFDC/raw/manuals/confluence/spaces/EHG/pages/EEMS_12_Tutorials/How-To_Guides_for_EE12/Getting_Started/Activating__Deactivating/Activating_with_Dongle.md
lines: 28
sha256: 02636a7f64bdc9698f655b989cb7572e4d4a745b61e60023f32df3d6a0b495a5
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Activating_with_Dongle.md — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 메타데이터와 오프라인 동글(dongle) 활성화 — 인터넷 연결 없이 USB 동글의 라이선스 파일을 사용할 수 있다고 적는다(1–10). 오프라인 라이선스는 구독형과 영구형 모두 가능하다고 적는다(10). Flexnet USB 동글 드라이버 설치가 필요할 수 있으며 동글 또는 지원팀에서 받을 수 있다고 적는다(12). USB 연결 후 Full과 Activate with a Dongle을 선택한다(13–14). 조건·불확실성 원문: `Users who require a licensed EEMS without a connection to the internet can do so with an offline license. DSI will provide the user with a USB dongle that can be plugged into their computer to provide the license file required for operation. Offline licenses can be provided for both subscription licenses as well as perpetual licenses. The steps for activation using a dongle are described below.` (10); `1. In order to use the dongle, a Flexnet USB dongle driver may need to be installed. This will be provided on the dongle, or can be requested by contacting the EEMS support team, [support@eemodelingsystem.com](mailto:support@eemodelingsystem.com)` (12); `3. Open EE10.0 from the shortcut on the desktop or with the Start button and the *Activation Wizard* form will appear as shown in [Activating with Dongle#Figure 1](https://eemodelingsystem.atlassian.net/wiki/spaces/EHG/pages/247726124#ActivatingwithDongle-Figure1). The user clicks on *Full* button, an activation form appears, as shown in [Activating with Dongle#Figure 2](https://eemodelingsystem.atlassian.net/wiki/spaces/EHG/pages/247726124#ActivatingwithDongle-Figure2). The user selects *Activate with a Dongle* option.` (14). |
| 16–23 | 라이선스 파일 선택과 활성화 — 16행의 로컬 그림 두 개를 열었다. 첫 그림은 Full 버튼, 둘째 그림은 `Activate with a Dongle`, `License File`, Browse, Activate 버튼과 선택된 `Report EEMS Usage Statistics` 상자를 보여 준다(16). Browse로 동글의 `\*.lic` 파일을 선택한 뒤 Activate를 누른다(18–22). 파일 형식 원문: ` 4. Select the *Browse* button to browse to license file ( \*.lic) in on the USB dongle drive as shown in [Activating with Dongle#Figure 3](https://eemodelingsystem.atlassian.net/wiki/spaces/EHG/pages/247726124#ActivatingwithDongle-Figure3) and select *Open*.` (18). 20행 로컬 그림은 USB 디스크의 `Lic Files (*.lic)` 선택 창이다. |
| 24–28 | 동글 제거 경고와 비활성화 — 사용 중 동글을 빼면 EE가 5분 뒤 자동으로 닫히므로 5분 안에 작업을 저장해야 한다고 적는다(24). 미연결 상태로 실행할 때도 경고를 표시한다(24). License Manager에서 Ctrl-R로 동글 라이선스를 비활성화하며 갱신된 유지보수 기간의 라이선스를 활성화하려면 필요하다고 적는다(26). 원문: `6. If the user unplugs the USB dongle during the use of EFDC+ Explorer, a warning form will appear as shown in [Activating with Dongle#Figure 5](https://eemodelingsystem.atlassian.net/wiki/spaces/EHG/pages/247726124#ActivatingwithDongle-Figure5). EE will count the time up to 5 minutes and then close automatically. So the user should save the current work within five minutes. In case the user opens EE and forgets to plug the USB dongle, a warning message will be prompted, as shown in [Activating with Dongle#Figure 6](https://eemodelingsystem.atlassian.net/wiki/spaces/EHG/pages/247726124#ActivatingwithDongle-Figure6).` (24); `7. The dongle license can be deactivated by selecting Ctrl-R from the license manager. This is required to activate a license with an updated maintenance period.` (26). 28행 로컬 그림 세 개를 열었다. 첫 그림은 `EE 11.8 PERPETUAL` 주 화면, 둘째 그림은 `You have 5 minutes to save your work after which EEMS will close.` 경고, 셋째 그림은 USB 동글 연결 요청이다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14·18·22·24행: Figure 1–6 링크의 fragment ID를 선언한 로컬 앵커가 본문에 없다. 여섯 그림은 존재한다.
