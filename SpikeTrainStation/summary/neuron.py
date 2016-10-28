from sklearn import ensemble
import scipy as sp

def reform(data):
    out = []
    for i in data:
        out.append(i[0])
    print out
    return out

class Neuron(object):
    """docstring for Neuron."""
    def __init__(self,name=None):
        super(Neuron, self).__init__()

        #private property
        self.__randomForestRegressor__ = ensemble.RandomForestRegressor()


        #public property
        self.inter_angle = None  #interaction angle
        self.fitScore = None     #R^2 : assigned in <method fitForest>
        self.PP = None           #Pearson coef. : assigned in <method fitForest>
        self.data = None         #
        self.target = None       #
        self.name = name

    def fitForest(self,train_len=0.8):
        #fit
        self.__randomForestRegressor__.fit(self.data[:int(len(self.data)*train_len)],self.target[:int(len(self.data)*train_len)])
        self.fitScore = self.__randomForestRegressor__.score(self.data[:int(len(self.data)*train_len)],self.target[:int(len(self.data)*train_len)])

        predict_result = self.__randomForestRegressor__.predict(self.data[int(len(self.data)*train_len):])

        #FIXME:
        print len(predict_result)
        print int(len(self.data)*train_len),len(self.data)

        try: #FIXME: ValueError: operands could not be broadcast together with shapes (59) (60) on ch10-0
            self.PP,a = sp.stats.pearsonr(reform(self.target[int(len(self.data)*train_len):]),predict_result)
        except ValueError:
            self.PP,a = sp.stats.pearsonr(reform(self.target[int(len(self.data)*train_len):]),predict_result[:len(self.target[int(len(self.data)*train_len):])])

        return

    def setData(self,data,target):
        self.data = data         #
        self.target = target       #
        return

    def appendResult(self,path):
        f = open(path,'a')
        entry = self.name+','
        entry += str(self.fitScore)+','
        entry += str(self.PP)+','
        entry += '\n'
        f.write(entry)
        f.close()
        return
