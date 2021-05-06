import os
import pandas as pd
import numpy as np
result = pd.DataFrame()
dir_list = os.listdir('classes')
for item in dir_list:
    tmpDf = pd.read_excel('classes/' + item)
    result = pd.concat([result, tmpDf])
result.to_excel('concated_class_data.xlsx')
print(np.mean(result[result['Position'] == '守门员'].loc[:, 'sum']))
result = result.sort_values(by=['sum'], ascending=False)
result = result[:316]

result = result[result['Position'] == '守门员']
result.to_excel('filted.xlsx')
dic = dict()
for rowIdx, rowVal in result.iterrows():
    if rowVal['team'] in dic.keys():
        dic[rowVal['team']] += 1
    else:
        dic[rowVal['team']] = 1

print(dic)
print(len(dic.keys()))