#!/usr/bin/env python3
"""raw.pdf 에 러닝 푸터(제목 · 쪽번호)를 찍어 최종 PDF 를 만든다.

Chrome headless 인쇄는 @page margin box(CSS)를 지원하지 않으므로 쪽번호는
렌더 후 PDF 에 직접 찍는다. 표지(1쪽)는 제외한다.

푸터는 ASCII + helv(베이스14)로만 쓴다. 한글 푸터를 넣으려면 NotoSansCJK 를
임베드해야 하는데, 이 TTC 는 MuPDF subsetter 가 처리하지 못해 PDF 가 15MB 가
된다(실측). 본문은 이미 한글이므로 푸터만 영문으로 두는 편이 낫다.

    python3 stamp_pages.py raw.pdf softmax-cross-entropy-workbook.pdf
"""
import sys

import pymupdf

TITLE = "softmax / cross-entropy  ·  arXiv:2610.31642"
GRAY = (0.365, 0.392, 0.408)
RULE = (0.84, 0.88, 0.90)


def main(src: str, dst: str) -> None:
    doc = pymupdf.open(src)
    total = doc.page_count
    for i, page in enumerate(doc):
        if i == 0:  # 표지
            continue
        w, h = page.rect.width, page.rect.height
        y = h - 30
        page.draw_line(pymupdf.Point(45, y - 12), pymupdf.Point(w - 45, y - 12),
                       color=RULE, width=0.5)
        page.insert_text(pymupdf.Point(45, y + 2), TITLE,
                         fontname="helv", fontsize=7, color=GRAY)
        label = f"{i + 1} / {total}"
        tw = pymupdf.get_text_length(label, fontname="helv", fontsize=7.5)
        page.insert_text(pymupdf.Point(w - 45 - tw, y + 2), label,
                         fontname="helv", fontsize=7.5, color=GRAY)
    doc.set_metadata({"title": "softmax와 cross-entropy의 수치 버그 — 스텝바이스텝 워크북",
                      "author": "kimhs950627", "subject": "arXiv:2610.31642 워크북",
                      "keywords": "softmax, cross-entropy, numerical stability, grokking"})
    doc.save(dst, garbage=4, deflate=True)
    print(f"wrote {dst} ({doc.page_count} pages)")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
