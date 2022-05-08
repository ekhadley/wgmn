import discord, ssl
from discord.ext import tasks

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # an attribute we can access from our task
        self.counter = 0

    async def setup_hook(self) -> None:
        # start the task to run in the background
        self.my_background_task.start()

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    @tasks.loop(seconds=5)  # task runs every 60 seconds
    async def my_background_task(self):
        channel = self.get_channel(551246526924455937)  # channel ID goes here
        self.counter += 1
        await channel.send(self.counter)

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in

client = MyClient()
client.run('MzUyMjI2MDQ1MjI4ODc1Nzg2.YngUnA.hORVUTyrazkOOm-6iF-A6XIHJCU')