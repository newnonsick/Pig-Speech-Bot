from discord.ext import commands
from utils import Utils

class GuildsEvents(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        await Utils.update_presence(self.client)  

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await Utils.update_presence(self.client) 
