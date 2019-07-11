from semigenre.cli.format_printer import FormatPrinter


def test_print_all_colors(color):
    FormatPrinter.print("TEXT", color=color)


def test_print_formats():
    FormatPrinter.print("TEXT", bold=True, italics=True,
                        underline=True, dim=True)
