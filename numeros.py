# Samuel Fandiño #
# Marzo 17 2018 #

pr=0
rest=0
prr=0
prp=0
num=input("Introduzca un número: ")
num=int(num)
if (num<1):
    print("Número no válido, ingrese el valor de nuevo")
rest=float(rest)
rest=num%2
if  (rest==0):
    print("El número es par")
else:
    print("El número es impar")

pr=float(pr)
prr=float(prr)
prp=float(prp)
pr=num%2
if (pr==0):
    print("El número no es primo")
else:
    pr=num%3
    prr=num%5
    prp=num&7
    if(pr==0 or prr==0 or prp==0) and num!=3:
        print("El número no es primo")
    else:
        print("El número es primo")


