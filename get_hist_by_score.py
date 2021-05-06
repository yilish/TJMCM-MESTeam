import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as clr
from matplotlib import rcParams
import numpy as np
import scipy.stats
import os
dir_list = os.listdir('classes')
color_list = [(0.95,0.6,0), (0, 0.57, 0.79), (0, 0.6, 0.33), (0.9, 0, 0.22)]
lim_list = [(3.8, 4.5), (6.5, 9), (2.2, 3), (40, 80), (1, 20), (400, 1100)]
test_list = ['30m', 'ArrowRun', 'LongJump', 'HighJump', 'PullUp', 'YoYo']
parameter = ['30m Score', 'Arrow Run Score', 'Long Jump Score', 'High Jump Score', 'Pull Up Score', 'YoYo Score']
# rcParams['font.family']='simhei'
i = 0
fig, ax = plt.subplots(nrows=6, ncols=4)
j = 0

for test in test_list:


    for item in dir_list:
        df = pd.read_excel('classes/' + item)
        run_data = df[test]
        print(item)

        # plt.title(item[:-5] + '\'s ' + test + ' Score Distribution')


        plt.subplot(6, 4, i + 1)
        plt.hist(run_data, 10, color=color_list[i % 4], density=True)
        plt.xlim((0, 10))
        plt.xticks(range(0, 11, 1))
        mu = np.mean(run_data)
        sigma = np.std(run_data)
        x = np.linspace(0, 10, 1000)
        print(mu, sigma)
        pdf = scipy.stats.norm.pdf(x, mu, sigma)
        plt.xlabel(parameter[j % 6])
        plt.ylabel('Probability')
        # plt.plot(x, pdf)

        # plt.savefig('fig/' + item[:-5] + '_' + test + 'score.jpg')
        # plt.close('fig/' + item[:-5] + '_' + test + 'score.jpg')
        # plt.show()
        #plt.xticks([])
        #plt.yticks([])

        i += 1
    # plt.show()
    # fig.show()
    # plt.xlim(7,9)
    j += 1

# plt.subplots_adjust(wspace = 1, hspace = 1)#调整子图间距
# fig = plt.gcf()
fig.set_size_inches(10.4, 10.4)


fig.tight_layout()#调整整体空白
plt.show()