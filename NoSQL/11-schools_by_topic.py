#!/usr/bin/env python3
"""Retrieve schools by a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Finds and returns a list of schools that contain the given topic"""
    return list(mongo_collection.find({"topics": topic}))
