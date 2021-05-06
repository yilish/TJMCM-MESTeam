import pandas as pd

df = pd.read_excel('concated_data.xlsx')

df.loc[:, 'fit_position'] = df.loc[:, 'Position']
df.loc[:, 'pos_code'] = 0
i = 0
for item in df.loc[:, 'fit_position']:
    if item == '后腰' or item == '后卫' or item == '边后':
        df.loc[i, 'fit_position'] = '后卫'
        df.loc[i, 'pos_code'] = 0

    elif item == '中场':
        df.loc[i, 'fit_position'] = '中场'
        df.loc[i, 'pos_code'] = 1
    elif item == '前腰' or item == '前卫' or item == '边前卫' or item == '前锋' or item == '边前':
        df.loc[i, 'fit_position'] = '前卫'
        df.loc[i, 'pos_code'] = 2
    else:
        df.loc[i, 'pos_code'] = 3
    i += 1

df.to_excel('coded_position.xlsx')