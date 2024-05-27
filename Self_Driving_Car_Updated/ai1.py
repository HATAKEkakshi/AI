import numpy as np
import random
import os
import torch
import torch.nn as nn
import torch.nn.functional as f
import torch.optim as optim
import torch.autograd as autograd
from  torch.autograd import Variable

#Creating the architecture of the neural network
class Network(nn.Module):
    def __init__(self, input_size, nb_action):
        super(Network,self).__init__()
        self.input_size=input_size
        self.nb_action=nb_action
        self.fc1=nn.Linear(input_size, 30)
        self.fc2=nn.Linear(30,nb_action)