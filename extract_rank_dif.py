import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel('concated_score_data_sorted.xlsx')
sum = list(df['sum'])
a = []
for i in range(len(sum)):
    flag = 0
    for j in range(i, len(sum)):
        if abs(sum[i] - sum[j]) >= 1.05:
            a.append(j)
            flag = 1
            break
    if flag == 0:
        a.append(-1)

b = []
for i in range(len(sum)):
    if a[i] == -1:
        continue
    b.append(a[i] - i)
print('均值\t\t\t方差')
print(np.mean(b), np.std(b))
print('最大值\t\t\t最小值')
print(np.max(b), np.min(b))
# plt.hist(sum, bins=10)
x = [i for i in range(len(b))]
plt.plot(x, b)
plt.show()