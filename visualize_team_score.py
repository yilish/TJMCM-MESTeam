import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel('score_group_by_team.xlsx')
plt.bar(range(1, len(df['sum']) + 1), df['sum'])
plt.yticks([y for y in range(1,9,1)])
plt.xticks(range(1, 16))
plt.title('Score Distribution Group By Team')
plt.xlabel('Team')
plt.ylabel('Score')
plt.show()
print(df['sum'])
