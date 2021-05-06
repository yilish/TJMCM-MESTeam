import pandas as pd

df = pd.read_excel('concated_score_data.xlsx')
newDF = pd.DataFrame(index=[i for i in range(16)], columns=['total', 'num', 'mean'])

newDF['mean'] = df['sum'].groupby(df['team']).mean()
newDF['total'] = df['sum'].groupby(df['team']).sum()
newDF['num'] = df.groupby(df['team']).size()
newDF.to_excel('total_num_mean.xlsx')