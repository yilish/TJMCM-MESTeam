import pandas as pd
df = pd.read_excel('source_data.xlsx', sheet_name=None)
newCol = ['Code','30m', 'ArrowRun', 'LongJump', 'HighJump', 'PullUp', 'YoYo', 'Position']
num = 1
for j in df.values():
    j.columns = newCol
    j.to_excel('changed_names/' + str(num) + '_changed_name.xlsx')
    num += 1
