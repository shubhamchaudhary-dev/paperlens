import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

EXPORT_DIR = BASE_DIR / "exports"


def export_json(
    report: dict,
    filename: str,
):

    EXPORT_DIR.mkdir(
        exist_ok=True
    )

    output_file = (
        EXPORT_DIR /
        f"{filename}.json"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(
            report,
            f,
            indent=4,
            ensure_ascii=False,
        )

    print(
        "JSON EXPORTED TO:",
        output_file.resolve(),
    )

    return str(
        output_file.resolve()
    )


def export_markdown(
    report: dict,
    filename: str,
):

    EXPORT_DIR.mkdir(
        exist_ok=True
    )

    output_file = (
        EXPORT_DIR /
        f"{filename}.md"
    )

    content = f"""# PaperLens Report

## Integrity Score

{report['score']}

## Citation Count

{report['citation_count']}

## Recommendation

{report['review']['recommendation']}

## Strengths

{chr(10).join('- ' + s for s in report['review']['strengths'])}

## Weaknesses

{chr(10).join('- ' + s for s in report['review']['weaknesses'])}

## Warnings

{chr(10).join('- ' + s for s in report['review']['warnings'])}
"""

    with open(
        output_file,
        "w",
        encoding="utf-8",
    ) as f:

        f.write(content)

    print(
        "MARKDOWN EXPORTED TO:",
        output_file.resolve(),
    )

    return str(
        output_file.resolve()
    )

def export_html(report, filename):

    output_file = EXPORT_DIR / f"{filename}.html"

    html = f"""
    <html>
    <head>
        <title>PaperLens Report</title>
        <style>
            body {{
                font-family: Arial;
                margin: 40px;
            }}

            .score {{
                font-size: 48px;
                font-weight: bold;
            }}
        </style>
    </head>

    <body>

        <h1>PaperLens Report</h1>

        <div class="score">
            {report['score']}
        </div>

        <h2>Recommendation</h2>
        <p>{report['review']['recommendation']}</p>

        <h2>Citations</h2>
        <p>{report['citation_count']}</p>

    </body>
    </html>
    """

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    return str(output_file)