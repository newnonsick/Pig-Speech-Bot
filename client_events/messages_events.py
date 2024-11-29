import asyncio
import os

import discord
from discord.ext import commands
from gtts import gTTS
from langdetect import detect

from data_storage import DataStorage


class MessagesEvents(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if self._should_process_message(message):
            asyncio.create_task(self._process_message(message))

    def _should_process_message(self, message):
        if (
            message.author == self.client.user
            or message.guild is None
            or not message.content
        ):
            return False
        if message.guild.id not in DataStorage.guild_dict:
            return False
        guild_data = DataStorage.guild_dict[message.guild.id]
        if message.channel.id != guild_data.channelID:
            return False
        if not message.content.startswith(guild_data.prefix):
            return False
        if message.content == DataStorage.guild_dict[message.guild.id].prefix:
            return False
        return True

    async def _process_message(self, message):
        guild_data = DataStorage.guild_dict[message.guild.id]

        try:
            user_voice_channel = message.author.voice.channel
        except AttributeError:
            await self._send_embed(
                message, "You are not in a voice channel.", discord.Color.red()
            )
            return

        in_voice_channel = discord.utils.get(
            self.client.voice_clients, guild=message.guild
        )

        if in_voice_channel and (user_voice_channel != in_voice_channel.channel):
            await self._send_embed(
                message, "I'm already in another voice channel.", discord.Color.red()
            )
            return

        message.content = message.content[len(guild_data.prefix) :]

        if guild_data.isReading:
            guild_data.readingQueue.append(message)
            return

        await self._connect_to_voice(message, user_voice_channel)
        await self._speak_message(message, guild_data)

    async def _connect_to_voice(self, message, voice_channel):
        if not discord.utils.get(self.client.voice_clients, guild=message.guild):
            permissions = voice_channel.permissions_for(message.guild.me)
            if not permissions.connect or not permissions.speak:
                await self._send_embed(
                    message,
                    "I don't have permission to connect or speak in that voice channel.",
                    discord.Color.red(),
                )
                return None

            try:
                return await voice_channel.connect()
            except discord.errors.ClientException:
                await self._send_embed(
                    message,
                    "I'm having trouble connecting to the voice channel. Please try again.",
                    discord.Color.red(),
                )
                return None
        return discord.utils.get(self.client.voice_clients, guild=message.guild)

    async def _speak_message(self, message, guild_data):
        voice = discord.utils.get(self.client.voice_clients, guild=message.guild)
        if not voice:
            return

        guild_data.isReading = True

        try:
            language = self._detect_language(message.content, guild_data.language)
            message_to_speak = self._format_message(message, guild_data, language)

            audio_file = await self._get_tts_audio(
                message.guild.id, message_to_speak, language
            )

            if audio_file:
                voice.play(discord.FFmpegPCMAudio(audio_file))  # type: ignore
                while voice.is_playing():  # type: ignore
                    await asyncio.sleep(0.1)
        except Exception as e:
            audio_file = f"{message.guild.id}.mp3"
        finally:
            guild_data.isReading = False

        if guild_data.readingQueue:
            next_message = guild_data.readingQueue.pop(0)
            asyncio.create_task(self._process_message(next_message))
        else:
            if os.path.exists(audio_file):
                try:
                    os.remove(audio_file)
                except:
                    pass

    def _detect_language(self, content, default_language):
        if default_language == "auto":
            try:
                return detect(content)
            except:
                return "en"
        return default_language if default_language in DataStorage.LANG_DICT else "en"

    def _format_message(self, message, guild_data, language):
        if guild_data.xSaidName:
            return message.content
        return (
            f"{message.author.name} {DataStorage.SAID_DICT[language]} {message.content}"
        )

    async def _get_tts_audio(self, guild_id, text, language):
        tts = gTTS(text, lang=language)
        filename = f"{guild_id}.mp3"
        tts.save(filename)
        return filename

    async def _send_embed(self, message, description, color):
        embed = discord.Embed(description=description, color=color)
        await message.channel.send(embed=embed, reference=message)

    # def cog_unload(self):
