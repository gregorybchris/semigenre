"""Command line interface for rating tracks."""


class RatingCLI:
    """Command line interface for rating tracks."""

    QUIT = 'q'

    def __init__(self, library):
        """Construct a RatingCLI."""
        self._library = library

    def run(self):
        """Run the CLI."""
        print("Welcome to the SemiGenre RatingCLI")
        name = input("Please enter your name: ")

        while True:
            decision = input("Input: ")
            if decision == RatingCLI.QUIT:
                break

        print("Thanks for using SemiGenre, {}".format(name))
