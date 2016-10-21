#!/usr/bin/env python
#encoding:utf-8

import os, re
psychopy_name = r'.*?psychopy.*?'

def timeSwitch(excel_time):
    return (excel_time-19-70*365)*86400

def getPsychoPyTime(dir_path):
    #open psychopy time recording file
    file_path = None
    for item in os.listdir(dir_path):
        # print item 
        if re.match(psychopy_name,item):
            file_path = os.path.join(dir_path,item)

    if file_path == None:
        raise IOError('no psychopy time tag file!')

    f = open(file_path,'r')
    data = f.read()
    f.close()

    T_p = []

    for item in re.split(r'\n',data):
        #split data into each session,

        #NB: the last line is empty
        if item is '':
            continue

        T_p.append(timeSwitch(float(re.split(r',',item)[1])))

    return T_p

if __name__ == '__main__':
    import sys
    #test
    print getPsychoPyTime(sys.argv[1])
