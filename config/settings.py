import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    AIO_SERVER = "io.adafruit.com"
    AIO_PORT = 1883
    AIO_USERNAME = os.getenv("AIO_USERNAME")
    AIO_KEY = os.getenv("AIO_KEY")
    TEMP_HIGH_THRESHOLD = float(os.getenv("TEMP_HIGH_THRESHOLD", "37"))
    TEMP_LOW_THRESHOLD = float(os.getenv("TEMP_LOW_THRESHOLD", "35"))