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
    return (["linea 1","linea 2"])

def puntos(n):
    #devuelve el puntaje, segun seguidilla
    return 5


def esCorrecta(palabraUsuario, artistaYCancion, correctas):
    #chequea que sea correcta, que pertenece solo a la frase siguiente. Devuelve puntaje segun seguidilla
    return puntos(1)




