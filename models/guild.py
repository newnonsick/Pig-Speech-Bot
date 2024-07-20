class Guild:
    def __init__(self, guildID:int, channelID:int, prefix:str, language:str, xSaidName:bool):
        self.__guildID = guildID
        self.channelID = channelID
        self.prefix = prefix
        self.language = language
        self.xSaidName = xSaidName
        self.isReading = False
        self.readingQueue = list()

    def __str__(self):
        return self.guildId
    
    @property
    def guildID(self):
        return self.__guildID
    
    def toDict(self):
        return {
            "guildID": self.__guildID,
            "channelID": self.channelID,
            "prefix": self.prefix,
            "language": self.language,
            "xSaidName": self.xSaidName
        }
    
