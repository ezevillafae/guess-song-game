from configuracion import *
from regex import *
import random
import math
import unicodedata

def modificarArtistaYCancion(cadena,artistaYcancion):
    """toma la cadena, filtra caracteres especiales y agrega los elemenos a la lista separados por ;"""
    cadena = filtrar(cadena)
    print(cadena)
    for e in cadena.split(";"):
        artistaYcancion.append(e)
            
# ALERTA : SE QUEDA CON TODAS LAS ORACIONES 
def modificarLetra(datosArchivo,letra):
    """Toma una lista y devuelve una nueva lista con elementos sin caracteres especiales y tildes"""
    for i in range(len(datosArchivo)):
        linea = filtrar(datosArchivo[i])
        letra.append(linea)

def lectura(archivo, letra, artistaYcancion): #se queda solo con los oraciones de cierta longitud y filtra tildes por ej
    datosArchivo = archivo.readlines()
    primeraLinea = datosArchivo[0] #guardo la primera linea
    cancion = datosArchivo[1:] #guardo las demas lineas
    modificarArtistaYCancion(primeraLinea,artistaYcancion) 
    modificarLetra(cancion,letra)

def seleccion(letra):#elige uno al azar, devuelve ese y el siguiente
    azar=random.randrange(1,N)
    siguiente = azar + 1 
    return [letra[azar],letra[siguiente]]

def puntos(n):
    if n==1 or n==0:
        puntaje+=2
    elif n>1:
        puntaje=puntaje+2**n
    else:
        puntaje=-2
    return puntaje


def esCorrecta(palabraUsuario, artistaYcancion, correctas):
    palnueva=palabraUsuario.strip()
    correct=False
    valor=0
    for palabraUsuario1 in artistaYcancion:
        palnueva1=palabraUsuario1.strip()
        if palnueva == palnueva1:
            correct=True
    if correct==True:
        valor=puntos(correctas)
    else:
        valor=puntos(-1)
    return valor




