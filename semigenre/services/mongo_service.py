"""Abstract service for MongoDB storage."""
from semigenre.services.storage_service import StorageService


class MongoService(StorageService):
    """Abstract service for MongoDB storage."""

    def __init__(self, collection_name):
        """Construct a MongoService."""
        self._collection_name = collection_name

    def insert(self, record):
        """
        Insert a record into the store.

        :param record: Record to store.
        """
        raise NotImplementedError

    def find(self, query, projection):
        """
        Find records in the store.

        :param query: Query to find records.
        :param projection: Fields to return.
        :return: All matching records from the store.
        """
        raise NotImplementedError

    def find_one(self, record, projection):
        """
        Find a record in the store.

        :param query: Query to find a record.
        :param projection: Fields to return.
        :return: One record from the store.
        """
        raise NotImplementedError
