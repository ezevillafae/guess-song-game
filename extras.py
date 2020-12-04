import pygame
from pygame.locals import *
from configuracion import *
import time
import re
import random
def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")


def dibujar(screen, palabraUsuario, lista, puntos, segundos, ayuda):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (190, 570))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 10))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<10):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

    #muestra el nombre
    screen.blit(defaultFont.render(ayuda, 1, COLOR_PELI), (ANCHO//2-len(ayuda)*TAMANNO_LETRA//4,(TAMANNO_LETRA)))

    #muestra las 2 lineas
    screen.blit(defaultFontGrande.render(lista[0], 1, COLOR_LETRAS), (ANCHO//2-len(lista[0])*TAMANNO_LETRA_GRANDE//4,(TAMANNO_LETRA_GRANDE)*2))
    screen.blit(defaultFontGrande.render(lista[1], 1, COLOR_LETRAS), (ANCHO//2-len(lista[1])*TAMANNO_LETRA_GRANDE//4,(TAMANNO_LETRA_GRANDE)*4))

def pantallaNueva(screen, puntos):
    #Arma la nueva posicion del jugador y carga las demas
    listaJugadores = armar(puntos,screen)
    #Limpiar pantalla anterior
    screen.fill(COLOR_FONDO)
    #tamaños de letra
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    #muestra titulo
    rank="ranking top 10"
    screen.blit(defaultFontGrande.render(rank.upper(), 1, COLOR_TIEMPO_FINAL), (340,10))
    #muestra zolapas
    lineaRank="puesto      nombre     puntos"
    screen.blit(defaultFont.render(lineaRank.upper(), 1, COLOR_TEXTO), (340,80))
    posi=80
    print(listaJugadores)
    #ordeno los jugadores de mayor a menor
    listaJugadores.sort(key=len, reverse=True)
    print(listaJugadores)
    for i in range(len(listaJugadores)):
        if i == 0:
            lineaRank=str(i+1) + "." +"                 "+ listaJugadores[i][len(listaJugadores[i])-4:len(listaJugadores[i])]+"                 " + listaJugadores[i][0:len(listaJugadores[i])-4]
            posi+=50
            screen.blit(defaultFont.render(lineaRank, 1,COLOR_PRI), (350,posi))
        if i == 1:
            lineaRank=str(i+1) + "." +"                 "+ listaJugadores[i][len(listaJugadores[i])-4:len(listaJugadores[i])]+"                 " + listaJugadores[i][0:len(listaJugadores[i])-4]
            posi+=50
            screen.blit(defaultFont.render(lineaRank, 1,COLOR_SEG), (350,posi))
        if i == 2:
            lineaRank=str(i+1) + "." +"                 "+ listaJugadores[i][len(listaJugadores[i])-4:len(listaJugadores[i])]+"                 " + listaJugadores[i][0:len(listaJugadores[i])-4]
            posi+=50
            screen.blit(defaultFont.render(lineaRank, 1,COLOR_TER), (350,posi))

        if i < 10 and i>2:
            lineaRank=str(i+1) + "." +"                 "+ listaJugadores[i][len(listaJugadores[i])-4:len(listaJugadores[i])]+"                 " + listaJugadores[i][0:len(listaJugadores[i])-4]
            posi+=50
            screen.blit(defaultFont.render(lineaRank, 1,COLOR_TEXTO), (350,posi))
    #ejecuta visualizacion de todo lo anterior
    pygame.display.flip()
    #se toma un tiempo para volver a la funcion principal
    time.sleep(1)

def armar(puntos,screen):
    #abre el archivo de jugadores y puntajes, los guarda, los acomoda, les elimina el salto de linea y las guarda en una lista nueva
    archivo=open("scoreJugadores.txt","r", encoding='utf-8') # abre el archivo elegido con unicode.
    listaPlayer = archivo.readlines()
    listaPlayer.sort(reverse = True)
    listaPlayerN=[]
    palabraUsuario=""
    cantPlayer=len(listaPlayer)
    for jugadores in range(cantPlayer):
        lineaN=re.sub("[\n]", "", listaPlayer[jugadores])
        listaPlayerN.append(lineaN)
    print(listaPlayerN)
    print(listaPlayerN[cantPlayer-1][0:len(listaPlayerN[0])-4])
    LineaPBajo=int(listaPlayerN[cantPlayer-1][0:len(listaPlayerN[0])-4])
    print(cantPlayer,puntos,LineaPBajo)
    pos_adec=0
    part1=[]
    part2=[]
    for i in range(cantPlayer):

        if puntos > int(listaPlayerN[i][0:len(listaPlayerN[0])-4]):
            pos_adec=i
            part1.append(listaPlayer[i])
        else:
            part2.append(listaPlayer[i])
    part1.pop(len(part1))
    print(part1," 1   y   2 ",part2)

    print(pos_adec)
    if(cantPlayer<10 or LineaPBajo<puntos):
            i=0
            while i < 1:

                    #limpia pantalla
                    screen.fill(COLOR_FONDO)

                    #tamaño de letra y tipo
                    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)
                    #palabra mensaje ingreso de datos
                    mensaje="Ingrese su nombre (capacidad 3 letras)"
                    screen.blit(defaultFont.render(mensaje, 1, COLOR_TEXTO), (190, 200))
                    #palabra de usuario
                    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (500, 300))
                    #acciona pantalla

                    #Buscar la tecla apretada del modulo de eventos de pygame
                    for e in pygame.event.get():
                        #Ver si fue apretada alguna tecla
                        if e.type == pygame.KEYDOWN:
                            letraApretada = dameLetraApretada(e.key)
                            if len(palabraUsuario)<3:
                                palabraUsuario += letraApretada.upper()
                            if e.key == K_BACKSPACE:
                                palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                            if e.key == K_RETURN and palabraUsuario!="" and palabraUsuario!=" " and len(palabraUsuario)==3:

                                if(cantPlayer<10):
                                    listaPlayerN.append(str(puntos)+" "+palabraUsuario)
                                if(cantPlayer>10 and LineaPBajo<puntos):
                                    part2.append(str(puntos)+" "+palabraUsuario)
                                    print(part2)
                                    listaPlayerN=part2+part1
                                    print(listaPlayerN)


                                i=1
                                #guardar lista en archivo TXT
                                archivoSave = open("scoreJugadores.txt","w")
                                print(listaPlayerN)
                                for i in range(len(listaPlayerN)):
                                   a=archivoSave.write(listaPlayerN[i]+"\n")
                                archivoSave.close()
                    pygame.display.flip()
    return listaPlayerN


def bienVenido(screen1,segundos):

    back=pygame.image.load("back.jpg").convert()# imagen de fondo

    fondo()#musica de fondo

    i=0

    while i < 1:

                    #limpia pantalla
                    screen1.fill(COLOR_FONDO1)
                    #posicionamiento de la imagen
                    screen1.blit(back,[-200,-150])
                    #tamaño de letra y tipo
                    defaultFontGrande= pygame.font.Font(  "./fonts/BabyBlue.otf", 80)
                    defaultFont= pygame.font.Font(  "./fonts/BabyBlue.otf", 40)
                    defaultFont1= pygame.font.Font( "./fonts/BabyBlue.otf", 70)

                    #textos de la pantalla bienvenida
                    mensaje="Cancionero"
                    screen1.blit(defaultFontGrande.render(mensaje, 1, COLOR_FONDO), (400, 100))

                    cartel="presione"
                    screen1.blit(defaultFont.render(cartel, 1, COLOR_FONDO), (480, 200))

                    infor="Integrantes:Toledo , Trejo y villafañe"
                    screen1.blit(defaultFont.render(infor, 1, COLOR_FONDO), (0, 550))

                    empezar="ENTER"


                    #cambia de color el texto enter
                    azar=random.choice((0,1))
                    print(azar)
                    if(azar==1):
                        print("rnte")
                        screen1.blit(defaultFont1.render(empezar, 1, COLOR_FONDO), (460, 300))

                    if(azar==0):
                        print("entre")
                        screen1.blit(defaultFont1.render(empezar, 1, COLOR_VIOLET), (460, 300))





                    #Buscar la tecla apretada del modulo de eventos de pygame
                    for e in pygame.event.get():
                        #Ver si fue apretada alguna tecla
                        if e.type == pygame.KEYDOWN:

                            if e.key == K_RETURN:
                                segundos = TIEMPO_MAX +  pygame.time.get_ticks()/1000
                                return
                                dificul()
                    pygame.display.flip()

def acert():
    SonidoN("./sonidos/acert.mp3")

def acer_Seg():
    SonidoN("./sonidos/segui.mp3")

def no_Acert():
    SonidoN("./sonidos/noacert.mp3")

def endG():
    SonidoN("./sonidos/endG.mp3")

def fondo():
    SonidoN("./sonidos/fondo.mp3")

def SonidoN(ruta):
                pygame.mixer.music.load(ruta)
                pygame.mixer.music.play()
                time.sleep(1)

