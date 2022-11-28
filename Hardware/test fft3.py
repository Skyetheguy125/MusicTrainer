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

filename = 'Hardware/Samples/11_21_12_50/uke_1st_string_0.csv'

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
<<<<<<< HEAD
i = np.argmax(abs(yf[220:1350])) + 221 # Just use this for less-accurate, naive version
print(abs(yf[220:1350]))
print("Max: ", i)
plt.plot(xf[220:1350], abs(yf[220:1350]))
=======
i = np.argmax(abs(yf[22:135])) + 22 # Just use this for less-accurate, naive version
print(abs(yf[22:135]))
print("Max: ", i/.122)
plt.plot([i/.112 for i in xf[22:135]], abs(yf[22:135]))
>>>>>>> a362da2822befbc9a5911086afba21513bf22e43
plt.title("File")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.grid()
plt.show()