from coord import Coord
from Jeu import Jeu
import random

class Joueur():
    """Crée un joueur de la partie."""
    def __init__(self, nom, orientation, points, pioche):
        """Initialise un joueur."""
        self.nom = nom
        self.orientation = orientation
        self.points = points
        self.main = []
        self.distribueJoueur(pioche)
        if orientation == 'sud':
            self.emplacements_x = 350
            self.emplacements_y = Coord.length - 310
            self.emplacements_width = 110 * 7
            self.emplacements_length = 150
            self.rotation = False
            self.coord_nom = (int(Coord.width / 2) - 50, Coord.length - 340)
        elif orientation == 'nord':
            self.emplacements_x = 350
            self.emplacements_y = 50
            self.emplacements_width = 110 * 7
            self.emplacements_length = 150
            self.rotation = False
            self.coord_nom = (int(Coord.width / 2) - 50, 220)
        else:
            print('Erreur : mauvaise orientation.')

    def trieMain(self):
        """
        Trie la main prise en paramètre en plaçant de gauche à droite
        les cartes jaunes, les cartes bleu, les cartes rouge, les cartes vert  puis les noires."""
        JauneMain, BleuMain, RougeMain, VertMain, NoirMain = [], [], [], [], []
        for carte in self.main:
            if carte in Jeu.listeJaune: # Si problème revoir jaune
                i = 0
                while len(JauneMain) > i:
                    i += 1
                JauneMain.insert(i, carte)
            elif carte in Jeu.listeBleu:
                if carte in BleuMain:
                    BleuMain.insert(BleuMain.index(carte), carte)
                else:
                    BleuMain.append(carte)
            elif carte in Jeu.listeRouge:
                if carte in RougeMain:
                    RougeMain.insert(RougeMain.index(carte), carte)
                else:
                    RougeMain.append(carte)
            elif carte in Jeu.listeRouge:
                if carte in VertMain:
                    VertMain.insert(VertMain.index(carte), carte)
                else:
                    VertMain.append(carte)
            elif carte in Jeu.listeNoir:
                NoirMain.append(carte)
        self.main = JauneMain + BleuMain + RougeMain + VertMain + NoirMain

    def distribueJoueur(self, pioche):
        """Distribue 7 cartes au joueur au début de la partie."""
        for _ in range(7):
            self.main.append(pioche.pop(0))
        self.trieMain()

    def joue(self, pioche, pot):
        """Fais joueur un joueur automatiquement."""
        listec = ['J', 'B', 'R', 'V']
        #Si attaqué par +2 ou +4
        if pot[-1] == "4+J":
            for i in self.main:
                if self.main[i] == "J+":
                    pot.append(self.main[i].pop(0))
                    return self.nom + " a posé" + pot[-1], False
                elif self.main[i] == "4+":
                    c = random.choice(listec)
                    pot.append(self.main[i].pop(0)+c)
                    return self.nom + " a posé" + pot[-1], False
                else:
                    for _ in range(4):
                        self.main.append(pioche.pop(0))
                        pot.append('J')
                    return self.nom + " a pioché 4 cartes", False
        elif pot[-1] == "4+B":
            for i in self.main:
                if self.main[i] == "B+":
                    pot.append(self.main[i].pop(0))
                    return self.nom + " a posé" + pot[-1], False
                elif self.main[i] == "4+":
                    c = random.choice(listec)
                    pot.append(self.main[i].pop(0)+c)
                    return self.nom + " a posé" + pot[-1], False
                else:
                    for _ in range(4):
                        self.main.append(pioche.pop(0))
                        pot.append('B')
                    return self.nom + " a pioché 4 cartes", False
        elif pot[-1] == "4+R":
            for i in self.main:
                if self.main[i] == "R+":
                    pot.append(self.main[i].pop(0))
                    return self.nom + " a posé" + pot[-1], False
                elif self.main[i] == "4+":
                    c = random.choice(listec)
                    pot.append(self.main[i].pop(0)+c)
                    return self.nom + " a posé" + pot[-1], False
                else:
                    for _ in range(4):
                        self.main.append(pioche.pop(0))
                        pot.append('R')
                    return self.nom + " a pioché 4 cartes", False
        elif pot[-1] == "4+V":
            for i in self.main:
                if self.main[i] == "V+":
                    pot.append(self.main[i].pop(0))
                    return self.nom + " a posé" + pot[-1], False
                elif self.main[i] == "4+":
                    c = random.choice(listec)
                    pot.append(self.main[i].pop(0)+c)
                    return self.nom + " a posé" + pot[-1], False
                else:
                    for _ in range(4):
                        self.main.append(pioche.pop(0))
                        pot.append('V')
                    return self.nom + " a pioché 4 cartes", False

        elif pot[-1] in Jeu.Listeplus2:
            for i in self.main:
                if self.main[i] in Jeu.Listeplus2:
                    pot.append(self.main[i].pop(0))
                    return self.nom + " a posé" + pot[-1], False
                elif self.main[i] == "4+":
                    c = random.choice(listec)
                    pot.append(self.main[i].pop(0) + c)
                    return self.nom + " a posé" + pot[-1], False
                else:
                    for _ in range(2):
                        self.main.append(pioche.pop(0))
                        pot.append(pot[-1][0])
                    return self.nom + " a pioché 2 cartes", False

        elif pot[-1] in Jeu.ListeJaune:
            for i in self.main:
                if self.main[i] in Jeu.ListeJaune:
                    pot.append(self.main[i].pop(0))
                    return self.nom + " a posé " + pot[-1], False
        elif pot[-1] in Jeu.ListeBleu:
            for i in self.main:
                if self.main[i] in Jeu.ListeBleu:
                    pot.append(self.main[i].pop(0))
                    return self.nom + " a posé " + pot[-1], False
        elif pot[-1] in Jeu.ListeRouge:
            for i in self.main:
                if self.main[i] in Jeu.ListeRouge:
                    pot.append(self.main[i].pop(0))
                    return self.nom + " a posé " + pot[-1], False
        elif pot[-1] in Jeu.ListeVert:
            for i in self.main:
                if self.main[i] in Jeu.ListeVert:
                    pot.append(self.main[i].pop(0))
                    return self.nom + " a posé " + pot[-1], False

        elif pot[-1] in Jeu.Liste1:
            for i in self.main:
                if self.main[i] in Jeu.Liste1:
                    pot.append(self.main[i].pop(0))
                    return self.nom + " a posé " + pot[-1], False
        elif pot[-1] in Jeu.Liste2:
            for i in self.main:
                if self.main[i] in Jeu.Liste2:
                    pot.append(self.main[i].pop(0))
                    return self.nom + " a posé " + pot[-1], False
        elif pot[-1] in Jeu.Liste3:
            for i in self.main:
                if self.main[i] in Jeu.Liste3:
                    pot.append(self.main[i].pop(0))
                    return self.nom + " a posé " + pot[-1], False
        elif pot[-1] in Jeu.Liste4:
            for i in self.main:
                if self.main[i] in Jeu.Liste4:
                    pot.append(self.main[i].pop(0))
                    return self.nom + " a posé " + pot[-1], False
        elif pot[-1] in Jeu.Liste5:
            for i in self.main:
                if self.main[i] in Jeu.Liste5:
                    pot.append(self.main[i].pop(0))
                    return self.nom + " a posé " + pot[-1], False
        elif pot[-1] in Jeu.Liste6:
            for i in self.main:
                if self.main[i] in Jeu.Liste6:
                    pot.append(self.main[i].pop(0))
                    return self.nom + " a posé " + pot[-1], False
        elif pot[-1] in Jeu.Liste7:
            for i in self.main:
                if self.main[i] in Jeu.Liste7:
                    pot.append(self.main[i].pop(0))
                    return self.nom + " a posé " + pot[-1], False
        elif pot[-1] in Jeu.Liste8:
            for i in self.main:
                if self.main[i] in Jeu.Liste8:
                    pot.append(self.main[i].pop(0))
                    return self.nom + " a posé " + pot[-1], False
        elif pot[-1] in Jeu.Liste9:
            for i in self.main:
                if self.main[i] in Jeu.Liste9:
                    pot.append(self.main[i].pop(0))
                    return self.nom + " a posé " + pot[-1], False

        else:
            for i in self.main:
                if self.main[i] in Jeu.ListeNoir:
                    if self.main[i] == 'C':
                        c = random.choice(listec)
                        pot.append(c)
                        self.main.pop(0)
                        return self.nom + " a posé "+ self.pot[-1], False
                    else:
                        c = random.choice(listec)
                        pot.append(self.main.pop(0)+c)
                        return self.nom + " a posé "+ self.pot[-1], False
                else:
                    self.main.append(pioche.pop(0))
        return "Erreur ordinateur n'a pas joué",False