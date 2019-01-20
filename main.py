from package import network

data = [[[0],[0]] for i in range(50)]
for i in range(50):
    data[i] = [[i],[i*i]]

x = network([1])
x.setdata(data,data,data)
x.train(0.1,5)

print(x.layers[-1].outputlayer)
