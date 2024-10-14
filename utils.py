import os

from matplotlib import pyplot as plt

def getDatasetPath():
    path = os.getenv("DatasetPath")
    if path == None:
        return './data'
    return path

def clearAxes(ax):
    ax.clear()
    ax.axis('off')

def newAxes():
    ax = plt.subplot()
    clearAxes(ax)
    return ax

def ensureExists(path: str):
    if not os.path.exists(path):
        os.mkdir(path)
    