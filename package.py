import random

class neuron():
    def __init__(self,input):
        self.weight = random.random()
        self.bias = random.random()
        self.activation_function = 'relu'
        self.input = input
        self.output = 0
    def activate(self,input,activation_function):
        if activation_function=='relu':return max(0,input)
    def forwardpropagation(self):
        for i in self.input:
            self.output += self.weight * i
            self.output += self.bias
            self.activate(self.output, self.activation_function)
    

class layer():
    def __init__(self, inputlayer, numofneuron):
        self.inputlayer = inputlayer
        self.neurons = [neuron(inputlayer) for i in range(numofneuron)]
        self.outputlayer = []
    def forwardpropagation(self):
        for i in self.neurons:
            i.forwardpropagation()
            self.outputlayer.append(i.output)


class network():
    def __init__(self,inputlayer,dimension):
        self.dimension = dimension
        self.inputlayer = inputlayer
        self.layers = [inputlayer]
        for i in range(len(self.dimension)):self.layers.append(layer(self.layers[-1],self.dimension[i]))#adding num of hidden layers based on given dimension ##including the outputlayer##
        self.output = ['initalization required!']  #above: add a layer with the privious layer as the inputlayer and numofnueron based on dimension
    def forwardpropagation(self):
        for i in self.layers:
            if i==self.layers[0]:pass
            else:i.forwardpropagation()
        self.output = self.layers[-1].outputlayer
        

x = network([1],[1])
x.forwardpropagation()
print(x.output)