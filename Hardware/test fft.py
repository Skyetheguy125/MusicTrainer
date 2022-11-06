import scipy.fft as fft
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

SAMPLE_RATE = 66.66  # Hertz
DURATION = 3  # Seconds
DATA_POINTS = 200  # Samples

#Use Pandas to read sample csv
df = pd.read_csv('sample200.csv', header=None)
#rint(df)

#Take channel 0 only and convert to a list
result = df[0].tolist()
#print(result)

#Attempt FFT
N = math.ceil(SAMPLE_RATE * DURATION)
yf = fft.rfft(result)
xf = fft.rfftfreq(N, (SAMPLE_RATE / DATA_POINTS))
plt.plot(xf, np.abs(yf))
plt.xlabel("Frequency")
plt.ylabel("Stuff")
plt.grid()
plt.show()
