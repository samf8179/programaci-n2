import serial

puerto = serial.Serial('/dev/tty.usbmodem1411')
while(True):
    datos = str(serial.Serial.readLine(puerto))
    print(datos)

