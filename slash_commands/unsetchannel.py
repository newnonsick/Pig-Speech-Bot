import discord
from discord import app_commands
from discord.ext import commands

from data_storage import DataStorage


class UnSetChannel(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(
        name="unsetchannel", description="Remove the channel for the bot to read from"
    )
    async def unsetChannel_command(self, interaction: discord.Interaction):
        if interaction.guild is None:
            await interaction.response.send_message(
                "This command can only be used in a server.", ephemeral=True
            )
            return

        await interaction.response.defer()

        if interaction.guild.id in DataStorage.guild_dict:
            DataStorage.guild_dict[interaction.guild.id].channelID = 0
            DataStorage.mongo_client.update_one(
                {"guildID": interaction.guild.id}, {"$set": {"channelID": 0}}
            )
        else:
            embed = discord.Embed(
                description="No channel to unset", color=discord.Color.red()
            )
            await interaction.edit_original_response(embed=embed)
            return

        embed = discord.Embed(description=f"Channel unset", color=discord.Color.blue())
        await interaction.edit_original_response(embed=embed)
