"""Command line interface for rating tracks."""
import sentry_sdk

from semigenre.cli.cli import CLI
from semigenre.cli import settings
from semigenre.rating.commands.main_command import MainCommand
from semigenre.rating.state import State


class RatingCLI(CLI):
    """Command line interface for rating tracks."""

    def __init__(self, library):
        """Construct a RatingCLI."""
        sentry_sdk.init(settings.sentry_conn)
        self._state = State(library=library)

    def run(self):
        """Run the CLI."""
        MainCommand().execute(self._state)
