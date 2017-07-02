#/usr/bin/env python
#encoding:utf-8
#
#  Created by Zane Muir
#  Copyright (c) 2016 ZaneMuir. All rights reserved.
#

import re, os
import csv
import IDClass
import numpy as np

def dataSplit(strdata):
    #format strdata into float spike train data
    temp = re.split(r'\t',re.split(r'\n',strdata)[1])[2]
    temp = re.split(r',',temp)
    data = []
    for item in temp:
        data.append(float(item))
    return data

class Spike(object):
    """docstring for Spike."""
    def __init__(self):
        super(Spike, self).__init__()
        self.ID = None
        self.train = None
        self.spike = None #{time_i : spike_i}

    def setID(self,path):
        level3 = re.findall(r'.*?(\d{1,2})\.txt',os.path.split(path)[1])[0]
        level2 = re.findall(r'.*?-s(\d{1,2})',os.path.split(os.path.split(path)[0])[1])[0]
        level1 = re.findall(r'(\d{8})-no.*?',os.path.split(os.path.split(path)[0])[1])[0][2:]

        self.ID = IDClass.IDClass(int(level1),int(level2),int(level3))
        return

    def formatSpikes(self, in_path,timeSet = [0,300,1]):
        f = open(in_path,'r')
        strdata = f.read()
        f.close()

        self.setID(in_path)

        self.train = dataSplit(strdata)

        time_stamp = timeSet[0]+timeSet[2]
        count_temp = 0
        count_result = {}

        for spike in self.train:
            if spike <= time_stamp:
                count_temp += 1
            else:
                count_result[time_stamp] = count_temp
                time_stamp += timeSet[2]
                count_temp = 0
                while spike > time_stamp:
                    count_result[time_stamp] = count_temp
                    time_stamp += timeSet[2]

                count_temp += 1

        self.spike = count_result

        return

    def csvSpike(self, out_path):

        with open(os.path.join(out_path,self.ID.getID()+'.csv'),'w') as csvfile:
            fieldnames = ['time', 'spike']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for key,value in self.spike.items():
                writer.writerow({'time':str(key), 'spike':str(value)})

    def arraySpike(self):
        cup = []
        for key, value in self.spike.items():
            cup.append([value])
        return cup
        #return np.array(cup)
