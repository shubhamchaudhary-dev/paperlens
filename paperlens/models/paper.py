from dataclasses import dataclass


@dataclass
class Paper:
    title: str
    content: str
    citations: list
    filler_hits: list
    integrity_score: int