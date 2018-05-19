# Samuel #

print('Conversor de unidades')

o=1
result=0
result2=0
result=float(result)
result2=float(result2)

while(o==1):
    print('1.Conversor de centimetros a pulgadas')
    print('2.Conversor de pulgadas a centimetros')
    print('3.Conversor de metros/segundos a kilometros/hora')
    print('4.Conversor de kilometros/segundos a ,etros/segundos')
    print('5.Conversor de kilometros a millas')
    print('6.Conversor de millas a kilometros')
    print('7.Conversor de UA a año luz')
    print('8.Conversor de año luz a UA')
    print('9.Salida')
    print()
    opc=input('Que opción desea ')
    opc=int(opc)
    print()
    if opc==1:
        print('Conversor de centimetros a pulgadas')
        cm=input('Introduzca el número de centimetros a convertir ')
        cm=float(cm)
        result = cm/2.54
        print('Son '+str(result)+' pulgadas')
        print()
    if opc==2:
        print('Conversor de pulgadas a centimetros')
        pul=input('Introduzca el número de pulgadas a convertir ')
        pul=float(pul)
        result = pul* 2.54
        print('Son ' + str(result) + ' centimetros')
        print()
    if opc==3:
        print('Conversor de metros/segundos a kilometros/horas')
        ms=input('Introduzca el número de metros/segundos a convertir ')
        ms=float(ms)
        result = ms*3.6
        print('Son ' + str(result) + ' kilometros sobre horas')
        print()
    if opc==4:
        print('Conversor de kilometros/horas a metros/segundos')
        kmh=input('Introduzca el número de kilometros a convertir ')
        kmh=float(kmh)
        result = kmh/3.6
        print('Son ' + str(result) + ' metros sobre segundos')
        print()
    if opc==5:
        print('Conversor de kilometros a millas')
        km = input('Introduzca el número de kilometros a convertir ')
        km=float(km)
        result = km/1.6
        print('Son ' + str(result) + ' millas')
        print()
    if opc==6:
        print('Conversor de millas a kilometros')
        mil= input('Introduzca el número de millas a convertir ')
        mil=float(mil)
        result = mil*1.6
        print('Son ' + str(result) + ' pulgadas')
        print()
    if opc==7:
        print('Conversor de UA a año luz')
        ua = input('Introduzca el número de UA a convertir ')
        ua=float(ua)
        result = ua/63241.1
        print('Son ' + str(result) + ' años luz')
        print()
    if opc==8:
        print('Conversor de años luz a UA')
        al = input('Introduzca el número de años luz a convertir ')
        al=float(al)
        result = al*63241.1
        print('Son ' + str(result) + ' UA')
        print()
    if opc==9:
        o=0
