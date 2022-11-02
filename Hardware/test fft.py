#Uses code from https://realpython.com/python-scipy-fft/ and https://towardsdatascience.com/music-in-python-2f054deb41f4
import scipy.fft as fft
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

SAMPLE_RATE = 44100  # Hertz
DURATION = 5  # Seconds

def generate_sine_wave(freq, duration, sample_rate = 44100, amplitude = 4096):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = amplitude * np.sin((2 * np.pi) * frequencies)
    return x, y


def get_piano_notes():
    # White keys are in Uppercase and black keys (sharps) are in lowercase
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
    base_freq = 440  # Frequency of Note A4
    keys = np.array([x + str(y) for y in range(0, 9) for x in octave])
    # Trim to standard 88 keys
    start = np.where(keys == 'A0')[0][0]
    end = np.where(keys == 'C8')[0][0]
    keys = keys[start:end + 1]

    note_freqs = dict(zip(keys, [2 ** ((n + 1 - 49) / 12) * base_freq for n in range(len(keys))]))
    note_freqs[''] = 0.0  # stop
    return note_freqs

def fourier(filename):
    fs, data = wavfile.read(filename) # load the data
    a = data.T[0] # this is a two channel soundtrack, I get the first track
    b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
    c = fft.rfft(b) # create a list of complex number
    d = len(c)//2  # you only need half of the fft list
    k = np.arange(len(data))
    T = len(data) / fs  # where fs is the sampling frequency
    frqLabel = k / T
    #max_y = max(c)
    #max_x = T[c.argmax()]
    #print("max_x: ", max_x)
    plt.plot(abs(c[:(d-1)]),'r')
    plt.xlim((0, 2000))
    plt.grid()
    plt.show()

#_, nice_tone = generate_sine_wave(400, DURATION, SAMPLE_RATE)
#_, noise_tone = generate_sine_wave(4000, DURATION, SAMPLE_RATE)
#noise_tone = noise_tone * 0.3

#mixed_tone = nice_tone + noise_tone

#normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)

#note_freqs = get_piano_notes()
#frequency = note_freqs['C4']

#sin_wave = generate_sine_wave(frequency, DURATION, SAMPLE_RATE, 2048)
#normalized_tone = np.int16((sin_wave))

#N = SAMPLE_RATE * DURATION
#yf = fft.fft(sin_wave)
#xf = fft.fftfreq(N, 1 / SAMPLE_RATE)

#print("yf: ", yf)
#print("xf: ", xf)

#plt.plot(xf, np.abs(yf))
#plt.show()

fourier('piano-c4.wav') #for piano_c4.wav, peak is either 0 or 726
