import numpy as np
from dataset.mnist import load_mnist
from two_layer_pytorch import TwoLayerNet
import pickle
import torch.optim as optim
import torch
import torch.nn as nn

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)
model = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

iters_num = 10000  
train_size = x_train.shape[0]
batch_size = 100

train_acc_list = []
test_acc_list = []

iter_per_epoch = max(train_size / batch_size, 1)
criterion = nn.MSELoss()

optimizer = optim.SGD(model.parameters(), lr=0.01)

#model.train()

for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch =torch.from_numpy(x_train[batch_mask]) 
    t_batch =torch.from_numpy(t_train[batch_mask]) 
    t_batch = torch.tensor(t_batch, dtype=torch.float32)

    optimizer.zero_grad()
    output = model(x_batch)
    loss = criterion(output,t_batch)
    loss.backward()
    optimizer.step()

    if i%iter_per_epoch==0:
        train_acc = model.accuracy(torch.from_numpy(x_train), t_train)
        test_acc = model.accuracy(torch.from_numpy(x_test), t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print("train acc, test acc | " + str(train_acc) + ", " + str(test_acc))