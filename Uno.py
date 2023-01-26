from Joueur import Joueur
from Partie import Partie
from Jeu import Jeu
from interface import Interface
from couleurs import Couleurs
from cartes import Images
from coord import Coord
import pygame
indice = 0
nom = 'j'
#input("Votre nom : ")
#carteChoisie = 'J2'
run = True
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
    #robot joue
    Joueur.joue(partie.listeJoueurs[1].main, partie.pioche, partie.pot)
    print(partie.pot)
    fenetre.ResetCentre()
    fenetre.afficheCarteCentre(partie.pot)
    pygame.display.update()
    partie.finPioche(partie.pioche, partie.pot)
    #joueur joue
    run=fenetre.ClickSouris(run)
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
    fenetre.ResetCartes()
    partie.joueJoueurSud(partie.pioche, partie.pot, carteChoisie,indice)  # cartechoisie = click
    #print(carteChoisie)
    partie.finPioche(partie.pioche, partie.pot)
    pygame.display.update()
