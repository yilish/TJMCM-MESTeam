import pandas as pd
import torch
import numpy as np
class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.n_hidden = torch.nn.Linear(n_feature, n_hidden)
        self.out = torch.nn.Linear(n_hidden, n_output)
    def forward(self, x_layer):
        x_layer = torch.relu(self.n_hidden(x_layer))
        x_layer = self.out(x_layer)
        x_layer = torch.softmax(x_layer,dim=0)
        return x_layer
net = Net(n_feature=6, n_hidden=10, n_output=4)
# print(net)
optimizer = torch.optim.SGD(net.parameters(), lr=0.02)
loss_func = torch.nn.CrossEntropyLoss()
df = pd.read_excel('coded_position.xlsx')
x = np.array(df.iloc[:, 3:9])

y = np.array(df.iloc[:, -1])

for i in range(len(y)):
    y[i] = list(y[i])
x = torch.FloatTensor(x)
y = torch.FloatTensor(y)
print(y)

for i in range(100):
    out = net(x)

    loss = loss_func(out, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

test = [3.93, 5.31, 2.76, 59.2, 10, 1040]
predict = net(test)
print(predict)