from Joueur import Joueur
from Jeu import Jeu
from Partie import Partie
from interface import Interface
import time
import pygame
indice = 0
nom = 'j'
#input("Votre nom : ")
#carteChoisie = 'J2'
run = True
playO = True
playJ = True
i = 0
pygame.init()
fenetre = Interface()
partie = Partie(nom)
fenetre.affichePioche()
fenetre.afficheCentre()
fenetre.afficheCartePioche()
fenetre.afficheEmplacementsCartes()

while run:
    fenetre.ResetCentre()
    fenetre.afficheCarteCentre(partie.pot)
    liste_cartes = partie.listeJoueurs[0].main
    listex=fenetre.AfficheMain(liste_cartes)
    fenetre.AfficheMainOrdi(partie.listeJoueurs[1].main)
    pygame.display.update()
    time.sleep(1)
    if ((partie.pot[-1] in Jeu.listeStop) and (i == 0)):
        playO = False
        i = 1
    if playO == True:
        #robot joue
        Joueur.joue(partie.listeJoueurs[1].main, partie.pioche, partie.pot)
        i = 0
    playO = True
    fenetre.ResetCentre()
    fenetre.afficheCarteCentre(partie.pot)
    pygame.display.update()
    partie.finPioche(partie.pioche, partie.pot)
    #joueur joue
    run=fenetre.ClickSouris(run)
    if ((partie.pot[-1] in Jeu.listeStop) and (i == 0)):
        playJ = False
        i = 1
    if playJ == True:
        fenetre.pos = (0,0)
        while fenetre.pos == (0,0):
            fenetre.ClickSouris(run)
        pos_x_J, pos_y_J, pos_x_P, pos_y_P = fenetre.TestClickSourisZone(listex)
        if pos_x_P == True and pos_y_P == True:
            carteChoisie = "pioche"
        if pos_x_J == True and pos_y_J == True:
            carteChoisie = liste_cartes[fenetre.indice_carte[0]]
            indice = fenetre.indice_carte[0]
            #print(liste_cartes, indice)
        #fenetre.afficheCarteCentre(partie.pot)
        #fenetre.ResetCartes()
        partie.joueJoueurSud(partie.pioche, partie.pot, carteChoisie,indice)  # cartechoisie = click
        i = 0
    fenetre.ResetCartes()
    playJ = True
    #print(carteChoisie)
    partie.finPioche(partie.pioche, partie.pot)
