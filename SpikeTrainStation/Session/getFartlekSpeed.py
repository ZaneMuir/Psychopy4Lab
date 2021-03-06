#!/usr/bin/env python
#encoding:utf-8

import math

#(A,T,x) -- A for amplitude, T for cycle time, x for duration time(if omitted, means infinite)
#fartlek_seq = [(2,30,30),(2,60,60),(2,90,90),(2,120,120),(2,30,)]
fartlek_seq = [
(2,30,30),(1.5,60,30),(1.5,30,30),(1,60,30),(2,30,30),
(2,30,30),(1.5,60,30),(1.5,30,30),(1,60,30),(2,30,30),(2,30,)]
#说明：
#fartlek_seq代表的是一个分段函数，每个tuple都是一个子函数的各个参数。
#每个子函数的形式都是v(x) = v_0 * A^{sin(2*pi/T*x)}
#latex: v(x) = v_0 \times A^{\sin{(\frac{2 \pi}{T} x)}}
#(A,T,x)，A代表振幅，T代表周期，A和T决定了自函数的形状；x表示该子函数运行的时间(单位为秒)
#当一个子函数运行完后即进入下一个子函数，若x为None，则该自函数将一直运行(这里设为9999秒以达到该目的)


# fartlek(time_tag,v_0=20,fartlek_seq=[(2,30,)])
# --> visual_speed (float)
# 调用时time_tag表示所求的时刻(单位为s)
# fartlek_seq为所求的参数列表
# v_0为20cm per sec，不需要改动
def fartlek(time_tag,v_0=20,fartlek_seq=[(2,30,)]):
	time_set = 0

	for seq_item in fartlek_seq:
		try:
			current_seq_time = seq_item[2]
		except IndexError:
			current_seq_time = 9999

		time_set += current_seq_time

		if time_tag < time_set:
			v_x = v_0*seq_item[0]**math.sin(2*math.pi/seq_item[1]*(time_tag+current_seq_time-time_set))
			#
			#equation:
			#v(x) = v_0 * A^{sin(2*pi/T*x)}
			#
			return v_x
		else:
			#debug_counter += 1
			continue


if __name__ == '__main__':
	#test
	for i in range(60):
		print sin_wave(i)
	#lab.gratingFourWindows(task_sequence,vel_func=vel_function)
	#default value of defaultVel is 0.1, which means 20 cm per sec in reality.
