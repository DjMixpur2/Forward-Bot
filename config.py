import datetime
from os import environ 

class Config:
    API_ID = environ.get("API_ID", "21344245")
    API_HASH = environ.get("API_HASH", "e72de40c666f1664f847a79f97dd3882")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7980904477:AAHQOHBwPES7dkDrgHPF40_leghWYQbIoFo") 
    BOT_SESSION = environ.get("BOT_SESSION", "Forward-Bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://djmixpuryt:djmixpuryt@cluster0.2qrq1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7585839477').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002363068125'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")
    PORT = environ.get('PORT', '8080')
   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
