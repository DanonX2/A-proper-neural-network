from package import *


data = [[[2,2],[10]]]
x = network([1,3,5,1])
x.setdata(data,data,data)
for i in range(10):
    x.train(0.008,1)

print(x.layers[-1].outputlayer)