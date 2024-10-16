import os

from matplotlib import pyplot as plt
from utils import ensureExists, getDatasetPath, newAxes
import pandas as pd

dt_path = getDatasetPath()
filename = 'PS4_GamesSales.csv'
root_folder = os.path.join(dt_path, filename[:-4])
output_folder = os.path.join(root_folder, 'region-genre-scatter')
ensureExists(output_folder)

region_genre_file_path = os.path.join(root_folder, 'region-genre', 'region_genre.csv')

rg_gn = pd.read_csv(region_genre_file_path, encoding='ISO-8859-1')
rg_gn.info()




def plotScatter(colX: str, colY: str, output_path: str, limXY: tuple = None):
    if limXY is not None:
        newAxes()
        rg_gn.plot.scatter(x=colX, y=colY, ylim= limXY, xlim= limXY)
        plt.savefig(os.path.join(output_path, '{}-{}-limited.svg'.format(colX, colY)))    
    else:
        newAxes()
        rg_gn.plot.scatter(x=colX, y=colY)
        plt.savefig(os.path.join(output_path, '{}-{}-not-limited.svg'.format(colX, colY)))

lim = (0, max(rg_gn['Global']) + rg_gn['Global'].mean()/2)
plotScatter('Global', 'North America', output_folder, lim)
plotScatter('Global', 'North America', output_folder)

plotScatter('Global', 'Europe', output_folder, lim)
plotScatter('Global', 'Europe', output_folder)

plotScatter('Global', 'Japan', output_folder, lim)
plotScatter('Global', 'Japan', output_folder)

plotScatter('Global', 'Rest of World', output_folder, lim)
plotScatter('Global', 'Rest of World', output_folder)


output_folder = os.path.join(output_folder, 'means')
ensureExists(output_folder)
lim2 = (0, max(rg_gn['Global per Count']) + rg_gn['Global per Count'].mean() / 2)

plotScatter('Global per Count', 'NA per Count', output_folder, lim2)
plotScatter('Global per Count', 'NA per Count', output_folder)

plotScatter('Global per Count', 'EU per Count', output_folder, lim2)
plotScatter('Global per Count', 'EU per Count', output_folder)

plotScatter('Global per Count', 'JP per Count', output_folder, lim2)
plotScatter('Global per Count', 'JP per Count', output_folder)

plotScatter('Global per Count', 'RW per Count', output_folder, lim2)
plotScatter('Global per Count', 'RW per Count', output_folder)