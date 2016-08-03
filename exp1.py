import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


import tensorflow.contrib.learn as skflow
from sklearn import datasets, metrics

all = np.loadtxt('exp01/exp01_train')

global iter

def get_batch(iter, x_data=[], y_data=[]):
    x_data = all[:, 0]  # arrival rate
    y_data = all[:, 1:10]  # response time
    x_data = np.reshape(x_data, (len(x_data), 1))
    y_data = np.reshape(y_data, (len(y_data), 9))
    iter = iter % len(x_data)

    resx = x_data[iter, :]
    resy = y_data[iter, :]

    resx = np.reshape(resx, (1, 1))
    resy = np.reshape(resy, (1, 9))
    return resx, resy

def add_layer(inputs, in_size, out_size, activation_function=None):
    # add one more layer and return the output of this layer
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name = 'W')
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name = 'b')
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases, name='add')

        with tf.name_scope('activation'):
            if activation_function is None:
                outputs = Wx_plus_b
            else:
                outputs = activation_function(Wx_plus_b)
        return outputs


def main():
    all = np.loadtxt('exp01/exp01_train')

    x_data = all[:, 0]  # arrival rate
    y_data = all[:, 1:10]  # response time
    x_data = np.reshape(x_data, (len(x_data), 1))
    y_data = np.reshape(y_data, (len(y_data), 9))

    # define placeholder for inputs to network
    with tf.name_scope('inputs'):
        xs = tf.placeholder(tf.float32, [None, 1], name = 'x_input')
        ys = tf.placeholder(tf.float32, [None, 9], name = 'y_label')
    # add hidden layer


    l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
    # add output layer
    prediction = add_layer(l1, 10, 9, activation_function=None)

    # the error between prediction and real data
    with tf.name_scope('loss'):
        loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))
    with tf.name_scope('train'):
        train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    # important step
    init = tf.initialize_all_variables()
    sess = tf.Session()
    writer = tf.train.SummaryWriter("logs/", sess.graph)
    sess.run(init)

    for i in range(20):
        # training
        sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
        if i % 10 == 0:
            # to see the step improvement
            print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
            prediction_value = sess.run(prediction, feed_dict={xs: x_data})

    test = np.loadtxt('exp01/exp01_test')

    x_test = test[:, 0]  # arrival rate
    y_test = test[:, 1:10]  # response time
    x_test = np.reshape(x_test, (len(x_test), 1))
    y_test = np.reshape(y_test, (len(y_test), 9))

    prediction_value = sess.run(prediction, feed_dict={xs: [[1]]})
    np.savetxt("pre.txt", prediction_value)

if __name__ == '__main__':
    main()