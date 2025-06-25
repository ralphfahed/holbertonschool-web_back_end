#!/usr/bin/env python3
"""
Module that contains a function to list all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection
    
    Args:
        mongo_collection: pymongo collection object
        
    Returns:
        List of documents in the collection, or empty list if no documents
    """
    documents = list(mongo_collection.find())
    return documents
