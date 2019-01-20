import random
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
        self.output = 0
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
        self.outputlayer = [0 for i in range(numofneuron)]
        self.gradients = [[0,0] for i in range(numofneuron)]
    def forwardpropagation(self):
        for i in range(len(self.neurons)):
            self.neurons[i].forwardpropagation()
            self.outputlayer[i] = self.neurons[i].output       

class network():
    def __init__(self,dimension):
        self.dimension = dimension
        self.layers = [[1]]
        for i in range(1):self.layers.append(layer(self.layers[0],self.dimension[i]))
        for i in range(1, len(self.dimension)):self.layers.append(layer(self.layers[-1].outputlayer,self.dimension[i]))#adding num of hidden layers based on given dimension ##including the outputlayer##
        #for i in self.layers[-1]:i.activation_function==None #output layer which has no activation
        self.output = ['initalization required!']  #above: add a layer with the privious layer as the inputlayer and numofnueron based on dimension
        self.gradients = [[] for i in range(len(self.dimension))]
        for j in range(len(self.dimension)):
            self.gradients[j] = [[[] for i in range(2)] for i in range(self.dimension[j])]
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
    def setdata(self,training,testing,valadating):
        self.trainingdata = training
        self.testingdata = testing
        self.valadatingdata = valadating
    def get_gradients(self,flashtarget):
        self.ata = [[] for i in range(len(self.dimension)-1)]
        for i in range(len(self.layers)-2):
            self.ata[i] = [j.weight for j in self.layers[i+2].neurons]
        for l in range(len(self.gradients)):
            for n in range(len(self.gradients[l])):
                if (sum(self.layers[l+1].neurons[n].input) * self.layers[l+1].neurons[n].weight + self.layers[l+1].neurons[n].bias) < 0:
                    try:del self.ata[l][n]
                    except:pass
        for i in range(len(self.ata)):self.ata[i] = sum(self.ata[i])
        for i in range(len(self.ata)):
            for j in self.ata[i:]:
                self.ata[i] *= j
        for l in range(len(self.layers[1:-1])):
            for n in range(len(self.gradients[l])):
                if sum(self.layers[l+1].neurons[n].input) * self.layers[l+1].neurons[n].weight + self.layers[l+1].neurons[n].bias > 0:
                    self.gradients[l][n][0] = sum(self.layers[l+1].neurons[n].input) * self.ata[l] * (-2 * (sum(flashtarget) - sum(self.layers[-1].outputlayer)))
                    self.gradients[l][n][1] = 1 * self.ata[l] * (-2 * (sum(flashtarget) - sum(self.layers[-1].outputlayer)))
                else:
                    self.gradients[l][n][0] = 0
                    self.gradients[l][n][1] = 0
        for i in self.gradients[-1]:
            i[0] = sum(self.layers[l+1].neurons[n].input) * (-2 * (sum(flashtarget) - sum(self.layers[-1].outputlayer)))
            i[1] = 1 * (-2 * (sum(flashtarget) - sum(self.layers[-1].outputlayer)))
    def train(self,rate,rounds):
        cost = 0
        for i in range(rounds):
            self.inputlayer = self.trainingdata[i][0]
            self.forwardpropagation()
            self.get_gradients(self.trainingdata[i][1])
            #backpropagation
            for l in range(0,len(self.layers[1:])):
                for n in range(len(self.layers[l+1].neurons)):
                    self.layers[l+1].neurons[n].weight += -self.gradients[l][n][0] * rate
                    self.layers[l+1].neurons[n].bias += -self.gradients[l][n][1] * rate
            for j in range(len(self.testingdata[i][1])):
                cost += (self.testingdata[i][1][j] - self.layers[-1].outputlayer[j]) ** 2

            
            print("rounds:",i,"costs:",cost/(i+1))