import os
import pandas as pd
import matplotlib.pyplot as plt

from utils import clearAxes, ensureExists, getDatasetPath, newAxes, readPS4DatasetFile

dt_path = getDatasetPath()

filename = 'PS4_GamesSales.csv'


def getColumnsData(data: pd.DataFrame):
    imagesPath= os.path.join(dt_path, filename[:-4])
    ensureExists(imagesPath)

    ax = newAxes()
    # Sales summary
    sales_cols_summary = data.agg({
        'North America': ['mean', 'median', 'max', 'min'],
        'Europe': ['mean', 'median', 'max', 'min'],
        'Japan': ['mean', 'median', 'max', 'min'],
        'Rest of World': ['mean', 'median', 'max', 'min'],
        'Global': ['mean', 'median', 'max', 'min']
    })
    pd.plotting.table(ax, sales_cols_summary, loc='center')
    plt.savefig(os.path.join(imagesPath, 'sales-columns-summary.png'), dpi=500)
    print(sales_cols_summary)
    print('---')

    # Sales mode
    sales_cols_mode = data.agg({
        'North America': ['mode'],
        'Europe': ['mode'],
        'Japan': ['mode'],
        'Rest of World': ['mode'],
        'Global': ['mode']
    })
    clearAxes(ax)
    pd.plotting.table(ax, sales_cols_mode, loc='center')
    plt.savefig(os.path.join(imagesPath, 'sales-columns-mode.png'), dpi=500)
    print(sales_cols_mode)
    print('---')

    # Year summary
    year_summary = data.agg({
        'Year': ['max', 'min', 'median']
    })
    clearAxes(ax)
    pd.plotting.table(ax, year_summary, loc='center', colWidths=[.2,.1])
    plt.savefig(os.path.join(imagesPath, 'year_summary.png'), dpi=500)
    print(year_summary)
    print('---')

    # Year value count
    data.loc[data['Year'].isna(), 'Year'] = 0
    year_value_count = data['Year'].value_counts()
    clearAxes(ax)
    pd.plotting.table(ax, year_value_count, loc='center', colWidths=[.2,.1])
    plt.savefig(os.path.join(imagesPath, 'year-values-count.png'), dpi=500)
    print(year_value_count)
    print('---')

    # Genre value count
    genre_value_count = data['Genre'].value_counts()
    clearAxes(ax)
    pd.plotting.table(ax, genre_value_count, loc='center', colWidths=[.2,.1])
    plt.savefig(os.path.join(imagesPath, 'genre-values-count.png'), dpi=500)
    print(genre_value_count)
    print('---')
    
data = readPS4DatasetFile()
print(data.info())
getColumnsData(data)