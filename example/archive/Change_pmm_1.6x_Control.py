from psychopy import visual, core, event
import random

TimePoint=[20,5] #time setting.
#Example:[t1,t2,t3,t4, ...], t1 seconds in fast speed, and t2 second in slow speed, and the same as t3,t4, and so on; or remain in slow speed mode.

#Basic Setup
mysize = 400    #size of grating
mysf =0.06       #spatial freq of grating

##################################################
myvel_fast = 0.167     #velocity of drifting
myvel_slow=0.1         #
myvel=myvel_slow       #default speed
##################################################

mytex = 'sqr'   #texture of grating
mytime =1       #period of cycle
mycol= [1,1,1] #color of grating
#n = 7          #???
ori_left = 180      #orientation of drifting
ori_right = 0

#s= 'sequece of grating:'

timer = core.Clock()

#Windows

#Left Side
mywin1 = visual.Window(fullscr = True, monitor = "testMonitor", screen = 1, units = "deg", allowGUI = False)
mywin3=visual.Window(fullscr = True, monitor = "testMonitor", screen = 3, units = "deg", allowGUI = False)
#Right Side
mywin4 = visual.Window(fullscr = True, monitor = "testMonitor", screen = 4, units = "deg", allowGUI = False)
mywin5 = visual.Window(fullscr = True, monitor = "testMonitor", screen = 5, units = "deg", allowGUI = False)


#Gratings
#Left Side
mygrat1 = visual.GratingStim(win=mywin1, tex=mytex,mask='None', size =mysize, sf = mysf,ori = ori_left, color = mycol)
mygrat3 = visual.GratingStim(win=mywin3, tex=mytex,mask='None', size =mysize, sf = mysf,ori = ori_left, color = mycol)
#Righy Side
mygrat4 = visual.GratingStim(win=mywin4, tex=mytex,mask='None', size =mysize, sf = mysf,ori = ori_right, color = mycol)
mygrat5 = visual.GratingStim(win=mywin5, tex=mytex,mask='None', size =mysize, sf = mysf,ori = ori_right, color = mycol)


#message = visual.TextStim(mywin,pos=(0.0,-0.9),text='Hit Q to quit')

timer.getTime()
setTimePoint=TimePoint[0]
i=1

while True:

    if timer.getTime()>=setTimePoint and i<=len(TimePoint):
        print i,'/',len(TimePoint)
        if i%2==1: # speed up
            print 'Speed Up'
            myvel=myvel_fast
        else:
            print 'speed down'
            myvel=myvel_slow

        try:
            setTimePoint=setTimePoint+TimePoint[i]
            print 'next set point',str(setTimePoint)

        except IndexError,e:
            print 'finished'
            pass
        i+=1
        print '----------------------'




    #print timer.getTime()
    mygrat1.setPhase(myvel, '+')
    mygrat1.draw()
    mygrat3.setPhase(myvel, '+')
    mygrat3.draw()
    mygrat4.setPhase(myvel, '+')
    mygrat4.draw()
    mygrat5.setPhase(myvel, '+')
    mygrat5.draw()
    #message.draw()

    mywin1.flip()
    mywin3.flip()
    mywin4.flip()
    mywin5.flip()





    '''
    if int(timer.getTime()) == mytime * i:
        if i==250:
            mywin2.close()
            seq.write(s)
            seq.close()
            core.quit()
        else:
            if i%5==4:
                mycol = [1,1,1]
                mygrat2 = visual.GratingStim(mywin2, tex=mytex,mask='None', size =mysize, sf = mysf,ori = myori, color = mycol)
                i= i+1
                myori +=0
            else:
                mycol= [0,0,0]
                mygrat2 = visual.GratingStim(mywin2, tex=mytex,mask='None', size =mysize, sf = mysf,ori = myori, color = mycol)
                i= i+1
                '''

    if event.getKeys()[0] in ['escape','q']:
        mywin1.close()
        mywin3.close()
        mywin4.close()
        mywin5.close()
        core.quit()
        #break


#Quiting
