import discord
from discord import app_commands
from discord.ext import commands

from data_storage import DataStorage
from models.guild import Guild


class XsaidName(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(
        name="xsaidname", description="Set the bot to read only the message"
    )
    async def xSaidName_command(self, interaction: discord.Interaction, option: str):
        if interaction.guild is None:
            await interaction.response.send_message(
                "This command can only be used in a server.", ephemeral=True
            )
            return

        if option not in ["on", "off"]:
            await interaction.response.send_message(
                "Invalid option. Please choose between 'on' and 'off'.", ephemeral=True
            )
            return

        await interaction.response.defer()

        if interaction.guild.id not in DataStorage.guild_dict:
            DataStorage.guild_dict[interaction.guild.id] = Guild(
                interaction.guild.id, 0, "", "th", True if option == "on" else False
            )
            DataStorage.mongo_client.insert_one(
                DataStorage.guild_dict[interaction.guild.id].toDict()
            )
        else:
            DataStorage.guild_dict[interaction.guild.id].xSaidName = (
                True if option == "on" else False
            )
            DataStorage.mongo_client.update_one(
                {"guildID": interaction.guild.id},
                {"$set": {"xSaidName": True if option == "on" else False}},
            )

        embed = discord.Embed(
            description=(
                f"Bot will now only read the message"
                if option == "on"
                else "Bot will now read the message with the author's name"
            ),
            color=discord.Color.blue(),
        )
        await interaction.edit_original_response(embed=embed)

    @xSaidName_command.autocomplete("option")
    async def xsaidname_autocomplete(
        self, interaction: discord.Interaction, current: str
    ):
        return [
            discord.app_commands.Choice(name="on", value="on"),
            discord.app_commands.Choice(name="off", value="off"),
        ]
