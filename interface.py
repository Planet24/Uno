from tkinter import *
import pygame
from coord import Coord
from couleurs import Couleurs

class Interface:
    """Gère l'interface du jeu."""
    def __init__(self):
        """Crée la fenêtre."""
        self.width = Coord.width
        self.length = Coord.length
        self.bgColor = Couleurs.WHITE
        self.screen = pygame.display.set_mode([self.width, self.length]).fill(self.bgColor)
        pygame.display.set_caption('Uno')
        # Noms des emplacements des cartes

    def affichePioche(self, pioche):
        """
        Affiche la pioche au centre à droite.
        Le dos de la carte est affiché si la pioche est non vide.
        """
        pygame.draw.rect(self.screen, Couleurs.RED,
                         [Coord.pioche_x, Coord.pioche_y,
                          Coord.pioche_width, Coord.pioche_length], 2)
        if len(pioche) != 0:
            self.screen.blit(Images.dos_carte,
                             (Coord.pioche_x + 5,
                              Coord.pioche_y + 5))

    def afficheMainJoueur(self, listeJoueurs, numCarteChoisie):
        """Affiche la main du joueur au sud de la fenêtre."""
        i = 0
        numCarte = 0
        for carte in listeJoueurs[0].main:
            if numCarte != numCarteChoisie:
                self.screen.blit(Images.dicoCartesImages[carte],
                                 (Coord.main_x + i, Coord.main_y))
            i += 110
            numCarte += 1

    def update(self, listeJoueurs, pioche, pot, numCarteChoisie, message,
               orientationJoueurQuiJoue, playMusic,
               bougeCarte=False, fini=False):

        """Met à jour la fenêtre."""
        self.screen.fill(self.bgColor)
        # Logo
        self.screen.blit(Images.logo,
                         (int(self.width / 2) - 163,
                          int(self.length / 2) - 110))
        if not fini:
            # Pioche
            self.affichePioche(pioche)
            # Pot
            self.afficheNoms(listeJoueurs, orientationJoueurQuiJoue)
            # Main actuelle
            self.afficheMainJoueur(listeJoueurs, numCarteChoisie)
            # Bottes

        if bougeCarte:
            # Affiche la carte sélectionnée à l'emplacement de la souris
            pos = pygame.mouse.get_pos()
            carte = listeJoueurs[0].main[numCarteChoisie]
            self.screen.blit(Images.dicoCartesImages[carte],(pos[0] - 50, pos[1] - 71))
        pygame.display.update()

while True :
    Interface()
    Interface.affiche_pioche()
    pygame.display.update()
