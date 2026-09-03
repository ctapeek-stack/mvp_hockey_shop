import os

import psycopg
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    """Открыть соединение с базой магазина в PostgreSQL."""
    conn = psycopg.connect(
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],    
    )
    return conn