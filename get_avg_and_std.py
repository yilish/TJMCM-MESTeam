import pandas as pd
import numpy as np

df = pd.read_excel('concated_data.xlsx')
for idx, val in df.iteritems():
    if type(val[0]) == str:
        continue
    print(str(idx) + '\t\tmean:\t' + str(np.mean(val)))
    # print(idx + '\t\tstd:\t' + str(np.std(val)))
    print('dic[\'' + idx + '\'] = ' + str(np.max(val) - np.min(val)))