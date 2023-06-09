import serial
import time
import csv

port = 'COM5'
baud = 115200
k = 0

f = open('dataStoreNew.csv', 'w', newline='')
f.truncate()

serialCom = serial.Serial(port, baud)
serialCom.setDTR(False)
time.sleep(1)
serialCom.flushInput()
serialCom.setDTR(True)


dataPoints = 2001

for k in range(dataPoints):
    try:
        s_bytes = serialCom.readline()
        decoded_bytes = s_bytes.decode('utf-8').strip('\r\n')
        #print(decoded_bytes)

        if k == 0:
            values = decoded_bytes.split(',')
        else:
            values = [float(x) for x in decoded_bytes.split()]
        print(values)

        writer = csv.writer(f, delimiter=',')
        writer.writerow(values)

    except:
        print('Error, not recorded')
