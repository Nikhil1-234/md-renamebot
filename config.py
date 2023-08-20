import os

class Config(object):
    BANNED_USERS = []
    DOWNLOAD_LOCATION = "./DOWNLOADS" 
    API_ID = int(os.environ.get("API_ID","22299340"))
    API_HASH = os.environ.get("API_HASH" "mongodb+srv://jidovi4576:B6HywpSzpSqZZ3W@clusterbot2.ezfn734.mongodb.net/?retryWrites=true&w=majority")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6439927958:AAHhSthTQi1DjQpqwZOC2vBjy_n_thi5sC8")
    OWNER_ID = int(os.environ.get("OWNER_ID","5380609667'))
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", None)
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://jidovi4576:B6HywpSzpSqZZ3W@clusterbot2.ezfn734.mongodb.net/?retryWrites=true&w=majority")
