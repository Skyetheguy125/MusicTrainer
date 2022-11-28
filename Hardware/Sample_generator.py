from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import rfft, rfftfreq
from scipy.signal import find_peaks
from scipy import signal
import matplotlib.pyplot as plt
import math
import os
from random import choice





DATA_POINTS = 10000  # Samples
# DURATION = .112  # Seconds
SAMPLE_RATE = 3000  # Hertz
# Number of sample points
N = 1000
# sample spacing
T = 1.0 / 3000.0
x = np.linspace(0.0, N*T, N, endpoint=False)
y = np.sin(329.0 * 2.0*np.pi*x)
yf = rfft(y)
xf = rfftfreq(N, T)[:N//2]
xf1 = rfftfreq(1000, 1 / SAMPLE_RATE)
import matplotlib.pyplot as plt
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
# plt.plot(xf1, np.abs(yf))

plt.grid()
print("raw unfiltered 3" ,xf[np.argmax(yf)])
plt.show()
