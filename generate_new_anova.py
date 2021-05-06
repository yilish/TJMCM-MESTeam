import os

import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import (pairwise_tukeyhsd,
                                         MultiComparison)
from matplotlib import pyplot as plt
lb = ['30m', 'ArrowRun', 'LongJump', 'HighJump', 'PullUp', 'YoYo']
def get_weight(L, label):
    if label == '30m':
        return L[0]
    if label == 'ArrowRun':
        return L[1]
    if label == 'PullUp':
        return L[4]
    if label == 'LongJump':
        return L[2]
    if label ==  'YoYo':
        return L[5]
    if label == 'HighJump':
        return L[3]
    return 0

df_w1 = pd.read_excel('weight_by_ref.xlsx', index_col=0)
df_w2 = pd.read_excel('weight_by_ent.xlsx', index_col=0)

pos = 'GoalKeeper'
w1 = np.array(df_w1.loc[pos])
w2 = np.array(df_w2.loc[pos])
alpha = 1
new_w = alpha * w1 + (1 - alpha) * w2
# new_w = [0.13755793796823537, 0.2273422874110575, 0.08105802144653494, 0.09877870379587016, 0.22537519844739137, 0.22988785093091066]
df = pd.read_excel('classes/' + pos + '.xlsx')
df = df.iloc[:, 3:9]
df.loc[:, 'sum'] = 0
new_sum = []
for rowIdx, rowVal in df.iterrows():
    sum = 0
    for i in range(6):
        sum += df.iloc[rowIdx, i] * get_weight(new_w, df.columns[i])
    new_sum.append(sum)
data_list = pd.DataFrame(columns=['Position', 'Score'])
for item in new_sum:
    data_list = data_list.append(pd.DataFrame({'Position': ["GoalKeeper"], 'Score': [item]}))
dir_list = os.listdir('classes')

for item in dir_list:
    # df_list.append(pd.read_excel('classes/' + item))
    if item[:-5] == "GoalKeeper":
        continue
    print(item[:-5])
    df = pd.read_excel('classes/' + item )

    for idx, val in df.iterrows():

        data_list = data_list.append(pd.DataFrame({'Position': [item[:-5]], 'Score': [val['sum']]}))

model = ols('Score~Position', data=data_list).fit()
anova_table = anova_lm(model, type=2)
print(anova_table)
tukey = pairwise_tukeyhsd(endog=data_list['Score'],
                          groups=data_list['Position'],
                          alpha=0.05)
print(tukey)
mod = MultiComparison(data_list['Score'], data_list['Position'])
import matplotlib
# matplotlib.use('MacOSX')
thsd=mod.tukeyhsd()
thsd.plot_simultaneous()
plt.show()