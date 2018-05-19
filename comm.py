import serial
from move import puerto


datos = str(serial.Serial.readline(puerto))
if int(datos.find("arriba"))== 2 :
    mov=(datos[2:len("arriba")+2])
if int(datos.find("abajo"))==2 :
    mov=(datos[2:len("abajo")+2])
if int(datos.find("derecha")) == 2:
    mov=(datos[2:len("derecha") + 2])
if int(datos.find("izquierda")) == 2:
    mov=(datos[2:len("izquierda") + 2])


