"""Abstract service class for any storage."""
from abc import ABC, abstractmethod


class StorageService(ABC):
    """Abstract service class for any storage."""

    @abstractmethod
    def insert_one(self, record):
        """
        Insert a record into the store.

        :param record: Record to store.
        """
        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def find(self, query, projection=None):
        """
        Find records in the store.

        :param query: Query to find records.
        :param projection: Fields to return.
        :return: All matching records from the store.
        """
        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def find_one(self, query, projection=None):
        """
        Find a record in the store.

        :param query: Query to find a record.
        :param projection: Fields to return.
        :return: One record from the store.
        """
        raise NotImplementedError  # pragma: no cover
