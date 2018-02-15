import sys
import time
import serial

ser = serial.Serial(
    port=sys.argv[1],
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)
ser.isOpen()
ser.write('\n'.encode())
time.sleep(1)
input_data = ser.read(ser.inWaiting())
print input_data
with open(sys.argv[2]) as f:
    content = f.readlines()

for current in range(len(content)):
     if content[current].startswith("!") != True:
        ser.write(content[current])
        time.sleep(1)
        input_data = ser.read(ser.inWaiting())
        print input_data
