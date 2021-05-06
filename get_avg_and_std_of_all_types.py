import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as clr
import os
import numpy as np
dir_list = os.listdir('classes')
color_list = [(0.95,0.6,0), (0, 0.57, 0.79), (0, 0.6, 0.33), (0.9, 0, 0.22)]
test_list = ['30m', 'ArrowRun', 'LongJump', 'HighJump', 'PullUp', 'YoYo']
i = 0
fig, ax = plt.subplots(nrows=6, ncols=4)

for test in test_list:


    for item in dir_list:
        df = pd.read_excel('classes_ori_data/' + item)
        run_data = df[test]

        print(test + ' ' + item[:5], end=" ")
        print(np.mean(run_data), np.std(run_data))