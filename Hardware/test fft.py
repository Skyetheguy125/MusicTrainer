import scipy.fft as fft
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import pandas as pd

SAMPLE_RATE = 20  # Hertz
DURATION = 0.05  # Seconds

#Use Pandas to read sample csv
df = pd.read_csv('sample.csv', header=None)
#print(df)

#Take channel 0 only and convert to a list
result = df[0].tolist()
#print(result)

#Plot List
plt.plot(result)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Boop')
plt.grid()
plt.show()
