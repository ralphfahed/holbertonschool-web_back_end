#!/usr/bin/env python3
""" Module 11-schools_by_topic """

def schools_by_topic(mongo_collection, topic):
    """
    Return a list of schools where the topics list contains the given topic.

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search for

    Returns:
        List of matching school documents.
    """
    return list(mongo_collection.find({"topics": topic}))
