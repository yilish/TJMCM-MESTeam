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


def find_score_of_label(l, label, num):
    i = 0
    # print(l)
    num = float(num)
    if label == '30m' or label == 'ArrowRun':
        while i < len(l) and num > l[i]:
            i += 1

    else:
        while i < len(l) and num < l[i]:
            i += 1
    return 10 - i


df_weight = pd.read_excel('weight_by_ref_new.xlsx', index_col=0)
list_dir = os.listdir('classes_ori_data')
lb = ['30m', 'ArrowRun', 'LongJump', 'HighJump', 'PullUp', 'YoYo']
for item in list_dir:
    df = pd.read_excel('classes_ori_data/' + item)
    # weight_list
    score_list = pd.read_excel('standard/' + item)
    # print(list(score_list['30m']))
    sum = []
    df.loc[:, 'sum'] = 0
    # j = 0
    weight_list = df_weight.loc[item[:-5]]
    for rowIdx, rowVal in df.iterrows():
        tmp = 0
        for colIdx, colVal in rowVal.iteritems():
             if colIdx in lb:
                 # print(colIdx)
                 df.loc[rowIdx, colIdx] = find_score_of_label(
                     list(score_list[colIdx]), colIdx, df.loc[rowIdx, colIdx]
                 )
                 if df.loc[rowIdx, colIdx] == 0:
                     print(2)
                 tmp += get_weight(weight_list, colIdx) * df.loc[rowIdx, colIdx]
        sum.append(tmp)
    df['sum'] = sum
    # df.to_excel
    df.to_excel('classes_new_data/' + item)