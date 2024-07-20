import discord
from discord.ext import commands
from discord import app_commands
from data_storage import DataStorage
from models.guild import Guild

class SetLanguage(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="setlanguage", description="Set the llanguage for bot to speak in") 
    async def setLanguage_command(self, interaction: discord.Interaction, language: str):     
        if interaction.guild_id is None:     
            await interaction.response.send_message("This command can only be used in a server.", ephemeral=True)
            return
        
        if language not in DataStorage.languages:
            embed = discord.Embed(description=f"Invalid language. Please use `/help` to see the list of available languages.", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)
            return
           
        await interaction.response.defer()

        if interaction.guild.id not in DataStorage.guildDict:
            DataStorage.guildDict[interaction.guild.id] = Guild(interaction.guild.id, 0, '', language, False)
            DataStorage.mongoClient.insert_one(DataStorage.guildDict[interaction.guild.id].toDict())
        else:
            DataStorage.guildDict[interaction.guild.id].language = language
            DataStorage.mongoClient.update_one({"guildID": interaction.guild.id}, {"$set": {"language": language}})

        embed = discord.Embed(description=f"Language set to `{language}`", color=discord.Color.blue())         
        await interaction.edit_original_response(embed=embed)
    