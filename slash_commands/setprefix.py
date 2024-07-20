import discord
from discord.ext import commands
from discord import app_commands
from data_storage import DataStorage
from models.guild import Guild

class SetPrefix(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="setprefix", description="(Optional) Set the prefix for the bot") 
    async def setPrefix_command(self, interaction: discord.Interaction, prefix: str):
        if interaction.guild_id is None:
            await interaction.response.send_message("This command can only be used in a server.", ephemeral=True)
            return
           
        await interaction.response.defer()

        if interaction.guild.id not in DataStorage.guildDict:
            DataStorage.guildDict[interaction.guild.id] = Guild(interaction.guild.id, 0, prefix, 'th', False)
            DataStorage.mongoClient.insert_one(DataStorage.guildDict[interaction.guild.id].toDict())
        else:
            DataStorage.guildDict[interaction.guild.id].prefix = prefix
            DataStorage.mongoClient.update_one({"guildID": interaction.guild.id}, {"$set": {"prefix": prefix}})

        embed = discord.Embed(description=f"Prefix set to `{prefix}`", color=discord.Color.blue())
        await interaction.edit_original_response(embed=embed)
        