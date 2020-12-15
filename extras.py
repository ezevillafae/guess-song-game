import pygame
from pygame.locals import *
from configuracion import *
import re
from ranking import *

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
    # SE AGREGARON LOS NÚMEROS DEL 0-9 Y LA LETRA Ñ
    elif key == K_0:
        return("0")
    elif key == K_1:
        return("1")
    elif key == K_2:
        return("2")
    elif key == K_3:
        return("3")
    elif key == K_4:
        return("4")
    elif key == K_5:
        return("5")
    elif key == K_6:
        return("6")
    elif key == K_7:
        return("7")
    elif key == K_8:
        return("8")
    elif key == K_9:
        return("9")    
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    elif key == K_SEMICOLON or key == 241: # 241 es el codigo de la ñ
        return("ñ")
    else:
        return("")

# -------------------------------- Pantalla de juego ------------------------------

def dibujar(screen, palabraUsuario, lista, puntos, segundos, ayuda):
    
    fondo = pygame.image.load("imagenes/fondo_1.jpg")
    defaultFont= pygame.font.Font("fonts/FRADM.TTF", TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( "fonts/FRADM.TTF", TAMANNO_LETRA_GRANDE)
    linea1 = defaultFontGrande.render(lista[0], 1, COLOR_LETRAS)
    linea2 = defaultFontGrande.render(lista[1], 1, COLOR_LETRAS)


    screen.blit(fondo,(0,0))
    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (181.52, 458.09))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (825, 31))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (38, 31))

    #muestra la ayuda
    screen.blit(defaultFont.render(ayuda, 1, COLOR_PELI), (ANCHO//2-len(ayuda)*TAMANNO_LETRA//4,33))

    #muestra las 2 lineas
    screen.blit(linea1, (ANCHO/2-linea1.get_width()/2,187.04))
    screen.blit(linea2, (ANCHO/2-linea2.get_width()/2,238.24))

# ------------------------------ Pantalla bienvenidos ------------------------------------

def bienvenidos(screen,matrizPuntajes):
    """Loop pantalla bienvenidos"""

    reloj = pygame.time.Clock() # reloj para controlar fps
    continuar = False 
    numImagen = 1 #contador para la animacion

    intro = playSoundIntro() #sonido intro

    """Crea los elementos de la pantalla"""
    imagen = pygame.image.load("imagenes/intro_"+str(numImagen)+".jpg").convert()
    fuente1= pygame.font.Font("fonts/FRAHV.TTF",18)
    fuente2 = pygame.font.Font("fonts/framd.ttf",15)
    pressEnterText = fuente1.render("PRESIONE ENTER PARA JUGAR",1,COLOR_BLANCO)
    botonRanking = fuente2.render("RANKING",1,COLOR_BLANCO)
    botonSalir = fuente2.render("SALIR",1,COLOR_BLANCO)
    botonOpciones = fuente2.render("OPCIONES",1,COLOR_BLANCO)
    
    while not(continuar): # ciclo espera que aprete una tecla para empezar
        reloj.tick(2) #fps 2

        # contador para la animacion
        if numImagen == 1:
            numImagen = 2
        elif numImagen == 2:
            numImagen = 1

        #Insertar en pantalla
        imagen = pygame.image.load("imagenes/intro_"+str(numImagen)+".jpg").convert() #en cada ciclo se cambia la imagen
        screen.blit(imagen,(0,0))
        screen.blit(pressEnterText,(ANCHO/2-pressEnterText.get_width()/2,451.48))
        #Guardo las superficies/rectangulos de los botones
        superficieBotonRanking = screen.blit(botonRanking, (ANCHO/3-botonRanking.get_width()/2, 510))
        superficieBotonOpciones = screen.blit(botonOpciones,(ANCHO/2-botonOpciones.get_width()/2,510))
        superficieBotonSalir = screen.blit(botonSalir,(682.66-botonSalir.get_width()/2,510))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == K_RETURN:
                    continuar = True
            # Eventos de los botones MOUSE POR ARRIBA
            if e.type == pygame.MOUSEMOTION: # Cambio de color cuando el mouse pasa por arriba 
                # BOTON RANKING
                if superficieBotonRanking.collidepoint(e.pos):
                    botonRanking = fuente2.render("RANKING",1,COLOR_LETRAS) #cambia de color
                else:
                    botonRanking = fuente2.render("RANKING",1,COLOR_BLANCO)
                #BOTON SALIR
                if superficieBotonSalir.collidepoint(e.pos):
                    botonSalir = fuente2.render("SALIR",1,COLOR_LETRAS) #cambia de color
                else:
                    botonSalir = fuente2.render("SALIR",1,COLOR_BLANCO)
                #BOTON OPCIONES
                if superficieBotonOpciones.collidepoint(e.pos):
                    botonOpciones = fuente2.render("OPCIONES",1,COLOR_LETRAS) #cambia de color
                else:
                    botonOpciones = fuente2.render("OPCIONES",1,COLOR_BLANCO)
            # Eventos de los botones CLICK
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1: # si es el boton izquierdo
                    #BOTON RANKING
                    if superficieBotonRanking.collidepoint(e.pos): #entro a la pantalla de ranking    
                        ranking(screen,matrizPuntajes)
                    #BOTON SALIR
                    if superficieBotonSalir.collidepoint(e.pos): #salgo del juego
                        quit()
                    if superficieBotonOpciones.collidepoint(e.pos): #entro a la pantalla de opciones
                        opciones(screen,matrizPuntajes)
                       

        pygame.display.update()
    intro.fadeout(2000) #baja el volumen durante 2 seg
    return pygame.time.get_ticks()/1000 #segundos transcurridos en el menú
    
    
# ---------------------------------- Pantalla Opciones -----------------------------------

def opciones(screen,matrizPuntajes):
    screen.fill(COLOR_FONDO)
    continuar = False

    #crear elementos
    imagen = pygame.image.load("imagenes/fondo_opciones.gif").convert()
    fuente1 = pygame.font.Font("fonts/FRAHV.TTF",25)
    fuente2 = pygame.font.Font("fonts/FRADM.TTF",18)
    textoBorrarRanking = fuente1.render("BORRAR RANKING",1,COLOR_BLANCO)
    pressEnterText = fuente2.render("PRESIONE ENTER PARA VOLVER AL MENÚ",1,COLOR_BLANCO)
    
    while not(continuar):

        screen.blit(imagen,(0,0))
        screen.blit(pressEnterText,(ANCHO/2-pressEnterText.get_width()/2,500))
        superficieBotonBorrarRanking = screen.blit(textoBorrarRanking,(ANCHO/2-textoBorrarRanking.get_width()/2,250))
        
        for e in pygame.event.get():
            if e.type == QUIT:
                quit()
            if e.type == KEYDOWN:
                if e.key == K_RETURN:
                    continuar = True
            if e.type == pygame.MOUSEMOTION:
                if superficieBotonBorrarRanking.collidepoint(e.pos):
                    textoBorrarRanking = fuente1.render("BORRAR RANKING",1,COLOR_LETRAS)
                else:
                    textoBorrarRanking = fuente1.render("BORRAR RANKING",1,COLOR_BLANCO)
            if e.type == pygame.MOUSEBUTTONDOWN:
                if superficieBotonBorrarRanking.collidepoint(e.pos):
                    borrarArchivoRanking()
                    print("Historial Archivo Borrado")
        pygame.display.update()

    

# --------------------------------- Pantalla Pedir Nombre ---------------------------------

def pedirNombre(screen):
    """Pantalla de pedir nombre retorna el nombre que ingresa el usuario"""
    nombre = ""
    reloj = pygame.time.Clock()
    screen.fill(COLOR_FONDO) #limpiar pantalla anterior
    continuar = False

    while not(continuar):
        reloj.tick(30)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == K_RETURN and len(nombre)>0: #tecla enter
                    continuar = True
                nombre = nombre + dameLetraApretada(e.key)
                nombre = nombre.upper()
                if e.key == K_BACKSPACE:
                    nombre = nombre[0:len(nombre)-1]
        dibujarPedirNombre(screen,nombre)
        pygame.display.update()
    
    return nombre

def dibujarPedirNombre(screen,nombre):
    """Se encarga de dibujar los elementos en la pantalla """
    imagen = pygame.image.load("imagenes/fondo_introducir_nombre.jpg")
    fuente1= pygame.font.Font("fonts/FRADM.TTF",18)
    fuente1Grande = pygame.font.Font("fonts/FRAHV.TTF",36) 
    introduzcaNombreText = fuente1.render("INTRODUZCA SU NOMBRE",1,COLOR_BLANCO)
    nombreText = fuente1Grande.render(nombre,1,COLOR_BLANCO)

    screen.blit(imagen,(0,0))
    screen.blit(introduzcaNombreText,(405,200))
    screen.blit(nombreText,(ANCHO/2-nombreText.get_width()/2,269))

# -------------------------------- Pantalla Ranking ----------------------------------------

def ranking(screen,matrizPuntajes):
    continuar = False
    
    lecturaArchivoRanking(matrizPuntajes) # leo archivo y lleno la matriz
    matrizPuntajes = puntajesMaximos(matrizPuntajes) #obtengo los puntajes maximos 
    matrizPuntajes = ordenarPorPuntajes(matrizPuntajes) #ordeno los puntajes de mayor a menor 
    if len(matrizPuntajes) > 10:
        matrizPuntajes = matrizPuntajes[:10] #tomo solo 10 si la matriz tiene 10 elementos o más
    
    screen.fill((COLOR_FONDO)) # Limpiar pantalla
    while not(continuar):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == K_RETURN:
                    continuar = True

        dibujarRanking(screen,matrizPuntajes)
        pygame.display.update()

            
def dibujarRanking(screen,matrizPuntajes):
    """se encarga de dibujar todos los elementos de la matriz en la pantalla de ranking"""
    fuente1 = pygame.font.Font("fonts/FRADM.TTF",18)
    fondo = pygame.image.load("imagenes/top_1.jpg")
    pressEnterText = fuente1.render("PRESIONE ENTER PARA VOLVER AL MENÚ",1,COLOR_BLANCO)

    #variables para ubicar elementos en la pantalla
    posXNombre = 250
    posXPuntaje = 450
    posXTop = 100
    posYTopNombrePuntos = 200  
    textTop = 1

    # Mostrar en pantalla
    screen.blit(fondo,(0,0))
    screen.blit(pressEnterText,(155,500))
    for i in range(len(matrizPuntajes)):
        nombreActual = matrizPuntajes[i][0] #nombre
        puntajeActual = matrizPuntajes[i][1] #puntaje
        screen.blit(fuente1.render(str(textTop),1,COLOR_LETRAS),(posXTop,posYTopNombrePuntos))
        textTop = textTop + 1 #numero de posicion
        screen.blit(fuente1.render(nombreActual,1,COLOR_LETRAS),(posXNombre,posYTopNombrePuntos))
        screen.blit(fuente1.render(puntajeActual,1,COLOR_LETRAS),(posXPuntaje,posYTopNombrePuntos))
        posYTopNombrePuntos = posYTopNombrePuntos + 25 #para que se ubiquen abajo los siguientes elementos

# ----------------------------- Sonidos ----------------------------------

def playSoundAcert():
    sonido = pygame.mixer.Sound("sounds/sonido_acierto_1.ogg")
    sonido.play()
    return sonido

def playSoundAcertBonus():
    sonido = pygame.mixer.Sound("sounds/sonido_aciertobonus_1.ogg")
    sonido.play()
    return sonido

def playSoundError():
    sonido = pygame.mixer.Sound("sounds/sonido_error_1.ogg")
    sonido.play()
    return sonido

def playSoundIntro():
    sonido = pygame.mixer.Sound("sounds/intro.ogg")
    sonido.play()
    return sonido