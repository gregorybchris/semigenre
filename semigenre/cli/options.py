"""Wrapper for enumerated CLI user options."""
from semigenre.cli.format_printer import FormatPrinter


class Options:
    """Wrapper for enumerated CLI user options."""

    def __init__(self, options, max_line=80, option_spacing=4):
        """
        Construct an Options wrapper.

        :param options: List of options from which to select.
        :param max_line: Line length character limit.
        :param option_spacing: Spacing between printed options.
        """
        self._options = options
        self._max_line = max_line
        self._option_spacing = option_spacing

        self._compute_aliases()

    def _compute_aliases(self):
        used = set()
        aliases = {option: (None, -1) for option in self._options}

        for option in self._options:
            alias, _ = aliases[option]
            if alias is None:
                for i, c in enumerate(option):
                    if c not in used:
                        aliases[option] = (c, i)
                        used.add(c)
                        break
        self._aliases = aliases

    def get_aliases(self):
        """
        Get one character aliases for the options.

        These aliases are used to efficiently enter commands.
        Aliases are selected by finding a unique letter for each option
        where that letter is toward the beginning of the option name.
        """
        alias_items = enumerate(self._aliases.items())
        aliases = dict()
        for option_index, (option, (alias, _)) in alias_items:
            aliases[option] = alias, option_index + 1
        return aliases

    def print_formatted(self):
        """Print the formatted options."""
        # TODO: Adhere to max_line constraint
        for option_index, option in enumerate(self._options):
            print(f"{option_index + 1}: ", end='')

            alias, alias_index = self._aliases[option]
            beginning = option[:alias_index]
            end = option[alias_index + 1:]

            print(beginning, end='')
            FormatPrinter.print(alias, color=FormatPrinter.BLUE, end='')
            print(end, end='')
            print(' ' * self._option_spacing, end='')
        print()
