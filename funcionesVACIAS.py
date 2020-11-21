from configuracion import *
from regex import *
import random
import math
import unicodedata

def modificarArtistaYCancion(cadena,artistaYCancion):
    """toma la cadena, filtra caracteres especiales y agrega cada 
    frase que este separada por ; en un nuevo elemento de la lista artistaYCancion"""
    cadena = filtrar(cadena)
    cadena = cadena + ";" #se agrega un ; al final para recorrer toda la cadena
    elemento = ""
    for letra in cadena:
        if letra != ";":
            elemento = elemento + letra    
        else:
            artistaYCancion.append(elemento)
            elemento = ""
            
# ALERTA : LOS VERSOS DE LA LETRA NO ESTAN LIMITADOS 
def modificarLetra(datosArchivo,letra):
    """Toma una lista y devuelve una nueva lista con elementos sin caracteres especiales y tildes"""
    for i in range(len(datosArchivo)):
        linea = filtrar(datosArchivo[i])
        letra.append(linea)

def lectura(archivo, letra, artistaYcancion): #se queda solo con los oraciones de cierta longitud y filtra tildes por ej
    datosArchivo = archivo.readlines()
    primeraLinea = datosArchivo[0]
    cancion = datosArchivo[1:]
    modificarArtistaYCancion(primeraLinea,artistaYcancion) #toma la primera linea del archivo y la lista a llenar (artistaYCancion)
    modificarLetra(cancion,letra) #toma los elementos menos el primero y la lista a llenar (letra)

def seleccion(letra):#elige uno al azar, devuelve ese y el siguiente
    return (["linea 1","linea 2"])

def puntos(n):
    #devuelve el puntaje, segun seguidilla
    return 5


def esCorrecta(palabraUsuario, artistaYCancion, correctas):
    #chequea que sea correcta, que pertenece solo a la frase siguiente. Devuelve puntaje segun seguidilla
    return puntos(1)




