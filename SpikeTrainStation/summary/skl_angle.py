from sklearn import linear_model
import matplotlib.pyplot as plt


def cost(predict,target):
    cost_v = 0
    #print 'predict',predict
    #print 'target',target
    for index in range(len(predict)):
        try:
            cost_v += (predict[index]-target[index])**2
        except IndexError:
            pass#FIXME
    return cost_v/len(predict)

def fig(data, target):
    #FIXME
    plt.scatter(data, target,  color='black')
    plt.xticks(())
    plt.yticks(())

    plt.show()


#skl_angle.main()
#data: [[visual, motor],[visual,motor],...]
#target: [spike,spike,...]
#learn_len = 50 (less than sample count)
def main(data,target,learn_len=50,cost_func = cost):

    linear_regr = linear_model.LinearRegression()
    #print data[:50]
    linear_regr.fit(data[:50],target[:50])

    predict_target = linear_regr.predict(data[50:])
    cost_value = cost_func(predict_target,target[50:]) #evaluate
    #print linear_regr.coef_

    #fig(data, target)

    return (linear_regr.coef_[0][0],linear_regr.coef_[0][1],cost_value)
