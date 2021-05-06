import pandas as pd
import numpy as np
import math
import os
from numpy import array



# 定义熵值法函数
def cal_weight(x):
    '''熵值法计算变量的权重'''
    # 标准化
    x = x.apply(lambda x: ((x - np.min(x)) / (np.max(x) - np.min(x))))

    # 求k
    rows = x.index.size  # 行
    cols = x.columns.size  # 列
    k = 1.0 / math.log(rows)

    lnf = [[None] * cols for i in range(rows)]

    # 矩阵计算--
    # 信息熵
    # p=array(p)
    x = array(x)
    lnf = [[None] * cols for i in range(rows)]
    lnf = array(lnf)
    for i in range(0, rows):
        for j in range(0, cols):
            if x[i][j] == 0:
                lnfij = 0.0
            else:
                p = x[i][j] / x.sum(axis=0)[j]
                lnfij = math.log(p) * p * (-k)
            lnf[i][j] = lnfij
    lnf = pd.DataFrame(lnf)
    E = lnf

    # 计算冗余度
    d = 1 - E.sum(axis=0)
    # 计算各指标的权重
    w = [[None] * 1 for i in range(cols)]
    for j in range(0, cols):
        wj = d[j] / sum(d)
        w[j] = wj
        # 计算各样本的综合得分,用最原始的数据

    w = pd.DataFrame(w)
    return w


if __name__ == '__main__':
    dir = os.listdir('classes')
    ent_df = pd.DataFrame()
    for item in dir:
        df = pd.read_excel('classes/' + item)
        df = df.iloc[:, 3:9]
        print(item[:-5])
        # print(df.columns)
        w = cal_weight(df)
        w = w.T
        w.columns = [df.columns]
        print(w)
        #print(list(w.iloc[0]))
        ent_df = ent_df.append(w)
        # print('\n\n')
    ent_df.to_excel('weight_by_ent.xlsx')
    # 计算df各字段的权重
    # w = cal_weight(df)  # 调用cal_weight
    # w.index = df.columns
    # w.columns = ['weight']
    # print(w)
    # print('运行完成!')