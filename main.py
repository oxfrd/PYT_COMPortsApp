
import serial
import serial.rs485


#python -m serial.tools.list_ports      ////////  show all ports in console

ser = serial.Serial('COM5', 115200, timeout=1)
print(ser.name)
print(ser.timeout)
print(ser.is_open)
x=0
while x < 200:
    print(ser.read(50))
    x=x+1

ser.close()

