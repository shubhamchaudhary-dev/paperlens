from textual.containers import Horizontal
from textual.widgets import Header
from textual.widgets import Footer

from .widgets.integrity_card import IntegrityCard
from .widgets.threat_panel import ThreatPanel
from .widgets.status_bar import StatusBar


class Dashboard(Horizontal):

    def compose(self):

        yield IntegrityCard(id="score")

        yield ThreatPanel(id="threats")

        yield StatusBar(id="status")