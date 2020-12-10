#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *

from funcionesVACIAS import *
from ranking import *

#Funcion principal
def main():


        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("Cancionero...")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #Pantalla de bienvenida
        segmenu = bienvenidos(screen)


        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial
        artistaYcancion=[]
        puntos = 0
        nombre = ""
        matrizPuntajes = []
        palabraUsuario = ""
        letra=[]
        correctas=0
        elegidos= []
        masDeUnaVuelta = False

        #elige una cancion de todas las disponibles
        azar=random.randrange(1,N+1)
        elegidos.append(azar) #la agrega a la lista de los ya elegidos
        archivo= open(".\\letras\\"+str(azar)+".txt","r", encoding='utf-8') # abre el archivo elegido con unicode.


        #lectura del archivo y filtrado de caracteres especiales, la primer linea es el artista y cancion
        lectura(archivo, letra, artistaYcancion)

        #elige una linea al azar y su siguiente
        lista=seleccion(letra)

##        print(lista)

        ayuda = ""
        dibujar(screen, palabraUsuario, lista, puntos, segundos, ayuda)

        while segundos > 0:
        
            gameClock.tick(fps)


            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    quit()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letraApretada = dameLetraApretada(e.key)
                    palabraUsuario += letraApretada
                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                    if e.key == K_RETURN:
                        #chequea si es correcta y suma o resta puntos
                        sumar=esCorrecta(palabraUsuario, artistaYcancion, correctas)
                        print("Puntos +",sumar)
                        puntos+=sumar
                        print("Puntos :",puntos)

                        if sumar>0:
                            correctas=correctas+1
                            print("Correctas ",correctas)
                        else:
                            correctas=0
                            print("Correctas ",correctas)
                        if len(elegidos)==N:
                                elegidos=[]
                                masDeUnaVuelta = True

                        azar=random.randrange(1,N+1)
                        while(azar in elegidos):
                            azar=random.randrange(1,N+1)

                        elegidos.append(azar)

                        if masDeUnaVuelta == True:
                            ayuda = artistaYcancion[0]


                        archivo= open(".\\letras\\"+str(azar)+".txt","r", encoding='utf-8')
                        palabraUsuario = ""
                        #lectura del archivo y filtrado de caracteres especiales
                        artistaYcancion=[]
                        letra = []
                        lectura(archivo, letra, artistaYcancion)
                        #elige una linea al azar y su siguiente
                        lista=seleccion(letra)


            segundos = TIEMPO_MAX + segmenu - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            dibujar(screen, palabraUsuario, lista, puntos, segundos, ayuda)
            pygame.display.update()

        #Pantalla de Ranking
        nombre = pedirNombre(screen)
        escrituraArchivoRanking(nombre,puntos) #guardo nombre y puntos en archivo
        lecturaArchivoRanking(matrizPuntajes) # leo archivo y lleno la matriz
        matrizPuntajes = puntajesMaximos(matrizPuntajes) #obtengo los puntajes maximos 
        matrizPuntajes = ordenarPorPuntajes(matrizPuntajes) #ordeno los puntajes de mayor a menor 
        if len(matrizPuntajes) > 10:
            matrizPuntajes = matrizPuntajes[:10] #tomo solo 10 si la matriz tiene 10 elementos o más
        ranking(screen,matrizPuntajes)
        archivo.close()

#Programa Principal ejecuta Main
while 1:
    main()
