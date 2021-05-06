import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel('failed_list.xlsx')
# print(df['team'])
freq = [0] * 16
for item in list(df['team']):
    freq[item] += 1
df = pd.DataFrame(freq)
df.to_excel('failed teams.xlsx')
print(freq)
plt.bar(range(16), freq, color=(0.9, 0, 0.22))
plt.xticks([x for x in range(1, 16)])
plt.yticks([y for y in range(2,22,2)])
plt.title('Failed Players\' Team Distribution')
plt.xlabel('Team Number')
plt.ylabel('Failed Player Sum')
plt.show()