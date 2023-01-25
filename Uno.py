from Joueur import Joueur
from Partie import Partie
from Jeu import Jeu
from interface import Interface
from couleurs import Couleurs
from cartes import Images
from coord import Coord
import pygame

nom = 'j'
#input("Votre nom : ")
run = True
#carteChoisie = 'J2'
partie = Partie(nom)
indice = 0
print(partie.listeJoueurs[0].main)
print(partie.listeJoueurs[1].main)
print(partie.pot)
while run:
    pygame.init()
    fenetre = Interface()
    fenetre.affichePioche()
    fenetre.afficheCartePioche()
    fenetre.afficheCentre()
    fenetre.afficheEmplacementsCartes()
    fenetre.afficheCarteCentre(partie.pot)
    liste_cartes = partie.listeJoueurs[0].main
    listex=fenetre.AfficheMain(liste_cartes)
    fenetre.AfficheMainOrdi(partie.listeJoueurs[1].main)

    run=fenetre.ClickSouris(run)
    pos_x_J, pos_y_J, pos_x_P, pos_y_P = fenetre.TestClickSourisZone(listex)

    if pos_x_P == True and pos_y_P == True:
        carteChoisie = 'pioche'
    if pos_x_J == True and pos_y_J == True:
        print("le joueur place une carte")
        print(carteChoisie)
        print(liste_cartes[fenetre.indice_carte[0]]) #affiche la carte courante
        carteChoisie = liste_cartes[fenetre.indice_carte[0]]
        print(carteChoisie)


        indice = fenetre.indice_carte[0]
    fenetre.afficheCarteCentre(partie.pot)
    partie.joueJoueurSud(partie.pioche, partie.pot, carteChoisie,indice)  # cartechoisie = click
    pygame.display.update()
