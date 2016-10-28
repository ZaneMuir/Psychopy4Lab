from skl_angle import main as skl
import os, re, math
import numpy as np
import neuron

outputHeader = 'ch,R^2,PP,angle\n'


def read_data(path):
    f = open(path,'r')
    data = f.read()
    f.close()

    speeds = []
    for item in re.split(r'\n',data):
        entry = re.split(r',',item)
        try:
            speeds.append([float(entry[1]),float(entry[2])]) #format: [[visual, motor]]
        except IndexError:
            pass
    return speeds

def read_spike(path):
        f = open(path,'r')
        data = f.read()
        f.close()

        spike = []
        for item in re.split(r'\n',data):
            entry = re.split(r',',item)
            try:
                spike.append([float(entry[1])]) #format: [[visual, motor]]
            except IndexError:
                pass
        return spike


def getSessionInfo(work_dir,session_sort=r's\d',session_item_sort=r'speed.csv'):
    session = []
    for item in os.listdir(work_dir):
        if re.match(session_sort,item):
            for subitem in os.listdir(os.path.join(work_dir,item)):
                if re.match(session_item_sort,subitem):
                    speeds = read_data(os.path.join(os.path.join(work_dir,item),subitem))
                    session.append(speeds)
    return session

def output_results(ch_name, theresults,path):
    f = open(os.path.join(path,'regression.csv'),'a')
    entry = ch_name+','
    entry += str(theresults[0])+','
    entry += str(theresults[1])+','
    entry += str(math.atan(theresults[0]/theresults[1]))+','
    entry += str(theresults[2][0])+'\n'
    f.write(entry)
    f.close()

def R_value(predict,target):
    s_mean = np.mean(predict)
    a = 0.0
    b = 0.0
    c = 0.0
    for index in range(len(predict)):
        try:
            v_p = predict[index]
            v_t = target[index]
        except IndexError:
            #FIXME
            continue
        a += (v_p - s_mean)*(v_t - s_mean)
        b += (v_p - s_mean)**2
        c += (v_t - s_mean)**2

    return (a/math.sqrt(b*c))**2


def main(work_dir=os.getcwd(),channel_sort=r'ch_.*?',channel_item_sort=r'\d\.csv'):
    dataset_data = getSessionInfo(work_dir)
    print 'dataset_data got'#FIXME
    dataset_target = []
    target_dir = os.path.join(work_dir,'summary')
    if not os.path.isdir(target_dir):
        os.mkdir(target_dir)
        #print 'make dir',target_dir

    f = open(os.path.join(target_dir,'regression.csv'),'w')
    f.write(outputHeader)
    f.close()

    for item in os.listdir(work_dir):
        if re.match(channel_sort,item):
            # get into each channel directory
            dataset_target = []
            for subitem in os.listdir(os.path.join(work_dir,item)):
                if re.match(channel_item_sort,subitem):
                    spike_info = read_spike(os.path.join(os.path.join(work_dir,item),subitem))
                    dataset_target.append(spike_info)

            print "channel:",item
            for index in range(len(dataset_target)):
                #print "ch:",index
                data = dataset_data[index]
                target = dataset_target[index]

                aNeuron = neuron.Neuron('%s-%d'%(item,index))
                aNeuron.setData(data,target)
                aNeuron.fitForest()
                aNeuron.appendResult(os.path.join(target_dir,'regression.csv'))

                print 'session:',index,'finished'


if __name__ == '__main__':
    main()
