#!/usr/bin/env python3
"""Write a Python function that lists all documents in a collection:
"""


def list_all(mongo_collection):
    """Return list of all docs in collection"""
    return list(mongo_collection.find())
