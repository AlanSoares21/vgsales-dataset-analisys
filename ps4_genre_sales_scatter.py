import os

from matplotlib import pyplot as plt
from utils import ensureExists, getDatasetPath, newAxes
import pandas as pd

dt_path = getDatasetPath()
filename = 'PS4_GamesSales.csv'
root_folder = os.path.join(dt_path, filename[:-4])
output_folder = os.path.join(root_folder, 'region_genre')
ensureExists(output_folder)

region_genre_path = os.path.join(root_folder, 'region_genre.csv')

rg_gn = pd.read_csv(region_genre_path, encoding='ISO-8859-1')
rg_gn.info()

newAxes()
rg_gn.plot.scatter(x='Global', y='North America')
plt.savefig(os.path.join(output_folder, 'global-na.svg'))

newAxes()
rg_gn.plot.scatter(x='Global', y='Europe')
plt.savefig(os.path.join(output_folder, 'global-eu.svg'))

newAxes()
rg_gn.plot.scatter(x='Global', y='Japan')
plt.savefig(os.path.join(output_folder, 'global-jp.svg'))

rg_gn.plot.scatter(x='Global', y='Rest of World')
plt.savefig(os.path.join(output_folder, 'global-rw.svg'))