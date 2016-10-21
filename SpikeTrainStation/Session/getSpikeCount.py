#!/usr/bin/env python
#encoding:utf-8

import os, re

def getSpikeCount(summary_path):

    # open summary.csv file
    f = open(summary_path,'r')
    data = f.read()
    f.close()

    spike_data = []

    for item in re.split(r'\n',data)[1:]: #exclude the header line

        if item == '':
            # exclude empty line
            continue
        subitems = re.split(r',',item)
        spike_data_item = (float(subitems[0]),float(subitems[-2])) #(time_tag, average_spike)
        spike_data.append(spike_data_item)

    return spike_data

if __name__ == '__main__':
    #test
    import sys
    print getSpikeCount(sys.argv[1])
