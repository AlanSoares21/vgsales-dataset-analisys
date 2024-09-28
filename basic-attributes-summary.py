import os
import pandas as pd

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
        'count': ['Genre', 'Year']
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
        'count': ['Genre', 'Year']
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
        'count': ['Platform', 'Year_of_Release', 'Genre', 'Publisher', 'Developer', 'Rating']
    }
]

def getColumnsData(file, data: pd.DataFrame):
    print('statisticts for ' + file['name'])
    print('---')
    print(data.agg(file['agg']))
    print('---')
    print(data.agg(file['agg2']))
    for col_name in file['count']:
        print('---')
        print(data[col_name].value_counts())
    


print('dataset path: ' + dt_path)
for file in files:
    filepath = os.path.join(dt_path, file['name'])
    print('reading file: ' + filepath)
    data = pd.read_csv(filepath, encoding= 'ISO-8859-1')

    print(data.info())
    
    getColumnsData(file, data)