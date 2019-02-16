import pandas as pd
from random import seed
from random import random

def initialize_network(n_inputs, n_hidden, n_outputs):
    network = list()
    hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
    network.append(hidden_layer)
    output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
    network.append(output_layer)
    return network

def activate(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights)-1):
        activation += weights[i] * inputs[i]
    return activation

def transfer(activation):
    return 1.0 / (1.0 + exp(-activation))


filename = "‪data.csv"

x = pd.read_csv(filename)

alpha = 1

mapping = {'P': 1,'A': 2, 'N': 3, 'NB': 1, 'B': 2}
cols = {'IR', 'MR', 'FF', 'CR', 'CO', 'OP'}
l = len(x)
for col in cols :
    x[col] = x[col].map(mapping).astype(int)
    
for col in cols:
    x[col] = x[col].fillna((x[col].mean())).astype(int)

n_inputs = len(x.index)
n_hidden = len(x.columns) - 1
seed(1)
network = initialize_network(n_inputs, n_hidden, 1)
for layer in network:
    print(layer)

