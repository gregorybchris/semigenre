"""Service for storage of track data."""
from semigenre.services.storage_service import StorageService
from semigenre.services.service_factory import ServiceFactory


class TrackService(StorageService):
    """Service for storage of track data."""

    COLLECTION_NAME = 'tracks'

    def __init__(self):
        """Construct a TrackService."""
        self._service = ServiceFactory.create(TrackService.COLLECTION_NAME)

    def insert_one(self, record):
        """
        Insert a record into the store.

        :param record: Record to store.
        """
        return self._service.insert_one(record)

    def find(self, query, projection=None):
        """
        Find records in the store.

        :param query: Query to find records.
        :param projection: Fields to return.
        :return: All matching records from the store.
        """
        return self._service.find(query, projection=projection)

    def find_one(self, query, projection=None):
        """
        Find a record in the store.

        :param query: Query to find a record.
        :param projection: Fields to return.
        :return: One record from the store.
        """
        return self._service.find_one(query, projection=projection)
