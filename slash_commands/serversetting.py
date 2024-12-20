import discord
from discord import app_commands
from discord.ext import commands

from data_storage import DataStorage
from models.guild import Guild


class ServerSetting(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(
        name="serversetting", description="Get the server settings for the bot"
    )
    async def serverSetting_command(self, interaction: discord.Interaction):
        if interaction.guild is None:
            await interaction.response.send_message(
                "This command can only be used in a server.", ephemeral=True
            )
            return

        await interaction.response.defer()

        guildID = interaction.guild.id

        if guildID not in DataStorage.guild_dict:
            embed = discord.Embed(
                description="No settings for this server", color=discord.Color.red()
            )
            await interaction.edit_original_response(embed=embed)
            return

        guild = DataStorage.guild_dict[guildID]

        await interaction.edit_original_response(
            embed=self._create_settings_embed(guild)
        )

    def _create_settings_embed(self, guild: Guild) -> discord.Embed:
        embed = discord.Embed(
            title="🌟 Server Settings 🌟",
            description="Here are the current server settings! 🎉",
            color=discord.Color.magenta(),
        )
        embed.add_field(
            name="📢 Channel",
            value=f"<#{guild.channelID}>" if guild.channelID else "Not set",
            inline=False,
        )
        embed.add_field(
            name="🌍 Language",
            value=f"`{DataStorage.LANG_DICT.get(guild.language, 'Unknown')} ({guild.language})`",
            inline=True,
        )
        embed.add_field(
            name="⚙️ Prefix",
            value=f"`{guild.prefix if guild.prefix else "None"}`",
            inline=True,
        )
        embed.add_field(
            name="🔊 xSaidName",
            value=f"`{guild.xSaidName if guild.xSaidName else "Not configured"}`",
            inline=False,
        )
        embed.add_field(
            name="ℹ️ Need Help?",
            value="Use `/help` for more info! 📚",
            inline=False,
        )
        embed.set_footer(text="Customize these settings as you like! ✨")
        return embed
