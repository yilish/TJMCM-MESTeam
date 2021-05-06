import pandas as pd
df = pd.read_excel('concated_score_data.xlsx')

df_door = pd.DataFrame(columns=df.columns)
df_guard = pd.DataFrame(columns=df.columns)
df_midField = pd.DataFrame(columns=df.columns)
df_striker = pd.DataFrame(columns=df.columns)

for idx, val in df.iterrows():
    if val['Position'] == '守门员' :
        df_door = df_door.append(val)
    elif val['Position'] == '后卫' or val['Position'] == '边后':
        df_guard = df_guard.append(val)
    elif val['Position'] == '后腰' or val['Position'] == '边前卫'or val['Position'] == '前腰'or val['Position'] == '中场'or val['Position'] == '前卫' or val['Position'] == '边前':
        df_midField = df_midField.append(val)
    elif val['Position'] == '前锋' or val['Position'] == '边前':
        df_striker = df_striker.append(val)
    elif val['Position'] == '待定':
        df_door = df_door.append(val)
        df_guard = df_guard.append(val)
        df_midField = df_midField.append(val)
        df_striker = df_striker.append(val)

df_door['Position'] = '守门员'
df_striker['Position'] = '前锋'
df_midField['Position'] = '中场'
df_guard['Position'] = '后卫'
df_door.to_excel('classes/GoalKeeper.xlsx')
df_striker.to_excel('classes/Striker.xlsx')
df_midField.to_excel('classes/MidField.xlsx')
df_guard.to_excel('classes/Guard.xlsx')
