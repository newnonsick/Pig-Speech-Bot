import asyncio

import discord
from discord.ext.commands import Bot

from data_storage import DataStorage


class Utils:

    @staticmethod
    async def update_presence(client: Bot):
        print("Updating presence...")
        while True:
            try:
                presences = DataStorage.presences

                if presences:
                    presences.pop(0)

                default_presence = f"{len(client.guilds)} servers"
                presences.insert(0, default_presence)

                for presence in presences:
                    await client.change_presence(
                        activity=discord.Activity(
                            type=discord.ActivityType.watching, name=presence
                        )
                    )
                    await asyncio.sleep(60)
            except Exception as e:
                print(f"An error occurred while updating presence: {e}")
                await asyncio.sleep(60)
