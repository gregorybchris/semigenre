"""Help command."""
from semigenre.cli.command import Command
from semigenre.cli.format_io import FormatIO


class HelpCommand(Command):
    """Help command."""

    NAME = 'help'

    def __init__(self, message):
        self._message = message

    def execute(self, state):
        """Execute the command."""
        FormatIO.print(self._message, bold=True)

    def get_name(self):
        """Get the name of the command."""
        return HelpCommand.NAME
