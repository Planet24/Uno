from Joueur import Joueur
from Jeu import Jeu
from random import shuffle
from operator import index
import random

class Partie:
    """Gère une partie."""
    def __init__(self, nom):
        """Initialise une partie."""
        # Préparation de la pioche
        i = 0
        self.pioche = []
        self.pioche.extend(Jeu.listeJaune[1:])
        self.pioche.extend(Jeu.listeJaune[2:])
        self.pioche.extend(Jeu.listeBleu[1:])
        self.pioche.extend(Jeu.listeBleu[2:])
        self.pioche.extend(Jeu.listeRouge[1:])
        self.pioche.extend(Jeu.listeRouge[2:])
        self.pioche.extend(Jeu.listeVert[1:])
        self.pioche.extend(Jeu.listeVert[2:])
        for i in range(6):
            self.pioche.append("J+")
            self.pioche.append("JS")
            self.pioche.append("JR")
            self.pioche.append("B+")
            self.pioche.append("BS")
            self.pioche.append("BR")
            self.pioche.append("R+")
            self.pioche.append("RS")
            self.pioche.append("RR")
            self.pioche.append("V+")
            self.pioche.append("VS")
            self.pioche.append("VR")
        self.pioche.extend(Jeu.listeNoir[0:]*4)
        shuffle(self.pioche)
        self.pot = [self.pioche.pop(0)]
        self.listeJoueurs = self.creationJoueurs(nom)

    def creationJoueurs(self, nom):
        """Crée les 2 joueurs et les placés dans une liste."""
        listeNoms = [nom,"Nord"]
        listeOrientations = ["sud", "nord"]
        liste = []
        for i in range(2):
            liste.append(Joueur(listeNoms[i],listeOrientations[i],self.pioche))
        return liste

    def joueJoueurSud(self, pioche, pot, carteChoisie, indice): #cartechoisie = click
        """
        Fait jouer le joueur sud (humain) en fonction de la carte et de
        l"endroit choisi.
        """
        listec = ["J", "B", "R", "V"]
        if carteChoisie == "pioche": #piocher une carte
            # pose une carte
            self.listeJoueurs[0].main.append(pioche.pop(0))
            return "".join([self.listeJoueurs[0].nom," a pioché une carte."])
        # Si attaqué par +2 ou +4
        if pot[-1] == "4+J":
            if carteChoisie == "J+":
                pot.append(self.listeJoueurs[0].main.pop(indice))
                return False
            elif carteChoisie == "4+":
                c = random.choice(listec)
                pot.append(self.listeJoueurs[0].main.pop(indice) + c)
                return False
            else:
                for _ in range(4):
                    self.listeJoueurs[0].main.append(pioche.pop(0))
                pot.append("J")
                return False
        if pot[-1] == "4+B":
            if carteChoisie == "B+":
                pot.append(self.listeJoueurs[0].main.pop(indice))
                return False
            elif carteChoisie == "4+":
                c = random.choice(listec)
                pot.append(self.listeJoueurs[0].main.pop(indice) + c)
                return False
            else:
                for _ in range(4):
                    self.listeJoueurs[0].main.append(pioche.pop(0))
                pot.append("B")
                return False
        if pot[-1] == "4+R":
            if carteChoisie == "R+":
                pot.append(self.listeJoueurs[0].main.pop(indice))
                return False
            elif carteChoisie == "4+":
                c = random.choice(listec)
                pot.append(self.listeJoueurs[0].main.pop(indice) + c)
                return False
            else:
                for _ in range(4):
                    self.listeJoueurs[0].main.append(pioche.pop(0))
                pot.append("R")
                return False
        if pot[-1] == "4+V":
            if carteChoisie == "V+":
                pot.append(self.listeJoueurs[0].main.pop(indice))
                return False
            elif carteChoisie == "4+":
                c = random.choice(listec)
                pot.append(self.listeJoueurs[0].main.pop(indice) + c)
                return False
            else:
                for _ in range(4):
                    self.listeJoueurs[0].main.append(pioche.pop(0))
                pot.append("V")
                return False

        if pot[-1] in Jeu.listeplus2:
            if carteChoisie in Jeu.listeplus2:
                pot.append(self.listeJoueurs[0].main.pop(indice))
                return False
            elif carteChoisie == "4+":
                c = random.choice(listec)
                pot.append(self.listeJoueurs[0].main.pop(indice) + c)
                return False
            else:
                for _ in range(2):
                    self.listeJoueurs[0].main.append(pioche.pop(0))
                pot.append(pot[-1][0])
                return False

        if pot[-1] in Jeu.listeJaune:
            if carteChoisie in Jeu.listeJaune:
                pot.append(self.listeJoueurs[0].main.pop(indice))
                return False
        if pot[-1] in Jeu.listeBleu:
            if carteChoisie in Jeu.listeBleu:
                pot.append(self.listeJoueurs[0].main.pop(indice))
                return False
        if pot[-1] in Jeu.listeRouge:
            if carteChoisie in Jeu.listeRouge:
                pot.append(self.listeJoueurs[0].main.pop(indice))
                return False
        if pot[-1] in Jeu.listeVert:
            if carteChoisie in Jeu.listeVert:
                pot.append(self.listeJoueurs[0].main.pop(indice))
                return False

        if pot[-1] in Jeu.liste1:
            if carteChoisie in Jeu.liste1:
                pot.append(self.listeJoueurs[0].main.pop(indice))
                return False
        if pot[-1] in Jeu.liste2:
            if carteChoisie in Jeu.liste2:
                pot.append(self.listeJoueurs[0].main.pop(indice))
                return False
        if pot[-1] in Jeu.liste3:
            if carteChoisie in Jeu.liste3:
                pot.append(self.listeJoueurs[0].main.pop(indice))
                return False
        if pot[-1] in Jeu.liste4:
            if carteChoisie in Jeu.liste4:
                pot.append(self.listeJoueurs[0].main.pop(indice))
                return False
        if pot[-1] in Jeu.liste5:
            if carteChoisie in Jeu.liste5:
                pot.append(self.listeJoueurs[0].main.pop(indice))
                return False
        if pot[-1] in Jeu.liste6:
            if carteChoisie in Jeu.liste6:
                pot.append(self.listeJoueurs[0].main.pop(indice))
                return False
        if pot[-1] in Jeu.liste7:
            if carteChoisie in Jeu.liste7:
                pot.append(self.listeJoueurs[0].main.pop(indice))
                return False
        if pot[-1] in Jeu.liste8:
            if carteChoisie in Jeu.liste8:
                pot.append(self.listeJoueurs[0].main.pop(indice))
                return False
        if pot[-1] in Jeu.liste9:
                if carteChoisie in Jeu.liste9:
                    pot.append(self.listeJoueurs[0].main.pop(indice))
                    return False

        if carteChoisie == "C":
            c = random.choice(listec)
            pot.append(c)
            self.listeJoueurs[0].main.pop(indice)
            return False
        if carteChoisie == "4+":
            c = random.choice(listec)
            pot.append(self.listeJoueurs[0].main.pop(indice) + c)
            return False

        return "Erreur joueur n'a pas joué", False