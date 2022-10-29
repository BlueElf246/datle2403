import numpy as np
import h5py
import random
import matplotlib.pyplot as plt
class Neuron_Network():
    costs=[]
    def __init__(self,layers_dims):
        self.parameters = self.initialize_parameters_deep(layers_dims)

    def predict(self,X, y, parameters):
        m =1
        n = len(parameters) // 2  # number of layers in the neural network
        p = np.zeros((1, m), dtype=int)
        # Forward propagation
        probas, caches = self.L_model_forward(X, parameters)
        print(probas)
        # convert probas to 0/1 predictions
        for i in range(0, probas.shape[1]):
            if probas[0, i] > 0.5:
                p[0, i] = 1
            else:
                p[0, i] = 0
        print("predictions: " + str(p))
        print("true labels: " + str(y))
        print("Accuracy: %s" % str(np.sum(p == y) / float(m)))
        return p
    def sigmoid(self,Z):
        A = 1 / (1 + np.exp(-Z))
        cache = Z
        return A, cache
    def relu(self,Z):
        A = np.maximum(0, Z)
        cache = Z
        return A, cache
    def relu_backward(self,dA, cache):
        Z = cache
        dZ = np.array(dA, copy=True)  # just converting dz to a correct object.
        # When z <= 0, you should set dz to 0 as well.
        dZ[Z <= 0] = 0
        return dZ
    def sigmoid_backward(self,dA, cache):
        Z = cache
        s = 1 / (1 + np.exp(-Z))
        dZ = dA * s * (1 - s)
        return dZ
    def load_data(self):
        train_dataset = h5py.File('datasets/train_catvnoncat.h5', "r")
        train_set_x_orig = np.array(train_dataset["train_set_x"][:])  # your train set features
        train_set_y_orig = np.array(train_dataset["train_set_y"][:])  # your train set labels

        test_dataset = h5py.File('datasets/test_catvnoncat.h5', "r")
        test_set_x_orig = np.array(test_dataset["test_set_x"][:])  # your test set features
        test_set_y_orig = np.array(test_dataset["test_set_y"][:])  # your test set labels

        classes = np.array(test_dataset["list_classes"][:])  # the list of classes

        train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
        test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

        return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes

    def initialize_parameters_deep(self,layer_dims):
        # np.random.seed(1)
        parameters = {}
        L = len(layer_dims)  # number of layers in the network

        for l in range(1, L):
            parameters['W' + str(l)] = np.random.randn(layer_dims[l], layer_dims[l - 1]) / np.sqrt(
                layer_dims[l - 1])  # *0.01
            parameters['b' + str(l)] = np.zeros((layer_dims[l], 1))
        return parameters
    def linear_forward(self,A, W, b):
        Z = W.dot(A) + b
        cache = (A, W, b)
        return Z, cache
    def linear_activation_forward(self,A_prev, W, b, activation):
        if activation == "sigmoid":
            # Inputs: "A_prev, W, b". Outputs: "A, activation_cache".
            Z, linear_cache = self.linear_forward(A_prev, W, b)
            A, activation_cache = self.sigmoid(Z)

        elif activation == "relu":
            # Inputs: "A_prev, W, b". Outputs: "A, activation_cache".
            Z, linear_cache = self.linear_forward(A_prev, W, b)
            A, activation_cache = self.relu(Z)
        cache = (linear_cache, activation_cache)
        return A, cache
    def L_model_forward(self,X, parameters):
        caches = []
        A = X
        L = len(parameters) // 2  # number of layers in the neural network
        for l in range(1, L):
            A_prev = A
            A, cache = self.linear_activation_forward(A_prev, parameters['W' + str(l)], parameters['b' + str(l)],activation="relu")
            caches.append(cache)
        AL, cache = self.linear_activation_forward(A, parameters['W' + str(L)], parameters['b' + str(L)], activation="sigmoid")
        caches.append(cache)
        return AL, caches
    def compute_cost(self,AL, Y):
        m = 1
        # Compute loss from aL and y.
        cost = (1. / m) * (-np.dot(Y, np.log(AL).T) - np.dot(1 - Y, np.log(1 - AL).T))
        cost = np.squeeze(cost)
        return cost
    def linear_backward(self,dZ, cache):
        A_prev, W, b = cache
        m = 1
        dW = 1. / m * np.dot(dZ, A_prev.T)
        db = 1. / m * np.sum(dZ, axis=1, keepdims=True)
        dA_prev = np.dot(W.T, dZ)
        return dA_prev, dW, db
    def linear_activation_backward(self,dA, cache, activation):
        linear_cache, activation_cache = cache
        if activation == "relu":
            dZ = self.relu_backward(dA, activation_cache)
            dA_prev, dW, db = self.linear_backward(dZ, linear_cache)
        elif activation == "sigmoid":
            dZ = self.sigmoid_backward(dA, activation_cache)
            dA_prev, dW, db = self.linear_backward(dZ, linear_cache)
        return dA_prev, dW, db
    def L_model_backward(self,AL, Y, caches):
        grads = {}
        L = len(caches)
        m = 1
        Y = Y.reshape(AL.shape)
        dAL = - (np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))
        current_cache = caches[-1]
        dA_prev_temp, dW_temp, db_temp = self.linear_activation_backward(dAL, current_cache, 'sigmoid')
        grads["dA" + str(L - 1)] = dA_prev_temp
        grads["dW" + str(L)] = dW_temp
        grads["db" + str(L)] = db_temp
        for l in reversed(range(L - 1)):
            current_cache = caches[l]
            dA_prev_temp, dW_temp, db_temp = self.linear_activation_backward(grads["dA" + str(l + 1)], current_cache, 'relu')
            grads["dA" + str(l)] = dA_prev_temp
            grads["dW" + str(l + 1)] = dW_temp
            grads["db" + str(l + 1)] = db_temp
        return grads
    def update_parameters(self,parameters, grads, learning_rate):
        L = len(parameters) // 2  # number of layers in the neural network
        for l in range(L):
            parameters["W" + str(l + 1)] = parameters["W" + str(l + 1)] - learning_rate * grads["dW" + str(l + 1)]
            parameters["b" + str(l + 1)] = parameters["b" + str(l + 1)] - learning_rate * grads["db" + str(l + 1)]
        return parameters
    def L_layer_model(self,X, Y,learning_rate=0.0075):  # lr was 0.009
        AL, caches = self.L_model_forward(X, self.parameters)
        cost = self.compute_cost(AL, Y)
        grads = self.L_model_backward(AL, Y, caches)
        self.parameters = self.update_parameters(self.parameters, grads, learning_rate)
        return cost
