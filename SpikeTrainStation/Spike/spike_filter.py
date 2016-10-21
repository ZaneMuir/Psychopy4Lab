#!/usr/bin/env python
#encoding:utf-8
#
#
#
#
#

#
#
#

import os, sys, re

time_step = 1.0

#
# spike_filter()
# output:
## dict -> counter{t_tag:count}
## void -> output data into file{{out_file}}
#
# input:
## in_file -> input spike train file path
## out_file -> output spike train count file path
## t_step -> time difference
## limit -> range for counting
#
def spike_filter(in_file, t_step=1.0, limit=99999, out_file=None):
    
    spike_train = get_spike_train(in_file)
    #TEST:    print 'spike train',spike_train

    cursor = 0
    counter = {}
    for spike in spike_train:
        while cursor < float(spike):
            cursor += t_step
            counter[cursor]=0
        try:
            counter[cursor] += 1
        except KeyError:
            counter[cursor] = 1
        if cursor >= limit:
            break
    #TEST:print counter

    if out_file is not None:
        f = open(out_file, 'w')
        for key, value in counter.items():
            f.write(str(key)+','+str(value)+'\n')
        print 'wrote file:', out_file
    return counter

def get_spike_train(in_file):
    f = open(in_file,'r')
    data = f.read()
    f.close()

    trains = re.split(r',',re.split(r'\n',data)[0])

    return trains



if __name__ == '__main__':
    try:
        if os.path.isfile(sys.argv[1]):
            spike_file_path = sys.argv[1]
        else:
            print 'invalid file path',sys.argv[1]
            exit(1)
    except IndexError:
        spike_file_path = None
        print 'need a file path'
        exit(1)

    try:
        result_file_path = sys.argv[2]
    except IndexError:
        result_file_path = None
        
    print spike_filter(spike_file_path, t_step=time_step, out_file=result_file_path)
