from typing import Optional
import psycopg2


DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "database"
DB_USER = "username"
DB_PASSWORD = "secret"


def get_connection() -> psycopg2.extensions.connection | None:
    """
    Get a connection to the database or None if it fails
    """
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        print("Connected to database")
        return connection

    except (Exception, psycopg2.Error) as error:
        print(f"Error: {error}")

    return None
