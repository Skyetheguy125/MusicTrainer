import scipy.fft as fft
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

SAMPLE_RATE = 33.33  # Hertz
DURATION = 3  # Seconds

#Use Pandas to read sample csv
df = pd.read_csv('sample.csv', header=None)
#print(df)

#Take channel 0 only and convert to a list
result = df[0].tolist()
#print(result)

#Attempt FFT
N = math.ceil(SAMPLE_RATE * DURATION)
yf = fft.rfft(result)
xf = fft.rfftfreq(N, 1 / SAMPLE_RATE)
plt.plot(xf, np.abs(yf))
plt.xlabel("Frequency")
plt.ylabel("Stuff")
plt.grid()
plt.show()

#Plot data
#plt.plot(result)
#plt.xlabel('Time')
#plt.ylabel('Amplitude')
#plt.title('Boop')
#plt.grid()
#plt.show()
