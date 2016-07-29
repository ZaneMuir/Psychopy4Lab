#!/usr/bin/env python
#encoding:utf-8
#----------------------------------------------
#Copyright © 2016 Zane Muir
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the “Software”),
#to deal in the Software without restriction, including without limitation
#the rights to use,copy, modify, merge, publish, distribute, sublicense,
#and/or sell copies of the Software, and to permit persons to whom the
#Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
#IN THE SOFTWARE.
#----------------------------------------------

from psychopy import core, event, visual
import os, time

def logMessage(message,isNew=False,logPath=None): #TODO:to add 'isNew' parameter
	if logPath is None:
		filePath=os.path.join(os.path.join(os.getcwd(),'Desktop'),time.strftime('%y%m%d')+'_psychopy.txt')
	else:
		filePath=logPath
	logfile=open(filePath,'a')
	logfile.write(message)
	logfile.close()
	return

def gratingFourWindows(TimePointSerial,gratingSize=400,gratingSpatialFreq=0.06,gratingTex='sqr',gratingMask='None',gratingColor=[0.7,0.7,0.7],timeCycle=1,defaultVel=0.1,timeLog=True,logPath=None):
	#Window
	#Left Side
	win1 = visual.Window(fullscr = True, monitor = "testMonitor", screen = 1, units = "deg", allowGUI = False)
	win3 = visual.Window(fullscr = True, monitor = "testMonitor", screen = 3, units = "deg", allowGUI = False)
	#Right Side
	win4 = visual.Window(fullscr = True, monitor = "testMonitor", screen = 4, units = "deg", allowGUI = False)
	win5 = visual.Window(fullscr = True, monitor = "testMonitor", screen = 5, units = "deg", allowGUI = False)

	#Grating
	#Left Side
	grat1 = visual.GratingStim(win=win1, tex=gratingTex,mask=gratingMask, size =gratingSize, sf = gratingSpatialFreq,ori = 180, color = gratingColor)
	grat3 = visual.GratingStim(win=win3, tex=gratingTex,mask=gratingMask, size =gratingSize, sf = gratingSpatialFreq,ori = 180, color = gratingColor)
	#Right Side
	grat4 = visual.GratingStim(win=win4, tex=gratingTex,mask=gratingMask, size =gratingSize, sf = gratingSpatialFreq,ori = 0, color = gratingColor)
	grat5 = visual.GratingStim(win=win5, tex=gratingTex,mask=gratingMask, size =gratingSize, sf = gratingSpatialFreq,ori = 0, color = gratingColor)

	vel=defaultVel
	setTimePoint=TimePointSerial[0][0]
	timer=core.Clock()
	i=1
	sysMessage='Start\n'

	if timeLog:
		theMessage='new session, '+str(time.time())+'\n'
		logMessage(theMessage) #TODO:

	while True:
		if timer.getTime()>=setTimePoint and i<=len(TimePointSerial):
			sysMessage=str(i)+'/'+str(len(TimePointSerial))+'\n'
			try:
				if(len(TimePointSerial[i])==2)and(TimePointSerial[i][1]!=1):
					sysMessage+='Speed Change\n'
					vel=defaultVel*TimePointSerial[i][1]
				else:
					sysMessage+='Speed Default\n'
					vel=defaultVel

				setTimePoint=setTimePoint+TimePointSerial[i][0]
				sysMessage+='next set point '+str(setTimePoint)+'\n'

			except IndexError, e:
				sysMessage+='finished\n'

			i+=1
			sysMessage+='===========================\n'

			os.system('cls')
			print sysMessage,'\n',timer.getTime()

		grat1.setPhase(vel,'+')
		grat3.setPhase(vel,'+')
		grat4.setPhase(vel,'+')
		grat5.setPhase(vel,'+')

		grat1.draw()
		grat3.draw()
		grat4.draw()
		grat5.draw()

		win1.flip()
		win3.flip()
		win4.flip()
		win5.flip()

		for keys in event.getKeys(timeStamped=True):
			if keys[0] in ['escape','q']:
				win1.close()
				win3.close()
				win4.close()
				win5.close()
				core.quit()



if __name__ == '__main__':
	gratingFourWindows([(10,),(10,2)])
	#logMessage(str(core.getAbsTime()))
