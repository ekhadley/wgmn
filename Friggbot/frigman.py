import discord, ssl, asyncio
from discord.ext import tasks

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel = self.get_channel(551246526924455937)  # channel ID goes here

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

    async def on_message(self, message):
        if "test" in message.content:
           await self.channel.send("yeg")

client = MyClient()
client.run('MzUyMjI2MDQ1MjI4ODc1Nzg2.G-601j.ZGCBqrQmpmU0NoYCZvJgHuPO-3rsd_bpFVTa6g')