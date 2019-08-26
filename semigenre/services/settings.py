"""Settings for services."""
import os

# Database

DATABASE_NAME = os.getenv('DATABASE_NAME', None)
DATABASE_CONN = os.getenv('DATABASE_CONN', None)
DATABASE_USER = os.getenv('DATABASE_USER', None)
DATABASE_KEY = os.getenv('DATABASE_KEY', None)
DATA_DIRECTORY = os.getenv('DATA_DIRECTORY', None)
SERVICE_TYPE = os.getenv('SERVICE_TYPE', None)

# Reporting

SENTRY_CONN = 'https://8b13d32348614eebb4734f6a44befb22@sentry.io/1510062'
