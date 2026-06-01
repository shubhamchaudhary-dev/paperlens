from paperlens.core.doi_extractor import (
    extract_dois,
)

from paperlens.services.crossref_service import (
    CrossrefService,
)


def validate_references(text: str):

    dois = extract_dois(text)

    return {
        "total": len(dois),
        "verified": "Pending",
        "invalid": "Pending",
    }