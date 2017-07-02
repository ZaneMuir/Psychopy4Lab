#/usr/bin/env python
#encoding:utf-8
#  Created by Zane Muir
#  Copyright (c) 2016 ZaneMuir. All rights reserved.
#

import os,re
import json, csv
from container import spike,speed
from summary import neuron
import math

setting_path = '/Users/zane/Desktop/ProjectE/Psychopy4Lab/SpikeStation/setting.json'
#TODO: 将setting的内容用json的格式保存与修改。
setting ={
"fartlek":[(2,30,30),(1.5,60,30),(1.5,30,30),(1,60,30),(2,30,30),(2,30,30),(1.5,60,30),(1.5,30,30),(1,60,30),(2,30,30),(2,30,)],
"time_limit":[0,300,1],
"raw_channel_regr":r'\d{8}-.*?-s\d{1,2}',
"train_regr":r'PSTH Ch\d{1,2}\.txt',
"psychopy_name":r'.*?psychopy.*?',
"corridor_name":r'.*?Corridor.*?',
"pathdata_name":r'.*?PathData.*?'

}


def getChannel(working_dir=os.getcwd()):
    global setting
    channel_files = []
    for item in os.listdir(working_dir):
        if re.match(setting['raw_channel_regr'],item):
            channel_files.append(item)
    return channel_files

def getSession(ch_file,working_dir=os.getcwd()):
    global setting
    ch_dir = os.path.join(working_dir,ch_file)
    session_files = []
    for item in os.listdir(ch_dir):
        if re.match(setting['train_regr'],item):
            session_files.append(item)
    return session_files

def getSetting(path):
    with open(path,'r') as jsonfile:
        return json.loads(jsonfile.read())

def getCorridorFileNames(target_dir=os.getcwd()):
    global setting
    corridorFileNames = []
    for item in os.listdir(target_dir):
        if re.match(setting["corridor_name"],item):
            corridorFileNames.append(item)
    return corridorFileNames

def getPathDataFileNames(target_dir=os.getcwd()):
    global setting
    pathDataFileNames = []
    for item in os.listdir(target_dir):
        if re.match(setting["pathdata_name"],item):
            pathDataFileNames.append(item)
    return pathDataFileNames



def main(work_dir=os.getcwd()):
    #setting = getSetting(setting_path)
    global setting

########################## Spike Train #########################################
    channels = getChannel(work_dir)
    spike_pool = {}

    #print channels

    for each_channel in channels:
        sessions = getSession(each_channel,work_dir)

        #print sessions

        for each_session in sessions:
            spike_temp = spike.Spike()
            spike_temp.formatSpikes(os.path.join(os.path.join(os.getcwd(),each_channel),each_session))
            if not os.path.isdir(os.path.join(os.getcwd(),'ch'+str(spike_temp.ID.lvl3))):
                os.mkdir(os.path.join(os.getcwd(),'ch'+str(spike_temp.ID.lvl3)))
            spike_temp.csvSpike(os.path.join(os.getcwd(),'ch'+str(spike_temp.ID.lvl3)))
            spike_pool[spike_temp.ID.getID()] = spike_temp
    print 'total spike count is:',len(spike_pool)
################################################################################

################################ Speed #########################################
    corridorFileNames = getCorridorFileNames(work_dir)
    pathDataFileNames = getPathDataFileNames(work_dir)

    session_pool = {}

    for index in range(len(pathDataFileNames)):
        s_temp = speed.Speed()
        s_temp.formatSpeed(os.path.join(work_dir,pathDataFileNames[index]),os.path.join(work_dir,corridorFileNames[index]),timeSet=setting['time_limit'],fartlek_seq=setting['fartlek'])
        if not os.path.isdir(os.path.join(work_dir,'s%s'%s_temp.ID.getLevel2())):
            os.mkdir(os.path.join(work_dir,'s%s'%s_temp.ID.getLevel2()))
        s_temp.csvSpeed(os.path.join(work_dir,'s%s'%s_temp.ID.getLevel2()))
        session_pool[s_temp.ID.getSessionID()] = s_temp

    print 'total session count is:',len(session_pool)
################################################################################

################################ Summary #######################################
    neuron_pool = []
    for spike_ID, each_spike in spike_pool.items():
        neuron_temp = neuron.Neuron(each_spike.ID.getID())
        verySession = None
        for item in session_pool.values():
            #print item.ID.getSessionID(),each_spike.ID.getSessionID()
            if item.ID.getSessionID() == each_spike.ID.getSessionID():
                verySession = item
                break
        if verySession is None:
            continue

        neuron_temp.setData(each_spike.arraySpike(),verySession.arrayVisual(),each_spike.arraySpike(),verySession.arrayMotor())
        neuron_temp.fitForest(train_len=0.8)
        neuron_pool.append(neuron_temp)
        #print 'theta:',neuron_temp.inter_angle
    print 'analyze neuron:',len(neuron_pool)

    if not os.path.isdir(os.path.join(work_dir,'summary')):
        os.mkdir(os.path.join(work_dir,'summary'))

    with open(os.path.join(work_dir,'summary/summary.csv'),'w') as csvfile:
        fieldnames = ['session', 'pp','R^2_v','R^2_m','angle']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in neuron_pool:
            writer.writerow({'session':item.name, 'pp':item.PP, 'R^2_v':item.fitScore_VF,'R^2_m':item.fitScore_RS,'angle':item.inter_angle/math.pi*180})
            item.imgPro(os.path.join(work_dir,'summary'))

    #for item in neuron_pool:
    #    with open(os.path.join(work_dir,'summary/%s.csv'%item.name),'w') as csvfile:
    #        fieldnames = ['spike','visual_test','visual_data','motor_test','motor_data']
    #        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #        writer.writeheader()
#
#            for subitem in item.

    #TODO:


################################################################################


def test():
    s1 = spike.Spike()
    s1.formatSpikes('/Users/zane/Desktop/ProjectE/Psychopy4Lab/SpikeStation/example/20160926-no.25-s1/Ch4.txt',time_limit=setting['time_limit'])
    s1.csvSpike('/Users/zane/Desktop/ProjectE/Psychopy4Lab/SpikeStation/example/20160926-no.25-s1/')


if __name__ == '__main__':
    main()
