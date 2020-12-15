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
        matrizPuntajes.append(nombreYPuntaje) #agrego la lista nombreYpuntaje a la lista matrizPuntajes
    archivo.close()

def puntajesMaximos(matrizPuntajes):
    """
    toma la matriz y devuelve el puntaje mas alto de cada nombre sin repetir
    matrizPuntajes[i][0] nombre del elemento
    matrizPuntajes[i][1] puntaje del elemento 
    """
    lista_nueva = []
    nombres = nombresSinRepetir(matrizPuntajes) #obtengo los nombres de la matriz pero sin repetir
    puntajeNombreActual = 0
    for nombre in nombres: #itero sobre los nombres
        puntajeNombreActual = puntajeMaximoDeNombre(matrizPuntajes,nombre) #obtengo el puntaje maximo de ese nombre
        lista_nueva.append([nombre,str(puntajeNombreActual)]) #agrego el nombre y su puntaje maximo

    return lista_nueva

def nombresSinRepetir(matrizPuntajes):
    """Se obtienen los nombres de la matriz pero sin repetirlos"""
    repetidos = []
    for i in range(len(matrizPuntajes)):
        if not(matrizPuntajes[i][0] in repetidos): #si el nombre no está en repetidos
            repetidos.append(matrizPuntajes[i][0])
    return repetidos


def puntajeMaximoDeNombre(matrizPuntajes,nombre):
    """se obtiene el puntaje maximo de un determinado nombre"""
    maximo = -9999999
    
    for i in range(len(matrizPuntajes)): #recorro por indice 
        nombreActual = matrizPuntajes[i][0] #nombre 
        puntajeActual = int(matrizPuntajes[i][1]) #puntaje
        if nombreActual == nombre: #si el nombre de la matriz coincide con el nombre pasado por parametro
            if puntajeActual > maximo:
                maximo = puntajeActual

    return maximo

def ordenarPorPuntajes(matrizPuntajes):
    """ordena los elementos de la matriz segun su puntaje, de mayor a menor"""
    return sorted(matrizPuntajes, key=lambda x : int(x[1]),reverse=True)


def borrarArchivoRanking():
    """Se sobrescribe el archivo scoreJugadores.txt y se borra todo su contenido"""
    archivo = open("scoreJugadores.txt","w",encoding="utf-8")
    archivo.write("")
    archivo.close()