import scipy.fft as fft
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def test_fft(file):
	#(SAMPLE_RATE * DURATION) MUST EQUAL DATA_POINTS
	DATA_POINTS = 1000  # Samples
	DURATION = .112  # Seconds
	SAMPLE_RATE = (DATA_POINTS / DURATION)  # Hertz

	#Use Pandas to read sample csv
	df = pd.read_csv('Hardware/Samples/{}'.format(file), header=None)
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
	#print(yf)

if __name__=="__main__":
	files = os.listdir("Hardware/Samples/11_21_12_50")
	for f in files:
		print(f)
		test_fft("11_21_12_50/"+f)