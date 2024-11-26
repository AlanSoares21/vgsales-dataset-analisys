from matplotlib import pyplot as plt
import pandas as pd
from utils import getOutputPath, readInOutputPath

rg = readInOutputPath('region-genre/region_genre.csv')

print(rg.info())
print(rg.describe())

output_image_inches=(25,35)

plt.rcParams.update({'legend.fontsize': 'xx-large'})

rg.plot.barh(
    subplots= True,
    x= 'Genre', 
    y=['Japan', 'Europe', 'North America', 'Rest of World'], 
    figsize=output_image_inches,
    fontsize=24,
    xlabel='Videogame units sales (in millions)')

plt.savefig(getOutputPath('region-genre/region-genre-bar.png'), dpi=50)

rg.plot.barh(
    x= 'Genre', 
    y=['Japan', 'Europe', 'North America', 'Rest of World'], 
    figsize=output_image_inches,
    fontsize=24,
    stacked=True,
    xlabel='Videogame units sales (in millions)')

plt.savefig(getOutputPath('region-genre/stacked-region-genre-bar.png'), dpi=50)

rg.plot.bar(
    x= 'Genre', 
    y=['JP/Global', 'EU/Global', 'NA/Global', 'RW/Global'], 
    figsize=output_image_inches,
    fontsize=24,
    stacked=True,
    xlabel='Percentage global sales')

plt.savefig(getOutputPath('region-genre/stacked-region-genre-bar.png'), dpi=50)