import re


DOI_PATTERN = r"(10\.\d{4,9}/[-._;()/:A-Z0-9]+)"


def extract_dois(text: str):

    matches = re.findall(
        DOI_PATTERN,
        text,
        flags=re.IGNORECASE,
    )

    return list(set(matches))