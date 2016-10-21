import pandas as pd
import matplotlib.pyplot as plt
import os, re
import numpy as np

def getSessionInfo(work_dir,session_sort=r's\d',session_item_sort=r'speed.csv'):
    session = []
    for item in os.listdir(work_dir):
        if re.match(session_sort,item):
            for subitem in os.listdir(os.path.join(work_dir,item)):
                if re.match(session_item_sort,subitem):
                    speeds = pd.read_csv(os.path.join(os.path.join(work_dir,item),subitem),sep=',',na_values='.')
                    names = speeds.columns.values
                    names[0]='time_m'
                    names[1]='visual'
                    names[2]='motor'
                    speeds.columns = names
                    session.append(speeds)
    return session



def main(work_dir=os.getcwd(),channel_sort=r'ch_.*?',channel_item_sort=r'\d\.csv'):
    session_info = getSessionInfo(work_dir)
    channel_info = []
    target_dir = os.path.join(work_dir,'summary')
    if not os.path.isdir(target_dir):
        os.mkdir(target_dir)
        #print 'make dir',target_dir

    for item in os.listdir(work_dir):
        if re.match(channel_sort,item):
            #print 'find channel',item
            channel_info = []
            for subitem in os.listdir(os.path.join(work_dir,item)):
                if re.match(channel_item_sort,subitem):
                    #print 'find sess',subitem
                    spike_info = pd.read_csv(os.path.join(os.path.join(work_dir,item),subitem),sep=',',na_values='.',header=None)
                    spike_info = spike_info.rename(columns = {0:'time_v',1:'spike'})
                    channel_info.append(spike_info)
            print len(channel_info)
            for index in range(len(channel_info)):
                print index
                data = pd.concat([channel_info[index],session_info[index]],axis=1, join='inner')
                #print data
                ax = data.plot.hexbin(x='visual', y='motor', C='spike',reduce_C_function=np.mean, gridsize=25)
                ax.figure.savefig(os.path.join(target_dir,item+'-'+str(index)+'.png'))
                print 'save figure',item+'-'+str(index)+'.png'
    pass

if __name__ == '__main__':
    main()
