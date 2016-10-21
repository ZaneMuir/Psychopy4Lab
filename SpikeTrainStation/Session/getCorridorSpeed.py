 #!/usr/bin/env python
 #encoding:utf-8

import os, re

def timeSwitch(excel_time):
    return (excel_time-19-70*365)*86400

def getCorridorSpeed(file_path,VR_ttl=0,time_limit=(0,300,1)):

    # open path data file
    f = open(file_path, 'r')
    data = f.read()
    f. close()

    pathData = []
    for item in re.split(r'\n', data)[1:]: # exclude the header line
        #exclude the empty line
        if item == '':
            continue


        subitems = re.split(r';',item)
        pathData.append((timeSwitch(float(subitems[0])),float(subitems[2]))) #(time_tag, pos)

    speed = []
    previous_pos = 0
    next_time = time_limit[0]+time_limit[2]
    for item in pathData:
        #print item #FIXME
        #print next_time
        #print item[0]-VR_ttl
        if item[0]-VR_ttl < next_time:
            continue
        else: # when time_point reachs next time point
            speed.append((item[1]-previous_pos)/time_limit[2]/100) #unit: cm/s
            previous_pos = item[1]
            next_time += time_limit[2]

    return speed
