# config.py - Secure Configuration File
# NEVER SHARE THIS FILE WITH ACTUAL CREDENTIALS

import os
from os import getenv

# ===== TELEGRAM CONFIGURATION =====
API_ID = int(getenv("API_ID", "26797881"))  # my.telegram.org से लें
API_HASH = getenv("API_HASH", "9699262c708c2e45ba18bfce925ed5ed")  # my.telegram.org से लें
BOT_TOKEN = getenv("BOT_TOKEN", "7734880223:AAHG5PexgS7JdRTipt51udOg6uoINAsEjuM")  # @BotFather से लें
BOT_USERNAME = getenv("BOT_USERNAME", "apnatxtwaalabot")  # बिना @ के

# ===== USER PERMISSIONS =====
OWNER_ID = int(getenv("OWNER_ID", "6567162029"))  # आपका Telegram User ID
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6567162029").split()))

# ===== DATABASE CONFIG =====
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://sevmamra01:<db_password>@cluster0.ff29e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # MongoDB Atlas से

# ===== CHANNEL CONFIG =====
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002303981738"))  # -100 के साथ
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002303981738"))  # -100 के साथ
