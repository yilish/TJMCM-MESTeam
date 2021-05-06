import pandas as pd
for i in range(1, 16):
    df = pd.read_excel('deleted_data/' + str(i) + '.xlsx')
    df = df[df['sum'] > 5.6]
    print(i, df.size())