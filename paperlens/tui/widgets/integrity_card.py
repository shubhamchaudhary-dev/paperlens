from textual.widgets import Static


class IntegrityCard(Static):

    def update_score(self, score):

        self.update(
            f"""
[bold cyan]
Integrity Score
[/bold cyan]

[bold green]{score}[/bold green]
"""
        )