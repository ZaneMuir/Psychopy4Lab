 #!/usr/bin/env python
 #encoding:utf-8

import os, re, sys
from Cleaner import clean as cleanDir
from getPsychoPyTime import getPsychoPyTime
from getCorridorTime import getCorridorTime
from getFartlekSpeed import sin_wave as getVisualSpeed
from getCorridorSpeed import getCorridorSpeed as getRunningSpeed
from writeSession import writeSession
import testSetting

corridor_name = r'.*?Corridor.*?'
pathdata_name = r'.*?PathData.*?'

def getCorridorFileNames(target_dir=os.getcwd()):
    corridorFileNames = []
    for item in os.listdir(target_dir):
        if re.match(corridor_name,item):
            corridorFileNames.append(item)
    return corridorFileNames

def getPathDataFileNames(target_dir=os.getcwd()):
    pathDataFileNames = []
    for item in os.listdir(target_dir):
        if re.match(pathdata_name,item):
            pathDataFileNames.append(item)
    return pathDataFileNames


if __name__ == '__main__':
    # main
    if len(sys.argv) == 2:
        target_dir = sys.argv[1]
    else:
        target_dir = os.getcwd()

    # make session info dir
    session_count = cleanDir(target_dir)

    # get psychopy time_tag
    psychopy_timetags = getPsychoPyTime(target_dir)

    #
    corridorFileNames = getCorridorFileNames(target_dir)
    pathDataFileNames = getPathDataFileNames(target_dir)

    # process session info
    for index in range(session_count):

        VR_ttl = getCorridorTime(os.path.join(target_dir,corridorFileNames[index]))
        Py_timetag = psychopy_timetags[index]
        time_lag = VR_ttl - Py_timetag

        visual_speed = []
        for time_point in range(testSetting.time_limit[0],testSetting.time_limit[1],testSetting.time_limit[2]):
            visual_speed.append(getVisualSpeed(time_point+time_lag,fartlek_seq=testSetting.fartlek_seq))

        #print visual_speed

        running_speed = getRunningSpeed(os.path.join(target_dir,pathDataFileNames[index]),VR_ttl=VR_ttl,time_limit=testSetting.time_limit)
        #print running_speed

        #TODO:output
        writeSession(time_limit=testSetting.time_limit, visual_speed=visual_speed, motor_speed=running_speed,index=index, working_dir=target_dir)
        print 'wrote',corridorFileNames[index]
