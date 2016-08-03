'''
@author: byshen
@date: 2016.07.24
impliment basic logistic regression classifier
'''
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


import tensorflow.contrib.learn as skflow
from sklearn import datasets, metrics


def add_layer(inputs, in_size, out_size, activation_function=None):
    # add one more layer and return the output of this layer
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

all = np.loadtxt('exp01/exp01_all')


x_data = all[:, 0]  # arrival rate
y_data = all[:, 1:10]  # response time
x_data = np.reshape(x_data, (len(x_data), 1))
y_data = np.reshape(y_data, (len(y_data), 9))

# define placeholder for inputs to network
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 9])
# add hidden layer
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
# add output layer
prediction = add_layer(l1, 10, 9, activation_function=None)

# the error between prediction and real data
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# important step
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)



for i in range(1000):
    # training
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 10 == 0:
        # to see the step improvement
        print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
    	prediction_value = sess.run(prediction, feed_dict={xs: x_data})
