import time

start=0
def initial():
	global start
	start=time.time()

def Clock():
	global start
	if start==0 or start==None:
		initial()

	return time.time()-start

def quit():
	print 'core quit'

if __name__ == '__main__':
	while True:
		print Clock()
