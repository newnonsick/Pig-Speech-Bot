import discord

class Utils:

    @staticmethod
    async def update_presence(client):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"for {len(client.guilds)} servers")) 