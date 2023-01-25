from coord import Coord
from Jeu import Jeu
import random

class Joueur():
    """Crée un joueur de la partie."""
    def __init__(self, nom, orientation, pioche):
        """Initialise un joueur."""
        self.nom = nom
        self.orientation = orientation
        self.main = []
        self.distribueJoueur(pioche)

    def distribueJoueur(self, pioche):
        """Distribue 7 cartes au joueur au début de la partie."""
        for _ in range(7):
            self.main.append(pioche.pop(0))
            print(self.main)

    def joue(self, pioche, pot):
        """Fais joueur un joueur automatiquement."""
        listec = ["J", "B", "R", "V"]
        #Si attaqué par +2 ou +4
        if pot[-1] == "4+J":
            for i in self.main:
                if self.main[i] == "J+":
                    pot.append(self.main.pop(i))
                    return False
                elif self.main[i] == "4+":
                    c = random.choice(listec)
                    pot.append(self.main.pop(i)+c)
                    return False
                else:
                    for _ in range(4):
                        self.main.append(pioche.pop(0))
                    pot.append("J")
                    return False
        if pot[-1] == "4+B":
            for i in self.main:
                if self.main[i] == "B+":
                    pot.append(self.main.pop(i))
                    return False
                elif self.main[i] == "4+":
                    c = random.choice(listec)
                    pot.append(self.main.pop(i)+c)
                    return False
                else:
                    for _ in range(4):
                        self.main.append(pioche.pop(0))
                    pot.append("B")
                    return False
        if pot[-1] == "4+R":
            for i in self.main:
                if self.main[i] == "R+":
                    pot.append(self.main.pop(i))
                    return False
                elif self.main[i] == "4+":
                    c = random.choice(listec)
                    pot.append(self.main.pop(i)+c)
                    return False
                else:
                    for _ in range(4):
                        self.main.append(pioche.pop(0))
                    pot.append("R")
                    return False
        if pot[-1] == "4+V":
            for i in self.main:
                if self.main[i] == "V+":
                    pot.append(self.main.pop(i))
                    return False
                elif self.main[i] == "4+":
                    c = random.choice(listec)
                    pot.append(self.main.pop(i)+c)
                    return False
                else:
                    for _ in range(4):
                        self.main.append(pioche.pop(0))
                    pot.append("V")
                    return False

        if pot[-1] in Jeu.listeplus2:
            for i in self.main:
                if self.main[i] in Jeu.listeplus2:
                    pot.append(self.main.pop(i))
                    return False
                elif self.main[i] == "4+":
                    c = random.choice(listec)
                    pot.append(self.main.pop(i) + c)
                    return False
                else:
                    for _ in range(2):
                        self.main.append(pioche.pop(0))
                    pot.append(pot[-1][0])
                    return False

        if pot[-1] in Jeu.listeJaune:
            for i in self.main:
                if self.main[i] in Jeu.listeJaune:
                    pot.append(self.main.pop(i))
                    return False
        if pot[-1] in Jeu.listeBleu:
            for i in self.main:
                if self.main[i] in Jeu.listeBleu:
                    pot.append(self.main.pop(i))
                    return False
        if pot[-1] in Jeu.listeRouge:
            for i in self.main:
                if self.main[i] in Jeu.listeRouge:
                    pot.append(self.main.pop(i))
                    return False
        if pot[-1] in Jeu.listeVert:
            for i in self.main:
                if self.main[i] in Jeu.listeVert:
                    pot.append(self.main.pop(i))
                    return False

        if pot[-1] in Jeu.liste1:
            for i in self.main:
                if self.main[i] in Jeu.liste1:
                    pot.append(self.main.pop(i))
                    return False
        if pot[-1] in Jeu.liste2:
            for i in self.main:
                if self.main[i] in Jeu.liste2:
                    pot.append(self.main.pop(i))
                    return False
        if pot[-1] in Jeu.liste3:
            for i in self.main:
                if self.main[i] in Jeu.liste3:
                    pot.append(self.main.pop(i))
                    return False
        if pot[-1] in Jeu.liste4:
            for i in self.main:
                if self.main[i] in Jeu.liste4:
                    pot.append(self.main.pop(i))
                    return False
        if pot[-1] in Jeu.liste5:
            for i in self.main:
                if self.main[i] in Jeu.liste5:
                    pot.append(self.main.pop(i))
                    return False
        if pot[-1] in Jeu.liste6:
            for i in self.main:
                if self.main[i] in Jeu.liste6:
                    pot.append(self.main.pop(i))
                    return False
        if pot[-1] in Jeu.liste7:
            for i in self.main:
                if self.main[i] in Jeu.liste7:
                    pot.append(self.main.pop(i))
                    return False
        if pot[-1] in Jeu.liste8:
            for i in self.main:
                if self.main[i] in Jeu.liste8:
                    pot.append(self.main.pop(i))
                    return False
        if pot[-1] in Jeu.liste9:
            for i in self.main:
                if self.main[i] in Jeu.liste9:
                    pot.append(self.main.pop(i))
                    return False

        else:
            for i in self.main:
                if self.main[i] in Jeu.listeNoir:
                    if self.main[i] == "C":
                        c = random.choice(listec)
                        pot.append(c)
                        self.main.pop(0)
                        return False
                    else:
                        c = random.choice(listec)
                        pot.append(self.main.pop(0)+c)
                        return False
                else:
                    self.main.append(pioche.pop(0))
                    return False
        return "Erreur ordinateur n'a pas joué",False