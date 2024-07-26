import discord
from discord.ext import commands
from discord import app_commands

class Select_Help(discord.ui.Select):     
    def __init__(self):         
        options=[            
        discord.SelectOption(label="Please select an option!",emoji="🏡",default=True),             
        discord.SelectOption(label="Main Page",emoji="🗼"),             
        discord.SelectOption(label="How to make a bot speak",emoji="❔"),             
        discord.SelectOption(label="Slash Commands",emoji="📏"),
        discord.SelectOption(label="Support Languages",emoji="🌐"),
        discord.SelectOption(label="Support Languages 2",emoji="✈️"),
        ]         
        super().__init__(max_values=1,min_values=1,options=options) 
        self.buttomImage = "https://cdn.discordapp.com/attachments/1041014713816977471/1264297698190688316/PigSpeech.png?ex=669d5c7c&is=669c0afc&hm=8937ed0e690cf64479944749c2417e87c41cc4d1b18a9ddd826b01f8950da6df&"  

    async def callback(self, interaction: discord.Interaction):         
        if self.values[0] == "Main Page":             
            embedVar = discord.Embed().set_author(name="Pig Speech", icon_url="https://cdn.discordapp.com/attachments/1041014713816977471/1216018350908379216/pig_logo_2.jpg?ex=65fedc57&is=65ec6757&hm=6e1d7e6c1f1c6a86e26a1072d7beef83a69ee33074b0925486745744c9e1612e&").set_image(url=self.buttomImage)             
            embedVar.add_field(name="🖥 INVITE BOT", value="┊[CLICK HERE](https://discord.com/oauth2/authorize?client_id=1196197441381339298)", inline=False)             
            embedVar.add_field(name="📖 Privacy Policy", value="┊[CLICK HERE](https://shorturl.at/CswvS)", inline=False)
            await interaction.response.edit_message(embed=embedVar)         
        elif self.values[0] == "How to make a bot speak":                          
            embedVar = discord.Embed(title="📄 How to make a bot speak", description="").set_image(url=self.buttomImage)             
            embedVar.add_field(name="", 
            value="""             
**Set up your channel first by using** `/setchannel` **and type in that channel**:

- **With Prefix** (Set up a prefix first using `/setprefix [prefix]`):
    - If you set a prefix, type the prefix followed by the message you want the bot to speak.
  - **Example**: Typing `[prefix] Hello` makes the bot speak "Hello"

- **Without Prefix**:
    - Simply type the message you want the bot to speak.
  - **Example**: Typing `Hello` will make the bot speak "Hello"

- **`/xsaidname [on/off]`**: Toggle the feature that lets the bot read messages without announcing the user's name.
    - With `xsaidname off`: Typing "Hello" will make the bot say, "<username> said Hello"
  - With `xsaidname on`: Typing "Hello" will make the bot say, "Hello"                                           
            """, inline=False)             
            await interaction.response.edit_message(embed=embedVar)         
        elif self.values[0] == "Slash Commands":            
            embedVar = discord.Embed(title="📏 Slash Commands", description="").set_image(url=self.buttomImage)             
            embedVar.add_field(name="Commands", 
            value="""             
- **`/help`**: View all available commands and learn how to use them effectively.
- **`/fix`**: Automatically fixes common issues or bugs to ensure smooth operation.
- **`/disconnect`**: Commands the bot to leave the voice channel, providing control over its activity.
- **`/setchannel`**: Designate a specific channel where the bot will read messages, allowing for tailored usage.
- **`/unsetchannel`**: Remove the channel setting.
- **`/setprefix [prefix]`**: Customize the prefix for bot commands to suit your server's style.
- **`/removeprefix`**: Remove the previously set prefix, reverting to default settings.
- **`/xsaidname [on/off]`**: Toggle the feature that lets the bot read messages without announcing the user's name.
    - With `xsaidname off`: Typing "Hello" will make the bot say, "<username> said Hello"
  - With `xsaidname on`: Typing "Hello" will make the bot say, "Hello"
- **`/setlanguage [language_code]`**: Change the language the bot uses to speak, perfect for multilingual communities.
            """, inline=False)             
            await interaction.response.edit_message(embed=embedVar) 
        elif self.values[0] == "Support Languages":
            embedVar = discord.Embed(title="🌐 Support Languages", description="").set_image(url=self.buttomImage)
            embedVar.add_field(name="Languages", 
            value="""         
- **af** > `Afrikaans`
- **ar** > `Arabic`
- **bg** > `Bulgarian`
- **bn** > `Bengali`
- **bs** > `Bosnian`
- **ca** > `Catalan`
- **cs** > `Czech`
- **da** > `Danish`
- **de** > `German`
- **el** > `Greek`
- **en** > `English`
- **es** > `Spanish`
- **et** > `Estonian`
- **fi** > `Finnish`
- **fr** > `French`
- **gu** > `Gujarati`
- **hi** > `Hindi`
- **hr** > `Croatian`
- **hu** > `Hungarian`
- **id** > `Indonesian`
- **is** > `Icelandic`
- **it** > `Italian`
- **iw** > `Hebrew`
- **ja** > `Japanese`
- **jw** > `Javanese`  
- **km** > `Khmer`
- **kn** > `Kannada`
- **ko** > `Korean`   
- **la** > `Latin` 
- **lv** > `Latvian`   
            """, inline=False) 
            embedVar.add_field(name="Usage", 
            value="""             
- **/setlanguage en** > `Change the language to English`   
- **/setlanguage auto** > `Let the bot choose the language by itself`
            """, inline=False) 
            await interaction.response.edit_message(embed=embedVar)
        elif self.values[0] == "Support Languages 2":
            embedVar = discord.Embed(title="✈️ Support Languages 2", description="").set_image(url=self.buttomImage)
            embedVar.add_field(name="Languages", 
            value="""
- **ml** > `Malayalam`
- **mr** > `Marathi`
- **ms** > `Malay`
- **my** > `Myanmar (Burmese)`
- **ne** > `Nepali`
- **nl** > `Dutch`
- **no** > `Norwegian`
- **pl** > `Polish`
- **pt** > `Portuguese`
- **ro** > `Romanian`
- **ru** > `Russian`
- **si** > `Sinhala`
- **sk** > `Slovak`
- **sq** > `Albanian`
- **sr** > `Serbian`
- **su** > `Sundanese`
- **sv** > `Swedish`
- **sw** > `Swahili`
- **ta** > `Tamil`
- **te** > `Telugu`
- **th** > `Thai`
- **tl** > `Filipino`
- **tr** > `Turkish`
- **uk** > `Ukrainian`
- **ur** > `Urdu`
- **vi** > `Vietnamese`
- **zh-CN** > `Chinese (Simplified)`
- **zh-TW** > `Chinese (Mandarin/Taiwan)`
- **zh** > `Chinese (Mandarin)`         
            """, inline=False) 
            embedVar.add_field(name="Usage", 
            value="""             
- **/setlanguage en** > `Change the language to English`   
- **/setlanguage auto** > `Let the bot choose the language by itself`      
            """, inline=False) 
            await interaction.response.edit_message(embed=embedVar)

