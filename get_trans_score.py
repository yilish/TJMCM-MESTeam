import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as clr
import os
dir_list = os.listdir('classes')
test_list = ['30m', 'ArrowRun', 'LongJump', 'HighJump', 'PullUp', 'YoYo']
parameter = ['30m(s)', 'Arrow Run(s)', 'Long Jump(m)', 'High Jump(m)', 'Pull Up times', 'YoYo(m)']

sigma_weight = [1.28, 0.84, 0.525, 0.255, -0.255, -0.525, -0.84, -1.04, -1.28, -1.645]
sigma_weight = sigma_weight[::-1]
for item in dir_list:
    df_std = pd.DataFrame(columns=test_list, index=range(10, 0, -1))
    for test in test_list:
        df = pd.read_excel('classes_ori_data/' + item)
        run_data = df[test]
        mean = run_data.mean()
        std = run_data.std()
        if test == '30m' or test == 'ArrowRun':
            for i in range(10, 0, -1):
                df_std.loc[i, test] = mean - sigma_weight[i - 1] * std
        else:
            for i in range(10):
                df_std.loc[i + 1, test] = mean + sigma_weight[i] * std

    # df_std = df_std.iloc[::-1]
    formater = "{0:.02f}".format
    df_std = df_std.applymap(formater)
    # df_std.round(2)
    print(df_std)
    df_std.to_excel('standard/' + item)