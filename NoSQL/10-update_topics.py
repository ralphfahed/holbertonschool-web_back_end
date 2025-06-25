#!/usr/bin/env python3
""" Module 10-update_topics """

def update_topics(mongo_collection, name, topics):
    """
    Update the topics list of the document(s) with the given school name.

    Args:
        mongo_collection: pymongo collection object
        name (str): name of the school to update
        topics (list of str): list of topics to set

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
