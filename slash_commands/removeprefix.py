import discord
from discord import app_commands
from discord.ext import commands

from data_storage import DataStorage


class RemovePrefix(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(
        name="removeprefix", description="Remove the prefix for the bot"
    )
    async def removePrefix_command(self, interaction: discord.Interaction):
        if interaction.guild is None:
            await interaction.response.send_message(
                "This command can only be used in a server.", ephemeral=True
            )
            return

        await interaction.response.defer()

        guildID = interaction.guild.id

        if (
            guildID not in DataStorage.guild_dict
            or DataStorage.guild_dict[guildID].prefix == ""
        ):
            embed = discord.Embed(
                description="No prefix to remove", color=discord.Color.red()
            )
            await interaction.edit_original_response(embed=embed)
            return

        DataStorage.guild_dict[guildID].prefix = ""
        DataStorage.mongo_client.update_one(
            {"guildID": guildID}, {"$set": {"prefix": ""}}
        )

        embed = discord.Embed(description=f"Prefix removed", color=discord.Color.blue())
        await interaction.edit_original_response(embed=embed)
