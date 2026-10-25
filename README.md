# ml_dl_study_material

ML/DL 학습 자료 보관소. 각 주제는 `workbooks/<주제>/` 아래에 두고, 단계별로 파일을 남긴다.

## 구조

```
workbooks/
  <topic-slug>/
    draft/      초안. 검토 전 상태. 오류가 있을 수 있음
    reviewed/   design-craft 검토를 통과한 판본
    REVIEW.md   무엇을 지적받고 무엇을 고쳤는지
```

## 목차

| 주제 | 다루는 논문 | 상태 |
|---|---|---|
| [softmax-cross-entropy](workbooks/softmax-cross-entropy/) | Barron et al., *A Fix for Softmax and Cross-Entropy* (arXiv:2610.31642) | **reviewed** (19쪽) · draft 보존 |

## 규칙

- 수치는 손으로 어림하지 않고 스크립트로 계산해 `verify_numbers.py` 로 함께 남긴다.
- 인용한 논문은 절 번호까지 적는다. 원문을 읽지 않은 참고문헌은 "원문 미확인"으로 표시한다.
- `draft/` 의 파일은 공유 전에 `reviewed/` 판본이 있는지 확인한다.
