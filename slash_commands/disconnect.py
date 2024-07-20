import os
import discord
from discord.ext import commands
from data_storage import DataStorage
from discord import app_commands

class Disconnect(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="disconnect", description="Disconnect the bot from the voice channel")
    async def disconnect_command(self, interaction: discord.Interaction):
        if interaction.guild_id is None:
            await interaction.response.send_message("This command can only be used in a server.", ephemeral=True)
            return
        await interaction.response.defer()

        voice_clients = self.client.voice_clients
        for voice_client in voice_clients:
            if interaction.guild_id == voice_client.guild.id:
                DataStorage.guildDict[interaction.guild_id].isReading = False
                DataStorage.guildDict[interaction.guild_id].readingQueue = list()
                if os.path.exists(f"{interaction.guild_id}.mp3"):
                    os.remove(f"{interaction.guild_id}.mp3")
                await voice_client.disconnect()
                embed = discord.Embed(description="Disconnected", color=discord.Color.blue())
                await interaction.edit_original_response(embed=embed)
                return
            
        embed = discord.Embed(description="I'm not in a voice channel", color=discord.Color.red())
        await interaction.edit_original_response(embed=embed)
