import pygame

class OptionBox():

    def __init__(self, x, y, w, h, color, couleur_sulignée, font, liste_option, selected = 0):
        self.color = color
        self.couleur_sulignée = couleur_sulignée
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.liste_option = liste_option
        self.selected = selected
        self.dessiner_menu = False
        self.menu_active = False
        self.active_option = -1

    def dessiner(self, surf):
        pygame.draw.rect(surf, self.couleur_sulignée if self.menu_active else self.color, self.rect)
        pygame.draw.rect(surf, (0, 0, 0), self.rect, 2)
        msg = self.font.render(self.liste_option[self.selected], 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center = self.rect.center))

        if self.dessiner_menu:
            for i, text in enumerate(self.liste_option):
                rect = self.rect.copy()
                rect.y += (i+1) * self.rect.height
                pygame.draw.rect(surf, self.couleur_sulignée if i == self.active_option else self.color, rect)
                msg = self.font.render(text, 1, (0, 0, 0))
                surf.blit(msg, msg.get_rect(center = rect.center))
            outer_rect = (self.rect.x, self.rect.y + self.rect.height, self.rect.width, self.rect.height * len(self.liste_option))
            pygame.draw.rect(surf, (0, 0, 0), outer_rect, 2)

    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)
        
        self.active_option = -1
        for i in range(len(self.liste_option)):
            rect = self.rect.copy()
            rect.y += (i+1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.dessiner_menu = False

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.dessiner_menu = not self.dessiner_menu
                elif self.dessiner_menu and self.active_option >= 0:
                    self.selected = self.active_option
                    self.dessiner_menu = False
                    return self.active_option
        return -1
