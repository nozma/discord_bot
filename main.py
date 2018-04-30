# -*- coding:utf-8 -*-
import os
from discord.ext import commands

startup_extensions = ["cogs.calc", "cogs.conversation"]

BOT_PREFIX = ('?', '!')
bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.event
async def on_ready():
    print("以下のユーザー名でログインしています。")
    print("ユーザー名: " + bot.user.name)
    print("ユーザーID: " + bot.user.id)
    print("--------------------------------------")

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(os.environ.get("DISCORD_TOKEN"))
