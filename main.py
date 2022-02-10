#-------------------------------------------------------------------------------
# Name:        main.py
# Purpose:     Le module principal du jeu. Ce module est utilisé pour le lancer.
#
# Author:      PICHOFF Ewen, ISOREZ Oscar
#
# Created:     30/11/2021
#-------------------------------------------------------------------------------

#tous les imports

#import des bibliotheques de python
import pygame, sys, time, math, os,random 

#import des fichiers du jeu
import food
import jeu
import Bouton_diff

#init
pygame.init()

###                           ###
### On définis les constantes ###
###                           ###

# Images par Secondes, qui varient suivant la difficulté
fps = 15

# Couleurs
NOIR = pygame.Color(0, 0, 0)
BLANC = pygame.Color(255, 255, 255)
VERT = pygame.Color(0, 255, 0)
ROUGE = pygame.Color(255, 0, 0)
BLEU = pygame.Color(0, 0, 255)
JAUNE = pygame.Color(227, 255, 51)
VIOLET = pygame.Color(217, 51, 255)
ORANGE = pygame.Color(255, 172, 51)


# Nom de la Fenêtre
pygame.display.set_caption('Snake Versus')

# On crée une Clock
MONTRE = pygame.time.Clock()

# Taille de la fenêtre
TAILLE = (720, 480)

# Fenetre du jeu
FENETRE = pygame.display.set_mode(TAILLE)

#création de l'objet Bouton choix difficulté
Bouton_choix_difficulté= Bouton_diff.OptionBox(40, 5, 160, 40, (255, 255, 255), (255, 255, 230), pygame.font.SysFont(None, 30), 
    ["Facile", " Moyenne", " Extreme"])

#creation  objtets bouton choix couleur serpents
Bouton_choix_couleur1= Bouton_diff.OptionBox(520, 5, 160, 40, (255, 255, 255), (255, 255, 230), pygame.font.SysFont(None, 30), 
    ["VERT", " BLEU", " ORANGE"])
Bouton_choix_couleur2= Bouton_diff.OptionBox(520, 320, 160, 40, (255, 255, 255), (255, 255, 230), pygame.font.SysFont(None, 30), 
    ["VIOLET", " JAUNE", " BLANC"])


# Le jeu tourne
RUNNING = True


#apparation des pommes
spawnApple = False


###                             ###
### chargements de l'image du bouton ###
###                             ###

play_button_image = pygame.image.load(os.path.join("images","button.png"))
play_button = pygame.transform.scale(play_button_image,(400, 180))
play_button_rect =play_button.get_rect()
play_button_rect.x = math.ceil( FENETRE.get_width()-700)
play_button_rect.y =  math.ceil( FENETRE.get_height()/3)



###                       ###
###   Boucle Principale   ###
###                       ###

#création objet jeux, utile pour les serpents
jeux = jeu.Jeu()

#fonction pour démarrer
def demarrer():
    jeux.is_playing = True


def mouv_serpent(nom_serpent, haut, bas, droite, gauche):
    '''gestion des coordonnées des serpents en fonction des touches du clavier'''


    if nom_serpent.dy != 1:
        if event.key == haut:
            nom_serpent.dy = -1
            nom_serpent.dx = 0
    if nom_serpent.dx != -1:
        if event.key == bas:
            nom_serpent.dy = 0
            nom_serpent.dx = 1
            
    if nom_serpent.dx != 1:
        if event.key == gauche:
            nom_serpent.dy = 0
            nom_serpent.dx = -1
    if nom_serpent.dy != -1:
        if event.key == droite:
            nom_serpent.dy = 1
            nom_serpent.dx = 0



