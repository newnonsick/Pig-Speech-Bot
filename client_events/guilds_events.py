from discord.ext import commands

from data_storage import DataStorage


class GuildsEvents(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        DataStorage.mongo_client.delete_one({"guildID": guild.id})
        DataStorage.guild_dict.pop(guild.id, None)