class Select_Help_View(discord.ui.View):     
    def __init__(self, *, timeout = 180):         
        super().__init__(timeout=timeout)         
        self.add_item(Select_Help())

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="help", description="Show the help menu") 
    async def help_command(self, interaction: discord.Interaction):     
        await interaction.response.defer()     
        embedVar = discord.Embed().set_author(name="Pig Speech", icon_url="https://cdn.discordapp.com/attachments/1041014713816977471/1216018350908379216/pig_logo_2.jpg?ex=65fedc57&is=65ec6757&hm=6e1d7e6c1f1c6a86e26a1072d7beef83a69ee33074b0925486745744c9e1612e&").set_image(url="https://cdn.discordapp.com/attachments/1041014713816977471/1264297698190688316/PigSpeech.png?ex=669d5c7c&is=669c0afc&hm=8937ed0e690cf64479944749c2417e87c41cc4d1b18a9ddd826b01f8950da6df&")     
        embedVar.add_field(name="🖥 INVITE BOT", value="┊[CLICK HERE](https://discord.com/oauth2/authorize?client_id=1196197441381339298)", inline=False)     
        embedVar.add_field(name="📖 Privacy Policy", value="┊[CLICK HERE](https://shorturl.at/CswvS)", inline=False)
        await interaction.edit_original_response(embed=embedVar,view=Select_Help_View()) 