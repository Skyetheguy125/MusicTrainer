from random import seed, uniform
from time import sleep, time

class SigProcessorScaffold:
	def __init__(self, delay=10, range=(0,5000)):
		"""
		delay - in miliseconds, the minimum time between generations of new output values
		range - any 2-element indexable object, where range[0] is the lowest value and range[1] the highest value for the output
		"""
		self._signal = self._signalReader()
		self._last_yield = 0
		self._last_value = None
        self.DATA_POINTS = 1000  # Samples
        self.SAMPLE_RATE = 3000  # Hertz

	def _signalReader(self):
		"""returns a generator that yields a value in {self.range} at most every {self.delay} ms"""
		while True:
			
            #Use Pandas to read sample csv
            df = pd.read_csv('Hardware/3k_uke/{}'.format(file), header=None)
            #print(df)

            #Take channel 0 only and convert to a list
            result = df[0].tolist()


            #Attempt FFT
            B = (SAMPLE_RATE / DATA_POINTS)
            yf = fft.rfft(result)
            yf = np.power(np.abs(yf),2) #work with power rather than complex value or magnitude
            yf = [0 if x < 22 or x > 135 else yf[x] for x in range(len(yf))] #zero-out out-of-range frequencies
            q1,q3 = np.percentile(yf[22:135], [25,75]) #find quartiles for in-range frequencies
            iqr = q3 - q1 #find interquartile range
            fence_high = q3 + (1.5 * iqr) #statistical cutoff for outliers (high end)
            #fence_low = q1 - (1.5 * iqr) #statistical cutoff for outliers (low end)
            yf1 = [0 if i <= fence_high else i for i in yf] #if the value is an outlier, keep it; otherwise, zero it
            xf = np.arange(0,len(yf))
            xf = xf * B
            #print(xf)
            plt.plot(xf, yf) #plot all data in range
            plt.plot(xf,yf1) #plot only outliers in range (overlaid)
            plt.axhline(fence_high) #visual representation of the cutoff for being an outlier
            #plt.axhline(q3)
            plt.title(file)
            plt.xlabel("Frequency")
            plt.ylabel("Amplitude")
            plt.grid()
            plt.show()

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