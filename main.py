from package import network

data = [[[0],[0]] for i in range(50)]
for i in range(50):
    data[i] = [[i],[i*i]]

x = network([1,3,3,1])
x.setdata(data,data,data)
for i in range(10):
    x.train(0.0001,5)

print(x.layers[-1].neurons[0].weight,x.layers[-1].neurons[0].bias)
