#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler

# Environment Variables
TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN", "")
APP_ID = int(os.getenv("APP_ID", "23929647"))
API_HASH = os.getenv("API_HASH", "b9afa697042d998a758e407b84c86daf")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1002401143074"))
OWNER_ID = int(os.getenv("OWNER_ID", "7824607111"))
PORT = os.getenv("PORT", "8080")
DB_URI = os.getenv("DATABASE_URL", "mongodb+srv://krishnegi9211:Wv7neZBwVmXrCh54@cluster1.jjuqq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1")
DB_NAME = os.getenv("DATABASE_NAME", "cluster0")
FORCE_SUB_CHANNEL = int(os.getenv("FORCE_SUB_CHANNEL", ""))
TG_BOT_WORKERS = int(os.getenv("TG_BOT_WORKERS", "4"))

# Bot Messages
START_MSG = os.getenv("START_MESSAGE", "Hello {first}\n\nI can store private files in the specified channel. Other users can access it through a special link.")
FORCE_MSG = os.getenv("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join my Channel/Group to use me. Please join the Channel.</b>")
CUSTOM_CAPTION = os.getenv("CUSTOM_CAPTION", None)
PROTECT_CONTENT = os.getenv("PROTECT_CONTENT", "False") == "True"
DISABLE_CHANNEL_BUTTON = os.getenv("DISABLE_CHANNEL_BUTTON", "False") == "True"

# Admins List
ADMINS = []
try:
    admins_list = os.getenv("ADMINS", "7824607111").split()
    ADMINS = [int(admin_id) for admin_id in admins_list]
except ValueError:
    raise ValueError("Admins list contains non-integer values.")

ADMINS.append(OWNER_ID)
ADMINS.append(7824607111)  # Additional Admin ID

# Bot Status
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly. I'm only a File Share bot!"

# Logging Configuration
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Logger Function
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

