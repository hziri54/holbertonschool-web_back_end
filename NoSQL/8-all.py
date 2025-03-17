#!/usr/bin/env python3
"""The ability to list every document in a collection."""


def list_all(mongo_collection):

    """Lists every document in a collection stored in MongoDB"""
    if mongo_collection is None:
        return []

    documents = list(mongo_collection.find())

    return documents
