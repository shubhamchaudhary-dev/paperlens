import fitz


def extract_pdf_data(pdf_path: str) -> dict:
    doc = fitz.open(pdf_path)

    full_text = []

    for page in doc:
        full_text.append(page.get_text())

    text = "\n".join(full_text)

    metadata = doc.metadata

    return {
        "title": metadata.get("title") or "Unknown Title",
        "author": metadata.get("author") or "Unknown Author",
        "pages": len(doc),
        "text": text,
    }