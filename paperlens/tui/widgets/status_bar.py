from textual.widgets import Static


class StatusBar(Static):

    def on_mount(self):

        self.update(
            """
Crossref ✓
PDF Engine ✓
Integrity Engine ✓
"""
        )