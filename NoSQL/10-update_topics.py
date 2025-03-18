#!/usr/bin/env python3
"""Modify the topics of a school document based on its name"""


def update_topics(mongo_collection, name, topics):
    """Updates the topics field of all documents that match the given name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
