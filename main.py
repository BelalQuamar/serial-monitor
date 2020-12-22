import serial
from time import sleep
import sys

arguments = sys.argv
COM = arguments[1]
BAUD = arguments[2]
print(BAUD)
ser = serial.Serial(COM, BAUD, timeout = .1)

print('Waiting for device');
#sleep(3)
print(ser.name)

while True:
	val = str(ser.readline().decode().strip('\r\n'))#Capture serial output as a decoded string
	#valA = val.split("/")
	#print()
	if val:
                print(val)
                #print("\n")
