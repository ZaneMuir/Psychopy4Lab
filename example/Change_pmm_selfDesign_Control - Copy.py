from Psychopy4Lab import gratingCorridor as lab

task_sequence=[
(45,),(5,1.4),
(75,),(5,1.4),
(45,),(5,1.4),
(35,),(5,1.4),
(55,),(5,1.4)
]


if __name__ == '__main__':
	lab.gratingFourWindows(task_sequence)
	#default value of defaultVel is 0.1, which means 20 cm per sec in reality.
