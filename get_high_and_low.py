import pandas as pd
import numpy as np

standard = pd.read_excel('standard.xlsx')
df = pd.read_excel('concated_data.xlsx')
def find_score_of_label(label, num):
    l = list(standard[label])
    i = 0
    # print(l)
    num = float(num)
    if label == '30m' or label == 'ArrowRun':
        while i < len(l) and num > l[i]  :
            i += 1

    else:
        while i < len(l) and num < l[i] :
            i += 1
    return 10 - i

for idx, val in df.iteritems():
    if type(val[0]) == str or idx[:3] == 'Unn' or idx == 'team':
        continue
    avg = np.mean(val)
    st = np.std(val)
    h_val = avg + 1.3 * st
    l_val = avg - 1.3 * st
    print('h_dict[\'' + idx + '\'] = ' + str(find_score_of_label(idx, h_val)))
    print('l_dict[\'' + idx + '\'] = ' + str(find_score_of_label(idx, l_val)))
    # print(idx + ':\thigh = '+ str(find_score_of_label(idx, h_val)))
    # print(idx + ':\tlow = ' + str(find_score_of_label(idx, l_val)))