import os

from matplotlib import pyplot as plt
from utils import ensureExists, getDatasetPath, newAxes
import pandas as pd

dt_path = getDatasetPath()
filename = 'PS4_GamesSales.csv'
output_folder = os.path.join(dt_path, filename[:-4])
ensureExists(output_folder)

games_sales= pd.read_csv(os.path.join(dt_path, filename), encoding='ISO-8859-1')

print(games_sales.info())

gs = games_sales.sort_values('Global')
int_quant =  gs['Global'].quantile(0.75) - gs['Global'].quantile(0.25)

wo_outliers = gs[gs['Global'] < gs['Global'].quantile(0.75) + int_quant][gs['Global'] > gs['Global'].quantile(0.25) - int_quant]

wo_outliers.to_csv(os.path.join(output_folder, 'without-outliers-'+filename))
print(wo_outliers.describe())
print(wo_outliers.info())
