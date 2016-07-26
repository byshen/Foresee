import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


learning_rate = 0.1
#softmax (Wx+b)
x = tf.placeholder("float", [None, 1])
y = tf.placeholder("float", [None, 1])

W = tf.Variable(tf.zeros([1, 1]))
b = tf.Variable(tf.zeros([1]))


# activation function
act = tf.nn.softmax(tf.matmul(x, W) + b)

# reduction_indices:  The dimensions to reduce. If None (the default), reduces all dimensions.
cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(act), reduction_indices=1)) # cross entrophy
# squared loss
# cost = tf.reduce_mean(tf.reduce_sum(y - act))

train_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# predict
pred = tf.equal(tf.argmax(act,1), tf.argmax(y,1))

acc = tf.reduce_mean(tf.cast(pred, "float"))


# --------------------- #
init = tf.initialize_all_variables()
print "Graph constructed"

# Lauch session
