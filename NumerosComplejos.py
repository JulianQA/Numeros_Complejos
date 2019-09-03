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
    matriz = [[0]*(len(m1[0])) for i in range(len(m1))]
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        for a in range(len(m1)):
            for b in range(len(m1[0])):
                matriz[a][b] = suma(m1[a][b],m2[a][b])
        return matriz
    else:
        return False

#Hacer multiplicacion de martices por escalar
def multi_matrices(esc,m1):
    matriz_res = [[None]*len(m1[0]) for x in range(len(m1))]
    if type(esc) is not tuple:
        esc = (esc,0)
    for a in range(len(m1)):
        for b in range(len(m1[a])):
            matriz_res[a][b] = multiplicacion(esc,m1[a][b])
    return matriz_res

#Hacer Transpuesta
def transpuesta(m1):
    matriz_res = [[None]*len(m1[0]) for i in range(len(m1))]
    
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            matriz_res[i][j] = m1[j][i]
    return matriz_res

#Inversa de una matriz
def inver_matriz(m1):
    res  = multi_matrices(-1,m1)
    return res

#Matriz conjugada
def mat_conjugada(m1):
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            m1[i][j] = conju(m1[i][j])
    return m1

#Matriz_adjunta
def mat_adjunta(m1):
    c = mat_conjugada(transpuesta(m1))
    return c
# Multipllicacion de  Matrices
def multiplicacion_matrices(m1,m2):
    matriz_res = [[(0,0)]*len(m2[0]) for i in range(len(m1))]
    cos = 0
    if len(matriz_res) == 1:
        cos = 1
        
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(matriz_res)+cos):
                matriz_res[i][j] = suma(matriz_res[i][j],multiplicacion(m1[i][k],m2[k][j]))
    return matriz_res

#Revisar si es unitaria
def unit(m1):
    res = multiplicacion_matrices(m1,mat_adjunta(m1))
    identidad = [[(0,0)]*len(m1) for i in range(len(m1))]
    for i in range(len(identidad)):
            identidad[i][i] = (1,0)
    if res == identidad:
        return True
    else:
        return False
#Revisar si es hermitian
def hermitian(m1):
    if mat_adjunta(m1) == m1:
        return True
    else:
        return False
#Producto tensor entre vectores
def producto_tensor_vector(v1,v2):
    res = []
    for i in range(len(v1)):
        for j in range(len(v2)):
            res.append(multiplicacion(v1[i],v2[j]))
    return res

#Producto tensor entre matrices
def producto_tensor_matriz(m1,m2):
    res = []
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            res.append((multi_matrices(m1[i][j],m2)))
    return res
def accion(v,m):
    res = multiplicacion_matrices(v,m)
    return res

#Hacer Norma
def norma(m1):
    res = 0
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res += (m1[i][j][0])**2 + (m1[i][j][1])**2
    raiz = round(res**0.5,2)
    return raiz
#distancia entre matrices
def distancia(m1,m2):
    res = [[(0,0)]*len(m1[0]) for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res[i][j] = resta(m1[i][j],m2[i][j])
    h = norma(res)
    return h
    
    
