#!/usr/bin/env python
#encoding:utf-8

#####################
import os, sys, re



def void_func(anyParam=None):
    return 1

def getSummary(channel_dir,t_step=1,limit=300,speed_func=void_func):

    session_data = getSession(channel_dir)

    summary = []
    spike_data = []

    for each_session in session_data:
        f = open(os.path.join(channel_dir,each_session),'r')
        each_session_data = {}
#        print f.read()[1:10]
        for item in  re.split(r'\n',f.read()):
#            print item
            if item != '':
#                print re.split(r',',item)
                each_session_data[re.split(r',',item)[0]] = re.split(r',',item)[1]
        spike_data.append(each_session_data)
        f.close()


#    print spike_data

    time_counter = 1.0

    summary = 'time,%saverage,speed\n'%('each_session,'*len(spike_data)) #header

    while time_counter <= limit:
        entry = str(time_counter)+','
        average_sum = 0
        for each_session in spike_data:
#            print each_session
            try:
                entry += each_session[str(time_counter)]+','
                average_sum += int(each_session[str(time_counter)])
            except KeyError:
                entry += '0,'
                average_sum += 0

        entry += str(average_sum/float(len(spike_data)))+','
        entry += str(speed_func(time_counter))
        summary += entry+'\n'

        time_counter += t_step

    f = open(os.path.join(channel_dir,'summary.csv'),'w')
    f.write(summary)
    f.close()
    return

def getSession(working_dir):
    session_data = []
    for item in os.listdir(working_dir):
        if re.match(r'\d{1,2}\.csv',item):
            session_data.append(item)
    return session_data

if __name__ == '__main__':
    print os.getcwd()
    getSummary(os.getcwd())
