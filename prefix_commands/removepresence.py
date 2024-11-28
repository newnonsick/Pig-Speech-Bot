import discord
from discord.ext import commands
from discord.ui import Select, View

from data_storage import DataStorage


class RemovePresence(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="removepresence")
    async def removepresence(self, ctx):
        if ctx.author.id != DataStorage.BOT_OWNER_ID:
            await ctx.send("You don't have permission to use this command.")
            return

        if len(DataStorage.presences) == 1:
            await ctx.send("There are no presences to remove.")
            return

        embed = discord.Embed(
            title="Select a Presence to Remove",
            description="Use the dropdown below to select the presence you want to remove.",
            color=discord.Color.red(),
        )

        class PresenceSelect(View):
            def __init__(self):
                super().__init__(timeout=30)
                self.response = None

                options = [
                    discord.SelectOption(label=presence, value=presence)
                    for presence in DataStorage.presences[1:]
                ]

                self.select = Select(
                    placeholder="Choose a presence to remove...", options=options
                )
                self.select.callback = self.select_callback
                self.add_item(self.select)

            async def select_callback(self, interaction: discord.Interaction):
                self.response = self.select.values[0]
                DataStorage.presences.remove(self.response)
                await interaction.response.edit_message(
                    content=f"Presence removed: {self.response}", view=None, embed=None
                )
                self.stop()

            async def on_timeout(self):
                await ctx.send("The selection menu timed out. Please try again.")
                self.stop()

        view = PresenceSelect()

        await ctx.send(embed=embed, view=view)
