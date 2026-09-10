import mysql.connector
import datetime
from utils.config import MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD


def log_test_result(test_name, script_name, status, duration, error_message=None, login_duration=None, run_type=None):

    conn = None
    cursor = None

    try:
        conn = mysql.connector.connect(
            host=MYSQL_URL,
            user=MYSQL_USERNAME,
            password=MYSQL_PASSWORD,
            database="playwright"
        )

        cursor = conn.cursor()

        query = """
            INSERT INTO playwright_orangehrmlive_demo
            (test_name, script_name, status, duration, error_message, executed_at, login_duration, run_type)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, (
            test_name,
            script_name,
            status,
            duration,
            error_message,
            datetime.datetime.now(),
            login_duration,
            run_type
        ))

        conn.commit()

    except Exception as e:
        print(f"MySQL logging error: {e}")

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass