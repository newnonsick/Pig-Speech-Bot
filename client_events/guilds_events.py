from discord.ext import commands
from utils import Utils
from data_storage import DataStorage

class GuildsEvents(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        DataStorage.mongoClient.delete_one({"guildID": guild.id})
        DataStorage.guildDict.pop(guild.id, None)
