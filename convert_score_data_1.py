# utf-8#
import pandas as pd
sheet = pd.read_excel('source_data.xlsx', sheet_name=None)
l = ['守门员', '中场', '前卫', '后腰', '后卫', '边前卫', '前腰', '边后', '边前', '前锋']
pdList = []
for i in range((len(l))):
    pdList.append(pd.DataFrame())
num = 1
standard = pd.read_excel('standard.xlsx')

# print(standard['30m'])
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

def get_weight(label):
    if label == '30m':
        return 0.15
    if label == 'ArrowRun':
        return 0.15
    if label == 'PullUp':
        return 0.1
    if label == 'LongJump':
        return 0.1
    if label ==  'YoYo':
        return 0.4
    if label == 'HighJump':
        return 0.1
for i in range(1, 16):
    df = pd.read_excel('deleted_data/' + str(i) +'.xlsx',usecols=range(1,9))
    df.loc[:, 'sum'] = 0
    # df.loc[:, 'team'] = i
              #(df.shape[1], 'sum', 0)
    # newDf = pd.DataFrame(columns=df.columns)
    j = 0
    for index, row in df.iterrows():
        # newL = []
        # newL.append([])
        sum = 0
        for idx, val in row.iteritems():
            if idx =='sum' or idx == 'team' or idx == 'id':
                continue
            elif idx == 'Unnamed: 0' or idx == 'Code' or idx == 'Position':
                print(idx)
                df.loc[j, idx] = val
            else:
                print(idx)
                df.loc[j, idx] = find_score_of_label(idx, val)
                sum += get_weight(idx) * find_score_of_label(idx, val)
        print(sum)
        df.loc[j, 'sum'] = sum
        j += 1
        # newDf.append(newL)
        # newDf = newDf.append(newL)

    df.to_excel('del_sum_score/' + str(i) + '.xlsx')