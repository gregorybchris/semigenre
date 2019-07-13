import os

VAR_DATABASE_NAME = 'DATABASE_NAME'
VAR_DATABASE_CONN = 'DATABASE_CONN'
VAR_DATABASE_KEY = 'DATABASE_KEY'

database_name = os.getenv(VAR_DATABASE_NAME, None)
database_conn = os.getenv(VAR_DATABASE_CONN, None)
database_key = os.getenv(VAR_DATABASE_KEY, None)

VAR_DATA_DIRECTORY = 'DATA_DIRECTORY'

data_directory = os.getenv(VAR_DATA_DIRECTORY, None)

VAR_SERVICE_TYPE = 'SERVICE_TYPE'

service_type = os.getenv(VAR_SERVICE_TYPE, None)
