# A-proper-neural-network
this is a simple nerual network based on gradient descent.
# what you need to start
1. a properly formated training dataset (features and target), see sample
2. a properly formated test dataset, another validation set is more favorable
3. thats it
# Notes
-the datasets function is undevelped meaning it doesnt matter if you put in a test set or a valadation set, it will always train the nn 1b1

-datasets format: 3d array : [[situation1, [situation2] .... ] situation [input,output]  input/output [feature1/output1,feature2/output2...]

-network class instructions: network1 = network(dimension)     dimension is a list of ints represents the dimension of the network 
eg: [1,2,3,5,1] represents 4 hidden layers of 1,2,3,5 neurons and a output dimension of 1

