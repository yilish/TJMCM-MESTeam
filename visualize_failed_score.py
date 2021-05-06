import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats
import numpy as np
df = pd.read_excel('failed_list.xlsx')
sum_list = df['sum']
n, bins, patches = plt.hist(sum_list, 20, density=True, color='#9999FF')
mu = np.mean(sum_list)
sigma = np.std(sum_list)
x = np.linspace(0, 6, 1000)
print(mu, sigma)
pdf = scipy.stats.norm.pdf(x, mu, sigma)
# plt.hist(df['sum'], 15, color=(0.9, 0, 0.22))
# plt.yticks([y for y in range(2,15,2)])
plt.plot(x, pdf, color='green')
plt.title('Failed Players\' Score Distribution')
plt.xlabel('Score')
plt.ylabel('Probability')
plt.show()
print(mu, sigma)