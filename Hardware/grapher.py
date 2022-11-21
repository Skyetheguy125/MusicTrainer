# Simple demo of reading each analog input from the ADS1x15 and printing it to
# the screen.
# Author: Tony DiCola
# License: Public Domain
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime as dt

# Import the ADS1x15 module.
import Adafruit_ADS1x15

#__PLOTTING__
#Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

#Animate graph function
def animate(value, xs, ys):
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(value)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    #plt.xticks(rotation=45, ha='right')
    #plt.subplots_adjust(bottom=0.30)
    plt.title('Sample Plotter')
    plt.ylabel('Number')

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

# Or create an ADS1015 ADC (12-bit) instance.
#adc = Adafruit_ADS1x15.ADS1015()

# Note you can change the I2C address from its default (0x48), and/or the I2C
# bus by passing in these optional parameters:
#adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Main loop.
while True:
    # Read all the ADC channel values in a list.
    #values = [0]*4
    #for i in range(4):
        # Read the specified ADC channel using the previously set gain value.
        #values[i] = adc.read_adc(i, gain=GAIN)

    value = adc.read_adc(0, gain=GAIN)

    #Plot values instead of printing
    ani = animation.FuncAnimation(fig, animate, fargs=(value, xs, ys))#, interval=1000)
    plt.show()

    # Pause for half a second.
    time.sleep(0.5)