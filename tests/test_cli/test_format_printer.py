from semigenre.cli.format_io import FormatIO


def test_print_all_colors(color):
    FormatIO.print("TEXT", color=color)


def test_print_formats():
    FormatIO.print("TEXT", bold=True, italics=True,
                   underline=True, dim=True)
