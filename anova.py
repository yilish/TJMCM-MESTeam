import pandas as pd
import os

import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import (pairwise_tukeyhsd,
                                         MultiComparison)
from matplotlib import pyplot as plt
import seaborn as sns
dir_list = os.listdir('classes')

df_list = []
data_list = pd.DataFrame(columns=['Position', 'Score'])
for item in dir_list:
    # df_list.append(pd.read_excel('classes/' + item))

    df = pd.read_excel('classes/' + item )
    # if item[:-5] == 'GoalKeeper':
    #     df = pd.read_excel('classes_fixed_data/' + item)
    for idx, val in df.iterrows():

        data_list = data_list.append(pd.DataFrame({'Position': [item[:-5]], 'Score': [val['sum']]}))
# import seaborn as sns
# for item in dir_list:
# rand_score = pd.read_csv('random_series.csv')
# rand_score = list(rand_score['Score'])
# for item in rand_score:
#     data_list = data_list.append(pd.DataFrame({'Position': ['OverAll'], 'Score': [item]}))
data_list.to_excel('data.xlsx')
import matplotlib.pyplot as plt
sns.boxplot(data = data_list)
plt.show()
# data_list.to_excel('data.xlsx')
#df_melt = data_list.melt()
#df_melt.columns = ['Position', 'Score']
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
model = ols('Score~Position', data=data_list).fit()
anova_table = anova_lm(model, type=2)
anova_table.to_excel('anova_result.xlsx')
tukey = pairwise_tukeyhsd(endog=data_list['Score'],
                          groups=data_list['Position'],
                          alpha=0.05)
# df_tukey = pd.DataFrame(tukey)
# print(df_tukey)
print(tukey)

mod = MultiComparison(data_list['Score'], data_list['Position'])
import matplotlib
# matplotlib.use('MacOSX')
thsd=mod.tukeyhsd()
thsd.plot_simultaneous()
plt.show()