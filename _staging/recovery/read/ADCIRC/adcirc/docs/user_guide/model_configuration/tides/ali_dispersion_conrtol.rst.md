---
file: models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/tides/ali_dispersion_conrtol.rst
lines: 48
sha256: f470dac40736a05650ba8eaf3fbb29bb385254a1de62f0de53b5a83533dcc9d6
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# ali_dispersion_conrtol.rst — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | Ali's Dispersion Control / Version — 메타데이터·앵커·제목을 포함한다(1–8). 압축성 해양(compressible ocean)과 탄성 지구(elastic Earth)의 긴 파에 대한 분산(dispersion) 보정을 fort.24 자기 인력·하중 조석(self-attraction and loading tide) 대신 쓰는 취지와 IM 여섯째 자릿수 3 조건을 옮긴다(10–14). v55 technical preview와 이론 작업 진행 중이라는 원문 상태를 유지한다(19–24). 원문: ` **Ali's Dispersion Correction** is a correction to the dispersive behavior of ` (10); ` very long waves in a compressible ocean on an elastic Earth. It is intended to ` (11); ` be used in lieu of the self-attraction and loading tide prescribed through the ` (12); `` `fort.24 file <fort.24_file>`__. It should be used with the sixth-digit of `` (13); `` `IM <IM>`__ equal to 3 (fully implicit gravity wave term). `` (14); ` .. raw:: mediawiki ` (19); `    {{Version support box\|version=55\|relation=+\|support=tp}} ` (21); ` This is considered a technical preview in version 55. Theoretical work is still ` (23); ` ongoing. ` (24). |
| 26–48 | Controlling Dispersive Behavior — fort.15 끝의 AliDispersionControl namelist로 활성화하는 예시를 옮긴다(31–34). 예시의 부동소수점(floating-point) 기본값과 CAliDisp 기본 F, Cs 단위 m/s·음수 비활성화, Ad·Bd 이름·역할을 옮긴다(33–42). 보정식과 Mach 수(Mach number) 정의, H의 총 수심(total water depth)을 원문 그대로 옮긴다(44–48). 원문: ` \| The feature is triggered by the presence of the &AliDispersionControl namelist ` (31); ``   at the bottom of the `fort.15 file <fort.15_file>`__. Here is an example of `` (32); `   how this line is used (the following floats are the default values): ` (33); ``` \| ``&AliDispersionControl CAliDisp=T, Cs=1500.0, Ad = 0.0050189, Bd = 0.23394/`` ``` (34); ``` -  ``CAliDisp`` logical flag to turn Ali's dispersion correction on (F=false by ``` (36); `    default). ` (37); ``` -  ``Cs`` is the speed of sound in water [m/s] for the Mach number based ``` (38); `    dispersive correction. Set Cs to a negative value to turn the Mach number ` (39); `    based correction off. ` (40); ``` -  ``Ad`` the power law constant. ``` (41); ``` -  ``Bd`` the power law exponent. ``` (42); ` For the following equation: ` (44); `` :math:`Correction = 1 - \frac{Ma^2}{4} - {A_d}H^{B_d}` `` (45); `` where Ma is the Mach number (:math:`Ma = \frac{\sqrt{gH}}{Cs}`) and H is the `` (47); ` total water depth. ` (48). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
