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

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (190, 570))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 10))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

    #muestra el nombre
    screen.blit(defaultFont.render(ayuda, 1, COLOR_PELI), (ANCHO//2-len(ayuda)*TAMANNO_LETRA//4,(TAMANNO_LETRA)))

    #muestra las 2 lineas
    screen.blit(defaultFontGrande.render(lista[0], 1, COLOR_LETRAS), (ANCHO//2-len(lista[0])*TAMANNO_LETRA_GRANDE//4,(TAMANNO_LETRA_GRANDE)*2))
    screen.blit(defaultFontGrande.render(lista[1], 1, COLOR_LETRAS), (ANCHO//2-len(lista[1])*TAMANNO_LETRA_GRANDE//4,(TAMANNO_LETRA_GRANDE)*4))

def bienvenidos(screen):
    """Loop pantalla bienvenidos"""
    continuar = False
    dibujarBienvenidos(screen) 
    #intro = pygame.mixer.Sound("sounds/intro.mp3")
    #intro.play()
    
    while not(continuar): # ciclo espera que aprete una tecla para empezar
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            if e.type == pygame.KEYDOWN:
                continuar = True
        pygame.display.update()
        
    #intro.fadeout(2000)
    return pygame.time.get_ticks()/1000 #segundos transcurridos en el menú
    

def dibujarBienvenidos(screen):
    """Crea y muestra los elementos en la pantalla"""

    fuente1 = pygame.font.Font("fonts/Ranchers-Regular.ttf",50)
    textCancionero = fuente1.render("Cancionero",1,COLOR_TEXTO)

    #Insertar en pantalla
    screen.blit(textCancionero,(ANCHO/2,ALTO/2))

def ranking(screen):
    continuar = False
    screen.fill((255,255,255)) # Limpiar pantalla

    dibujarRanking(screen)

    while not(continuar):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.KEYDOWN:
                continuar = True
        pygame.display.update()
            
def dibujarRanking(screen):
    fuente1 = pygame.font.Font(None,40)
    textoTop = fuente1.render("Top Jugadores",1,COLOR_LETRAS)
    

    # Mostrar en pantalla
    screen.blit(textoTop,(0,0))
          