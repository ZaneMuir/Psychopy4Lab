 #!/usr/bin/env python
#encoding:utf-8

import os, re

corridor_name = r'.*?Corridor.*?'

def getSessionCounter(target_dir):
    count = 0
    for item in os.listdir(target_dir):
        #print item #DEGUG
        if re.match(corridor_name,item):
            count += 1

    return count

def clean(target_dir=os.getcwd()):

    #make session info directories
    session_count = getSessionCounter(target_dir)
    for index in range(1,session_count+1):
        if not os.path.isdir(os.path.join(target_dir,'s%d'%index)):
            print 'make dir: %s'%os.path.join(target_dir,'s%d'%index)
            os.mkdir(os.path.join(target_dir,'s%d'%index))

    return session_count

if __name__ == '__main__':
    import sys
    clean(sys.argv[1])
