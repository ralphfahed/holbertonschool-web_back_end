#!/usr/bin/env python3
""" Module 9-insert_school """

def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into mongo_collection with fields from kwargs.
    
    Args:
        mongo_collection (pymongo.collection.Collection): The collection instance.
        **kwargs: Key-value pairs to insert as document fields.

    Returns:
        The _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
