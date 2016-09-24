#!/usr/bin/env python
#encoding:utf-8
#-----------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------
try:
	from psychopy import core, event, visual
except ImportError,e:
	from psychopyTest import core, event, visual

'''
function:
continuous grating corridor

parameters:
TimePointSerial
gratingSize
gratingSpatialFreq
gratingTex
gratingMask
gratingColor
timeCycle
defaultVel
timeLog
logPath

'''

def null_func(the_input):
	return the_input

def gratingFourWindows(TimePointSerial,gratingSize=400,gratingSpatialFreq=0.06,gratingTex='sqr',gratingMask='None',gratingColor=[0.7,0.7,0.7],timeCycle=1,defaultVel=0.1,timeLog=True,logPath=None,vel_func=null_func):
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
		#theMessage='new session, '+str(time.time())+'\n'
		#logMessage(theMessage)
		gadget.logMessage(task='ExcelTimeTag')

	startTimePoint=time.time()

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
				vel=defaultVel
				sysMessage+='finished\n'

			i+=1
			sysMessage+='===========================\n'
		else:
			vel = defaultVel

		os.system('cls')
		print sysMessage,'\n','%.2f'%timer.getTime()

		vel=vel_func(vel,timer.getTime())

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
