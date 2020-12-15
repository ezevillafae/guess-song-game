def escrituraArchivoRanking(nombre,puntos):
    """Escribe nombre y puntos en la ultima linea del archivo"""
    archivo = open("scoreJugadores.txt","a",encoding="utf-8")
    linea = nombre + " " +str(puntos) + "\n"
    archivo.write(linea)
    archivo.close()

def lecturaArchivoRanking(matrizPuntajes):
    """Lee el archivo de los puntajes y llena la matriz puntajes"""
    archivo = open("scoreJugadores.txt", "r",encoding="utf-8")
    lineaActual = ""
    for linea in archivo.readlines():
        lineaActual = linea.replace("\n","") #saco el salto de linea
        nombreYPuntaje = lineaActual.split(" ") #hago una lista con el nombre y puntaje
        matrizPuntajes.append(nombreYPuntaje) #agrego ese elemento a la lista general
    archivo.close()

def puntajesMaximos(matrizPuntajes):
    """
    toma la matriz y devuelve el puntaje mas alto de cada nombre
    matrizPuntajes[i][0] nombre del elemento
    matrizPuntajes[i][1] puntaje del elemento 
    """
    lista_nueva = []
    nombres = nombresRepetidos(matrizPuntajes)
    puntajeNombreActual = 0
    for nombre in nombres:
        puntajeNombreActual = puntajeMaximoDeNombre(matrizPuntajes,nombre)
        lista_nueva.append([nombre,str(puntajeNombreActual)])

    return lista_nueva

def nombresRepetidos(matrizPuntajes):
    repetidos = []

    for i in range(len(matrizPuntajes)):
        if not(matrizPuntajes[i][0] in repetidos):
            repetidos.append(matrizPuntajes[i][0])


    return repetidos


def puntajeMaximoDeNombre(matrizPuntajes,nombre):
    maximo = -9999999
    
    for i in range(len(matrizPuntajes)):
        nombreActual = matrizPuntajes[i][0]
        puntajeActual = int(matrizPuntajes[i][1])
        if nombreActual == nombre:
            if puntajeActual > maximo:
                maximo = puntajeActual

    return maximo

def ordenarPorPuntajes(matrizPuntajes):
    return sorted(matrizPuntajes, key=lambda x : int(x[1]),reverse=True)


def borrarArchivoRanking():
    archivo = open("scoreJugadores.txt","w",encoding="utf-8")
    archivo.write("")
    archivo.close()