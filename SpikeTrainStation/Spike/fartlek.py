import math

#(A,T,x) -- A for amplitude, T for cycle time, x for duration time(if omitted, means infinite)
#fartlek_seq = [(2,30,30),(2,60,60),(2,90,90),(2,120,120),(2,30,)] 
fartlek_seq = [
(2,30,30),(1.5,60,30),(1.5,30,30),(1,60,30),(2,30,30),
(2,30,30),(1.5,60,30),(1.5,30,30),(1,60,30),(2,30,30),(2,30,)]

def sin_wave(time_tag,raw_vel=20,fartlek_seq=[(2,30,)]):
	#debug_counter = 1
	time_set = 0
	for seq_item in fartlek_seq:
		try:
			current_seq_time = seq_item[2]
		except IndexError:
			current_seq_time = 9999
		
		time_set += current_seq_time
			
		if time_tag < time_set:
			new_vel = raw_vel*seq_item[0]**math.sin(2*math.pi/seq_item[1]*(time_tag+current_seq_time-time_set))
			#
			#equation:
			#v(x) = v_0 * A^{sin(2*pi/T*x)}
			#
			#print debug_counter
			return new_vel
		else:
			#debug_counter += 1
			continue


if __name__ == '__main__':
	lab.gratingFourWindows(task_sequence,vel_func=vel_function)
	#default value of defaultVel is 0.1, which means 20 cm per sec in reality.
