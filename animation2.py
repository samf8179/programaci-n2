import time
from tkinter import*

flag=True

def arriba():
    lienzo.move(1, 0, -100)
    Tk.update(ventana)
    time.sleep(1)
def abajo():
    lienzo.move(1, 0, 50)
    Tk.update(ventana)
    time.sleep(1)
def izquierda():
    lienzo.move(1, -40, 0)
    Tk.update(ventana)
    time.sleep(1)
def derecha():
    lienzo.move(1, 35, 0)
    Tk.update(ventana)
    time.sleep(1)
def salir():
    global flag
    flag=False

ventana=Tk()
btn1=Button(ventana,text="arriba",command=arriba)
btn2=Button(ventana,text="abajo",command=abajo)
btn3=Button(ventana,text="izquieda",command=izquierda)
btn4=Button(ventana,text="derecha",command=derecha)
btn5=Button(ventana,text="salir",command=salir)

lienzo=Canvas(ventana,width=500,height=500)
lienzo.pack()
lienzo.create_rectangle(200,350,300,450,fill='red')

Tk.update(ventana)

btn1.pack(side="top")
btn2.pack(side="bottom")
btn3.pack(side="left")
btn4.pack(side="right")
btn5.pack()

while(flag):
    Tk.update(ventana)

tecla=1
tecla=str(tecla)



