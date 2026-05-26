# mysql_logger.py
import mysql.connector
import datetime

def log_test_result(test_name, status, duration, error_message=None, login_duration=None):
    conn = mysql.connector.connect(
        host="192.168.239.1",
        user="selenium",
        password="Selenium#123#",
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
