import asyncio

from discord.ext import commands

from utils import Utils


class GatewayEvents(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.tree.sync()
        if not self.client.user:
            print("We are not logged in.")
            return
        print(f"We have logged in as {self.client.user.name}")
        asyncio.create_task(Utils.update_presence(self.client))
