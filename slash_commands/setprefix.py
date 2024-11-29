import discord
from discord import app_commands
from discord.ext import commands

from data_storage import DataStorage
from models.guild import Guild


class SetPrefix(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(
        name="setprefix", description="(Optional) Set the prefix for the bot"
    )
    async def setPrefix_command(self, interaction: discord.Interaction, prefix: str):
        if interaction.guild is None:
            await interaction.response.send_message(
                "This command can only be used in a server.", ephemeral=True
            )
            return

        if len(prefix) > 5:
            await interaction.response.send_message(
                "Prefix can't be longer than 5 characters.", ephemeral=True
            )

        await interaction.response.defer()

        if interaction.guild.id not in DataStorage.guild_dict:
            DataStorage.guild_dict[interaction.guild.id] = Guild(
                interaction.guild.id, 0, prefix, "th", False
            )
            DataStorage.mongo_client.insert_one(
                DataStorage.guild_dict[interaction.guild.id].toDict()
            )
        else:
            DataStorage.guild_dict[interaction.guild.id].prefix = prefix
            DataStorage.mongo_client.update_one(
                {"guildID": interaction.guild.id}, {"$set": {"prefix": prefix}}
            )

        embed = discord.Embed(
            description=f"Prefix set to `{prefix}`", color=discord.Color.blue()
        )
        await interaction.edit_original_response(embed=embed)
