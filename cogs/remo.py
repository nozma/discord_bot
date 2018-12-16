# -*- coding:utf-8 -*-
from discord.ext import commands
import requests
import os


class Remo():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="私の部屋の温湿度を知ることが出来ます。",
                      brief="温湿度の取得")
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
            await self.bot.say("取得できませんでした。")

        d = response.json()
        result = "現在私の部屋は\n" +\
            " 気温:" + str(d[0]["newest_events"]["te"]["val"]) + "℃\n"\
            " 湿度:" + str(d[0]["newest_events"]["hu"]["val"]) + "%\n"\
            "です。"
        await self.send(result)


def setup(bot):
    bot.add_cog(Remo(bot))
