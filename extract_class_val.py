# utf-8#
import pandas as pd
sheet = pd.read_excel('source_data.xlsx', sheet_name=None)
l = ['守门员', '中场', '前卫', '后腰', '后卫', '边前卫', '前腰', '边后', '边前', '前锋']
pdList = []
for i in range((len(l))):
    pdList.append(pd.DataFrame())
num = 1
for j in sheet.values():
    df = j
    for i in range(len(df)):
        pos = df.iloc[i]['场上位置']
        for k in range(len(l)):
            if l[k] == pos:
                tmpDf = df.loc[i]
                tmpDf.loc['team'] = num
                pdList[k] = pdList[k].append(tmpDf, sort=False)
                #print(df.iloc[i])
                #print(pdList[k])
    num += 1
for i in range((len(l))):
    pdList[i].to_excel('class_data/' + l[i] + '.xlsx')
