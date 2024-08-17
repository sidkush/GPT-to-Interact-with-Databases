# create a database connection class to handle database operations
import os
import psycopg2
from psycopg2 import extras

class DB_CONTEXT:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            dbname=os.getenv("DB_NAME", "your_database_name"),
            user=os.getenv("DB_USER", "your_user"),
            password=os.getenv("DB_PASSWORD", "your_password"),
        )
        self.connection.autocommit = True

    def cursor(self, query):
        with self.connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            cursor.execute(query)
            try:
                result = cursor.fetchall()
                return result
            except psycopg2.ProgrammingError:
                return None
            