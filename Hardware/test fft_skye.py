from scipy.fft import rfft, rfftfreq
from scipy.signal import find_peaks
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import os
from random import choice



#(SAMPLE_RATE * DURATION) MUST EQUAL DATA_POINTS
DATA_POINTS = 1000  # Samples
# DURATION = .112  # Seconds
SAMPLE_RATE = 3000  # Hertz

#Use Pandas to read sample csv
df = pd.read_csv('Hardware/3k_uke/uke_4th_string_4.csv', header=None)
#print(df)
files = os.listdir("Hardware/3k_uke")
ran_file = choice(files)
print(ran_file)
#Take channel 0 only and convert to a list
result = df[0].tolist()
# result = result[:500]
# print(len(result))
#print(result[-1])
sos = signal.butter(10, [240,1200], 'bp', fs=3000, output='sos')
filtered = signal.sosfilt(sos, result)
yf = rfft(filtered)
xf = rfftfreq(1000, 1 / SAMPLE_RATE)
# xf = xf[:]
# plt.plot(xf, np.abs(yf))
plt.plot(filtered)
plt.plot(result)
print(xf[np.argmax(yf)])
plt.show()
