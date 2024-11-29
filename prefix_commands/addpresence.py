from discord.ext import commands

from data_storage import DataStorage


class AddPresence(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(name="addpresence")
    async def addpresence(self, ctx, *, message: str):
        if ctx.author.id != DataStorage.BOT_OWNER_ID or not message:
            return

        if message in DataStorage.presences:
            await ctx.send("This presence already exists.")
            return

        try:
            DataStorage.presences.append(message)
        except Exception as e:
            print(f"An error occurred while adding presence: {e}")
            return

        await ctx.send(f"Presence added: {message}")
