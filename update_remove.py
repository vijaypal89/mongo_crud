#!/usr/bin/python

import sys
from mongo_connection import Connection

def update_one_doc(coll):

    #update only one matching document, even though more than one document can match query
    # upsert=True will insert document if no document matches to the filter.
    coll.update_one({"favorites.artist": "Picasso"}, 
                    {"$set": {"favorites.food": "pie", type: 3}}, upsert=True)

def update_many_doc(coll):

    #update all document matching to the query
    coll.update_many({"favorites.artist": "Picasso"}, 
                    {"$set": {"favorites.food": "Pisanello", type: 3}})

def replace_one_doc(coll):

    # replace only one document that match query
    coll.replace_one({"name":"xyz"},
                        {"name": "mee", "age": 25, "type": 1, "status": "A", "favorites": { "artist": "Matisse", "food": "mango" } })

def remove_doc(coll):

    # delete a single document or all document matching specified query
    coll.remove({"status": "P"})

def delete_one_doc(coll):

    # delete at most a single document mathing to specified query
    coll.delete_one({"status": "D"})

def delete_many_doc(coll):

    # delete all document matching the query
    coll.delete_many({"status": "A"})


def query_document(users):
    # Specify equality condition - 
    cur = users.find({"status":"P"})
    print "condotion: status = P"
    print print_cursor_obj(cur), "\n"

    # Specify condition using query operator - 
    cur = users.find({"status": {"$in": ["P", "D"]}})
    print "condition: [P, D] in status"
    print print_cursor_obj(cur), "\n"

    # Specify AND condition - 
    cur = users.find({"status": "A", "age": {"$lt": 30}})
    print "condition: status  A and age < 30"
    print print_cursor_obj(cur), "\n"

    # Specify OR condition - 
    cur = users.find({"$or": [{"status": "A"}, {"age": {"$lt": 30}}]})
    print "condition: status = A or age < 30"
    print print_cursor_obj(cur), "\n"

    # Specify AND as well as OR condition - 
    cur = users.find({"status": "A", "$or": [{"type": 1}, {"age": {"$lt": 30}}]})
    print "condition: status = A and (age < 30 or type = 1)"
    print print_cursor_obj(cur), "\n"

    # equality match within the embedded document - 
    cur = users.find({"favorites.artist": "Picasso"})
    print "condition: favorites = {artist: Picasso}"
    print print_cursor_obj(cur), "\n"

    # exact match on array - 
    cur = users.find({"badges": ["blue", "black"]})
    print "condition: badges = [blue , black]"
    print print_cursor_obj(cur), "\n"

    # match an array element - 
    cur = users.find({"badges": "black"})
    print "condition: badges = black"
    print print_cursor_obj(cur), "\n"

    # match a specific element of an array - 
    cur = users.find({"badges.0": "black"}, projection={"badges": True})
    print "condition: badges[0] = black"
    print print_cursor_obj(cur), "\n"

def print_cursor_obj(cur):
    res = [ x for x in cur ]
    return res

def main(args):
    conn = Connection("127.0.0.1", 27017, "u1")
    db = conn.get_db()

    # create and get new collection
    #users2 = conn.create_collection("users2")

    # getting user collection
    users = db['users']

    query_document(users)

if __name__ == '__main__':
    main(sys.argv)

