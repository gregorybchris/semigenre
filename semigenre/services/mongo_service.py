"""Abstract service for MongoDB storage."""
from pymongo import MongoClient

from semigenre.services import settings
from semigenre.services.storage_service import StorageService


class MongoService(StorageService):
    """Abstract service for MongoDB storage."""

    def __init__(self, collection_name):
        """Construct a MongoService."""
        self._collection = self._connect(collection_name)

    def _connect(self, collection_name):
        """
        Connect to the database.

        :param collection_name: Name of the collection.
        :return: Mongo collection object.
        """
        client = MongoClient(settings.DATABASE_CONN)
        if settings.DATABASE_NAME is None:
            raise EnvironmentError('DATABASE_NAME not set.')
        db = client[settings.DATABASE_NAME]
        return db[collection_name]

    def insert_one(self, record):
        """
        Insert a record into the store.

        :param record: Record to store.
        :return: Document ID.
        """
        return self._collection.insert_one(record)

    def find(self, query, projection=None):
        """
        Find records in the store.

        :param query: Query to find records.
        :param projection: Fields to return.
        :return: All matching records from the store.
        """
        return self._collection.find(query)

    def find_one(self, query, projection=None):
        """
        Find a record in the store.

        :param query: Query to find a record.
        :param projection: Fields to return.
        :return: One record from the store.
        """
        return self._collection.find_one(query)
