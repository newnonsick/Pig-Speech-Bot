import json
from models.guild import Guild
from models.mongodb_client import MongoDBClient
import os

class DataStorage:
    # Class variables to store data
    guildDict  = {}
    mongoClient = None
    saidDict = {}
    landict = {}

    @classmethod
    def initialize(cls):
        # Initialize the MongoDB client using environment variables
        mongo_uri = os.getenv('MONGO_URI')
        mongo_db = os.getenv('MONGO_DB')
        mongo_collection = os.getenv('MONGO_COLLECTION')

        if not (mongo_uri and mongo_db and mongo_collection):
            raise ValueError("MongoDB environment variables are not set properly.")

        cls.mongoClient = MongoDBClient(mongo_uri, mongo_db, mongo_collection)
        
        # Retrieve all guild IDs
        guild_list = cls.mongoClient.find_all_guildID()

        # Initialize guild dictionary with chat history
        for guild_id in guild_list:
            guild = cls.mongoClient.find_one({"guildID": guild_id})
            cls.guildDict[guild_id] = Guild(guild['guildID'], guild['channelID'], guild['prefix'], guild['language'], guild['xSaidName'])

        cls.saidDict = {'af': 'gesê', 'ar': 'قال', 'bg': 'казах', 'bn': 'বলেছেন', 'bs': 'rekao je', 'ca': 'dit', 'cs': 'řekl', 'da': 'sagde', 'de': 'sagte', 'el': 'είπε', 'en': 'Say that', 'es': 'dicho', 'et': 'ütles', 'fi': 'sanoi', 'fr': 'dit', 'gu': 'જણાવ્યું હતું', 'hi': 'कहा', 'hr': 'rekao je', 'hu': 'mondott', 'id': 'dikatakan', 'is': 'sagði', 'it': 'disse', 'iw': 'אמר', 'ja': '言った', 'jw': 'ngandika', 'km': 'បាននិយាយថា', 'kn': 'ಎಂದರು', 'ko': '말했다', 'la': 'dixit', 'lv': 'teica', 'ml': 'പറഞ്ഞു', 'mr': 'म्हणाला', 'ms': 'berkata', 'my': 'ဟုဆိုသည်။', 'ne': 'भन्नुभयो', 'nl': 'gezegd', 'no': 'sa', 'pl': 'powiedział', 'pt': 'disse', 'ro': 'a spus', 'ru': 'сказал', 'si': 'කිව්වා', 'sk': 'povedal', 'sq': 'tha', 'sr': 'рекао', 'su': 'ceuk', 'sv': 'sa', 'sw': 'sema', 'ta': 'கூறினார்', 'te': 'అన్నారు', 'th': 'บอกว่า', 'tl': 'sabi', 'tr': 'söz konusu', 'uk': 'сказав', 'ur': 'کہا', 'vi': 'nói', 'zh-CN': '说', 'zh-TW': '說', 'zh': '說'}
        cls.landict = {'auto': 'Auto', 'af': 'Afrikaans', 'ar': 'Arabic', 'bg': 'Bulgarian', 'bn': 'Bengali', 'bs': 'Bosnian', 'ca': 'Catalan', 'cs': 'Czech', 'da': 'Danish', 'de': 'German', 'el': 'Greek', 'en': 'English', 'es': 'Spanish', 'et': 'Estonian', 'fi': 'Finnish', 'fr': 'French', 'gu': 'Gujarati', 'hi': 'Hindi', 'hr': 'Croatian', 'hu': 'Hungarian', 'id': 'Indonesian', 'is': 'Icelandic', 'it': 'Italian', 'iw': 'Hebrew', 'ja': 'Japanese', 'jw': 'Javanese', 'km': 'Khmer', 'kn': 'Kannada', 'ko': 'Korean', 'la': 'Latin', 'lv': 'Latvian', 'ml': 'Malayalam', 'mr': 'Marathi', 'ms': 'Malay', 'my': 'Myanmar (Burmese)', 'ne': 'Nepali', 'nl': 'Dutch', 'no': 'Norwegian', 'pl': 'Polish', 'pt': 'Portuguese', 'ro': 'Romanian', 'ru': 'Russian', 'si': 'Sinhala', 'sk': 'Slovak', 'sq': 'Albanian', 'sr': 'Serbian', 'su': 'Sundanese', 'sv': 'Swedish', 'sw': 'Swahili', 'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tl': 'Filipino', 'tr': 
'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 'vi': 'Vietnamese', 'zh-CN': 'Chinese (Simplified)', 'zh-TW': 'Chinese (Mandarin/Taiwan)', 'zh': 'Chinese (Mandarin)'}

        print("DataStorage initialized")