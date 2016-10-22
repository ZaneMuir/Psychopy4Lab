#!/usr/bin/env python
#encoding:utf-8

import os, sys, re
import getFartlekSpeed
#import numpy as np
# sin_wave(time_tag,raw_vel=20,fratlek_seq=[(2,30,)])

corridor_name = r'.*?_Corridor.*?_S\d.*?'
# No.25_Corridor-16.09.26_S1
psychopy_name = r'.*?_psychopy_S.*?'
# No.25_160926_psychopy_S1-4
pathdata_name = r'.*?_PathData_S\d.*?'
# No.25_16.09.22_PathData_S3

time_seq = (0,300,1)
visual_seq = [(2,30,)]

def getCorridorTime(file_path):
    f = open(os.path.join(os.getcwd(),file_path),'r')
    data = f.read()
    f.close()
#    print re.split(r';',re.split(r'\n',data)[2])
    tv_str_ = re.split(r';',re.split(r'\n',data)[2])[0]
    tv_str =''
    for char in tv_str_:
        if char != '\x00':
            tv_str += char
#DEBUG:
#    print tv_str
    T_v = (float(tv_str)-19-70*365)*86400

    return T_v

def getPsychoPyTime(file_path):
    f = open(os.path.join(os.getcwd(),file_path),'r')
    data = f.read()
    f.close()

    T_p = []

    for item in re.split(r'\n',data):
        try:
            T_p.append((float(re.split(r',',item)[1])-19-70*365)*86400)
        except IndexError:
            pass

    return T_p

def timeSwitch(excel_time):
    if type(excel_time) is type('String'):
        temp = excel_time
        excel_time = ''
        for char in temp:
            if char != '\x00':
                excel_time += char
#DEBUG:print excel_time
        try:
            excel_time = float(excel_time)
        except ValueError:
            return 0
    return (excel_time-19-70*365)*86400

def getPathData(index, path_data,time_seq, visual_seq, t_v, t_p):
    f = open(os.path.join(os.getcwd(),path_data),'r')
    data = f.read()
    f.close()

    t_lag = t_v - t_p

    PathData = []
    for each_line in re.split(r'\n',data)[1:]:
        line_item = re.split(r';',each_line)
        try:
            PathData.append((float(timeSwitch(line_item[0]))-t_v,float(line_item[2])))
        except IndexError:
            pass

    speed_data = []

    previous_tag = 0
    previous_pos = 0
    next_tag = 0+time_seq[2]
    next_pos = 0

    for item in PathData:
        if item[0] >= previous_tag:
            previous_pos = item[1]
            previous_tag += time_seq[2]
        if item[0] >= next_tag:
            next_pos = item[1]
            next_tag += time_seq[2]

            speed_data.append((previous_tag,(next_pos-previous_pos)/time_seq[2],fartlek.sin_wave(previous_tag+t_lag,fartlek_seq=visual_seq)))

    return speed_data

def main():
    corridor_time = []
    psychopy_time = []
    pathdata_file = []
    for item in os.listdir(os.getcwd()):
#        print item
        if re.match(corridor_name, item):
            corridor_time.append(getCorridorTime(item))
#    print corridor_files
        if re.match(psychopy_name, item):
            psychopy_time = getPsychoPyTime(item)

        if re.match(pathdata_name, item):
            pathdata_file.append(item)

    for index in range(len(corridor_time)):
        if not os.path.isdir(os.path.join(os.getcwd(),'s'+str(index))):
            os.mkdir(os.path.join(os.getcwd(),'s'+str(index)))
        #DEBUG
        try:
            speed_data = getPathData(index, pathdata_file[index], time_seq, visual_seq, corridor_time[index], psychopy_time[index])
        except IndexError:
            pass

        f = open(os.path.join(os.path.join(os.getcwd(),'s'+str(index)),'speed.csv'),'w')
        for item in speed_data:
            f.write('%s,%s,%s\n'%(str(item[0]),str(item[1]),str(item[2])))
        f.close()

if __name__ == '__main__':
    main()
