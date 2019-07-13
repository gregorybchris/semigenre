"""Abstract service for TSV storage."""
import os
import pandas as pd

from semigenre.services.storage_service import StorageService
from semigenre.services import settings


class CSVService(StorageService):
    """Abstract service for TSV storage."""

    def __init__(self, collection_name):
        """Construct a CSVService."""
        self._collection_name = collection_name
        self._data_directory = settings.data_directory
        self._df = self._get_create_collection()

    def _get_create_collection(self):
        data_dir = self._data_directory
        if data_dir is None:
            raise EnvironmentError("DATA_DIRECTORY not set")
        if not os.path.exists(data_dir):
            os.makedirs(data_dir, exist_ok=True)
        collection_filename = f'{self._collection_name}.tsv'
        collection_path = os.path.join(data_dir, collection_filename)
        if not os.path.exists(collection_path):
            # with open(collection_path, 'a'):
            #     os.utime(collection_path, None)
            return None
        return pd.read_csv(collection_path)

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
