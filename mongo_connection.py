#!/usr/bin/python

import pymongo

class Connection():
    def __init__(self, host="127.0.0.1", port=27017, db=None):
        self.conn = pymongo.MongoClient(host=host, port=port)
        self.db = self.conn[db]
    
    def get_db(self):
        return self.db

    def create_collection(self, collection_name):
        return pymongo.collection.Collection(self.db, collection_name, create=True)
