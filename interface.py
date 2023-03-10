from tkinter import *
import pygame
from coord import Coord
from couleurs import Couleurs
from cartes import Images
import time
class Interface:
    """Gère l'interface du jeu."""
    def __init__(self):
        """Crée la fenêtre."""
        self.width = Coord.width
        self.length = Coord.length
        self.bgColor = Couleurs.WHITE
        self.indice_carte=[0]
        self.pos = (0,0)
        self.myfont = pygame.font.SysFont('impact', 150)
        self.screen = pygame.display.set_mode([self.width, self.length])
        self.screen.fill(self.bgColor)
        pygame.display.set_caption('Uno')

    def AfficheFond(self):
        fond = Images.dicoCartesImages['Fond']
        fond = fond.convert()
        self.screen.blit(fond, (0, 0))
        pygame.display.flip()

    def affichePioche(self):
        """
        Affiche la pioche au centre à droite.
        Le dos de la carte est affiché si la pioche est non vide.
        """
        pygame.draw.rect(self.screen, Couleurs.RED,
                         [Coord.pioche_x-220, Coord.pioche_y,
                          Coord.pioche_width, Coord.pioche_length], 2)

    def afficheCentre(self):
        """
        Affiche la pioche au centre à droite.
        Le dos de la carte est affiché si la pioche est non vide.
        """
        pygame.draw.rect(self.screen, Couleurs.BLUE,
                         [Coord.pioche_x, Coord.pioche_y,
                          Coord.pioche_width, Coord.pioche_length], 2)
    def afficheCarteCentre(self, pot):
        self.screen.blit(Images.dicoCartesImages[pot[-1]],
                         (Coord.pioche_x, Coord.pioche_y))

    def afficheCartePioche(self):
        self.screen.blit(Images.dicoCartesImages['D'],
                         (Coord.pioche_x-220, Coord.pioche_y))

    def ResetCartes(self):
        """
        Affiche les emplacements où les joueurs posent les cartes,
        ainsi que la carte du dessus sur chaque emplacement.
        """
        pygame.draw.rect(self.screen, Couleurs.WHITE, (200, 50, 1300, 150))
        pygame.draw.rect(self.screen, Couleurs.WHITE, (200, 500, 1300, 150))
    def ResetCentre(self):
        """
        Affiche la pioche au centre à droite.
        Le dos de la carte est affiché si la pioche est non vide.
        """
        pygame.draw.rect(self.screen, Couleurs.BLUE,
                         [Coord.pioche_x, Coord.pioche_y,
                          Coord.pioche_width, Coord.pioche_length])
    def afficheEmplacementsCartes(self):
        """
        Affiche les emplacements où les joueurs posent les cartes,
        ainsi que la carte du dessus sur chaque emplacement.
        """
        pygame.draw.rect(self.screen, Couleurs.RED, (200, 50, 1100, 150), 2)
        pygame.draw.rect(self.screen, Couleurs.RED,(200,500,1100,150), 2)
    def ClickSouris(self,run):
        ev = pygame.event.get()
        for event in ev:
            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                exit()
        return run
    def TestClickSourisZone(self,listex):
        pos_y_J = False
        pos_x_J= False
        pos_y_P = False
        pos_x_P = False
        n = len(listex)
        i=0

        if self.pos[1]<=650 and self.pos[1]>=500:
            pos_y_J = True
        if pos_y_J == True:
            while i < n:
                if i == n-1:
                    if self.pos[0] > listex[i]:
                        pos_x_J = True
                        self.indice_carte[0] =i
                        break
                elif self.pos[0]<  listex[i+1] and self.pos[0] > listex[i]:
                    pos_x_J = True
                    self.indice_carte[0] = i
                    break

                i+=1
        if self.pos[1] >= Coord.pioche_y and self.pos[1] <= Coord.pioche_y + 150  :
            pos_y_P = True
            if self.pos[0] < Coord.pioche_x - 110 and self.pos[0] > Coord.pioche_x -220:
                pos_x_P = True


        return pos_x_J,pos_y_J,pos_x_P,pos_y_P


    def AfficheMain(self, liste_cartes):
        #la main peut contenir jusqu'a 50 cartes
        N = len(liste_cartes)
        listex = []
        if N ==0:
            #pygame.draw.rect(self.screen, Couleurs.WHITE, (200, 50, 1100, 150))
            textsurface = self.myfont.render('Tu as gagné !!!', 1, Couleurs.WHITE)
            self.screen.blit(textsurface, (0, 0))
            pygame.display.update()
            time.sleep(10)
            exit()
        else :
            espace = 1100 / N
            emplacement= 200
            i=0
            for cartes in liste_cartes:
                self.screen.blit(Images.dicoCartesImages[cartes],
                                 (emplacement +espace*i, 500))
                listex.append(emplacement +espace*i)
                i+=1
        return listex


    def AfficheMainOrdi(self, liste_cartes):
        #la main peut contenir jusqu'a 20 cartes
        N = len(liste_cartes)
        if N ==0:
            #pygame.draw.rect(self.screen, Couleurs.WHITE, (200, 500, 1100, 150))
            textsurface = self.myfont.render("Tu as perdu...", 1, Couleurs.WHITE)
            self.screen.blit(textsurface, (0, 0))
            pygame.display.update()
            time.sleep(10)
            exit()
        else :
            espace = 1100 / N
            emplacement= 200
            i=0
            while i < N:
                self.screen.blit(Images.dicoCartesImages['D'],
                                 (emplacement +espace*i, 50))
                i+=1

