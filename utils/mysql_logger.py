import mysql.connector
import datetime

from utils.config import (
    MYSQL_URL,
    MYSQL_USERNAME,
    MYSQL_PASSWORD,
)


def log_test_result(
    test_name,
    script_name,
    status,
    duration,
    error_message=None,
    login_duration=None,
    run_type="manual",
):
    conn = None
    cursor = None

    try:
        # Never allow NULL/invalid values for run_type
        if run_type not in ("jenkins", "manual"):
            run_type = "manual"

        print(f"MySQL host: {MYSQL_URL}")
        print(f"MySQL user: {MYSQL_USERNAME}")
        print(f"Run type: {run_type}")

        conn = mysql.connector.connect(
            host=MYSQL_URL,
            user=MYSQL_USERNAME,
            password=MYSQL_PASSWORD,
            database="playwright",
        )

        print("MySQL connection successful")

        cursor = conn.cursor()

        query = """
            INSERT INTO playwright_orangehrmlive_demo
            (
                test_name,
                script_name,
                status,
                duration,
                error_message,
                executed_at,
                login_duration,
                run_type
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            test_name,
            script_name,
            status,
            duration,
            error_message,
            datetime.datetime.now(),
            login_duration,
            run_type,
        )

        print(f"MySQL insert values: {values}")

        cursor.execute(query, values)
        conn.commit()

        print(
            f"MySQL logging successful: "
            f"{test_name} / {run_type}"
        )

    except Exception as e:
        print(f"MY SQL LOGGING ERROR: {type(e).__name__}: {e}")

        # Roll back a failed transaction
        if conn is not None:
            try:
                conn.rollback()
            except Exception:
                pass

    finally:
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass

        if conn is not None:
            try:
                conn.close()
            except Exception:
                pass