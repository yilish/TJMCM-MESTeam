import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as clr
from matplotlib import rcParams

import os
dir_list = os.listdir('classes')
color_list = [(0.95,0.6,0), (0, 0.57, 0.79), (0, 0.6, 0.33), (0.9, 0, 0.22)]
lim_list = [(3.8, 4.5), (6.5, 9), (2.2, 3), (40, 80), (1, 20), (400, 1100)]
test_list = ['30m', 'ArrowRun', 'LongJump', 'HighJump', 'PullUp', 'YoYo']
parameter = ['30m(s)', 'Arrow Run(s)', 'Long Jump(m)', 'High Jump(m)', 'Pull Up times', 'YoYo(m)']
rcParams['font.family']='simhei'
i = 0
fig, ax = plt.subplots(nrows=6, ncols=4)
j = 0

for test in test_list:


    for item in dir_list:
        df = pd.read_excel('classes_new_data/' + item)
        run_data = df[test]


        # plt.title(item[:-5] + '\'s ' + test + ' Score Distribution')


        plt.subplot(6, 4, i + 1)
        plt.hist(run_data, 10, color=color_list[i % 4])
        # plt.xlim(lim_list[j % 6])
        plt.xlabel(parameter[j % 6])
        plt.ylabel('frequency')


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