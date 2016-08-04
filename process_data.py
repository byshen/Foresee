import fileinput
import numpy as np

exp = 'exp13'
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

f_exp = open('%s/%s_all' % (exp, exp) , 'w')
fname = './frank/%s.dataop.docker.savi.raw-metrics.data' % exp
fname13 = '/home/handsome/Foresee/frank/exp13.legis.docker.savi.raw-metrics.data'

with open(fname13,'r') as file:
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
        # for exp 01
        #f_exp.write('\t'.join([items[11], items[12],items[13],items[9],items[7],items[8],items[25], items[29], items[17], items[21]]) + '\n')
        # for exp 03 - 07
        # arrival rate and # containers
        # arrival rate, throughput, response time, cpu_web, cpu_sql, cpu_load, mem_web, mem_mysql, mem_load, #of containers.
        '''
        f_exp.write('\t'.join(
            [items[10], items[11], items[12], items[8], items[6], items[7], items[16],
             items[20], items[85]]) + '\n')
        '''
        # for exp 13
        '''
        - Given the "ArrivalRate", "# Web Containers" and "# Spark Containers", predict
       - Response Time
       - CPU Utilization for Web Workers (avg) containers
       - CPU Utilization for Spark Workers (avg) containers
       - Throughput
       - Memory utilization for Web Workers (avg) containers => worker 1
       - Memory utilization for Spark Workers (avg) containers => spark master
       - VMs CPU and MEM utilization are swarms
        '''
        f_exp.write('\t'.join(
            [items[20], items[12],items[13], items[22], items[18], items[16], items[21], items[74], items[26], items[3], items[4], items[5], \
             items[8], items[9], items[10]]) + '\n')
