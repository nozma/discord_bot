# -*- coding:utf-8 -*-
import os
from discord.ext import commands

BOT_PREFIX = ('?', '!')

bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
    print("以下のユーザー名でログインしています。")
    print("ユーザー名: " + bot.user.name)
    print("ユーザーID: " + bot.user.id)
    print("--------------------------------------")

bot.run(os.environ.get("DISCORD_TOKEN"))
