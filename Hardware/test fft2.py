import scipy.fft as fft
import scipy.signal.windows as win
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import parabolic
import time

def freq_from_fft(sig, fs):
    """
    Estimate frequency from peak of FFT
    """
    # Compute Fourier transform of windowed signal
    windowed = sig * win.hann(len(sig))
    #print(len(sig))
    #print(len(windowed))
    f = fft.rfft(windowed)
    #print(f)

    # Find the peak and interpolate to get a more accurate peak
    i = np.argmax(abs(f[22:135])) + 22 # Just use this for less-accurate, naive version
    print("Max: ", i)
    #true_i = parabolic(math.log(abs(f)), i)[0]

    # Convert to equivalent frequency
    return fs * i / len(windowed) #swap between i and true_i


#(SAMPLE_RATE * DURATION) MUST EQUAL DATA_POINTS
DATA_POINTS = 10000  # Samples
DURATION = 3.35  # Seconds
SAMPLE_RATE = 3000  # Hertz

#Use Pandas to read sample csv
df = pd.read_csv('Samples/uke_4th_string_1.csv', header=None)
#print(df)

#Take channel 0 only and convert to a list
result = df[0].tolist()
print("Length: ", len(result))

#Attempt function
print('Calculating frequency from FFT:', end=' ')
start_time = time.time()
f = fft.rfft(result)
i = np.argmax(abs(f[220:1350])) + 221 # Just use this for less-accurate, naive version
#print("Max: ", i)
#print("B: ", (SAMPLE_RATE / len(result)))
print('%f Hz' % freq_from_fft(result, SAMPLE_RATE))
#print('%f Hz' % ((SAMPLE_RATE / len(result)) * i)) #swap between i and true_i
print('Time elapsed: %.3f s\n' % (time.time() - start_time))
