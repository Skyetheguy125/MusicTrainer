import scipy.fft as fft
import scipy.signal.windows as win
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import parabolic
import time

def freq_from_HPS(sig, fs):
    """
    Estimate frequency using harmonic product spectrum (HPS)
    """
    windowed = sig * win.blackmanharris(len(sig))

    from pylab import subplot, plot, log, copy, show

    # harmonic product spectrum:
    c = abs(fft.rfft(windowed)[22:135])
    maxharms = 8
    subplot(maxharms, 1, 1)
    plot(log(c))
    for x in range(2, maxharms):
        a = copy(c[::x])  # Should average or maximum instead of decimating
        max(c[::x],c[1::x],c[2::x],...)
        c = c[:len(a)]
        i = np.argmax(abs(c))
        #true_i = parabolic(abs(c), i)[0]
        print('Pass %d: %f Hz' % (x, fs * i / len(windowed)))
        c *= a
        subplot(maxharms, 1, x)
        plot(log(c))
    show()

#(SAMPLE_RATE * DURATION) MUST EQUAL DATA_POINTS
DATA_POINTS = 1000  # Samples
DURATION = .112  # Seconds
SAMPLE_RATE = (DATA_POINTS / DURATION)  # Hertz

#Use Pandas to read sample csv
df = pd.read_csv('Samples/uke_3rd_string_0.csv', header=None)
#print(df)

#Take channel 0 only and convert to a list
result = df[0].tolist()
print("Length: ", len(result))

#Attempt function
print('Calculating frequency from FFT:', end=' ')
start_time = time.time()
print('%f Hz' % freq_from_HPS(result, SAMPLE_RATE))
print('Time elapsed: %.3f s\n' % (time.time() - start_time))