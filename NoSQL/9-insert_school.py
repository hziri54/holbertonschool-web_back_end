#!/usr/bin/env python3
"""Kwargs-based function to add a new document to a MongoDB collection"""


def insert_school(mongo_collection, **kwargs):
    """Add a latest document in a collection MongoDB"""
    if mongo_collection is None:
        return []

    documents = mongo_collection.insert_one(kwargs)

    return documents.inserted_id
