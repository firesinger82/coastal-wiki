# 독립 Codex 검토 실행 시 권한 재시도 — 2026-09-12

이번 기본 sandbox 실행은 `Read-only file system (os error 30)`과 `failed to initialize in-process app-server client`로 검토 시작 전에 실패했다. PATH alias 생성 경고도 함께 있었다. 실패 메시지는 정확한 쓰기 대상 경로를 표시하지 않으므로 특정 DB·파일 하나의 고장으로 단정하지 않는다.

현재 세션은 저장소와 `/tmp` 중심의 쓰기 범위를 갖는다. `.git`, `.agents`, `.codex`는 세션 보호 대상이며, `models/XBeach/source-analysis`는 별도로 소유자 nobody·그룹 nogroup, 디렉터리 0555/문서 0444 보호가 있다. 일반 Unix 모드와 sandbox 허용 여부는 별개다. 실행한 자식 명령에도 sandbox 경계가 적용된다는 설명은 [OpenAI 공식 문서](https://learn.chatgpt.com/docs/sandboxing)를 따른다.

읽기 전용 **검토 작업**도 Codex 프로세스를 시작하기 위한 쓰기가 필요할 수 있다. 이번 명령은 외부 실행만 `require_escalated`로 재요청해 승인받았고, 검토 명령 자체의 `--sandbox read-only --ephemeral --disable multi_agent`는 유지했다. 이후 검토 이벤트에서 모델 소스 읽기가 진행됨을 확인했다.

재개 시 이 실행 유형을 기본 sandbox에서 되풀이해 실패시키지 말고, 해당 승인 규칙이 적용되는 권한 요청 경로로 실행한다. 저장된 규칙이 새 명령을 포괄하는지 확인하며 새 승인이 필요한 경우 도구의 절차를 따른다. 보호 문서 반영은 별도 manifest에 고정한 installer로 처리한다. 전체 접근 모드·전역 권한을 임의로 변경하는 설정 수정은 이번 조치에 포함하지 않았다.
