import os

import pandas as pd
import numpy as np
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

def get_p(pos, alpha):
    # pos = 'GoalKeeper'
    w1 = np.array(df_w1.loc[pos])
    w2 = np.array(df_w2.loc[pos])
    # alpha = 0.001
    new_w = w1

    df = pd.read_excel('classes/' + pos + '.xlsx')
    df = df.iloc[:, 3:9]
    df.loc[:, 'sum'] = 0
    new_sum = []
    for rowIdx, rowVal in df.iterrows():
        sum = 0
        for i in range(6):
            sum += df.iloc[rowIdx, i] * get_weight(new_w, df.columns[i])
        new_sum.append(sum)
    return new_sum

dir_list = os.listdir('classes')
for item in dir_list:
    df = pd.read_excel('classes/' + item)
    new_sum = get_p(item[:-5], 1)
    df['sum'] = new_sum
    df.to_excel('classes_fixed_data/' + item)
