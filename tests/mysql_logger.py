# mysql_logger.py
import mysql.connector
import datetime
from dotenv import load_dotenv
import os

def log_test_result(test_name, status, duration, error_message=None, login_duration=None):
    
    load_dotenv()  # Load environment variables from .env file

    mysql_url = os.getenv("MYSQL_URL")
    mysql_username = os.getenv("MYSQL_USERNAME")
    mysql_password = os.getenv("MYSQL_PASSWORD")

    conn = mysql.connector.connect(
        host=mysql_url,
        user=mysql_username,
        password=mysql_password,
        database="playwright"
    )
    cursor = conn.cursor()

    query = """
        INSERT INTO playwright_test_run_results (test_name, status, duration, error_message, executed_at, login_duration)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, (
        test_name,
        status,
        duration,
        error_message,
        datetime.datetime.now(),
        login_duration
    ))

    conn.commit()
    cursor.close()
    conn.close()
