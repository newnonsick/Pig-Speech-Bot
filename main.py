import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from client_events.gateway_events import GatewayEvents
from client_events.guilds_events import GuildsEvents
from client_events.messages_events import MessagesEvents
from client_events.voice_events import VoiceEvents
from data_storage import DataStorage
from prefix_commands.addpresence import AddPresence
from prefix_commands.notification import Notification
from prefix_commands.removepresence import RemovePresence
from slash_commands.disconnect import Disconnect
from slash_commands.fix import Fix
from slash_commands.help import Help
from slash_commands.removeprefix import RemovePrefix
from slash_commands.setchannel import SetChannel
from slash_commands.setlanguage import SetLanguage
from slash_commands.setprefix import SetPrefix
from slash_commands.unsetchannel import UnSetChannel
from slash_commands.xsaidname import XsaidName

intents = discord.Intents.default()
intents.messages = True
intents.voice_states = True
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix="n!", intents=intents)


async def main():
    async with client:
        load_dotenv()
        DataStorage.initialize()
        await client.add_cog(GatewayEvents(client=client))
        await client.add_cog(GuildsEvents(client=client))
        await client.add_cog(MessagesEvents(client=client))
        await client.add_cog(VoiceEvents(client=client))
        await client.add_cog(SetChannel(client=client))
        await client.add_cog(UnSetChannel(client=client))
        await client.add_cog(SetPrefix(client=client))
        await client.add_cog(RemovePrefix(client=client))
        await client.add_cog(SetLanguage(client=client))
        await client.add_cog(XsaidName(client=client))
        await client.add_cog(Fix(client=client))
        await client.add_cog(Disconnect(client=client))
        await client.add_cog(Help(client=client))
        await client.add_cog(Notification(client=client))
        await client.add_cog(AddPresence(client=client))
        await client.add_cog(RemovePresence(client=client))
        await client.start(str(os.getenv("BOT_TOKEN")))


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except discord.HTTPException as e:
        if e.status == 429:
            print(
                "The Discord servers denied the connection for making too many requests."
            )
            print(
                "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
            )
            os.system("python restart.py")
            os.system("kill 1")
        else:
            raise e
