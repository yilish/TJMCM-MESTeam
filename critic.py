# coding: gbk
# 使用CRITIC客观赋权法获得真实误差序列与组合预测值
# 所有的评价指标均为损益性指标，越小越好
# 参考链接：https://blog.csdn.net/stephen_curry300/article/details/106989729
# 参考论文：两种客观赋权法及其在确定组合预测权重中的应用

# 确定各单一预测模型权重步骤如下：
# 1）对原始决策矩阵X进行标准化处理，得到标准化矩阵R
# 2）由标准化矩阵求出各评价指标的概率
# 3）按客观赋权方法求各评定指标的权重（这里有CRITIC法和变异系数法两种）
# 4）最后，根据  各评价指标概率  和  各评价指标的权重  计算各预测方法的权重，权重之和为1.0

import numpy as np
import pandas as pd
import os
################### 计算变异系数权重 ###########################
def CvWeight(data,collist):
    '''
    data: dataframe类型数据
    collist：需要计算权重的属性列表
    '''
    # print('计算变异系数法....')
    statistic = data[collist].describe()                     # 描述统计值
    cv = statistic.loc['std'] / abs(statistic.loc['mean'])   # 计算CV值
    cv_sum = cv.sum()                                        # cv总和
    # print('变异系数总和：' + str(cv_sum))
    cv_weight = cv / cv_sum                                  # 计算权重
    # print('%s 的权重是：%s ；' % (collist,[cv_weight[col] for col in collist]))
    # pass
    return cv_weight
# pass
if __name__ == '__main__':
    # 四种预测模型的误差指标为
    dir = os.listdir('classes')
    for item in dir:
        df = pd.read_excel('classes/' + item)
        df = df.iloc[:, 3:9]
        print(item[:-5])
        # df = np.array(df)
        w = CvWeight(df, df.columns)
        w = pd.DataFrame(w)
        print(w)
        # critic(df)
        # print(df.columns)
        # w = cal_weight(df)
        # w = w.T
        # w.columns = [df.columns]
        # print(w)
        print('\n\n')

    # X = np.array(
    #     [[0.0197, 199.4, 0.0083,  3.7740,  0.0244],
    #      [0.0545, 1603.6, 0.0619, 10.7023, 0.0665],
    #      [0.0263, 308,    0.0135, 4.6903,  0.0310],
    #      [0.0184, 158.5,  0.0062,  3.3642,  0.0211]]
    # )
    # CRITIC法求各个评价指标的权重


