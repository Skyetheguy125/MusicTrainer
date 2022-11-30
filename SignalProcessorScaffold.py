"""
This is a testing scaffold to simulate output from the signal processing method.
It is used by constructing a SigProcessorScaffold object with the desired delay and range.
"""
from random import seed, uniform
from time import sleep, time

class SigProcessorScaffold:
	"""
	Class wrapping the characteristics and functions for a scaffold simulating signal processor output.
	Public attributes:
		* .delay: numeric -	in miliseconds, the minimum time between generation of new output values
		* .range: 2-element indexable -	the lower and upper bounds for output values
	Public methods:
		* .wait_and_read() -> float -	waits for at most {delay} ms, then updates output value and returns it
		* .read_latest() -> float -	if output value is more than {delay} ms old, updates it; returns output value without waiting
	Private attributes:
		* ._signal: PyGen_Type (float) -	generator object implementing waiting and random value generation
		* ._last_yield: float -	time of last output value update (given by time.time())
		* ._last_value: float -	saved value of last output
	Private methods:
		* ._rand_value(): float - wraps random.uniform(self.range[0],self.range[1])
		* ._signalGenerator(): PyGen_Type (float)-	function used to generate self._signal
	"""
	def __init__(self, delay=10, range=(0,5000)):
		"""
		delay - in miliseconds, the minimum time between generations of new output values
		range - any 2-element indexable object, where range[0] is the lowest value and range[1] the highest value for the output
		"""
		self.delay = delay
		self.range = range
		self._signal = self._signalGenerator()
		self._last_yield = 0
		self._last_value = None
	
	def _rand_value(self):
		"""returns uniform value between self.range[0] and self.range[1]"""
		return uniform(self.range[0], self.range[1])
	
	def _signalGenerator(self):
		"""returns a generator that yields a value in {self.range} at most every {self.delay} ms"""
		while True:
			now = time()
			if(now-self._last_yield < self.delay/1000):
				sleep(self.delay/1000-(now-self._last_yield))
			self._last_yield = time()
			self._last_value = self._rand_value()
			yield self._last_value
	
	def wait_and_read(self):
		"""
		returns a fresh output value. If it is too soon to generate a new value, waits (i.e. hangs/sleeps) until a new one can be generated, then outputs it.
		"""
		return next(self._signal)
	
	def read_latest(self):
		"""
		returns an output value no more than {self.delay} seconds old without waiting. If output value is outdated, updates it and returns it; otherwise, returns )self._last_value without waiting.
		"""
		now = time()
		if(now-self._last_yield > self.delay/1000):
			return next(self._signal)
		else:
			return self._last_value

class SmartSignalScaffold(SigProcessorScaffold):
	"""
	Simulates a signal processor being fed an input that is controlled, i.e. that attempts to reach a given reference value.
	"""
	def __init__(self, refBuf, delay=10, range=(0,5000),rate=0.1):
		"""
		delay - in miliseconds, the minimum time between generations of new output values
		range - any 2-element indexable object, where range[0] is the lowest value and range[1] the highest value for the output
		refBuf - buffer for interthread communication, carries the current reference (target) value
		rate - Speed at which the controller adjusts (proportional constant)
		"""
		self.delay = delay
		self.range = range
		self.rate = rate
		self._referenceBuffer = refBuf
		self._signal = self._signalGenerator()
		self._last_yield = 0
		self._last_value = uniform(self.range[0], self.range[1])
		self._last_err = 0
	
	def _next_value(self,r):
		"""calculates the next value, given a reference value"""
		Kp, Kd = self.rate, 0
		err = self._last_value - r
		#print(err)
		return self._last_value - Kp*err - Kd*(err-self._last_err)
	
	def _signalGenerator(self):
		while True:
			now = time()
			r = self._referenceBuffer.get()
			if(now-self._last_yield < self.delay/1000):
				sleep(self.delay/1000-(now-self._last_yield))
			self._last_yield = time()
			self._last_value = self._next_value(r)
			#print(r,self._last_value)
			yield self._last_value

if __name__=="__main__":
	#Use examples

	#Low delay, narrow band output
	fast_narrow_signal = SigProcessorScaffold(10,(100,200))
	#High delay, vocal range output
	slow_signal = SigProcessorScaffold(1000)

	#Read fast signal 20 times as fast as it will allow
	for i in range(20):
		print(fast_narrow_signal.wait_and_read())
	
	#Read slow signal 20 times, once every quarter second, regardless of output age
	for i in range(20):
		print(slow_signal.read_latest())
		sleep(.25)