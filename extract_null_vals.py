import pandas as pd
df = pd.DataFrame()
for i in range(1, 16):
    change_name_data = pd.read_excel('changed_names/' + str(i) + '_changed_name.xlsx', usecols=range(2,9))
    # change_name_data = change_name_data[[1, :]]
    for index, row in change_name_data.iterrows():
        for idx, val in row.iteritems():
            if pd.isna(val) or val == 0:
                row['team'] = i
                df = df.append(row, ignore_index=True)
                break

df.to_excel('null_vals.xlsx')