import scipy.fft as fft
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

#(SAMPLE_RATE * DURATION) MUST EQUAL DATA_POINTS
SAMPLE_RATE = 25  # Hertz
DURATION = 8  # Seconds
DATA_POINTS = 200  # Samples

#Use Pandas to read sample csv
df = pd.read_csv('sample860.csv', header=None)
#print(df)

#Take channel 0 only and convert to a list
result = df[0].tolist()
#print(result)

#Attempt FFT
N = math.ceil(SAMPLE_RATE * DURATION)
B = (SAMPLE_RATE / DATA_POINTS)
B2 = (1 / SAMPLE_RATE)
yf = fft.rfft(result)
xf = fft.rfftfreq(N, B)
print(len(xf))
plt.plot(xf[1:], np.abs(yf[1:]))
plt.title("Test FFT 1")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
