import os
import pandas as pd
import textdistance as td
import numpy as np    
from scipy.spatial.distance import cdist, squareform
from utils import *


df = pd.read_excel('FreeEnglishTextbooks.xlsx')

epubs = np.array([file for file in os.listdir('books/')]).reshape(-1,1)

df['Reduced Name'] = df.apply(lambda r: str(r['Copyright Year']) + ' ' + r['Book Title'], axis=1)

reduced = df['Reduced Name'].to_numpy().reshape((-1,1))

df['File Name'] = df.apply(lambda r: create_file_name(r, '.epub'), axis=1)

sim_dist = cdist(reduced, epubs, lambda x, y: td.jaro.normalized_distance(x[0], y[0]))

df_sim = pd.DataFrame(sim_dist, columns=epubs.flatten())
df_sim.index = reduced.flatten()

df_sim_2 = pd.DataFrame(df_sim.idxmin()).reset_index()
df_sim_2.columns = ['epub', 'Reduced Name']

df2 = df.merge(df_sim_2, on='Reduced Name')[['epub', 'File Name']]

df2.to_csv('renamed-epubs.csv', index=False, header=None)

for i, row in df2.iterrows():
    os.rename('books/' + row['epub'], 'books/' + row['File Name'])