def game_over(qui):

    #fonction de fin de jeu appelée dès qu'il y a un vainqueur ou égalité
    
    if qui == "egalite":
        vainqueur = "égalité"
        couleur = ROUGE
    else:
        vainqueur = qui
        if qui == "Joueur01":
            couleur = jeux.couleur1
        else:
            couleur = jeux.couleur2
        

    my_font = pygame.font.SysFont('times new roman', 70)
    game_over_surface = my_font.render("Vainqueur : " + vainqueur, True, couleur)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (TAILLE[0]//2, TAILLE[1]//2-40)
    FENETRE.fill(pygame.Color(0, 0, 0))
    FENETRE.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

#permet d'afficher les noms de joueur sur l'écran
def afficher_noms(noms_serpent, coordonées):
    ma_font = pygame.font.SysFont('times new roman', 20)
    _surface = ma_font.render(noms_serpent+": ", True, pygame.Color(255,255, 255))
    _rect = _surface.get_rect()
    _rect.midtop = coordonées
    FENETRE.blit(_surface, _rect)
    pygame.display.flip()

def update_collisions(pomme, serpent, opposant=jeux.serpent02):

    '''détecter les collisions des serpents avec les murs, autres serpents, pommes...'''

    global spawnApple
    global fps

    ## Collisions avec les murs
    if serpent.pos[0] < 0:
        serpent.pos[0] = 72
    if serpent.pos[0] > 72:
        serpent.pos[0] = 0
    if serpent.pos[1] < 0:
        serpent.pos[1] = 48
    if serpent.pos[1] > 48:
        serpent.pos[1] = 0

    #test si un serpent mange une pomme
    if serpent.pos[0] == pomme.pos[0] and serpent.pos[1] == pomme.pos[1]:
        serpent.MANGER = True
        if random.randint(0, 10) == 5:
            fps += 1
        spawnApple = False

    #quand il y a égalite: que les deux serpents rentrent en meme temps en contact
    if serpent.body[0] == opposant.body[0]:
        serpent.vie = False
        opposant.vie = False
        game_over("egalite")


    #si le joueur se cogne contre lui meme, le repositionner en 900,900 (soit un coin aléatoire de la carte)
    for corps in serpent.body[1:-1]:
        if serpent.pos == corps:
            serpent.pos = [900,900]

    #test des collisions entre les serpents
    for corps in opposant.body[1:-1]:
        if serpent.pos == corps:
            serpent.vie = False
            #fin du jeu
            game_over(opposant.NOM)
    




def manger_pomme(serpent):

        '''gestion des pommes sur le terrain'''
        #si une pomme est mangée, le corps s'agrandit 

        if serpent.MANGER == False:
            serpent.body.insert(0, list(serpent.pos))
            serpent.body.pop()
        if serpent.MANGER:
            serpent.body.append(list(serpent.pos))
            serpent.MANGER = False



#boucle infini du jeu
while RUNNING:

    #gestion des evenements
    list_event = pygame.event.get()
    for event in list_event:
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.KEYDOWN:
            #deplacement des deux serpents
            mouv_serpent(jeux.serpent01,pygame.K_UP,pygame.K_RIGHT,pygame.K_DOWN,pygame.K_LEFT )
            mouv_serpent(jeux.serpent02,pygame.K_z,pygame.K_d,pygame.K_s, pygame.K_q)

    #choix de l'utilisateur sur la difficulté et ses couleurs de serpents    
    choix_option = Bouton_choix_difficulté.update(list_event)
    choix_couleur1 = Bouton_choix_couleur1.update(list_event)
    choix_couleur2 = Bouton_choix_couleur2.update(list_event)

    #raffraichit la fenetre en noir
    FENETRE.fill(pygame.Color(0, 0, 0))

    #choix de la difficulté pour changer la vitesse
    if choix_option>= 0:
        if choix_option == 0:
            fps = 15
            
        if choix_option == 1:
            fps = 20

        if choix_option == 2:
            fps = 25


    #tests choix des couleurs des serpents
    if choix_couleur1>= 0:
        if choix_couleur1 == 0:
            jeux.couleur1 = VERT
            
        if choix_couleur1 == 1:
            jeux.couleur1 = BLEU

        if choix_couleur1 == 2:
            jeux.couleur1 = ORANGE

    if choix_couleur2>= 0:
        if choix_couleur2 == 0:
            jeux.couleur2 = VIOLET
            
        if choix_couleur2 == 1:
            jeux.couleur2 = JAUNE

        if choix_couleur2 == 2:
            jeux.couleur2 = BLANC

    #changement d'état de spawnApple pour un bon fonctionnement 
    # et affichage de l'objet pomme 
    if jeux.is_playing:
        if spawnApple == False:
            spawnApple = True
            pom = food.Pomme()

        #actualisations
        update_collisions(pom, jeux.serpent01, jeux.serpent02)
        update_collisions(pom, jeux.serpent02, jeux.serpent01)
        jeux.serpent01.updatepos()
        jeux.serpent02.updatepos()

        #raffaraichit la fenetre 
        FENETRE.fill(pygame.Color(0, 0, 0))

        #affiche les joueurs 
        jeux.afficher_serpent(jeux.serpent01, jeux.couleur1)
        jeux.afficher_serpent(jeux.serpent02, jeux.couleur2)

        #fctn qui agrandit les serpents si ils mangent une pomme
        manger_pomme(jeux.serpent01)
        manger_pomme(jeux.serpent02)

        #affiche la pomme
        jeux.afficher_pomme(pom)


    if event.type == pygame.MOUSEBUTTONDOWN:
            
            if  jeux.is_playing == False:
                #verifer si souris en collision avec le bouton play
                if play_button_rect.collidepoint(event.pos):
                    #cacher le bouton et la bannière
                    #raffraichir l'écran
                    FENETRE.fill(pygame.Color(0, 0, 0))
                    #démarrer le jeu
                    demarrer()
                

    #verifie si notre jeu a commencé ou non
    if jeux.is_playing:
        pygame.display.update()
    else:
        #ajoute mon écran de bienvenu et les boutons sur la fenetre
        FENETRE.blit(play_button, play_button_rect)
        Bouton_choix_difficulté.dessiner(FENETRE)
        Bouton_choix_couleur1.dessiner(FENETRE)
        Bouton_choix_couleur2.dessiner(FENETRE)

        #appelle la fonction qui affiche les noms de joueur
        afficher_noms(jeux.serpent01.NOM,(450, 15))
        afficher_noms(jeux.serpent02.NOM,(450, 330))
        #actualise l'écran
        pygame.display.flip()

    #gestion des fps
    MONTRE.tick(fps)

#fin du jeu
pygame.quit()
