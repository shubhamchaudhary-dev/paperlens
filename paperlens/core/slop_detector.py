SLOP_PHRASES = [

    "in today's rapidly evolving",

    "it is important to note that",

    "plays a crucial role",

    "has gained significant attention",

    "in recent years",

    "this study aims to",

    "this paper presents",

    "it can be concluded that",

    "future research directions",

    "further investigation is needed",

    "researchers have increasingly",

    "the results demonstrate",

    "the findings suggest",

    "state of the art",

    "comprehensive framework",

    "robust solution",
]


def detect_slop(text: str):

    text_lower = text.lower()

    matches = []

    for phrase in SLOP_PHRASES:

        count = text_lower.count(
            phrase.lower()
        )

        if count:

            matches.append(
                {
                    "phrase": phrase,
                    "count": count,
                }
            )

    return matches