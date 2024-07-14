import configparser
import os

config = configparser.ConfigParser()
config.read("config.ini")

OPENAI_KEY = os.getenv("OPENAI_KEY", config.get("openai", "OPENAI_KEY", fallback=None))

if not OPENAI_KEY:
    raise ValueError("OPENAI_KEY is not set")
