import os
import pandas as pd
import matplotlib.pyplot as plt

from utils import getDatasetPath

dt_path = getDatasetPath()

files = [
    {
        'name': 'PS4_GamesSales.csv',
        'agg': {
            'Year': ['max', 'min', 'median'],
            'North America': ['mean', 'median', 'max', 'min'],
            'Europe': ['mean', 'median', 'max', 'min'],
            'Japan': ['mean', 'median', 'max', 'min'],
            'Rest of World': ['mean', 'median', 'max', 'min'],
            'Global': ['mean', 'median', 'max', 'min']
        },
        'agg2': {
            'Year': ['mode'],
            'Genre': ['mode'],

            # useless
            'North America': ['mode'],
            'Europe': ['mode'],
            'Japan': ['mode'],
            'Rest of World': ['mode'],
            'Global': ['mode']
        },
        'count': ['Genre', 'Year'],
        'countOutput': 'png'
    },
    {
        'name': 'XboxOne_GameSales.csv',
        'agg': {
            'Year': ['max', 'min', 'median'],
            'North America': ['mean', 'median', 'max', 'min'],
            'Europe': ['mean', 'median', 'max', 'min'],
            'Japan': ['mean', 'median', 'max', 'min'],
            'Rest of World': ['mean', 'median', 'max', 'min'],
            'Global': ['mean', 'median', 'max', 'min']
        },
        'agg2': {
            'Year': ['mode'],
            'Genre': ['mode'],

            # useless
            'North America': ['mode'],
            'Europe': ['mode'],
            'Japan': ['mode'],
            'Rest of World': ['mode'],
            'Global': ['mode']
        },
        'count': ['Genre', 'Year'],
        'countOutput': 'png'
    },
    {
        'name': 'Video_Games_Sales_as_at_22_Dec_2016.csv',
        'agg': {
            'Year_of_Release': ['max', 'min', 'median'],
            'NA_Sales': ['mean', 'median', 'max', 'min'],
            'EU_Sales': ['mean', 'median', 'max', 'min'],
            'JP_Sales': ['mean', 'median', 'max', 'min'],
            'Other_Sales': ['mean', 'median', 'max', 'min'],
            'Global_Sales': ['mean', 'median', 'max', 'min'],
            'Critic_Score': ['mean', 'median', 'max', 'min'],
            'Critic_Count': ['mean', 'median', 'max', 'min'],
            'User_Score': ['mean', 'median', 'max', 'min'],
            'User_Count': ['mean', 'median', 'max', 'min']
        },
        'agg2': {
            'Platform': ['mode'],
            'Year_of_Release': ['mode'],
            'Genre': ['mode'],
            'Publisher': ['mode'],
            'Developer': ['mode'],
            'Rating': ['mode'],
            'Critic_Score': ['mode'],
            'Critic_Count': ['mode'],
            'User_Score': ['mode'],
            'User_Count': ['mode']
        },
        'count': ['Platform', 'Year_of_Release', 'Genre', 'Publisher', 'Developer', 'Rating'],
        'countOutput': 'csv'
    }
]

def clearAxes(ax):
    ax.clear()
    ax.axis('off')

def newAxes():
    ax = plt.subplot()
    clearAxes(ax)
    return ax

def getColumnsData(file, data: pd.DataFrame):
    imagesPath= os.path.join(dt_path, file['name'][:-4])
    if not os.path.exists(imagesPath):
        os.mkdir(imagesPath)
    print('statisticts for ' + file['name'])
    print('output in: ' + imagesPath)
    print('---')
    agg1_result = data.agg(file['agg'])
    ax = newAxes()
    pd.plotting.table(ax, agg1_result, loc='center')
    plt.savefig(os.path.join(imagesPath, 'agg1.png'), dpi=500)
    print(agg1_result)
    print('---')
    agg2_result = data.agg(file['agg2'])
    clearAxes(ax)
    pd.plotting.table(ax, agg2_result, loc='center')
    plt.savefig(os.path.join(imagesPath, 'agg2.png'), dpi=500)
    print(agg2_result)
    for col_name in file['count']:
        print('---')
        count_result = data[col_name].value_counts()
        if file['countOutput'] == 'png':
            clearAxes(ax)
            pd.plotting.table(ax, count_result, loc='center', colWidths=[.2,.1])
            plt.savefig(os.path.join(imagesPath, col_name + '-values-count.png'), dpi=500)
        elif file['countOutput'] == 'csv':
            count_result.to_csv(os.path.join(imagesPath, col_name + '-values-count.csv'), sep=',')
        print(count_result)
    


print('dataset path: ' + dt_path)
for file in files:
    filepath = os.path.join(dt_path, file['name'])
    print('reading file: ' + filepath)
    data = pd.read_csv(filepath, encoding= 'ISO-8859-1')

    print(data.info())
    
    getColumnsData(file, data)