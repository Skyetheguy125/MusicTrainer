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
DATA_POINTS = 10000  # Samples
# DURATION = .112  # Seconds
SAMPLE_RATE = 3000  # Hertz

#Use Pandas to read sample csv
df = pd.read_csv('Hardware/10k_sample/uke_2nd_string_1.csv', header=None)
df1 = pd.read_csv('Hardware/10k_sample/uke_2nd_string_2.csv', header=None)

#print(df)
files = os.listdir("Hardware/3k_uke")
ran_file = choice(files)
print(ran_file)
#Take channel 0 only and convert to a list
result = df[0].tolist()
result1 = df1[0].tolist()

# result = result[:500]
# print(len(result))
#print(result[-1])
#frequency x axis create
xf = rfftfreq(10000, 1 / SAMPLE_RATE)[10:] 

#filter
sos = signal.butter(100, [240,1200], 'bp', fs=3000, output='sos')

filtered = signal.sosfilt(sos, result)

yf = rfft(filtered)[10:]
yf1 = rfft(result)[10:]


filtered1 = signal.sosfilt(sos, result1)

yf_1 = rfft(filtered1)[10:]
yf1_1 = rfft(result1)[10:]

# xf = xf[:]
# plt.plot(xf, np.abs(yf_1))
# plt.plot(xf, np.abs(yf))

# plt.plot(filtered1)
plt.plot(result1)
print("filtered 0 ", xf[np.argmax(yf)])
print("raw unfiltered 0" ,xf[np.argmax(yf1)])
print()
print("filtered 3", xf[np.argmax(yf_1)])
print("raw unfiltered 3" ,xf[np.argmax(yf1_1)])

plt.show()
