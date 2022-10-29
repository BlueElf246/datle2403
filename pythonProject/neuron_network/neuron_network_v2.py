import random
import numpy as np
def flatten(input):
    input=np.array(input)
    return input.reshape(len(input), 1)
def sigmoid(input):
    input=np.array(input)
    return 1/(1+np.exp(-input))
def prime_sigmoid(input):
    input=np.array(input)
    return input*(1-input)
class Neuron_Network():
    def __init__(self,input_layer_nodes, hidden_layers_nodes, output_layers_nodes):
        self.input_nodes=input_layer_nodes
        self.hidden_nodes= hidden_layers_nodes
        self.output_nodes= output_layers_nodes

        self.weight_ih=np.random.rand(hidden_layers_nodes, input_layer_nodes)
        self.weight_ho= np.random.rand(output_layers_nodes, hidden_layers_nodes)
        self.bias_ih=np.random.rand(hidden_layers_nodes,1)
        self.bias_ho=np.random.rand(output_layers_nodes,1)

        self.learning_rate=0.1
    def feedforward_1(self, input): # let take example with (2,2,1)
        lst=[]
        input= flatten(input)
        hidden=np.dot(self.weight_ih, input) + self.bias_ih # result= 2x1
        hidden_s=sigmoid(hidden)
        lst.append(hidden_s)
        output=np.dot(self.weight_ho, hidden_s) +self.bias_ho # result= 1x1
        output_s=sigmoid(output)
        lst.append(output_s)
        return lst

    def feedforward(self, input):  # let take example with (2,2,1)
        input = flatten(input)
        hidden = np.dot(self.weight_ih, input) + self.bias_ih # result= 2x1
        hidden_s = sigmoid(hidden)
        output = np.dot(self.weight_ho, hidden_s)+self.bias_ho  # result= 1x1
        output_s = sigmoid(output)
        return output_s
    def train(self,input, output):
        # calculate the guess
        output=flatten(output)
        hidden, predict= self.feedforward_1(input)


        #calculate error
        error_o= output- predict

        sigmoid_predict= prime_sigmoid(predict)
        # delta_B_output
        delta= self.learning_rate * (np.multiply(sigmoid_predict, error_o)) # result 1x1
        #delta_W_output
        delta_W= np.dot(delta, np.array(hidden).transpose()) #result 1x2
        #update the weight, bias
        self.bias_ho+=delta
        self.weight_ho+=delta_W

        error_hidden=np.dot(np.array(self.weight_ho).transpose(), error_o) # result 2x1
        sigmoid_hidden=prime_sigmoid(hidden)
        delta_B_hidden= self.learning_rate * (np.multiply(sigmoid_hidden, error_hidden)) # result 2x1
        input=flatten(input)
        delta_W_hidden= np.dot(delta_B_hidden, np.array(input).transpose()) #reuslt 2x2
        self.bias_ih+=delta_B_hidden
        self.weight_ih+=delta_W_hidden
        print(error_o)







nn= Neuron_Network(2,128,1)
a=[[1,1],[0]]
b=[[0,0],[0]]
c=[[1,0],[1]]
d=[[0,1],[1]]
lst=[a,b,c,d]
def doloop():
    for i in range(50000):
        rand = random.randint(0, 3)
        nn.train(lst[rand][0], lst[rand][1])
doloop()

print(nn.feedforward([1,0]))
print(nn.feedforward([0,1]))
print(nn.feedforward([0,0]))
print(nn.feedforward([1,1]))

