import random
import discord

class Conversation():
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if self.bot.user == message.author:
            return

        if message.channel.name == 'benkyo_yatta':
            if "勉強した" in message.content:
                mlist = ["えらい", "すっごーい", "えらみ", "えらさ"]
                await self.bot.send_message(message.channel, random.choice(mlist))

        if message.channel.name == "hello_bot":
            if "こんにちは" in message.content:
                mlist = [
                    "ちーっす",
                    "こんにちは! " + message.author.name + "さん!"
                    ]
                await self.bot.send_message(message.channel, random.choice(mlist))
            elif "こんばんは" in message.content:
                mlist = [
                    "ねむい",
                    "こんばんは! " + message.author.name + "さん!"
                ]
                await self.bot.send_message(message.channel, random.choice(mlist))
            elif "おはよう" in message.content:
                mlist = [
                    "ねむい",
                    "おはようございます! " + message.author.name + "さん!"
                ]
                await self.bot.send_message(message.channel, random.choice(mlist))
            else:
                mlist = [
                    "何を言うとるんや…",
                    "わからん…なんも…",
                    "ごめんなさい! 何を言っているのか理解できませんでした!"
                ]
                await self.bot.send_message(message.channel, random.choice(mlist))

def setup(bot):
    bot.add_cog(Conversation(bot))
