import os
import discord
from discord.ext import commands
from data_storage import DataStorage
from discord import app_commands

class VoiceEvents(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        guildData = DataStorage.guildDict[member.guild.id]
        if member == self.client.user:         
            if before.channel and (after.channel is None or after.channel != before.channel):
                guildData.readingQueue = list()
                guildData.isReading = False

        if after.channel != before.channel:         
            voice_clients = self.client.voice_clients         
            for voice_client in voice_clients:             
                if before.channel == voice_client.channel or after.channel == voice_client.channel:                 
                    if (before.channel and len(before.channel.members) == 1 and before.channel.members[0] == self.client.user) or (after.channel and len(after.channel.members) == 1 and member == self.client.user):                     
                        if member == self.client.user:                         
                            guildData.readingQueue = list()                                      
                            guildData.isReading = False

                            if os.path.exists(f"{before.channel.guild.id}.mp3"): 
                                try:                            
                                    os.remove(f"{before.channel.guild.id}.mp3")  
                                except:
                                    pass                       
                            await voice_client.disconnect()                     
                        else:                         
                            guildData.readingQueue = list()                        
                            guildData.isReading = False                      
                                
                            if os.path.exists(f"{before.channel.guild.id}.mp3"):                               
                                try:                            
                                    os.remove(f"{before.channel.guild.id}.mp3")  
                                except:
                                    pass                          
                            await voice_client.disconnect()                 
                        break 