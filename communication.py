"""
import serial
from serial import SerialException

ser = serial.Serial()


# to list ports run the following command in shell
# python3 -m serial.tools.list_ports
def connect_ethercat0():
    ser.baudrate = 115200
    ser.port = '/dev/ttyACM0'
    try:
        ser.open()
        return True
    except SerialException:
        return False


def connect_ethercat1():
    ser.baudrate = 115200
    ser.port = '/dev/ttyACM1'
    ser.timeout = 1
    try:
        ser.open()
        return True
    except SerialException:
        return False


def connect_ethercat2():
    ser.baudrate = 115200
    ser.port = '/dev/ttyACM2'
    try:
        ser.open()
        return True
    except SerialException:
        return False


def connect_ethercat3():
    ser.baudrate = 115200
    ser.port = '/dev/ttyACM3'
    try:
        ser.open()
        return True
    except SerialException:
        return False


def read_data():
    data_in = ser.readline()
    if data_in == 'Y':
        return True
    else:
        return False


def write_data(data_out):
    formatted_data = data_out.encode()
    ret = ser.write(formatted_data)
    return ret
"""
