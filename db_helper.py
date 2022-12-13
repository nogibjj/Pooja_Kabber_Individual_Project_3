import psycopg2
import os

host = os.environ.get("RDS_HOSTNAME")
user = os.environ.get("RDS_USER")
password = os.environ.get("RDS_PASSWORD")
database = os.environ.get("RDS_DATABASE")


def connect_to_db():

    connection = psycopg2.connect(
        host=host, port=5432, user=user, password=password, database="titanic"
    )
    cursor = connection.cursor()

    return cursor
