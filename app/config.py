from configparser import ConfigParser
from dotenv import load_dotenv
import os


load_dotenv()
config = ConfigParser()
with open("app.conf") as fh:
    config.read_file(fh)


SECRET_KEY = os.environ.get("SECRET_KEY")
HEADERS = config["HEADERS"]
PORT = config["SERVER"]["port"]
LOG_FILE = config["SERVER"]["log_file"]
HOST = config["SERVER"]["host"]
