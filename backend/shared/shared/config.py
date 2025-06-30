"""config"""

import os
from dotenv import load_dotenv

dotenv_path = os.getenv("DOTENV_PATH", os.path.join(os.getcwd(), ".env"))

load_dotenv(dotenv_path)

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
DATABASE_URL = os.getenv('DATABASE_URL')
FASTAPI_HOST = os.getenv('FASTAPI_HOST')
FASTAPI_PORT = int(os.getenv('FASTAPI_PORT'))
