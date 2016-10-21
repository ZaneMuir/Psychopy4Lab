#!/usr/bin/env python
#encoding:utf-8

import os, sys, re

def timeSwitch(excel_time):
    return (excel_time-19-70*365)*86400

def getCorridorTime(file_path):
    #open corridor file
    f = open(file_path,'r')
    data = f.read()
    f.close()

    tv_str_ = re.split(r';',re.split(r'\n',data)[2])[0]
    # USING DOS ENCODING, ELIMINATE '\x00'
    tv_str =''
    for char in tv_str_:
        if char != '\x00':
            tv_str += char

    T_v = timeSwitch(float(tv_str))

    return T_v

if __name__ == '__main__':
    #test
    print getCorridorTime(sys.argv[1])
    print type(getCorridorTime(sys.argv[1]))
