import os

from matplotlib import pyplot as plt
import pandas as pd

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

def getOutputPath(filename):
    dt_path = getDatasetPath()
    datasetfilename = 'PS4_GamesSales.csv'
    output_folder = os.path.join(dt_path, datasetfilename[:-4])
    return os.path.join(output_folder, filename)

def readInOutputPath(filename):
    return pd.read_csv(getOutputPath(filename), encoding='ISO-8859-1')

def readPS4DatasetFile():
    dt_path = getDatasetPath()
    filename = 'PS4_GamesSales.csv'
    output_folder = getOutputPath()
    ensureExists(output_folder)
    return pd.read_csv(os.path.join(dt_path, filename), encoding='ISO-8859-1')
