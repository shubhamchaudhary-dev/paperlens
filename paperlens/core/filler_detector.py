FILLER_PHRASES = [
    "it is important to note",
    "various studies have shown",
    "the findings highlight",
    "in today's rapidly evolving landscape",
    "significant implications",
    "future research should",
    "plays a crucial role",
    "can be utilized",
    "state-of-the-art",
]


def detect_fillers(text: str):
    text = text.lower()

    found = []

    for phrase in FILLER_PHRASES:
        if phrase in text:
            found.append(phrase)

    return found


def filler_count(text: str):
    return len(detect_fillers(text))