"""Track compare command."""
from semigenre.cli.command import Command


class CompareCommand(Command):
    """Track compare command."""

    NAME = 'compare'

    def execute(self, state):
        """Execute the command."""
        print("COMPARE")

    def get_name(self):
        """Get the name of the command."""
        return CompareCommand.NAME
