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

class network():
    def __init__(self,inputlayer,dimension):
        self.dimension = dimension
        self.inputlayer = inputlayer
        self.layers = [inputlayer]
        for i in range(1):self.layers.append(layer(self.layers[0],self.dimension[i]))
        for i in range(1, len(self.dimension)):self.layers.append(layer(self.layers[-1].outputlayer,self.dimension[i]))#adding num of hidden layers based on given dimension ##including the outputlayer##
        #for i in self.layers[-1]:i.activation_function==None #output layer which has no activation
        self.output = ['initalization required!']  #above: add a layer with the privious layer as the inputlayer and numofnueron based on dimension
        self.gradients = [[] for i in range(len(self.dimension))]
        for j in range(len(self.dimension)):
            self.gradients[j] = [[] for i in range(self.dimension[j])]
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
    def get_gradients(self):
        for l in self.layers[1:]:
            for n in l.neurons:
                if sum(n.input) * n.weight + n.bias > 0:
                    self.gradients[l][n] = sum(n.input)
                else:
                    self.gradients[l][n] = 0
        self.ata = [[] for i in range(len(self.dimension)-1)]
        for i in range(len(self.layers)-2):
            self.ata[i] = [sum(j.weight for j in self.layers[i+2].neurons)]
        for l in range(len(self.gradients)):
            for n in range(len(self.gradients[l].neurons)):
                if (sum(self.layers[l+1].neurons[n].input) * self.layers[l+1].neurons[n+1].weight + self.layers[l+1].neurons[n+1].bias) > 0:
                    #self.gradients[l][n] *= 
                    pass
            


x = network([1],[1,2,1])
x.forwardpropagation()
print(x.output)
x.get_gradients()
print(x.ata)