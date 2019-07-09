"""Command line interface for rating tracks."""


class RatingCLI:
    """Command line interface for rating tracks."""

    def __init__(self, library):
        """Construct a RatingCLI."""
        self._library = library

    def run(self):
        """Run the CLI."""
        print("Welcome to the SemiGenre RatingCLI")
        name = input("Please enter your name: ")
        print("Thanks for using SemiGenre, {}".format(name))
        decision = input("What's your decision?")
        if decision == 'no':
            print("That's too bad!")
        else:
            print("Nice!")
