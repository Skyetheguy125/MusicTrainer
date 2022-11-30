import serial
import time
import csv

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.reset_input_buffer()

    numSamples = 0
    start = time.monotonic()

    f = open('output.csv', 'w')
    writer = csv.writer(f)


    while numSamples < 10000:
        if ser.in_waiting > 0:
            line = ser.readline().rstrip()
            decodeLine = line.decode('UTF-8',errors='ignore')
            numSamples += 1
            # decodeLine.translate({ord('"'): None})
            if (decodeLine.isdigit()):
                writer.writerow([decodeLine])
            else:
                writer.writerow([0])
            # writer.writerow(line)

    end = time.monotonic()
    runtime = end - start
    print(runtime)
    f.close()
