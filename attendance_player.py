import pandas as pd
import numpy as np
L = []
for i in range(1, 16):
    df = pd.read_excel('del_sum_score/' + str(i) + '.xlsx')
    newDf = df[df['sum'] >= 6]
    L.append( np.mean(df['sum']))
    newDf.to_excel('1_passed_list/' + str(i) + '.xlsx')

print(L)