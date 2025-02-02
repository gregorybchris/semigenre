"""Tag tracks command."""
from semigenre.cli.command import Command


class TagCommand(Command):
    """Tag tracks command."""

    NAME = 'tag'

    def execute(self, state):
        """Execute the command."""

    def get_name(self):
        """Get the name of the command."""
        return TagCommand.NAME
