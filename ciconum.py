# Samuel Fandiño #

num1=input('Introduzca el primer número ')
num1=int(num1)

num2=input('Introduzca el segundo número ')
num2=int(num2)

while num1 >= num2:
    num2=input('Introduzca el segundo número nuevamente ')
    num2=int(num2)
print('Los números introducidos  fueron: '+str(num1)+' '+str(num2))



