import discord, ssl
from discord.ext import tasks

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel = self.get_channel(551246526924455937)
        #self.channel = self.get_channel(785014933758410793)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

    async def on_message(self, message):
        if "ozzy" == message.content:
           await self.channel.send("yes, this is ozzy speaking")

client = MyClient()
client.run('MzUyMjI2MDQ1MjI4ODc1Nzg2.Ynh7nA.iZSWXUI2SL3bdH4TY1mliDcsgKY')
