from paperlens.core.pdf_parser import extract_pdf_data
from paperlens.core.integrity_engine import analyze_paper


from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import (
    Footer,
    DirectoryTree,
    Static,
    Label,
)


class PaperLensApp(App):

    CSS_PATH = "../themes/cyber.tcss"

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("e", "export_report", "Export"),
    ]

    def on_mount(self):
        print("APP STARTED")

    def compose(self) -> ComposeResult:

        yield Label(
            """
██████╗  █████╗ ██████╗ ███████╗██████╗ ██╗     ███████╗███╗   ██╗███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██║     ██╔════╝████╗  ██║██╔════╝
██████╔╝███████║██████╔╝█████╗  ██████╔╝██║     █████╗  ██╔██╗ ██║███████╗
██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗██║     ██╔══╝  ██║╚██╗██║╚════██║
██║     ██║  ██║██║     ███████╗██║  ██║███████╗███████╗██║ ╚████║███████║
╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝╚══════╝

                    Research Integrity Command Center
            """,
            id="banner",
        )

        with Horizontal():

            yield DirectoryTree(
                "./data/papers",
                id="explorer",
            )

            with Vertical(id="center"):

                yield Static(
                    """
████████████████████████

        No Paper Selected

    Integrity Score

████████████████████████
                    """,
                    id="score",
                )

                yield Static(
                    """
Research DNA

────────────────────

No paper loaded.

Select a PDF.
                    """,
                    id="dna",
                )

            with Vertical(id="right"):

                yield Static(
                    """
Threat Analysis

────────────────────

No analysis available.

Select a PDF.
                    """,
                    id="threats",
                )

                yield Static(
                    """
Citation Health

────────────────────

No citation data.

Select a PDF.
                    """,
                    id="citations",
                )

        yield Static(
            """
Crossref ✓     OpenAlex ✓     Semantic Scholar ✓     Integrity Engine ✓
            """,
            id="status",
        )

        yield Footer()

    @on(DirectoryTree.FileSelected)
    def handle_file_selected(
        self,
        event: DirectoryTree.FileSelected,
    ) -> None:

        print("=" * 50)
        print("FILE SELECTED")
        print(event.path)

        path = str(event.path)

        if not path.lower().endswith(".pdf"):
            return

        try:

            print("PARSING PDF")

            paper = extract_pdf_data(path)

            print("ANALYZING PAPER")

            result = analyze_paper(paper)
            self.current_report = result
            self.current_paper = paper

            print(result)

            # -----------------------
            # Integrity Score
            # -----------------------

            self.query_one("#score").update(
                f"""
████████████████████████

        {result['score']}

    Integrity Score

████████████████████████
"""
            )

            # -----------------------
            # Threat Analysis
            # -----------------------

            threat_text = "\n".join(result["fillers"])

            if not threat_text:
                threat_text = "No filler detected"

            self.query_one("#threats").update(
                f"""
            Threat Analysis

            ────────────────────

            {threat_text}
            """
            )

            # -----------------------
            # Citation Health
            # -----------------------

            health = result.get(
                "citation_health",
                {
                    "total": 0,
                    "verified": 0,
                    "invalid": 0,
                },
            )

            self.query_one("#citations").update(
                f"""
Citation Health

────────────────────

DOIs Found

{health['total']}

Verified

{health['verified']}

Invalid

{health['invalid']}
"""
            )

            # -----------------------
            # Research DNA
            # -----------------------

            review = result["review"]

            strengths = "\n".join(
                review["strengths"][:2]
            )

            recommendation = review[
                "recommendation"
            ]

            self.query_one("#dna").update(
                f"""
Research DNA

────────────────────

Pages: {result['pages']}

Words: {result['word_count']}

Paper: {self.current_paper['title']}

Recommendation:

{recommendation}

{strengths}
"""
            )

        except Exception as e:

            print("ERROR:", e)

            self.query_one("#score").update(
                f"""
ERROR

{e}
"""
            )


    def action_export_report(self):

        try:

            print("EXPORT PRESSED")

            if not hasattr(
                self,
                "current_report",
            ):

                self.notify(
                    "Analyze a PDF first.",
                    title="PaperLens",
                )

                return

            from paperlens.core.export_engine import (
                export_json,
                export_markdown,
                export_html,
            )

            filename = "paperlens_report"

            json_file = export_json(
                self.current_report,
                filename,
            )

            md_file = export_markdown(
                self.current_report,
                filename,
            )

            html_file = export_html(
                self.current_report,
                filename,
            )

            print("JSON:", json_file)
            print("MD:", md_file)
            print("HTML:", html_file)

            self.notify(
                "Report exported successfully!",
                title="PaperLens",
                timeout=3,
            )

            self.query_one("#status").update(
                f"""
            Score: {self.current_report['score']}
            |
            Citations: {self.current_report['citation_count']}
            |
            Recommendation: {self.current_report['review']['recommendation']}
            """
            )

        except Exception as e:

            print("EXPORT ERROR:", e)

            self.notify(
                f"Export failed: {e}",
                title="PaperLens Error",
                timeout=5,
            )

            self.query_one("#status").update(
                f"Export Error: {e}"
            )