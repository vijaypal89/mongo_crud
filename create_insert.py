#!/usr/bin/python

import sys
from mongo_connection import Connection
import pymongo

def insert_doc(coll):
    try:
        coll.insert_one({"_id":1, "fname": "AA01", "days": ["M", "T"]})
    except pymongo.errors.DuplicateKeyError as e:
        print >> sys.stderr, "Error: ", str(e)

def main():
    conn = Connection("127.0.0.1", 27017, "u2")
    db = conn.get_db()

    # create and get collection object
    #users = conn.create_collection("users")

    # get already existing collection
    users = db['users']

    #insert documents to collection
    insert_doc(users)

if __name__ == '__main__':
    main()
