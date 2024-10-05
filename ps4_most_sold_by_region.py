import os
from utils import getDatasetPath
import pandas as pd

dt_path = getDatasetPath()
filename = 'PS4_GamesSales.csv'

games_sales= pd.read_csv(os.path.join(dt_path, filename), encoding='ISO-8859-1')

print(games_sales.info())

most_sold = {
    'EU': games_sales[games_sales['Europe'] > games_sales['Japan']][games_sales['Europe'] > games_sales['North America']][games_sales['Europe'] > games_sales['Rest of World']],
    'JP': games_sales[games_sales['Japan'] > games_sales['Europe']][games_sales['Japan'] > games_sales['North America']][games_sales['Japan'] > games_sales['Rest of World']],
    'NA': games_sales[games_sales['North America'] > games_sales['Europe']][games_sales['North America'] > games_sales['Japan']][games_sales['North America'] > games_sales['Rest of World']],
    'RW': games_sales[games_sales['Rest of World'] > games_sales['Europe']][games_sales['Rest of World'] > games_sales['Japan']][games_sales['Rest of World'] > games_sales['North America']]
}

output_folder = os.path.join(dt_path, filename[:-4], 'most_sold')

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

for key in most_sold:
    most_sold[key].to_csv(os.path.join(output_folder, key+ '.csv'), sep=',')
    