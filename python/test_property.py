class Parrot(object):
	def __init__(self):
		self._voltage = 100000
	
	@property
	def voltage(self):
		"""get the current voltage."""
		return self._voltage

if __name__ == '__main__':
	p = Parrot()
	print p.voltage
	p.voltage = 12
