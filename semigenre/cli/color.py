"""Console colors."""


class Color:
    """Console colors."""

    BLUE = '\033[34m'
    GREEN = '\033[32m'
    RED = '\033[31m'
    YELLOW = '\033[33m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    PURPLE = '\033[95m'

    ALL = {BLUE, GREEN, RED, YELLOW, MAGENTA, CYAN, WHITE, PURPLE}

    @staticmethod
    def get(color_name):
        """
        Get a color by name.

        :param color_name: Name of the color.
        :return: Color string.
        """
        return {
            'blue': Color.BLUE,
            'green': Color.GREEN,
            'red': Color.RED,
            'yellow': Color.YELLOW,
            'magenta': Color.MAGENTA,
            'cyan': Color.CYAN,
            'white': Color.WHITE,
            'purple': Color.PURPLE
        }[color_name]
