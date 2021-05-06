import pandas as pd
for i in range(1, 16):
    df = pd.read_excel('del_sum_score/' + str(i) + '.xlsx')
    df = df[df['sum'] >= 5.6]
    print(i, len(df))
    df.to_excel('attend_list/' + str(i) + '.xlsx')