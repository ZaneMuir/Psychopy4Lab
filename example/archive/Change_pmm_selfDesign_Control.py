#!/usr/bin/env python
from psychopy import visual, core, event
import os

TimePoint=[(60,),(10,1.6),(90,),(10,1.2),(130,),(10,1.6),(70,),(10,1.2),(110,),(10,1.6)] #time setting.
#Example:[(t1,s1),(t2,s2),(t3,s3),(t4,s4), ...], t1 seconds in default speed by s1, and t2 second in set speed by s2,
#and the same as t3,t4, and so on; or remain in default speed mode (by 1).

#----------------------------------------------
#Copyright © 2016 Zane Muir
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the “Software”), to deal in
#the Software without restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
#Software, and to permit persons to whom the Software is furnished to do so,
#subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
#IN THE SOFTWARE.
#----------------------------------------------

#Basic Setup
mysize = 400     #size of grating
mysf =0.06       #spatial freq of grating

##################################################
myvel_changed = 0.05      #velocity of drifting
myvel_default=0.1         #
myvel=myvel_default       #default speed
##################################################

mytex = 'sqr'   #texture of grating
mytime =1       #period of cycle
mycol= [0.7,0.7,0.7]  #color of grating

#orientation of drifting
ori_left = 180
ori_right = 0

sysMessage=''   #output message container

timer = core.Clock()

#Windows
#Left Side
mywin1 = visual.Window(fullscr = True, monitor = "testMonitor", screen = 1, units = "deg", allowGUI = False)
mywin3 = visual.Window(fullscr = True, monitor = "testMonitor", screen = 3, units = "deg", allowGUI = False)
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

setTimePoint=TimePoint[0][0]
i=1                       #counter to determine which speed to use.


#process starts
sysMessage='Start\n'

while True:
	if timer.getTime()>=setTimePoint and i<=len(TimePoint):  #reach the time set point
		print 'c'
		sysMessage=str(i)+'/'+str(len(TimePoint))+'\n'       #to show the session number

        #sysMessage
        #if i%2==1: # speed change
        #    sysMessage+='Speed Changes\n'
        #    myvel=myvel_changed
        #else:
        #    sysMessage+='Speed Normal\n'
        #    myvel=myvel_default
        #

		try:
			if (len(TimePoint[i])==2) and (TimePoint[i][1] != 1):
				sysMessage+='Speed Changes\n'
				myvel=myvel_default*TimePoint[i][1]
			else:
				sysMessage+='Speed Default\n'
				myvel=myvel_default

			setTimePoint=setTimePoint+TimePoint[i][0]           #to set the next time set point
			sysMessage+='next set point '+str(setTimePoint)+'\n'

		except IndexError,e:                                 #to handle the last item of the list.
			sysMessage+='finished\n'
			pass
		i+=1
		sysMessage+='----------------------\n'

	#using cmd.exe
	os.system('cls')
	print sysMessage,'\n',timer.getTime()

    #DEBUG: print timer.getTime()
	mygrat1.setPhase(myvel, '+')
	mygrat1.draw()
	mygrat3.setPhase(myvel, '+')
	mygrat3.draw()
	mygrat4.setPhase(myvel, '+')
	mygrat4.draw()
	mygrat5.setPhase(myvel, '+')
	mygrat5.draw()

	mywin1.flip()
	mywin3.flip()
	mywin4.flip()
	mywin5.flip()

	for keys in event.getKeys(timeStamped=True):
		if keys[0] in ['escape','q']:             #Quiting
			mywin1.close()
			mywin3.close()
			mywin4.close()
			mywin5.close()
			core.quit()
            #TODO: break
