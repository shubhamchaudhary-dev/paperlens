from paperlens.core.citation_extractor import count_citations
from paperlens.core.citation_validator import validate_references
from paperlens.core.filler_detector import detect_fillers
from paperlens.core.reviewer_engine import generate_review


def analyze_paper(paper: dict):

    text = paper["text"]
    pages = paper["pages"]

    citation_count = count_citations(text)

    fillers = detect_fillers(text)

    citation_health = validate_references(text)

    word_count = len(text.split())

    score = 100

    # Filler penalty
    score -= len(fillers) * 4

    # Citation penalty
    if citation_count < 5:
        score -= 15
    elif citation_count < 15:
        score -= 8

    # Page penalty
    if pages < 3:
        score -= 30
    elif pages < 5:
        score -= 15

    # Word count penalty
    if word_count < 1000:
        score -= 20
    elif word_count < 3000:
        score -= 10

    score = max(0, min(100, score))

    review = generate_review(
        score,
        citation_count,
        pages,
        fillers,
    )

    return {
        "score": score,
        "pages": pages,
        "word_count": word_count,
        "citation_count": citation_count,
        "citation_health": citation_health,
        "fillers": fillers,
        "review": review,
    }