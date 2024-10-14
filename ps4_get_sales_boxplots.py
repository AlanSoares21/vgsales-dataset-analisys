import os

from matplotlib import pyplot as plt
from utils import clearAxes, ensureExists, getDatasetPath, newAxes
import pandas as pd

dt_path = getDatasetPath()
filename = 'PS4_GamesSales.csv'
output_folder = os.path.join(dt_path, filename[:-4])
ensureExists(output_folder)

games_sales= pd.read_csv(os.path.join(dt_path, filename), encoding='ISO-8859-1')

print(games_sales.info())



games_sales.boxplot(
    column=['Global','North America','Europe','Japan','Rest of World'], 
    showfliers=True, 
    showmeans=True, 
    grid=True)
plt.savefig(os.path.join(output_folder, 'boxplots-sales.png'), dpi=500)
