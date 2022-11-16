import scipy.fft as fft
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

#(SAMPLE_RATE * DURATION) MUST EQUAL DATA_POINTS
DATA_POINTS = 1000  # Samples
DURATION = .112  # Seconds
SAMPLE_RATE = (DATA_POINTS / DURATION)  # Hertz

#Use Pandas to read sample csv
df = pd.read_csv('Hardware/1000samples_1pluck.csv', header=None) #G4 / 392 Hz
#print(df)

#Take channel 0 only and convert to a list
result = df[0].tolist()
#print(result[-1])

#Attempt FFT
N = math.ceil(SAMPLE_RATE * DURATION)
B = (SAMPLE_RATE / DATA_POINTS)
B2 = (1 / SAMPLE_RATE)
yf = fft.rfft(result)
l = np.min(np.abs(yf))
yf = [l if x < 22 else yf[x] for x in range(len(yf))] #zero out low frequency
q1,q3 = np.percentile(yf[22:], [25,75]) #find quartiles (ignoring low frequency)
iqr = q3 - q1 #find interquartile range
fence_high = q3 + (1.5 * iqr) #statistical cutoff for outliers (high end)
fence_low = q1 - (1.5 * iqr) #statistical cutoff for outliers (low end)
yf = [0 if fence_low <= i <= fence_high else i for i in yf] #if the value is an outlier, keep it; otherwise, zero it
xf = np.arange(0,501)
xf = xf * B
print(xf)
plt.plot(xf[1:], np.abs(yf[1:]))
plt.title("Test FFT 1")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
