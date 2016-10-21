#!/usr/bin/env python
#encoding:utf-8

import os

def writeSession(time_limit, visual_speed, motor_speed, index, working_dir):
    f = open(os.path.join(working_dir, 's%d/speed.csv'%(index+1)),'w')
    entry =''
    for tick in range((time_limit[1]-time_limit[0])/time_limit[2]):
        entry =''
        entry += str(time_limit[0]+time_limit[2]*tick)+','
        entry += str(visual_speed[tick])+','
        entry += str(motor_speed[tick])+'\n'
        f.write(entry)
    f.close()
