from semigenre.services import settings
from semigenre.services.track_service import TrackService
from semigenre.services.service_factory import ServiceFactory


def test_create_track_service_mongo():
    service_type = settings.service_type
    settings.service_type = ServiceFactory.MONGO_TYPE
    TrackService()
    settings.service_type = service_type


def test_create_track_service_csv():
    service_type = settings.service_type
    settings.service_type = ServiceFactory.CSV_TYPE
    TrackService()
    settings.service_type = service_type
