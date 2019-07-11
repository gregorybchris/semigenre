"""Command line interface for rating tracks."""
from semigenre.rating.commands.main_command import MainCommand
from semigenre.rating.state import State


class RatingCLI:
    """Command line interface for rating tracks."""

    def __init__(self, library):
        """Construct a RatingCLI."""
        self._state = State(library=library)

    def run(self):
        """Run the CLI."""
        main_command = MainCommand()
        main_command.execute(self._state)
