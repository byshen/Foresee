import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt



def get_batch(iter, all, M, N, batch_size, x_data=[], y_data=[]):
    x_data = all[:, 0:M]  # arrival rate
    y_data = all[:, M:N+1]  # response time
    x_data = np.reshape(x_data, (len(x_data), M))
    y_data = np.reshape(y_data, (len(y_data), N))

    iter = iter % len(x_data)

    if iter + batch_size >= len(x_data):
        resx = x_data[iter:len(x_data), :]
        resy = y_data[iter:len(x_data), :]
        for i in range(batch_size + iter - len(x_data)):
            resx = np.r_[np.reshape(resx,(resx.shape[0], M)), \
                         np.reshape(x_data[i, :], (1, M))]
            resy = np.r_[np.reshape(resy,(resy.shape[0], N)), \
                         np.reshape(y_data[i, :], (1, N))]
    else:
        resx = x_data[iter:iter+batch_size, :]
        resy = y_data[iter:iter+batch_size, :]

    resx = np.reshape(resx, (batch_size, M))
    resy = np.reshape(resy, (batch_size, N))
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

def cal_accuracy(arr1, arr2):
    length = arr1.shape[1]
    res = np.zeros(length)

    kuan = arr1.shape[0]
    print arr1.shape
    print arr2.shape

    for i in range(length):
        for j in range(kuan):
            res[i] += abs( (arr1[j][i] - arr2[j][i])/arr1[j][i] )

    res = res/kuan

    print res
    return res



def main(M, N):
    all = np.loadtxt('exp01/exp01_norm_1_100_train')

    x_data = all[:, 0:M]  # arrival rate
    y_data = all[:, M:N+1]  # response time
    x_data = np.reshape(x_data, (len(x_data), M))
    y_data = np.reshape(y_data, (len(y_data), N))

    # define placeholder for inputs to network
    with tf.name_scope('inputs'):
        xs = tf.placeholder(tf.float64, [None, M], name='x_input')
        ys = tf.placeholder(tf.float64, [None, N], name='y_label')
    # add hidden layer
    l1 = add_layer(xs, M, 10, activation_function=tf.nn.relu)
    # add output layer
    l2 = add_layer(l1, 10, 10, activation_function=tf.nn.relu)

    prediction = add_layer(l2, 10, N, activation_function=None)

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

    for i in range(5000):
        # training
        train_x, train_y = get_batch(i, all, M, N, 5, x_data, y_data)

        sess.run(train_step, feed_dict={xs: train_x, ys: train_y})
        if i % 10 == 0:
            # to see the step improvement

            error_loss = sess.run(loss, feed_dict={xs: x_data, ys: y_data})
            print error_loss
            if error_loss < 0.01:
                break

            # prediction_value = sess.run(prediction, feed_dict={xs: x_data})

    test = np.loadtxt('exp01/exp01_norm_1_100_test')

    x_test = test[:, 0:M]  # arrival rate
    y_test = test[:, M:N+1]  # response time
    x_test = np.reshape(x_test, (len(x_test), M))
    y_test = np.reshape(y_test, (len(y_test), N))

    res_predict = np.zeros((1, N))

    for i in range(0, len(x_test)):
        test_batch_x = np.reshape(x_test[i,:], (1,M))
        prediction_value = sess.run(prediction, feed_dict={xs: test_batch_x})
        res_predict = np.row_stack((res_predict, prediction_value))
        print test_batch_x, prediction_value
    res_predict = np.delete(res_predict,0,axis=0)
    print res_predict
    print '------ acc ------'
    print cal_accuracy(y_test, res_predict)
    '''
    prediction_value = sess.run(prediction, feed_dict={xs: x_test})
    for i in range(0,len(x_test)):
        print x_test[i], prediction_value[]
    '''
    np.savetxt("exp01/exp01_1_100_pre_test.txt", res_predict)

if __name__ == '__main__':
    main(1, 5)