import fileinput
import numpy as np

exp = 'exp1'
'''
f_arrival = open('%s_arrival_rate' % exp, 'w')
f_through_put = open('%s_through_put' % exp, 'w')
f_response_time = open('%s_response_time' % exp, 'w')
f_cpu_web = open('%s_cpu_web' % exp, 'w')
f_cpu_mysql = open('%s_cpu_mysql' % exp, 'w')
f_cpu_load = open('%s_cpu_load' % exp, 'w')
f_mem_web1 = open('%s_mem_web1' % exp, 'w')
f_mem_web2 = open('%s_mem_web2' % exp, 'w')
f_mem_mysql = open('%s_mem_mysql' % exp, 'w')
f_mem_load = open('%s_mem_load' % exp, 'w')
'''
f_exp = open('%s_all' % exp, 'w')
with open('./frank/exp01.dataop.docker.savi.raw-metrics.data','r') as file:
    lines = file.readlines()

    for index, line in enumerate(lines):
        if line[0] == '#':
            continue
        items = line.split()
        #print items
        '''
        f_arrival.write(items[11] + '\n')
        f_through_put.write(items[12] + '\n')
        f_response_time.write(items[13] + '\n')
        f_cpu_web.write(items[9] + '\n')
        f_cpu_mysql.write(items[7] + '\n')
        f_cpu_load.write(items[8] + '\n')
        f_mem_web1.write(items[25] + '\n')
        f_mem_web2.write(items[29] + '\n')
        f_mem_mysql.write(items[17] + '\n')
        f_mem_load.write(items[21] + '\n')
        '''
        f_exp.write('\t'.join([items[11], items[12],items[13],items[9],items[7],items[8],items[25], items[29], items[17], items[21]]) + '\n')
