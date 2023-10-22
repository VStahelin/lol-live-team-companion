from os import environ

from dotenv import load_dotenv

load_dotenv()

DEBUG = True
DEBUG_MATCH_ID = "EUW1_123456789"


CLIENT_ID = environ.get("CLIENT_ID")

DATABASE_HOST = environ.get("DATABASE_HOST")
DATABASE_PORT = int(environ.get("POSTGRES_PORT"))
DATABASE_NAME = environ.get("POSTGRES_DB")
DATABASE_USER = environ.get("POSTGRES_USER")
DATABASE_PASSWORD = environ.get("POSTGRES_PASSWORD")

DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

MQTT_HOST = environ.get("MQTT_HOST")
MQTT_PORT = int(environ.get("MQTT_PORT"))
MQTT_USER = environ.get("MQTT_USER")
MQTT_PASSWORD = environ.get("MQTT_PASSWORD")

RIOT_CLIENT_URL = environ.get("RIOT_CLIENT_URL")
