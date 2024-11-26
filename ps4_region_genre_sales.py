import os

from matplotlib import pyplot as plt
from utils import ensureExists, getDatasetPath, newAxes
import pandas as pd

dt_path = getDatasetPath()
filename = 'PS4_GamesSales.csv'

games_sales= pd.read_csv(os.path.join(dt_path, filename), encoding='ISO-8859-1')

print(games_sales.info())

genres_count = games_sales['Genre'].value_counts()
genres = genres_count.keys()

gloabl_sales_per_genre = [games_sales[games_sales['Genre'] == genre]['Global'].sum() for genre in genres]
jp_sales_per_genre = [games_sales[games_sales['Genre'] == genre]['Japan'].sum() for genre in genres]
eu_sales_per_genre = [games_sales[games_sales['Genre'] == genre]['Europe'].sum() for genre in genres]
na_sales_per_genre = [games_sales[games_sales['Genre'] == genre]['North America'].sum() for genre in genres]
rw_sales_per_genre = [games_sales[games_sales['Genre'] == genre]['Rest of World'].sum() for genre in genres]

genre_sales = pd.DataFrame({
    'Genre': [x for x in genres],
    
    'Japan': jp_sales_per_genre,

    'Europe': eu_sales_per_genre,

    'North America': na_sales_per_genre,
    
    'Rest of World': rw_sales_per_genre,
    
    'Global': gloabl_sales_per_genre,

    'Count': [x for x in genres_count],

    'Global per Count': [x/y for x,y in zip(gloabl_sales_per_genre, genres_count)],
    'JP per Count': [x/y for x,y in zip(jp_sales_per_genre, genres_count)],
    'EU per Count': [x/y for x,y in zip(eu_sales_per_genre, genres_count)],
    'NA per Count': [x/y for x,y in zip(na_sales_per_genre, genres_count)],
    'RW per Count': [x/y for x,y in zip(rw_sales_per_genre, genres_count)],
    'JP/Global': [x/y for x,y in zip(jp_sales_per_genre, gloabl_sales_per_genre)],
    'EU/Global': [x/y for x,y in zip(eu_sales_per_genre, gloabl_sales_per_genre)],
    'NA/Global': [x/y for x,y in zip(na_sales_per_genre, gloabl_sales_per_genre)],
    'RW/Global': [x/y for x,y in zip(rw_sales_per_genre, gloabl_sales_per_genre)]
})

result = genre_sales.sort_values('Global', ascending=False)

print(result)

output_folder = os.path.join(dt_path, filename[:-4], 'region-genre')
ensureExists(output_folder)
output_file = os.path.join(output_folder, 'region_genre.csv')

result.to_csv(output_file, sep=',', index=False)

def plotTop10(col: str, meanPrefix: str):
    meanCol = '{} per Count'.format(meanPrefix)
    
    sorted = result.sort_values(col, ascending=False)[0:11]
    table = pd.DataFrame({
        'Genre': sorted['Genre'],
        col: sorted[col],
        meanCol: sorted[meanCol] 
    })

    pd.plotting.table(
        newAxes(), 
        table, 
        loc='center')
    plt.savefig(
        os.path.join(
            output_folder, 
            'top-10-by-{}.png'.format(col)
        ), 
        dpi=500)
    
    sorted = result.sort_values(meanCol, ascending=False)[0:11]
    table = pd.DataFrame({
        'Genre': sorted['Genre'],
        col: sorted[col],
        meanCol: sorted[meanCol] 
    })

    pd.plotting.table(
        newAxes(), 
        table,
        loc='center')
    plt.savefig(
        os.path.join(
            output_folder, 
            'top-10-by-{}-mean.png'.format(col)
        ), 
        dpi=500)

plotTop10('Global', 'Global')
plotTop10('North America', 'NA')
plotTop10('Japan', 'JP')
plotTop10('Europe', 'EU')
plotTop10('Rest of World', 'RW')