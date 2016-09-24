from Psychopy4Lab import gratingCorridor as lab

task_sequence=[
(50,),(10,1.6),
(50,),(10,1.1),
(50,),(10,1.0),
(50,),(10,1.2),
(50,),(10,1.6),
(50,),(10,1.0),
(50,),(10,1.2),
(50,),(10,1.4),
(50,),(10,1.2),
(50,),(10,1.4),
(50,),(10,1.0),
(50,),(10,1.1),
(50,),(10,1.4),
(50,),(10,1.6),
(50,),(10,1.1),
(50,),(10,1.6),
(50,),(10,1.1),
(50,),(10,1.4),
(50,),(10,1.0),
(50,),(10,1.2)]

if __name__ == '__main__':
	lab.gratingFourWindows(task_sequence)
	#default value of defaultVel is 0.1, which means 20 cm per sec in reality.
