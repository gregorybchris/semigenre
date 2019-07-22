"""Command line interface abstract class."""
from abc import ABC, abstractmethod


class CLI(ABC):
    """Command line interface abstract class."""

    @abstractmethod
    def run(self):
        """Run the CLI."""
        ...  # pragma: no cover
