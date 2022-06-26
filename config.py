from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "7565862"))
API_HASH = getenv("API_HASH", "7915d5d62f4a5add0560a4d5191767b7")
BOT_TOKEN = getenv("BOT_TOKEN", "5123767305:AAGmN8s2IyMCMY5DtHRsOf37UCa5_VKqJD8")
BOT_NAME = getenv("BOT_NAME","ғᴀʟʟᴇɴ ᴍᴜsɪᴄ ʙᴏᴛ")
BOT_USERNAME = getenv("BOT_USERNAME", "Teshhsst000000_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "bar_lo0o0")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "handbsbsn")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/89cbc8b8760b6abff430f.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/89cbc8b8760b6abff430f.jpg")
SESSION_NAME = getenv("SESSION_NAME", "AQAIrExEPZwUHk_p2QkqO07yg57LFk-0m2pOJfupZm6PZnKYFvgyJdvOkFyFQHuRMm91NaC0XGVyafuh5AupmDkRGENEeWyAbChuZppTDqHBecu3HCP6dt0lTHvgjrmKiSk-GC5vy3iblCDZxmPodJMtkKw0YfoCJ_2Av_SdxwB783nx1lfWqvNe62LCn3_RZdesblKFXo5kbUkyIjdOeFDBhXcDeYUAuYQUrF_hKDtiH2oylBg4PDAjJ4274y6AbmhYWs0qX4qKp0Etv4F83UO3JTCV4do_9XfaF0lfbQNzPyj4UY1julnPrOCnaD6tZUdEIOiYjvuB5lQb35F6joofUN171gA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1001132193").split()))
