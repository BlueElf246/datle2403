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
        hidden = np.dot(self.weight_ih, input) + self.bias_h
        hidden = np.array(sigmoid(hidden))

        output = np.dot(self.weight_ho, hidden) + self.bias_o
        output = np.array(sigmoid(output))

        output_error= target-output
        gradient=prime_sigmoid(output)
        gradient=np.multiply(gradient, output_error)
        gradient= self.learning_rate * gradient

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





nn=Neuron_Network(784,300,1)
def change(input):
    return np.array(input).reshape(784,1)
mnist=tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test)= mnist.load_data()
for i in range(100000):
    rand = random.randint(0, 59999)
    x_train_element= change(x_train[rand])
    nn.train(x_train_element,y_train[rand])

print(nn.feedforward(change(x_train[0])))













