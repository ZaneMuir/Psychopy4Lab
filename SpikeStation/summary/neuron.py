from sklearn import ensemble
import scipy as sp
import math

def reform(data):
    out = []
    for i in data:
        out.append(i[0])
    #print out
    return out

class Neuron(object):
    """docstring for Neuron."""
    def __init__(self,name=None,visual_data=None,visual_target=None,motor_data=None, motor_target=None):
        super(Neuron, self).__init__()

        #private property
        self.randomForestRegressor_VF = ensemble.RandomForestRegressor()
        self.randomForestRegressor_RS = ensemble.RandomForestRegressor()

        #public property
        self.inter_angle = None  #interaction angle

        self.fitScore_VF = None     #R^2 : assigned in <method fitForest>
        self.fitScore_RS = None

        self.PP = None           #Pearson coef. : assigned in <method fitForest>
        self.PP_VF = None
        self.PP_RS = None

        self.visual_data = visual_data         #
        self.motor_data = motor_data
        self.visual_target = visual_target       #
        self.motor_target = motor_target

        self.name = name

    def fitForest(self,train_len=0.8):
        #fit
        self.randomForestRegressor_VF.fit(self.visual_data[:int(len(self.visual_data)*train_len)],self.visual_target[:int(len(self.visual_data)*train_len)])
        self.randomForestRegressor_RS.fit(self.motor_data[:int(len(self.motor_data)*train_len)],self.motor_target[:int(len(self.motor_data)*train_len)])

        self.fitScore_RS = self.randomForestRegressor_RS.score(self.motor_data[:int(len(self.motor_data)*train_len)],self.motor_target[:int(len(self.motor_data)*train_len)])
        self.fitScore_VF = self.randomForestRegressor_VF.score(self.visual_data[:int(len(self.visual_data)*train_len)],self.visual_target[:int(len(self.visual_data)*train_len)])

        predict_result_VF = self.randomForestRegressor_VF.predict(self.visual_data[int(len(self.visual_data)*train_len):])
        predict_result_RS = self.randomForestRegressor_RS.predict(self.motor_data[int(len(self.motor_data)*train_len):])

        self.PP_VF, _ = sp.stats.pearsonr(reform(self.visual_data[int(len(self.visual_data)*train_len):]),predict_result_VF)
        self.PP_RS, _ = sp.stats.pearsonr(reform(self.motor_data[int(len(self.motor_data)*train_len):]),predict_result_RS)
        self.PP = math.sqrt(self.PP_RS**2 + self.PP_VF**2)

        self.inter_angle = math.atan(self.PP_VF/self.PP_RS)  #interaction angle

        return

    def setData(self,visual_data,visual_target,motor_data, motor_target):
        self.visual_data = visual_data         #
        self.motor_data = motor_data
        self.visual_target = visual_target       #
        self.motor_target = motor_target
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
