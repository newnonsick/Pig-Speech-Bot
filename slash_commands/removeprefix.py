import discord
from discord.ext import commands
from discord import app_commands
from data_storage import DataStorage

class RemovePrefix(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="removeprefix", description="Remove the prefix for the bot") 
    async def removePrefix_command(self, interaction: discord.Interaction):
        if interaction.guild_id is None:
            await interaction.response.send_message("This command can only be used in a server.", ephemeral=True)
            return
           
        await interaction.response.defer()

        if interaction.guild.id not in DataStorage.guildDict or DataStorage.guildDict[interaction.guild.id].prefix == '':
            embed = discord.Embed(description="No prefix to remove", color=discord.Color.red())
            await interaction.edit_original_response(embed=embed)
            return

        DataStorage.guildDict[interaction.guild.id].prefix = ''
        DataStorage.mongoClient.update_one({"guildID": interaction.guild.id}, {"$set": {"prefix": ''}})

        embed = discord.Embed(description=f"Prefix removed", color=discord.Color.blue())         
        await interaction.edit_original_response(embed=embed)