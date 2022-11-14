host = "dbinstance1.cndtu3jnk9za.us-east-1.rds.amazonaws.com"
user = "postgres"
password = "Pthescript7!"
database = "titanic"

import psycopg2

connection = psycopg2.connect(
    host=host, port=5432, user=user, password=password, database="titanic"
)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE passengers(
id SERIAL PRIMARY KEY,
name text,
sex text,
age float,
sibsp integer,
parch integer)"""
)

cursor.execute(
    """SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'"""
)
for table in cursor.fetchall():
    print(table)