new=Neuron_Network([12288,20,7,5,1])
train_x_orig, train_y, test_x_orig, test_y, classes = new.load_data()
# Reshape the training and test examples
train_x_flatten = train_x_orig.reshape(train_x_orig.shape[0], -1).T   # The "-1" makes reshape flatten the remaining dimensions
test_x_flatten = test_x_orig.reshape(test_x_orig.shape[0], -1).T
# Standardize seq.txt to have feature values between 0 and 1.
train_x = train_x_flatten / 255.
test_x = test_x_flatten / 255.
m=[]
special=np.array(train_x).reshape(209,12288)
for x in range(np.array(special).shape[0]):
    x=np.array(special[x]).reshape(12288,1)
    m.append(x)
for x in range(0,10000):
    num=random.randint(0,208)
    cost = new.L_layer_model(m[num], train_y[0][num],learning_rate=0.01)
    if x % 100 == 0:
        print("Cost after iteration %i: %f" % (x, cost))
        new.costs.append(cost)
plt.plot(np.squeeze(new.costs))
plt.ylabel('cost')
plt.xlabel('iterations (per tens)')
plt.title("Learning rate =" + str(0.0075))
plt.show()



train_set_x_orig=np.array(train_x_orig)
train_set_y=np.array(train_y).reshape(209,1)
x=np.array(train_set_x_orig)
x_flat=x.reshape(64*64*3,209)
x_flat=np.array(x_flat).transpose()
traing=[]
for x,y in zip(x_flat,train_set_y):
    traing.append((np.array(x).reshape(12288,1)/255.,y))
test_set_x_orig=np.array(test_x_orig)
test_set_y=np.array(test_y).reshape(50,1)
x=np.array(test_set_x_orig)
x_flat=x.reshape(64*64*3,50)
x_flat_test=np.array(x_flat).transpose()
traing_1=[]
for x,y in zip(x_flat_test,test_set_y):
    traing_1.append((np.array(x).reshape(12288,1)/255.,y))
while True:
    num=int(input('type number'))
    if num==100:
        break
    plt.matshow(train_x_orig[num])
    plt.show()
    p=new.predict(traing[num][0],traing[num][1],new.parameters)
