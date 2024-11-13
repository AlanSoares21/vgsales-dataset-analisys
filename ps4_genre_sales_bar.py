from matplotlib import pyplot as plt
import pandas as pd
from utils import getOutputPath, readInOutputPath

rg = readInOutputPath('region_genre.csv')

print(rg.info())
print(rg.describe())

output_image_inches=(25,25)

plt.rcParams.update({'legend.fontsize': 'xx-large'})

rg.plot.barh(
    x= 'Genre', 
    y=['Japan', 'Europe', 'North America', 'Rest of World'], 
    figsize=output_image_inches,
    fontsize=24,
    xlabel='Videogame units sales (in millions)')

plt.savefig(getOutputPath('regin-genre-bar.png'), dpi=50)