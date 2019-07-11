"""Main menu command."""
from semigenre.cli.command import Command
from semigenre.cli.format_io import FormatIO
from semigenre.cli.options import Options


class MainCommand(Command):
    """Main menu command."""

    TAG = 'tag'
    COMPARE = 'compare'
    HELP = 'help'
    QUIT = 'quit'
    OPTION_NAMES = [TAG, COMPARE, HELP, QUIT]

    def execute(self, state):
        """Execute the command."""
        welcome_message = "Welcome to SemiGenre!"
        FormatIO.print(welcome_message, bold=True)

        options = Options(MainCommand.OPTION_NAMES)
        aliases = options.get_aliases()
        options.print_formatted()

        while True:
            response = FormatIO.prompt()
            valid, done = self._map_action(response, aliases)
            if done:
                break
            if not valid:
                FormatIO.print("Invalid command...", color=FormatIO.RED)

        print(f"Thanks for using SemiGenre!")

    def _map_action(self, response, aliases):
        action_map = {
            MainCommand.TAG: self._tag,
            MainCommand.COMPARE: self._compare,
            MainCommand.HELP: self._help,
            MainCommand.QUIT: self._quit
        }

        valid = False
        done = False
        for option_name in MainCommand.OPTION_NAMES:
            if response == option_name or response in aliases[option_name]:
                done = action_map[option_name]()
                valid = True
        return valid, done

    def _tag(self):
        print("TAG")
        return False

    def _compare(self):
        print("COMPARE")
        return False

    def _help(self):
        print("HELP")
        return False

    def _quit(self):
        return True
