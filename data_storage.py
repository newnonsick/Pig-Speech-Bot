import os
from typing import Dict, List

from models.guild import Guild
from models.mongodb_client import MongoDBClient


class DataStorage:
    guild_dict: Dict[int, Guild] = {}
    BOT_OWNER_ID: int = 360399310539718658
    presences: List[str] = []

    @classmethod
    def initialize(cls):
        """Initialize the DataStorage class with data from the database and static dictionaries."""
        cls._initialize_mongo_client()
        cls._load_guild_data()
        cls._initialize_said_dict()
        cls._initialize_lang_dict()

        print("DataStorage initialized")

    @classmethod
    def _initialize_mongo_client(cls):
        """Set up the MongoDB client using environment variables."""
        mongo_uri = os.getenv("MONGO_URI")
        mongo_db = os.getenv("MONGO_DB")
        mongo_collection = os.getenv("MONGO_COLLECTION")

        if not mongo_uri or not mongo_db or not mongo_collection:
            raise ValueError(
                "MongoDB environment variables (MONGO_URI, MONGO_DB, MONGO_COLLECTION) must be set."
            )

        cls.mongo_client: MongoDBClient = MongoDBClient(
            mongo_uri, mongo_db, mongo_collection
        )

    @classmethod
    def _load_guild_data(cls):
        """Load guild data from the MongoDB collection into the guild_dict."""
        try:
            guild_list = cls.mongo_client.find_all_guildID()
        except Exception as e:
            raise RuntimeError(f"Failed to fetch guild IDs from database: {e}")

        for guild_id in guild_list:
            guild_data = cls.mongo_client.find_one({"guildID": guild_id})
            if guild_data:
                cls.guild_dict[guild_id] = Guild(
                    guild_data["guildID"],
                    guild_data["channelID"],
                    guild_data["prefix"],
                    guild_data["language"],
                    guild_data["xSaidName"],
                )

    @classmethod
    def _initialize_said_dict(cls):
        """Initialize a dictionary mapping language codes to their 'said' equivalent."""
        cls.SAID_DICT: Dict[str, str] = {
            "af": "gesê",
            "ar": "قال",
            "bg": "казах",
            "bn": "বলেছেন",
            "bs": "rekao je",
            "ca": "dit",
            "cs": "řekl",
            "da": "sagde",
            "de": "sagte",
            "el": "είπε",
            "en": "said",
            "es": "dicho",
            "et": "ütles",
            "fi": "sanoi",
            "fr": "dit",
            "gu": "જણાવ્યું હતું",
            "hi": "कहा",
            "hr": "rekao je",
            "hu": "mondott",
            "id": "dikatakan",
            "is": "sagði",
            "it": "disse",
            "iw": "אמר",
            "ja": "言った",
            "jw": "ngandika",
            "km": "បាននិយាយថា",
            "kn": "ಎಂದರು",
            "ko": "말했다",
            "la": "dixit",
            "lv": "teica",
            "ml": "പറഞ്ഞു",
            "mr": "म्हणाला",
            "ms": "berkata",
            "my": "ဟုဆိုသည်။",
            "ne": "भन्नुभयो",
            "nl": "gezegd",
            "no": "sa",
            "pl": "powiedział",
            "pt": "disse",
            "ro": "a spus",
            "ru": "сказал",
            "si": "කිව්වා",
            "sk": "povedal",
            "sq": "tha",
            "sr": "рекао",
            "su": "ceuk",
            "sv": "sa",
            "sw": "sema",
            "ta": "கூறினார்",
            "te": "అన్నారు",
            "th": "บอกว่า",
            "tl": "sabi",
            "tr": "söz konusu",
            "uk": "сказав",
            "ur": "کہا",
            "vi": "nói",
            "zh-CN": "说",
            "zh-TW": "說",
            "zh": "說",
        }

    @classmethod
    def _initialize_lang_dict(cls):
        """Initialize a dictionary mapping language codes to their full names."""
        cls.LANG_DICT: Dict[str, str] = {
            "auto": "Auto",
            "af": "Afrikaans",
            "ar": "Arabic",
            "bg": "Bulgarian",
            "bn": "Bengali",
            "bs": "Bosnian",
            "ca": "Catalan",
            "cs": "Czech",
            "da": "Danish",
            "de": "German",
            "el": "Greek",
            "en": "English",
            "es": "Spanish",
            "et": "Estonian",
            "fi": "Finnish",
            "fr": "French",
            "gu": "Gujarati",
            "hi": "Hindi",
            "hr": "Croatian",
            "hu": "Hungarian",
            "id": "Indonesian",
            "is": "Icelandic",
            "it": "Italian",
            "iw": "Hebrew",
            "ja": "Japanese",
            "jw": "Javanese",
            "km": "Khmer",
            "kn": "Kannada",
            "ko": "Korean",
            "la": "Latin",
            "lv": "Latvian",
            "ml": "Malayalam",
            "mr": "Marathi",
            "ms": "Malay",
            "my": "Myanmar (Burmese)",
            "ne": "Nepali",
            "nl": "Dutch",
            "no": "Norwegian",
            "pl": "Polish",
            "pt": "Portuguese",
            "ro": "Romanian",
            "ru": "Russian",
            "si": "Sinhala",
            "sk": "Slovak",
            "sq": "Albanian",
            "sr": "Serbian",
            "su": "Sundanese",
            "sv": "Swedish",
            "sw": "Swahili",
            "ta": "Tamil",
            "te": "Telugu",
            "th": "Thai",
            "tl": "Filipino",
            "tr": "Turkish",
            "uk": "Ukrainian",
            "ur": "Urdu",
            "vi": "Vietnamese",
            "zh-CN": "Chinese (Simplified)",
            "zh-TW": "Chinese (Taiwan)",
            "zh": "Chinese (Mandarin)",
        }
