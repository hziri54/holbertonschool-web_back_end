#!/usr/bin/env python3
from pymongo import MongoClient

def list_all(mongo_collection):
    """
    Function to retrieve all documents from a MongoDB collection.
    
    :param mongo_collection: The pymongo collection object
    :return: A list of all documents in the collection or an empty list if none exist
    """
    if not mongo_collection:
        return []
    
    return list(mongo_collection.find())
