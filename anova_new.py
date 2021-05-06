import pandas as pd
import os

import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import (pairwise_tukeyhsd,
                                         MultiComparison)
from matplotlib import pyplot as plt
import seaborn as sns
dir_list = os.listdir('classes')
df_final = pd.DataFrame(columns=[d[:-5] for d in dir_list])
data_list = pd.DataFrame(columns=['Position', 'Score'])
for item in dir_list:
    # df_list.append(pd.read_excel('classes/' + item))

    # df = pd.read_excel('classes/' + item )
    df = pd.read_excel('classes/' + item)
    df_final[item[:-5]] = df['sum']

# import seaborn as sns
# for item in dir_list:
# rand_score = pd.read_csv('random_series.csv')
# rand_score = list(rand_score['Score'])
# for item in rand_score:
#     data_list = data_list.append(pd.DataFrame({'Position': ['OverAll'], 'Score': [item]}))
data_list.to_excel('data.xlsx')
import matplotlib.pyplot as plt
sns.boxplot(data = df_final, palette=[(0.95,0.6,0), (0, 0.57, 0.79), (0, 0.6, 0.33), (0.9, 0, 0.22)])
sns.swarmplot(data=df_final, palette=sns.light_palette("blue"))
fig = plt.gcf()
fig.set_size_inches(10.4, 10.4)
font1 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 23,
}

plt.tick_params(labelsize=23)

plt.show()
# data_list.to_excel('data.xlsx')
#df_melt = data_list.melt()
#df_melt.columns = ['Position', 'Score']
