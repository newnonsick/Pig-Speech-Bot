from pymongo import MongoClient

class MongoDBClient:

    def __init__(self, connection_string, db_name, collection_name):
        self.__client = MongoClient(connection_string)
        self.__db = self.client[db_name]
        self.__collection = self.db[collection_name]

    @property
    def client(self):
        return self.__client
    
    @property
    def db(self):
        return self.__db
    
    @property
    def collection(self):
        return self.__collection
    
    def insert_one(self, document):
        return self.collection.insert_one(document)
    
    def insert_many(self, documents):
        return self.collection.insert_many(documents)
    
    def find_one(self, query):
        return self.collection.find_one(query)
    
    def find(self, query):
        return self.collection.find(query)
    
    def find_all_guildID(self):
        return self.collection.distinct("guildID")
    
    def delete_one(self, query):
        return self.collection.delete_one(query)
    
    def delete_many(self, query):
        return self.collection.delete_many(query)
    
    def update_one(self, query, new_values):
        return self.collection.update_one(query, new_values)
    
