import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('torque_data.txt',index_col=0)
data = data['Torque'].astype(float).values
print(data)

N = data.shape[0] #number of elements
t = np.linspace(0, 300, N)
#t=np.arange(N)
s = data

fft = np.fft.fft(s)
fftfreq = np.fft.fftfreq(len(s))

T = t[1] - t[0]
print(T)

f = np.linspace(0, 1 / T, N)
plt.ylabel("Amplitude")
plt.xlabel("Frequency [Hz]")
plt.plot(fftfreq, np.absolute(fft))
#plt.xlim(0,100)
