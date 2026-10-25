# softmax와 cross-entropy의 수치 버그 — 워크북

원문: Jonathan T. Barron, Dan Gnanapragasam, Michael Tschannen.
*A Fix for Softmax and Cross-Entropy*. Google DeepMind. arXiv:[2610.31642](https://arxiv.org/abs/2610.31642) (2026-10-22, CC BY 4.0).

## 상태: DRAFT (초안)

이 디렉터리의 파일은 **초안**이다. design-craft 검토 전이므로 다음이 아직 확인되지 않았다.

- 구성·위계·밀도에 대한 디자인 리뷰
- 오탈자·문장 리듬에 대한 교정 패스
- 인쇄 판형에서의 최종 확인

검토를 마친 판본은 `../reviewed/` 에 둔다. 초안을 인용하거나 배포할 때는 이 점을 밝힌다.

## 파일

| 파일 | 설명 |
|---|---|
| `reviewed/softmax-cross-entropy-workbook.pdf` | **검토 통과본.** A4 19쪽, 러닝 푸터·쪽번호 포함 |
| `reviewed/softmax-cross-entropy-workbook.html` | 검토본 HTML 원본 |
| `reviewed/REVIEW.md` | design-craft 루브릭 리뷰 결과와 수정 내역 |
| `reviewed/stamp_pages.py` | PDF 후처리(푸터·쪽번호·메타데이터) |
| `draft/softmax-cross-entropy-workbook-draft.pdf` | 초안(수정 전, 비교용) |
| `draft/softmax-cross-entropy-workbook-draft.html` | 초안 HTML |
| `draft/verify_numbers.py` | 본문 수치 계산 스크립트 |

## 검토 이력

`draft/` → design-craft 루브릭(치명 0 · 중요 5 · 제안 6) → 중요 5건 전부 수정 + 제안 3건 반영 →
`reviewed/`. 남은 선택 3건은 `reviewed/REVIEW.md` 마지막 절에 있다.

## 대상 독자

한국 고3 수학(지수·로그·시그마·간단한 미분) + CNN/ViT를 아는 사람. 행렬 없이 3-클래스 숫자 예로만 전개한다.

## 내용 요약

1. softmax는 비교를 확률로 바꾸는 기계
2. margin — 압승의 정도를 재는 자
3. 손실의 미분은 정확히 `q − p`
4. float는 눈금이다 — 반올림 경계 `2^-p`
5. 버그 1: `1 + e^-m` 이 1.0이 되는 순간, 절벽 `c = p·ln2`
6. 버그 1의 결과: 정답 gradient만 0이 되어 합이 0이 아님
7. Adam은 0을 특별히 다룬다 → Slingshot
8. 수정 1: argmax 항을 합에서 빼고 softplus
9. 버그 2: 증류에서 두 softmax를 빼면 안 되는 이유
10. 수정 2: expm1 / log1p
11. 왜 Adam 기본값 `ε = 1e-8` 이 최악인가 — `m* ≈ log(1/ε)`

## 재현

```bash
python3 verify_numbers.py
```

PDF 재생성은 Chrome headless 로 HTML 을 인쇄한다(A4, 여백 16mm/15mm).

## 라이선스

원문은 CC BY 4.0. 이 워크북의 설명·도해·연습문제는 원문을 요약·재구성한 2차 저작물이며 같은 조건(CC BY 4.0)으로 배포한다.
