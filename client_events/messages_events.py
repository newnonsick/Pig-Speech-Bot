import asyncio
import os
import discord
from discord.ext import commands
from gtts import gTTS
from data_storage import DataStorage
from langdetect import detect

class MessagesEvents(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if message.guild is None:         
            return

        if not message.content:
            return

        if message.guild.id not in DataStorage.guildDict:
            return

        guildData = DataStorage.guildDict[message.guild.id]

        if message.channel.id != guildData.channelID:
            return

        if not message.content.startswith(guildData.prefix):
            return

        try:
            userVoiceChannel = message.author.voice.channel
        except AttributeError:                 
            embed = discord.Embed(description="You are not in a voice channel.", color=discord.Color.red())                 
            await message.channel.send(embed=embed, reference=message)                 
            return
        inVoiceChannel = discord.utils.get(self.client.voice_clients, guild=message.guild) 

        if inVoiceChannel and (userVoiceChannel != inVoiceChannel.channel):                 
            embed = discord.Embed(description="I'm already in another voice channel.", color=discord.Color.red())                 
            await message.channel.send(embed=embed, reference=message)                 
            return
        
        message.content = message.content[len(guildData.prefix):]

        if guildData.isReading:
            guildData.readingQueue.append(message)
            return
        else:
            if not inVoiceChannel:                 
                permissions = userVoiceChannel.permissions_for(message.guild.me)                 
                if not permissions.connect or not permissions.speak:                     
                    embed = discord.Embed(description="I don't have permission to connect or speak in that voice channel.", color=discord.Color.red())                    
                    await message.channel.send(embed=embed, reference=message)                     
                    return   
                               
                voice = await userVoiceChannel.connect()  

                while not voice.is_connected():                     
                    await asyncio.sleep(0.5)  
            else:
                voice = inVoiceChannel
                permissions = userVoiceChannel.permissions_for(message.guild.me)
                if not permissions.speak:
                    embed = discord.Embed(description="I don't have permission to speak in that voice channel.", color=discord.Color.red())
                    await message.channel.send(embed=embed, reference=message)
                    return

            guildData.isReading = True

            language = guildData.language
            
            if language == 'auto':
                try:
                    language = detect(message.content)
                except:
                    language = 'en'

            if language not in DataStorage.languages:
                language = 'en'

            if guildData.xSaidName:
                messageToSpeak = message.content
            else:
                messageToSpeak = f"{message.author.name} {DataStorage.saidDict[language]} {message.content}"

            tts = gTTS(messageToSpeak, lang=language)

            tts.save(f"{message.guild.id}.mp3")
            voice.play(discord.FFmpegPCMAudio(f"{message.guild.id}.mp3"))

            while voice.is_playing():                     
                await asyncio.sleep(1) 

            if os.path.exists(f"{message.guild.id}.mp3"):
                os.remove(f"{message.guild.id}.mp3")

            guildData.isReading = False

            if guildData.readingQueue:
                await self.on_message(guildData.readingQueue.pop(0))
        
