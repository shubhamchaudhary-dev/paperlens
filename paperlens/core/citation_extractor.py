import re


CITATION_PATTERN = r"\[(\d+)\]"


def extract_citations(text: str):
    citations = re.findall(CITATION_PATTERN, text)

    unique = sorted(set(citations))

    return unique


def count_citations(text: str):
    return len(extract_citations(text))