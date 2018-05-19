''' Samuel Fandiño
Marzo 3 2018
Primer código en Python'''

print("Samuel Fandiño")
print("Programacion 2")
print("Edad 14")
print("Grado 9 - Liceo de Cervantes \n")
# el \n es para saltar de linea y dejar un espacio #

# Calculadora #


a=input("Ingrese el primer valor: ")
b=input("Ingrese el segundo valor: ")
a=int(a)
b=int(b)


c=a+b
print("La suma de los 2 números es: "+ str(c))
c=a-b
print("La resta de los dos números es: "+ str(c))
c=a*b
print("La multiplicación de los dos números es: "+ str(c))
c=a/b
print("La división de los dos números es: "+ str(c))

# suma de cadenas #

cad1="Hola mudo"
cad2="me llamo Samuel"

cad3=cad1+"  "+cad2

print(cad3)