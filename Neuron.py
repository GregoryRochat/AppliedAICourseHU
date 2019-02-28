import random
import math


class Neuron:
    def __init__(self, weights=[], ninput=0):
        self.activation = ninput
        self.weights = weights

    error = 0

    def setinput(self, newactivation):
        self.activation = newactivation

    def getoutput(self, weight):
        return self.weights[weight] * self.activation

    def update(self, outputerrors, hiddenlayer, stepsize):
        for i in range(0, len(outputerrors)):
            self.weights[i] = self.weights + stepsize * self.activation * outputerrors



class NeuronLayer:
    def __init__(self, layersize):
        self.neurons = []
        for neuron in range(0, layersize):
            self.neurons.append(Neuron())

    def update(self):
        for neuron in self.neurons:
            neuron.update()


class GenericNeuralNetwork:
    def __init__(self, neuronlayers):
        self.neuronnetwork = []
        for n in range(0, len(neuronlayers)):
            self.neuronnetwork.append(NeuronLayer(neuronlayers[n]))


gnn = GenericNeuralNetwork([10,10,10,10,10,5])
for neuronlayer in gnn.neuronnetwork:
    neuronlayer.update()
    print("")



