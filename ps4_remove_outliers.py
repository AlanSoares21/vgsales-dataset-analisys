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
outliers = gs[gs['Global'] >= gs['Global'].quantile(0.75) + int_quant]
outliers.add(gs[gs['Global'] <= gs['Global'].quantile(0.25) - int_quant])
outliers = outliers.sort_values('Global', ascending=False)

wo_outliers.to_csv(os.path.join(output_folder, 'without-outliers-'+filename), index=False)
outliers.to_csv(os.path.join(output_folder, 'outliers-'+filename), index=False)
print(wo_outliers.describe())
print(wo_outliers.info())
print('---')
print(outliers.describe())
print(outliers.info())

top_10 = outliers[0:11]
print(top_10)

pd.plotting.table(newAxes(), top_10, loc='center')
plt.savefig(os.path.join(output_folder, 'top-10.svg'), dpi=250)
top_10.to_csv(os.path.join(output_folder, 'top_10-'+filename), index=False)