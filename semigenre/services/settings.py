"""Settings for services."""
import os

# Database

VAR_DATABASE_NAME = 'DATABASE_NAME'
VAR_DATABASE_CONN = 'DATABASE_CONN'
VAR_DATABASE_USER = 'DATABASE_USER'
VAR_DATABASE_KEY = 'DATABASE_KEY'
VAR_DATA_DIRECTORY = 'DATA_DIRECTORY'
VAR_SERVICE_TYPE = 'SERVICE_TYPE'

database_name = os.getenv(VAR_DATABASE_NAME, None)
database_conn = os.getenv(VAR_DATABASE_CONN, None)
database_user = os.getenv(VAR_DATABASE_USER, None)
database_key = os.getenv(VAR_DATABASE_KEY, None)
data_directory = os.getenv(VAR_DATA_DIRECTORY, None)
service_type = os.getenv(VAR_SERVICE_TYPE, None)

# Reporting

VAR_SENTRY_CONN = 'SENTRY_CONN'
sentry_conn = os.getenv(VAR_SENTRY_CONN,
    "https://8b13d32348614eebb4734f6a44befb22@sentry.io/1510062")
