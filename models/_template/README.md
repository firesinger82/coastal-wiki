# models/_template/

> **Canonical source**: 이 디렉토리(`models/<model>/`)가 해당 모델의 구현·메커닉에 대한 진실의 원천. `concepts/<topic>/06-model-application.md`는 여기로의 링크만 가짐.

새 모델 정리용 템플릿. 사용:

```bash
cp -r models/_template models/<model-name>
```

## 하위 디렉토리

| 경로 | 역할 |
|---|---|
| `source-analysis/` | 소스코드 분석 (서브루틴별, 모듈별). 파일: `<module>.md`. 인용: file:line |
| `manual-notes/` | 공식 메뉴얼 발췌·정리. 인용: 메뉴얼 페이지 |
| `web-refs/` | 공식 wiki·논문·기술 블로그 인용 정리 |

## 정체 카드 (이 README 본문에 채울 내용)

- **이름**: 
- **저자/관리주체**: 
- **라이선스**: 
- **공식 사이트**: 
- **소스 위치**: 
- **공식 메뉴얼 위치**: 
- **사용 도메인**: (수리, 표사, 파랑 등)
- **주 좌표계·격자**: 

## 작성 원칙

- 객관 자료만. 사용 경험은 `experience/`로.
- 소스코드 인용은 `<repo>/path/to/file.f90:NN` 형식
- 메뉴얼 인용은 `<manual_filename>.pdf p.NN` 형식
- 외부 자료 인용 시 URL + 접근 일자
