import numpy as np

def method1():
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


def method2(exp):
    with open('./%s/%s_norm' % (exp, exp), 'r') as f:
        lines = f.readlines()
        length = len(lines)
        #print length
    print length
    # print lines[0]

    train_size = int(0.7 * length)
    test_size = length - train_size

    print train_size, test_size

    f_train =  open('./%s/%s_norm_train' % (exp, exp), 'w')
    f_test = open('./%s/%s_norm_test' % (exp, exp), 'w')

    # divide by time and size

    for i in range(train_size):
        f_train.write(lines[i])
    for i in range(test_size):
        f_test.write(lines[i + train_size])

def method3(exp):
    with open('./%s/%s_norm2' % (exp, exp), 'r') as f:
        lines = f.readlines()
        length = len(lines)
        #print length
    print length
    # print lines[0]

    train_size = int(0.7 * length)
    test_size = length - train_size

    print train_size, test_size

    f_train =  open('./%s/%s_norm2_train' % (exp, exp), 'w')
    f_test = open('./%s/%s_norm2_test' % (exp, exp), 'w')

    # divide by time and size

    for i in range(train_size):
        f_train.write(lines[i])
    for i in range(test_size):
        f_test.write(lines[i + train_size])

def mynorm(exp):
    all = np.loadtxt('%s/%s_all' %(exp,exp))

    length = all.shape[0]

    res = np.ones((length, 1))

    for i in range(0, all.shape[1]):
        col = all[:, i]
        max_col = col.max()
        min_col = col.min()
        print col
        # print max_col, min_col
        for j in range(0, length):
            col[j] = (col[j] - min_col) / (max_col - min_col)
        res = np.c_[res, col]
        #res = res[:, 1:all.shape[1]]
    res = np.delete(res, 0, axis=1)
    #print res
    np.savetxt('%s/%s_norm' %(exp,exp), res)

def mynorm2(exp):
    all = np.loadtxt('%s/%s_all_changed' %(exp,exp))

    length = all.shape[0]

    res = np.ones((length, 1))

    for i in range(0, all.shape[1]):
        col = all[:, i]
        max_col = col.max()
        min_col = col.min()
        print col
        # print max_col, min_col
        for j in range(0, length):
            col[j] = (col[j] - min_col) / (max_col - min_col)
        res = np.c_[res, col]
        #res = res[:, 1:all.shape[1]]
    res = np.delete(res, 0, axis=1)
    np.savetxt('%s/%s_norm2' %(exp,exp), res)

def mynorm1_100(exp):
    all = np.loadtxt('%s/%s_all' %(exp,exp))

    length = all.shape[0]

    res = np.ones((length, 1))

    for i in range(0, all.shape[1]):
        col = all[:, i]
        max_col = col.max()
        min_col = col.min()
        # print col
        # print max_col, min_col
        for j in range(0, length):
            col[j] = ((col[j] - min_col) / (max_col - min_col)) * 99 + 1
        res = np.c_[res, col]

    res = np.delete(res, 0, axis=1)
    np.savetxt('%s/%s_norm1_100' %(exp,exp), res)

def re_arrange(exp):
    all = np.loadtxt('%s/%s_all' % (exp,exp))
    for i in range(all.shape[0]):
        all[i][1], all[i][8] = all[i][8], all[i][1]


    np.savetxt('%s/%s_all_changed'%(exp,exp), all)

def spllit_13(exp):
    with open('./%s/%s_norm' % (exp, exp), 'r') as f:
        lines = f.readlines()
        length = len(lines)
        #print length
    print length
    # print lines[0]

    train_size = 129
    test_size = length - train_size

    print train_size, test_size

    f_train =  open('./%s/%s_norm_train' % (exp, exp), 'w')
    f_test = open('./%s/%s_norm_test' % (exp, exp), 'w')

    # divide by time and size

    for i in range(train_size):
        f_train.write(lines[i])
    for i in range(test_size):
        f_test.write(lines[i + train_size])


def random_sample70(exp):
    with open('./%s/%s_norm1_100' % (exp, exp), 'r') as f:
        lines = f.readlines()
        length = len(lines)
        # print length
    print length
    # print lines[0]

    train_size = 0
    test_size = 0

    f_train = open('./%s/%s_norm_1_100_train' % (exp, exp), 'w')
    f_test = open('./%s/%s_norm_1_100_test' % (exp, exp), 'w')

    # divide by time and size
    rand_arr = np.random.randint(0,9,size=length)

    for index in range(length):
        if rand_arr[index] < 7:
            f_train.write(lines[index])
            train_size += 1
        else:
            f_test.write(lines[index])
            test_size += 1

    res = [int(x < 7) for x in rand_arr]
    np.savetxt('%s/%s_divide' % (exp, exp), res)

    print train_size, test_size


if __name__ == '__main__':
    #mynorm2('exp05')
    #method2('exp13')
    #re_arrange('exp07')
    #spllit_13('exp13')
    #method3('exp05')
    #mynorm1_100('exp01')
    random_sample70('exp13')



















