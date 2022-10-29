import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow.keras.layers as tfl
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.layers.experimental.preprocessing import RandomFlip, RandomRotation
def data_augmenter():
    data_argument=tf.keras.Sequential()
    data_argument.add(RandomFlip('horizontal'))
    data_argument.add(RandomRotation(0.2))
BATCH_SIZE=32
IMG_SIZE=(160,160)
directory='dataset/'
train_data_set=image_dataset_from_directory(directory,shuffle=True,batch_size=BATCH_SIZE,image_size=IMG_SIZE,validation_split=0.2,
                                            subset='training',seed=42)
test_data_set=image_dataset_from_directory(directory,shuffle=True,batch_size=BATCH_SIZE,image_size=IMG_SIZE,validation_split=0.2,
                                            subset='validation',seed=42)
IMG_SHAPE = IMG_SIZE + (3,)
base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,
                                               include_top=True,
                                               weights='imagenet')
# image_batch, label_batch = next(iter(train_data_set))
# feature_batch = tf.Variable(image_batch)
# pred = base_model(feature_batch)
# print(tf.keras.applications.mobilenet_v2.decode_predictions(pred.numpy(), top=2))
# base_model.trainable=False


def alpaca_model(image_shape=IMG_SIZE, data_augmentation=data_augmenter()):
    ''' Define a tf.keras model for binary classification out of the MobileNetV2 model
    Arguments:
        image_shape -- Image width and height
        data_augmentation -- seq.txt augmentation function
    Returns:
    Returns:
        tf.keras.model
    '''

    input_shape = image_shape + (3,)

    ### START CODE HERE

    base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,
                                                   include_top=False,  # <== Important!!!!
                                                   weights='imagenet')  # From imageNet

    # freeze the base model by making it non trainable
    base_model.trainable = False
    # create the input layer (Same as the imageNetv2 input size)
    inputs = tf.keras.Input(shape=input_shape)
    # apply seq.txt augmentation to the inputs
    # seq.txt preprocessing using the same weights the model was trained on
    preprocess_input = tf.keras.applications.mobilenet_v2.preprocess_input
    x = preprocess_input(inputs)
    # set training to False to avoid keeping track of statistics in the batch norm layer
    x = base_model(x, training=False)
    # add the new Binary classification layers
    # use global avg pooling to summarize the info in each channel
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    # include dropout with probability of 0.2 to avoid overfitting
    x = tfl.Dropout(.2)(x)
    # use a prediction layer with one neuron (as a binary classifier only needs one)
    outputs = tf.keras.layers.Dense(1)
    outputs = outputs(x)
    model = tf.keras.Model(inputs, outputs)
    return model
model2 = alpaca_model(IMG_SIZE)
print(model2.summary())
base_learning_rate = 0.001
model2.compile(optimizer=tf.keras.optimizers.Adam(lr=base_learning_rate),
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])
initial_epochs = 5
history = model2.fit(train_data_set, validation_data=train_data_set, epochs=initial_epochs)