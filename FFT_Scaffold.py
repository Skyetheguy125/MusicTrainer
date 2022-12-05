from random import seed, uniform
from time import sleep, time
from scipy.fft import rfft, rfftfreq
from scipy import signal
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from random import choice
import serial


class FFT_Scaffold:
	def __init__(self):
		"""
		delay - in miliseconds, the minimum time between generations of new output values
		range - any 2-element indexable object, where range[0] is the lowest value and range[1] the highest value for the output
		"""
		self._signal = self._signalReader()
		self._last_value = None
		self.DATA_POINTS = 1000  # Samples 
		self.SAMPLE_RATE = 3000  # Hertz
		
	def _signalReader(self):
		"""returns a signal by reading the csv that is updated"""
		ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
		ser.reset_input_buffer()
		while True:
			# sleep(.1)git add
			# df = pd.read_csv('Hardware/3k_uke/uke_4th_string_4.csv', header=None)
			# files = os.listdir("Hardware/3k_uke")
			# ran_file = choice(files)
			# # print(ran_file)
			# df = pd.read_csv('Hardware/3k_uke/{}'.format(ran_file), header=None)

			#print(df)
			
			Temp_list=[]
			numSamples = 0
			# start = time.monotonic()
			while numSamples < self.DATA_POINTS:
				if ser.in_waiting > -0:
					line = ser.readline().rstrip()
					decodeLine = line.decode('UTF-8',errors='ignore')
					numSamples += 1
					# print(decodeLine)
					if (not decodeLine.isdigit()):
						decodeLine = 0
					Temp_list.append(int(decodeLine))

			# result = df[0].tolist()  #SIMULATED DATA
			result=Temp_list #REALTIME DATA
			# result = result[:500]
			# print(len(result))
			#print(result[-1])
			# if(len(result)<self.DATA_POINTS))
			sos = signal.butter(10, [200,1100], 'bp', fs=self.SAMPLE_RATE, output='sos')
			filtered = signal.sosfilt(sos, result)
			yf = rfft(filtered)[10:]
			xf = rfftfreq(self.DATA_POINTS, 1 / self.SAMPLE_RATE)[10:]
			# xf = xf[:]
			# plt.plot(xf, np.abs(yf))
			# plt.plot(filtered)
			# plt.plot(result)
			fund_freq=xf[np.argmax(yf)]
			# print(fund_freq)
			self._last_value = fund_freq
			# print(ran_file)

			yield self._last_value

	def wait_and_read(self):	
		"""
		returns a fresh output value. If it is too soon to generate a new value, waits (i.e. hangs/sleeps) until a new one can be generated, then outputs it.
		"""
		return next(self._signal)
	
	# def _SerialReader(self):
	# 		ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
	# 		ser.reset_input_buffer()

	# 		while True:
	# 			Temp_list=[]
	# 			numSamples = 0
	# 			# start = time.monotonic()
	# 			while numSamples < self.DATA_POINTS:
	# 				if ser.in_waiting > -0:
	# 					line = ser.readline().rstrip()
	# 					decodeLine = line.decode('UTF-8',errors='ignore')
	# 					numSamples += 1
	# 					if (not decodeLine.isdigit()):
	# 						decodeLine = 0
	# 					Temp_list.append(decodeLine)
	# 			self._last_list = Temp_list
	# 			yield self._last_list

					# csvwriter.writerow(decodeLine)


# if __name__=="__main__":
# 	#Use examples

# 	#Low delay, narrow band output
# 	fast_narrow_signal = SigProcessorScaffold(10,(100,200))
# 	#High delay, vocal range output
# 	slow_signal = SigProcessorScaffold(1000)

# 	#Read fast signal 20 times as fast as it will allow
# 	for i in range(20):
# 		print(fast_narrow_signal.wait_and_read())
	
# 	#Read slow signal 20 times, once every quarter second, regardless of output age
# 	for i in range(20):
# 		print(slow_signal.read_latest())
# 		sleep(.25)