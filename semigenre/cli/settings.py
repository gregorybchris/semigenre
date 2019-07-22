"""Settings for the CLI."""
import os

VAR_SENTRY_CONN = 'SENTRY_CONN'

sentry_conn = os.getenv(VAR_SENTRY_CONN,
    "https://8b13d32348614eebb4734f6a44befb22@sentry.io/1510062")
