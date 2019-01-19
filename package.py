import random
def decode(op,object):
    for i in op:
        if i[0] == "*":object *= i[1]
        elif i[0] == "+":object += i[1]
        elif i[0] == 'relu':object = max(0,object)
        elif i[0] == "**":object = object ** i[1]
def chain(op,object):
    dop = []
    for i in op.reverse():
        if i[0] == "*":
            dop.append([""])
class neuron():
    def __init__(self,input):
        self.weight = random.random()
        self.bias = random.random()
        self.activation_function = 'relu'
        self.input = input
        self.output = 0
        self.op_output = [["*",self.weight],["+",self.bias],['relu','relu']]
    def activate(self,input,activation_function):
        if activation_function=='relu':return max(0,input)
        if activation_function==None:pass
    def forwardpropagation(self):
        for i in self.input:
            self.output += self.weight * i
            self.output += self.bias
            self.activate(self.output, self.activation_function)
    def get_gradients(self, target): #target can be either int or float
        if self.activation_function == 'relu':
            if sum(self.input) * self.weight - self.bias > 0:
                dw = -2 * (target - max(0, (self.weight * sum(self.input) - self.bias))) * sum(self.input) #-2(y-Relu(wx+b))*1*x
                db = -2 * (target - max(0, (self.weight * sum(self.input) - self.bias))) #-2(y-Relu(wx+b))
            else:
                dw = 0
                db = 0
        self.gradients = [dw,db]
class layer():
    def __init__(self, inputlayer, numofneuron):
        self.inputlayer = inputlayer
        self.neurons = [neuron(inputlayer) for i in range(numofneuron)]
        self.outputlayer = []
        self.gradients = [[0,0] for i in range(numofneuron)]
    def forwardpropagation(self):
        for i in self.neurons:
            i.forwardpropagation()
            self.outputlayer.append(i.output)
    def get_gradients(self, target): #target here should be a list of int or float
        for i in range(len(self.neurons)):
            self.gradients[i] = self.neurons[i].get_gradients(target[i])
        

class network():
    def __init__(self,inputlayer,dimension):
        self.dimension = dimension
        self.inputlayer = inputlayer
        self.layers = [inputlayer]
        for i in range(len(self.dimension)):self.layers.append(layer(self.layers[-1],self.dimension[i]))#adding num of hidden layers based on given dimension ##including the outputlayer##
        #for i in self.layers[-1]:i.activation_function==None #output layer which has no activation
        self.output = ['initalization required!']  #above: add a layer with the privious layer as the inputlayer and numofnueron based on dimension
    def forwardpropagation(self):
        for i in self.layers:
            if i==self.layers[0]:pass
            else:i.forwardpropagation()
        self.output = self.layers[-1].outputlayer
    def get_cost(self, target): #flexable to change based on need, below is the template
        self.cost = 0 
        for i in range(len(target)):
            self.cost += (target[i]-self.output[i]) ** 2
        return self.cost
    def OTC(self,target):
        pass



x = network([1],[1])
x.forwardpropagation()
print(x.output)