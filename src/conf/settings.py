import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
API_ACCU_KEY=os.getenv("API_ACCU_KEY")
CITY_KEY=os.getenv("CITY_KEY")
URL_ACCU=os.getenv("URL_ACCU")
