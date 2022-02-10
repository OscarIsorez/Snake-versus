

class Serpent:
    #constructeur
    def __init__(self, xy, HAUT, DROIT, GAUCHE ,BAS, NOM):
        #attributs
        self.vie = True
        self.x = xy[0]
        self.y = xy[1]
        self.dx = 1
        self.dy = 0
        self.body = [[self.x, self.y], [self.x-1, self.y], [self.x-2, self.y], [self.x-3, self.y], [self.x-4, self.y]]
        self.pos = [self.x, self.y]
        self.HAUT, self.DROIT, self.GAUCHE , self.BAS = HAUT, DROIT, GAUCHE ,BAS
        self.score = 0
        self.MANGER = False
        self.NOM = NOM

    #METHODES

    def est_en_vie(self):
        return self.vie

    #actualise les positions de serpent
    def updatepos(self):
        if self.dy == 1:
            self.pos[1] += 1
        if self.dy == -1:
            self.pos[1] -= 1
        if self.dx == -1:
            self.pos[0] -= 1
        if self.dx == 1:
            self.pos[0] += 1
