import pandas as pd
import numpy as np

dic = dict()
h_dict = dict()
l_dict = dict()
dic['30m'] = 1.4449924824170637
dic['ArrowRun'] = 2.595618243919013
dic['LongJump'] = 1.7851701352487557
dic['HighJump'] = 2.098949423258075
dic['PullUp'] = 3.1878110313078336
dic['YoYo'] = 2.3026788067947632
h_dict['30m'] = 6
l_dict['30m'] = 10
h_dict['ArrowRun'] = 3
l_dict['ArrowRun'] = 10
h_dict['LongJump'] = 9
l_dict['LongJump'] = 4
h_dict['HighJump'] = 10
l_dict['HighJump'] = 4
h_dict['PullUp'] = 10
l_dict['PullUp'] = 1
h_dict['YoYo'] = 10
l_dict['YoYo'] = 0
df = pd.read_excel('null_vals.xlsx')
df.loc[:, 'lackSum'] = 0
def get_weight(label):
    if label == '30m':
        return 0.15
    if label == 'ArrowRun':
        return 0.15
    if label == 'PullUp':
        return 0.1
    if label == 'LongJump':
        return 0.1
    if label ==  'YoYo':
        return 0.4
    if label == 'HighJump':
        return 0.1
    else:
        return 0

i = 0
for rowIdx, rowVal in df.iterrows():
    lackSum = 0
    for colIdx, colVal in rowVal.iteritems():
        if colIdx == 'Unnamed: 0' or colIdx == 'lackSum' or colIdx == 'Position':
            continue
        if colVal == 0 or pd.isna(colVal):
            lackSum += get_weight(colIdx) * abs(h_dict[colIdx] - l_dict[colIdx]) #
    df.loc[i, 'lackSum'] = lackSum
    i += 1

df.to_excel('sigma_result_1.xlsx')