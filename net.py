import numpy as np

class Layer:
    def __init__(self,weights, biases, activation, learning_rate):
        self.weights= np.array(weights)
        self.biases = np.array(biases)
        self.activation = activation
        self.learning_rate = learning_rate


    def forward(self, inputs):
        forwrd = np.dot(inputs, self.weights) + self.biases
        
        return self.activation(forwrd)
    
    def train(self, previous, loss):
        grad_weight = np.outer(loss,  previous)
        grad_bias = loss

        previous_blame = np.dot(self.weights.T, loss)

        self.weights -= grad_weight * self.learning_rate
        self.biases -= grad_bias * self.learning_rate

        return previous_blame





class Network:
    def __init__(self, layers, predicted, learning_rate, cache):
        self.layers = layers
        self.predicted = predicted
        self.learning_rate = learning_rate
        self.cache = [cache]

    def train(self):
        layers = self.layers
        for layer in layers:
            print(input,  "input")
            print(layer, "layer")
            output = layer.forward(input)
            self.cache.append(input)
        return input

    def calculate(self, input):
        
        layers = self.layers
        for layer in layers:
            print(input,  "input")
            print(layer, "layer")
            output = layer.forward(input)

        return output
    
    def backward(self, output):
        self.layers.count.downto(0) 
    # do this here







def ReLU(x):
    return np.maximum(0, x)

def ReLU_derivative(x):
    return np.where(x > 0, 1, 0)

def Sigmoid(x):
    return 1 / (1 + np.exp(-x)) 

# Create layers


def rand_network(input, layers, output):
    network_layers = []
    past = input

    for layer in layers:
        np.random.seed(43)
        weights = np.random.randn(past, layer) * np.sqrt(2 / past)
        biases = np.zeros(layer)

        net = Layer(weights, biases, ReLU)
        network_layers.append(net)

        past = layer

    weights = np.random.randn(past, output) * np.sqrt(1 / past)
    biases = np.zeros(output)

    last = Layer(weights, biases, Sigmoid)
    network_layers.append(last)

    network = Network(network_layers, 1, 1)

    return network



network = rand_network(2, [2, 3], 1)

print(network.calculate([1,2 ]))
