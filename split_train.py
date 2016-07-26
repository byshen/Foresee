import numpy as np

def method1():
    exp = 'exp1'
    with open('./%s/%s_all' % (exp, exp), 'r') as f:
        lines = f.readlines()
        length = len(lines)
        #print length
    print length
    # print lines[0]

    train_size = int(0.7 * length)
    test_size = length - train_size

    print train_size, test_size

    f_train =  open('./%s/%s_train' % (exp, exp), 'w')
    f_test = open('./%s/%s_test' % (exp, exp), 'w')

    # divide by time and size

    for i in range(train_size):
        f_train.write(lines[i])
    for i in range(test_size):
        f_test.write(lines[i + train_size])


if __name__ == '__main__':
    # method1()
    arr = np.loadtxt('exp1/exp1_all')
    print arr[:, 0]