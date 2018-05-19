" Samuel, Nicolas, Santiago, Julian, Sebastian"

meses= ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
festivos=["1,8", "No tiene", "19,29,30", "No tiene", "1,14", "4,11", "2,20", "7,20", "No tiene", "15", "5,12", "8,25"]

Dic={"mes": meses}
print(Dic["mes"])
m=input("Escoja un mes enter 1 y 12: ")
print("El mes escogido es: "+meses[int(m)-1]+" y  sus festivos son: "+festivos[int(m)-1])


