import configparser

config = configparser.ConfigParser()
config.read("config.ini")

OPENAI_KEY = config["openai"]["OPENAI_KEY"]
