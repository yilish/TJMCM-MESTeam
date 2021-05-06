import pandas as pd
df = pd.DataFrame()
for i in range(1, 16):
    change_name_data = pd.read_excel('changed_names/' + str(i) + '_changed_name.xlsx', usecols=range(2,9))
    # change_name_data = change_name_data[[1, :]]
    #change_name_data.loc[:, 'id'] = 0
    for index, row in change_name_data.iterrows():
        change_name_data.loc[index, 'id'] = index + 1
        for idx, val in row.iteritems():
            if pd.isna(val) or val == 0:
                change_name_data = change_name_data.drop(labels=index)
                break
        # print(change_name_data)
    change_name_data['team'] = i
    change_name_data.to_excel('deleted_data/' + str(i) + '.xlsx')
# df.to_excel('null_vals.xlsx')