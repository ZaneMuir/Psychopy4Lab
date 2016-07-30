class Window(object):
	"""docstring for Window"""
	def __init__(self,fullscr, monitor, screen, units, allowGUI):
		#super(Window, self).__init__()
		#self.arg = arg
		print 'new Window'

	def flip(self):
		pass

	def close(self):
		print 'window close'

class GratingStim(object):
	"""docstring for GratingStim"""
	def __init__(self, win, tex,mask, size, sf,ori, color):
		#super(GratingStim, self).__init__()
		#self.arg = arg
		print 'new GratingStim'

	def setPhase(self,vel,ori):
		pass

	def draw(self,):
		pass
