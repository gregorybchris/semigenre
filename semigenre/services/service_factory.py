"""Fatory for creating services."""
from semigenre.services.csv_service import CSVService
from semigenre.services.mongo_service import MongoService
from semigenre.services import settings


class ServiceFactory:
    """Fatory for creating services."""

    MONGO_TYPE = 'mongo'
    CSV_TYPE = 'csv'

    @staticmethod
    def create(collection_name):
        """
        Create new service based on the collection.

        :param collection_name: Name of the collection to create.
        :return: New service of the type defined by the settings.
        """
        if settings.SERVICE_TYPE == ServiceFactory.MONGO_TYPE:
            return MongoService(collection_name)
        elif settings.SERVICE_TYPE == ServiceFactory.CSV_TYPE:
            return CSVService(collection_name)
