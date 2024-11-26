import os
from matplotlib import pyplot as plt
from utils import readPS4DatasetFile, ensureExists, getDatasetPath, newAxes

dt_path = getDatasetPath()
filename = 'PS4_GamesSales.csv'
output_folder = os.path.join(dt_path, filename[:-4], 'sales-scatter')
ensureExists(output_folder)

gs = readPS4DatasetFile()
gs.info()

newAxes()
gs.plot.scatter(x='Global', y='North America')
plt.savefig(os.path.join(output_folder, 'global-na.svg'))

newAxes()
gs.plot.scatter(x='Global', y='Europe')
plt.savefig(os.path.join(output_folder, 'global-eu.svg'))

newAxes()
gs.plot.scatter(x='Global', y='Japan')
plt.savefig(os.path.join(output_folder, 'global-jp.svg'))

gs.plot.scatter(x='Global', y='Rest of World')
plt.savefig(os.path.join(output_folder, 'global-rw.svg'))

maxGlobal = max(gs['Global'])

newAxes()
gs.plot.scatter(x='Global', y='North America', ylim= (0, maxGlobal))
plt.savefig(os.path.join(output_folder, 'max-global-na.svg'))

newAxes()
gs.plot.scatter(x='Global', y='Europe', ylim= (0, maxGlobal))
plt.savefig(os.path.join(output_folder, 'max-global-eu.svg'))

newAxes()
gs.plot.scatter(x='Global', y='Japan', ylim= (0, maxGlobal))
plt.savefig(os.path.join(output_folder, 'max-global-jp.svg'))

gs.plot.scatter(x='Global', y='Rest of World', ylim= (0, maxGlobal))
plt.savefig(os.path.join(output_folder, 'max-global-rw.svg'))