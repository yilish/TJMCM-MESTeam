import pandas as pd
import numpy as np

df_w1 = pd.read_excel('weight_by_ref.xlsx', index_col=0)
df_w2 = pd.read_excel('weight_by_ent.xlsx', index_col=0)
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

pos = 'GoalKeeper'
w1 = np.array(df_w1.loc[pos])
w2 = np.array(df_w2.loc[pos])
df1= pd.read_excel('classes/' + pos + '.xlsx')
df = df1.iloc[:, 3:9]
df.loc[:, 'sum'] = 0
new_sum = []
for rowIdx, rowVal in df.iterrows():
    sum = 0
    for i in range(6):
        sum += df.iloc[rowIdx, i] * get_weight(w1, df.columns[i])
    new_sum.append(sum)
# df = pd.read_excel('classes/' + pos + '.xlsx')
df1.loc[:, 'sum'] = new_sum
df1.to_excel('classes/GoalKeeper.xlsx')