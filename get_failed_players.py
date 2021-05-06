import pandas as pd
df = pd.read_excel('concated_score_data.xlsx')
df[df['sum'] < 6].to_excel('failed_list.xlsx')