import tensorflow as tf
import h5py
import numpy as np
import matplotlib.pyplot as plt
from Deep_learning_AI.build_nn_from_scratch import dnn_app_utils

test_dataset=h5py.File('test_catvnoncat.h5','r')
train_dataset=h5py.File('train_catvnoncat.h5','r')

x_train=tf.data.Dataset.from_tensor_slices(train_dataset['train_set_x'])
y_train=tf.data.Dataset.from_tensor_slices(train_dataset['train_set_y'])

x_test=tf.data.Dataset.from_tensor_slices(test_dataset['test_set_x'])
y_test=tf.data.Dataset.from_tensor_slices(test_dataset['test_set_y'])


# images_iter = iter(x_train)
# labels_iter = iter(y_train)
# plt.figure(figsize=(10, 10))
# for i in range(25):
#     ax = plt.subplot(5, 5, i + 1)
#     plt.imshow(next(images_iter).numpy().astype("uint8"))
#     plt.title(next(labels_iter).numpy().astype("uint8"))
#     plt.axis("off")
# plt.show()
def normalize(image):
    image= tf.cast(image, tf.float32)/255.0
    image= tf.reshape(image,[-1,])
    return image

new_train=x_train.map(normalize)
new_test=x_test.map(normalize)

def sigmoid(z):
    z = tf.cast(z, tf.float32)
    a = tf.keras.activations.sigmoid(z)
    return a
def one_hot_matrix(label, depth=2):
    """
    Arguments:
            label --  (int) Categorical labels
            depth --  (int) Number of different classes that label can take
    Returns:
             one_hot -- tf.Tensor A single-column matrix with the one hot encoding.
        """
    one_hot = tf.one_hot(label, depth, axis=0)
    one_hot = tf.reshape(one_hot, (-1,))
    return one_hot
new_y_test=y_test.map(one_hot_matrix)
new_y_train=y_train.map(one_hot_matrix)
def initialize_parameters(layer_dims):
    initializer=tf.keras.initializers.GlorotNormal(seed=1)
    parameters = {}
    L = len(layer_dims)  # number of layers in the network

    for l in range(1, L):
        parameters['W' + str(l)] = tf.Variable(initializer(shape=(layer_dims[l],layer_dims[l-1])))
        parameters['b' + str(l)] = tf.Variable(initializer(shape=(layer_dims[l],1)))
    return parameters
#forward_prop
def forward_propagation(X, parameters):
    A=X
    L = len(parameters) // 2
    for l in range(1,L):
        Z= tf.math.add(tf.linalg.matmul(parameters['W'+str(l)],A),parameters['b'+str(l)])
        A= tf.keras.activations.relu(Z)
    ZL=tf.math.add(tf.linalg.matmul(parameters['W'+str(L)],A),parameters['b'+str(L)])
    return ZL


def compute_cost(logits, labels):
    """
    Computes the cost

    Arguments:
    logits -- output of forward propagation (output of the last LINEAR unit), of shape (6, num_examples)
    labels -- "true" labels vector, same shape as Z3

    Returns:
    cost - Tensor of the cost function
    """
    cost = tf.reduce_mean(tf.reduce_mean(tf.maximum(logits, 0) - logits * labels + tf.math.log(1 + tf.math.exp(-abs(logits))), axis=-1))
    # cce = tf.keras.losses.CategoricalCrossentropy(
    #     from_logits=False,reduction=tf.keras.losses.Reduction.SUM)
    # cost=cce(logits, labels).numpy()
    return cost

def model(X_train, Y_train, X_test, Y_test,layer_dim, learning_rate = 0.0001,
          num_epochs = 1500, minibatch_size = 32, print_cost = True):
    costs = []  # To keep track of the cost
    train_acc = []
    test_acc = []

    parameters = initialize_parameters(layer_dim)
    L=len(parameters)//2
    optimizer=tf.keras.optimizers.Adam(learning_rate)

    # The CategoricalAccuracy will track the accuracy for this multiclass problem
    test_accuracy = tf.keras.metrics.CategoricalAccuracy()
    train_accuracy = tf.keras.metrics.CategoricalAccuracy()

    dataset = tf.data.Dataset.zip((X_train, Y_train))
    test_dataset = tf.data.Dataset.zip((X_test, Y_test))

    # We can get the number of elements of a dataset using the cardinality method
    m = dataset.cardinality().numpy()

    minibatches = dataset.batch(minibatch_size).prefetch(8)
    test_minibatches = test_dataset.batch(minibatch_size).prefetch(8)

    for epoch in range(num_epochs):
        epoch_cost=0
        train_accuracy.reset_states()
        for (minibatch_X, minibatch_Y) in minibatches:
            with tf.GradientTape() as tape:
                # 1. predict
                Z3 = forward_propagation(tf.transpose(minibatch_X), parameters)

                # 2. loss
                minibatch_cost = compute_cost(Z3, tf.transpose(minibatch_Y))

            # We accumulate the accuracy of all the batches
            train_accuracy.update_state(minibatch_Y, tf.transpose(Z3))
            trainable_variables = []
            for l in range(1,L+1):
                trainable_variables.append(parameters['W' + str(l)])
                trainable_variables.append(parameters['b' + str(l)])

            grads = tape.gradient(minibatch_cost, trainable_variables)

            optimizer.apply_gradients(zip(grads, trainable_variables))
            epoch_cost += minibatch_cost
        epoch_cost /= m

        # Print the cost every 10 epochs
        if print_cost == True and epoch % 10 == 0:
            print("Cost after epoch %i: %f" % (epoch, epoch_cost))
            print("Train accuracy:", train_accuracy.result())

            # We evaluate the test set every 10 epochs to avoid computational overhead
            for (minibatch_X, minibatch_Y) in test_minibatches:
                Z3 = forward_propagation(tf.transpose(minibatch_X), parameters)
                test_accuracy.update_state(minibatch_Y, tf.transpose(Z3))
            print("Test_accuracy:", test_accuracy.result())

            costs.append(epoch_cost)
            train_acc.append(train_accuracy.result())
            test_acc.append(test_accuracy.result())
            test_accuracy.reset_states()

    return parameters, costs, train_acc, test_acc
layer=[12288, 25, 12, 6]
layer_cat=[12288, 64, 32,32, 2]
parameter, costs, train_acc, test_acc = model(new_train, new_y_train, new_test, new_y_test, num_epochs=50,layer_dim=layer_cat)

dnn_app_utils.predict(new_test, new_y_test, parameter)
# Plot the train accuracy
plt.plot(np.squeeze(train_acc))
plt.ylabel('Train Accuracy')
plt.xlabel('iterations (per fives)')
plt.title("Learning rate =" + str(0.0001))
# Plot the test accuracy
plt.plot(np.squeeze(test_acc))
plt.ylabel('Test Accuracy')
plt.xlabel('iterations (per fives)')
plt.title("Learning rate =" + str(0.0001))
plt.show()





