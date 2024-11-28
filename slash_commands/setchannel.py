import discord
from discord import app_commands
from discord.ext import commands

from data_storage import DataStorage
from models.guild import Guild


class SetChannel(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(
        name="setchannel", description="Set the channel for the bot to read from"
    )
    async def setChannel_command(self, interaction: discord.Interaction):
        if interaction.guild is None:
            await interaction.response.send_message(
                "This command can only be used in a server.", ephemeral=True
            )
            return

        if interaction.channel is None:
            await interaction.response.send_message(
                "This command can only be used in a channel.", ephemeral=True
            )
            return

        await interaction.response.defer()

        if interaction.guild.id not in DataStorage.guild_dict:
            DataStorage.guild_dict[interaction.guild.id] = Guild(
                interaction.guild.id, interaction.channel.id, "", "th", False
            )
            DataStorage.mongo_client.insert_one(
                DataStorage.guild_dict[interaction.guild.id].toDict()
            )
        else:
            DataStorage.guild_dict[interaction.guild.id].channelID = (
                interaction.channel.id
            )
            DataStorage.mongo_client.update_one(
                {"guildID": interaction.guild.id},
                {"$set": {"channelID": interaction.channel.id}},
            )

        embed = discord.Embed(
            description=f"Channel set to <#{interaction.channel_id}>",
            color=discord.Color.blue(),
        )
        await interaction.edit_original_response(embed=embed)
