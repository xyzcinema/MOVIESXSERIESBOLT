# ©️ @Sujan_Ch || @Sujan_BotZ

import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", ""))
  API_HASH = os.environ.get("API_HASH", "")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "H_G_R_A_Bot") # bot username without @
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001813638350"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", ""))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://sujanch5:sujanch5@cluster0.jz36jmo.mongodb.net/?appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001813638350")
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
Tʜɪꜱ Iꜱ Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ.
Sᴇɴᴅ Mᴇ Aɴʏ Mᴇᴅɪᴀ Oʀ Fɪʟᴇ. I Cᴀɴ Wᴏʀᴋ Iɴ Cʜᴀɴɴᴇʟ Tᴏᴏ. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [Sujan_Ch](https://t.me/Sujan_Ch)
"""
  HOME_TEXT = """
Hᴇʟʟᴏ, [{}](tg://user?id={})♥️\n\nTʜɪꜱ Iꜱ Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ.

Jᴏɪɴ: @Sujan_BotZ"""
