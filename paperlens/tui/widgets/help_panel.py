from textual.widgets import Static

class HelpPanel(Static):

    DEFAULT_CSS = """
    HelpPanel {
        height: 7;
    }
    """

    def compose(self):
        yield Static(
"""
↑ ↓ Navigate

Enter Open PDF

R Reviewer

D DNA

H Heatmap

Q Quit
"""
        )