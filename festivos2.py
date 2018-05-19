" Samuel, Nicolas, Santiago, Julian, Sebastian"

meses= ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
festivos=["1,8", "No tiene", "19,29,30", "No tiene", "1,14", "4,11", "2,20", "7,20", "No tiene", "15", "5,12", "8,25"]

Dic={"mes": meses, "festivo": festivos}
print(Dic["mes"])
m=input("Escoja un mes enter 1 y 12: ")
m=int(m)
m-=1
" 0 Y 11 son las posiciones entre las que se encuentre el arreglo "
if(m>11 or m<0):
    print("Número no válido")
else:
    print("El mes escogido es: "+Dic["mes"][m]+" y sus festivos son: "+Dic["festivo"][m])


