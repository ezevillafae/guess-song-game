from configuracion import *
from extras import playSoundAcert,playSoundAcertBonus,playSoundError
from regex import *
import random
import math
import unicodedata

def modificarArtistaYCancion(primeraLinea,artistaYcancion):
    """toma la cadena, filtra caracteres especiales y agrega los elemenos a la lista separados por ;"""
    primeraLinea = filtrar(primeraLinea)
    for e in primeraLinea.split(";"):
        artistaYcancion.append(e)
    print(artistaYcancion) #respuestas
            
def modificarLetra(cancion,letra):
    """Toma una lista y devuelve una nueva lista con elementos sin caracteres especiales y tildes"""
    for i in range(len(cancion)):
        linea = filtrar(cancion[i])
        if len(linea)> 1 and len(linea)<51: # para que entre en la pantalla y no tome lineas vacias
            letra.append(linea)

def lectura(archivo, letra, artistaYcancion):
    """Lee las lineas del archivo y llena las listas letra y artistaycancion filtando caracteres especiael y tildes"""
    datosArchivo = archivo.readlines()
    primeraLinea = datosArchivo[0] #guardo la primera linea
    cancion = datosArchivo[1:] #guardo las demas lineas
    modificarArtistaYCancion(primeraLinea,artistaYcancion) #llena la lista artistaYcancion
    modificarLetra(cancion,letra) #llena la lista letra

def seleccion(letra):#elige uno al azar, devuelve ese y el siguiente
    azar=random.randrange(0,len(letra)-1) 
    siguiente = azar + 1 
    return [letra[azar],letra[siguiente]]

def puntos(n):
    if n > 0: #Si acierta
        if n >= 3: #Si acerto 3 veces o mas
            playSoundAcertBonus() #sonido de bonus
            return 2 ** n
        else:
            playSoundAcert() #sonido de acierto
            return 2
    else:
        playSoundError() #sonido de error
        return -2 


def esCorrecta(palabraUsuario, artistaYcancion, correctas):
    for respuesta in artistaYcancion:
        if palabraUsuario == respuesta:
            correctas += 1
            return puntos(correctas)
    correctas = 0 #Si es incorrecta vuelve a cero
    return puntos(correctas)




