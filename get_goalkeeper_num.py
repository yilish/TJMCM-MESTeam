import pandas as pd

df = pd.read_excel('concated_score_data.xlsx')
df = df[df['sum'] >= 6]
print(df[df['Position'] == '守门员'].groupby(df['team']).size())