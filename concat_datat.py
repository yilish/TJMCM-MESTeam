import pandas as pd
result = pd.DataFrame()
for i in range(1, 16):
    tmpDf = pd.read_excel('deleted_data/' + str(i) + '.xlsx')
    result = pd.concat([result, tmpDf])
result.to_excel('concated_data.xlsx')