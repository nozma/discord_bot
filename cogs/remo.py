# -*- coding:utf-8 -*-
from discord.ext import commands
import requests
import os
import discord
import pyper


class Remo():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="私の部屋の温湿度と明るさを知ることが出来ます。",
                      brief="温湿度と明るさの取得")
    async def gettemp(ctx, self):
        headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer ' + os.environ.get("REMO_TOKEN")
        }
        try:
            response = requests.get(
                'https://api.nature.global/1/devices',
                headers=headers)
        except Exception:
            await self.send("取得できませんでした。")

        d = response.json()
        result = "現在私の部屋は\n" +\
            " 気温:" + str(d[0]["newest_events"]["te"]["val"]) + "℃\n"\
            " 湿度:" + str(d[0]["newest_events"]["hu"]["val"]) + "%\n"\
            " 明るさ:" + str(d[0]["newest_events"]["il"]["val"]) + "\n"\
            "です。"
        await self.send(result)

    @commands.command(description="私の部屋の温湿度と明るさをプロットします。",
                      brief="温湿度と明るさのプロット")
    async def plottemp(ctx, self):
        r = pyper.R()
        r("source(file='/home/rito/Programming/Python/discord_bot/cogs/plot.R')")
        await self.send("部屋の温湿度と明るさはこんな感じです。")
        await self.send(file=discord.File('/home/rito/image/plot.png'))


def setup(bot):
    bot.add_cog(Remo(bot))
