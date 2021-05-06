import pandas as pd
df = pd.read_excel('concated_score_data.xlsx')
res = []
for rowIdx, rowVal in df.iterrows():
    res.append(abs( rowVal['HighJump'] - rowVal['LongJump']))
print(max(res))