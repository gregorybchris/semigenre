"""Command line interface for rating tracks."""
from semigenre.cli.cli import CLI
from semigenre.rating.commands.main_command import MainCommand
from semigenre.rating.state import State
from semigenre.services.reporting import Sentry


class RatingCLI(CLI):
    """Command line interface for rating tracks."""

    def __init__(self, library):
        """Construct a RatingCLI."""
        Sentry().init()
        self._state = State(library=library)

    def run(self):
        """Run the CLI."""
        MainCommand().execute(self._state)
