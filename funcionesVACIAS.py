from configuracion import *
from regex import *
import random
import math
import unicodedata

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
    modificarArtistaYCancion(primeraLinea,artistaYcancion) #llena la lista artistaYcancion
    modificarLetra(cancion,letra) #llena la lista letra

def seleccion(letra):#elige uno al azar, devuelve ese y el siguiente
    azar=random.randrange(0,len(letra)-1) #del 0 al anteultimo
    siguiente = azar + 1 
    return [letra[azar],letra[siguiente]]

def puntos(n):
    if n > 0: #Si acierta
        if n >= 3: #Si acerto 3 veces
            return 2 ** n
        else:
            return 2
    else:
        return -2 


def esCorrecta(palabraUsuario, artistaYcancion, correctas):
    for respuesta in artistaYcancion:
        if palabraUsuario == respuesta:
            correctas += 1
            return puntos(correctas)
    correctas = 0 #Si es incorrecta vuelve a cero
    return puntos(correctas)




