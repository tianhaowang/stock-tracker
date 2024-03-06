from mysql.connector import pooling
import os

# Read the database credentials from environment variables
DB_HOST = os.environ.get("DB_HOST", "").strip()
DB_USER = os.environ.get("DB_USER", "").strip()
DB_PASSWORD = os.environ.get("DB_PASSWORD", "").strip()
DB_NAME = os.environ.get("DB_NAME", "").strip()

# Configuration for the connection pool
dbconfig = {
    "host": DB_HOST,
    "user": DB_USER,
    "password": DB_PASSWORD,
    "database": DB_NAME
}

# Create a connection pool
pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **dbconfig)

def get_database_connection():
    # Get connection from the connection pool
    return pool.get_connection()