import pygame
from pygame.locals import *
from configuracion import *

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
    elif key == 241: #241 es el codigo de la ñ
        return("ñ")
    else:
        return("")


def dibujar(screen, palabraUsuario, lista, puntos, segundos, ayuda):
    fondo = pygame.image.load("imagenes/fondo_1.jpg")
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #Linea Horizontal
    screen.blit(fondo,(0,0))

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (190, 570))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (825, 33))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (38, 33))

    #muestra el nombre
    screen.blit(defaultFont.render(ayuda, 1, COLOR_PELI), (ANCHO//2-len(ayuda)*TAMANNO_LETRA//4,33))

    #muestra las 2 lineas
    screen.blit(defaultFontGrande.render(lista[0], 1, COLOR_LETRAS), (ANCHO//2-len(lista[0])*TAMANNO_LETRA_GRANDE//4,187.04))
    screen.blit(defaultFontGrande.render(lista[1], 1, COLOR_LETRAS), (ANCHO//2-len(lista[1])*TAMANNO_LETRA_GRANDE//4,238.24))

# ------------------------------ Pantalla bienvenidos ------------------------------------

def bienvenidos(screen):
    """Loop pantalla bienvenidos"""
    reloj = pygame.time.Clock()
    continuar = False
    contador = 1
    #intro = pygame.mixer.Sound("sounds/intro.mp3")
    #intro.play()
    
    while not(continuar): # ciclo espera que aprete una tecla para empezar
        reloj.tick(2)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            if e.type == pygame.KEYDOWN:
                continuar = True
        if contador == 1:
            dibujarBienvenidos(screen,contador)
            contador = 2
        elif contador == 2:
            dibujarBienvenidos(screen,contador)
            contador = 1 
        pygame.display.update()
        
    #intro.fadeout(2000)
    return pygame.time.get_ticks()/1000 #segundos transcurridos en el menú
    

def dibujarBienvenidos(screen,contador):
    """Crea y muestra los elementos en la pantalla"""
    imagen = pygame.image.load("imagenes/intro_"+str(contador)+".jpg").convert()

    

    #Insertar en pantalla
    screen.blit(imagen,(0,0))

# -------------------------------- Pantalla Ranking ----------------------------------------

def ranking(screen):
    continuar = False
    screen.fill((255,255,255)) # Limpiar pantalla


    while not(continuar):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.KEYDOWN:
                continuar = True

        dibujarRanking(screen)
        pygame.display.update()

            
def dibujarRanking(screen):
    fuente1 = pygame.font.Font(None,40)
    fondo = pygame.image.load("imagenes/top_1.jpg")    

    # Mostrar en pantalla
    screen.blit(fondo,(0,0))

def lecturaArchivoRanking():
    pass