"""Quit command."""
from semigenre.cli.command import Command
from semigenre.cli.format_io import FormatIO


class QuitCommand(Command):
    """Quit command."""

    NAME = 'quit'
    YES = 'y'
    NO = 'n'

    def execute(self, state):
        """Execute the command."""
        while True:
            response = FormatIO.input("Are you sure you want to quit? (y/n) ", bold=True)
            if response == QuitCommand.YES:
                return QuitCommand.NAME
            elif response == QuitCommand.NO:
                return None

    def get_name(self):
        """Get the name of the command."""
        return QuitCommand.NAME
