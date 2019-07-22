"""Command for a CLI application."""
from abc import ABC, abstractmethod


class Command(ABC):
    """Command for a CLI application."""

    @abstractmethod
    def execute(self, *args, **kwargs):
        """Execute the command."""
        ...  # pragma: no cover

    def get_name(self):
        """Get the name of the command."""
        ...  # pragma: no cover
