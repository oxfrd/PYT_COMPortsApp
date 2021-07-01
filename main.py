
import serial
import serial.rs485


#python -m serial.tools.list_ports      ////////  show all ports in console

ser = serial.Serial('COM6', 38400, timeout=0.75)
print(ser.name)
print(ser.timeout)

modbus = serial.rs485.RS485()
modbus.rs485_mode = serial.rs485.RS485Settings()


ser.close()

