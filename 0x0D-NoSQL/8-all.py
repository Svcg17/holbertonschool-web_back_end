#!/usr/bin/env python3
"""Task 8"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """Lists all documents in a collection
    Args:
        mongo_collection: the pymongo collection object
    """
    return (mongo_collection.find() if mongo_collection.find().count() > 0
            else [])
