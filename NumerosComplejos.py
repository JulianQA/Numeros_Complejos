
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
    print(a,b)
    first = a[0] * b[0]
    second = a[0] * b[1]
    third = a[1] * b[0]
    fourth = a[1] * b[1]
    ent = first-fourth
    imag = second+third
    return ent,imag
#Hacer el conjugado
def conju(a):
    res = (a[0],a[1]*-1)
    return res

#Hacer la division
def division(a,b):
    arriba = multiplicacion(a,conju(b))
    abajo = (b[0]**2)+(b[1]**2)
    ent = arriba[0]/abajo
    imag = arriba[1]/abajo
    return ent,imag

#Hacer el modulo
def modulo(a):
    res = round(((a[0]**2 + a[1]**2)**0.5),2)
    return res

#Hacer fase
def fase(a):
    div = abs(a[1]/a[0])
    res = math.atan(div)
    return round(math.degrees(res),2)
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
    first = round((r * coseno),2)
    second = round((r * seno),2)
    return first,second

#Hacer suma de vectores
def suma_vectores(v1,v2):
    lis_res = []
    if len (v1) == len (v2):
        for i in range(len(v1)):
            res = suma(v1[i],v2[i])
            lis_res.append(res)
        return lis_res

#Hacer inversa de vectores
def inversa_vectores(v1):
    lis_res = []
    for i in v1:
        oper = (i[0]*-1,i[1]*-1)
        lis_res.append(oper)
    return lis_res


#Hacer multiplicacion de vectores
def multi_escalar_vec(esc,v1):
    lis_res = []
    for i in v1:
        oper = (i[0]*esc,i[1]*esc)
        lis_res.append(oper)
    return lis_res

#Hacer suma de matrices
def suma_matrices(m1,m2):
    filas = len(m1)
    for i in range(len(m1)):
        x = len(m1[i])
    cols = x
    matriz = [[0]*cols for i in range(filas)]
    for a in range(filas):
        for b in range(cols):
            matriz[a][b] = suma(m1[a][b],m2[a][b])
    return matriz

#Hacer multiplicacion de martices
def multi_matrices(esc,m1):
    filas = len(m1)
    for i in range(len(m1)):
        x = len(m1[i])
    cols = x
    print(filas,cols)
    matriz_res = [[None]*cols for i in range(filas)]
    for a in range(filas):
        for b in range(cols):
            matriz_res[a][b] = multiplicacion((esc,0),m1[a][b])
    return matriz_res

