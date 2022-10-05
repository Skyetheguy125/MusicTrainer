from random import seed, uniform
from time import sleep, time

class SigProcessorScaffold:
	def __init__(self, delay=10, range=(0,5000)):
		self.delay = delay
		self.range = range
		self.signal = self.signalGenerator()
	
	def rand_value(self):
		return uniform(self.range[0], self.range[1])
	
	def signalGenerator(self):
		invoke_time,yield_time = 0,0
		while True:
			if(invoke_time-yield_time < self.delay/1000):
				sleep(self.delay/1000-(invoke_time-yield_time))
			yield_time = time()
			yield self.rand_value()
			invoke_time = time()

if __name__=="__main__":
	testScaffold = SigProcessorScaffold(1000)
	signal = testScaffold.signal
	while True:
		print(next(signal))