
import os
import pandas as pd
from utils import ensureExists, getDatasetPath, readPS4DatasetFile


data = readPS4DatasetFile()

output_folder = os.path.join(getDatasetPath(), 'PS4_GamesSales', 'empty-year-filter')
ensureExists(output_folder)

def getNanValues(gs: pd.DataFrame):
    return gs[gs['Year'].isna()]

def getNonNanValues(gs: pd.DataFrame):
    return gs[gs['Year'] != gs['Year'].isna()]

nan_year = getNanValues(data)
print(nan_year)
nan_year.to_csv(os.path.join(output_folder, 'empty-years.csv'))

print('---')

nonnan_year = getNonNanValues(data)
print(nonnan_year)
nonnan_year.to_csv(os.path.join(output_folder, 'non-empty-years.csv'))