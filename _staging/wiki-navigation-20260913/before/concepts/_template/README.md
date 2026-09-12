# concepts/_template/

새 토픽 생성용 템플릿. 다음과 같이 사용:

```bash
cp -r concepts/_template concepts/<topic-name>
cd concepts/<topic-name>
# 6개 파일 채우기
```

## 단계 파일

| 파일 | 역할 |
|---|---|
| `01-concept.md` | 정의·맥락·핵심 용어 |
| `02-theory.md` | 지배방정식·가정·차원분석 |
| `03-analysis-methods.md` | 측정·통계·처리 절차·검증 |
| `04-code-and-tools.md` | 라이브러리·툴·사용 패턴 |
| `05-examples.md` | 학습 예제 (재현 가능) |
| `06-model-application.md` | EFDC/ADCIRC/XBeach/Delft3D 적용 |

## 작성 원칙

- 모든 단언에 출처 인용
- "내 경험" 금지 (객관 자료만)
- AI 요약은 검증 단계 명시
- 짧고 명확하게. 한 파일 800줄 초과 시 분할
