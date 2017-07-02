#/usr/bin/env python
#encoding:utf-8
#
#  Created by Zane Muir
#  Copyright (c) 2016 ZaneMuir. All rights reserved.
#

import csv
import re, os
import getFartlekSpeedx
import IDClass
import numpy as np

psychopy_name = r'.*?psychopy.*?'

def timeSwitch(excel_time,origin=0.0):
    return (excel_time-19-70*365)*86400-origin

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

def getPsychoPyTime(dir_path, session = 1,psychopy_regr=psychopy_name):
    #open psychopy time recording file
    file_path = None
    for item in os.listdir(dir_path):
        # print item
        if re.match(psychopy_regr,item):
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

    return T_p[session]

def fartlek(time_tag,v_0=20,fartlek_seq=[(2,30,)]):
    time_set = 0
    for seq_item in fartlek_seq:
        try:
            current_seq_time = seq_item[2]
        except IndexError:
            current_seq_time = 9999

        time_set += current_seq_time

        if time_tag < time_set:
            v_x = v_0*seq_item[0]**math.sin(2*math.pi/seq_item[1]*(time_tag+current_seq_time-time_set))
            #
            #equation:
            #v(x) = v_0 * A^{sin(2*pi/T*x)}
            #
            return v_x
        else:
            #debug_counter += 1
            continue



class Speed(object):
    """docstring for Speed."""
    def __init__(self):
        super(Speed, self).__init__()
        self.ID = None
        self.Motor = None
        self.corridorStart = None
        self.Visual = None

    def setID(self,path):
        level1_ = re.findall(r'.*?_(.*?)_PathData_S\d\.csv',os.path.split(path)[1])[0]
        temp = re.split(r'\.',level1_)
        level1 = '%s%s%s'%(temp[0],temp[1],temp[2])
        #print level1
        level2 = re.findall(r'.*?_.*?_PathData_S(\d)\.csv',os.path.split(path)[1])[0]
        #print level2
        self.ID = IDClass.IDClass(int(level1),int(level2),None)
        return

    def formatSpeed(self,csvPath, corridorPath, timeSet = [0,300,1],fartlek_seq=[(2,30,)]):
        self.setID(csvPath) #设置ID号
        self.formatMotor(csvPath,corridorPath,timeSet=timeSet) #处理运动速度
        self.formatVisual(os.path.split(csvPath)[0],timeSet=timeSet,fartlek_seq=fartlek_seq) #处理视觉速度

    def formatMotor(self,csvPath ,corridorPath ,timeSet = [0,300,1]):
        raw_data = []

        self.corridorStart = getCorridorTime(corridorPath) #获得VR系统开始运行的时刻点

        with open(csvPath,'r') as csvfile:
            #获得PathData的数据，主要获取其中的DateTime，xPosComp，yPosComp数据，并写入raw_data中保存
            reader = csv.DictReader(csvfile,delimiter=';')
            for row in reader:
                raw_data.append((timeSwitch(float(row['DateTime']),self.corridorStart),float(row['xPosComp']),float(row['yPosComp'])))

        time_stamp = timeSet[0]+timeSet[2]
        previous_pos = raw_data[0][2]
        speed_result = {}

        for point in raw_data:
            #计算指定时间间隔的位移，并以起点和终点的位置计算对应的算术平均速度。单位为厘米每秒。
            if point[0] >= time_stamp:
                #NOTE: the speed algorithm: ignore the xPosComp
                speed = (point[2]-previous_pos)/timeSet[2]/100
                speed_result[int(time_stamp)] = speed
                previous_pos = point[2]
                time_stamp += timeSet[2]

                if time_stamp > timeSet[1]:
                    break

        self.Motor = speed_result

    def formatVisual(self, work_dir, timeSet=[0,300,1],fartlek_seq=[(2,30,)]):
        #计算PsychoPy的启动时间和VR启动时间的差值
        time_setoff = self.corridorStart - timeSwitch(getPsychoPyTime(work_dir,int(self.ID.getLevel2())-1))
        speed_result = {}
        for time_tag in range(timeSet[0],timeSet[1]-timeSet[2],timeSet[2]):
            speed = getFartlekSpeedx.fartlek(time_setoff+time_tag+0.5,fartlek_seq=fartlek_seq) #调用Fartlek函数
            #print speed
            speed_result[time_tag+1] = speed

        self.Visual = speed_result

    def csvSpeed(self, out_path):
        #输出运动数据
        with open(os.path.join(out_path,self.ID.getSessionID()+'.csv'),'w') as csvfile:
            fieldnames = ['time', 'visual','motor']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            #TODO::
            #for key,value in self.Visual.items():
            #    writer.writerow({'time':str(key), 'visual':str(value), 'motor':self.Motor[key+1]})

    def arrayMotor(self):
        #格式化数据，以进行scikitlearn的算法和pyplot的算法
        cup = []
        for key, value in self.Motor.items():
            cup.append([value])
        return cup
        #return np.array(cup)

    def arrayVisual(self):
        #格式化数据，以进行scikitlearn的算法和pyplot的算法
        cup = []
        for key, value in self.Visual.items():
            cup.append([value])
        return cup
        #return np.array(cup)
