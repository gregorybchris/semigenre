"""Interfaces for connecting to reporting tools."""
from semigenre.services import settings


class Sentry:
    """Service class used to connect to sentry.io."""

    def __init__(self):
        """Construct a Sentry connection service."""
        self._conn = settings.SENTRY_CONN
        self._enabled = False

    def init(self, conn=None):
        """Start the Sentry service."""
        if conn is None:
            conn = self._conn

        try:
            import sentry_sdk
            sentry_sdk.init(conn)
            self._enabled = True
        except Exception:
            self._enabled = False

    def is_enabled(self):
        """Check if the service is running."""
        return self._enabled
