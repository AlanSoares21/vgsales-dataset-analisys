import os

def getDatasetPath():
    path = os.getenv("DatasetPath")
    if path == None:
        return './data'
    return path
