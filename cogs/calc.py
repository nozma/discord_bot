# -*- coding:utf-8 -*-
from discord.ext import commands
import numpy as np

class Calc():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="与えられた任意の数の実数の合計を返します。",
                      brief = "数値の合計")
    async def add(self, *num: str):
        try:
            num = [float(i) for i in num]
        except Exception:
            await self.bot.say("数字を入力してください。")

        ans = np.sum(num)
        result = "答えは" + str(ans) + "ですね。"
        await self.bot.say(result)

def setup(bot):
    bot.add_cog(Calc(bot))
