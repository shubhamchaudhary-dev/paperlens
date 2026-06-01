import re


def detect_repetition(text: str):

    paragraphs = [
        p.strip()
        for p in text.split("\n\n")
        if len(p.strip()) > 100
    ]

    seen = {}
    repeated = []

    for para in paragraphs:

        normalized = re.sub(
            r"\s+",
            " ",
            para.lower(),
        )

        if normalized in seen:

            seen[normalized] += 1

        else:

            seen[normalized] = 1

    for para, count in seen.items():

        if count > 1:

            repeated.append(
                {
                    "count": count,
                    "preview": para[:80],
                }
            )

    return repeated