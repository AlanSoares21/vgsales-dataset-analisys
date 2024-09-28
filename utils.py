import os

def getPath():
    path = os.getenv("DatasetPath")
    if path == None:
        return './data'
    return path
