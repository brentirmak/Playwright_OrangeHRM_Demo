import os
from dotenv import load_dotenv

load_dotenv()

APP_USERNAME = os.getenv("APP_USERNAME")
APP_PASSWORD = os.getenv("APP_PASSWORD")

MYSQL_URL = os.getenv("MYSQL_URL")
MYSQL_USERNAME = os.getenv("MYSQL_USERNAME")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

RESEND_API_KEY = os.getenv("RESEND_API_KEY")
EMAIL_ALERT_RECIPIENT = os.getenv("EMAIL_ALERT_RECIPIENT")