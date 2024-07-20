from discord.ext import commands
from utils import Utils

class GatewayEvents(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.tree.sync()
        await Utils.update_presence(self.client)
        print(f'We have logged in as {self.client.user.name}')  
