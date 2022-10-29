import random
import numpy as np
def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    return sigmoid(z)*(1-sigmoid(z))

class Neuron_Network(object):
    def __init__(self,sizes):
        self.num_layers=len(sizes)
        self.sizes=sizes
        self.bias= [np.random.randn(y,1) for y in sizes[1:]]
        self.weight=[np.random.randn(y,x)for x,y in zip(sizes[:-1], sizes[1:])]
    def feedforward(self, a):
        for b, w in zip(self.bias, self.weight):
            a = sigmoid(np.dot(w, a) + b)
        return a
    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):

        if test_data:
            n_test=len(test_data)
        n=len(training_data) # return the total example
        for j in range(epochs):
            random.shuffle(training_data)
            minibatches=[training_data[k:k+mini_batch_size] for k in range(0,n,mini_batch_size)]
            # if total training seq.txt is 60000, then minibatch size is only 6000
            for mini_batch in minibatches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print('Epchos {0}: {1}/{2}'.format(j, self.evaluate(test_data), n_test ))
            else:
                print('Epchos {0} complete'.format(j))

    def update_mini_batch(self,mini_batch, eta):
        nabla_w= [np.zeros(w.shape) for w in self.weight]
        nabla_b=[np.zeros(b.shape) for b in self.bias]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w= self.backprop(x,y)
            nabla_b=[nb +dnb for nb,dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w=[nw + dnw for nw,dnw in zip(nabla_w, delta_nabla_w)]

        self.weight=[w -((eta/len(mini_batch))* nw) for w, nw in zip(self.weight, nabla_w)]
        self.bias = [b -((eta / len(mini_batch)) * nb) for b, nb in zip(self.bias, nabla_b)]

    def backprop(self,x,y):
        nabla_b = [np.zeros(b.shape) for b in self.bias]
        nabla_w = [np.zeros(w.shape) for w in self.weight]
        # feedforward
        activation=x # the input
        activations=[x] # use to store all activation function
        zs=[] # use to store all activation function without sigmoid
        # produce all the activation function

        for b,w in zip(self.bias, self.weight):
            z=np.dot(w,activation) +b
            zs.append(z)
            activation=sigmoid(z)
            activations.append(activation)
        #backward pass
        delta= self.cost_derivative(activations[-1], y) * sigmoid_prime(zs[-1])
        nabla_b[-1]=delta
        nabla_w[-1]=np.dot(delta, np.array(activations[-2]).transpose())
        for l in range(2, self.num_layers):
            z=zs[-l]
            sp=sigmoid_prime(z)
            delta= np.dot(np.array(self.weight[-l+1]).transpose(),delta ) * sp
            nabla_b[-l]= delta
            nabla_w[-l]= np.dot(delta, np.array(activations[-l-1]).transpose())
        return (nabla_b,nabla_w)

    def evaluate(self, test_data):
        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):
        return (output_activations-y)



