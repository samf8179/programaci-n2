import time 
from tkinter import*
import serial

puerto = serial.Serial('/dev/tty.usbmodem1411')

ventana=Tk()
lienzo=Canvas(ventana,width=500,height=500)

lienzo.pack()
lienzo.create_rectangle(200,350,300,400,fill='red')
Tk.update(ventana)
time.sleep(3)

mov="0"

while True:
    datos = str(serial.Serial.readLine(puerto))
    if int(datos.find("arriba")) == 2:
        mov = (datos[2:len("arriba") +2])
    if int(datos.find("abajo")) == 2:
        mov = (datos[2:len("abajo") + 2])
    if int(datos.find("derecha")) == 2:
        mov = (datos[2:len("derecha") + 2])
    if int(datos.find("izquierda")) == 2:
        mov = (datos[2:len("izquierda") + 2])


