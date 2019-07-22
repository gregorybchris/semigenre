"""Main menu command."""
from semigenre.cli.color import Color
from semigenre.cli.command import Command
from semigenre.cli.format_io import FormatIO
from semigenre.cli.options import Options
from semigenre.rating.commands.compare_command import CompareCommand
from semigenre.rating.commands.tag_command import TagCommand


class MainCommand(Command):
    """Main menu command."""

    NAME = 'main'

    def execute(self, state):
        """Execute the command."""
        welcome_message = "Welcome to SemiGenre!"
        FormatIO.print(welcome_message, bold=True)

        help_message = ("Choose tag to tag songs.\n"
                        "Choose compare to compare songs.")

        commands = [CompareCommand(), TagCommand()]
        Options(commands, state, loop=True,
                help_message=help_message).prompt()

        print("Thanks for using SemiGenre!")

    def get_name(self):
        """Get the name of the command."""
        return MainCommand.NAME
