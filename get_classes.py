import pandas as pd
sheet = pd.read_excel('source_data.xlsx', sheet_name=None)
s = dict()
for j in sheet.values():
    df = j
    for i in range(len(df)):
        if df.iloc[i]['场上位置'] in s.keys():
            s[df.iloc[i]['场上位置']] += 1
        else:
            s[df.iloc[i]['场上位置']] = 1
print(s)