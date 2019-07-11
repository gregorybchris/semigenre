"""Main menu command."""
from semigenre.cli.command import Command
from semigenre.cli.format_printer import FormatPrinter
from semigenre.cli.options import Options


class MainCommand(Command):
    """Main menu command."""

    QUIT = 'q'

    def execute(self, state):
        """Execute the command."""
        welcome_message = "Welcome to SemiGenre!"
        FormatPrinter.print(welcome_message, bold=True)

        # options = Options(['tag', 'compare', 'help', 'quit'])
        options = Options(['tag', 'tompare', 'help', 'quit'])
        aliases = options.get_aliases()
        print("Aliases: ", aliases)
        options.print_formatted()

        name = input("Please enter your name: ")

        while True:
            decision = input("Input: ")
            if decision == MainCommand.QUIT:
                break

        print(f"Thanks for using SemiGenre, {name}")
