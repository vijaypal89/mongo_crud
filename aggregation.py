#!/usr/bin/python

import sys
from mongo_connection import Connection
import bson

def print_doc(cur):
    res = [ x for x in cur ]
    return res

def aggregate(coll):
    cur = coll.aggregate([
                {"$match":{"status":"A"}}, # matching document
                {"$group":{"_id":"$cust_id", "total":{"$sum":"$amount"}}} # transforming matched document
            ])
    print print_doc(cur), "\n"

def mapreduce(coll):

    coll.map_reduce(
                    "function() { emit(this.cust_id, this.amount) }", # map
                    "function(key, value) { return  Array.sum( value ) }", # reduce
                    bson.son.SON([('replace', 'total_orders')]), # output putting into collection
                    query={"status":"A"} # document filter before map
                    #limit = 10 # maximum number of document given to map
            )

def main():
    conn = Connection("127.0.0.1", 27017, "u1")
    db = conn.get_db()

    #get collection
    orders = db['orders']

    # Aggregation pipeline
    aggregate(orders)
    
    # mapreduce
    mapreduce(orders)


if __name__ == '__main__':
    main()

