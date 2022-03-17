import pygame
from Player import Player
import time
import sys
from jeu import Jeu


# from Grid import Grid
taille_fenetre = (640, 480)

def fonctions_player():
    player.render()
    player.update(0, 0, [])

le_jeu = Jeu()


pygame.init()
pygame.font.init()

pygame.display.set_caption('pizzagario')

screen = pygame.display.set_mode(taille_fenetre)

player = Player(screen)


# def demarrer_jeu():
#     fonctions_player()

def ecran_de_chargement():
    screen.fill((0,255,0))

    # grille  = Grid(screen, taille_fenetre)
while True:
    time.sleep(0.01)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # player.split()
                le_jeu.is_playing = True
                

    if le_jeu.is_playing:
        
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(0, 0, 1000, 1000))
        fonctions_player()
    else:
        ecran_de_chargement()
    
    pygame.display.flip()
        