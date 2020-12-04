from configuracion import *
from regex import *
import random
import math
import unicodedata
from extras import *

def modificarArtistaYCancion(cadena,artistaYcancion):
    """toma la cadena, filtra caracteres especiales y agrega los elemenos a la lista separados por ;"""
    cadena = filtrar(cadena)
    for e in cadena.split(";"):
        artistaYcancion.append(e)
    print(artistaYcancion)
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
    puntaje=0
    if n==1 or n==0:
        acert()
        puntaje+=2
    elif n>1:
        acer_Seg()
        puntaje=puntaje+2**n
    else:
        no_Acert()
        puntaje=-2
    return puntaje


def esCorrecta(palabraUsuario, modificarArtistaYCancion, correctas):
    palnueva=palabraUsuario.strip()
    print(modificarArtistaYCancion)
    correct=False

    valor=0
    for palabraUsuario1 in modificarArtistaYCancion:
        print(palnueva,modificarArtistaYCancion)
        palnueva1=palabraUsuario1.strip()
        if palnueva == palnueva1:
            correct=True

    if correct==True:
        valor=puntos(correctas)
    else:
        valor=puntos(-1)

    return valor



