from psychopy import visual, core, event
import random

#size of grating
mysize = 100

#spatial freq of grating 
mysf =0.5

#velocity of drifting
myvel = 0.1

#texture of grating
mytex = 'sqr'

#period of cycle
mytime =1

#color of grating
mycol= [1,1,1]

#orientation of drifting
n = 7
myori =180

s= 'sequece of grating:'

timer = core.Clock()
#mywin1 = visual.Window(size=[200,200],pos=[900,400], monitor = "testMonitor", screen = 0, units = "deg", allowGUI = False)
mywin2 = visual.Window(fullscr = True, monitor = "testMonitor", screen = 3, units = "deg", allowGUI = False)
#mygrat1 = visual.GratingStim(mywin1, tex=mytex,mask='None', size =mysize, sf = mysf,ori = myori, color = mycol) 
mygrat2 = visual.GratingStim(mywin2, tex=mytex,mask='None', size =mysize, sf = mysf,ori = myori, color = mycol) 
#message = visual.TextStim(mywin,pos=(0.0,-0.9),text='Hit Q to quit')

i=1

while timer.getTime() < 10000:
    #mygrat1.setPhase(myvel, '+')
    #mygrat1.draw()
    mygrat2.setPhase(myvel, '+')
    mygrat2.draw()
    #message.draw()
    #mywin1.flip()
    mywin2.flip()
    if int(timer.getTime()) == mytime * i:
        if i==250:
            #mywin1.close()
            mywin2.close()
            seq.write(s)
            seq.close()
            core.quit()
        else:
            if i%5==4:
                mycol = [1,1,1]
                #mygrat1 = visual.GratingStim(mywin1, tex=mytex,mask='None', size =mysize, sf = mysf,ori = myori, color = mycol) 
                mygrat2 = visual.GratingStim(mywin2, tex=mytex,mask='None', size =mysize, sf = mysf,ori = myori, color = mycol)
                i= i+1
                myori +=0
            else:
                mycol= [0,0,0]
                #mygrat1 = visual.GratingStim(mywin1, tex=mytex,mask='None', size =mysize, sf = mysf,ori = myori, color = mycol)
                mygrat2 = visual.GratingStim(mywin2, tex=mytex,mask='None', size =mysize, sf = mysf,ori = myori, color = mycol)
                i= i+1
    for keys in event.getKeys(timeStamped=True):
        if keys[0] in ['escape','q']:
            #mywin1.close()
            mywin2.close()
            seq=open('F:\lab\sequence.txt','w+')
            seq.write(s)
            seq.close()
            core.quit()
