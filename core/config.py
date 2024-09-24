from dotenv import load_dotenv
import os

load_dotenv()
DB_HOST2 = os.environ.get("DB_HOST2")
DB_PORT2 = os.environ.get("DB_PORT2")
DB_NAME2 = os.environ.get("DB_NAME2")
DB_USER2 = os.environ.get("DB_USER2")
DB_PASS2 = os.environ.get("DB_PASS2")
SECRET_KEY=os.environ.get("SECRET_KEY")