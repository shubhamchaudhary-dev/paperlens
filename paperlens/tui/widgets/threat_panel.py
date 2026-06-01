from textual.widgets import Static


class ThreatPanel(Static):

    def update_threats(self, fillers):

        content = "\n".join(fillers)

        self.update(
            f"""
[bold red]
Detected Filler
[/bold red]

{content}
"""
        )