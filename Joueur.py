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

    def joue(main, pioche, pot):
        """Fais joueur le robot automatiquement."""
        listec = ["J", "B", "R", "V"]
        i = 0
        #Si attaqué par +2 ou +4
        if pot[-1] == "4+J":
            for i in main:
                if i == "J+":
                    pot.append(main.pop(main.index(i)))
                    return False
                elif i == "4+":
                    c = random.choice(listec)
                    pot.append(main.pop(main.index(i))+c)
                    return False
                else:
                    for _ in range(4):
                        main.append(pioche.pop(0))
                    pot.append("J")
                    return False
        if pot[-1] == "4+B":
            for i in main:
                if i == "B+":
                    pot.append(main.pop(main.index(i)))
                    return False
                elif i == "4+":
                    c = random.choice(listec)
                    pot.append(main.pop(main.index(i))+c)
                    return False
                else:
                    for _ in range(4):
                        main.append(pioche.pop(0))
                    pot.append("B")
                    return False
        if pot[-1] == "4+R":
            for i in main:
                if i == "R+":
                    pot.append(main.pop(main.index(i)))
                    return False
                elif i == "4+":
                    c = random.choice(listec)
                    pot.append(main.pop(main.index(i))+c)
                    return False
                else:
                    for _ in range(4):
                        main.append(pioche.pop(0))
                    pot.append("R")
                    return False
        if pot[-1] == "4+V":
            for i in main:
                if i == "V+":
                    pot.append(main.pop(main.index(i)))
                    return False
                elif i == "4+":
                    c = random.choice(listec)
                    pot.append(main.pop(main.index(i))+c)
                    return False
                else:
                    for _ in range(4):
                        main.append(pioche.pop(0))
                    pot.append("V")
                    return False

        if pot[-1] in Jeu.listeplus2:
            for i in main:
                if i in Jeu.listeplus2:
                    pot.append(main.pop(main.index(i)))
                    return False
                elif i == "4+":
                    c = random.choice(listec)
                    pot.append(main.pop(main.index(i)) + c)
                    return False
                else:
                    for _ in range(2):
                        main.append(pioche.pop(0))
                    pot.append(pot[-1][0])
                    return False

        if pot[-1] in Jeu.listeJaune:
            for i in main:
                if i in Jeu.listeJaune:
                    pot.append(main.pop(main.index(i)))
                    return False
        if pot[-1] in Jeu.listeBleu:
            for i in main:
                if i in Jeu.listeBleu:
                    pot.append(main.pop(main.index(i)))
                    return False
        if pot[-1] in Jeu.listeRouge:
            for i in main:
                if i in Jeu.listeRouge:
                    pot.append(main.pop(main.index(i)))
                    return False
        if pot[-1] in Jeu.listeVert:
            for i in main:
                if i in Jeu.listeVert:
                    pot.append(main.pop(main.index(i)))
                    return False

        if pot[-1] in Jeu.liste1:
            for i in main:
                if i in Jeu.liste1:
                    pot.append(main.pop(main.index(i)))
                    return False
        if pot[-1] in Jeu.liste2:
            for i in main:
                if i in Jeu.liste2:
                    pot.append(main.pop(main.index(i)))
                    return False
        if pot[-1] in Jeu.liste3:
            for i in main:
                if i in Jeu.liste3:
                    pot.append(main.pop(main.index(i)))
                    return False
        if pot[-1] in Jeu.liste4:
            for i in main:
                if i in Jeu.liste4:
                    pot.append(main.pop(main.index(i)))
                    return False
        if pot[-1] in Jeu.liste5:
            for i in main:
                if i in Jeu.liste5:
                    pot.append(main.pop(main.index(i)))
                    return False
        if pot[-1] in Jeu.liste6:
            for i in main:
                if i in Jeu.liste6:
                    pot.append(main.pop(main.index(i)))
                    return False
        if pot[-1] in Jeu.liste7:
            for i in main:
                if i in Jeu.liste7:
                    pot.append(main.pop(main.index(i)))
                    return False
        if pot[-1] in Jeu.liste8:
            for i in main:
                if i in Jeu.liste8:
                    pot.append(main.pop(main.index(i)))
                    return False
        if pot[-1] in Jeu.liste9:
            for i in main:
                if i in Jeu.liste9:
                    pot.append(main.pop(main.index(i)))
                    return False
        if pot[-1] in Jeu.listeReverse:
            for i in main:
                if i in Jeu.listeReverse:
                    pot.append(main.pop(main.index(i)))
                    return False
        if pot[-1] in Jeu.listeStop:
            for i in main:
                if i in Jeu.listeStop:
                    pot.append(main.pop(main.index(i)))
                    return False

        else:
            for i in main:
                if i in Jeu.listeNoir:
                    if i == "C":
                        c = random.choice(listec)
                        pot.append(c)
                        main.pop(0)
                        return False
                    elif i == "4+":
                        c = random.choice(listec)
                        pot.append(main.pop(0)+c)
                        return False
                else:
                    main.append(pioche.pop(0))
                    return False
        return "Erreur ordinateur n'a pas joué",False