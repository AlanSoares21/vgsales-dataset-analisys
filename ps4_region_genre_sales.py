import os
from utils import getDatasetPath
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
    'RW per Count': [x/y for x,y in zip(rw_sales_per_genre, genres_count)]
})

result = genre_sales.sort_values('Global', ascending=False)

print(result)

output_file = os.path.join(dt_path, filename[:-4], 'region_genre.csv')

result.to_csv(output_file, sep=',')