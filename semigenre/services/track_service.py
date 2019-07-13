"""Service for storage of track data."""
from semigenre.services.storage_service import StorageService
from semigenre.services.service_factory import ServiceFactory


class TrackService(StorageService):
    """Service for storage of track data."""

    COLLECTION_NAME = 'tracks'

    def __init__(self):
        """Construct a TrackService."""
        self._service = ServiceFactory.create(TrackService.COLLECTION_NAME)

    def insert(self, record):
        """
        Insert a record into the store.

        :param record: Record to store.
        """
        self._service.insert(record)

    def find(self, query, projection):
        """
        Find records in the store.

        :param query: Query to find records.
        :param projection: Fields to return.
        :return: All matching records from the store.
        """
        self._service.find(query, projection)

    def find_one(self, record, projection):
        """
        Find a record in the store.

        :param query: Query to find a record.
        :param projection: Fields to return.
        :return: One record from the store.
        """
        self._service.find_one(query, projection)
