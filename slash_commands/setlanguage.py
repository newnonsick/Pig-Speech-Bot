import discord
from discord import app_commands
from discord.ext import commands

from data_storage import DataStorage
from models.guild import Guild


class SetLanguage(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(
        name="setlanguage",
        description="Set the language for bot to speak in. /help to see the list of available languages",
    )
    async def setLanguage_command(
        self, interaction: discord.Interaction, language: str
    ):
        if interaction.guild is None:
            await interaction.response.send_message(
                "This command can only be used in a server.", ephemeral=True
            )
            return

        language = language.lower().strip()

        if language not in DataStorage.LANG_DICT.keys():
            embed = discord.Embed(
                description=f"Invalid language. Please use `/help` to see the list of available languages.",
                color=discord.Color.red(),
            )
            await interaction.response.send_message(embed=embed)
            return

        await interaction.response.defer()

        if interaction.guild.id not in DataStorage.guild_dict:
            DataStorage.guild_dict[interaction.guild.id] = Guild(
                interaction.guild.id, 0, "", language, False
            )
            DataStorage.mongo_client.insert_one(
                DataStorage.guild_dict[interaction.guild.id].toDict()
            )
        else:
            DataStorage.guild_dict[interaction.guild.id].language = language
            DataStorage.mongo_client.update_one(
                {"guildID": interaction.guild.id}, {"$set": {"language": language}}
            )

        embed = discord.Embed(
            description=f"Language set to `{DataStorage.LANG_DICT[language]}`",
            color=discord.Color.blue(),
        )
        await interaction.edit_original_response(embed=embed)
