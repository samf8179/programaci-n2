import time
from tkinter import*

ventana=Tk()
lienzo=Canvas(ventana,width=500,height=500)

lienzo.pack()
lienzo.create_rectangle(200,350,300,450,fill='red')
Tk.update(ventana)
time.sleep(3)

tecla=1
tecla=str(tecla)

while tecla!='finish':
    tecla=input("Introduzca una letra para moviento: ")

    if tecla=='w':
        lienzo.move(1,0,-100)
        Tk.update(ventana)
        time.sleep(1)

    if tecla=='s':
        lienzo.move(1,0,50)
        Tk.update(ventana)
        time.sleep(1)

    if tecla=='a':
        lienzo.move(1,-40,0)
        Tk.update(ventana)
        time.sleep(1)
    if tecla=='d':
        lienzo.move(1,35,0)
        Tk.update(ventana)
        time.sleep(1)
