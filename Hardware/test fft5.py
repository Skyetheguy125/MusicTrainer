import scipy.fft as fft
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

SAMPLE_RATE = 25  # Hertz
DURATION = 8  # Seconds
DATA_POINTS = 200  # Samples
N = math.ceil(SAMPLE_RATE * DURATION)

#Use Pandas to read sample csv
df = pd.read_csv('sample860.csv', header=None)
#print(df)

#Take channel 0 only and convert to a list
result = df[0].tolist()

x = np.linspace(0, DURATION, N, endpoint=False)
plt.plot(x, result)
plt.title("Plot CSV")
plt.xlabel("Time (seconds)")
plt.ylabel("ADC Value")
plt.grid()
plt.show()