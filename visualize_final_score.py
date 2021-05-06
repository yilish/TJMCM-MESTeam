import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.pyplot import Polygon
import scipy.stats
def normfun(x, mu, sigma):
    pdf = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    return pdf


df = pd.read_excel('concated_score_data.xlsx')
sum_list = df['sum']
n, bins, patches = plt.hist(sum_list, 30, density=True, color='#9999FF')
mu = np.mean(sum_list)
sigma = np.std(sum_list)
x = np.linspace(0, 10, 1000)
# print(mu, sigma)
pdf = scipy.stats.norm.pdf(x, mu, sigma)
# print(pdf)
import seaborn as sns
import matplotlib as mpl
# sns.set_palette("hls")
mpl.rc("figure", figsize=(6,4))
# sns.distplot(sum_list,bins=30, hist_kws={ "color": "b" },kde=False)
# plt.show()
#  ,kde_kws={"color":"seagreen", "lw":3 }
plt.plot(x, pdf, color='green', lw=3)
# plt.yticks([y for y in range(2,15,2)])
plt.title('Players\' Score Distribution')
plt.xlabel('Score')
plt.ylabel('Probability')
ix = np.linspace(0, 5.6, 560)
iy = pdf[:560]

# print(ixy)
plt.show()
# print(mu, sigma)