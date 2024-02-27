from dotenv import load_dotenv
from dataclasses import dataclass
import os

load_dotenv()

# APP
APP_HOST = os.getenv('APP_HOST')
APP_PORT = int(os.getenv('APP_PORT'))

# DATABASE SETTINGS
DB_ENGINE = os.getenv('DB_ENGINE')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT', ''))

DB_CONNECTION_STRING = f"{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# URL
BASE_URL_PREFIX = '/api'

# TOKEN CONFIG
@dataclass(frozen=True)
class TokenConfig:
    secret_key: str = os.getenv("SECRET_KEY")
    algorithm: str = "HS256"
    default_expired: int = 120 # in minutes
    access_expired: int = 15 # in minutes
    refresh_expired: int = 7 * 1440 # in days
    url: str = '/api/auth/login'

TOKEN_CONFIG = TokenConfig()
