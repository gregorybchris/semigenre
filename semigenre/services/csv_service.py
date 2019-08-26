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
        self._data_directory = settings.DATA_DIRECTORY
        self._collection_path = self._get_collection_path()
        self._df = self._get_df()

    def _get_collection_path(self):
        collection_filename = f'{self._collection_name}.tsv'
        return os.path.join(self._data_directory, collection_filename)

    def _get_df(self):
        if self._data_directory is None:
            raise EnvironmentError("DATA_DIRECTORY not set.")
        if not os.path.exists(self._data_directory):
            os.makedirs(self._data_directory, exist_ok=True)
        if not os.path.exists(self._collection_path):
            return None
        return pd.read_csv(self._collection_path)

    def insert_one(self, record):
        """
        Insert a record into the store.

        :param record: Record to store.
        """
        if not os.path.exists(self._collection_path):
            with open(self._collection_path, 'a'):
                os.utime(self._collection_path, None)
        raise NotImplementedError

    def find(self, query, projection=None):
        """
        Find records in the store.

        :param query: Query to find records.
        :param projection: Fields to return.
        :return: All matching records from the store.
        """
        raise NotImplementedError

    def find_one(self, query, projection=None):
        """
        Find a record in the store.

        :param query: Query to find a record.
        :param projection: Fields to return.
        :return: One record from the store.
        """
        raise NotImplementedError
