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
client.run('MzQ1MTM1NTA1MDQzNzUwOTEy.YnhmkQ.ie7YQoKui4wVHZfPYIX-eVX3z0o')