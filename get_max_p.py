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
rand_score = pd.read_csv('random_series.csv')
rand_score = list(rand_score['Score'])
def get_p(pos, alpha):
    # pos = 'GoalKeeper'
    w1 = np.array(df_w1.loc[pos])
    w2 = np.array(df_w2.loc[pos])
    # alpha = 0.001
    new_w = alpha * w1 + (1 - alpha) * w2

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
        data_list = data_list.append(pd.DataFrame({'Position': [pos], 'Score': [item]}))
    for item in rand_score:
        data_list = data_list.append(pd.DataFrame({'Position': ['OverAll'], 'Score': [item]}))
    model = ols('Score~Position', data=data_list).fit()
    anova_table = anova_lm(model, type=2)
    return anova_table.loc['Position', 'PR(>F)']

result = []
epoch = 100
for a in range(epoch, 0 , -1):
    alpha = a / epoch
    result.append(get_p('Guard', alpha))
    print (result[-1])

result = np.array(result)
print(result)