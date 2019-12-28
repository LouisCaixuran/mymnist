import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import torch

class TwoLayerNet(nn.Module):

    def __init__(self, input_size=784, hidden_size=50, output_size=10):
        super(TwoLayerNet, self).__init__()
        self.fc1=nn.Linear(784,50)
        self.fc2=nn.Linear(50,10)

    def forward(self,x):
        a1=F.relu(self.fc1(x))
        z1=torch.sigmoid(a1)
        a2=F.relu(self.fc2(z1))
        y=F.softmax(a2,dim=0)

        return y


    def accuracy(self, x, t):
        y = self.forward(x)
        y = torch.argmax(y, dim=1)
        t = np.argmax(t, axis=1)
        z=y.numpy()
        indx=0
        for i,j in zip(z,t):
            if i==j:
                indx=indx+1
        accuracy = indx / len(z)
        return accuracy
