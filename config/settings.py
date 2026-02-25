import os

class Settings:
    AIO_SERVER = "io.adafruit.com"
    AIO_PORT = 1883
    AIO_USERNAME = os.getenv("AIO_USERNAME")
    AIO_KEY = os.getenv("AIO_KEY")