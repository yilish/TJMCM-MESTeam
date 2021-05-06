import pandas as pd
import numpy as np

df = pd.read_excel('concated_data.xlsx')
pull_up = df['PullUp']
print(np.std(pull_up))
print(np.mean(pull_up)-1.3*np.std(pull_up))
print(np.mean(pull_up)+1.3*np.std(pull_up))