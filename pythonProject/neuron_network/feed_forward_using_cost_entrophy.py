import random
import tensorflow as tf
import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))
def flatten(input):
    input = np.array(input)
    input = input.reshape(len(input), 1)
    return input
def prime_sigmoid(x):
    x=np.array(x)
    return x*(1-x)

def fn(a, y):
    return np.sum(np.nan_to_num(-y * np.log(a) - (1 - y) * np.log(1 - a)))
class Neuron_Network:
    def __init__(self,input_nodes, hidden_nodes, output_nodes):
        self.input_nodes= input_nodes
        self.hidden_nodes= hidden_nodes
        self.output_nodes= output_nodes

        self.weight_ih= np.random.randn(hidden_nodes, input_nodes)
        self.weight_ho= np.random.randn(output_nodes, hidden_nodes)

        self.bias_h= np.random.randn(hidden_nodes,1)
        self.bias_o= np.random.randn(output_nodes,1)

        self.learning_rate=0.1
    def feedforward(self, input):
        input=np.array(flatten(input))
        hidden= np.dot(self.weight_ih, input)+ self.bias_h
        hidden_s= np.array(sigmoid(hidden))


        output=np.dot(self.weight_ho, hidden_s)+ self.bias_o
        output_s=np.array(sigmoid(output))
        return output_s
    def train(self,input, target):
        input = np.array(flatten(input))
        hidden = np.dot(self.weight_ih, input) + self.bias_h
        hidden = np.array(sigmoid(hidden))

        output = np.dot(self.weight_ho, hidden) + self.bias_o
        output = np.array(sigmoid(output))

        target=flatten(target)
        output_error= target-output
        gradient= self.learning_rate * output_error

        hidden_T=hidden.transpose()
        weight_ho_delta=np.dot(gradient, hidden_T)
        self.weight_ho+=weight_ho_delta
        self.bias_o+=gradient

        who_t= self.weight_ho.transpose()
        hidden_error= np.dot(who_t, output_error)

        hidden_gradient=prime_sigmoid(hidden)
        hidden_gradient=np.multiply(hidden_gradient, hidden_error)
        hidden_gradient=self.learning_rate * hidden_gradient
        input_T= input.transpose()
        weight_ih_delta=np.dot(hidden_gradient, input_T)
        self.weight_ih+=weight_ih_delta
        self.bias_h+=hidden_gradient
        print(fn(output,target))




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