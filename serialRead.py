import serial
import time
import csv

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 250000, timeout=1)
    ser.reset_input_buffer()

    numSamples = 0
    start = time.monotonic()
    with open('output.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        while numSamples < 1000:
            if ser.in_waiting > -0:
                line = ser.readline().rstrip()
                decodeLine = line.decode('UTF-8',errors='ignore')
                numSamples += 1
                csvwriter.writerow(decodeLine)

    end = time.monotonic()
    runtime = end - start
    print(runtime)
