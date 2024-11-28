import os

import discord
from discord import app_commands
from discord.ext import commands

from data_storage import DataStorage


class Fix(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="fix", description="Fix the bot if it is not working")
    async def fix_command(self, interaction: discord.Interaction):
        if interaction.guild_id is None:
            await interaction.response.send_message(
                "This command can only be used in a server.", ephemeral=True
            )
            return
        await interaction.response.defer()

        voice_clients = self.client.voice_clients
        for voice_client in voice_clients:
            if interaction.guild_id == voice_client.guild.id:
                await voice_client.disconnect()
                break

        DataStorage.guild_dict[interaction.guild_id].readingQueue = list()
        DataStorage.guild_dict[interaction.guild_id].isReading = False

        if os.path.exists(f"{interaction.guild_id}.mp3"):
            try:
                os.remove(f"{interaction.guild_id}.mp3")
            except:
                pass

        embed = discord.Embed(description="Fixed", color=discord.Color.blue())
        await interaction.edit_original_response(embed=embed)
