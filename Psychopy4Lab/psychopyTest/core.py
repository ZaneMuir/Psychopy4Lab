import time

class Clock(object):
	"""docstring for Clock"""
	def __init__(self):
		super(Clock, self).__init__()
		self.start=time.time()

	def getTime(self):
		return time.time()-self.start

def quit():
	print 'core quit'

if __name__ == '__main__':
	while True:
		print Clock()
