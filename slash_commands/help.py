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
        self.buttomImage = "https://cdn.discordapp.com/attachments/1041014713816977471/1216018299465371668/image.png?ex=65fedc4b&is=65ec674b&hm=af5149ecb6915e4543a88bbd525e2f92436bb546249d27a14ca0677c614c86b6&"  

    async def callback(self, interaction: discord.Interaction):         
        if self.values[0] == "Main Page":             
            embedVar = discord.Embed().set_author(name="Pig Speech", icon_url="https://cdn.discordapp.com/attachments/1041014713816977471/1216018350908379216/pig_logo_2.jpg?ex=65fedc57&is=65ec6757&hm=6e1d7e6c1f1c6a86e26a1072d7beef83a69ee33074b0925486745744c9e1612e&").set_image(url=self.buttomImage)             
            embedVar.add_field(name="🖥 INVITE BOT", value="┊[CLICK HERE](https://discord.com/api/oauth2/authorize?client_id=1196197441381339298&permissions=551906461696&scope=bot)", inline=False)             
            embedVar.add_field(name="📖 Privacy Policy", value="┊[CLICK HERE](https://shorturl.at/CswvS)", inline=False)
            await interaction.response.edit_message(embed=embedVar)         
        elif self.values[0] == "How to make a bot speak":                          
            embedVar = discord.Embed(title="📄 How to make a bot speak", description="/setprefix เพื่อเซ็ต prefix เพื่อให้บอทอ่าน (ไม่เซ็ตก็ได้)").set_image(url=self.buttomImage)             
            embedVar.add_field(name="Usage", 
            value="""             
            ┊ **ถ้าเช็ต prefix ให้พิมพ์ prefix ตามด้วยคำที่ต้องการให้บอทอ่าน** 
            ┊ **/setprefix  .s** > `เซ็ต prefix เป็น .s`             
            ┊ **.s สวัสดี** > `บอทจะอ่านว่าสวัสดี`                 
            ┊             
            ┊ **ถ้าไม่เช็ต prefix \ให้พิมพ์แค่คำที่ต้องการให้บอทอ่าน**             
            ┊ **สวัสดี** > `บอทจะอ่านว่าสวัสดี`                                               
            """, inline=False)             
            await interaction.response.edit_message(embed=embedVar)         
        elif self.values[0] == "Slash Commands":                          
            embedVar = discord.Embed(title="📏 Slash Commands", description="Prefix ที่ไว้สำหรับเรียกใช้คำสั่งคือ `/`").set_image(url=self.buttomImage)             
            embedVar.add_field(name="Commands", 
            value="""             
            ┊ **/help** > `ดูคำสั่งทั้งหมด`             
            ┊ **/fix** > `แก้ไขบัค`             
            ┊ **/disconnect** > `ให้บอทออกจากห้อง`             
            ┊ **/setchannel** > `ตั้งค่าห้องที่จะให้บอทอ่าน`             
            ┊ **/unsetchannel** > `ยกเลิกการตั้งค่าห้องที่จะให้บอทอ่าน`             
            ┊ **/setprefix** > `ตั้งค่า prefix ให้กับบอท`  
            ┊ **/removeprefix** > `ลบ prefix ที่ตั้งไว้` 
            ┊ **/xsaidname** > `ให้บอทอ่านแค่ข้อความไม่พูดชื่อ`
            ┊ **/setlanguage** > `เปลี่ยนภาษาที่บอทจะพูด`          
            """, inline=False)             
            await interaction.response.edit_message(embed=embedVar) 
        elif self.values[0] == "Support Languages":
            embedVar = discord.Embed(title="🌐 Support Languages", description="ดูภาษาที่บอท support").set_image(url=self.buttomImage)
            embedVar.add_field(name="Languages", 
            value="""    
            ┊ **auto** > `Auto Detect Language`      
            ┊ **af** > `Afrikaans`
            ┊ **ar** > `Arabic`
            ┊ **bg** > `Bulgarian`
            ┊ **bn** > `Bengali`
            ┊ **bs** > `Bosnian`
            ┊ **ca** > `Catalan`
            ┊ **cs** > `Czech`
            ┊ **da** > `Danish`
            ┊ **de** > `German`
            ┊ **el** > `Greek`
            ┊ **en** > `English`
            ┊ **es** > `Spanish`
            ┊ **et** > `Estonian`
            ┊ **fi** > `Finnish`
            ┊ **fr** > `French`
            ┊ **gu** > `Gujarati`
            ┊ **hi** > `Hindi`
            ┊ **hr** > `Croatian`
            ┊ **hu** > `Hungarian`
            ┊ **id** > `Indonesian`
            ┊ **is** > `Icelandic`
            ┊ **it** > `Italian`
            ┊ **iw** > `Hebrew`
            ┊ **ja** > `Japanese`
            ┊ **jw** > `Javanese`  
            ┊ **km** > `Khmer`
            ┊ **kn** > `Kannada`
            ┊ **ko** > `Korean`   
            ┊ **la** > `Latin` 
            ┊ **lv** > `Latvian`   
            """, inline=False) 
            embedVar.add_field(name="Usage", 
            value="""             
            ┊ **/setlanguage en** > `เปลี่ยนภาษาเป็นอังกฤษ`        
            """, inline=False) 
            await interaction.response.edit_message(embed=embedVar)
        elif self.values[0] == "Support Languages 2":
            embedVar = discord.Embed(title="✈️ Support Languages 2", description="ดูภาษาที่บอท support").set_image(url=self.buttomImage)
            embedVar.add_field(name="Languages", 
            value="""
            ┊ **ml** > `Malayalam`
            ┊ **mr** > `Marathi`
            ┊ **ms** > `Malay`
            ┊ **my** > `Myanmar (Burmese)`
            ┊ **ne** > `Nepali`
            ┊ **nl** > `Dutch`
            ┊ **no** > `Norwegian`
            ┊ **pl** > `Polish`
            ┊ **pt** > `Portuguese`
            ┊ **ro** > `Romanian`
            ┊ **ru** > `Russian`
            ┊ **si** > `Sinhala`
            ┊ **sk** > `Slovak`
            ┊ **sq** > `Albanian`
            ┊ **sr** > `Serbian`
            ┊ **su** > `Sundanese`
            ┊ **sv** > `Swedish`
            ┊ **sw** > `Swahili`
            ┊ **ta** > `Tamil`
            ┊ **te** > `Telugu`
            ┊ **th** > `Thai`
            ┊ **tl** > `Filipino`
            ┊ **tr** > `Turkish`
            ┊ **uk** > `Ukrainian`
            ┊ **ur** > `Urdu`
            ┊ **vi** > `Vietnamese`
            ┊ **zh-CN** > `Chinese (Simplified)`
            ┊ **zh-TW** > `Chinese (Mandarin/Taiwan)`
            ┊ **zh** > `Chinese (Mandarin)`         
            """, inline=False) 
            embedVar.add_field(name="Usage", 
            value="""             
            ┊ **/setlanguage en** > `เปลี่ยนภาษาเป็นอังกฤษ`        
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
        embedVar = discord.Embed().set_author(name="Pig Speech", icon_url="https://cdn.discordapp.com/attachments/1041014713816977471/1216018350908379216/pig_logo_2.jpg?ex=65fedc57&is=65ec6757&hm=6e1d7e6c1f1c6a86e26a1072d7beef83a69ee33074b0925486745744c9e1612e&").set_image(url="https://cdn.discordapp.com/attachments/1041014713816977471/1216018299465371668/image.png?ex=65fedc4b&is=65ec674b&hm=af5149ecb6915e4543a88bbd525e2f92436bb546249d27a14ca0677c614c86b6&")     
        embedVar.add_field(name="🖥 INVITE BOT", value="┊[CLICK HERE](https://discord.com/api/oauth2/authorize?client_id=1196197441381339298&permissions=551906461696&scope=bot)", inline=False)     
        embedVar.add_field(name="📖 Privacy Policy", value="┊[CLICK HERE](https://shorturl.at/CswvS)", inline=False)
        await interaction.edit_original_response(embed=embedVar,view=Select_Help_View()) 