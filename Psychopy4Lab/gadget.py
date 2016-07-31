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
#----------------------------------------------------------------------------
import time,os

'''
function:
to log the custom or special message

parameter:
message:		custom log message (automatically add a '\n' to each one)
isNew:			currently no use
logPath:		custom log file path, default file path format: ~\Desktop\$<current_date>_psychopy.$<logFileType>
logFileType:	file type, default: csv
timeTag:		to tag a time tag before each message
task:			special task, include: ExcelTimeTag-->to output the time tag in Excel format

'''
def logMessage(message='',isNew=False,logPath=None,task=None,logFileType='csv',timeTag=True):
	#TODO:to add 'isNew' parameter

	#set filePath
	if logPath is None:
		#default file path format: ~\Desktop\$<date>_psychopy.$<logFileType>
		filePath=os.path.join(os.path.join(os.getcwd(),'Desktop'),time.strftime('%y%m%d')+'_psychopy.'+logFileType)
	else:
		filePath=logPath

	#open file in appending mode
	logfile=open(filePath,'a')

	#timeTag:
	if timeTag:
		logfile.write(time.strftime('%y%m%d-%H:%M:%S,'))

	#special task:
	#ExcelTimeTag
	if task is 'ExcelTimeTag':
		logfile.write('Session,'+str('%.10f'%((time.time()+8*3600)/86400+70*365+19)))
	else:
		logfile.write(message)

	#write an 'enter' and close the file and return
	logfile.write('\n')
	logfile.close()
	return

'''
function:
clear the termial screen
'''
def cleanScreen():
	if os.name is 'posix': #for unix-like system
		os.system('clear')
	elif os.name is 'nt': #for windows
		os.system('cls')
	return
