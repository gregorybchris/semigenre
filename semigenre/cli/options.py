"""Wrapper for enumerated CLI user options."""
from semigenre.cli.color import Color
from semigenre.cli.format_io import FormatIO
from semigenre.rating.commands.help_command import HelpCommand
from semigenre.rating.commands.quit_command import QuitCommand


class Options:
    """Wrapper for enumerated CLI user options."""

    HELP_OPTION = 'help'
    QUIT_OPTION = 'quit'

    def __init__(self,
                 commands,
                 state,
                 loop=False,
                 help_message=None,
                 include_quit=True,
                 max_line=80,
                 option_spacing=4):
        """
        Construct an Options wrapper.

        :param commands: Commands from which to select.
        :param state: State to pass commands.
        :param loop: Whether to loop on input until quit.
        :param help_message: Message for getting help with the options.
        :param include_quit: Whether to include a quit command.
        :param max_line: Line length character limit.
        :param option_spacing: Spacing between printed options.
        """
        self._commands = commands
        self._state = state

        self._loop = loop
        self._help_message = help_message
        self._include_quit = include_quit
        self._max_line = max_line
        self._option_spacing = option_spacing

        self._add_default_commands()
        self._options = self._prepare_options()

    def _add_default_commands(self):
        if self._help_message is not None:
            self._commands.append(HelpCommand(self._help_message))

        if self._include_quit:
            self._commands.append(QuitCommand())

    def _prepare_options(self):
        # TODO: Fix to work when no alias can be found
        used = set()
        options = list()
        for command_index, command in enumerate(self._commands):
            name = command.get_name()
            for alias_index, alias in enumerate(name):
                if alias not in used:
                    option = Option(name, command,
                                    command_index + 1, alias, alias_index)
                    options.append(option)
                    used.add(alias)
                    break
        return options

    def _print_formatted(self):
        """Print the formatted options."""
        # TODO: Adhere to max_line constraint
        FormatIO.print("\nOptions:", bold=True)
        for option in self._options:
            print(f"{option.number}: ", end='')

            beginning = option.name[:option.alias_index]
            end = option.name[option.alias_index + 1:]

            print(beginning, end='')
            FormatIO.print(option.alias, color=Color.BLUE,
                           bold=True, end='')
            print(end, end='')
            print(' ' * self._option_spacing, end='')
        print()

    def prompt(self):
        full_options = dict()
        for option in self._options:
            for reference in option.get_references():
                full_options[reference] = option.command

        while True:
            self._print_formatted()
            response = FormatIO.prompt()
            if response in full_options:
                command_result = full_options[response].execute(self._state)
                if command_result == QuitCommand.NAME:
                    break
            else:
                FormatIO.print("Invalid command...", color=Color.RED)

            if not self._loop:
                break


class Option:
    def __init__(self, name, command, number, alias, alias_index):
        self.name = name
        self.command = command
        self.number = number
        self.alias = alias
        self.alias_index = alias_index

    def get_references(self):
        return [self.name, self.alias, str(self.number)]
