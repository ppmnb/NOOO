from telethofrom telethon.sync import TelegramClient

from telethon.sessions import StringSession

import os

APP_ID = input("APP_ID", "5971310627")

APP_HASH = input("APP_HASH", "371d1dc33eccaa19bb0814a27bb98f3c")

BOT_USERNAME = input("BOT_USERNAME", "ajwjhwjwjwbot")

session = input("TERMUX")

SESSION = input("TERMUX", "1BJWap1sBu5lXEw4ZCnSLUhRdpsjzlvw7Ei29ftCRtIN3kGw-SXokpEVOQZyMsTWntk6b27ygLJmo00T1sYxG66hVRrhayf09ahji8CqzUo52nk2t4-aYkfhBblHb9sRIYaxDoCWB2HGbU3QzwgIMlGo4bltHhYrKb1220CiAD8EzIX_G41hxr0N9XJSd1MrGIe5LNs_P7JR-orlrE86CqqE3Y2zjTMTOZUOxzflC_C9g9EVjB9XuXGXPLrtlP-z7UB1ptk_1KRlUjxqsIQVng1JkS2TLnHfrpljM66hbZ3USldVjounkliWz8tUa7SB7JLqRgCL7NR6TCAb3xysgtrTolw9g7k0=")

token = input("TOKEN", "5894248371:AAH-JAOK_vizSwUqcJvL6VYIeldwo0QaDL4")

fifthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)

bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)

ispay = ['yes']

ispay2 = ['yes']

bot.start()
