# -*- coding:utf-8 -*-
from discord.ext import commands
import numpy as np

class Calc():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="与えられた任意の数の実数の合計を返します。",
                      brief = "数値の合計")
    async def add(self, *num: float):
        try:
            ans = np.sum(num)
        except Exception:
            await self.bot.say('実数を入力してください')
            return

        result = "答えは" + str(ans) + "ですね。"
        await self.bot.say(result)

def setup(bot):
    bot.add_cog(Calc(bot))
