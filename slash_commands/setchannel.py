import discord
from discord.ext import commands
from discord import app_commands
from models.guild import Guild
from data_storage import DataStorage

class SetChannel(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="setchannel", description="Set the channel for the bot to read from") 
    async def setChannel_command(self, interaction: discord.Interaction):     
        if interaction.guild_id is None:     
            await interaction.response.send_message("This command can only be used in a server.", ephemeral=True)
            return
           
        await interaction.response.defer()

        if interaction.guild.id not in DataStorage.guildDict:
            DataStorage.guildDict[interaction.guild.id] = Guild(interaction.guild.id, interaction.channel.id, '', 'th', False)
            DataStorage.mongoClient.insert_one(DataStorage.guildDict[interaction.guild.id].toDict())
        else:
            DataStorage.guildDict[interaction.guild.id].channelID = interaction.channel.id
            DataStorage.mongoClient.update_one({"guildID": interaction.guild.id}, {"$set": {"channelID": interaction.channel.id}})

        embed = discord.Embed(description=f"Channel set to <#{interaction.channel_id}>", color=discord.Color.blue())         
        await interaction.edit_original_response(embed=embed)