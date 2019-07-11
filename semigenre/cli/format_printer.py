"""Printer for colored console text."""


class FormatPrinter:
    """Printer for colored console text."""

    BLUE = '\033[34m'
    GREEN = '\033[32m'
    RED = '\033[31m'
    YELLOW = '\033[33m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    PURPLE = '\033[95m'

    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALICS = '\033[3m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

    COLORS = [BLUE, GREEN, RED, YELLOW, MAGENTA, CYAN, WHITE, PURPLE]

    @staticmethod
    def print(message: str,
              color: str = RESET,
              bold: bool = False,
              italics: bool = False,
              dim: bool = False,
              underline: bool = False,
              end: str = '\n') -> None:
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
        bold_pre = FormatPrinter.BOLD if bold else ''
        italics_pre = FormatPrinter.ITALICS if italics else ''
        dim_pre = FormatPrinter.DIM if dim else ''
        underline_pre = FormatPrinter.UNDERLINE if underline else ''
        full_pre = bold_pre + italics_pre + dim_pre + underline_pre
        reset = FormatPrinter.RESET
        formatted = "{}{}{}{}".format(full_pre, color, message, reset)
        print(formatted, end=end)
