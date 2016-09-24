#encoding:utf-8
from Psychopy4Lab import goNogoGrating as lab

task_sequence_0=[
1,1,1,1,1,1,
1,1,1,1,1,1
]

task_sequence_1=[
1,1,2,1,2,1,
1,1,2,2,1,2
]

task_sequence_2=[
1,2,2,1,1,2,
1,1,2,1,2,1,
1,1,2,2,1,2
]

task_sequence_3=[
1,5,5,1,1,5,
1,1,5,1,5,1,
1,1,5,5,1,5
]

task_sequence_4=[
1,1,5,1,5,1,
1,5,1,5,5,1,
1,5,1,5,5,1
]

task_sequence_5=[
5,1,1,5,1,5,
1,1,5,5,1,1,
1,5,1,5,1,5
]

task_sequence_x=[
#没有光栅
]

if __name__=='__main__':
	lab.goNogoGrating(task_sequence_5,windowDuration=10, gratingDuration=10,defaultVel=0.1)
	#可以将不同的task sequence编号，使用时只需要修改上面这句话中的号码即可。
	#windowDuration指的是interval的时间
	#defaultVel为1x的速度，默认为0.1