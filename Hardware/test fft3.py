import scipy.fft as fft
import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

#(SAMPLE_RATE * DURATION) MUST EQUAL DATA_POINTS
DATA_POINTS = 10000  # Samples
DURATION = 3.35  # Seconds
SAMPLE_RATE = 3000  # Hertz

filename = 'Samples/uke_3rd_string_0.csv'

#Use Pandas to read sample csv
df = pd.read_csv(filename, header=None)
#print(df)

#Take channel 0 only and convert to a list
result = df[0].tolist()

#Stuff
B = (SAMPLE_RATE / DATA_POINTS)
yf = fft.rfft(result)
xf = np.arange(0,5001)
#xf = xf * B

#Plot FFT
i = np.argmax(abs(yf[220:1350])) + 221 # Just use this for less-accurate, naive version
print(abs(yf[220:1350]))
print("Max: ", i)
plt.plot(xf[220:1350], abs(yf[220:1350]))
plt.title("File")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.grid()
plt.show()