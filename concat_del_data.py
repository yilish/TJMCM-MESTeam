import pandas as pd
result = pd.DataFrame()
for i in range(1, 16):
    tmpDf = pd.read_excel('del_sum_score/' + str(i) + '.xlsx')
    tmpDf['team'] = i
    result = pd.concat([result, tmpDf])
result.to_excel('concated_score_data.xlsx')