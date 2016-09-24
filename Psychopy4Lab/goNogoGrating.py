#!/usr/bin/env python
#encoding:utf-8
#----------------------------------------------------------------------------
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
#
#----------------------------------------------------------------------------
try:
	from psychopy import visual, core, event
except ImportError, e:
	from psychopyTest import visual, core, event #to run debug on my mac
import gadget

'''
Experiment Setup:
each subsession consists of a window epoch of a gray solid screen for 10 seconds (by default), and a grating epoch of a grate with a temporal frequency of self-designed times of defaultVel for 5 seconds (by default).

parameters:
TaskSerial			task sequence for the speed information of each grating epoch and determine the total number of the subsessios. eg: [1.1,1.6,1.3]
windowDuration		time of window epoch, unit of seconds, default value: 10 (seconds)
gratingDuration		time of grating epoch, unit of seconds, default value: 5 (seconds)
defaultVel			default temporal frequency of grating,  default value: 0.1
timeLog				to log the start time in order to align the time line
logPath				custom log file path

'''
def goNogoGrating(TaskSerial=[], windowDuration=10, gratingDuration=5, defaultVel=0.1, timeLog=True, logPath=None, gratingColor_Grating=[0.7,0.7,0.7]):
	gratingSize=400
	gratingSpatialFreq=0.06
	gratingTex='sqr'
	gratingMask='None'
#	gratingColor_Grating=[0.7,0.7,0.7]
	gratingColor_Window=[0,0,0]
	timeCycle=1
	#defaultVel=0.1

	#Window
	#Left Side
	win1 = visual.Window(fullscr = True, monitor = "testMonitor", screen = 1, units = "deg", allowGUI = False)
	win3 = visual.Window(fullscr = True, monitor = "testMonitor", screen = 3, units = "deg", allowGUI = False)
	#Right Side
	win4 = visual.Window(fullscr = True, monitor = "testMonitor", screen = 4, units = "deg", allowGUI = False)
	win5 = visual.Window(fullscr = True, monitor = "testMonitor", screen = 5, units = "deg", allowGUI = False)

	#Grating
	#Left Side
	grat1 = visual.GratingStim(win=win1, tex=gratingTex,mask=gratingMask, size =gratingSize, sf = gratingSpatialFreq,ori = 180, color = gratingColor_Window)
	grat3 = visual.GratingStim(win=win3, tex=gratingTex,mask=gratingMask, size =gratingSize, sf = gratingSpatialFreq,ori = 180, color = gratingColor_Window)
	#Right Side
	grat4 = visual.GratingStim(win=win4, tex=gratingTex,mask=gratingMask, size =gratingSize, sf = gratingSpatialFreq,ori = 0, color = gratingColor_Window)
	grat5 = visual.GratingStim(win=win5, tex=gratingTex,mask=gratingMask, size =gratingSize, sf = gratingSpatialFreq,ori = 0, color = gratingColor_Window)

	vel=defaultVel
	timer=core.Clock()
	i=1
	j=1
	length=len(TaskSerial)
	sysMessage='Start\n1/'+str(length)+'\nwindow epoch\nnext set point: '+str(windowDuration)

	if timeLog:
		gadget.logMessage(task='ExcelTimeTag')
		#theMessage='session, '
		#logMessage(theMessage,str('%.10f'%((time.time()+8*3600)/86400+70*365+19)))

	while True:
		#10*i+5*(i-1)
		if i<=len(TaskSerial):
			if timer.getTime()>j*(windowDuration+gratingDuration)-gratingDuration:

				try:
					sysMessage=str(j)+'/'+str(len(TaskSerial))+'\n'
					sysMessage+='grating epoch'+str(TaskSerial[j-1])+'\n'
					sysMessage+='next set point: '+str(j*(windowDuration+gratingDuration))
					vel=defaultVel*TaskSerial[j-1]
				except IndexError, e:
					vel=defaultVel

				grat1.color=gratingColor_Grating
				grat3.color=gratingColor_Grating
				grat4.color=gratingColor_Grating
				grat5.color=gratingColor_Grating

				j+=1
			elif timer.getTime()>i*(windowDuration+gratingDuration):
				sysMessage=str(j)+'/'+str(len(TaskSerial))+'\n'
				sysMessage+='window epoch\n'
				sysMessage+='next set point: '+str(j*(windowDuration+gratingDuration)-gratingDuration)

				grat1.color=gratingColor_Window
				grat3.color=gratingColor_Window
				grat4.color=gratingColor_Window
				grat5.color=gratingColor_Window

				i+=1
		elif i<=j:
			sysMessage='finished'

			grat1.color=gratingColor_Window
			grat3.color=gratingColor_Window
			grat4.color=gratingColor_Window
			grat5.color=gratingColor_Window

			i+=1
		#os.system('cls')
		gadget.cleanScreen()
		print sysMessage
		print '======================='
		print '%0.2f'%timer.getTime()

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
	#demo
	goNogoGrating([2,2])#,windowDuration=2,gratingDuration=1)
