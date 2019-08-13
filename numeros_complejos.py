import math
#Hacer la suma
def suma(a,b):
    ent = a[0]+b[0]
    imag = a[1]+b[1]
    return ent,imag


#Hacer la resta
def resta(a,b):
    ent = a[0]-b[0]
    imag = a[1]-b[1]
    return ent,imag


#Hacer la multiplicacion
def multiplicacion(a,b):
    first = a[0] * b[0]
    second = a[0] * b[1]
    third = a[1] * b[0]
    fourth = a[1] * b[1]
    ent = first-fourth
    imag = second+third
    return ent,imag
#Hacer el conjugado
def conju(a):
    a[0],a[1] = a[0],-a[1]
    return a
#Hacer la division
def division(a,b):
    arriba = multiplicacion(a,conju(b))
    abajo = (b[0]**2)+(b[1]**2)
    ent = arriba[0]/abajo
    imag = arriba[1]/abajo
    return ent,imag
#Hacer el modulo
def modulo(a):
    res = (a[0]**2 + a[1]**2)**0.5
    return res
#Hacer fase
def fase(a):
    div = abs(a[1]/a[0])
    res = math.atan(div)
    return math.degrees(res)
#Hacer Polar
def polar(a):
    r = modulo(a)
    ang = fase(a)
    return r,ang
#Hacer Cartesiano
def cartesiano(a):
    r = a[0]
    ang = a[1]
    coseno = math.cos(ang)
    seno = math.sin(ang)
    first = r * coseno
    second = r * seno
    return first,second
#Hacer Pruebas
def pruebas():
    number1 = [2,3]
    number2 = [1,-5]
    resSuma = (3,-2)
    resResta = (1,8)
    resMulti = (17,-7)
    resDivi = (-0.5,0.5)
    if suma(number1,number2) == resSuma and resta(number1,number2) == resResta and multiplicacion(number1,number2) == resMulti :
        print('Suma:',suma(number1,number2))
        print('Resta:',resta(number1,number2))
        print('Multiplicación:',multiplicacion(number1,number2))
        print('División:',division(number1,number2))
        print("Las operaciones son correctas")
    else:
        print('Las operaciones son incorrectas')


pruebas()

