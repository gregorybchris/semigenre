"""Printer for colored console text."""
from semigenre.cli.color import Color


class FormatIO:
    """Printer for colored console text."""

    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALICS = '\033[3m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

    @staticmethod
    def format(message, color='', bold=False, italics=False,
               dim=False, underline=False):
        """
        Format a message with colors and styles.

        :param message: Message to print.
        :param color: Color to print the text.
        :param bold: Whether to bold the text.
        :param italics: Whether to italicize the text.
        :param dim: Whether to dim the text.
        :param underline: Whether to underline the text.
        :return: Formatted message.
        """
        bold_pre = FormatIO.BOLD if bold else ''
        italics_pre = FormatIO.ITALICS if italics else ''
        dim_pre = FormatIO.DIM if dim else ''
        underline_pre = FormatIO.UNDERLINE if underline else ''

        full_pre = bold_pre + italics_pre + dim_pre + underline_pre
        reset = FormatIO.RESET

        return f"{color}{full_pre}{message}{reset}"

    @staticmethod
    def print(message, color='', bold=False, italics=False,
              dim=False, underline=False, end='\n'):
        """
        Print a message to standard output with formatting.

        :param message: Message to print.
        :param color: Color to print the text.
        :param bold: Whether to bold the text.
        :param italics: Whether to italicize the text.
        :param dim: Whether to dim the text.
        :param underline: Whether to underline the text.
        :param end: Text to end the printed line.
        """
        formatted = FormatIO.format(message, color=color, bold=bold,
                                    italics=italics, dim=dim,
                                    underline=underline)
        print(formatted, end=end)

    @staticmethod
    def input(message, color='', bold=False, italics=False,
              dim=False, underline=False):
        """
        Accept user input with formatting.

        :param message: Message to print.
        :param color: Color to print the text.
        :param bold: Whether to bold the text.
        :param italics: Whether to italicize the text.
        :param dim: Whether to dim the text.
        :param underline: Whether to underline the text.
        """
        formatted = FormatIO.format(message, color=color, bold=bold,
                                    italics=italics, dim=dim,
                                    underline=underline)
        return input(formatted)

    @staticmethod
    def prompt():
        """Prompt user for some input."""
        delimiter = u'\u279C'
        return FormatIO.input(f"Your move {delimiter} ", color=Color.BLUE)
