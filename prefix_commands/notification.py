import asyncio

import discord
from discord.ext import commands
from discord.ui import Button, View

from data_storage import DataStorage


class Notification(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(name="notification")
    async def notification(self, ctx, *, message: str):
        if ctx.author.id != DataStorage.BOT_OWNER_ID or not message:
            return

        embedVar = (
            discord.Embed(
                title="🐷 Oink Oink! Pig Speech Notification! 🎉",
                description=(
                    f"Hello there, friend! 🐽\n"
                    f"Here's an exciting update or notification just for you:\n"
                    f"\n{message}\n\n"
                    "Thank you for being an awesome part of our community! 💖"
                ),
                color=discord.Color.magenta(),
            )
            .set_image(
                url="https://cdn.discordapp.com/attachments/1041014713816977471/1264297698190688316/PigSpeech.png"
            )
            .add_field(
                name="💌 Got Questions?",
                value="Hit me up on Discord **@newnosick** – I'm always here to help! 😄",
                inline=False,
            )
            .set_footer(
                text="Powered by Pig Speech 🐷 | We ❤️ our users!",
                icon_url="https://cdn.discordapp.com/attachments/1041014713816977471/1216018350908379216/pig_logo_2.jpg",
            )
        )

        class DecisionView(View):
            def __init__(self, client):
                super().__init__(timeout=120)
                self.client = client

            @discord.ui.button(
                label="Send Notification", style=discord.ButtonStyle.green
            )
            async def send_button(
                self, interaction: discord.Interaction, button: Button
            ):
                if interaction.user.id != ctx.author.id:
                    await interaction.response.send_message(
                        "You are not allowed to use this button.", ephemeral=True
                    )
                    return

                await interaction.response.edit_message(
                    content="Sending notifications, this may take some time...",
                    view=None,
                )

                sent_count = 0
                error_count = 0
                userSent = []
                for guild in self.client.guilds:
                    server_owner = guild.owner

                    if (
                        (not server_owner)
                        or (server_owner.id == DataStorage.BOT_OWNER_ID)
                        or (server_owner.id in userSent)
                    ):
                        continue

                    try:
                        await server_owner.send(embed=embedVar)
                        sent_count += 1
                    except discord.Forbidden:
                        # print(f"Could not send a DM to the owner of {guild.name} (ID: {guild.id}).")
                        error_count += 1
                    except Exception as e:
                        # print(f"An error occurred while sending a DM to the owner of {guild.name} (ID: {guild.id}): {e}")
                        error_count += 1
                    finally:
                        userSent.append(server_owner.id)

                    await asyncio.sleep(2)

                final_message = (
                    f"Notification process completed!\n"
                    f"✅ Successfully sent: {sent_count}\n"
                    f"❌ Failed to send: {error_count}\n"
                    f"Thank you for your patience!"
                )
                await interaction.followup.send(content=final_message)

            @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
            async def cancel_button(
                self, interaction: discord.Interaction, button: Button
            ):
                if interaction.user.id != ctx.author.id:
                    await interaction.response.send_message(
                        "You are not allowed to use this button.", ephemeral=True
                    )
                    return

                await interaction.response.edit_message(
                    content="Notification sending canceled.", view=None
                )

        await ctx.send(
            content="Here is a preview of the notification. Use the buttons below to decide:",
            embed=embedVar,
            view=DecisionView(client=self.client),
        )
