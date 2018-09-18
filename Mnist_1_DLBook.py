# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 17:53:20 2018

@author: Tejas_K_Reddy

First and Basic Deep Learning, Character Recognition From mnist database.
"""


## Load the data into respective variables
from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels)= mnist.load_data()

train_images.shape
len(train_labels)

## Build the network
from keras import models
from keras import layers

network = models.Sequential()
network.add(layers.Dense(512, activation ='relu', input_shape=(28*28,))) # or (28,28)
network.add(layers.Dense(10, activation = 'softmax'))

# Compile 
network.compile(optimizer='rmsprop', loss= 'categorical_crossentropy', metrics=['accuracy'])

# Preprocessing the data
train_images = train_images.reshape((60000, 28*28))
train_images = train_images.astype('float32')/255     # converting uint8 to double
#normalising the pixel values in the range [0, 1].
test_images = test_images.reshape((10000, 28*28))
test_images = test_images.astype('float32')/255     # converting uint8 to double

# Preparing the label
from keras.utils import to_categorical

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# fit the model
network.fit(train_images, train_labels, epochs=5, batch_size=128)

# Calculate accuracy and loss
test_loss, test_accuracy = network.evaluate(test_images, test_labels)
print(test_accuracy)

############################################################done with program.
## Load the data into respective variables
from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels)= mnist.load_data()

# Check Image Details
print(train_images.dtype)

# Display 7th image
digit_to_display = train_images[7]

import matplotlib.pyplot as plt
plt.figure(1)
plt.imshow(digit_to_display, cmap = plt.cm.binary)
plt.show()

#Dividing the database into batches
s
batch1= train_images[:128]
batch2 = train_images[128:256] #256 not included
batchn = train_images[128*n:128*(n+1)]



