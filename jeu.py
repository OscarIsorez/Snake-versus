import  pygame, snake

# TAILLE DE LA GRILLE DE JEU
GRILLE = 10

# Taille de la fenêtre
TAILLE = (720, 480)

# Fenetre du jeu
FENETRE = pygame.display.set_mode(TAILLE)

# Couleurs
NOIR = pygame.Color(0, 0, 0)
BLANC = pygame.Color(255, 255, 255)
VERT = pygame.Color(0, 255, 0)
ROUGE = pygame.Color(255, 0, 0)
BLEU = pygame.Color(0, 0, 255)
JAUNE = pygame.Color(227, 255, 51)
VIOLET = pygame.Color(217, 51, 255)
ORANGE = pygame.Color(255, 172, 51)

class Jeu:
    def __init__(self):
        self.pos01 = (36, 24)
        self.pos02 = (600, 300)

        #elements du serpents

        #noms à définir et CHANGEABLES
        self.noms01 = "Joueur01"
        self.noms02 = "Joueur02"

        #objets serpents
        self.serpent01 = snake.Serpent((36, 24), pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_DOWN, self.noms01)
        self.serpent02 = snake.Serpent((40, 30), pygame.K_z, pygame.K_d, pygame.K_q, pygame.K_s, self.noms02)
        self.is_playing = False
        self.couleur1 = VERT
        self.couleur2 = VIOLET

        #liste de tous les joueurs serpents
        self.listeserpent = [self.serpent01, self.serpent02]
    #afficher les dexu serpents
    def afficher_serpent(self, choix_serpent, choix_couleur):
        for i in choix_serpent.body[:-1]:
            pygame.draw.rect(FENETRE,choix_couleur, pygame.Rect(i[0] * GRILLE, i[1] * GRILLE, GRILLE, GRILLE))


    def afficher_pomme(self, pom):
        pygame.draw.rect(
            FENETRE, ROUGE, pygame.Rect(pom.pos[0] * GRILLE, pom.pos[1] * GRILLE, 10, 10))
    
    # def serpent_en_vie(self, serpent):
    #     return serpent.est_en_vie()



