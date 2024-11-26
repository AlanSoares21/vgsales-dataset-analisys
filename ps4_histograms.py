import math
import os

from matplotlib import pyplot as plt, rc
from utils import ensureExists, getDatasetPath
import pandas as pd

dt_path = getDatasetPath()
filename = 'PS4_GamesSales.csv'

games_sales= pd.read_csv(os.path.join(dt_path, filename), encoding='ISO-8859-1')

print(games_sales.info())

output_folder = os.path.join(dt_path, filename[:-4])

ensureExists(output_folder)

nbins = round(math.log(len(games_sales), 2) + 1)
max_global = max(games_sales['Global'])
bin_size = max_global/nbins

print('nbins: {} \nbin_size: {}'.format(nbins, bin_size))

plt.rcParams.update({'font.size': 250})

output_image_inches=(250,300)

games_sales.hist(
    column=['Global', 'Japan', 'North America', 'Europe', 'Rest of World'], 
    bins=nbins,
    figsize=output_image_inches)

plt.savefig(os.path.join(output_folder, 'histogram-sales-default-bin-size.png'), dpi=25)

games_sales.hist(
    column=['Global', 'Japan', 'North America', 'Europe', 'Rest of World'], 
    bins=[x*bin_size for x in range(nbins)],
    figsize=output_image_inches)
    
plt.savefig(os.path.join(output_folder, 'histogram-sales.png'), dpi=25)
