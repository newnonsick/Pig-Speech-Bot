import json
from models.guild import Guild
from models.mongodb_client import MongoDBClient
import os

class DataStorage:
    # Class variables to store data
    guildDict  = {}
    mongoClient = None
    saidDict = {}
    languages = list()

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
        cls.languages = [
            'auto',
            'af',
            'ar',
            'bg',
            'bn',
            'bs',
            'ca',
            'cs',
            'da',
            'de',
            'el',
            'en',
            'es',
            'et',
            'fi',
            'fr',
            'gu',
            'hi',
            'hr',
            'hu',
            'id',
            'is',
            'it',
            'iw',
            'ja',
            'jw',
            'km',
            'kn',
            'ko',
            'la',
            'lv',
            'ml',
            'mr',
            'ms',
            'my',
            'ne',
            'nl',
            'no',
            'pl',
            'pt',
            'ro',
            'ru',
            'si',
            'sk',
            'sq',
            'sr',
            'su',
            'sv',
            'sw',
            'ta',
            'te',
            'th',
            'tl',
            'tr',
            'uk',
            'ur',
            'vi',
            'zh-CN',
            'zh-TW',
            'zh',
        ]

        print("DataStorage initialized")