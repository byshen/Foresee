import numpy as np

exp = 'exp01'

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


def method2():
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
def mynorm(exp):
    all = np.loadtxt('exp01/exp01_all')

    length = all.shape[0]

    res = np.ones((length, 1))

    for i in range(0, all.shape[1]):
        col = all[:, i]
        max_col = col.max()
        min_col = col.min()

        for j in range(0, length):
            col[j] = (col[j] - min_col) / (max_col - min_col)
        res = np.c_[res, col]
        #res = res[:, 1:all.shape[1]]
    res = np.delete(res, 0, axis=1)
    #print res
    np.savetxt('exp01/exp01_norm', res)

def re_arrange(exp):
    all = np.loadtxt('%s/%s_all' % (exp,exp))
    for i in range(all.shape[0]):
        all[i][1], all[i][8] = all[i][8], all[i][1]


    np.savetxt('%s/%s_all_changed'%(exp,exp), all)

if __name__ == '__main__':
    #mynorm('exp01')
    #method2()
    re_arrange('exp07')






















