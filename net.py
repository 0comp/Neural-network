import numpy as np

class Layer:
    def __init__(self,weights, biases, activation):
        self.weights= np.array(weights)
        self.biases = np.array(biases)
        self.activation = activation


    def forward(self, inputs):
        forwrd = np.dot(inputs, self.weights) + self.biases
        
        return self.activation(forwrd)


class Network:
    def __init__(self, layers, predicted, learning_rate):
        self.layers = layers
        self.predicted = predicted
        self.learning_rate = learning_rate


    def calculate(self, input):
        layers = self.layers
        for layer in layers:
            input = layer.forward(input)
            print("leter")

        return input






def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def ReLU(x):
    return np.maximum(0, x)

def ReLU_derivative(x):
    return np.where(x > 0, 1, 0)

def Sigmoid(x):
    return 1 / (1 + np.exp(-x)) 


weights1 = np.random.randn(9, 20) * np.sqrt(2 / 9)
biases1 = np.zeros(20)

weights2 = np.random.randn(16, 20) * np.sqrt(2 / 20)
biases2 = np.zeros(20)

weights3 = np.random.randn(20, 9) * np.sqrt(1 / 20)
biases3 = np.zeros(9)


# Create layers


def rand_network(input, layers, output):
    network_layers = []
    past = input

    for layer in layers:
        weights = np.random.randn(layer, past) * np.sqrt(2 / past)
        biases = np.zeros(layer)

        net = Layer(weights, biases, ReLU)
        network_layers.append(net)

        past = layer

    weights = np.random.randn(output, past) * np.sqrt(1 / past)
    biases = np.zeros(output)

    last = Layer(weights, biases, Sigmoid)
    network_layers.append(last)

    network = Network(network_layers, 1, 1)

    return network



network = rand_network(2, [2, 3], 1)

print(network.calculate([1, 2]))

